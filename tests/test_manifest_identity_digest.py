from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_contract_manifest.py"
SPEC = importlib.util.spec_from_file_location("generate_contract_manifest_identity", SCRIPT)
assert SPEC and SPEC.loader
manifest_tool = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = manifest_tool
SPEC.loader.exec_module(manifest_tool)


def sample_manifest() -> dict[str, object]:
    return {
        "manifest_version": 1,
        "compatibility_set_id": "example-v1",
        "status": "candidate",
        "canonicalization": {
            "profile": "qso-canonical-json-v1",
            "encoding": "UTF-8",
            "object_key_order": "lexicographic_unicode_code_point",
            "array_order": "preserved",
            "insignificant_whitespace": "removed",
            "duplicate_object_keys": "rejected",
            "non_finite_numbers": "rejected",
            "trailing_bytes": "LF",
        },
        "set_digest": manifest_tool.set_digest_metadata(),
        "artifacts": [
            {
                "artifact_id": "example",
                "canonical_bytes": 2,
                "kind": "contract",
                "path": "contracts/example.json",
                "schema_version": 1,
                "sha256": "0" * 64,
            }
        ],
        "set_sha256": "not-part-of-identity",
    }


class ManifestIdentityDigestTests(unittest.TestCase):
    def test_committed_digest_replays_from_identity_payload(self) -> None:
        manifest = json.loads(
            (ROOT / "manifests" / "qso-genomes-compatibility-v1.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(
            manifest["set_sha256"],
            manifest_tool.compute_set_sha256(manifest),
        )
        self.assertEqual(
            "3583dd05506c8d2921554676f80140cd66efa23a83154dbf4536ed51e56d5ed6",
            manifest["set_sha256"],
        )

    def test_digest_profile_declares_complete_identity_scope(self) -> None:
        self.assertEqual(
            {
                "algorithm": "sha256",
                "profile": "qso-genomes-manifest-identity-v1",
                "scope": "complete_identity_manifest",
                "excluded_fields": ["status", "set_sha256"],
            },
            manifest_tool.set_digest_metadata(),
        )

    def test_every_identity_section_changes_the_digest(self) -> None:
        manifest = sample_manifest()
        baseline = manifest_tool.compute_set_sha256(manifest)
        changes = {
            "manifest_version": 2,
            "compatibility_set_id": "example-v2",
            "canonicalization": {
                **manifest["canonicalization"],
                "trailing_bytes": "none",
            },
            "set_digest": {
                **manifest["set_digest"],
                "profile": "other-profile",
            },
            "artifacts": [
                {
                    **manifest["artifacts"][0],
                    "schema_version": 2,
                }
            ],
        }
        for field, replacement in changes.items():
            with self.subTest(field=field):
                changed = copy.deepcopy(manifest)
                changed[field] = replacement
                self.assertNotEqual(
                    baseline,
                    manifest_tool.compute_set_sha256(changed),
                )

    def test_artifact_descriptor_metadata_is_identity_bearing(self) -> None:
        manifest = sample_manifest()
        baseline = manifest_tool.compute_set_sha256(manifest)
        for field, replacement in (
            ("artifact_id", "renamed"),
            ("canonical_bytes", 3),
            ("kind", "schema"),
            ("path", "contracts/renamed.json"),
            ("schema_version", 2),
            ("sha256", "1" * 64),
        ):
            with self.subTest(field=field):
                changed = copy.deepcopy(manifest)
                changed["artifacts"][0][field] = replacement
                self.assertNotEqual(
                    baseline,
                    manifest_tool.compute_set_sha256(changed),
                )

    def test_lifecycle_status_and_digest_value_are_not_recursive_identity(self) -> None:
        manifest = sample_manifest()
        baseline = manifest_tool.compute_set_sha256(manifest)
        changed = copy.deepcopy(manifest)
        changed["status"] = "accepted"
        changed["set_sha256"] = "f" * 64
        self.assertEqual(baseline, manifest_tool.compute_set_sha256(changed))


if __name__ == "__main__":
    unittest.main()
