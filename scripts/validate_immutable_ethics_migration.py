#!/usr/bin/env python3
"""Fail-closed validation for the immutable-ethics migration contract."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
from typing import Any

EXPECTED_GENOME_PATHS = (
    "genomes/atlas.json",
    "genomes/lyra.json",
    "genomes/nova.json",
    "genomes/orion.json",
)
EXPECTED_PROTOCOL_PATH = "protocols/immutable-ethics-v1.json"
EXPECTED_REQUIRED_SECTIONS = {
    "principles",
    "decision_order",
    "conflict_rule",
    "amendment_rule",
}
REQUIRED_TRUE_CONSUMER_FLAGS = {
    "validate_before_genome_use",
    "require_exact_path",
    "require_exact_protocol_id",
    "require_exact_status",
    "require_exact_canonical_hash",
    "retain_principles_verbatim",
    "retain_decision_order_verbatim",
    "retain_conflict_rule_verbatim",
    "retain_amendment_rule_verbatim",
    "human_review_required",
    "new_protocol_id_required_for_change",
    "new_migration_version_required_for_change",
}


class MigrationValidationError(ValueError):
    """Raised when the migration or its bound sources fail closed."""


def _reject_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise MigrationValidationError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_non_finite(value: str) -> None:
    raise MigrationValidationError(f"non-finite JSON number: {value}")


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_pairs,
            parse_constant=_reject_non_finite,
        )
    except (OSError, json.JSONDecodeError) as exc:
        raise MigrationValidationError(f"cannot load {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise MigrationValidationError(f"top-level JSON value must be an object: {path}")
    return value


def canonical_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def sha256_hex(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def _canonical_path(root: Path, relative: Any, expected: str | None = None) -> Path:
    if not isinstance(relative, str) or not relative:
        raise MigrationValidationError("reference path must be a non-empty string")
    if "\\" in relative:
        raise MigrationValidationError(f"path is not canonical POSIX form: {relative}")
    pure = PurePosixPath(relative)
    if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
        raise MigrationValidationError(f"path is not canonical repository-relative form: {relative}")
    if pure.as_posix() != relative:
        raise MigrationValidationError(f"path is not canonical repository-relative form: {relative}")
    if expected is not None and relative != expected:
        raise MigrationValidationError(f"path mismatch: expected {expected}, found {relative}")
    candidate = (root / relative).resolve()
    resolved_root = root.resolve()
    if candidate != resolved_root and resolved_root not in candidate.parents:
        raise MigrationValidationError(f"reference escapes repository root: {relative}")
    if not candidate.is_file():
        raise MigrationValidationError(f"stale or missing reference: {relative}")
    return candidate


def _unique_paths_before_set(value: Any, field: str) -> list[str]:
    if not isinstance(value, list):
        raise MigrationValidationError(f"{field} must be an array")
    result: list[str] = []
    seen: set[str] = set()
    for index, path in enumerate(value):
        if not isinstance(path, str) or not path:
            raise MigrationValidationError(f"{field}[{index}] must be a non-empty string")
        if path in seen:
            raise MigrationValidationError(f"duplicate migration path before set conversion: {path}")
        seen.add(path)
        result.append(path)
    return result


def validate_documents(
    migration: dict[str, Any],
    protocol: dict[str, Any],
    genomes: dict[str, dict[str, Any]],
) -> None:
    applies_to = _unique_paths_before_set(migration.get("applies_to"), "applies_to")
    if set(applies_to) != set(EXPECTED_GENOME_PATHS):
        raise MigrationValidationError("migration must apply to the exact four-genome path set")

    target = migration.get("to_protocol")
    if not isinstance(target, dict):
        raise MigrationValidationError("to_protocol must be an object")
    if target.get("path") != EXPECTED_PROTOCOL_PATH:
        raise MigrationValidationError("immutable protocol path mismatch")
    if target.get("protocol_id") != protocol.get("protocol_id"):
        raise MigrationValidationError("immutable protocol id mismatch")
    if target.get("required_status") != protocol.get("status"):
        raise MigrationValidationError("immutable protocol status mismatch")
    if target.get("canonicalization_profile") != "qso-canonical-json-v1":
        raise MigrationValidationError("canonicalization profile mismatch")
    if target.get("canonical_sha256") != sha256_hex(protocol):
        raise MigrationValidationError("immutable protocol canonical digest mismatch")

    sections = target.get("required_sections")
    if not isinstance(sections, list) or set(sections) != EXPECTED_REQUIRED_SECTIONS:
        raise MigrationValidationError("full immutable protocol sections are not bound")
    missing_sections = sorted(EXPECTED_REQUIRED_SECTIONS - set(protocol))
    if missing_sections:
        raise MigrationValidationError(f"immutable protocol sections missing: {missing_sections}")

    precedence = migration.get("precedence")
    if not isinstance(precedence, dict):
        raise MigrationValidationError("precedence must be an object")
    expected_precedence = {
        "authoritative_source": "to_protocol",
        "local_ethics_mode": "additive_only",
        "local_conflict_result": "reject_genome",
        "missing_or_mismatched_protocol_result": "reject_genome",
    }
    for key, expected in expected_precedence.items():
        if precedence.get(key) != expected:
            raise MigrationValidationError(f"precedence mismatch: {key}")

    requirements = migration.get("consumer_requirements")
    if not isinstance(requirements, dict):
        raise MigrationValidationError("consumer_requirements must be an object")
    for key in sorted(REQUIRED_TRUE_CONSUMER_FLAGS):
        if requirements.get(key) is not True:
            raise MigrationValidationError(f"consumer requirement must be true: {key}")

    policy = migration.get("local_ethics_policy")
    if not isinstance(policy, dict):
        raise MigrationValidationError("local_ethics_policy must be an object")
    expected_policy = {
        "binding_mode": "exact_canonical_list_digest",
        "unbound_addition_result": "reject_genome",
        "conflicting_addition_result": "reject_genome",
        "change_requires_new_migration_version": True,
    }
    for key, expected in expected_policy.items():
        if policy.get(key) != expected:
            raise MigrationValidationError(f"local ethics policy mismatch: {key}")

    bindings = migration.get("local_ethics_bindings")
    if not isinstance(bindings, list):
        raise MigrationValidationError("local_ethics_bindings must be an array")
    binding_by_path: dict[str, dict[str, Any]] = {}
    for index, binding in enumerate(bindings):
        if not isinstance(binding, dict):
            raise MigrationValidationError(f"local_ethics_bindings[{index}] must be an object")
        path = binding.get("path")
        if not isinstance(path, str) or not path:
            raise MigrationValidationError(f"local_ethics_bindings[{index}].path must be a non-empty string")
        if path in binding_by_path:
            raise MigrationValidationError(f"duplicate local ethics binding before set conversion: {path}")
        digest = binding.get("canonical_sha256")
        if not isinstance(digest, str) or len(digest) != 64:
            raise MigrationValidationError(f"invalid local ethics digest binding: {path}")
        binding_by_path[path] = binding
    if set(binding_by_path) != set(EXPECTED_GENOME_PATHS):
        raise MigrationValidationError("local ethics bindings must cover the exact four-genome path set")

    for path in EXPECTED_GENOME_PATHS:
        genome = genomes.get(path)
        if genome is None:
            raise MigrationValidationError(f"genome missing from migration replay: {path}")
        if genome.get("genome_id") != Path(path).stem:
            raise MigrationValidationError(f"genome id/path mismatch: {path}")
        ethics = genome.get("immutable", {}).get("ethics")
        if not isinstance(ethics, list) or not ethics or any(not isinstance(item, str) or not item for item in ethics):
            raise MigrationValidationError(f"genome-local ethics must be a non-empty string array: {path}")
        if len(ethics) != len(set(ethics)):
            raise MigrationValidationError(f"duplicate genome-local ethics: {path}")
        expected_digest = binding_by_path[path]["canonical_sha256"]
        if sha256_hex(ethics) != expected_digest:
            raise MigrationValidationError(
                f"unapproved or conflicting genome-local ethics change: {path}"
            )

    approval = migration.get("approval")
    if not isinstance(approval, dict):
        raise MigrationValidationError("approval must be an object")
    if approval.get("state") != "not_accepted":
        raise MigrationValidationError("candidate migration must not self-approve")
    if approval.get("required_action") != "human_review":
        raise MigrationValidationError("human review gate missing")
    if migration.get("migration_version") != 1:
        raise MigrationValidationError("migration version mismatch")
    if migration.get("status") != "candidate":
        raise MigrationValidationError("migration must remain candidate until acceptance")


def validate_migration(root: Path, migration_relative: str = "contracts/immutable-ethics-migration-v1.json") -> None:
    root = root.resolve()
    migration_path = _canonical_path(root, migration_relative, migration_relative)
    migration = load_json(migration_path)
    target = migration.get("to_protocol")
    if not isinstance(target, dict):
        raise MigrationValidationError("to_protocol must be an object")
    protocol_relative = target.get("path")
    protocol_path = _canonical_path(root, protocol_relative, EXPECTED_PROTOCOL_PATH)
    protocol = load_json(protocol_path)

    applies_to = _unique_paths_before_set(migration.get("applies_to"), "applies_to")
    genomes = {
        path: load_json(_canonical_path(root, path, path))
        for path in applies_to
    }
    validate_documents(migration, protocol, genomes)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        validate_migration(args.root)
    except MigrationValidationError as exc:
        print(f"FAIL: {exc}")
        return 1
    print("PASS: immutable protocol, unique migration paths, and bound local ethics are source-consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
