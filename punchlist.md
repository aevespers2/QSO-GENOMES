# QSOBuilder Punch List

The Architect controls dependency order in `taskchain.md`. Execute only the first unblocked item and attach reproducible evidence. PR #2 is a candidate under review, not an accepted release.

## Immediate — PR #2 acceptance findings

- [x] Replace inaccessible or non-ancestor intermediate commit references with reachable submitted-state provenance.
- [x] Make schema validation assert the exact required Atlas, Nova, Orion, and Lyra artifact set.
- [x] Prove immutable protections match the full approved immutable-ethics protocol or record an explicit versioned migration.
- [x] Validate Aequitas published invariants against source artifacts and reject duplicate, stale, or path-inconsistent references before de-duplication.
- [x] Define whether the set digest identifies artifact bytes only or the complete compatibility manifest; bind all identity-bearing metadata accordingly.
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
- 2026-07-16 — Completed the exact four-genome assertion finding. `scripts/validate_schema_set.py` now fails closed unless `genomes/` contains exactly `atlas.json`, `lyra.json`, `nova.json`, and `orion.json`; `tests/test_schema_artifact_set.py` adds four focused tests for exact, missing, unexpected, and non-JSON-support-file cases. All four focused tests and bytecode compilation passed under CPython 3.13.5 with `jsonschema` 4.26.0. Reachable implementation/test ancestor: `28f419e60dd16a1cc482076f6dc3e3e56bf2ab79`; evidence: `reports/p0-exact-genome-artifact-set-validation.md`. Complete clean-checkout/CI acceptance remains open.
- 2026-07-16 — Completed the immutable-policy finding by adding explicit candidate migration `QSO-GENOME-IMMUTABLE-ETHICS-MIGRATION-v1`. The migration binds the exact four genome paths to authoritative `QSO-IMMUTABLE-ETHICS-v1` canonical digest `ecbab42031461161e91e511ce5f1ba19f1d2d75d81a8351a32f185b181c206af`, treats genome-local ethics as additive only, and rejects missing, mismatched, weakened, or conflicting bindings. Five focused standard-library tests passed under CPython 3.13.5. Reachable implementation/test ancestor: `257839316082faf2a3ab115a65fb1550b74ecc06`; evidence: `reports/p0-immutable-ethics-migration-validation.md`. Clean-checkout, manifest-identity, downstream, and human-acceptance gates remain open.
- 2026-07-16 — Completed Aequitas reference and invariant integrity on implementation/test head `92dcc4b01c598248c72185b0352d8f4c8fdea9f2`. The standard-library validator rejects duplicate IDs and paths before de-duplication, non-canonical paths, missing or stale source identities/schema versions, incomplete reference sets, missing/unknown invariants, and any published invariant that disagrees with the Sprite or four genome sources. Eight focused tests, direct validator replay, and bytecode compilation passed under CPython 3.13.5; evidence: `reports/p0-aequitas-reference-integrity-validation.md`. Clean-checkout/CI acceptance remains open; the next unblocked finding is compatibility-set digest semantics and identity-bearing manifest metadata.
- 2026-07-16 — Completed complete-manifest identity digest semantics on implementation/focused-test ancestor `1ae9979fafe5211d8b3f7df0476f675f12e7e884`. Digest profile `qso-genomes-manifest-identity-v1` binds manifest version, compatibility-set ID, the complete canonicalization object, digest rules, and every artifact descriptor field; only lifecycle `status` and recursive `set_sha256` are explicitly excluded. Five focused tests and bytecode compilation passed under CPython 3.13.5. The new candidate digest is `3583dd05506c8d2921554676f80140cd66efa23a83154dbf4536ed51e56d5ed6`; evidence: `reports/p0-manifest-identity-digest-validation.md`. Clean-checkout/CI acceptance remains open; the next unblocked finding is reproducible schema-validation dependency declaration or replacement.
