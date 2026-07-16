# QSOBuilder Punch List

The Architect controls dependency order in `taskchain.md`. Execute only the first unblocked item and attach reproducible evidence.

## Immediate
- [x] Run schema validation for Atlas, Nova, Orion, and Lyra.
- [x] Verify immutable ethics and required forbidden-capability sets are identical where intended.
- [x] Validate Aequitas Sprite references and external-review activation rules.
- [x] Generate a deterministic contract manifest with paths, schema versions, and canonical hashes.
- [ ] Add negative fixtures for immutable-field mutation and incompatible schema versions. Blocked until P1 publishes the reviewed compatibility manifest.

## Held behind approval
- [ ] Payment-policy genome fields remain blocked until the settlement boundary and migration policy are approved.

## Quality Gates
- [x] Genomes remain declarative data only.
- [x] No shell, network, credential, package-installation, repository-write, or self-replication authority is introduced.
- [x] Every completed item records the exact command, result, commit, and hash set.

## Evidence Log

- 2026-07-16 — Added `genomes/atlas.json` and validated Atlas, Lyra, Nova, and Orion with `jsonschema 4.26.0` using `Draft202012Validator`; all four passed. Evidence: `reports/p0-four-genome-schema-validation.md`. Atlas implementation commit: `807261a1e1313b61cf7f877ae9afb675c2a4ec18`.
- 2026-07-16 — Added a normative immutable baseline plus five standard-library tests. Verified shared ethics slots, approved specialization slots, the ordered fifteen-item forbidden-capability set, identity, safety priority, and immutable object shape across all four genomes; all tests passed. Evidence: `reports/p0-immutable-contract-validation.md`. Contract commit: `3536d5d4b49e4656f4dc406343eee1d686cfc90a`; test commit: `e11c4109fda7efd56ac2065bb236286b66a2ab71`.
- 2026-07-16 — Added `contracts/aequitas-review-binding.json` and five standard-library tests for path/identifier resolution, complete oversight-surface coverage, non-executing Sprite authority, external human-review activation, fail-closed missing review, and four-genome external-commit/mutation boundaries. All five tests passed. Evidence: `reports/p0-aequitas-review-binding-validation.md`. Binding commit: `c952ac0d993db83309312ed20895e18b5b26e9b6`; test commit: `454db0855e843395f5244e2fc98f92b2945f1ce4`; evidence commit: `ed083bce0db6cbf97d1945faf1f3153f05976fed`.
- 2026-07-16 — Added `qso-canonical-json-v1`, a nine-artifact candidate manifest, and six deterministic manifest tests. The complete sixteen-test suite passed, manifest replay passed, and the compatibility-set digest is `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`. Evidence: `reports/p0-contract-manifest-validation.md`. Generator commit: `5af944da48456b695d4cb53abd55bfc1f64ddd06`; manifest commit: `73049e07188b00a0a4821f9bb5ce6a3675b40a5c`; test commit: `4b69dfe3b38ce6859f03812d3c56e66b1952e51d`; evidence commit: `c772d8eabfc1951e97d85482aa3553bc5365e76b`.
