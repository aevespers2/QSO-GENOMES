# PR #2 Submitted-State Provenance

Date: 2026-07-16

## Purpose

This record replaces branch-local or rewritten intermediate commit identifiers in the P0 reports with one GitHub-reachable submitted source state. The validation reports bind their claims to this commit plus the exact Git blob and SHA-256 values recorded for the files they inspected.

## Reachable source state

- Repository: `aevespers2/QSO-GENOMES`
- Pull request: `#2`
- Submitted branch: `builder/p0-four-genome-validation-20260716`
- PR base at review: `c6c6ccdd61391da5fae5a268022c510069016b33`
- Submitted source state: `9de3db6a33308346d09b7004e6702e997dce9ba8`
- Comparison result: submitted source state is `ahead` of the recorded PR base by 28 commits and behind by 0 commits.

The submitted source state contains the Atlas genome, immutable baseline, Aequitas binding, canonicalization generator, candidate manifest, validators, tests, reports, and conformance workflow reviewed in PR #2. Later documentation-only provenance corrections are descendants of this state and do not alter the validated contract artifacts unless separately recorded.

## Reproduction checks

```bash
git fetch origin pull/2/head:pr-2-submitted
git cat-file -e 9de3db6a33308346d09b7004e6702e997dce9ba8^{commit}
git merge-base --is-ancestor \
  c6c6ccdd61391da5fae5a268022c510069016b33 \
  9de3db6a33308346d09b7004e6702e997dce9ba8
git checkout --detach 9de3db6a33308346d09b7004e6702e997dce9ba8
```

Expected ancestry result: exit status `0`.

## Evidence boundary

This record establishes reachable source provenance only. It does not accept the candidate, replace clean-checkout or CI replay, resolve immutable-protocol equivalence, validate all Aequitas invariants, define final digest semantics, or authorize publication. Those remain separate acceptance findings in `punchlist.md`.
