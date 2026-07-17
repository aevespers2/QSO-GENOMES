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
            "activation_rules": {
                "review_surfaces": [
                    {
                        "surface": "input",
                        "required_oversight": [
                            "classify_snippet_purpose",
                            "detect_vulnerabilities",
                        ],
                    },
                    {
                        "surface": "interpretation",
                        "required_oversight": [
                            "assess_integrity",
                            "assess_transparency",
                        ],
                    },
                    {
                        "surface": "ontology",
                        "required_oversight": [
                            "map_ontology",
                            "assess_equity",
                            "detect_bias",
                        ],
                    },
                    {
                        "surface": "proposed_edit",
                        "required_oversight": [
                            "assess_integrity",
                            "assess_transparency",
                            "detect_vulnerabilities",
                        ],
                    },
                    {
                        "surface": "communication",
                        "required_oversight": [
                            "classify_snippet_purpose",
                            "assess_equity",
                            "detect_bias",
                            "assess_transparency",
                        ],
                    },
                ]
            },
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
        self.sprite = {
            "schema_version": 1,
            "sprite_id": "aequitas",
            "oversight": {
                "classify_snippet_purpose": True,
                "map_ontology": True,
                "assess_equity": True,
                "detect_bias": True,
                "detect_vulnerabilities": True,
                "assess_integrity": True,
                "assess_transparency": True,
            },
            "ethics": {"human_review_required": True},
            "authority": {
                "may_annotate": True,
                "may_block_pending_review": True,
                "may_modify_genome": False,
                "may_execute": False,
                "may_write_repository": False,
                "may_override_immutable_ethics": False,
            },
        }
        self.write("contracts/aequitas-review-binding.json", self.binding)
        self.save_sprite()
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

    def save_sprite(self) -> None:
        self.write("sprites/aequitas.json", self.sprite)

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

    def test_duplicate_review_surface_is_rejected_before_deduplication(self) -> None:
        surfaces = self.binding["activation_rules"]["review_surfaces"]
        surfaces.append(copy.deepcopy(surfaces[0]))
        self.save_binding()
        with self.assertRaisesRegex(
            BindingValidationError, "duplicate review surface before de-duplication"
        ):
            validate_binding(self.root)

    def test_conflicting_duplicate_review_surface_is_rejected(self) -> None:
        surfaces = self.binding["activation_rules"]["review_surfaces"]
        conflicting = copy.deepcopy(surfaces[0])
        conflicting["required_oversight"] = ["assess_integrity"]
        surfaces.append(conflicting)
        self.save_binding()
        with self.assertRaisesRegex(
            BindingValidationError,
            "conflicting oversight definitions for duplicate review surface",
        ):
            validate_binding(self.root)

    def test_duplicate_oversight_definition_is_rejected_before_deduplication(self) -> None:
        required = self.binding["activation_rules"]["review_surfaces"][0][
            "required_oversight"
        ]
        required.append(required[0])
        self.save_binding()
        with self.assertRaisesRegex(
            BindingValidationError, "duplicate oversight definition before de-duplication"
        ):
            validate_binding(self.root)

    def test_unknown_oversight_definition_is_rejected(self) -> None:
        self.binding["activation_rules"]["review_surfaces"][0][
            "required_oversight"
        ].append("unpublished_capability")
        self.save_binding()
        with self.assertRaisesRegex(BindingValidationError, "unknown oversight definition"):
            validate_binding(self.root)

    def test_disabled_oversight_definition_is_rejected(self) -> None:
        self.sprite["oversight"]["detect_vulnerabilities"] = False
        self.save_sprite()
        with self.assertRaisesRegex(
            BindingValidationError, "required oversight conflicts with sprite source"
        ):
            validate_binding(self.root)

    def test_missing_review_surface_is_rejected(self) -> None:
        self.binding["activation_rules"]["review_surfaces"].pop()
        self.save_binding()
        with self.assertRaisesRegex(BindingValidationError, "review surface set mismatch"):
            validate_binding(self.root)


if __name__ == "__main__":
    unittest.main()
