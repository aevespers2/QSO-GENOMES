import json, subprocess, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; SCRIPT=ROOT/'scripts'/'compile_repair_directive.py'
class RepairDirectiveTests(unittest.TestCase):
 def run_compiler(self,source):
  with tempfile.TemporaryDirectory() as tmp:
   sp=Path(tmp)/'source.json'; op=Path(tmp)/'directive.json'; sp.write_text(json.dumps(source))
   r=subprocess.run(['python',str(SCRIPT),'--input',str(sp),'--output',str(op)],cwd=ROOT,text=True,capture_output=True,check=False)
   return r,json.loads(op.read_text()) if op.exists() else None
 def test_classifies_manifest_and_provenance(self):
  r,d=self.run_compiler({'pull_request_number':2,'head_sha':'a'*40,'report':'Manifest digest and provenance ancestor are stale in manifests/set.json','comments':[]})
  self.assertEqual(r.returncode,0);self.assertIn('manifest',d['finding_class']);self.assertIn('provenance',d['finding_class']);self.assertIn('manifests/set.json',d['exact_code_locations']);self.assertFalse(d['human_review_requirement']['automatic_final_merge'])
 def test_rejects_empty_source(self):
  r,d=self.run_compiler({'pull_request_number':2,'head_sha':'b'*40});self.assertNotEqual(r.returncode,0);self.assertIsNone(d)
 def test_preserves_comments_and_rollback(self):
  c='Exact-head CI failed in .github/workflows/conformance.yml';r,d=self.run_compiler({'pull_request_number':7,'head_sha':'c'*40,'review_body':c,'comments':[c]});self.assertEqual(r.returncode,0);self.assertEqual(d['accepted_comments'],[c]);self.assertIn('rollback_plan',d);self.assertIn('workflow',d['finding_class'])
if __name__=='__main__':unittest.main()
