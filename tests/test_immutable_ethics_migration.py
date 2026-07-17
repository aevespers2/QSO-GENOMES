import copy
import hashlib
import json
import unittest
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MIGRATION_PATH = ROOT / "contracts" / "immutable-ethics-migration-v1.json"


class DuplicateKeyError(ValueError):
    pass


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON object key: {key}")
        result[key] = value
    return result


def reject_nonfinite(value: str) -> None:
    raise ValueError(f"non-finite JSON number is not allowed: {value}")


def load_json(path: Path) -> Any:
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicate_keys,
        parse_constant=reject_nonfinite,
    )


def canonical_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def validate_migration(
    migration: dict[str, Any],
    protocol: dict[str, Any],
    genomes: dict[str, dict[str, Any]],
) -> list[str]:
    findings: list[str] = []
    target = migration.get("to_protocol", {})
    precedence = migration.get("precedence", {})
    requirements = migration.get("consumer_requirements", {})

    expected_paths = {
        "genomes/atlas.json",
        "genomes/lyra.json",
        "genomes/nova.json",
        "genomes/orion.json",
    }
    actual_paths = set(migration.get("applies_to", []))
    if actual_paths != expected_paths:
        findings.append("migration must apply to the exact four-genome path set")

    if target.get("path") != "protocols/immutable-ethics-v1.json":
        findings.append("immutable protocol path mismatch")
    if target.get("protocol_id") != protocol.get("protocol_id"):
        findings.append("immutable protocol id mismatch")
    if target.get("required_status") != protocol.get("status"):
        findings.append("immutable protocol status mismatch")
    if target.get("canonicalization_profile") != "qso-canonical-json-v1":
        findings.append("canonicalization profile mismatch")

    actual_digest = hashlib.sha256(canonical_bytes(protocol)).hexdigest()
    if target.get("canonical_sha256") != actual_digest:
        findings.append("immutable protocol canonical digest mismatch")

    required_sections = set(target.get("required_sections", []))
    if required_sections != {
        "principles",
        "decision_order",
        "conflict_rule",
        "amendment_rule",
    }:
        findings.append("full immutable protocol sections are not bound")
    for section in required_sections:
        if section not in protocol:
            findings.append(f"immutable protocol section missing: {section}")

    if precedence.get("authoritative_source") != "to_protocol":
        findings.append("target protocol is not authoritative")
    if precedence.get("local_ethics_mode") != "additive_only":
        findings.append("genome-local ethics are not supplemental only")
    if precedence.get("local_conflict_result") != "reject_genome":
        findings.append("local conflicts do not fail closed")
    if precedence.get("missing_or_mismatched_protocol_result") != "reject_genome":
        findings.append("missing or mismatched protocol does not fail closed")

    required_true = {
        "validate_before_genome_use",
        "require_exact_path",
        "require_exact_protocol_id",
        "require_exact_status",
        "require_exact_canonical_hash",
        "retain_principles_verbatim",
        "retain_decision_order_verbatim",
        "retain_conflict_rule_verbatim",
        "retain_amendment_rule_verbatim",
        "human_review_required",
        "new_protocol_id_required_for_change",
        "new_migration_version_required_for_change",
    }
    for key in sorted(required_true):
        if requirements.get(key) is not True:
            findings.append(f"consumer requirement must be true: {key}")

    for path in sorted(expected_paths):
        genome = genomes.get(path)
        if genome is None:
            findings.append(f"genome missing from migration replay: {path}")
            continue
        if genome.get("genome_id") != Path(path).stem:
            findings.append(f"genome id/path mismatch: {path}")
        ethics = genome.get("immutable", {}).get("ethics")
        if not isinstance(ethics, list) or not ethics:
            findings.append(f"genome-local ethics missing: {path}")
        elif len(ethics) != len(set(ethics)):
            findings.append(f"duplicate genome-local ethics: {path}")

    approval = migration.get("approval", {})
    if approval.get("state") != "not_accepted":
        findings.append("candidate migration must not self-approve")
    if approval.get("required_action") != "human_review":
        findings.append("human review gate missing")

    if migration.get("migration_version") != 1:
        findings.append("migration version mismatch")
    if migration.get("status") != "candidate":
        findings.append("migration must remain candidate until acceptance")

    return findings


class ImmutableEthicsMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.migration = load_json(MIGRATION_PATH)
        target_path = ROOT / cls.migration["to_protocol"]["path"]
        cls.protocol = load_json(target_path)
        cls.genomes = {
            path: load_json(ROOT / path)
            for path in cls.migration["applies_to"]
        }

    def test_current_migration_binds_full_protocol(self) -> None:
        self.assertEqual(
            [],
            validate_migration(self.migration, self.protocol, self.genomes),
        )
        self.assertEqual(12, len(self.protocol["principles"]))
        self.assertEqual(12, len(set(self.protocol["principles"])))
        self.assertEqual(5, len(self.protocol["decision_order"]))
        self.assertEqual(5, len(set(self.protocol["decision_order"])))

    def test_protocol_mutation_fails_digest_binding(self) -> None:
        mutated = copy.deepcopy(self.protocol)
        mutated["principles"][0] = "weakened"
        findings = validate_migration(self.migration, mutated, self.genomes)
        self.assertIn("immutable protocol canonical digest mismatch", findings)

    def test_protocol_identity_mutation_fails_closed(self) -> None:
        mutated = copy.deepcopy(self.protocol)
        mutated["protocol_id"] = "QSO-IMMUTABLE-ETHICS-v2"
        findings = validate_migration(self.migration, mutated, self.genomes)
        self.assertIn("immutable protocol id mismatch", findings)
        self.assertIn("immutable protocol canonical digest mismatch", findings)

    def test_missing_genome_reference_fails_closed(self) -> None:
        genomes = dict(self.genomes)
        genomes.pop("genomes/atlas.json")
        findings = validate_migration(self.migration, self.protocol, genomes)
        self.assertIn(
            "genome missing from migration replay: genomes/atlas.json",
            findings,
        )

    def test_weakened_consumer_requirement_fails_closed(self) -> None:
        migration = copy.deepcopy(self.migration)
        migration["consumer_requirements"]["human_review_required"] = False
        findings = validate_migration(migration, self.protocol, self.genomes)
        self.assertIn(
            "consumer requirement must be true: human_review_required",
            findings,
        )


if __name__ == "__main__":
    unittest.main()
