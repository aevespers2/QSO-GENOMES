from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_schema_set.py"
SPEC = importlib.util.spec_from_file_location("validate_schema_set", SCRIPT)
assert SPEC and SPEC.loader
schema_tool = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = schema_tool
SPEC.loader.exec_module(schema_tool)


class ExactArtifactSetTests(unittest.TestCase):
    def write_json(self, directory: Path, *names: str) -> None:
        for name in names:
            (directory / name).write_text("{}\n", encoding="utf-8")

    def test_exact_required_genome_set_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            self.write_json(directory, *schema_tool.REQUIRED_GENOME_FILENAMES)
            schema_tool.assert_exact_json_artifact_set(
                directory,
                schema_tool.REQUIRED_GENOME_FILENAMES,
                label="genome",
            )

    def test_missing_required_genome_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            names = tuple(
                name
                for name in schema_tool.REQUIRED_GENOME_FILENAMES
                if name != "nova.json"
            )
            self.write_json(directory, *names)
            with self.assertRaisesRegex(
                schema_tool.ArtifactSetError,
                r"missing required genome artifacts: nova\.json",
            ):
                schema_tool.assert_exact_json_artifact_set(
                    directory,
                    schema_tool.REQUIRED_GENOME_FILENAMES,
                    label="genome",
                )

    def test_unexpected_genome_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            self.write_json(
                directory,
                *schema_tool.REQUIRED_GENOME_FILENAMES,
                "rogue.json",
            )
            with self.assertRaisesRegex(
                schema_tool.ArtifactSetError,
                r"unexpected genome artifacts: rogue\.json",
            ):
                schema_tool.assert_exact_json_artifact_set(
                    directory,
                    schema_tool.REQUIRED_GENOME_FILENAMES,
                    label="genome",
                )

    def test_empty_active_sprite_set_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            schema_tool.assert_exact_json_artifact_set(
                Path(temporary_directory),
                schema_tool.REQUIRED_SPRITE_FILENAMES,
                label="active sprite",
            )

    def test_disengaged_sprite_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            self.write_json(directory, "aequitas.json")
            with self.assertRaisesRegex(
                schema_tool.ArtifactSetError,
                r"unexpected active sprite artifacts: aequitas\.json",
            ):
                schema_tool.assert_exact_json_artifact_set(
                    directory,
                    schema_tool.REQUIRED_SPRITE_FILENAMES,
                    label="active sprite",
                )

    def test_non_json_support_file_does_not_change_schema_bound_set(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            self.write_json(directory, *schema_tool.REQUIRED_GENOME_FILENAMES)
            (directory / "README.md").write_text("documentation\n", encoding="utf-8")
            schema_tool.assert_exact_json_artifact_set(
                directory,
                schema_tool.REQUIRED_GENOME_FILENAMES,
                label="genome",
            )


if __name__ == "__main__":
    unittest.main()
