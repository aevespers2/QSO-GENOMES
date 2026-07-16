# Task Chain

## Repository role

Canonical declarative genomes, immutable ethics, and supervisory Sprite definitions. This repository is an upstream dependency of `QuantumStateObjects` and `QSO-FABRIC` and contains data contracts rather than runtime behavior.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Independently verify and accept the four-genome compatibility-set candidate, then publish the accepted contract for downstream consumption.
- **User outcome:** A consuming runtime can validate Atlas, Nova, Orion, and Lyra against one reviewed schema/reference/canonicalization boundary and reproduce the exact compatibility-set digest without importing repository code.
- **MVP scope:** preserve the candidate artifacts in PR #2; replay validation from a clean checkout or CI; add positive, negative, boundary, unknown-field, unresolved-reference, immutable-mutation, incompatible-version, and canonicalization-drift fixtures; verify the data-only security boundary; publish the accepted manifest and one independent consumer smoke fixture.
- **Priority:** QSO-GENOMES remains the highest portfolio unblocker. The implementation focus changes from creating the candidate to independently accepting it because PR #2 now supplies Atlas, the immutable baseline, the Aequitas binding, canonicalization, and a candidate manifest.
- **Success criteria:** clean-checkout or CI replay passes at the reviewed commit; all required fail-closed fixtures pass; repeated canonicalization reproduces the recorded SHA-256 set digest; security and provenance reports are retained; the manifest is explicitly promoted from candidate to accepted; at least one downstream consumer validates the released hashes without executing repository code.
- **Non-goals:** runtime implementation, external access, credentials, autonomous policy changes, payment authority, financial operations, or treating branch-local test claims as release acceptance.
- **Release rationale:** The candidate materially removes the missing-Atlas blocker, but downstream integration must remain blocked until independent replay, adversarial fixtures, provenance, and explicit approval establish a stable contract boundary.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Produce the four-genome compatibility-set candidate | QSOBuilder | — | REVIEW | Atlas, Nova, Orion, and Lyra, the immutable baseline, Aequitas binding, canonicalization profile, candidate manifest, commands, and hashes are present in PR #2; branch evidence is preserved but not yet accepted as release evidence. |
| P1 | Complete independent conformance and security acceptance | Architect + Reviewer | P0 candidate artifacts | READY | A clean checkout or CI replays all validators; positive, negative, boundary, unknown-field, unresolved-reference, immutable-mutation, incompatible-version, and canonicalization-drift fixtures fail or pass as specified; no executable authority is introduced. |
| P2 | Publish the accepted manifest and downstream consumer fixture | QSOBuilder | P1 | PROPOSED | The manifest status/version and immutable digest are approved, release artifacts and provenance are retained, and an independent QuantumStateObjects or QSO-FABRIC fixture validates the exact set by schema version, path, reference, canonical bytes, and hash. |
| P3 | Define a declarative payment-policy extension | Architect | P2 and approved settlement boundary | BLOCKED | Any extension remains data-only and has approved versioning, migration, privacy, and authority boundaries. |

## Cross-repository gate

`QuantumStateObjects` and `QSO-FABRIC` may not claim a verified four-object integration until P0–P2 are `DONE` and the accepted hashes are consumed successfully. PR #2 is a candidate, not a published compatibility contract.

## Builder Log

- 2026-07-16 — Claimed P0's first unblocked item. Added `genomes/atlas.json`; validated Atlas, Lyra, Nova, and Orion against the Draft 2020-12 schema with `jsonschema 4.26.0`; all four passed. Evidence: `reports/p0-four-genome-schema-validation.md`.
- 2026-07-16 — Completed P0's immutable-contract item. Added `contracts/immutable-baseline.json` and `tests/test_immutable_contracts.py`; five standard-library tests passed. Evidence: `reports/p0-immutable-contract-validation.md`.
- 2026-07-16 — Completed P0's Aequitas reference and external-review item. Added `contracts/aequitas-review-binding.json` and `tests/test_aequitas_review_binding.py`; five standard-library tests passed. Evidence: `reports/p0-aequitas-review-binding-validation.md`.
- 2026-07-16 — Completed P0's deterministic-manifest item. Added `scripts/generate_contract_manifest.py`, `manifests/qso-genomes-compatibility-v1.json`, and six tests. All sixteen tests passed in a repository-shaped replay; manifest replay verified nine artifacts and set digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`. Evidence: `reports/p0-contract-manifest-validation.md`.
- 2026-07-16 — Product review retained QSO-GENOMES as the highest portfolio priority, moved the next objective to independent acceptance, and corrected the prior circular dependency that placed negative fixtures after manifest publication. P1 conformance work is now the next unblocked review task; publication remains P2.