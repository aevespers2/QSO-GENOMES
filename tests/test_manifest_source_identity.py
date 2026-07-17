from __future__ import annotations

import importlib.util
import json
import shutil
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


class ManifestSourceIdentityTests(unittest.TestCase):
    def _artifact_fixture(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        directory = tempfile.TemporaryDirectory()
        root = Path(directory.name)
        for spec in manifest_tool.ARTIFACT_SPECS:
            relative_path = spec[2]
            destination = root / relative_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative_path, destination)
        return directory, root

    @staticmethod
    def _rewrite(root: Path, relative_path: str, mutator) -> None:
        path = root / relative_path
        document = json.loads(path.read_text(encoding="utf-8"))
        mutator(document)
        path.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")

    def test_all_manifest_ids_and_versions_are_source_derived(self) -> None:
        manifest = manifest_tool.build_manifest(ROOT)
        by_path = {item["path"]: item for item in manifest["artifacts"]}

        for (
            _kind,
            declared_artifact_id,
            relative_path,
            identity_source,
            version_source,
        ) in manifest_tool.ARTIFACT_SPECS:
            document = manifest_tool.load_json(ROOT / relative_path)
            version = manifest_tool._resolve_version(document, version_source)
            artifact_id = manifest_tool._resolve_artifact_id(
                document,
                relative_path,
                identity_source,
                version,
            )
            self.assertEqual(declared_artifact_id, artifact_id)
            self.assertEqual(artifact_id, by_path[relative_path]["artifact_id"])
            self.assertEqual(version, by_path[relative_path]["schema_version"])

    def test_genome_identity_drift_fails_closed(self) -> None:
        directory, root = self._artifact_fixture()
        self.addCleanup(directory.cleanup)
        self._rewrite(
            root,
            "genomes/atlas.json",
            lambda document: document.__setitem__("genome_id", "atlas-drift"),
        )
        with self.assertRaisesRegex(ValueError, "source-derived artifact_id"):
            manifest_tool.build_manifest(root)

    def test_schema_id_path_drift_fails_closed(self) -> None:
        directory, root = self._artifact_fixture()
        self.addCleanup(directory.cleanup)
        self._rewrite(
            root,
            "schema/qso-genome.schema.json",
            lambda document: document.__setitem__(
                "$id",
                "https://github.com/aevespers2/QSO-GENOMES/blob/main/schema/other.schema.json",
            ),
        )
        with self.assertRaisesRegex(ValueError, "does not identify"):
            manifest_tool.build_manifest(root)

    def test_protocol_id_supplies_both_identity_and_version(self) -> None:
        directory, root = self._artifact_fixture()
        self.addCleanup(directory.cleanup)
        self._rewrite(
            root,
            "protocols/immutable-ethics-v1.json",
            lambda document: document.__setitem__(
                "protocol_id",
                "QSO-IMMUTABLE-ETHICS-v2",
            ),
        )
        with self.assertRaisesRegex(ValueError, "source-derived artifact_id"):
            manifest_tool.build_manifest(root)

    def test_path_version_identity_drift_fails_closed(self) -> None:
        directory, root = self._artifact_fixture()
        self.addCleanup(directory.cleanup)
        self._rewrite(
            root,
            "contracts/immutable-baseline.json",
            lambda document: document.__setitem__("schema_version", 2),
        )
        with self.assertRaisesRegex(ValueError, "immutable-baseline-v2"):
            manifest_tool.build_manifest(root)


if __name__ == "__main__":
    unittest.main()
