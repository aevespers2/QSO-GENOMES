# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product
- 2026-07-16 — Defined the MVP as a complete, deterministic Atlas/Nova/Orion/Lyra compatibility set with immutable ethics, Aequitas references, canonical hashes, and an independent consumer manifest.
- 2026-07-16 — Confirmed this repository remains declarative and data-only; executable behavior and payment authority are out of scope.
- 2026-07-16 — Advanced the objective from candidate creation to independent acceptance of PR #2, preserving QSO-GENOMES as the highest portfolio unblocker while requiring exact-head evidence.
- 2026-07-16 — Selected existing PR #2 as the single canonical compatibility-set submission path and consolidated remediation there rather than opening a competing release PR.
- 2026-07-16 — Kept portfolio priority unchanged after consolidation. The intended acceptance scope remains manifest identity, immutable binding, duplicate/conflict validation, reproducible dependencies, exact-head CI, review disposition, and downstream replay.
- 2026-07-16 — Changed the local execution order after GitHub reported PR #2 non-mergeable and diverged from `main`: provenance-preserving branch reconciliation and one frozen submitted head now precede further exact-head remediation.
- 2026-07-17 — Classified draft PR #3 as a separate governance control-plane candidate. Its exact-head ontology workflow passed, but governance adoption does not supersede PR #2 reconciliation or compatibility-set acceptance.
- 2026-07-17 — Added an Architect merge-order decision gate: the recommended sequence is to keep PR #3 draft, reconcile and freeze PR #2 first, then refresh and revalidate PR #3 against the resulting `main`.

### Architecture
- QSO-GENOMES is the highest upstream contract blocker for the four-QSO portfolio and must publish schema/version/hash boundaries before runtime integration proceeds.
- PR #2 remains the sole compatibility-set review path; reconciliation should integrate current `main` into the existing branch without force-rewriting reviewed history unless the Architect explicitly approves and documents an alternative.
- PR #3 is a separate repository-governance change, not a compatibility-set release path. It must not create a competing acceptance head or silently widen PR #2's data-only scope.
- The accepted set identity must bind all consumer-relevant manifest metadata, including the authoritative immutable protocol and migration, or explicitly distinguish separate digest scopes.
- Immutable protections must be derived from or proven equivalent to the approved immutable-ethics protocol, and local additions must fail closed when conflicting or duplicated.
- Manifest identity-bearing fields must be validated against source documents rather than trusted from hard-coded generator metadata.
- Aequitas references and review surfaces must be unique before set/dictionary normalization.

### Candidate implementation
- PR #2 proposes the missing Atlas genome, immutable baseline, Aequitas review binding, deterministic canonicalization, compatibility manifests, conformance tests, reports, provenance, and workflow configuration.
- Earlier branch evidence reports sixteen passing tests, a nine-artifact replay, and candidate set digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`.
- Candidate remediation includes exact four-genome enforcement, a versioned immutable-ethics migration, Aequitas reference/invariant validation, and reachable provenance work.
- PR #3 adds a machine-readable PR ontology, Change Analyst, PR Steward, independent Inspector, PR-body validation, retained evidence, and daily audit automation.
- At PR #3 head `c456434b660a380d67f5bcb8a56a46d21c1dc3e3`, workflow run `29556170567` completed successfully and retained artifact `pr-ontology-c456434b660a380d67f5bcb8a56a46d21c1dc3e3` with digest `sha256:41c7f2d090b4f0bc9da99940762c9fdf7808c328ca01fab6c495e99f04b401af`.
- These remain candidate implementations. The ontology workflow result verifies only the configured exact-head governance check; it does not establish portfolio-wide adoption, legacy-PR migration, semantic execution of every domain control, compatibility-set acceptance, release, or deployment.

### Repository health
- PR #2 is open and non-mergeable at head `cacd9dda3d4d9c933c917306374cdde0afdab991`.
- Against default-branch head `1901b0c303cc48f0ea2fa8bf76bf60cf9e1ba79d`, PR #2 is 69 commits ahead and 23 commits behind, with merge base `c6c6ccdd61391da5fae5a268022c510069016b33`.
- Merging PR #3 before PR #2 reconciliation would add default-branch drift and require renewed reconciliation counts and exact-head evidence.
- Reconciliation must record old base/head, method, conflict resolutions, retained changes, resulting immutable head, review-thread mapping, and renewed evidence.

### Review findings
- Current compatibility-set findings include complete immutable-statement enforcement, local-ethics conflict rejection, duplicate migration-path and Aequitas-surface rejection, source-derived manifest identities, digest-scope semantics, declared schema dependency, pip-cache setup, submitted-head checkout, exact-head provenance, and review-thread disposition.
- Governance follow-up includes legacy-PR ontology migration, semantic domain-control packages, default-branch schedule activation, and portfolio adoption review.
- Every finding must be resolved or explicitly dispositioned against the applicable final frozen head before acceptance.

### Release
- The compatibility-set candidate remains blocked until PR reconciliation produces one mergeable immutable head; exact-head CI or independent clean replay succeeds; all blocking findings and adversarial fixtures pass; downstream consumers validate the accepted set; and provenance, checksums, rollback, review, and approval evidence is retained.
- Draft PR #3 remains candidate governance only. Its successful workflow is evidence for review, not release or adoption authority.
- Consolidation, reconciliation, governance sequencing, and documentation synchronization are review corrections, not release promotions.
- No release, tag, deployment, or downstream compatibility claim is authorized from current candidate evidence alone.

### Deployment
- No deployment surface is authorized; consumers retrieve only an approved, versioned declarative artifact set.
- The scheduled Inspector becomes portfolio-relevant only after approved governance changes reach the default branch and legacy PR coverage is addressed.

## Entry Format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable