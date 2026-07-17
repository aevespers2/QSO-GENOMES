# P0 Aequitas Reference Integrity Validation

Date: 2026-07-16

## Claimed task

Validate the published Aequitas invariants against their source artifacts and reject duplicate, stale, or path-inconsistent references before any de-duplication.

## Implementation

- Added `scripts/validate_aequitas_binding.py` using only the Python standard library.
- Strict JSON loading rejects duplicate object keys and non-finite numbers.
- Sprite and schema references must use canonical repository-relative POSIX paths and match the referenced source identifiers and schema version.
- Genome references are checked in input order before any set or mapping is constructed; duplicate identifiers and duplicate paths fail closed.
- Each genome reference must use the exact `genomes/<genome_id>.json` path and the source `genome_id` must match.
- The exact Atlas, Lyra, Nova, and Orion reference set is required.
- The complete published invariant-key set is required, and every invariant is compared directly with the Aequitas Sprite or all four genome source artifacts.

## Focused verification

Environment:

```text
CPython 3.13.5
Linux 4.4.0 x86_64, glibc 2.41
```

Commands:

```bash
python3 -m unittest -v tests/test_aequitas_reference_integrity.py
python3 scripts/validate_aequitas_binding.py --root .
python3 -m py_compile scripts/validate_aequitas_binding.py tests/test_aequitas_reference_integrity.py
```

Result:

```text
8 tests passed
PASS: Aequitas references and invariants are unique, canonical, and source-consistent
bytecode compilation passed
```

Covered failures:

- duplicate genome identifier before de-duplication;
- duplicate genome path before de-duplication;
- non-canonical or path-inconsistent reference;
- stale source identifier;
- published invariant/source disagreement;
- missing invariant;
- repository candidate binding acceptance.

## Provenance and limitations

Implementation/test head: `92dcc4b01c598248c72185b0352d8f4c8fdea9f2`.

Direct GitHub cloning remained unavailable in the verification runner because DNS resolution for `github.com` failed. The focused suite and command-line replay were executed under CPython 3.13.5 in a repository-shaped local tree containing the candidate binding and the exact source fields exercised by the validator. The committed repository test also validates the complete branch artifacts when run from a clean checkout or CI. No clean-checkout, workflow run, or commit-status acceptance is claimed.

## Residual gates

- define whether the compatibility-set digest covers artifact bytes only or the complete manifest and bind all identity-bearing metadata;
- declare or remove the schema-validation dependency;
- repair workflow caching and submitted-head certification;
- run the complete suite from a clean checkout or CI;
- resolve or disposition remaining review threads.
