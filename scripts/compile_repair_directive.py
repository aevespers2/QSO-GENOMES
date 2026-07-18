#!/usr/bin/env python3
"""Compile reports and review comments into a bounded repair directive."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

MECHANISMS = {
    "provenance": ["provenance", "ancestor", "reachable", "digest", "sha", "chain-of-custody"],
    "manifest": ["manifest", "canonical", "identity", "artifact set", "set_sha256"],
    "schema": ["schema", "duplicate key", "non-finite", "required artifact"],
    "ethics": ["immutable ethics", "aequitas", "jacob elias redmond", "oversight", "review authority"],
    "workflow": ["workflow", "github actions", "checkout", "permissions", "exact head", "ci"],
    "migration": ["migration", "legacy", "alias", "compatibility", "deprecation"],
    "security": ["vulnerability", "path traversal", "symlink", "credential", "network", "injection"],
    "release_state": ["release", "candidate", "accepted", "deployed", "status contradiction"],
}

FILE_RE = re.compile(r"(?<![\w.-])(?:[\w.-]+/)+[\w.-]+(?:\.[A-Za-z0-9_-]+)?")


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def classify(text: str) -> list[str]:
    lowered = text.lower()
    return [name for name, terms in MECHANISMS.items() if any(term in lowered for term in terms)] or ["general_integrity"]


def exact_locations(text: str) -> list[str]:
    locations = sorted(set(FILE_RE.findall(text)))
    return [item for item in locations if not item.startswith("http")][:50]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    source = json.loads(args.input.read_text(encoding="utf-8"))
    text_parts = [
        str(source.get("report", "")),
        str(source.get("review_body", "")),
        "\n".join(str(x) for x in source.get("comments", [])),
    ]
    text = "\n".join(text_parts).strip()
    if not text:
        raise ValueError("repair source contains no report or review text")

    classes = classify(text)
    locations = exact_locations(text)
    source_digest = hashlib.sha256(canonical_bytes(source)).hexdigest()

    implementation_actions = []
    tests = []
    for finding in classes:
        implementation_actions.append(f"Repair the {finding} mechanism without weakening existing invariants.")
        tests.append(f"Add one positive and one negative regression test for {finding}.")

    directive = {
        "directive_version": 1,
        "team_id": "qso-report-repair-team-v1",
        "source_pr": source.get("pull_request_number"),
        "source_head_sha": source.get("head_sha"),
        "source_evidence_digest": source_digest,
        "finding_class": classes,
        "accepted_comments": source.get("accepted_comments", source.get("comments", [])),
        "rejected_or_stale_comments": source.get("rejected_or_stale_comments", []),
        "affected_invariants": [
            "truthful-lifecycle",
            "provenance-continuity",
            "least-privilege",
            "human-final-approval",
        ],
        "exact_code_locations": locations,
        "implementation_actions": implementation_actions,
        "test_plan": tests + [
            "Run the complete repository conformance suite on the exact repair head.",
            "Retain logs and bind them to the repair commit digest.",
        ],
        "migration_effects": "Preserve legacy identifiers and historical receipts; use explicit versioned aliases where identities change.",
        "rollback_plan": "Revert the isolated repair commit or close the draft repair PR without changing the source PR history.",
        "reevaluation_criteria": [
            "Every accepted comment is answered by code or an evidence-backed disposition.",
            "Original failing checks pass on the exact repair head.",
            "No new high or critical findings are introduced.",
            "Michael Aaron Redmond can reconcile the repair branch without history rewriting.",
        ],
        "human_review_requirement": {
            "review_authority_id": "jacob_elias_redmond",
            "human_final_approval_required": True,
            "automatic_final_merge": False,
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(canonical_bytes(directive) + b"\n")
    print(json.dumps(directive, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
