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


class ManifestDigestScopeTests(unittest.TestCase):
    def _write_json(self, root: Path, relative_path: str, value: object) -> None:
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

    def _fixture_root(self, root: Path) -> None:
        documents = {
            "contracts/aequitas-review-binding.json": {
                "binding_id": "aequitas-external-review-v1",
                "contract_version": 1,
            },
            "contracts/immutable-baseline.json": {"schema_version": 1},
            "contracts/immutable-ethics-migration-v1.json": {
                "migration_id": "QSO-GENOME-IMMUTABLE-ETHICS-MIGRATION-v1",
                "migration_version": 1,
            },
            "genomes/atlas.json": {"genome_id": "atlas", "schema_version": 1},
            "genomes/lyra.json": {"genome_id": "lyra", "schema_version": 1},
            "genomes/nova.json": {"genome_id": "nova", "schema_version": 1},
            "genomes/orion.json": {"genome_id": "orion", "schema_version": 1},
            "protocols/immutable-ethics-v1.json": {
                "protocol_id": "QSO-IMMUTABLE-ETHICS-v1"
            },
            "schema/qso-genome.schema.json": {
                "$id": "https://example.invalid/schema/qso-genome.schema.json",
                "properties": {"schema_version": {"const": 1}},
            },
            "schema/qso-sprite.schema.json": {
                "$id": "https://example.invalid/schema/qso-sprite.schema.json",
                "properties": {"schema_version": {"const": 1}},
            },
            "sprites/aequitas.json": {
                "sprite_id": "aequitas",
                "schema_version": 1,
            },
        }
        for path, document in documents.items():
            self._write_json(root, path, document)

    def test_declares_artifact_and_manifest_digest_scopes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._fixture_root(root)
            manifest = manifest_tool.build_manifest(root)

        semantics = manifest["digest_semantics"]
        self.assertEqual("canonical_artifact_bytes", semantics["artifact_sha256"]["input"])
        self.assertEqual("canonical_manifest_identity", semantics["set_sha256"]["input"])
        self.assertEqual(
            ["set_sha256", "status"],
            semantics["set_sha256"]["excluded_top_level_fields"],
        )
        self.assertEqual(
            list(manifest_tool.ARTIFACT_DESCRIPTOR_FIELDS),
            semantics["set_sha256"]["artifact_descriptor_fields"],
        )
        self.assertEqual(
            manifest["set_sha256"],
            manifest_tool.set_sha256_for_manifest(manifest),
        )

    def test_lifecycle_status_is_not_set_identity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._fixture_root(root)
            manifest = manifest_tool.build_manifest(root)

        accepted = copy.deepcopy(manifest)
        accepted["status"] = "accepted"
        self.assertEqual(
            manifest_tool.set_sha256_for_manifest(manifest),
            manifest_tool.set_sha256_for_manifest(accepted),
        )

    def test_every_artifact_descriptor_field_is_bound(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._fixture_root(root)
            manifest = manifest_tool.build_manifest(root)

        original = manifest_tool.set_sha256_for_manifest(manifest)
        mutations = {
            "artifact_id": "changed-id",
            "canonical_bytes": manifest["artifacts"][0]["canonical_bytes"] + 1,
            "kind": "changed-kind",
            "path": "changed/path.json",
            "schema_version": manifest["artifacts"][0]["schema_version"] + 1,
            "sha256": "0" * 64,
        }
        for field, value in mutations.items():
            with self.subTest(field=field):
                changed = copy.deepcopy(manifest)
                changed["artifacts"][0][field] = value
                self.assertNotEqual(
                    original,
                    manifest_tool.set_sha256_for_manifest(changed),
                )

    def test_new_top_level_consumer_metadata_is_bound(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._fixture_root(root)
            manifest = manifest_tool.build_manifest(root)

        changed = copy.deepcopy(manifest)
        changed["consumer_contract"] = {"minimum_runtime": "1"}
        self.assertNotEqual(
            manifest_tool.set_sha256_for_manifest(manifest),
            manifest_tool.set_sha256_for_manifest(changed),
        )

    def test_undeclared_artifact_descriptor_metadata_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._fixture_root(root)
            manifest = manifest_tool.build_manifest(root)

        changed = copy.deepcopy(manifest)
        changed["artifacts"][0]["consumer_hint"] = "not declared"
        with self.assertRaisesRegex(ValueError, "fields do not match digest scope"):
            manifest_tool.set_sha256_for_manifest(changed)

    def test_digest_semantics_mutation_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._fixture_root(root)
            manifest = manifest_tool.build_manifest(root)

        changed = copy.deepcopy(manifest)
        changed["digest_semantics"]["algorithm"] = "SHA-512"
        with self.assertRaisesRegex(ValueError, "digest semantics"):
            manifest_tool.set_sha256_for_manifest(changed)


if __name__ == "__main__":
    unittest.main()
