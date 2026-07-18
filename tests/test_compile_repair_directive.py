import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "compile_repair_directive.py"


class RepairDirectiveTests(unittest.TestCase):
    def run_compiler(self, source):
        with tempfile.TemporaryDirectory() as tmp:
            source_path = Path(tmp) / "source.json"
            output_path = Path(tmp) / "directive.json"
            source_path.write_text(json.dumps(source), encoding="utf-8")
            result = subprocess.run(
                ["python", str(SCRIPT), "--input", str(source_path), "--output", str(output_path)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            return result, json.loads(output_path.read_text()) if output_path.exists() else None

    def test_classifies_manifest_and_provenance(self):
        result, directive = self.run_compiler({
            "pull_request_number": 2,
            "head_sha": "a" * 40,
            "report": "Manifest digest and provenance ancestor are stale in manifests/set.json",
            "comments": [],
        })
        self.assertEqual(result.returncode, 0)
        self.assertIn("manifest", directive["finding_class"])
        self.assertIn("provenance", directive["finding_class"])
        self.assertIn("manifests/set.json", directive["exact_code_locations"])
        self.assertFalse(directive["human_review_requirement"]["automatic_final_merge"])

    def test_rejects_empty_source(self):
        result, directive = self.run_compiler({"pull_request_number": 2, "head_sha": "b" * 40})
        self.assertNotEqual(result.returncode, 0)
        self.assertIsNone(directive)

    def test_preserves_comments_and_rollback(self):
        comment = "Exact-head CI failed in .github/workflows/conformance.yml"
        result, directive = self.run_compiler({
            "pull_request_number": 7,
            "head_sha": "c" * 40,
            "review_body": comment,
            "comments": [comment],
        })
        self.assertEqual(result.returncode, 0)
        self.assertEqual(directive["accepted_comments"], [comment])
        self.assertIn("rollback_plan", directive)
        self.assertIn("workflow", directive["finding_class"])


if __name__ == "__main__":
    unittest.main()
