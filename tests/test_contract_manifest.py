from __future__ import annotations

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
        self.assertEqual(11, len(paths))

    def test_manifest_binds_immutable_protocol_and_migration(self) -> None:
        manifest = manifest_tool.build_manifest(ROOT)
        by_path = {item["path"]: item for item in manifest["artifacts"]}
        protocol_path = "protocols/immutable-ethics-v1.json"
        migration_path = "contracts/immutable-ethics-migration-v1.json"

        self.assertIn(protocol_path, by_path)
        self.assertIn(migration_path, by_path)
        self.assertEqual(
            "QSO-IMMUTABLE-ETHICS-v1",
            by_path[protocol_path]["artifact_id"],
        )
        self.assertEqual(
            "QSO-GENOME-IMMUTABLE-ETHICS-MIGRATION-v1",
            by_path[migration_path]["artifact_id"],
        )

        migration = manifest_tool.load_json(ROOT / migration_path)
        self.assertEqual(
            migration["to_protocol"]["canonical_sha256"],
            by_path[protocol_path]["sha256"],
        )
        self.assertEqual(
            manifest_tool.sha256_hex(
                manifest_tool.canonical_bytes(migration)
            ),
            by_path[migration_path]["sha256"],
        )

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
            "2b59fe7c865409f9112eb3d21bb1954abb7c8195eaa7758da6602fec8410ba6e",
            first["set_sha256"],
        )


if __name__ == "__main__":
    unittest.main()
