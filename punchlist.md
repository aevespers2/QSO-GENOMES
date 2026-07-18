# QSOBuilder Punch List

The Architect controls dependency order in `taskchain.md`. PR #2 is the sole canonical candidate, not an accepted release. A checked implementation item means candidate remediation is present somewhere in the submitted lineage; it does not mean the finding is accepted. **Do not add further acceptance-remediation commits until the Architect completes P0a reconciliation and freezes one mergeable head, unless an explicit bounded exception is recorded.**

## P0a — Architect reconciliation and scope containment

- [ ] Recapture current `main`, PR head, merge base, ahead/behind counts, mergeability, workflow/status state, and review-thread inventory.
- [ ] Reconcile current `main` and every intended in-scope candidate commit into existing PR #2 without force-rewriting reviewed history.
- [ ] Exclude or explicitly quarantine `sprites/socrates.json`, `contracts/socrates-review-binding.json`, Aequitas compatibility aliases, and repair-pull-request authority from the current `0.1.0-alpha.1` candidate.
- [ ] Record conflicts, retained paths, excluded paths, Socrates disposition, old/new heads, reconciliation method, and rollback plan.
- [ ] Freeze the resulting mergeable submitted head for exact-head review.

## Pre-Review Tasks — reconciliation automation

- [ ] Bound scheduled open-PR enumeration explicitly and deduplicate the resulting PR-number set before processing.
- [ ] Paginate existing PR comments before deciding whether a reconciliation notice already exists.
- [ ] Add stable hidden markers keyed by finding type and exact head/base SHAs so hourly runs do not post duplicate fork/conflict notices.
- [ ] Add regression coverage proving more than 30 open PRs are enumerated up to the configured bound and repeated runs leave one notice per exact reconciliation state.
- [ ] Run the corrected workflow from trusted `main`, retain its evidence artifact, and verify PR #2 receives no duplicate comment on a second identical run.
- [ ] Keep PR #2 in draft while it is non-mergeable or lacks exact-head CI.

## P0b — Candidate findings after the head is frozen

- [x] Reachable submitted-state provenance is present. **Final-head replay and review disposition remain.**
- [x] Exact Atlas/Nova/Orion/Lyra artifact-set enforcement is present. **Final-head replay and review disposition remain.**
- [x] Versioned immutable-ethics migration and authoritative protocol binding are present in the candidate lineage. **Complete identity/content/boundary enforcement remains.**
- [x] Local-ethics conflict and duplicate migration-path rejection are present. **Final-head replay and review disposition remain.**
- [x] Aequitas reference, invariant, review-surface, oversight uniqueness, and source-consistency candidate checks are present. **Approved identity, activation semantics, numeric finiteness, final replay, and disposition remain.**
- [x] Source-derived manifest identity validation is present. **Complete digest-scope semantics remain.**
- [x] A pinned `jsonschema==4.26.0` dependency and cache input are present on current PR head `e51a814cd329c55e45a1599b205ef234859e4848`. **Not accepted until reconciled and replayed.**
- [x] Submitted-head checkout and verification are configured on the current PR head. **No attached exact-head workflow run exists; acceptance remains open.**
- [ ] Define artifact-byte and complete-manifest digest scopes and bind all consumer-relevant metadata.
- [ ] Pin the approved immutable protocol identity and contents; require exact migration identity, source profile, status, boundary, consumer key set, and unique paths.
- [ ] Pin the approved Aequitas identity and validate activation mode, human-review semantics, per-surface oversight, aliases, and numeric finiteness.
- [ ] Correct any deterministic-suite failures exposed at the frozen reconciled head.
- [ ] Resolve or formally disposition every current and still-material outdated review thread against that exact head.

## Acceptance replay

- [ ] Run the complete schema, immutable, migration, Aequitas, canonicalization, manifest, duplicate/conflict, numeric-overflow, scope-exclusion, and negative suite from a clean checkout at the frozen reviewed commit.
- [ ] Retain supported Python/OS/tool versions, install commands, exit codes, workflow URLs, logs, artifact hashes, and digest-scope identities.
- [ ] Verify missing, stale, mutated, duplicate, conflicting, overflowed, weakened-review, unapproved-supervisor, alias-drift, and incompatible artifacts fail closed.
- [ ] Validate the accepted version/hash set read-only in `QuantumStateObjects` and `QSO-FABRIC`.

## Held behind approval

- [ ] Publish or tag the compatibility set only after all release gates pass and explicit approval is recorded.
- [ ] Evaluate Socrates only as a separately versioned supervisory migration after the four-genome alpha and explicit product/security approval.
- [ ] Payment-policy genome fields remain blocked until the settlement boundary and migration policy are approved.

## Quality gates

- [ ] Genomes and supervisory contracts remain declarative data only.
- [ ] No shell, network, credential, package-installation-at-runtime, repository-write, repair-PR, payment, or self-replication authority enters the accepted alpha.
- [ ] Every evidence claim records exact command, result, reachable commit, canonicalization profile, artifact paths, and hash set.
- [ ] Candidate implementations, configured workflows, accepted CI, review dispositions, and downstream evidence remain explicitly separated.
