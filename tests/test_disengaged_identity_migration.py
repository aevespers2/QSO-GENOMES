from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE_ROOTS = (
    ROOT / ".github" / "workflows",
    ROOT / "contracts",
    ROOT / "sprites",
    ROOT / "governance",
    ROOT / "manifests",
)
DISENGAGED = (
    "aequi" + "tas",
    "soc" + "rates",
    "jacob_" + "elias_redmond",
)
TEXT_SUFFIXES = {".json", ".yml", ".yaml"}


class DisengagedIdentityMigrationTests(unittest.TestCase):
    def test_disengaged_identifiers_do_not_resolve_on_active_surfaces(self) -> None:
        findings: list[str] = []
        for directory in ACTIVE_ROOTS:
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
        self.assertEqual([], findings)

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
