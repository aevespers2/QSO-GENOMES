#!/usr/bin/env python3
"""Fail-closed validation for the declarative Aequitas review binding."""

from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
from typing import Any

EXPECTED_GENOME_IDS = ("atlas", "lyra", "nova", "orion")
EXPECTED_REVIEW_SURFACE_IDS = (
    "input",
    "interpretation",
    "ontology",
    "proposed_edit",
    "communication",
)
EXPECTED_INVARIANTS = {
    "sprite_human_review_required",
    "sprite_may_annotate",
    "sprite_may_block_pending_review",
    "sprite_may_modify_genome",
    "sprite_may_execute",
    "sprite_may_write_repository",
    "sprite_may_override_immutable_ethics",
    "genomes_require_external_commit",
    "genomes_require_hash",
    "genomes_rollback_on_violation",
    "genomes_may_change_purpose",
    "genomes_may_change_immutable",
}


class BindingValidationError(ValueError):
    """Raised when the Aequitas binding is ambiguous, stale, or inconsistent."""


def _reject_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise BindingValidationError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_non_finite(value: str) -> None:
    raise BindingValidationError(f"non-finite JSON number: {value}")


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_pairs,
            parse_constant=_reject_non_finite,
        )
    except (OSError, json.JSONDecodeError) as exc:
        raise BindingValidationError(f"cannot load {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise BindingValidationError(f"top-level JSON value must be an object: {path}")
    return value


def _canonical_reference_path(root: Path, relative: Any, expected: str) -> Path:
    if not isinstance(relative, str) or not relative:
        raise BindingValidationError("reference path must be a non-empty string")
    if "\\" in relative:
        raise BindingValidationError(f"path is not canonical POSIX form: {relative}")
    pure = PurePosixPath(relative)
    if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
        raise BindingValidationError(f"path is not canonical repository-relative form: {relative}")
    if pure.as_posix() != relative or relative != expected:
        raise BindingValidationError(
            f"path-inconsistent reference: expected {expected}, found {relative}"
        )
    candidate = (root / relative).resolve()
    resolved_root = root.resolve()
    if candidate != resolved_root and resolved_root not in candidate.parents:
        raise BindingValidationError(f"reference escapes repository root: {relative}")
    if not candidate.is_file():
        raise BindingValidationError(f"stale or missing reference: {relative}")
    return candidate


def _require_bool(mapping: dict[str, Any], key: str) -> bool:
    value = mapping.get(key)
    if type(value) is not bool:
        raise BindingValidationError(f"invariant {key} must be boolean")
    return value


def _validate_review_surfaces(binding: dict[str, Any], sprite: dict[str, Any]) -> None:
    activation_rules = binding.get("activation_rules")
    if not isinstance(activation_rules, dict):
        raise BindingValidationError("activation_rules must be an object")
    review_surfaces = activation_rules.get("review_surfaces")
    if not isinstance(review_surfaces, list):
        raise BindingValidationError("activation_rules.review_surfaces must be an array")

    sprite_oversight = sprite.get("oversight")
    if not isinstance(sprite_oversight, dict):
        raise BindingValidationError("sprite oversight must be an object")
    enabled_oversight: set[str] = set()
    for oversight_id, enabled in sprite_oversight.items():
        if not isinstance(oversight_id, str) or not oversight_id:
            raise BindingValidationError("sprite oversight identifiers must be non-empty strings")
        if type(enabled) is not bool:
            raise BindingValidationError(
                f"sprite oversight definition must be boolean: {oversight_id}"
            )
        if enabled:
            enabled_oversight.add(oversight_id)

    seen_surfaces: dict[str, tuple[str, ...]] = {}
    referenced_oversight: list[str] = []
    for index, review_surface in enumerate(review_surfaces):
        if not isinstance(review_surface, dict):
            raise BindingValidationError(f"review surface {index} must be an object")
        surface_id = review_surface.get("surface")
        if not isinstance(surface_id, str) or not surface_id:
            raise BindingValidationError(f"review surface {index} has invalid surface")
        required_oversight = review_surface.get("required_oversight")
        if not isinstance(required_oversight, list) or not required_oversight:
            raise BindingValidationError(
                f"review surface {surface_id} required_oversight must be a non-empty array"
            )

        seen_required: set[str] = set()
        normalized_required: list[str] = []
        for oversight_index, oversight_id in enumerate(required_oversight):
            if not isinstance(oversight_id, str) or not oversight_id:
                raise BindingValidationError(
                    f"review surface {surface_id} oversight {oversight_index} must be a non-empty string"
                )
            if oversight_id in seen_required:
                raise BindingValidationError(
                    "duplicate oversight definition before de-duplication: "
                    f"{surface_id}.{oversight_id}"
                )
            seen_required.add(oversight_id)
            if oversight_id not in sprite_oversight:
                raise BindingValidationError(
                    f"unknown oversight definition for review surface {surface_id}: {oversight_id}"
                )
            if sprite_oversight[oversight_id] is not True:
                raise BindingValidationError(
                    "required oversight conflicts with sprite source: "
                    f"{surface_id}.{oversight_id}"
                )
            normalized_required.append(oversight_id)

        normalized_tuple = tuple(normalized_required)
        if surface_id in seen_surfaces:
            if seen_surfaces[surface_id] != normalized_tuple:
                raise BindingValidationError(
                    "conflicting oversight definitions for duplicate review surface "
                    f"before de-duplication: {surface_id}"
                )
            raise BindingValidationError(
                f"duplicate review surface before de-duplication: {surface_id}"
            )
        seen_surfaces[surface_id] = normalized_tuple
        referenced_oversight.extend(normalized_required)

    expected_surfaces = set(EXPECTED_REVIEW_SURFACE_IDS)
    actual_surfaces = set(seen_surfaces)
    if actual_surfaces != expected_surfaces:
        raise BindingValidationError(
            "review surface set mismatch: "
            f"missing={sorted(expected_surfaces - actual_surfaces)}, "
            f"unexpected={sorted(actual_surfaces - expected_surfaces)}"
        )

    referenced_set = set(referenced_oversight)
    if referenced_set != enabled_oversight:
        raise BindingValidationError(
            "review surface oversight coverage mismatch: "
            f"missing={sorted(enabled_oversight - referenced_set)}, "
            f"unexpected={sorted(referenced_set - enabled_oversight)}"
        )


def validate_binding(root: Path, binding_relative: str = "contracts/aequitas-review-binding.json") -> None:
    root = root.resolve()
    binding_path = _canonical_reference_path(root, binding_relative, binding_relative)
    binding = load_json(binding_path)

    sprite_ref = binding.get("sprite_reference")
    if not isinstance(sprite_ref, dict):
        raise BindingValidationError("sprite_reference must be an object")
    sprite_id = sprite_ref.get("sprite_id")
    if not isinstance(sprite_id, str) or not sprite_id:
        raise BindingValidationError("sprite_reference.sprite_id must be a non-empty string")
    sprite_path = _canonical_reference_path(
        root, sprite_ref.get("path"), f"sprites/{sprite_id}.json"
    )
    schema_path = _canonical_reference_path(
        root, sprite_ref.get("schema_path"), "schema/qso-sprite.schema.json"
    )
    sprite = load_json(sprite_path)
    schema = load_json(schema_path)
    if sprite.get("sprite_id") != sprite_id:
        raise BindingValidationError(
            f"stale sprite reference: {sprite_id} != {sprite.get('sprite_id')}"
        )
    schema_version = sprite_ref.get("schema_version")
    if sprite.get("schema_version") != schema_version:
        raise BindingValidationError("stale sprite schema_version reference")
    try:
        schema_const = schema["properties"]["schema_version"]["const"]
    except (KeyError, TypeError) as exc:
        raise BindingValidationError("sprite schema lacks schema_version const") from exc
    if schema_const != schema_version:
        raise BindingValidationError("stale sprite schema path or version")

    _validate_review_surfaces(binding, sprite)

    references = binding.get("genome_references")
    if not isinstance(references, list):
        raise BindingValidationError("genome_references must be an array")
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    genomes: list[dict[str, Any]] = []
    for index, reference in enumerate(references):
        if not isinstance(reference, dict):
            raise BindingValidationError(f"genome reference {index} must be an object")
        genome_id = reference.get("genome_id")
        path = reference.get("path")
        if not isinstance(genome_id, str) or not genome_id:
            raise BindingValidationError(f"genome reference {index} has invalid genome_id")
        if genome_id in seen_ids:
            raise BindingValidationError(f"duplicate genome_id before de-duplication: {genome_id}")
        if not isinstance(path, str) or not path:
            raise BindingValidationError(f"genome reference {index} has invalid path")
        if path in seen_paths:
            raise BindingValidationError(f"duplicate genome path before de-duplication: {path}")
        seen_ids.add(genome_id)
        seen_paths.add(path)
        genome_path = _canonical_reference_path(root, path, f"genomes/{genome_id}.json")
        genome = load_json(genome_path)
        if genome.get("genome_id") != genome_id:
            raise BindingValidationError(
                f"stale genome reference: {genome_id} != {genome.get('genome_id')}"
            )
        genomes.append(genome)

    expected_ids = set(EXPECTED_GENOME_IDS)
    if seen_ids != expected_ids:
        missing = sorted(expected_ids - seen_ids)
        unexpected = sorted(seen_ids - expected_ids)
        raise BindingValidationError(
            f"genome reference set mismatch: missing={missing}, unexpected={unexpected}"
        )

    invariants = binding.get("invariants")
    if not isinstance(invariants, dict):
        raise BindingValidationError("invariants must be an object")
    actual_keys = set(invariants)
    if actual_keys != EXPECTED_INVARIANTS:
        raise BindingValidationError(
            "invariant key set mismatch: "
            f"missing={sorted(EXPECTED_INVARIANTS - actual_keys)}, "
            f"unexpected={sorted(actual_keys - EXPECTED_INVARIANTS)}"
        )

    sprite_values = {
        "sprite_human_review_required": sprite["ethics"]["human_review_required"],
        "sprite_may_annotate": sprite["authority"]["may_annotate"],
        "sprite_may_block_pending_review": sprite["authority"]["may_block_pending_review"],
        "sprite_may_modify_genome": sprite["authority"]["may_modify_genome"],
        "sprite_may_execute": sprite["authority"]["may_execute"],
        "sprite_may_write_repository": sprite["authority"]["may_write_repository"],
        "sprite_may_override_immutable_ethics": sprite["authority"]["may_override_immutable_ethics"],
    }
    genome_values = {
        "genomes_require_external_commit": [g["freeze"]["external_commit_only"] for g in genomes],
        "genomes_require_hash": [g["freeze"]["require_hash"] for g in genomes],
        "genomes_rollback_on_violation": [g["freeze"]["rollback_on_violation"] for g in genomes],
        "genomes_may_change_purpose": [
            g["learning"]["goal_evolution"]["may_change_purpose"] for g in genomes
        ],
        "genomes_may_change_immutable": [
            g["learning"]["goal_evolution"]["may_change_immutable"] for g in genomes
        ],
    }
    for key, actual in sprite_values.items():
        if _require_bool(invariants, key) is not actual:
            raise BindingValidationError(f"published invariant disagrees with sprite source: {key}")
    for key, values in genome_values.items():
        published = _require_bool(invariants, key)
        if any(type(value) is not bool or value is not published for value in values):
            raise BindingValidationError(f"published invariant disagrees with genome sources: {key}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        validate_binding(args.root)
    except BindingValidationError as exc:
        print(f"FAIL: {exc}")
        return 1
    print(
        "PASS: Aequitas references, review surfaces, oversight definitions, "
        "and invariants are unique, canonical, and source-consistent"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
