# QSOBuilder Punch List

The Architect controls dependency order in `taskchain.md`. Execute only the first unblocked item and attach reproducible evidence. PR #2 is the canonical candidate under review, not an accepted release. A checked implementation item means the candidate contains an attempted remediation; it does not mean the review finding or release gate is accepted.

## Immediate — PR #2 acceptance findings

- [x] Replace inaccessible or non-ancestor intermediate commit references with reachable submitted-state provenance. **Candidate remediation present; final review disposition and exact-head replay remain.**
- [x] Make schema validation assert the exact required Atlas, Nova, Orion, and Lyra artifact set. **Candidate remediation present; review thread remains open.**
- [x] Record an explicit versioned migration binding the full approved immutable-ethics protocol. **Candidate artifact present; complete enforcement and final acceptance remain open.**
- [x] Add Aequitas invariant/reference validation before de-duplication. **Candidate validator present; original and newly identified uniqueness/source-identity findings remain open.**
- [x] Bind `protocols/immutable-ethics-v1.json` and `contracts/immutable-ethics-migration-v1.json` into the compatibility manifest or another explicit accepted set identity. **Candidate manifest now contains both artifacts; exact-head replay and review disposition remain.**
- [x] Reject local ethics additions that conflict with the authoritative protocol; reject duplicate migration paths before set conversion. **Candidate validator now binds exact local-ethics list digests and rejects duplicate migration and binding paths before conversion; exact-head replay and review disposition remain.**
- [ ] Reject duplicate Aequitas review surfaces and conflicting oversight definitions before set conversion.
- [ ] Derive or verify manifest artifact IDs, versions, and other identity-bearing fields against source documents.
- [ ] Define whether each digest identifies artifact bytes only or the complete compatibility manifest; bind all consumer-relevant metadata accordingly.
- [ ] Declare the schema-validation dependency or replace it with reproducible standard-library tooling.
- [ ] Fix conformance workflow setup so pip caching cannot fail for lack of a dependency file.
- [ ] Make pull-request CI check out and certify the submitted head, or explicitly retain both submitted and synthetic merge SHAs.
- [ ] Resolve or formally disposition every current review thread against the final candidate head.

## Acceptance replay

- [ ] Run schema, immutable, migration, Aequitas, canonicalization, manifest, duplicate/conflict, and negative tests from a clean checkout at the exact reviewed commit.
- [ ] Retain supported Python/OS/tool versions, install commands, exit codes, workflow URLs, logs, artifact hashes, and digest-scope identities.
- [ ] Verify missing artifacts, unknown fields, source-identity drift, immutable mutations, conflicting local ethics, duplicate migration paths, duplicate review surfaces, unresolved/duplicate references, incompatible versions, and canonicalization drift fail closed.
- [ ] Validate the accepted version/hash set read-only in `QuantumStateObjects` and `QSO-FABRIC`.

## Held behind approval

- [ ] Publish or tag the compatibility set only after all release gates pass and explicit approval is recorded.
- [ ] Payment-policy genome fields remain blocked until the settlement boundary and migration policy are approved.

## Quality Gates

- [ ] Genomes remain declarative data only.
- [ ] No shell, network, credential, package-installation-at-runtime, repository-write, payment, or self-replication authority is introduced.
- [ ] Every completed item records the exact command, result, reachable commit, canonicalization profile, artifact paths, and hash set.
- [ ] Candidate implementations, unresolved findings, accepted CI evidence, and downstream-consumer evidence remain explicitly separated.

## Evidence Log

- 2026-07-16 — Completed the highest-priority immutable artifact binding item on implementation/test head `74c7d714a14123f52903178e805a614f2ead1bf1`, based directly on canonical PR #2 head `2d42c960cefb70fdaada969e75debf50fb06f36c`. The candidate manifest now contains eleven artifacts, including the authoritative protocol and versioned migration, with protocol digest `ecbab42031461161e91e511ce5f1ba19f1d2d75d81a8351a32f185b181c206af`, migration digest `d56994e90dd9d57a65db62b558d4acbd99b8b28ac8b1e124ed48257a9e29fb30`, and candidate path/hash set digest `6d9b0ca8c6766fbb63b4613df5b2baee455f1e63c848d6f75e56726efbc57cac`. CPython 3.13.5 bytecode compilation and a focused deterministic canonical replay passed; evidence is recorded in `reports/p0-immutable-artifact-manifest-binding-validation.md`. Clean-checkout CI and review acceptance remain open; the next unblocked item is local-ethics conflict and duplicate migration-path rejection.
- 2026-07-16 — Completed local-ethics conflict and duplicate migration-path rejection on implementation/test ancestor `a75f23c3e91dea925ee5b97cc265bddb5ec7b1fc`, based directly on canonical PR #2 head `8c65748cfaa9a213d29d7f03d250a3f797bbb1a1`. A standard-library validator now checks duplicate `applies_to` and local-binding paths before set/map conversion and binds each genome's exact canonical local-ethics list digest, causing any unreviewed addition or mutation to fail closed pending a new migration version. CPython 3.13.5 compilation, direct validator replay, and eight focused tests passed against an exact relevant-data fixture mirror. The migration digest is `7677a01c9ea9d35f3c8c3a84e4601c0ffa2ac289aaf65699771e25876bbf8926`; the candidate set digest is `99f33227247ef39fef3e1c3206c8ea49b9be9af86148298f07bdbf00b0cd6921`. Evidence and limitations are recorded in `reports/p0-local-ethics-conflict-validation.md`; clean-checkout CI and review acceptance remain open.
