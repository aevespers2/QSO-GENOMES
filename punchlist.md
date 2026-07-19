# QSOBuilder Punch List

The Architect controls dependency order in `taskchain.md`. PR #2 remains the canonical four-genome candidate, not an accepted release. Checked implementation items show that candidate remediation exists somewhere in the submitted lineage; they do not establish acceptance.

## P0a — Architect reconciliation and scope containment

- [ ] Recapture current `main`, PR #2 head, merge base, ahead/behind counts, mergeability, workflow/status state, and review-thread inventory.
- [ ] Reconcile current `main` and every intended in-scope candidate commit into PR #2 without force-rewriting reviewed history.
- [ ] Complete PR #12 removal of active Aequitas, Socrates, and `jacob_elias_redmond` identity surfaces while retaining historical reports as provenance only.
- [ ] Remove remaining live references from manifests, generators, workflows, identity registries, release records, and current candidate descriptions.
- [ ] Regenerate the compatibility manifest and all affected canonical digests after nomenclature removal.
- [ ] Add negative migration tests proving disengaged identifiers cannot resolve through an active contract, workflow, manifest, registry, or runtime path.
- [ ] Record retained historical paths, removed active paths, old/new authority IDs, digest changes, reconciliation method, and rollback plan.
- [ ] Freeze one mergeable submitted head for exact-head review.

## P0b — Reconciliation workflow repair

- [x] Bound scheduled open-PR enumeration to 100 and deduplicate the PR-number set.
- [x] Paginate prior issue comments before posting reconciliation notices.
- [x] Key notices to exact head/base state and suppress duplicate notices.
- [x] Replace active `jacob_elias_redmond` workflow authority references with `jacob_thomas_redmond`.
- [x] Add exact-head, least-privilege pre-review tests with pinned action and test-runner versions.
- [ ] Pass the reconciliation pre-review workflow at the final submitted head.
- [ ] Replay the trusted-main reconciliation workflow against PR #2 and retain deterministic artifacts.
- [ ] Prove repeated runs create no duplicate notice for the same exact reconciliation state.
- [ ] Preserve the rule that automated reconciliation may open a draft repair PR but may never merge, publish, or release.

## P0c — Consent-capacity lock repair

- [x] Correct the validator so the immutable all-files policy scope binds covered files without noisy per-file marker false positives.
- [x] Preserve fail-closed rejection of bypass patterns, invalid UTF-8, duplicate policy keys, non-finite numbers, missing principles, and weakened lock responses.
- [x] Add focused regression tests for global scope, bypass rejection, and duplicate-key policy failure.
- [x] Pin workflow actions, disable persisted credentials, assert the exact submitted head, and retain hashed evidence.
- [ ] Pass the Consent Capacity Lock workflow at the final submitted head.
- [ ] Verify the retained evidence names the exact head and reproduces its report digest.

## P1 — Candidate findings after the head is frozen

- [x] Reachable submitted-state provenance is present. **Final-head replay and review disposition remain.**
- [x] Exact Atlas/Nova/Orion/Lyra artifact-set enforcement is present. **Final-head replay and review disposition remain.**
- [x] Versioned immutable-ethics migration and authoritative protocol binding are present in the candidate lineage. **Complete identity/content/boundary enforcement remains.**
- [x] Local-ethics conflict and duplicate migration-path rejection are present. **Final-head replay and review disposition remain.**
- [x] Source-derived manifest identity validation is present. **Complete digest-scope semantics remain.**
- [ ] Define artifact-byte and complete-manifest digest scopes and bind all consumer-relevant metadata.
- [ ] Pin the approved immutable protocol identity and contents; require exact migration identity, source profile, status, boundary, consumer key set, and unique paths.
- [ ] Validate Jacob Thomas Redmond review semantics, non-execution boundaries, evidence requirements, and human final approval.
- [ ] Correct deterministic-suite failures exposed at the frozen reconciled head.
- [ ] Resolve or formally disposition every still-material review thread against that exact head.

## Acceptance replay

- [ ] Run the complete schema, immutable, migration, canonicalization, manifest, duplicate/conflict, numeric-overflow, scope-exclusion, consent-lock, human-authority, and negative suite from a clean checkout at the frozen reviewed commit.
- [ ] Retain supported Python/OS/tool versions, install commands, exit codes, workflow URLs, logs, artifact hashes, and digest-scope identities.
- [ ] Verify missing, stale, mutated, duplicate, conflicting, overflowed, unapproved-supervisor, identity-drift, consent-bypass, and incompatible artifacts fail closed.
- [ ] Validate the accepted version/hash set read-only in `QuantumStateObjects` and `QSO-FABRIC`.

## Held behind approval

- [ ] Publish or tag the compatibility set only after all release gates pass and explicit approval is recorded.
- [ ] Payment-policy genome fields remain blocked until the settlement boundary and migration policy are approved.

## Quality gates

- [ ] All active agent and authority identities use approved three-part human naming conventions.
- [ ] Genomes and supervisory contracts remain declarative data only.
- [ ] No shell, network, credential, package-installation-at-runtime, repository-write, repair-PR, payment, or self-replication authority enters the accepted alpha.
- [ ] Every evidence claim records exact command, result, reachable commit, canonicalization profile, artifact paths, and hash set.
- [ ] Candidate implementations, configured workflows, accepted CI, review dispositions, and downstream evidence remain explicitly separated.
