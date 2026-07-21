# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product

- 2026-07-20 — Added a portfolio obstruction and gluing analysis for QSO-GENOMES, covering declarative identity, operational authority, generic QSO formats, digest scopes, lifecycle, mutation, freeze, manifest acceptance, downstream interpretation, QSIO adapters, public projections, correction, freshness, governance artifacts, evidence vocabulary, and recovery.
- 2026-07-20 — Added ADR-0003 proposing that genome and Sprite records remain declarative policy and identity data and cannot themselves grant credentials, capabilities, approvals, repository writes, releases, deployments, payments, or canonical operational state.
- 2026-07-20 — Reconciled documentation planning around the interacting PR #2 compatibility set, PR #12 identity migration, PR #13 repair path, PR #14 QSIO adapter, and PR #15 documentation candidate without approving a merge order or changing implementation scope.
- 2026-07-19 — Added a GitHub Pages-ready documentation candidate covering repository purpose, lifecycle vocabulary, architecture, contracts, diagrams, onboarding, security/governance, release evidence, operations/rollback, and architecture decisions. The change is documentation-only and does not alter the canonical review path, release scope, runtime behavior, or gate status.
- 2026-07-16 — Defined the MVP as a complete, deterministic Atlas/Nova/Orion/Lyra compatibility set with immutable policy, approved supervisory treatment, canonical hashes, and an independent consumer manifest.
- 2026-07-16 — Confirmed this repository remains declarative and data-only; executable behavior and payment authority are out of scope.
- 2026-07-16 — Advanced the objective from candidate creation to independent acceptance of PR #2, preserving QSO-GENOMES as the highest portfolio unblocker while requiring exact-head evidence.
- 2026-07-16 — Selected existing PR #2 as the single compatibility-set submission path and consolidated remediation there rather than opening a competing release PR.

### Architecture

- 2026-07-20 — Defined pairwise contract candidates for genome→runtime, genome→Fabric, genome→QSIO/kernel, genome→Repository `1`, and genome→QSO-STUDIO/AionUi.
- 2026-07-20 — Defined six triple-overlap witnesses: genome→runtime→Fabric; genome→Repository `1`→runtime; genome→QSIO/kernel→runtime; identity migration→alias resolver→cache; immutable policy→freeze/revocation→recovery; and public projection→interface→correction.
- 2026-07-20 — Proposed the lowest-coupling ownership split: QSO-GENOMES owns declarative genome contracts and genome-specific canonicalization; an approved kernel/package owns generic formats; QuantumStateObjects owns runtime interpretation; QSO-FABRIC owns collaboration; Repository `1` owns operational admission and capabilities; `ALISTAIRE-` owns constitutional governance; and interfaces own read-only presentation.
- 2026-07-20 — Documented that repository location, file names, passing tests, and successful execution do not establish canonical ownership or authority.
- QSO-GENOMES remains an upstream contract dependency and must publish schema, version, digest, identity, migration, and compatibility boundaries before runtime integration claims proceed.
- The accepted set identity must bind all consumer-relevant manifest metadata or explicitly distinguish domain-separated digest scopes.
- Immutable protections must be pinned to approved protocol identity and contents; local additions fail closed when conflicting or duplicated.
- Manifest identity-bearing fields must be validated against source documents rather than trusted from generator metadata.
- JSON loading used for contract replay must reject duplicate keys, invalid UTF-8, non-finite constants, unsupported critical fields, and numeric overflow.

### Governance and identity

- 2026-07-20 — Recorded a material conflict between PR #2 Aequitas-oriented compatibility semantics and PR #12’s proposed removal of active Aequitas and Socrates governance surfaces with review responsibility transferred to Jacob Thomas Redmond.
- 2026-07-20 — Required an approved migration to distinguish historical provenance identity, declarative contract identity, current human authority, compatibility aliases, retired aliases, and operational principals.
- 2026-07-20 — Required correction, revocation, supersession, and downstream cache-invalidation evidence before a retired identity can be considered fully inactive.
- Candidate identity migrations remain proposals. Historical records remain reachable as provenance but do not grant active authority.

### Candidate implementation

- PR #2 proposes Atlas, Nova, Orion, and Lyra artifacts, immutable policy, supervisory bindings, deterministic canonicalization, a compatibility manifest, conformance tests, reports, provenance, and workflow configuration.
- PR #12 proposes removal of active Aequitas and Socrates governance identities and migration of review responsibility to Jacob Thomas Redmond.
- PR #13 proposes reconciliation and Consent Capacity Lock repairs; focused deduplication repairs later merged through PRs #16 and #18.
- PR #14 proposes a disabled QSIO adapter mapping genome identity, lineage, revisions, traits, provenance, projections, commitments, and validation records.
- PR #15 proposes documentation and exact-head documentation validation only.
- These changes are candidate evidence, not accepted capability, publication, release, deployment, or downstream authority.

### Review findings

- Material findings now include active identity disposition, historical aliases, generic format ownership, genome-specific canonicalization, digest scopes, lifecycle mapping, mutation vocabulary, freeze and recovery semantics, manifest acceptance, Repository `1` admission, downstream interpretation, QSIO package ownership, public/protected data boundaries, correction, revocation, freshness, evidence reason codes, and portfolio recovery.
- Every current and still-material outdated finding must be resolved or explicitly dispositioned against one frozen reconciled head before compatibility acceptance.
- Shared positive, negative, stale, replay, unsupported-version, wrong-identity, tamper, partial-failure, correction, revocation, and rollback fixtures remain required.

### Documentation

- 2026-07-20 — Added `docs/obstruction-and-gluing.md` and linked it from Pages navigation and the landing page.
- 2026-07-20 — Added `docs/adr/0003-separate-declarative-identity-from-operational-authority.md`.
- 2026-07-20 — Updated `taskchain.md`, `punchlist.md`, `release.md`, `changelog.md`, `docs/index.md`, and `mkdocs.yml` to align with the current portfolio contract graph and unresolved decisions.
- Documentation remains explanatory and review-oriented; it does not activate Pages publication or alter genome artifacts, schemas, migrations, aliases, runtime behavior, credentials, capabilities, or canonical state.

### Release

- The candidate remains blocked until one merge and supersession order is approved, identity scope is settled, one mergeable immutable compatibility head exists, conformance and gluing fixtures pass, downstream consumers replay the same set, Repository `1` admission remains distinct from local validity, privacy and recovery controls are approved, and explicit publication approval is recorded.
- No release, tag, Pages publication, package publication, adapter activation, runtime integration claim, or downstream-authoritative manifest is authorized from current candidate evidence.

### Deployment

- No deployment surface is authorized; consumers may retrieve only an explicitly approved, versioned declarative artifact set.
- Governance workflows, scheduled review automation, capability issuance, remote writes, and runtime activation remain outside this documentation milestone.

## Entry format

- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
