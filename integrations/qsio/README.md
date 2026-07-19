# QSIO Integration — QSO-GENOMES

Status: Phase 1–3 scaffold, disabled by default.

## Domain mapping

| Local concept | QSIO concept |
|---|---|
| genome definition / lineage identity | QSO descriptor |
| genesis, inheritance, or revision request | QSI |
| accepted immutable genome revision | QSIO |
| inheritance relation | Nexis |
| goal / trait objective | Telion |
| provenance, evidence, revision history | Memora |
| public trait projection | Lumen |
| protected trait commitment | Umbra commitment |
| validation result | Witness record |

Enable with `QSIO_INTEGRATION_ENABLED=true` only after compatibility, replay, and tamper tests pass. Genome files remain domain artifacts; accepted state changes must be derived from QSIO records rather than direct mutation.

## Compatibility and aliases

Existing genome, trait, genesis, and lineage terminology remains valid during migration. Aliases must resolve to stable `qso:genome:<local_id>` identifiers and must not generate new identities.

## Rollback

Disable the feature flag, stop submissions, preserve received QSIO records, and restore projections from the last accepted replay checkpoint. Kernel lifecycle authority, Canon evaluation, signatures, and ledger persistence remain outside this repository.
