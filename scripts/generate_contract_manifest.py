#!/usr/bin/env python3
"""Generate and verify the deterministic QSO-GENOMES compatibility manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "manifests" / "qso-genomes-compatibility-v1.json"
PROFILE_ID = "qso-canonical-json-v1"
COMPATIBILITY_SET_ID = "qso-genomes-four-object-v1"
IDENTITY_FROM_PATH_VERSION = "@path-version"
IDENTITY_FROM_SCHEMA_ID = "@schema-id"
VERSION_FROM_ID_PREFIX = "@id-version:"

# kind, declared artifact id, relative path, source identity selector, source version selector
ARTIFACT_SPECS = (
    (
        "contract",
        "aequitas-external-review-v1",
        "contracts/aequitas-review-binding.json",
        "binding_id",
        "contract_version",
    ),
    (
        "contract",
        "immutable-baseline-v1",
        "contracts/immutable-baseline.json",
        IDENTITY_FROM_PATH_VERSION,
        "schema_version",
    ),
    (
        "contract",
        "QSO-GENOME-IMMUTABLE-ETHICS-MIGRATION-v1",
        "contracts/immutable-ethics-migration-v1.json",
        "migration_id",
        "migration_version",
    ),
    ("genome", "atlas", "genomes/atlas.json", "genome_id", "schema_version"),
    ("genome", "lyra", "genomes/lyra.json", "genome_id", "schema_version"),
    ("genome", "nova", "genomes/nova.json", "genome_id", "schema_version"),
    ("genome", "orion", "genomes/orion.json", "genome_id", "schema_version"),
    (
        "protocol",
        "QSO-IMMUTABLE-ETHICS-v1",
        "protocols/immutable-ethics-v1.json",
        "protocol_id",
        f"{VERSION_FROM_ID_PREFIX}protocol_id",
    ),
    (
        "schema",
        "qso-genome",
        "schema/qso-genome.schema.json",
        IDENTITY_FROM_SCHEMA_ID,
        "properties.schema_version.const",
    ),
    (
        "schema",
        "qso-sprite",
        "schema/qso-sprite.schema.json",
        IDENTITY_FROM_SCHEMA_ID,
        "properties.schema_version.const",
    ),
    ("sprite", "aequitas", "sprites/aequitas.json", "sprite_id", "schema_version"),
)


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a key."""


def _reject_duplicate_keys(pairs: Iterable[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON object key: {key}")
        result[key] = value
    return result


def _reject_nonfinite(value: str) -> None:
    raise ValueError(f"non-finite JSON number is not allowed: {value}")


def load_json(path: Path) -> Any:
    """Load strict JSON while rejecting duplicate keys and non-finite numbers."""
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=_reject_duplicate_keys,
        parse_constant=_reject_nonfinite,
    )


def canonical_bytes(value: Any) -> bytes:
    """Encode QSO Canonical JSON v1.

    The profile uses UTF-8, lexicographically sorted object keys, preserved array
    order, no insignificant whitespace, JSON-native finite numbers, and one
    trailing LF. Input JSON is parsed with duplicate-key rejection.
    """
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


def sha256_hex(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _resolve_document_value(document: Any, source: str) -> Any:
    value = document
    for part in source.split("."):
        try:
            value = value[part]
        except (KeyError, TypeError) as exc:
            raise ValueError(f"missing source identity field: {source}") from exc
    return value


def _resolve_version(document: Any, version_source: str | int) -> int:
    if isinstance(version_source, int) and not isinstance(version_source, bool):
        if version_source < 1:
            raise ValueError("literal artifact version must be positive")
        return version_source

    if not isinstance(version_source, str):
        raise TypeError("version source must be a dotted document path or integer")

    if version_source.startswith(VERSION_FROM_ID_PREFIX):
        identity_source = version_source.removeprefix(VERSION_FROM_ID_PREFIX)
        identity = _resolve_document_value(document, identity_source)
        if not isinstance(identity, str):
            raise ValueError(f"{identity_source} must resolve to a string")
        match = re.fullmatch(r".+-v([1-9][0-9]*)", identity)
        if match is None:
            raise ValueError(
                f"{identity_source} must end with a positive '-vN' version suffix"
            )
        return int(match.group(1))

    value = _resolve_document_value(document, version_source)
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise ValueError(f"{version_source} must resolve to a positive integer")
    return value


def _resolve_artifact_id(
    document: Any,
    relative_path: str,
    identity_source: str,
    version: int,
) -> str:
    if identity_source == IDENTITY_FROM_PATH_VERSION:
        source_stem = Path(relative_path).stem
        return f"{source_stem}-v{version}"

    if identity_source == IDENTITY_FROM_SCHEMA_ID:
        schema_id = _resolve_document_value(document, "$id")
        if not isinstance(schema_id, str) or not schema_id:
            raise ValueError("$id must resolve to a non-empty string")
        parsed = urlsplit(schema_id)
        expected_suffix = f"/{relative_path}"
        if not parsed.path.endswith(expected_suffix):
            raise ValueError(
                f"schema $id path {parsed.path!r} does not identify {relative_path!r}"
            )
        filename = Path(parsed.path).name
        suffix = ".schema.json"
        if not filename.endswith(suffix):
            raise ValueError("schema $id filename must end with '.schema.json'")
        return filename[: -len(suffix)]

    artifact_id = _resolve_document_value(document, identity_source)
    if not isinstance(artifact_id, str) or not artifact_id.strip():
        raise ValueError(f"{identity_source} must resolve to a non-empty string")
    if artifact_id != artifact_id.strip():
        raise ValueError(f"{identity_source} must not contain surrounding whitespace")
    return artifact_id


def build_manifest(root: Path = ROOT) -> dict[str, Any]:
    artifacts: list[dict[str, Any]] = []
    seen_paths: set[str] = set()
    seen_artifact_ids: set[str] = set()

    for (
        kind,
        declared_artifact_id,
        relative_path,
        identity_source,
        version_source,
    ) in ARTIFACT_SPECS:
        if relative_path in seen_paths:
            raise ValueError(f"duplicate manifest artifact path: {relative_path}")
        seen_paths.add(relative_path)

        path = root / relative_path
        document = load_json(path)
        version = _resolve_version(document, version_source)
        artifact_id = _resolve_artifact_id(
            document,
            relative_path,
            identity_source,
            version,
        )
        if artifact_id != declared_artifact_id:
            raise ValueError(
                f"{relative_path}: source-derived artifact_id {artifact_id!r} "
                f"does not match declared artifact_id {declared_artifact_id!r}"
            )
        if artifact_id in seen_artifact_ids:
            raise ValueError(f"duplicate manifest artifact_id: {artifact_id}")
        seen_artifact_ids.add(artifact_id)

        encoded = canonical_bytes(document)
        artifacts.append(
            {
                "artifact_id": artifact_id,
                "canonical_bytes": len(encoded),
                "kind": kind,
                "path": relative_path,
                "schema_version": version,
                "sha256": sha256_hex(encoded),
            }
        )

    artifacts.sort(key=lambda item: item["path"])
    set_payload = {
        "compatibility_set_id": COMPATIBILITY_SET_ID,
        "artifacts": [
            {"path": item["path"], "sha256": item["sha256"]}
            for item in artifacts
        ],
    }

    return {
        "manifest_version": 1,
        "compatibility_set_id": COMPATIBILITY_SET_ID,
        "status": "candidate",
        "canonicalization": {
            "profile": PROFILE_ID,
            "encoding": "UTF-8",
            "object_key_order": "lexicographic_unicode_code_point",
            "array_order": "preserved",
            "insignificant_whitespace": "removed",
            "duplicate_object_keys": "rejected",
            "non_finite_numbers": "rejected",
            "trailing_bytes": "LF",
        },
        "artifacts": artifacts,
        "set_sha256": sha256_hex(canonical_bytes(set_payload)),
    }


def rendered_manifest(root: Path = ROOT) -> str:
    return json.dumps(build_manifest(root), ensure_ascii=False, indent=2) + "\n"


def write_manifest(root: Path = ROOT) -> None:
    path = root / MANIFEST_PATH.relative_to(ROOT)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(rendered_manifest(root), encoding="utf-8")


def check_manifest(root: Path = ROOT) -> bool:
    path = root / MANIFEST_PATH.relative_to(ROOT)
    if not path.exists():
        return False
    return path.read_text(encoding="utf-8") == rendered_manifest(root)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify the committed manifest instead of rewriting it",
    )
    args = parser.parse_args()

    if args.check:
        if not check_manifest(ROOT):
            print(f"FAIL: {MANIFEST_PATH.relative_to(ROOT)} is missing or stale")
            return 1
        manifest = build_manifest(ROOT)
        print(
            "PASS: "
            f"{len(manifest['artifacts'])} artifacts; "
            f"set_sha256={manifest['set_sha256']}"
        )
        return 0

    write_manifest(ROOT)
    manifest = build_manifest(ROOT)
    print(
        f"WROTE: {MANIFEST_PATH.relative_to(ROOT)}; "
        f"{len(manifest['artifacts'])} artifacts; "
        f"set_sha256={manifest['set_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
