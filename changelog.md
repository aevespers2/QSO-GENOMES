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

### Architecture
- QSO-GENOMES is the highest upstream contract blocker for the four-QSO portfolio and must publish schema/version/hash boundaries before runtime integration proceeds.
- PR #2 remains the sole review path; reconciliation should integrate current `main` into the existing branch without force-rewriting reviewed history unless the Architect explicitly approves and documents an alternative.
- The accepted set identity must bind all consumer-relevant manifest metadata, including the authoritative immutable protocol and migration, or explicitly distinguish separate digest scopes.
- Immutable protections must be derived from or proven equivalent to the approved immutable-ethics protocol, and local additions must fail closed when conflicting or duplicated.
- Manifest identity-bearing fields must be validated against source documents rather than trusted from hard-coded generator metadata.
- Aequitas references and review surfaces must be unique before set/dictionary normalization.

### Candidate implementation
- PR #2 proposes the missing Atlas genome, immutable baseline, Aequitas review binding, deterministic canonicalization, compatibility manifests, conformance tests, reports, provenance, and workflow configuration.
- Earlier branch evidence reports sixteen passing tests, a nine-artifact replay, and candidate set digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`.
- Candidate remediation includes exact four-genome enforcement, a versioned immutable-ethics migration, Aequitas reference/invariant validation, and reachable provenance work.
- More recent branch work appears to bind the immutable protocol and migration into an eleven-artifact candidate manifest and records focused deterministic replay.
- These remain candidate implementations and self-reported evidence: no mergeable final head, exact-head status checks, independent clean-checkout replay, accepted release identity, downstream verification, or publication approval exists.

### Repository health
- At review time, PR #2 head `8c65748cfaa9a213d29d7f03d250a3f797bbb1a1` was 62 commits ahead and 20 commits behind default-branch head `b6c2344bfba4cfd90583ce001d75020396d9603d`, with merge base `c6c6ccdd61391da5fae5a268022c510069016b33`.
- GitHub reported the PR non-mergeable and returned no combined status checks for the observed head.
- Reconciliation must record old base/head, method, conflict resolutions, retained changes, resulting immutable head, review-thread mapping, and renewed evidence.

### Review findings
- Current findings include complete immutable-statement enforcement, local-ethics conflict rejection, duplicate migration-path and Aequitas-surface rejection, source-derived manifest identities, digest-scope semantics, declared schema dependency, pip-cache setup, submitted-head checkout, exact-head provenance, and review-thread disposition.
- Candidate immutable-manifest binding may address part of the earlier set-completeness finding, but it cannot be accepted until it survives reconciliation and renewed exact-head review.
- Every finding must be resolved or explicitly dispositioned against the final frozen reconciled head before acceptance.

### Release
- The candidate remains blocked until PR reconciliation produces one mergeable immutable head; exact-head CI or independent clean replay succeeds; all blocking findings and adversarial fixtures pass; downstream consumers validate the accepted set; and provenance, checksums, rollback, review, and approval evidence is retained.
- Consolidation, reconciliation, and documentation synchronization are review corrections, not release promotions.
- No release, tag, deployment, or downstream compatibility claim is authorized from current candidate evidence alone.

### Deployment
- No deployment surface is authorized; consumers retrieve only an approved, versioned declarative artifact set.

## Entry Format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
