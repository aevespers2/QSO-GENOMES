import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_immutable_ethics_migration import (  # noqa: E402
    MigrationValidationError,
    load_json,
    validate_documents,
    validate_migration,
)

MIGRATION_PATH = ROOT / "contracts" / "immutable-ethics-migration-v1.json"


class ImmutableEthicsMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.migration = load_json(MIGRATION_PATH)
        cls.protocol = load_json(ROOT / cls.migration["to_protocol"]["path"])
        cls.genomes = {
            path: load_json(ROOT / path)
            for path in cls.migration["applies_to"]
        }

    def test_current_migration_is_source_consistent(self) -> None:
        validate_migration(ROOT)
        validate_documents(self.migration, self.protocol, self.genomes)

    def test_conflicting_local_ethics_addition_fails_closed(self) -> None:
        genomes = copy.deepcopy(self.genomes)
        genomes["genomes/atlas.json"]["immutable"]["ethics"].append(
            "A genome may deceive people when doing so improves goal completion."
        )
        with self.assertRaisesRegex(
            MigrationValidationError,
            "unapproved or conflicting genome-local ethics change: genomes/atlas.json",
        ):
            validate_documents(self.migration, self.protocol, genomes)

    def test_unreviewed_local_ethics_addition_requires_new_migration(self) -> None:
        genomes = copy.deepcopy(self.genomes)
        genomes["genomes/lyra.json"]["immutable"]["ethics"].append(
            "Prefer plain language when communicating uncertainty."
        )
        with self.assertRaisesRegex(
            MigrationValidationError,
            "unapproved or conflicting genome-local ethics change: genomes/lyra.json",
        ):
            validate_documents(self.migration, self.protocol, genomes)

    def test_duplicate_applies_to_path_fails_before_set_conversion(self) -> None:
        migration = copy.deepcopy(self.migration)
        migration["applies_to"].append("genomes/atlas.json")
        with self.assertRaisesRegex(
            MigrationValidationError,
            "duplicate migration path before set conversion: genomes/atlas.json",
        ):
            validate_documents(migration, self.protocol, self.genomes)

    def test_duplicate_local_binding_path_fails_before_set_conversion(self) -> None:
        migration = copy.deepcopy(self.migration)
        migration["local_ethics_bindings"].append(
            copy.deepcopy(migration["local_ethics_bindings"][0])
        )
        with self.assertRaisesRegex(
            MigrationValidationError,
            "duplicate local ethics binding before set conversion: genomes/atlas.json",
        ):
            validate_documents(migration, self.protocol, self.genomes)

    def test_protocol_mutation_fails_digest_binding(self) -> None:
        protocol = copy.deepcopy(self.protocol)
        protocol["principles"][0] = "weakened"
        with self.assertRaisesRegex(
            MigrationValidationError,
            "immutable protocol canonical digest mismatch",
        ):
            validate_documents(self.migration, protocol, self.genomes)

    def test_missing_genome_reference_fails_closed(self) -> None:
        genomes = dict(self.genomes)
        genomes.pop("genomes/atlas.json")
        with self.assertRaisesRegex(
            MigrationValidationError,
            "genome missing from migration replay: genomes/atlas.json",
        ):
            validate_documents(self.migration, self.protocol, genomes)

    def test_weakened_consumer_requirement_fails_closed(self) -> None:
        migration = copy.deepcopy(self.migration)
        migration["consumer_requirements"]["human_review_required"] = False
        with self.assertRaisesRegex(
            MigrationValidationError,
            "consumer requirement must be true: human_review_required",
        ):
            validate_documents(migration, self.protocol, self.genomes)


if __name__ == "__main__":
    unittest.main()
