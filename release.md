# Release Plan

## Current Decision

Status: `BLOCKED — PR #2 ACCEPTANCE AND CONFORMANCE EVIDENCE`

QSO-GENOMES remains the portfolio's highest-priority declarative contract dependency. PR #2 proposes the previously missing Atlas genome plus immutable, Aequitas, canonicalization, manifest, test, report, and workflow artifacts, but no release is eligible. The review timeline now contains fifteen threads: four earlier provenance threads are resolved and outdated, while eleven remain unresolved, including one outdated release-sync thread and ten current integrity/workflow findings.

The candidate's exact accepted source state is still not established. This release record previously named `9de3db6a33308346d09b7004e6702e997dce9ba8`, while the latest submitted-state provenance review references a different reviewed state and finds that its recorded source commit is not an ancestor of that state. Exact-head status checks, workflow runs, and reachable provenance must therefore be re-established against one final immutable candidate before acceptance.

The objective remains independent acceptance or rejection of the submitted compatibility-set candidate. Reported local results are preserved as candidate evidence and are not treated as merged or release-verified capabilities.

## Versioning

- Scheme: Semantic Versioning for the compatibility set and machine-readable manifest.
- First eligible candidate: `0.1.0-alpha.1`.
- Compatible data corrections may be patches; compatible fields/genomes/fixtures are minor changes.
- Schema, immutable-ethics, forbidden-capability, canonicalization, manifest-identity, or reference breaks require a declared major/breaking version and migration fixtures.
- The accepted release must distinguish any artifact-only digest from the identity of the full manifest metadata consumers rely on.

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
- validation reports for schemas, immutable contracts, Aequitas, and the manifest.

These items are selected as candidate review inputs only. They are not accepted completed work until current findings are resolved and an independent replay verifies the exact reviewed state.

## Planned Changelog Entries

- `Added`: accepted four-genome set, compatibility manifest, validator, workflow, and conformance fixtures.
- `Security`: immutable ethics, forbidden capabilities, fail-closed references/versions, duplicate-reference rejection, and data-only boundary checks.
- `Changed`: canonicalization, compatibility, manifest-identity, and migration policy.
- `Fixed`: provenance pointers, exact-set validation, immutable-policy drift, Aequitas invariant/reference checks, dependency declaration, pip-cache setup, and PR-head checkout semantics.
- `Release`: clean replay reports, downstream-consumer reports, source artifact, checksums, provenance, rollback instructions, and approval.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Candidate review | FAIL | Resolve or explicitly disposition the eleven currently unresolved PR #2 review threads against one final immutable head. |
| Set completeness | REVIEW | Atlas, Nova, Orion, and Lyra are present in the candidate; validation must assert that exact required set and reject omissions, renames, extras where prohibited, and stale references. |
| Immutable policy | FAIL | Full approved immutable-ethics statements and versioned variants are source-derived or proven equivalent; the candidate cannot enforce a weaker parallel baseline. |
| Aequitas integrity | FAIL | Published invariants mirror source artifacts; references are unique, path-correct, source-consistent, and validated before de-duplication. |
| Provenance | FAIL | The final reviewed head and every report's generator, manifest, test, schema, and source state are mutually reachable and reproducible. |
| Dependencies/environment | FAIL | Supported Python versions and all required dependencies are checked in through reproducible installation instructions or standard-library-only tooling. |
| CI semantics | FAIL | Workflow setup succeeds without missing cache inputs and certifies the PR head or explicitly records both submitted and synthetic merge SHAs. |
| Canonicalization/identity | REVIEW | Repeated serialization is deterministic and the release identity binds all consumer-relevant manifest metadata or clearly scopes separate digest types. |
| Negative fixtures | INCOMPLETE | Immutable mutation, unknown field, unresolved/duplicate reference, incompatible version, missing artifact, and canonicalization drift fail closed. |
| Downstream consumption | BLOCKED | `QuantumStateObjects` and `QSO-FABRIC` independently accept the exact published set and reject stale, altered, missing, or incompatible artifacts. |
| Status checks | NO EVIDENCE | One final immutable candidate head has attached passing checks and retained workflow logs. |
| Approval | PENDING | Explicit release approval after all blocking gates pass. |

## Artifact Requirements

- Versioned schemas, four canonical genomes, ethics protocols, immutable baseline/equivalence record, and Aequitas definition.
- Machine-readable compatibility manifest with stable paths, references, schema versions, canonicalization, identity semantics, and hashes.
- Validator plus positive/negative/boundary/migration fixture bundle and deterministic report.
- Exact-head CI logs, clean-checkout report, downstream-consumer reports, source archive, security-boundary report, SBOM where applicable, SHA-256 checksums, provenance, and rollback instructions.

## Rollback Criteria

Rollback or reject the candidate if any required genome is missing, hashes or manifest identity change without approved versioning, immutable protections are weakened, forbidden capabilities are absent/inconsistent, Aequitas references or invariants drift, duplicate/stale references pass, dependencies are undeclared, CI certifies the wrong source state, provenance points to an unreachable or sibling commit, incompatible consumers do not fail closed, or executable authority is introduced. Restore the previous reviewed declarative state and preserve rejected manifests, fixtures, reports, workflow logs, hashes, and review dispositions.

## Unresolved Blockers

- Eleven PR #2 review threads remain unresolved; one is outdated but not formally resolved and ten are current.
- The final immutable candidate head is not consistently identified across the release record and latest provenance review.
- The replacement submitted-state provenance record still points to a source state that review finds is not reachable from the reviewed candidate.
- Exact four-genome set assertion, full immutable-protocol equivalence, Aequitas invariant and duplicate-reference validation, and complete digest identity semantics are not accepted.
- The workflow's pip cache can fail without a dependency file and pull-request checkout can certify a synthetic merge instead of the submitted head.
- Exact-head status checks/workflow runs, clean-checkout replay, remaining fail-closed fixtures, downstream-consumer verification, checksums, provenance, and rollback evidence remain incomplete.

## Release Log

- 2026-07-16: Confirmed the complete four-genome contract as the highest-priority portfolio unblocker.
- 2026-07-16: Advanced the objective to independent acceptance of PR #2 after the candidate supplied the missing artifact set; held release `BLOCKED` because review, CI, provenance, immutable-policy, manifest-identity, and downstream-consumer gates remain incomplete.
- 2026-07-16: Synchronized partial review progress: four prior provenance threads are resolved/outdated, eleven remain unresolved, and replacement submitted-state provenance still fails the reachable-source-state requirement. No priority or release decision changed.
