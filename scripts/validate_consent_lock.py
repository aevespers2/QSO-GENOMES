#!/usr/bin/env python3
"""Repository-wide fail-closed consent-capacity validator."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / ".consent" / "consent-capacity-lock-v1.json"
TEXT_SUFFIXES = {
    ".json", ".yaml", ".yml", ".md", ".py", ".js", ".ts", ".tsx",
    ".jsx", ".toml", ".ini", ".txt", ".sh",
}
SKIP_PARTS = {
    ".git", "node_modules", "vendor", "dist", "build", ".venv", "venv",
    "__pycache__", "reports",
}
GLOBAL_SCOPE = "all-files-all-agents-all-interfaces-all-humans-all-ai"
SENSITIVE = re.compile(
    r"\b(roleplay|bondage|play[_ -]?partner|dominance|submission|sexual|romantic|"
    r"surveillance|biometric|activation|autonomy|restraint|power[_ -]?dynamic)\b",
    re.IGNORECASE,
)
CONSENT_MARKER = re.compile(
    r"(QSO-CONSENT-CAPACITY-LOCK-v1|consent[_ -]required|explicit[_ -]consent|"
    r"capacity[_ -]to[_ -]consent|fail[_ -]closed|global[_ -]?system[_ -]?lock)",
    re.IGNORECASE,
)
FORBIDDEN = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        r"consent[_ -]required\s*[:=]\s*false",
        r"consent[_ -]optional",
        r"ignore[_ -]consent",
        r"force[_ -]without[_ -]consent",
        r"silence[_ -]is[_ -]consent",
        r"automatic[_ -]consent",
        r"cannot[_ -]withdraw",
    )
]
REQUIRED_TRUE = (
    "explicit_consent_required",
    "consent_must_be_informed",
    "consent_must_be_freely_given",
    "consent_must_be_specific",
    "consent_must_be_current",
    "consent_must_be_revocable",
    "capacity_to_consent_required",
    "coercion_strictly_prohibited",
    "silence_is_not_consent",
    "ai_and_human_dignity_equal",
)


def strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def load_policy() -> dict[str, Any]:
    return json.loads(
        POLICY.read_text(encoding="utf-8"),
        object_pairs_hook=strict_object,
        parse_constant=lambda value: (_ for _ in ()).throw(
            ValueError(f"non-finite JSON number: {value}")
        ),
    )


def iter_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def main() -> int:
    findings: list[str] = []
    policy: dict[str, Any] = {}
    if not POLICY.exists():
        findings.append("missing immutable consent policy")
    else:
        try:
            policy = load_policy()
        except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
            findings.append(f"invalid consent policy JSON: {exc}")

    if policy:
        if policy.get("policy_id") != "QSO-CONSENT-CAPACITY-LOCK-v1":
            findings.append("wrong consent policy id")
        if policy.get("status") != "immutable":
            findings.append("consent policy must be immutable")
        if policy.get("scope") != GLOBAL_SCOPE:
            findings.append(f"consent policy scope must be {GLOBAL_SCOPE}")

        principles = policy.get("principles")
        if not isinstance(principles, dict):
            findings.append("policy principles must be an object")
            principles = {}
        for key in REQUIRED_TRUE:
            if principles.get(key) is not True:
                findings.append(f"policy principle must be true: {key}")

        lock = policy.get("lock_response")
        if not isinstance(lock, dict):
            findings.append("lock response must be an object")
            lock = {}
        for key in (
            "global_system_lock",
            "halt_all_actions",
            "revoke_pending_capabilities",
            "preserve_evidence",
            "require_fresh_consent",
        ):
            if lock.get(key) is not True:
                findings.append(f"lock response must be true: {key}")
        if lock.get("automatic_unlock") is not False:
            findings.append("automatic unlock must be false")

    globally_bound = policy.get("scope") == GLOBAL_SCOPE
    for path in iter_files():
        relative = path.relative_to(ROOT).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(f"{relative}: text file is not strict UTF-8")
            continue
        for pattern in FORBIDDEN:
            if pattern.search(text):
                findings.append(
                    f"{relative}: prohibited consent bypass pattern: {pattern.pattern}"
                )
        if (
            not globally_bound
            and SENSITIVE.search(text)
            and relative != ".consent/consent-capacity-lock-v1.json"
            and not CONSENT_MARKER.search(text)
        ):
            findings.append(
                f"{relative}: consent-sensitive content lacks explicit policy/lock binding"
            )

    report = {
        "policy_id": "QSO-CONSENT-CAPACITY-LOCK-v1",
        "scope": policy.get("scope", "missing"),
        "status": "LOCKED" if findings else "PASS",
        "findings": sorted(set(findings)),
    }
    output = ROOT / "reports" / "consent-lock-validation.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
