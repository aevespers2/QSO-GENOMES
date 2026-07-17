# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product
- 2026-07-16 — Defined the MVP as a complete, deterministic Atlas/Nova/Orion/Lyra compatibility set with immutable ethics, Aequitas references, canonical hashes, and an independent consumer manifest.
- 2026-07-16 — Confirmed this repository remains declarative and data-only; executable behavior and payment authority are out of scope.
- 2026-07-16 — Advanced the objective from candidate creation to independent acceptance of PR #2, preserving QSO-GENOMES as the highest portfolio unblocker while requiring exact-head evidence.
- 2026-07-16 — Selected existing PR #2 as the single canonical submission path and consolidated remediation there rather than opening a competing release PR.
- 2026-07-16 — Changed the local execution order after GitHub reported PR #2 non-mergeable and diverged from `main`: provenance-preserving branch reconciliation and one frozen submitted head now precede further exact-head remediation.
- 2026-07-17 — Kept portfolio priority unchanged after PR #2 advanced to head `e51a814cd329c55e45a1599b205ef234859e4848`; reconciliation remains P0 because the branch is materially diverged and exact-head evidence cannot stabilize while either side continues moving.
- 2026-07-17 — Scoped the first eligible alpha to the four genomes and the approved Aequitas boundary. Socrates, Aequitas compatibility aliases, and repair-pull-request authority are quarantined from the current release candidate and require a separately versioned migration plus explicit product and security approval.
- 2026-07-17 — Classified draft PR #3 as a separate governance-control-plane candidate rather than part of compatibility-set acceptance. Recommended merge order is PR #2 reconciliation and freeze first, followed by PR #3 refresh and independent governance review; an alternate order requires explicit Architect approval and a provenance-preserving migration record.

### Architecture
- QSO-GENOMES is the highest upstream contract blocker for the four-QSO portfolio and must publish schema/version/hash boundaries before runtime integration proceeds.
- PR #2 remains the sole compatibility-set review path; reconciliation must integrate current `main` and every intended in-scope candidate commit without force-rewriting reviewed history unless the Architect explicitly approves and documents an alternative.
- Draft PR #3 must remain isolated from the compatibility set and scheduled governance automation must remain inactive until the governance candidate is refreshed against the post-reconciliation default branch, independently certified at its exact head, and separately approved.
- The accepted set identity must bind all consumer-relevant manifest metadata, including the authoritative immutable protocol and migration, or explicitly distinguish separate digest scopes.
- Immutable protections must be pinned to the approved protocol identity and contents; local additions must fail closed when conflicting or duplicated.
- Migration validation must bind the expected migration identity, source profile, protocol identity, immutable status, enforcement boundary, exact consumer requirements, and unique paths.
- Manifest identity-bearing fields must be validated against source documents rather than trusted from hard-coded generator metadata.
- Aequitas references, review surfaces, activation rules, and per-surface oversight mappings must be unique, approved, and source-consistent before normalization.
- JSON loading used for contract replay must reject non-finite constants and numeric overflow.
- Socrates is not an alias-level replacement for Aequitas in the current compatibility set. Any future transition requires explicit identity, authority, migration, compatibility, and rollback semantics.

### Candidate implementation
- PR #2 proposes the missing Atlas genome, immutable baseline, Aequitas review binding, deterministic canonicalization, compatibility manifest, conformance tests, reports, provenance, and workflow configuration.
- Candidate remediation includes exact four-genome enforcement, a versioned immutable-ethics migration, Aequitas reference/invariant validation, immutable protocol and migration inclusion in an eleven-artifact manifest, local-ethics conflict checks, source-derived manifest identities, and reachable provenance work.
- 2026-07-17 — Candidate changes added `requirements.txt` pinning `jsonschema==4.26.0`, keyed setup-python caching to that file, checked out and verified the submitted PR head, and extended schema-set validation to both `aequitas.json` and `socrates.json`.
- Those changes are implemented candidate evidence, not accepted capability. No exact-head workflow run, mergeable reconciled head, independent clean replay, downstream verification, or publication approval exists.
- Validation of `socrates.json` establishes only schema conformance; it does not authorize Socrates, compatibility aliases, or repair authority for the current release.
- Draft PR #3 implements a candidate PR ontology, lifecycle validator, Inspector sampling workflow, escalation behavior, and governance-agent definitions. Those files are proposal evidence only: they do not resolve PR #2 findings, authorize issue mutation, activate scheduled automation, or establish portfolio-wide governance adoption.

### Repository health
- Historical snapshot: PR #2 head `46f3248d8f67b7f0cc734159d2fa0a27e6051ea7` was 74 commits ahead and 24 behind default head `0ac8960db20dba6ef083d928a44f4ca756d44713` at the earlier review point.
- Review-start snapshot: PR #2 was open and non-mergeable at `e51a814cd329c55e45a1599b205ef234859e4848`; then-current `main` was `20efbbf2f869b48a921519943580d2b491c686eb`; the branch was 86 commits ahead and 28 behind with merge base `c6c6ccdd61391da5fae5a268022c510069016b33`.
- Governance-document commits made during this review intentionally advance `main`, so the review-start counts are historical evidence rather than current reconciliation inputs.
- Reconciliation must recapture base, head, ahead/behind state, workflow state, and review-thread state immediately before work begins, then record method, conflict resolutions, retained and excluded changes, Socrates disposition, governance merge order, resulting immutable head, and renewed evidence.
- Draft PR #3 is open, non-mergeable, and draft at current head `91db1a9176e8274140a48a9fcfc8ba08af40ac43`. Its retained ontology-workflow evidence is tied to earlier head `8ba56bccd241db1e2b01c910065584a10af230e5`; no combined status checks or pull-request workflow runs currently certify `91db1a9…`.

### Review findings
- Material findings include complete immutable-statement enforcement; approved protocol-content pinning; migration source-profile, contract-ID, protocol-ID, status, boundary, exact-key, and unique-path checks; Aequitas identity, activation, per-surface oversight, duplicate-reference, duplicate-surface, and source-integrity checks; overflowed-number rejection; digest-scope semantics; exact-head provenance; and review-thread disposition.
- Candidate dependency and workflow changes may address earlier declared-dependency, cache-input, and submitted-head-checkout findings, but they are not accepted until they survive reconciliation, exact-head CI, and review disposition.
- Socrates introduces a separate scope finding because it adds a new supervisory identity, aliases, and repair authority outside the eleven-artifact manifest.
- PR #3 has separate governance findings: current-head evidence is absent; legacy PR ontology migration remains undefined; zero/one/three-finding escalation fixtures are incomplete; domain-specific control execution is partial; and merge order can invalidate PR #2 reconciliation evidence.
- Every current and still-material outdated finding must be resolved or explicitly dispositioned against the final frozen reconciled head before acceptance.

### Release
- The candidate remains blocked until reconciliation produces one mergeable immutable head; Socrates is removed or quarantined from the alpha scope; the deterministic suite passes; exact-head CI or independent clean replay succeeds; all blocking findings and adversarial fixtures pass; downstream consumers validate the accepted set; and provenance, checksums, rollback, review, and approval evidence is retained.
- PR #3 remains excluded from this release. Merging it before PR #2 reconciliation and freeze is not authorized because it would move the default branch and require a new compatibility-set conflict and exact-head evidence cycle.
- Consolidation, reconciliation, scope containment, governance isolation, documentation synchronization, and candidate remediation are review corrections, not release promotions.
- No release, tag, deployment, governance rollout, scheduled Inspector activation, or downstream compatibility claim is authorized from current candidate evidence alone.

### Deployment
- No deployment surface is authorized; consumers retrieve only an approved, versioned declarative artifact set.
- Governance workflows, scheduled Inspector execution, and automated issue mutation remain undeployed and must not be enabled through the compatibility-set release path.

## Entry Format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable