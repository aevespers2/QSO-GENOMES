from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_contract_manifest.py"
SPEC = importlib.util.spec_from_file_location("generate_contract_manifest", SCRIPT)
assert SPEC and SPEC.loader
manifest_tool = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = manifest_tool
SPEC.loader.exec_module(manifest_tool)


class ContractManifestTests(unittest.TestCase):
    def test_manifest_is_current(self) -> None:
        self.assertTrue(manifest_tool.check_manifest(ROOT))

    def test_artifact_paths_are_complete_sorted_and_unique(self) -> None:
        manifest = manifest_tool.build_manifest(ROOT)
        paths = [item["path"] for item in manifest["artifacts"]]
        expected = sorted(spec[2] for spec in manifest_tool.ARTIFACT_SPECS)
        self.assertEqual(expected, paths)
        self.assertEqual(len(paths), len(set(paths)))
        self.assertEqual(9, len(paths))

    def test_each_hash_and_byte_count_matches_canonical_content(self) -> None:
        manifest = manifest_tool.build_manifest(ROOT)
        for item in manifest["artifacts"]:
            document = manifest_tool.load_json(ROOT / item["path"])
            encoded = manifest_tool.canonical_bytes(document)
            self.assertEqual(manifest_tool.sha256_hex(encoded), item["sha256"])
            self.assertEqual(len(encoded), item["canonical_bytes"])
            self.assertEqual(64, len(item["sha256"]))

    def test_canonicalization_is_format_independent(self) -> None:
        left = json.loads('{"z":[3,2,1],"a":{"y":true,"x":0.7}}')
        right = json.loads('{\n  "a": {"x": 0.7, "y": true},\n  "z": [3, 2, 1]\n}')
        self.assertEqual(
            manifest_tool.canonical_bytes(left),
            manifest_tool.canonical_bytes(right),
        )

    def test_duplicate_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"a":1,"a":2}', encoding="utf-8")
            with self.assertRaises(manifest_tool.DuplicateKeyError):
                manifest_tool.load_json(path)

    def test_set_digest_is_repeatable_and_committed(self) -> None:
        first = manifest_tool.build_manifest(ROOT)
        second = manifest_tool.build_manifest(ROOT)
        committed = json.loads(
            (ROOT / "manifests" / "qso-genomes-compatibility-v1.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(first, second)
        self.assertEqual(first["set_sha256"], committed["set_sha256"])
        self.assertEqual(
            "3583dd05506c8d2921554676f80140cd66efa23a83154dbf4536ed51e56d5ed6",
            first["set_sha256"],
        )

    def test_digest_covers_all_identity_bearing_metadata(self) -> None:
        manifest = manifest_tool.build_manifest(ROOT)
        expected = manifest["set_sha256"]
        mutations = (
            ("manifest_version", lambda value: value + 1),
            ("compatibility_set_id", lambda value: value + "-changed"),
            ("canonicalization", lambda value: {**value, "encoding": "UTF-16"}),
            ("set_digest", lambda value: {**value, "profile": "changed"}),
            (
                "artifacts",
                lambda value: [
                    {**value[0], "artifact_id": value[0]["artifact_id"] + "-changed"},
                    *value[1:],
                ],
            ),
        )
        for field, mutate in mutations:
            with self.subTest(field=field):
                changed = copy.deepcopy(manifest)
                changed[field] = mutate(changed[field])
                self.assertNotEqual(expected, manifest_tool.compute_set_sha256(changed))

    def test_status_is_explicitly_non_identity_bearing(self) -> None:
        manifest = manifest_tool.build_manifest(ROOT)
        accepted = copy.deepcopy(manifest)
        accepted["status"] = "accepted"
        self.assertEqual(
            manifest["set_sha256"],
            manifest_tool.compute_set_sha256(accepted),
        )
        self.assertEqual(
            ["status", "set_sha256"],
            manifest["set_digest"]["excluded_fields"],
        )


if __name__ == "__main__":
    unittest.main()
