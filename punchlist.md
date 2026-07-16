# QSOBuilder Punch List

The Architect controls dependency order in `taskchain.md`. Execute only the first unblocked item and attach reproducible evidence.

## Immediate
- [x] Run schema validation for Atlas, Nova, Orion, and Lyra.
- [x] Verify immutable ethics and required forbidden-capability sets are identical where intended.
- [ ] Validate Aequitas Sprite references and external-review activation rules.
- [ ] Generate a deterministic contract manifest with paths, schema versions, and canonical hashes.
- [ ] Add negative fixtures for immutable-field mutation and incompatible schema versions.

## Held behind approval
- [ ] Payment-policy genome fields remain blocked until the settlement boundary and migration policy are approved.

## Quality Gates
- [ ] Genomes remain declarative data only.
- [ ] No shell, network, credential, package-installation, repository-write, or self-replication authority is introduced.
- [ ] Every completed item records the exact command, result, commit, and hash set.

## Evidence Log

- 2026-07-16 — Added `genomes/atlas.json` and validated Atlas, Lyra, Nova, and Orion with `jsonschema 4.26.0` using `Draft202012Validator`; all four passed. Evidence: `reports/p0-four-genome-schema-validation.md`. Atlas implementation commit: `807261a1e1313b61cf7f877ae9afb675c2a4ec18`.
- 2026-07-16 — Added a normative immutable baseline plus five standard-library tests. Verified shared ethics slots, approved specialization slots, the ordered fifteen-item forbidden-capability set, identity, safety priority, and immutable object shape across all four genomes; all tests passed. Evidence: `reports/p0-immutable-contract-validation.md`. Contract commit: `3536d5d4b49e4656f4dc406343eee1d686cfc90a`; test commit: `e11c4109fda7efd56ac2065bb236286b66a2ab71`.
