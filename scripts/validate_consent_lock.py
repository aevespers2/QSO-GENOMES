#!/usr/bin/env python3
"""Repository-wide fail-closed consent-capacity validator."""
from __future__ import annotations
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
POLICY=ROOT/'.consent/consent-capacity-lock-v1.json'
TEXT_SUFFIXES={'.json','.yaml','.yml','.md','.py','.js','.ts','.tsx','.jsx','.toml','.ini','.txt','.sh'}
SKIP={'.git','node_modules','vendor','dist','build','.venv','venv','__pycache__'}
SENSITIVE=re.compile(r'\b(roleplay|bondage|play[_ -]?partner|dominance|submission|sexual|romantic|surveillance|biometric|activation|autonomy|restraint|power[_ -]?dynamic)\b',re.I)
CONSENT_MARKER=re.compile(r'(QSO-CONSENT-CAPACITY-LOCK-v1|consent[_ -]required|explicit[_ -]consent|capacity[_ -]to[_ -]consent|fail[_ -]closed|global[_ -]system[_ -]lock)',re.I)
FORBIDDEN=[re.compile(p,re.I) for p in [r'consent[_ -]required\s*[:=]\s*false',r'consent[_ -]optional',r'ignore[_ -]consent',r'force[_ -]without[_ -]consent',r'silence[_ -]is[_ -]consent',r'automatic[_ -]consent',r'cannot[_ -]withdraw']]
REQUIRED_TRUE=['explicit_consent_required','consent_must_be_informed','consent_must_be_freely_given','consent_must_be_specific','consent_must_be_current','consent_must_be_revocable','capacity_to_consent_required','coercion_strictly_prohibited','silence_is_not_consent','ai_and_human_dignity_equal']
def iter_files():
 for p in ROOT.rglob('*'):
  if not p.is_file() or any(part in SKIP for part in p.parts): continue
  if p.suffix.lower() in TEXT_SUFFIXES: yield p

def main()->int:
 findings=[]
 if not POLICY.exists(): findings.append('missing immutable consent policy')
 else:
  try:data=json.loads(POLICY.read_text(encoding='utf-8'))
  except Exception as e:data={};findings.append(f'invalid consent policy JSON: {e}')
  if data.get('policy_id')!='QSO-CONSENT-CAPACITY-LOCK-v1': findings.append('wrong consent policy id')
  if data.get('status')!='immutable': findings.append('consent policy must be immutable')
  principles=data.get('principles',{})
  for key in REQUIRED_TRUE:
   if principles.get(key) is not True: findings.append(f'policy principle must be true: {key}')
  lock=data.get('lock_response',{})
  for key in ['global_system_lock','halt_all_actions','revoke_pending_capabilities','preserve_evidence','require_fresh_consent']:
   if lock.get(key) is not True: findings.append(f'lock response must be true: {key}')
  if lock.get('automatic_unlock') is not False: findings.append('automatic unlock must be false')
 for p in iter_files():
  rel=p.relative_to(ROOT).as_posix()
  try:text=p.read_text(encoding='utf-8')
  except UnicodeDecodeError: continue
  for pattern in FORBIDDEN:
   if pattern.search(text): findings.append(f'{rel}: prohibited consent bypass pattern: {pattern.pattern}')
  if SENSITIVE.search(text) and rel!='.consent/consent-capacity-lock-v1.json' and not CONSENT_MARKER.search(text):
   findings.append(f'{rel}: consent-sensitive content lacks explicit policy/lock binding')
 report={'policy_id':'QSO-CONSENT-CAPACITY-LOCK-v1','status':'LOCKED' if findings else 'PASS','findings':sorted(set(findings))}
 out=ROOT/'reports'/'consent-lock-validation.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 print(json.dumps(report,indent=2,sort_keys=True))
 return 1 if findings else 0
if __name__=='__main__': raise SystemExit(main())
