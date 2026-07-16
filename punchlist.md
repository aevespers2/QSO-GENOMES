# QSOBuilder Punch List

The Architect controls dependency order in `taskchain.md`. Execute only the first unblocked item and attach reproducible evidence. PR #2 is a candidate under review, not an accepted release.

## Immediate — PR #2 acceptance findings

- [x] Replace inaccessible or non-ancestor intermediate commit references with reachable submitted-state provenance.
- [ ] Make schema validation assert the exact required Atlas, Nova, Orion, and Lyra artifact set.
- [ ] Prove immutable protections match the full approved immutable-ethics protocol or record an explicit versioned migration.
- [ ] Validate Aequitas published invariants against source artifacts and reject duplicate, stale, or path-inconsistent references before de-duplication.
- [ ] Define whether the set digest identifies artifact bytes only or the complete compatibility manifest; bind all identity-bearing metadata accordingly.
- [ ] Declare the schema-validation dependency or replace it with reproducible standard-library tooling.
- [ ] Fix conformance workflow setup so pip caching cannot fail for lack of a dependency file.
- [ ] Make pull-request CI check out and certify the submitted head, or explicitly retain both submitted and synthetic merge SHAs.
- [ ] Resolve or formally disposition every current review thread against the final candidate head.

## Acceptance replay

- [ ] Run schema, immutable, Aequitas, canonicalization, manifest, and negative tests from a clean checkout at the exact reviewed commit.
- [ ] Retain supported Python/OS/tool versions, install commands, exit codes, workflow URLs, logs, artifact hashes, and set identity.
- [ ] Verify missing artifacts, unknown fields, immutable mutations, duplicate/unresolved references, incompatible versions, and canonicalization drift fail closed.
- [ ] Validate the accepted version/hash set read-only in `QuantumStateObjects` and `QSO-FABRIC`.

## Held behind approval

- [ ] Publish or tag the compatibility set only after all release gates pass and explicit approval is recorded.
- [ ] Payment-policy genome fields remain blocked until the settlement boundary and migration policy are approved.

## Quality Gates

- [ ] Genomes remain declarative data only.
- [ ] No shell, network, credential, package-installation-at-runtime, repository-write, payment, or self-replication authority is introduced.
- [ ] Every completed item records the exact command, result, reachable commit, canonicalization profile, artifact paths, and hash set.
- [ ] Candidate claims are clearly separated from accepted CI and downstream-consumer evidence.

## Evidence Log

- 2026-07-16 — Completed the highest-priority provenance finding. Added `reports/submitted-state-provenance.md` and replaced non-reproducible intermediate commit references in all four P0 validation reports with reachable submitted source state `9de3db6a33308346d09b7004e6702e997dce9ba8`, exact Git blob identifiers, and retained SHA-256 evidence. GitHub comparison records that state as 28 commits ahead of PR base `c6c6ccdd61391da5fae5a268022c510069016b33` and behind by 0. This correction establishes provenance only; all remaining integrity, dependency, workflow, replay, and publication findings stay open.
