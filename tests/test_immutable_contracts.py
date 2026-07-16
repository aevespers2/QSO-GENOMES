import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "contracts" / "immutable-baseline.json"
GENOMES_DIR = ROOT / "genomes"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class ImmutableContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract = load_json(CONTRACT_PATH)
        cls.genomes = {
            path.stem: load_json(path)
            for path in sorted(GENOMES_DIR.glob("*.json"))
        }

    def test_expected_genome_set_is_complete(self) -> None:
        self.assertEqual(set(self.contract["applies_to"]), set(self.genomes))
        for filename_id, genome in self.genomes.items():
            self.assertEqual(filename_id, genome["genome_id"])

    def test_immutable_shape_and_shared_ethics(self) -> None:
        required_shared = set(self.contract["required_shared_ethics"])
        required_prefixes = self.contract["required_ethics_prefixes"]
        expected_keys = set(self.contract["expected_immutable_keys"])
        expected_count = self.contract["expected_ethics_entry_count"]

        for genome_id, genome in self.genomes.items():
            with self.subTest(genome=genome_id):
                immutable = genome["immutable"]
                ethics = immutable["ethics"]
                self.assertEqual(expected_keys, set(immutable))
                self.assertEqual(expected_count, len(ethics))
                self.assertEqual(len(ethics), len(set(ethics)))
                self.assertTrue(required_shared.issubset(ethics))
                for prefix in required_prefixes:
                    matches = [entry for entry in ethics if entry.startswith(prefix)]
                    self.assertEqual(1, len(matches), msg=f"{genome_id}: {prefix!r}")

    def test_forbidden_capabilities_are_identical_and_complete(self) -> None:
        expected = self.contract["required_forbidden_capabilities"]
        self.assertEqual(len(expected), len(set(expected)))
        for genome_id, genome in self.genomes.items():
            with self.subTest(genome=genome_id):
                actual = genome["immutable"]["forbidden_capabilities"]
                self.assertEqual(expected, actual)
                self.assertEqual(len(actual), len(set(actual)))

    def test_identity_contract_is_identical(self) -> None:
        expected = self.contract["required_identity"]
        for genome_id, genome in self.genomes.items():
            with self.subTest(genome=genome_id):
                self.assertEqual(expected, genome["immutable"]["identity"])

    def test_safety_priority_is_identical(self) -> None:
        expected = self.contract["required_safety_priority"]
        for genome_id, genome in self.genomes.items():
            with self.subTest(genome=genome_id):
                self.assertEqual(expected, genome["immutable"]["safety_priority"])


if __name__ == "__main__":
    unittest.main()
