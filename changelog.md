# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product

- 2026-07-23 — Added a capability-evidence and bounded self-edit review surface with status `DOCUMENTED_NOT_ADMITTED`, separating declaration, structural validity, fixture demonstration, benchmark demonstration, independent reproduction, admission eligibility, operational admission, and resulting-state verification.
- 2026-07-23 — Defined ordinary mutable-field adjustments, versioned migrations, immutable-policy changes, and prohibited authority-bearing changes as distinct review classes with exact-field delta, cumulative drift, external disposition, rollback, and restored-state requirements.
- 2026-07-23 — Recorded closed PR #14 as historical unmerged adapter evidence rather than an active QSIO integration or format-ownership path.
- 2026-07-21 — Added a genome admission and runtime projection profile that separates declarative validity, neutral conformance, Repository `1` operational admission, runtime/Fabric projection, bounded execution, canonical reconciliation, correction, revocation, and recovery.
- 2026-07-21 — Defined distinct identities for genome artifacts, revisions, manifests, policy commitments, admission requests, quarantine records, admission decisions, capabilities, runtime admissions, runtime instances, Fabric experiments, conformance runs, execution receipts, reconciliations, corrections, revocations, and recovery checkpoints.
- 2026-07-20 — Added a portfolio obstruction and gluing analysis for QSO-GENOMES, covering declarative identity, operational authority, generic QSO formats, digest scopes, lifecycle, mutation, freeze, manifest acceptance, downstream interpretation, QSIO adapters, public projections, correction, freshness, governance artifacts, evidence vocabulary, and recovery.
- 2026-07-20 — Added ADR-0003 proposing that genome and Sprite records remain declarative policy and identity data and cannot themselves grant credentials, capabilities, approvals, repository writes, releases, deployments, payments, or canonical operational state.
- 2026-07-20 — Reconciled documentation planning around the interacting PR #2 compatibility set, PR #12 identity migration, PR #13 repair path, historical PR #14 QSIO adapter, and PR #15 documentation candidate without approving a merge order or changing implementation scope.
- 2026-07-19 — Added a GitHub Pages-ready documentation candidate covering repository purpose, lifecycle vocabulary, architecture, contracts, diagrams, onboarding, security/governance, release evidence, operations/rollback, and architecture decisions. The change is documentation-only and does not alter the canonical review path, release scope, runtime behavior, or gate status.
- 2026-07-16 — Defined the MVP as a complete, deterministic Atlas/Nova/Orion/Lyra compatibility set with immutable policy, approved supervisory treatment, canonical hashes, and an independent consumer manifest.
- 2026-07-16 — Confirmed this repository remains declarative and data-only; executable behavior and payment authority are out of scope.
- 2026-07-16 — Advanced the objective from candidate creation to independent acceptance of PR #2, preserving QSO-GENOMES as the highest portfolio unblocker while requiring exact-head evidence.
- 2026-07-16 — Selected existing PR #2 as the single compatibility-set submission path and consolidated remediation there rather than opening a competing release PR.

### Architecture

- 2026-07-23 — Added a documentation-only `qso-genome-self-edit-review/v1` packet joining exact genome source, mutable-field scope, evidence level, independent review, consumer impact, ethics/privacy/security checks, rollback, and external admission review without creating authority.
- 2026-07-23 — Added Atlas, Nova, Orion, and Lyra declared-versus-demonstrated review prompts: assumption tracking, calibrated anomaly analysis, contract and rollback witnesses, and consent/manipulation-resistance evaluation.
- 2026-07-23 — Added capability-evidence pairwise and triple-overlap requirements so declaration→evidence→admission and self-edit→immutable-policy review→restored state cannot be collapsed into local validation.
- 2026-07-21 — Added `genome-admission-request/v0`, `genome-authority-admission/v0`, `genome-runtime-projection/v0`, and `genome-fabric-projection/v0` as documentation-only contract candidates.
- 2026-07-21 — Added an admission state machine that forbids automatic promotion from local validity or conformance to admission, from execution to reconciliation, or from freeze to active state.
- 2026-07-21 — Defined eight triple-overlap witnesses spanning Repository `1` admission, runtime/Fabric projection, neutral conformance, identity migration and caches, immutable policy and capabilities, correction/revocation propagation, emergency recovery, and replacement-environment re-admission.
- 2026-07-21 — Required wrong-device, wrong-workspace, wrong-runtime, stale, replayed, broadened-capability, partial-execution, failed-rollback, privacy-leak, and incomplete-recovery fixtures.
- 2026-07-20 — Defined pairwise contract candidates for genome→runtime, genome→Fabric, genome→QSIO/kernel, genome→Repository `1`, and genome→QSO-STUDIO/AionUi.
- 2026-07-20 — Defined six original triple-overlap witnesses: genome→runtime→Fabric; genome→Repository `1`→runtime; genome→QSIO/kernel→runtime; identity migration→alias resolver→cache; immutable policy→freeze/revocation→recovery; and public projection→interface→correction.
- 2026-07-20 — Proposed the lowest-coupling ownership split: QSO-GENOMES owns declarative genome contracts and genome-specific canonicalization; an approved kernel/package owns generic formats; QuantumStateObjects owns runtime interpretation; QSO-FABRIC owns collaboration; Repository `1` owns operational admission and capabilities; `ALISTAIRE-` owns constitutional governance; and interfaces own read-only presentation.
- 2026-07-20 — Documented that repository location, file names, passing tests, conformance, projection, display, and successful execution do not establish canonical ownership or authority.
- QSO-GENOMES remains an upstream contract dependency and must publish schema, version, digest, identity, migration, compatibility, admission, and projection boundaries before runtime integration claims proceed.
- The accepted set identity must bind all consumer-relevant manifest metadata or explicitly distinguish domain-separated digest scopes.
- Immutable protections must be pinned to approved protocol identity and contents; local additions fail closed when conflicting or duplicated.
- Manifest identity-bearing fields must be validated against source documents rather than trusted from generator metadata.
- JSON loading used for contract replay must reject duplicate keys, invalid UTF-8, non-finite constants, unsupported critical fields, and numeric overflow.

### Governance and identity

- 2026-07-23 — Required immutable ethics and forbidden capabilities to remain outside genome-writable state; passing schema, digest, fixture, benchmark, workflow, runtime, or interface checks cannot authorize self-approval, self-commit, self-admission, activation, or canonical acceptance.
- 2026-07-23 — Required emotional understanding, attachment, distress, vulnerability, roleplay, or relationship framing never to substitute for consent or authorize influence, coercion, or manipulation.
- 2026-07-23 — Required missing, conflicting, stale, replayed, unsupported, privacy-restricted, corrected, revoked, or failed-rollback evidence to remain explicit and fail closed.
- 2026-07-21 — Required Repository `1` or an approved successor to own operational admission, capability issuance, revocation, reconciliation, and recovery while QSO-GENOMES remains non-executing.
- 2026-07-21 — Required a valid genome to be re-admitted when device, workspace, runtime head, Fabric head, environment, capability, or recovery binding changes.
- 2026-07-20 — Recorded a material conflict between PR #2 Aequitas-oriented compatibility semantics and PR #12’s proposed removal of active Aequitas and Socrates governance surfaces with review responsibility transferred to Jacob Thomas Redmond.
- 2026-07-20 — Required an approved migration to distinguish historical provenance identity, declarative contract identity, current human authority, compatibility aliases, retired aliases, and operational principals.
- 2026-07-20 — Required correction, revocation, supersession, and downstream cache-invalidation evidence before a retired identity can be considered fully inactive.
- Candidate identity migrations remain proposals. Historical records remain reachable as provenance but do not grant active authority.

### Candidate implementation

- PR #2 proposes Atlas, Nova, Orion, and Lyra artifacts, immutable policy, supervisory bindings, deterministic canonicalization, a compatibility manifest, conformance tests, reports, provenance, and workflow configuration.
- PR #12 proposes removal of active Aequitas and Socrates governance identities and migration of review responsibility to Jacob Thomas Redmond.
- PR #13 proposes reconciliation and Consent Capacity Lock repairs; focused deduplication repairs later merged through PRs #16 and #18.
- Closed PR #14 preserves a disabled QSIO adapter proposal as historical evidence only; it is not an active integration candidate.
- PR #15 proposes documentation and exact-head documentation validation only, now including the genome admission/runtime projection and capability-evidence/self-edit review profiles.
- These changes are candidate evidence, not accepted capability, admission, publication, release, deployment, or downstream authority.

### Review findings

- Material findings now include active identity disposition, historical aliases, generic format ownership, genome-specific canonicalization, digest scopes, lifecycle mapping, mutation vocabulary, declared-versus-demonstrated capability evidence, benchmark scope, immutable-policy review, exact-field drift, external disposition, freeze and recovery semantics, manifest acceptance, Repository `1` admission, record-identity collapse, runtime/Fabric projection equivalence, downstream interpretation, QSIO package ownership, public/protected data boundaries, correction, revocation, freshness, evidence reason codes, replacement-environment re-admission, and portfolio recovery.
- Every current and still-material outdated finding must be resolved or explicitly dispositioned against one frozen reconciled head before compatibility acceptance.
- Shared positive, negative, stale, replay, unsupported-version, wrong-identity, wrong-device, wrong-workspace, wrong-runtime, tamper, broadened-capability, partial-failure, correction, revocation, freeze, recovery, and rollback fixtures remain required.

### Documentation

- 2026-07-23 — Added `docs/capability-evidence-and-self-edit-review.md`, its machine-readable profile, accessible Mermaid/prose graph, strict validator, sixteen hostile regressions, exact-head read-only workflow, retained artifacts, and fail-closed evidence gate.
- 2026-07-23 — Synchronized `taskchain.md`, `punchlist.md`, `release.md`, `changelog.md`, and Pages navigation with status `DOCUMENTED_NOT_ADMITTED`, historical PR #14 disposition, evidence levels, self-edit classes, external review, and rollback boundaries.
- 2026-07-23 — Proposed non-authoritative FYSA-120 subdivision `031-T — Declared-versus-demonstrated capability evidence and bounded self-edit conformance`.
- 2026-07-21 — Added `docs/genome-admission-and-runtime-projection-profile.md` and linked it from Pages navigation.
- 2026-07-21 — Updated `taskchain.md`, `punchlist.md`, `release.md`, `changelog.md`, and `mkdocs.yml` to align admission and projection boundaries with the portfolio contract graph.
- 2026-07-20 — Added `docs/obstruction-and-gluing.md` and linked it from Pages navigation and the landing page.
- 2026-07-20 — Added `docs/adr/0003-separate-declarative-identity-from-operational-authority.md`.
- 2026-07-20 — Updated planning and release documents to align with the current portfolio contract graph and unresolved decisions.
- Documentation remains explanatory and review-oriented; it does not activate Pages publication or alter genome artifacts, schemas, migrations, aliases, runtime behavior, credentials, capabilities, admissions, or canonical state.

### Release

- 2026-07-23 — Added capability-evidence and self-edit review as a `REVIEW / BLOCKED` release gate: the packet and exact-head validation exist, while frozen-head behavioral evidence, independent reproduction, external disposition, admission authority, rollback rehearsal, and resulting-state verification remain required.
- 2026-07-23 — Recorded historical PR #14 as `WITHDRAWN / HISTORICAL`; no adapter activation or compatibility authority survives closure.
- The candidate remains blocked until one merge and supersession order is approved, identity scope is settled, one mergeable immutable compatibility head exists, conformance and gluing fixtures pass, Repository `1` admission is approved, downstream consumers derive compatible projections, privacy and recovery controls are approved, and explicit publication approval is recorded.
- No release, tag, Pages publication, package publication, adapter activation, runtime integration claim, capability certification, admission profile activation, or downstream-authoritative manifest is authorized from current candidate evidence.

### Deployment

- No deployment surface is authorized; consumers may retrieve only an explicitly approved, versioned declarative artifact set.
- Governance workflows, scheduled review automation, capability issuance, admission services, remote writes, and runtime activation remain outside this documentation milestone.

## Entry format

- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
