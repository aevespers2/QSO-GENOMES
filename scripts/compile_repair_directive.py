#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
from typing import Any
MECHANISMS={"provenance":["provenance","ancestor","reachable","digest","sha","chain-of-custody"],"manifest":["manifest","canonical","identity","artifact set","set_sha256"],"schema":["schema","duplicate key","non-finite","required artifact"],"ethics":["immutable ethics","aequitas","jacob elias redmond","oversight","review authority"],"workflow":["workflow","github actions","checkout","permissions","exact head","ci"],"migration":["migration","legacy","alias","compatibility","deprecation"],"security":["vulnerability","path traversal","symlink","credential","network","injection"],"release_state":["release","candidate","accepted","deployed","status contradiction"]}
FILE_RE=re.compile(r"(?<![\w.-])(?:[\w.-]+/)+[\w.-]+(?:\.[A-Za-z0-9_-]+)?")
def canonical_bytes(v:Any)->bytes:return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def main()->int:
 p=argparse.ArgumentParser();p.add_argument("--input",required=True,type=Path);p.add_argument("--output",required=True,type=Path);a=p.parse_args()
 s=json.loads(a.input.read_text());t="\n".join([str(s.get("report","")),str(s.get("review_body","")),"\n".join(map(str,s.get("comments",[])))]).strip()
 if not t: raise ValueError("repair source contains no report or review text")
 l=t.lower();classes=[n for n,terms in MECHANISMS.items() if any(x in l for x in terms)] or ["general_integrity"]
 loc=[x for x in sorted(set(FILE_RE.findall(t))) if not x.startswith("http")][:50]
 d={"directive_version":1,"team_id":"qso-report-repair-team-v1","source_pr":s.get("pull_request_number"),"source_head_sha":s.get("head_sha"),"source_evidence_digest":hashlib.sha256(canonical_bytes(s)).hexdigest(),"finding_class":classes,"accepted_comments":s.get("accepted_comments",s.get("comments",[])),"rejected_or_stale_comments":s.get("rejected_or_stale_comments",[]),"affected_invariants":["truthful-lifecycle","provenance-continuity","least-privilege","human-final-approval"],"exact_code_locations":loc,"implementation_actions":[f"Repair the {c} mechanism without weakening existing invariants." for c in classes],"test_plan":[f"Add one positive and one negative regression test for {c}." for c in classes]+["Run the complete repository conformance suite on the exact repair head.","Retain logs and bind them to the repair commit digest."],"migration_effects":"Preserve legacy identifiers and historical receipts; use explicit versioned aliases where identities change.","rollback_plan":"Revert the isolated repair commit or close the draft repair PR without changing the source PR history.","reevaluation_criteria":["Every accepted comment is answered by code or an evidence-backed disposition.","Original failing checks pass on the exact repair head.","No new high or critical findings are introduced.","Michael Aaron Redmond can reconcile the repair branch without history rewriting."],"human_review_requirement":{"review_authority_id":"jacob_elias_redmond","human_final_approval_required":True,"automatic_final_merge":False}}
 a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_bytes(canonical_bytes(d)+b"\n");print(json.dumps(d,indent=2,sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
