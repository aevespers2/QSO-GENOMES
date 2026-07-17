# Release Plan

## Current Decision

Status: `BLOCKED — CANONICAL SUBMISSION, REVIEW, AND CONFORMANCE EVIDENCE REQUIRED`

QSO-GENOMES remains the portfolio's highest-priority declarative contract dependency. PR #2 proposes the previously missing Atlas genome plus immutable, Aequitas, canonicalization, manifest, test, report, and workflow artifacts, but no release is eligible. The review timeline contains fifteen threads: four earlier provenance threads are resolved and outdated; eleven remain unresolved, including one outdated release-sync thread, one provenance thread whose underlying ancestry defect is now repaired but not formally dispositioned, and nine current integrity/workflow findings.

The submitted PR head remains `5a435807487fd713c87465f3d23aaf9cd7cdd2b4`. A separate remediation chain ending at `8c3d4ad3a8fc8cae864586d873cca319225c3e1d` is fifteen commits ahead and zero behind that PR head. It contains candidate fixes for exact four-genome set enforcement, a versioned immutable-ethics migration, and Aequitas reference/invariant validation, but those changes are not on the submitted review head. Side-branch evidence cannot close PR findings, establish exact-head CI, or define the immutable release source.

The objective remains independent acceptance or rejection of one canonical compatibility-set candidate. Reported local results and remediation commits are preserved as candidate evidence and are not treated as merged or release-verified capabilities.

## Versioning

- Scheme: Semantic Versioning for the compatibility set and machine-readable manifest.
- First eligible candidate: `0.1.0-alpha.1`.
- Compatible data corrections may be patches; compatible fields, genomes, or fixtures are minor changes.
- Schema, immutable-ethics, forbidden-capability, canonicalization, manifest-identity, or reference breaks require a declared major/breaking version and migration fixtures.
- The accepted release must distinguish any artifact-only digest from the identity of the full manifest metadata consumers rely on.
- No version or tag may be assigned until one final submitted head is selected and every release artifact is generated from that immutable state.

## Release Scope

- Canonical Atlas, Nova, Orion, and Lyra genome documents.
- Genome/Sprite schemas, approved immutable and attribution ethics, forbidden-capability rules, and Aequitas references/invariants.
- Deterministic canonical JSON and SHA-256 hashes.
- Machine-readable manifest containing schema versions, stable paths, references, hashes, canonicalization, compatibility state, and identity-bearing metadata.
- Positive, negative, boundary, unknown-field, unresolved-reference, duplicate-reference, immutable-mutation, incompatible-version, and migration fixtures.
- Clean-checkout and CI replay at the exact submitted and accepted commit.
- Read-only downstream validation in `QuantumStateObjects` and `QSO-FABRIC`.

## Candidate Work Under Review

PR #2 reports:

- Atlas plus a nine-artifact compatibility-set candidate;
- an immutable baseline and Aequitas review binding;
- `qso-canonical-json-v1` canonicalization;
- sixteen passing tests and a nine-artifact manifest replay;
- set digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`;
- validation reports for schemas, immutable contracts, Aequitas, and the manifest;
- submitted-state provenance reachable from PR head `5a435807487fd713c87465f3d23aaf9cd7cdd2b4`.

The separate remediation chain through `8c3d4ad3a8fc8cae864586d873cca319225c3e1d` adds candidate exact-set enforcement, immutable migration evidence, and Aequitas integrity validation. These items are review inputs only. They are not accepted completed work until they are placed on one canonical submitted head, all applicable findings are resolved or dispositioned, and an independent replay verifies that exact immutable state.

## Planned Changelog Entries

- `Added`: accepted four-genome set, compatibility manifest, validator, workflow, and conformance fixtures.
- `Security`: immutable ethics, forbidden capabilities, fail-closed references/versions, duplicate-reference rejection, and data-only boundary checks.
- `Changed`: canonicalization, compatibility, manifest-identity, migration, and canonical-submission policy.
- `Fixed`: provenance pointers, exact-set validation, immutable-policy drift, Aequitas invariant/reference checks, dependency declaration, pip-cache setup, and PR-head checkout semantics.
- `Release`: clean replay reports, review-disposition record, downstream-consumer reports, source artifact, checksums, provenance, rollback instructions, and approval.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Canonical submission | FAIL | Advance PR #2 to the consolidated remediation state or open one replacement PR that explicitly supersedes it; all review, CI, provenance, reports, and release artifacts must refer to that exact final head. |
| Candidate review | FAIL | Resolve or explicitly disposition the eleven currently unresolved PR #2 review threads against one final immutable submitted head. |
| Set completeness | REVIEW | Atlas, Nova, Orion, and Lyra are present in the candidate; validation must assert that exact required set and reject omissions, renames, extras where prohibited, and stale references on the canonical submitted head. |
| Immutable policy | FAIL | The approved versioned immutable-ethics migration and full-protocol equivalence must be present, reviewed, and replayed on the canonical submitted head. |
| Aequitas integrity | FAIL | The fail-closed reference/invariant validator must be present on the canonical submitted head and prove unique, canonical, source-consistent references before de-duplication. |
| Provenance | PARTIAL | Recorded source state is reachable from current PR head, and the remediation chain descends from it; the final submitted head and every report's generator, manifest, test, schema, and source state must still be mutually reachable and reproducible. |
| Dependencies/environment | FAIL | Supported Python versions and all required dependencies are checked in through reproducible installation instructions or standard-library-only tooling. |
| CI semantics | FAIL | Workflow setup succeeds without missing cache inputs and certifies the submitted head or explicitly records both submitted and synthetic merge SHAs. |
| Canonicalization/identity | REVIEW | Repeated serialization is deterministic and the release identity binds all consumer-relevant manifest metadata or clearly scopes separate digest types. |
| Negative fixtures | INCOMPLETE | Immutable mutation, unknown field, unresolved/duplicate reference, incompatible version, missing artifact, and canonicalization drift fail closed. |
| Downstream consumption | BLOCKED | `QuantumStateObjects` and `QSO-FABRIC` independently accept the exact published set and reject stale, altered, missing, or incompatible artifacts. |
| Status checks | NO EVIDENCE | One final immutable submitted candidate head has attached passing checks and retained workflow logs. |
| Documentation | PARTIAL | Contract scope and review requirements are documented; clean-checkout use, consumer migration, limitations, recovery, and publication instructions must be verified against the final candidate. |
| Security | PARTIAL | The declarative/no-execution boundary is defined; independent checks must confirm no runtime, network, credential, repository-write, payment, or self-modification authority enters the final artifact set. |
| Approval | PENDING | Explicit release approval after all blocking gates pass. |

## Artifact Requirements

- Versioned schemas, four canonical genomes, ethics protocols, immutable migration/equivalence record, and Aequitas definition.
- Machine-readable compatibility manifest with stable paths, references, schema versions, canonicalization, identity semantics, and hashes.
- Validator plus positive, negative, boundary, migration, exact-set, and reference-integrity fixture bundles with deterministic reports.
- Review-thread disposition map tied to the final submitted head.
- Exact-head CI logs, clean-checkout report, downstream-consumer reports, source archive, security-boundary report, SBOM where applicable, SHA-256 checksums, provenance manifest, and rollback instructions.

## Rollback Criteria

Rollback or reject the candidate if the reviewed head and release head differ, side-branch fixes are claimed without submission, any required genome is missing, hashes or manifest identity change without approved versioning, immutable protections are weakened, forbidden capabilities are absent or inconsistent, Aequitas references or invariants drift, duplicate or stale references pass, dependencies are undeclared, CI certifies the wrong source state, provenance points to an unreachable or sibling commit, incompatible consumers do not fail closed, or executable authority is introduced. Restore the previous reviewed declarative state and preserve rejected manifests, fixtures, reports, workflow logs, hashes, review dispositions, and supersession records.

## Unresolved Blockers

- No canonical submitted acceptance head exists: PR #2 remains at `5a435807487fd713c87465f3d23aaf9cd7cdd2b4`, while the consolidated remediation state `8c3d4ad3a8fc8cae864586d873cca319225c3e1d` is fifteen commits ahead and not part of that PR.
- A decision is required to advance PR #2 to the consolidated remediation head or open a replacement PR that explicitly supersedes PR #2 while preserving review provenance.
- Eleven PR #2 review threads remain unresolved: one outdated release-sync thread, one now-repaired provenance finding awaiting formal disposition, and nine current substantive integrity/workflow findings.
- Exact four-genome set enforcement, immutable-protocol migration, and Aequitas integrity fixes exist only as candidate side-chain evidence until consolidated into the canonical submitted head.
- Complete digest identity semantics, declared dependencies, pip-cache-safe setup, and submitted-head checkout semantics remain unresolved.
- Exact-head status checks/workflow runs, clean-checkout replay, remaining fail-closed fixtures, downstream-consumer verification, checksums, final provenance, security boundary report, documentation verification, and rollback evidence remain incomplete.

## Release Log

- 2026-07-16: Confirmed the complete four-genome contract as the highest-priority portfolio unblocker.
- 2026-07-16: Advanced the objective to independent acceptance of PR #2 after the candidate supplied the missing artifact set; held release `BLOCKED` because review, CI, provenance, immutable-policy, manifest-identity, and downstream-consumer gates remain incomplete.
- 2026-07-16: Synchronized partial review progress: four prior provenance threads were resolved/outdated and eleven remained unresolved.
- 2026-07-16: Recorded current PR head `5a435807487fd713c87465f3d23aaf9cd7cdd2b4` and confirmed that submitted source state `9de3db6a33308346d09b7004e6702e997dce9ba8` is its ancestor by seven commits. Provenance improved from `FAIL` to `PARTIAL`.
- 2026-07-16: Added the canonical-submission gate after remediation work accumulated through `8c3d4ad3a8fc8cae864586d873cca319225c3e1d`, fifteen commits ahead of the unchanged PR #2 head. Release remains blocked until one submitted head contains the accepted fixes and passes exact-head review, CI, security, documentation, provenance, downstream, artifact, and rollback gates.
