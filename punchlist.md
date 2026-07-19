# QSOBuilder Punch List

The Architect controls dependency order in `taskchain.md`. PR #2 is the sole canonical candidate, not an accepted release. A checked implementation item means candidate remediation is present somewhere in the submitted lineage; it does not mean the finding is accepted. **Do not add further acceptance-remediation commits until the Architect completes P0a reconciliation and freezes one mergeable head, unless an explicit bounded exception is recorded.**

## P0a — Architect reconciliation and scope containment

- [ ] Recapture current `main`, PR head, merge base, ahead/behind counts, mergeability, workflow/status state, and review-thread inventory.
- [ ] Reconcile current `main` and every intended in-scope candidate commit into existing PR #2 without force-rewriting reviewed history.
- [x] Disengage and remove active Aequitas and Socrates persona records, bindings, validator, and focused tests while retaining historical reports as provenance only.
- [x] Retire `jacob_elias_redmond` as an active authority identity and transfer review responsibility to `jacob_thomas_redmond`.
- [ ] Remove remaining Aequitas/Socrates/Elias references from manifests, generators, workflows, release documents, identity registries, and current candidate descriptions.
- [ ] Regenerate the compatibility manifest and all affected digests after the removal.
- [ ] Add migration regression tests proving no active contract, workflow, manifest, agent record, or runtime path resolves the disengaged identities.
- [ ] Record retained historical paths, removed active paths, old/new authority IDs, digest changes, and rollback plan.
- [ ] Freeze the resulting mergeable submitted head for exact-head review.

## P0b — Candidate findings after the head is frozen

- [x] Reachable submitted-state provenance is present. **Final-head replay and review disposition remain.**
- [x] Exact Atlas/Nova/Orion/Lyra artifact-set enforcement is present. **Final-head replay and review disposition remain.**
- [x] Versioned immutable-ethics migration and authoritative protocol binding are present in the candidate lineage. **Complete identity/content/boundary enforcement remains.**
- [x] Local-ethics conflict and duplicate migration-path rejection are present. **Final-head replay and review disposition remain.**
- [x] Source-derived manifest identity validation is present. **Complete digest-scope semantics remain.**
- [x] A pinned `jsonschema==4.26.0` dependency and cache input are present on current PR head `e51a814cd329c55e45a1599b205ef234859e4848`. **Not accepted until reconciled and replayed.**
- [x] Submitted-head checkout and verification are configured on the current PR head. **No attached exact-head workflow run exists; acceptance remains open.**
- [ ] Define artifact-byte and complete-manifest digest scopes and bind all consumer-relevant metadata.
- [ ] Pin the approved immutable protocol identity and contents; require exact migration identity, source profile, status, boundary, consumer key set, and unique paths.
- [ ] Validate Jacob Thomas Redmond review semantics, non-execution boundaries, evidence requirements, and human final approval.
- [ ] Correct any deterministic-suite failures exposed at the frozen reconciled head.
- [ ] Resolve or formally disposition every current and still-material outdated review thread against that exact head.

## Acceptance replay

- [ ] Run the complete schema, immutable, migration, canonicalization, manifest, duplicate/conflict, numeric-overflow, scope-exclusion, human-authority, and negative suite from a clean checkout at the frozen reviewed commit.
- [ ] Retain supported Python/OS/tool versions, install commands, exit codes, workflow URLs, logs, artifact hashes, and digest-scope identities.
- [ ] Verify missing, stale, mutated, duplicate, conflicting, overflowed, unapproved-supervisor, identity-drift, and incompatible artifacts fail closed.
- [ ] Validate the accepted version/hash set read-only in `QuantumStateObjects` and `QSO-FABRIC`.

## Held behind approval

- [ ] Publish or tag the compatibility set only after all release gates pass and explicit approval is recorded.
- [ ] Payment-policy genome fields remain blocked until the settlement boundary and migration policy are approved.

## Quality gates

- [ ] All active agent and authority identities use three-part human naming conventions.
- [ ] Genomes and supervisory contracts remain declarative data only.
- [ ] No shell, network, credential, package-installation-at-runtime, repository-write, repair-PR, payment, or self-replication authority enters the accepted alpha.
- [ ] Every evidence claim records exact command, result, reachable commit, canonicalization profile, artifact paths, and hash set.
- [ ] Candidate implementations, configured workflows, accepted CI, review dispositions, and downstream evidence remain explicitly separated.
