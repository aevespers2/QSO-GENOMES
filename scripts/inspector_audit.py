#!/usr/bin/env python3
"""Random, reproducible PR ontology audits with escalation output."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import random
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY = json.loads((ROOT / "governance" / "pr-ontology.json").read_text(encoding="utf-8"))
TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "")
API = os.environ.get("GITHUB_API_URL", "https://api.github.com")
SAMPLE_SIZE = int(os.environ.get("INSPECTOR_SAMPLE_SIZE", "5"))
LOOKBACK_DAYS = int(os.environ.get("INSPECTOR_LOOKBACK_DAYS", "30"))


def request(path: str) -> Any:
    req = urllib.request.Request(
        f"{API}{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {TOKEN}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "portfolio-inspector-v1",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def extract(body: str) -> dict[str, Any] | None:
    match = re.search(r"```pr-ontology\s*(\{.*?\})\s*```", body or "", re.DOTALL)
    if not match:
        return None
    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError:
        return {"_invalid_json": True}
    return data if isinstance(data, dict) else {"_invalid_object": True}


def path_exists(path: str, ref: str) -> bool:
    try:
        request(f"/repos/{REPOSITORY}/contents/{path}?ref={ref}")
        return True
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return False
        raise


def successful_run_exists(head_sha: str) -> bool:
    runs = request(f"/repos/{REPOSITORY}/actions/runs?head_sha={head_sha}&per_page=100").get("workflow_runs", [])
    return any(run.get("head_sha") == head_sha and run.get("conclusion") == "success" for run in runs)


def reachable(commit_sha: str, head_sha: str) -> bool:
    try:
        result = request(f"/repos/{REPOSITORY}/compare/{commit_sha}...{head_sha}")
    except urllib.error.HTTPError:
        return False
    return result.get("status") in {"ahead", "identical"}


def evidence_items(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(item) for item in value]
    return []


def audit_pr(pr: dict[str, Any]) -> dict[str, Any]:
    number = pr["number"]
    head_sha = pr["head"]["sha"]
    declaration = extract(pr.get("body") or "")
    findings: list[dict[str, str]] = []

    if declaration is None:
        findings.append({"control": "ontology-presence", "detail": "Missing pr-ontology declaration."})
        return {"pr": number, "head_sha": head_sha, "findings": findings}
    if declaration.get("_invalid_json") or declaration.get("_invalid_object"):
        findings.append({"control": "ontology-validity", "detail": "Invalid pr-ontology declaration."})
        return {"pr": number, "head_sha": head_sha, "findings": findings}

    category = declaration.get("category")
    required = ONTOLOGY["categories"].get(category)
    if required is None:
        findings.append({"control": "ontology-category", "detail": f"Unknown category: {category!r}."})
        return {"pr": number, "head_sha": head_sha, "findings": findings}

    controls = declaration.get("controls") or {}
    for control in required:
        item = controls.get(control)
        if not isinstance(item, dict):
            findings.append({"control": control, "detail": "Required control disposition is missing."})
            continue
        status = item.get("status")
        if status not in {"pass", "planned", "not-applicable", "blocked"}:
            findings.append({"control": control, "detail": f"Unsupported status: {status!r}."})
            continue
        if status != "pass":
            continue

        evidence = evidence_items(item.get("evidence"))
        if not evidence:
            findings.append({"control": control, "detail": "PASS has no evidence."})
            continue

        for entry in evidence:
            path_match = re.fullmatch(r"(?:path:)?([A-Za-z0-9_./-]+)", entry.strip())
            if path_match and "/" in path_match.group(1):
                path = path_match.group(1)
                if not path_exists(path, head_sha):
                    findings.append({"control": control, "detail": f"Evidence path does not exist at head: {path}."})
            for sha in re.findall(r"\b[0-9a-f]{40}\b", entry.lower()):
                if not reachable(sha, head_sha):
                    findings.append({"control": control, "detail": f"Evidence commit is not reachable from head: {sha}."})

        if control == "exact-head-certification" and not successful_run_exists(head_sha):
            findings.append({"control": control, "detail": "PASS claimed without a successful workflow run on the exact PR head."})

    lifecycle = declaration.get("lifecycle")
    if lifecycle in {"accepted", "released", "deployed"}:
        incomplete = [c for c in required if (controls.get(c) or {}).get("status") != "pass"]
        if incomplete:
            findings.append({"control": "lifecycle-consistency", "detail": "Lifecycle exceeds evidence; incomplete controls: " + ", ".join(incomplete)})

    return {"pr": number, "head_sha": head_sha, "category": category, "findings": findings}


def main() -> None:
    if not TOKEN or not REPOSITORY:
        raise SystemExit("GITHUB_TOKEN and GITHUB_REPOSITORY are required")

    today = dt.datetime.now(dt.timezone.utc).date()
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=LOOKBACK_DAYS)
    seed_text = f"{REPOSITORY}:{today.isoformat()}"
    seed = int.from_bytes(hashlib.sha256(seed_text.encode()).digest()[:8], "big")

    candidates: list[dict[str, Any]] = []
    for state in ("open", "closed"):
        prs = request(f"/repos/{REPOSITORY}/pulls?state={state}&sort=updated&direction=desc&per_page=100")
        for pr in prs:
            updated = dt.datetime.fromisoformat(pr["updated_at"].replace("Z", "+00:00"))
            if state == "open" or updated >= cutoff:
                candidates.append(pr)

    unique = {pr["number"]: pr for pr in candidates}
    candidates = [pr for pr in unique.values() if extract(pr.get("body") or "") is not None]
    rng = random.Random(seed)
    sample = rng.sample(candidates, min(SAMPLE_SIZE, len(candidates))) if candidates else []
    audits = [audit_pr(pr) for pr in sample]
    finding_count = sum(len(item["findings"]) for item in audits)
    escalation = "none" if finding_count == 0 else "investigation" if finding_count < 3 else "control-system-rework"

    report = {
        "agent": "portfolio-inspector-v1",
        "repository": REPOSITORY,
        "audit_date_utc": today.isoformat(),
        "seed": seed_text,
        "sample_size_requested": SAMPLE_SIZE,
        "sampled_prs": [item["pr"] for item in audits],
        "finding_count": finding_count,
        "escalation": escalation,
        "audits": audits,
    }
    Path("inspector-audit-report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    Path("inspector-escalation.txt").write_text(escalation + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    if finding_count:
        raise SystemExit(2 if finding_count >= 3 else 1)


if __name__ == "__main__":
    main()
