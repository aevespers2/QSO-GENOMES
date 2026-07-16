# QSOBuilder Punch List

The Architect controls dependency order in `taskchain.md`. Execute only the first unblocked item and attach reproducible evidence.

## Immediate
- [ ] Run schema validation for Atlas, Nova, Orion, and Lyra.
- [ ] Verify immutable ethics and required forbidden-capability sets are identical where intended.
- [ ] Validate Aequitas Sprite references and external-review activation rules.
- [ ] Generate a deterministic contract manifest with paths, schema versions, and canonical hashes.
- [ ] Add negative fixtures for immutable-field mutation and incompatible schema versions.

## Held behind approval
- [ ] Payment-policy genome fields remain blocked until the settlement boundary and migration policy are approved.

## Quality Gates
- [ ] Genomes remain declarative data only.
- [ ] No shell, network, credential, package-installation, repository-write, or self-replication authority is introduced.
- [ ] Every completed item records the exact command, result, commit, and hash set.
