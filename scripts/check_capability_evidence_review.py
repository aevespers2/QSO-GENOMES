#!/usr/bin/env python3
"""Validate the documentation-only capability evidence and self-edit review packet."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "docs/capability-evidence-and-self-edit-review-v1.json"
GUIDE_PATH = ROOT / "docs/capability-evidence-and-self-edit-review.md"
EXPECTED_PROFILE_ID = "QSO-GENOMES-CAPABILITY-EVIDENCE-SELF-EDIT-REVIEW-001"
EXPECTED_STATUS = "DOCUMENTED_NOT_ADMITTED"
EXPECTED_GAP = "031-T"
SHA40 = re.compile(r"^[0-9a-f]{40}$")

EXPECTED_LEVELS = [
    "DECLARED",
    "STRUCTURALLY_VALID",
    "FIXTURE_DEMONSTRATED",
    "BENCHMARK_DEMONSTRATED",
    "INDEPENDENTLY_REPRODUCED",
    "ADMISSION_ELIGIBLE",
    "OPERATIONALLY_ADMITTED",
    "RESULTING_STATE_VERIFIED",
]
EXPECTED_HEADS = {
    "1259693433814129f44d0255b5e0ecf741d9a79b",
    "622530232248a8df8c24c91ed09ce58f66988e63",
    "992d8263bf62666fd6a05152cc0f6ad16791706c",
    "73f481bb5bd6cd55a681a047a0c571bce048d033",
}
EXPECTED_DISPOSITIONS = {
    "approved_for_external_admission_review",
    "revise",
    "rejected",
    "withdrawn",
    "superseded",
}
EXPECTED_GATES = {
    "CANONICAL_COMPATIBILITY_HEAD",
    "APPROVED_IDENTITY_AND_ALIAS_MIGRATION",
    "IMMUTABLE_POLICY_EXACT_BINDING",
    "MUTABLE_FIELD_SCHEMA_AUTHORITY",
    "COMPLETE_DELTA_AND_DRIFT_ACCOUNTING",
    "HOSTILE_FIXTURES",
    "INDEPENDENT_REPRODUCTION",
    "SECURITY_PRIVACY_ETHICS_COMPATIBILITY_REVIEW",
    "EXTERNAL_HUMAN_DISPOSITION",
    "SEPARATE_OPERATIONAL_ADMISSION",
    "ROLLBACK_TARGET_AND_REHEARSAL",
    "RESULTING_STATE_VERIFICATION",
}
EXPECTED_CATEGORIES = {
    "CAT-011",
    "CAT-012",
    "CAT-013",
    "CAT-017",
    "CAT-018",
    "CAT-019",
    "CAT-031",
    "CAT-040",
}

REQUIRED_GUIDE_PHRASES = (
    EXPECTED_STATUS,
    "A declaration is not a demonstration",
    "A genome cannot approve, commit, activate, or canonicalize its own self-edit",
    "Class A — ordinary bounded mutable-field adjustment",
    "Class B — versioned migration",
    "Class C — immutable-policy or forbidden-capability change",
    "Class D — authority-bearing or operational change",
    "Required self-edit packet",
    "Immutable ethics and safety review",
    "Declared versus demonstrated capability map",
    "### Prose equivalent",
    "031-T — Declared-versus-demonstrated capability evidence and bounded self-edit conformance",
)

COORDINATION_REQUIREMENTS = {
    ROOT / "taskchain.md": (
        "A genome is data.",
        "declarative validity",
        "operational admission",
        "runtime projection",
    ),
    ROOT / "punchlist.md": (
        "Prove a genome or Sprite cannot issue credentials",
        "local validity and neutral conformance never imply operational admission",
        "Every claim is tied to an immutable commit and reproducible evidence",
    ),
    ROOT / "release.md": (
        "A genome or Sprite may constrain operational behavior but cannot itself grant credentials",
        "Declarative validity",
        "Operational admission",
        "Runtime projection and execution",
    ),
    ROOT / "changelog.md": (
        "These changes are candidate evidence, not accepted capability",
        "Documentation remains explanatory and review-oriented",
    ),
    ROOT / "mkdocs.yml": (
        "Capability evidence and self-edit review: capability-evidence-and-self-edit-review.md",
    ),
}


def reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON value prohibited: {value}")


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_profile(path: Path = PROFILE_PATH) -> dict[str, Any]:
    raw = path.read_bytes().decode("utf-8", errors="strict")
    value = json.loads(
        raw,
        object_pairs_hook=reject_duplicate_keys,
        parse_constant=reject_constant,
    )
    if not isinstance(value, dict):
        raise ValueError("profile root must be an object")
    return value


def validate_profile(profile: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if profile.get("profile_id") != EXPECTED_PROFILE_ID:
        errors.append("unexpected profile_id")
    if profile.get("version") != 1:
        errors.append("version must be 1")
    if profile.get("status") != EXPECTED_STATUS:
        errors.append("status must remain documented but not admitted")
    if profile.get("authority_effect") != "none":
        errors.append("authority_effect must remain none")

    generations = profile.get("observed_generations")
    if not isinstance(generations, list) or len(generations) != 4:
        errors.append("exactly four observed generations are required")
    else:
        heads: set[str] = set()
        pull_requests: set[int] = set()
        for index, generation in enumerate(generations):
            if not isinstance(generation, dict):
                errors.append(f"observed generation {index} must be an object")
                continue
            head = generation.get("head")
            if not isinstance(head, str) or not SHA40.fullmatch(head):
                errors.append(f"invalid exact head at observed generation {index}")
            else:
                heads.add(head)
            pr = generation.get("pull_request")
            if not isinstance(pr, int):
                errors.append(f"invalid pull request at observed generation {index}")
            else:
                pull_requests.add(pr)
            if generation.get("repository") != "aevespers2/QSO-GENOMES":
                errors.append("observed repository must remain QSO-GENOMES")
        if heads != EXPECTED_HEADS:
            errors.append("observed exact-head set changed")
        if pull_requests != {2, 12, 14, 15}:
            errors.append("observed pull-request set changed")

    if profile.get("evidence_levels") != EXPECTED_LEVELS:
        errors.append("evidence ladder must remain complete and ordered")

    self_edit_classes = profile.get("self_edit_classes")
    if not isinstance(self_edit_classes, dict) or set(self_edit_classes) != {"A", "B", "C", "D"}:
        errors.append("self-edit classes A through D are required")

    required_sections = profile.get("required_packet_sections")
    if not isinstance(required_sections, list) or set(required_sections) != {
        "source", "changes", "evidence", "impact", "rollback", "disposition"
    }:
        errors.append("self-edit packet sections are incomplete")

    boundaries = profile.get("immutable_review_boundaries")
    required_boundaries = {
        "immutable_policy_not_genome_writable",
        "forbidden_capabilities_not_genome_writable",
        "no_self_approval",
        "no_self_admission",
        "no_self_activation",
        "no_emotional_vulnerability_exploitation",
        "unknown_conflicting_stale_or_replayed_evidence_fails_closed",
    }
    if not isinstance(boundaries, list) or not required_boundaries.issubset(set(boundaries)):
        errors.append("immutable review boundaries are incomplete")

    dispositions = profile.get("dispositions")
    if not isinstance(dispositions, list) or set(dispositions) != EXPECTED_DISPOSITIONS:
        errors.append("review dispositions are incomplete")

    gates = profile.get("acceptance_gates")
    if not isinstance(gates, list) or set(gates) != EXPECTED_GATES:
        errors.append("acceptance gates are incomplete or changed")

    prohibited = profile.get("prohibited_promotions")
    required_prohibited = {
        "self_edit_commit",
        "self_approval",
        "operational_admission",
        "capability_issuance",
        "runtime_activation",
        "canonical_acceptance",
        "release",
        "deployment",
        "credential_change",
        "infrastructure_apply",
        "destructive_history_rewrite",
    }
    if not isinstance(prohibited, list) or not required_prohibited.issubset(set(prohibited)):
        errors.append("prohibited promotions are incomplete")

    fysa = profile.get("fysa_120")
    if not isinstance(fysa, dict):
        errors.append("FYSA-120 mapping is required")
    else:
        categories = fysa.get("categories")
        if not isinstance(categories, list) or set(categories) != EXPECTED_CATEGORIES:
            errors.append("FYSA-120 categories are incomplete")
        gap = fysa.get("proposed_gap")
        if not isinstance(gap, dict) or gap.get("id") != EXPECTED_GAP or gap.get("authoritative") is not False:
            errors.append("proposed FYSA-120 gap must remain non-authoritative 031-T")

    return errors


def validate_guide(path: Path = GUIDE_PATH) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors = [
        f"guide missing required phrase: {phrase}"
        for phrase in REQUIRED_GUIDE_PHRASES
        if phrase not in text
    ]
    if text.count("```mermaid") != 1:
        errors.append("guide must contain exactly one Mermaid graph")
    if "| Atlas |" not in text or "| Nova |" not in text or "| Orion |" not in text or "| Lyra |" not in text:
        errors.append("guide must include all four genome review prompts")
    return errors


def validate_coordination_routes(requirements: dict[Path, tuple[str, ...]] = COORDINATION_REQUIREMENTS) -> list[str]:
    errors: list[str] = []
    for path, phrases in requirements.items():
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"cannot read controlled route {path.relative_to(ROOT)}: {exc}")
            continue
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"controlled route {path.relative_to(ROOT)} missing phrase: {phrase}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submitted-sha", default=None)
    args = parser.parse_args()

    errors: list[str] = []
    try:
        profile = load_profile()
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        errors.append(f"invalid profile: {exc}")
    else:
        errors.extend(validate_profile(profile))
    try:
        errors.extend(validate_guide())
    except (OSError, UnicodeError) as exc:
        errors.append(f"invalid guide: {exc}")
    errors.extend(validate_coordination_routes())

    report = {
        "profile_id": EXPECTED_PROFILE_ID,
        "status": "PASS" if not errors else "FAIL",
        "submitted_sha": args.submitted_sha,
        "disposition": EXPECTED_STATUS,
        "authority_effect": "none",
        "errors": errors,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
