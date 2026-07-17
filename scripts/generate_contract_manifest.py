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
SET_DIGEST_PROFILE = "qso-genomes-manifest-identity-v1"
SET_DIGEST_SCOPE = "complete_identity_manifest"
SET_DIGEST_EXCLUDED_FIELDS = ("status", "set_sha256")

ARTIFACT_SPECS = (
    ("contract", "aequitas-external-review-v1", "contracts/aequitas-review-binding.json", "contract_version"),
    ("contract", "immutable-baseline-v1", "contracts/immutable-baseline.json", "schema_version"),
    ("genome", "atlas", "genomes/atlas.json", "schema_version"),
    ("genome", "lyra", "genomes/lyra.json", "schema_version"),
    ("genome", "nova", "genomes/nova.json", "schema_version"),
    ("genome", "orion", "genomes/orion.json", "schema_version"),
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


def _resolve_version(document: Any, version_path: str) -> int:
    value = document
    for part in version_path.split("."):
        value = value[part]
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f"{version_path} must resolve to an integer")
    return value


def set_digest_metadata() -> dict[str, Any]:
    """Return the versioned rules that define compatibility-set identity."""
    return {
        "algorithm": "sha256",
        "profile": SET_DIGEST_PROFILE,
        "scope": SET_DIGEST_SCOPE,
        "excluded_fields": list(SET_DIGEST_EXCLUDED_FIELDS),
    }


def manifest_identity_payload(manifest: dict[str, Any]) -> dict[str, Any]:
    """Select every identity-bearing manifest field for set hashing.

    Lifecycle status is deliberately excluded so an accepted candidate retains
    the same set identity. The digest value itself is excluded to avoid
    recursion. Manifest version, set ID, complete canonicalization rules, digest
    semantics, and every artifact descriptor are identity-bearing.
    """
    return {
        "manifest_version": manifest["manifest_version"],
        "compatibility_set_id": manifest["compatibility_set_id"],
        "canonicalization": manifest["canonicalization"],
        "set_digest": manifest["set_digest"],
        "artifacts": manifest["artifacts"],
    }


def compute_set_sha256(manifest: dict[str, Any]) -> str:
    """Hash the complete versioned identity manifest under QSO Canonical JSON v1."""
    return sha256_hex(canonical_bytes(manifest_identity_payload(manifest)))


def build_manifest(root: Path = ROOT) -> dict[str, Any]:
    artifacts: list[dict[str, Any]] = []
    for kind, artifact_id, relative_path, version_path in ARTIFACT_SPECS:
        path = root / relative_path
        document = load_json(path)
        encoded = canonical_bytes(document)
        artifacts.append(
            {
                "artifact_id": artifact_id,
                "canonical_bytes": len(encoded),
                "kind": kind,
                "path": relative_path,
                "schema_version": _resolve_version(document, version_path),
                "sha256": sha256_hex(encoded),
            }
        )

    artifacts.sort(key=lambda item: item["path"])
    manifest = {
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
        "set_digest": set_digest_metadata(),
        "artifacts": artifacts,
    }
    manifest["set_sha256"] = compute_set_sha256(manifest)
    return manifest


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
            f"set_digest_profile={manifest['set_digest']['profile']}; "
            f"set_sha256={manifest['set_sha256']}"
        )
        return 0

    write_manifest(ROOT)
    manifest = build_manifest(ROOT)
    print(
        f"WROTE: {MANIFEST_PATH.relative_to(ROOT)}; "
        f"{len(manifest['artifacts'])} artifacts; "
        f"set_digest_profile={manifest['set_digest']['profile']}; "
        f"set_sha256={manifest['set_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
