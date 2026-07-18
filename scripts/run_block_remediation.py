#!/usr/bin/env python3
"""Run allow-listed QSO remediation checks from a block receipt.

This tool never writes genome artifacts, changes immutable ethics, commits, pushes,
or merges. It converts a blocking review decision into deterministic local checks
and a machine-readable remediation report for human review.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "governance" / "block-remediation-registry.json"
REPORT_PATH = ROOT / "reports" / "block-remediation-result.json"
ALLOWED_AUTHORITIES = {"jacob_redmond", "aequitas"}
ALLOWED_DECISIONS = {"block_pending_review", "reject"}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def validate_receipt(receipt: dict[str, Any], registry: dict[str, Any]) -> list[str]:
    required = {
        "authority_id",
        "decision",
        "block_codes",
        "reviewer_id",
        "input_sha256",
        "rationale",
    }
    missing = sorted(required - receipt.keys())
    if missing:
        raise ValueError(f"missing receipt fields: {', '.join(missing)}")
    if receipt["authority_id"] not in ALLOWED_AUTHORITIES:
        raise ValueError("authority_id must be jacob_redmond or deprecated alias aequitas")
    if receipt["decision"] not in ALLOWED_DECISIONS:
        raise ValueError("decision must be block_pending_review or reject")
    if not isinstance(receipt["block_codes"], list) or not receipt["block_codes"]:
        raise ValueError("block_codes must be a non-empty list")
    if not all(isinstance(code, str) and code for code in receipt["block_codes"]):
        raise ValueError("every block code must be a non-empty string")
    if not isinstance(receipt["input_sha256"], str) or len(receipt["input_sha256"]) != 64:
        raise ValueError("input_sha256 must be a 64-character digest")
    unknown = sorted(set(receipt["block_codes"]) - set(registry["rules"]))
    if unknown:
        raise ValueError(f"unknown block codes: {', '.join(unknown)}")
    return list(dict.fromkeys(receipt["block_codes"]))


def run_command(command: list[str]) -> dict[str, Any]:
    started = datetime.now(timezone.utc)
    process = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=300,
    )
    return {
        "command": command,
        "exit_code": process.returncode,
        "stdout": process.stdout[-20000:],
        "stderr": process.stderr[-20000:],
        "started_at": started.isoformat(),
        "finished_at": datetime.now(timezone.utc).isoformat(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", required=True, type=Path)
    parser.add_argument("--registry", type=Path, default=REGISTRY_PATH)
    parser.add_argument("--report", type=Path, default=REPORT_PATH)
    args = parser.parse_args()

    registry = load_json(args.registry)
    receipt = load_json(args.receipt)
    block_codes = validate_receipt(receipt, registry)

    commands: list[list[str]] = []
    for code in block_codes:
        for command in registry["rules"][code]["commands"]:
            if command not in commands:
                commands.append(command)

    results = [run_command(command) for command in commands]
    passed = all(result["exit_code"] == 0 for result in results)
    normalized_authority = (
        "jacob_redmond" if receipt["authority_id"] == "aequitas" else receipt["authority_id"]
    )
    report = {
        "report_version": 1,
        "authority_id": normalized_authority,
        "authority_alias_received": receipt["authority_id"],
        "decision": receipt["decision"],
        "block_codes": block_codes,
        "receipt_sha256": hashlib.sha256(canonical_bytes(receipt)).hexdigest(),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checks_passed": passed,
        "external_commit_authorized": False,
        "human_review_required": True,
        "results": results,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_bytes(canonical_bytes(report) + b"\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print(f"block remediation failed closed: {exc}", file=sys.stderr)
        raise SystemExit(2)
