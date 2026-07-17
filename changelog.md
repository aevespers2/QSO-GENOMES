# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product
- 2026-07-16 — Defined the MVP as a complete, deterministic Atlas/Nova/Orion/Lyra compatibility set with immutable ethics, Aequitas references, canonical hashes, and an independent consumer manifest.
- 2026-07-16 — Confirmed this repository remains declarative and data-only; executable behavior and payment authority are out of scope.
- 2026-07-16 — Advanced the objective from candidate creation to independent acceptance of PR #2, preserving QSO-GENOMES as the highest portfolio unblocker while requiring exact-head evidence.
- 2026-07-16 — Selected existing PR #2 as the single canonical submission path and fast-forwarded its branch through the fifteen-commit remediation lineage rather than opening a competing pull request.
- 2026-07-16 — Synchronized product, release, punch-list, and changelog directives on the default and PR branches; the submitted review head is `2d42c960cefb70fdaada969e75debf50fb06f36c`.
- 2026-07-16 — Kept portfolio priority unchanged after consolidation. The immediate P0 focus is manifest identity, immutable binding, duplicate/conflict validation, reproducible dependencies, exact-head CI, and review-thread disposition.

### Architecture
- QSO-GENOMES is the highest upstream contract blocker for the four-QSO portfolio and must publish schema/version/hash boundaries before runtime integration proceeds.
- The accepted set identity must bind all consumer-relevant manifest metadata, including the authoritative immutable protocol and migration, or explicitly distinguish separate digest scopes.
- Immutable protections must be derived from or proven equivalent to the approved immutable-ethics protocol, and local additions must fail closed when conflicting or duplicated.
- Manifest identity-bearing fields must be validated against source documents rather than trusted from hard-coded generator metadata.
- Aequitas references and review surfaces must be unique before set/dictionary normalization.

### Candidate implementation
- PR #2 proposes the missing Atlas genome, immutable baseline, Aequitas review binding, deterministic canonicalization, a compatibility manifest, conformance tests, reports, and a workflow.
- Earlier branch evidence reports sixteen passing tests, a nine-artifact replay, and candidate set digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`.
- The canonical submitted head includes exact four-genome enforcement, a versioned immutable-ethics migration, Aequitas reference/invariant validation, reachable provenance work, and synchronized product/release documentation.
- Additional focused reports record four exact-set tests, five migration tests, and eight Aequitas reference-integrity tests under CPython 3.13.5.
- These remain candidate claims: no exact-head workflow run, independent clean-checkout replay, accepted release identity, downstream verification, or publication approval exists.

### Review findings
- The current review timeline contains twenty threads: four resolved/outdated, one unresolved/outdated release-sync thread, and fifteen current unresolved findings.
- Existing blockers include complete immutable-statement enforcement, invariant/source validation, declared schema dependency, compatibility-set digest semantics, pip-cache setup, submitted-head checkout, duplicate reference rejection, and final reachable provenance.
- Consolidation surfaced five additional gaps: the manifest omits the immutable migration/protocol binding; local ethics conflicts are not rejected; artifact identifiers are not validated against source documents; duplicate migration paths can pass; and duplicate Aequitas review surfaces can pass.
- Every finding must be resolved or explicitly dispositioned against the final immutable submitted head before acceptance.

### Release
- The candidate remains blocked until exact-head CI or independent clean replay succeeds, all blocking findings and adversarial fixtures pass, downstream consumers validate the accepted set, and provenance/checksum/rollback evidence is retained.
- Consolidating and synchronizing the submission path is a review correction, not a release promotion.
- No release, tag, deployment, or downstream compatibility claim is authorized from current candidate evidence alone.

### Deployment
- No deployment surface is authorized; consumers retrieve only an approved, versioned declarative artifact set.

## Entry Format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
