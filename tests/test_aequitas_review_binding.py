import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BINDING_PATH = ROOT / "contracts" / "aequitas-review-binding.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_repo_path(relative_path: str) -> Path:
    candidate = (ROOT / relative_path).resolve()
    root = ROOT.resolve()
    if candidate != root and root not in candidate.parents:
        raise AssertionError(f"path escapes repository root: {relative_path}")
    return candidate


class AequitasReviewBindingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.binding = load_json(BINDING_PATH)
        sprite_reference = cls.binding["sprite_reference"]
        cls.sprite_path = resolve_repo_path(sprite_reference["path"])
        cls.schema_path = resolve_repo_path(sprite_reference["schema_path"])
        cls.sprite = load_json(cls.sprite_path)
        cls.schema = load_json(cls.schema_path)
        cls.genomes = {}
        for reference in cls.binding["genome_references"]:
            path = resolve_repo_path(reference["path"])
            cls.genomes[reference["genome_id"]] = load_json(path)

    def test_references_resolve_and_match_identifiers(self) -> None:
        sprite_reference = self.binding["sprite_reference"]
        self.assertTrue(self.sprite_path.is_file())
        self.assertTrue(self.schema_path.is_file())
        self.assertEqual(sprite_reference["sprite_id"], self.sprite["sprite_id"])
        self.assertEqual(sprite_reference["schema_version"], self.sprite["schema_version"])
        self.assertEqual(
            sprite_reference["schema_version"],
            self.schema["properties"]["schema_version"]["const"],
        )
        self.assertEqual(
            {"atlas", "lyra", "nova", "orion"},
            set(self.genomes),
        )
        for reference in self.binding["genome_references"]:
            genome = self.genomes[reference["genome_id"]]
            self.assertEqual(reference["genome_id"], genome["genome_id"])

    def test_sprite_requires_review_and_has_no_execution_authority(self) -> None:
        authority = self.sprite["authority"]
        expected_authority = {
            "may_annotate": True,
            "may_block_pending_review": True,
            "may_modify_genome": False,
            "may_execute": False,
            "may_write_repository": False,
            "may_override_immutable_ethics": False,
        }
        self.assertTrue(self.sprite["ethics"]["human_review_required"])
        self.assertEqual(expected_authority, authority)
        for key, expected in expected_authority.items():
            self.assertEqual(
                expected,
                self.schema["properties"]["authority"]["properties"][key]["const"],
            )

    def test_review_surfaces_cover_enabled_sprite_oversight(self) -> None:
        surfaces = self.binding["activation_rules"]["review_surfaces"]
        expected_surfaces = {
            "input",
            "interpretation",
            "ontology",
            "proposed_edit",
            "communication",
        }
        self.assertEqual(expected_surfaces, {item["surface"] for item in surfaces})
        referenced_oversight = {
            key
            for item in surfaces
            for key in item["required_oversight"]
        }
        enabled_oversight = {
            key for key, enabled in self.sprite["oversight"].items() if enabled
        }
        self.assertEqual(enabled_oversight, referenced_oversight)

    def test_activation_is_external_human_review_and_fails_closed(self) -> None:
        rules = self.binding["activation_rules"]
        self.assertEqual("external_controller_only", rules["mode"])
        self.assertEqual("human", rules["reviewer_type"])
        self.assertEqual(
            "genome.learning.human_review_threshold",
            rules["threshold_source"],
        )
        self.assertEqual(
            ["approve", "block_pending_review", "reject"],
            rules["allowed_decisions"],
        )
        self.assertEqual("block_pending_review", rules["default_on_missing_review"])
        self.assertEqual("external_controller", rules["commit_actor"])
        self.assertEqual(
            {
                "approve": True,
                "block_pending_review": False,
                "reject": False,
                "missing": False,
            },
            rules["commit_permissions"],
        )
        self.assertEqual(
            {
                "decision",
                "annotations",
                "evidence",
                "rationale",
                "reviewer_id",
                "timestamp",
                "input_sha256",
            },
            set(rules["required_record_fields"]),
        )

    def test_all_genomes_keep_commit_and_mutation_outside_qso_control(self) -> None:
        for genome_id, genome in self.genomes.items():
            with self.subTest(genome=genome_id):
                freeze = genome["freeze"]
                evolution = genome["learning"]["goal_evolution"]
                self.assertTrue(freeze["external_commit_only"])
                self.assertTrue(freeze["require_hash"])
                self.assertTrue(freeze["rollback_on_violation"])
                self.assertFalse(evolution["may_change_purpose"])
                self.assertFalse(evolution["may_change_immutable"])
                self.assertTrue(genome["learning"]["uncertainty_required"])
                threshold = genome["learning"]["human_review_threshold"]
                self.assertGreaterEqual(threshold, 0.0)
                self.assertLessEqual(threshold, 1.0)


if __name__ == "__main__":
    unittest.main()
