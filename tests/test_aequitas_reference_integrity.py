import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_aequitas_binding import BindingValidationError, validate_binding

ROOT = Path(__file__).resolve().parents[1]


class RepositoryAequitasBindingTests(unittest.TestCase):
    def test_repository_binding_passes(self) -> None:
        validate_binding(ROOT)


class AequitasReferenceIntegrityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for directory in ("contracts", "sprites", "schema", "genomes"):
            (self.root / directory).mkdir()
        self.binding = {
            "sprite_reference": {
                "sprite_id": "aequitas",
                "path": "sprites/aequitas.json",
                "schema_path": "schema/qso-sprite.schema.json",
                "schema_version": 1,
            },
            "genome_references": [
                {"genome_id": genome_id, "path": f"genomes/{genome_id}.json"}
                for genome_id in ("atlas", "lyra", "nova", "orion")
            ],
            "invariants": {
                "sprite_human_review_required": True,
                "sprite_may_annotate": True,
                "sprite_may_block_pending_review": True,
                "sprite_may_modify_genome": False,
                "sprite_may_execute": False,
                "sprite_may_write_repository": False,
                "sprite_may_override_immutable_ethics": False,
                "genomes_require_external_commit": True,
                "genomes_require_hash": True,
                "genomes_rollback_on_violation": True,
                "genomes_may_change_purpose": False,
                "genomes_may_change_immutable": False,
            },
        }
        self.write("contracts/aequitas-review-binding.json", self.binding)
        self.write(
            "sprites/aequitas.json",
            {
                "schema_version": 1,
                "sprite_id": "aequitas",
                "ethics": {"human_review_required": True},
                "authority": {
                    "may_annotate": True,
                    "may_block_pending_review": True,
                    "may_modify_genome": False,
                    "may_execute": False,
                    "may_write_repository": False,
                    "may_override_immutable_ethics": False,
                },
            },
        )
        self.write(
            "schema/qso-sprite.schema.json",
            {"properties": {"schema_version": {"const": 1}}},
        )
        for genome_id in ("atlas", "lyra", "nova", "orion"):
            self.write(
                f"genomes/{genome_id}.json",
                {
                    "genome_id": genome_id,
                    "freeze": {
                        "external_commit_only": True,
                        "require_hash": True,
                        "rollback_on_violation": True,
                    },
                    "learning": {
                        "goal_evolution": {
                            "may_change_purpose": False,
                            "may_change_immutable": False,
                        }
                    },
                },
            )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write(self, relative: str, value: object) -> None:
        (self.root / relative).write_text(json.dumps(value), encoding="utf-8")

    def save_binding(self) -> None:
        self.write("contracts/aequitas-review-binding.json", self.binding)

    def test_source_artifacts_pass(self) -> None:
        validate_binding(self.root)

    def test_duplicate_identifier_is_rejected_before_deduplication(self) -> None:
        self.binding["genome_references"].append(
            copy.deepcopy(self.binding["genome_references"][0])
        )
        self.save_binding()
        with self.assertRaisesRegex(
            BindingValidationError, "duplicate genome_id before de-duplication"
        ):
            validate_binding(self.root)

    def test_duplicate_path_is_rejected_before_deduplication(self) -> None:
        self.binding["genome_references"][1]["path"] = "genomes/atlas.json"
        self.save_binding()
        with self.assertRaisesRegex(
            BindingValidationError, "duplicate genome path before de-duplication"
        ):
            validate_binding(self.root)

    def test_path_inconsistent_reference_is_rejected(self) -> None:
        self.binding["genome_references"][0]["path"] = "./genomes/atlas.json"
        self.save_binding()
        with self.assertRaisesRegex(
            BindingValidationError, "path is not canonical|path-inconsistent"
        ):
            validate_binding(self.root)

    def test_stale_source_identifier_is_rejected(self) -> None:
        genome_path = self.root / "genomes/atlas.json"
        genome = json.loads(genome_path.read_text(encoding="utf-8"))
        genome["genome_id"] = "atlas-v0"
        self.write("genomes/atlas.json", genome)
        with self.assertRaisesRegex(BindingValidationError, "stale genome reference"):
            validate_binding(self.root)

    def test_published_invariant_must_match_source(self) -> None:
        self.binding["invariants"]["sprite_may_execute"] = True
        self.save_binding()
        with self.assertRaisesRegex(
            BindingValidationError, "published invariant disagrees"
        ):
            validate_binding(self.root)

    def test_missing_invariant_is_rejected(self) -> None:
        del self.binding["invariants"]["genomes_require_hash"]
        self.save_binding()
        with self.assertRaisesRegex(BindingValidationError, "invariant key set mismatch"):
            validate_binding(self.root)


if __name__ == "__main__":
    unittest.main()
