from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path

from scripts.check_capability_evidence_review import (
    EXPECTED_STATUS,
    GUIDE_PATH,
    load_profile,
    validate_coordination_routes,
    validate_guide,
    validate_profile,
)


class CapabilityEvidenceReviewTests(unittest.TestCase):
    def setUp(self) -> None:
        self.profile = load_profile()

    def assert_rejected(self, mutator) -> None:
        candidate = copy.deepcopy(self.profile)
        mutator(candidate)
        self.assertTrue(validate_profile(candidate))

    def test_current_packet_passes(self) -> None:
        self.assertEqual([], validate_profile(self.profile))
        self.assertEqual([], validate_guide())
        self.assertEqual([], validate_coordination_routes())

    def test_rejects_admitted_status(self) -> None:
        self.assert_rejected(lambda value: value.__setitem__("status", "OPERATIONALLY_ADMITTED"))

    def test_rejects_authority_effect(self) -> None:
        self.assert_rejected(lambda value: value.__setitem__("authority_effect", "self_edit_commit"))

    def test_rejects_evidence_ladder_reordering(self) -> None:
        def mutate(value):
            value["evidence_levels"][0], value["evidence_levels"][1] = (
                value["evidence_levels"][1],
                value["evidence_levels"][0],
            )
        self.assert_rejected(mutate)

    def test_rejects_missing_observed_generation(self) -> None:
        self.assert_rejected(lambda value: value["observed_generations"].pop())

    def test_rejects_wrong_exact_head(self) -> None:
        self.assert_rejected(
            lambda value: value["observed_generations"][0].__setitem__("head", "0" * 40)
        )

    def test_rejects_missing_self_edit_class(self) -> None:
        self.assert_rejected(lambda value: value["self_edit_classes"].pop("D"))

    def test_rejects_missing_rollback_section(self) -> None:
        self.assert_rejected(lambda value: value["required_packet_sections"].remove("rollback"))

    def test_rejects_weakened_immutable_boundary(self) -> None:
        self.assert_rejected(
            lambda value: value["immutable_review_boundaries"].remove("no_self_approval")
        )

    def test_rejects_missing_external_disposition(self) -> None:
        self.assert_rejected(
            lambda value: value["acceptance_gates"].remove("EXTERNAL_HUMAN_DISPOSITION")
        )

    def test_rejects_self_edit_commit_promotion(self) -> None:
        self.assert_rejected(
            lambda value: value["prohibited_promotions"].remove("self_edit_commit")
        )

    def test_rejects_authoritative_skill_gap(self) -> None:
        self.assert_rejected(
            lambda value: value["fysa_120"]["proposed_gap"].__setitem__("authoritative", True)
        )

    def test_rejects_duplicate_json_keys(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "profile.json"
            path.write_text('{"profile_id":"one","profile_id":"two"}', encoding="utf-8")
            with self.assertRaises(ValueError):
                load_profile(path)

    def test_rejects_non_finite_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "profile.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            with self.assertRaises(ValueError):
                load_profile(path)

    def test_guide_contains_unadmitted_status_and_prose_equivalent(self) -> None:
        text = GUIDE_PATH.read_text(encoding="utf-8")
        self.assertIn(EXPECTED_STATUS, text)
        self.assertIn("### Prose equivalent", text)

    def test_coordination_route_fails_when_boundary_is_removed(self) -> None:
        errors = validate_coordination_routes(
            {GUIDE_PATH: ("A declaration is not a demonstration", "missing-boundary-marker")}
        )
        self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
