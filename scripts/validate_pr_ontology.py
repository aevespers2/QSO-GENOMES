#!/usr/bin/env python3
"""Validate a pull request's ontology declaration and derive required controls."""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY_PATH = ROOT / "governance" / "pr-ontology.json"
REQUIRED_FIELDS = {
    "category",
    "subtype",
    "layer",
    "system",
    "authority",
    "lifecycle",
    "risk_classes",
    "affected_invariants",
    "evidence",
    "non_goals",
}


def fail(message: str) -> None:
    print(f"PR ontology validation: FAIL — {message}", file=sys.stderr)
    raise SystemExit(1)


def extract_declaration(body: str) -> dict:
    match = re.search(r"```pr-ontology\s*(\{.*?\})\s*```", body, re.DOTALL)
    if not match:
        fail("missing fenced `pr-ontology` JSON declaration")
    try:
        value = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        fail(f"invalid ontology JSON: {exc}")
    if not isinstance(value, dict):
        fail("ontology declaration must be a JSON object")
    return value


def main() -> None:
    ontology = json.loads(ONTOLOGY_PATH.read_text(encoding="utf-8"))
    event_path = os.getenv("GITHUB_EVENT_PATH")
    if event_path:
        event = json.loads(Path(event_path).read_text(encoding="utf-8"))
        body = (event.get("pull_request") or {}).get("body") or ""
        head_sha = (event.get("pull_request") or {}).get("head", {}).get("sha")
    else:
        body = os.getenv("PR_BODY", "")
        head_sha = os.getenv("PR_HEAD_SHA")

    declaration = extract_declaration(body)
    missing = sorted(REQUIRED_FIELDS - declaration.keys())
    if missing:
        fail(f"missing required fields: {', '.join(missing)}")

    category = declaration["category"]
    if category not in ontology["categories"]:
        fail(f"unknown category: {category}")
    if declaration["layer"] not in ontology["layers"]:
        fail(f"unknown layer: {declaration['layer']}")
    if declaration["authority"] not in ontology["authorities"]:
        fail(f"unknown authority: {declaration['authority']}")
    if declaration["lifecycle"] not in ontology["lifecycles"]:
        fail(f"unknown lifecycle: {declaration['lifecycle']}")

    for field in ("risk_classes", "affected_invariants", "evidence", "non_goals"):
        if not isinstance(declaration[field], list) or not declaration[field]:
            fail(f"{field} must be a non-empty array")
        if len(declaration[field]) != len(set(declaration[field])):
            fail(f"{field} must not contain duplicates")

    required_controls = ontology["categories"][category]
    declared_controls = declaration.get("controls", {})
    if not isinstance(declared_controls, dict):
        fail("controls must be an object keyed by control ID")
    absent = [control for control in required_controls if control not in declared_controls]
    if absent:
        fail("missing required control dispositions: " + ", ".join(absent))

    invalid_states = []
    allowed_states = {"pass", "planned", "not-applicable", "blocked"}
    for control in required_controls:
        item = declared_controls[control]
        if not isinstance(item, dict) or item.get("status") not in allowed_states:
            invalid_states.append(control)
        if not item.get("evidence") and item.get("status") in {"pass", "not-applicable"}:
            invalid_states.append(control)
    if invalid_states:
        fail("invalid or unsupported control disposition: " + ", ".join(sorted(set(invalid_states))))

    if declaration["lifecycle"] in {"accepted", "released", "deployed"}:
        incomplete = [c for c in required_controls if declared_controls[c]["status"] != "pass"]
        if incomplete:
            fail("accepted/released/deployed changes require PASS for: " + ", ".join(incomplete))

    output = {
        "head_sha": head_sha,
        "category": category,
        "required_controls": required_controls,
        "declaration": declaration,
    }
    output_path = Path(os.getenv("PR_ONTOLOGY_OUTPUT", "pr-ontology-report.json"))
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PR ontology validation: PASS — {category}; {len(required_controls)} controls derived")


if __name__ == "__main__":
    main()
