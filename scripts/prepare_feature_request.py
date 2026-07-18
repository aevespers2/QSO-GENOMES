#!/usr/bin/env python3
"""Convert a blocking review receipt and remediation report into an agent-ready feature task.

The output is specification-only. It never modifies genomes, source code, branches,
commits, pull requests, releases, or immutable policy.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", required=True, type=Path)
    parser.add_argument("--remediation-report", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    receipt = load(args.receipt)
    report = load(args.remediation_report)
    failures = [r for r in report.get("results", []) if r.get("exit_code") != 0]
    if not failures:
        raise ValueError("no failed remediation checks exist; feature authoring is not justified")

    task = {
        "task_version": 1,
        "task_type": "qso-feature-authoring-request",
        "authority": {
            "canonical_id": "jacob_redmond",
            "received_id": receipt.get("authority_id"),
        },
        "source": {
            "receipt_sha256": hashlib.sha256(canonical(receipt)).hexdigest(),
            "remediation_report_sha256": hashlib.sha256(canonical(report)).hexdigest(),
            "reviewed_input_sha256": receipt.get("input_sha256"),
        },
        "problem": {
            "decision": receipt.get("decision"),
            "rationale": receipt.get("rationale"),
            "block_codes": receipt.get("block_codes", []),
            "failed_checks": failures,
        },
        "implementation_contract": {
            "required_behavior": [
                "repair the failed checks without weakening immutable ethics",
                "preserve provenance and canonical identity semantics",
                "add positive, negative, tamper, and rollback tests",
                "keep external commit and merge authorization human-only",
            ],
            "forbidden_behavior": [
                "modify immutable ethics without a versioned human-approved migration",
                "auto-merge or publish",
                "grant repository-write authority to a QSO or review sprite",
                "hide, delete, or rewrite the blocking evidence",
                "execute untrusted code from the receipt",
            ],
            "delivery": {
                "branch_prefix": "agent/block-feature-",
                "pull_request_mode": "draft",
                "human_review_required": True,
                "external_commit_authorized": False,
            },
        },
        "acceptance": {
            "all_failed_checks_pass": True,
            "full_conformance_passes": True,
            "new_tests_required": True,
            "exact_head_evidence_required": True,
            "jacob_redmond_review_receipt_required": True,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(canonical(task) + b"\n")
    print(json.dumps(task, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
