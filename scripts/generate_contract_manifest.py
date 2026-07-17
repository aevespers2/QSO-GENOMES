#!/usr/bin/env python3
"""Generate and verify the deterministic QSO-GENOMES compatibility manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "manifests" / "qso-genomes-compatibility-v1.json"
PROFILE_ID = "qso-canonical-json-v1"
COMPATIBILITY_SET_ID = "qso-genomes-four-object-v1"

ARTIFACT_SPECS = (
    ("contract", "aequitas-external-review-v1", "contracts/aequitas-review-binding.json", "contract_version"),
    ("contract", "immutable-baseline-v1", "contracts/immutable-baseline.json", "schema_version"),
    (
        "contract",
        "QSO-GENOME-IMMUTABLE-ETHICS-MIGRATION-v1",
        "contracts/immutable-ethics-migration-v1.json",
        "migration_version",
    ),
    ("genome", "atlas", "genomes/atlas.json", "schema_version"),
    ("genome", "lyra", "genomes/lyra.json", "schema_version"),
    ("genome", "nova", "genomes/nova.json", "schema_version"),
    ("genome", "orion", "genomes/orion.json", "schema_version"),
    (
        "protocol",
        "QSO-IMMUTABLE-ETHICS-v1",
        "protocols/immutable-ethics-v1.json",
        1,
    ),
    ("schema", "qso-genome", "schema/qso-genome.schema.json", "properties.schema_version.const"),
    ("schema", "qso-sprite", "schema/qso-sprite.schema.json", "properties.schema_version.const"),
    ("sprite", "aequitas", "sprites/aequitas.json", "schema_version"),
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


def _resolve_version(document: Any, version_source: str | int) -> int:
    if isinstance(version_source, int) and not isinstance(version_source, bool):
        if version_source < 1:
            raise ValueError("literal artifact version must be positive")
        return version_source

    if not isinstance(version_source, str):
        raise TypeError("version source must be a dotted document path or integer")

    value = document
    for part in version_source.split("."):
        value = value[part]
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f"{version_source} must resolve to an integer")
    return value


def build_manifest(root: Path = ROOT) -> dict[str, Any]:
    artifacts: list[dict[str, Any]] = []
    for kind, artifact_id, relative_path, version_source in ARTIFACT_SPECS:
        path = root / relative_path
        document = load_json(path)
        encoded = canonical_bytes(document)
        artifacts.append(
            {
                "artifact_id": artifact_id,
                "canonical_bytes": len(encoded),
                "kind": kind,
                "path": relative_path,
                "schema_version": _resolve_version(document, version_source),
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
