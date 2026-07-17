# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product
- 2026-07-16 — Defined the MVP as a complete, deterministic Atlas/Nova/Orion/Lyra compatibility set with immutable ethics, Aequitas references, canonical hashes, and an independent consumer manifest.
- 2026-07-16 — Confirmed this repository remains declarative and data-only; executable behavior and payment authority are out of scope.
- 2026-07-16 — Advanced the objective from candidate creation to independent acceptance of PR #2, preserving QSO-GENOMES as the highest portfolio unblocker while requiring exact-head evidence.
- 2026-07-16 — Selected existing PR #2 as the single canonical submission path and consolidated remediation there rather than opening a competing release PR.
- 2026-07-16 — Kept portfolio priority unchanged after consolidation. The intended acceptance scope remains manifest identity, immutable binding, duplicate/conflict validation, reproducible dependencies, exact-head CI, review disposition, and downstream replay.
- 2026-07-16 — Changed the local execution order after GitHub reported PR #2 non-mergeable and diverged from `main`: provenance-preserving branch reconciliation and one frozen submitted head now precede further exact-head remediation.
- 2026-07-16 — Confirmed the local order again after the PR branch advanced by five additional remediation commits. This is not a portfolio reprioritization; it is a documented containment decision because continued head movement increases divergence and makes earlier exact-head evidence obsolete.

### Architecture
- QSO-GENOMES is the highest upstream contract blocker for the four-QSO portfolio and must publish schema/version/hash boundaries before runtime integration proceeds.
- PR #2 remains the sole review path; reconciliation should integrate current `main` and all intended candidate commits into the existing branch without force-rewriting reviewed history unless the Architect explicitly approves and documents an alternative.
- The accepted set identity must bind all consumer-relevant manifest metadata, including the authoritative immutable protocol and migration, or explicitly distinguish separate digest scopes.
- Immutable protections must be pinned to the approved protocol identity and contents, not merely to a digest stored in another editable candidate document; local additions must fail closed when conflicting or duplicated.
- Migration validation must bind the expected migration identity, source profile, protocol identity, immutable status, enforcement boundary, exact consumer requirements, and unique paths.
- Manifest identity-bearing fields must be validated against source documents rather than trusted from hard-coded generator metadata.
- Aequitas references, review surfaces, activation rules, and per-surface oversight mappings must be unique, approved, and source-consistent before normalization.
- JSON loading used for contract replay must reject non-finite constants and numeric overflow.

### Candidate implementation
- PR #2 proposes the missing Atlas genome, immutable baseline, Aequitas review binding, deterministic canonicalization, compatibility manifests, conformance tests, reports, provenance, and workflow configuration.
- Earlier branch evidence reports sixteen passing tests, a nine-artifact replay, and candidate set digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`.
- Candidate remediation includes exact four-genome enforcement, a versioned immutable-ethics migration, Aequitas reference/invariant validation, immutable protocol and migration inclusion in an eleven-artifact manifest, local-ethics conflict checks, and reachable provenance work.
- Five commits after head `cacd9dda3d4d9c933c917306374cdde0afdab991` further modify the Aequitas validator and tests, add an Aequitas review-surface report, and update branch-local task and punch-list records.
- Those five commits are implemented candidate hardening, not accepted capability. They do not change `tests/test_contract_manifest.py`; the hard-coded expected digest remains `6d9b0ca8c6766fbb63b4613df5b2baee455f1e63c848d6f75e56726efbc57cac` while the committed manifest reports `99f33227247ef39fef3e1c3206c8ea49b9be9af86148298f07bdbf00b0cd6921`.
- No mergeable final head, passing exact-head suite, accepted status check, independent clean-checkout replay, accepted release identity, downstream verification, or publication approval exists.

### Repository health
- At the latest observed snapshot, PR #2 head `46f3248d8f67b7f0cc734159d2fa0a27e6051ea7` was 74 commits ahead and 24 commits behind default-branch head `0ac8960db20dba6ef083d928a44f4ca756d44713`, with merge base `c6c6ccdd61391da5fae5a268022c510069016b33`.
- GitHub reported the PR open and non-mergeable and returned no combined status checks or pull-request workflow runs for the observed head.
- The review timeline contained 34 threads: four resolved/outdated and 30 unresolved, including 23 current findings and seven unresolved outdated findings.
- Snapshot counts are historical evidence, not stable identifiers. Reconciliation must recapture base, head, ahead/behind state, workflow state, and thread state immediately before work begins.
- Reconciliation must record old base/head, method, conflict resolutions, retained changes, resulting immutable head, review-thread mapping, and renewed evidence.

### Review findings
- Current findings include the failing manifest-digest assertion; complete immutable-statement enforcement; approved protocol-content pinning; migration source-profile, contract-ID, protocol-ID, status, boundary, exact-key, and unique-path checks; local-ethics conflict rejection; Aequitas identity, activation, per-surface oversight, duplicate-reference, duplicate-surface, and source-integrity checks; overflowed-number rejection; source-derived manifest identities; digest-scope semantics; declared schema dependency; pip-cache setup; submitted-head checkout; exact-head provenance; and review-thread disposition.
- The latest four review findings cover migration source-profile identity, migration contract identity, overflowed JSON numbers, and pinning the approved immutable-protocol contents.
- Candidate Aequitas review-surface hardening may address part of earlier uniqueness and oversight findings, but it cannot be accepted until it is reconciled, frozen, replayed, and reviewed against one exact head.
- Every current and still-material outdated finding must be resolved or explicitly dispositioned against the final frozen reconciled head before acceptance.

### Release
- The candidate remains blocked until PR reconciliation produces one mergeable immutable head; the deterministic suite passes; exact-head CI or independent clean replay succeeds; all blocking findings and adversarial fixtures pass; downstream consumers validate the accepted set; and provenance, checksums, rollback, review, and approval evidence is retained.
- Consolidation, reconciliation, documentation synchronization, and candidate remediation are review corrections, not release promotions.
- No release, tag, deployment, or downstream compatibility claim is authorized from current candidate evidence alone.

### Deployment
- No deployment surface is authorized; consumers retrieve only an approved, versioned declarative artifact set.

## Entry Format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable