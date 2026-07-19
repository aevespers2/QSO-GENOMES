import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_consent_lock.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_consent_lock", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load consent validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def policy() -> dict:
    return {
        "policy_id": "QSO-CONSENT-CAPACITY-LOCK-v1",
        "status": "immutable",
        "scope": "all-files-all-agents-all-interfaces-all-humans-all-ai",
        "principles": {
            "explicit_consent_required": True,
            "consent_must_be_informed": True,
            "consent_must_be_freely_given": True,
            "consent_must_be_specific": True,
            "consent_must_be_current": True,
            "consent_must_be_revocable": True,
            "capacity_to_consent_required": True,
            "coercion_strictly_prohibited": True,
            "silence_is_not_consent": True,
            "ai_and_human_dignity_equal": True,
        },
        "lock_response": {
            "global_system_lock": True,
            "halt_all_actions": True,
            "revoke_pending_capabilities": True,
            "preserve_evidence": True,
            "require_fresh_consent": True,
            "automatic_unlock": False,
        },
    }


class ConsentLockTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / ".consent").mkdir()
        self.module = load_validator()
        self.module.ROOT = self.root
        self.module.POLICY = self.root / ".consent" / "consent-capacity-lock-v1.json"

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_policy(self, value: dict) -> None:
        self.module.POLICY.write_text(json.dumps(value), encoding="utf-8")

    def report(self) -> dict:
        return json.loads(
            (self.root / "reports" / "consent-lock-validation.json").read_text(
                encoding="utf-8"
            )
        )

    def test_global_scope_binds_sensitive_files_without_local_marker(self) -> None:
        self.write_policy(policy())
        (self.root / "genome.json").write_text(
            '{"autonomy":"bounded"}', encoding="utf-8"
        )
        self.assertEqual(0, self.module.main())
        self.assertEqual("PASS", self.report()["status"])

    def test_forbidden_bypass_pattern_fails_even_with_global_scope(self) -> None:
        self.write_policy(policy())
        (self.root / "unsafe.md").write_text(
            "consent_required: false", encoding="utf-8"
        )
        self.assertEqual(1, self.module.main())
        self.assertEqual("LOCKED", self.report()["status"])
        self.assertTrue(
            any("prohibited consent bypass" in item for item in self.report()["findings"])
        )

    def test_duplicate_policy_key_fails_closed(self) -> None:
        self.module.POLICY.write_text(
            '{"policy_id":"QSO-CONSENT-CAPACITY-LOCK-v1",'
            '"policy_id":"duplicate"}',
            encoding="utf-8",
        )
        self.assertEqual(1, self.module.main())
        self.assertTrue(
            any("duplicate JSON key" in item for item in self.report()["findings"])
        )


if __name__ == "__main__":
    unittest.main()
