from __future__ import annotations

import json
import unittest
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STRICT_TEXT_ROOTS = (
    ROOT / ".github" / "workflows",
    ROOT / "manifests",
)
STRUCTURED_ROOTS = (
    ROOT / "contracts",
    ROOT / "sprites",
    ROOT / "governance",
)
DISENGAGED = (
    "aequi" + "tas",
    "soc" + "rates",
    "jacob_" + "elias_redmond",
)
TEXT_SUFFIXES = {".json", ".yml", ".yaml"}
RETIREMENT_CONTEXT = {
    "blocked",
    "denylist",
    "denied",
    "deprecated",
    "disengaged",
    "forbidden",
    "historical",
    "legacy",
    "retired",
}


def _walk_strings(value: Any, path: tuple[str, ...] = ()):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from _walk_strings(child, (*path, str(key)))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _walk_strings(child, (*path, str(index)))
    elif isinstance(value, str):
        yield path, value


class DisengagedIdentityMigrationTests(unittest.TestCase):
    def test_disengaged_identifiers_do_not_resolve_on_active_surfaces(self) -> None:
        findings: list[str] = []

        for directory in STRICT_TEXT_ROOTS:
            if not directory.exists():
                continue
            for path in directory.rglob("*"):
                if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                    continue
                relative = path.relative_to(ROOT).as_posix()
                lowered = path.read_text(encoding="utf-8").lower()
                for identity in DISENGAGED:
                    if identity in lowered:
                        findings.append(f"{relative}: active reference to {identity}")

        for directory in STRUCTURED_ROOTS:
            if not directory.exists():
                continue
            for path in directory.rglob("*.json"):
                relative = path.relative_to(ROOT).as_posix()
                lowered_path = relative.lower()
                for identity in DISENGAGED:
                    if identity in lowered_path:
                        findings.append(f"{relative}: disengaged identity in active path")
                document = json.loads(path.read_text(encoding="utf-8"))
                for field_path, text in _walk_strings(document):
                    breadcrumb = ".".join(field_path).lower()
                    retirement_only = any(
                        marker in breadcrumb for marker in RETIREMENT_CONTEXT
                    )
                    lowered = text.lower()
                    for identity in DISENGAGED:
                        if identity in lowered and not retirement_only:
                            findings.append(
                                f"{relative}:{breadcrumb}: resolves active {identity}"
                            )

        if findings:
            self.fail("disengaged identities remain active:\n" + "\n".join(findings))

    def test_manifest_contains_only_current_active_artifacts(self) -> None:
        manifest = json.loads(
            (ROOT / "manifests" / "qso-genomes-compatibility-v1.json").read_text(
                encoding="utf-8"
            )
        )
        serialized = json.dumps(manifest, sort_keys=True).lower()
        for identity in DISENGAGED:
            self.assertNotIn(identity, serialized)
        self.assertEqual(8, len(manifest["artifacts"]))

    def test_retired_authority_record_is_absent(self) -> None:
        self.assertFalse(
            (ROOT / "governance" / "agents" / "jacob-elias-redmond.json").exists()
        )
        current = json.loads(
            (ROOT / "governance" / "agents" / "jacob-thomas-redmond.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual("jacob_thomas_redmond", current["agent_id"])


if __name__ == "__main__":
    unittest.main()
