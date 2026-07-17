# P0 Aequitas Review-Surface Integrity Validation

Date: 2026-07-16

## Scope

This bounded remediation addresses the next PR #2 acceptance finding: reject duplicate Aequitas review surfaces and conflicting oversight definitions before any set or map conversion can hide them.

The change remains data-validation only. It does not grant the Sprite execution, mutation, repository-write, credential, network, or commit authority.

## Implementation provenance

- Canonical PR branch: `builder/p0-four-genome-validation-20260716`
- Starting submitted head: `cacd9dda3d4d9c933c917306374cdde0afdab991`
- Validator commit: `aebedf5744211ed8cedcd3fd4f640211121d6351`
- Implementation/test head: `6c6ad0b02e83126c24411cc27e129cda8cc58bdc`
- `scripts/validate_aequitas_binding.py` Git blob: `670290e5630f416630708119b0d82af7aac683f3`
- `tests/test_aequitas_reference_integrity.py` Git blob: `c189e111ea4fef152b547ca8528fb5735a64c87d`

## Fail-closed behavior added

The standard-library validator now rejects:

1. duplicate review-surface identifiers before de-duplication;
2. repeated surface identifiers carrying different oversight lists as conflicting definitions;
3. duplicate oversight identifiers inside one surface before de-duplication;
4. unknown oversight identifiers not declared by the Aequitas Sprite;
5. required oversight whose Sprite source definition is disabled or non-boolean;
6. missing or unexpected review surfaces; and
7. incomplete coverage of enabled Sprite oversight definitions.

The accepted candidate surface set remains `input`, `interpretation`, `ontology`, `proposed_edit`, and `communication`. Oversight capabilities may be reused across different surfaces, but duplicates within one surface or multiple definitions for one surface fail closed.

## Verification

Environment:

```text
CPython 3.13.5
standard library only
```

Commands:

```bash
python3 -m py_compile \
  scripts/validate_aequitas_binding.py \
  tests/test_aequitas_reference_integrity.py

python3 -m unittest tests.test_aequitas_reference_integrity -v

python3 scripts/validate_aequitas_binding.py --root /tmp/qso_aequitas

sha256sum \
  scripts/validate_aequitas_binding.py \
  tests/test_aequitas_reference_integrity.py
```

Results:

```text
compile exit code: 0
14 tests run: PASS
validator replay exit code: 0
validator result: PASS
```

Focused negative coverage passed for duplicate surfaces, conflicting duplicate-surface definitions, duplicate per-surface oversight entries, unknown oversight definitions, disabled source definitions, and missing surfaces. Existing genome-reference, path, source-identity, and invariant tests also remained green.

Local SHA-256 values for the tested files:

```text
8bd3a84b67890a9ba5bc525b7b262a1117b54465d29257f6e075b916caef2dc8  scripts/validate_aequitas_binding.py
0d65fb023b86da76217a6049425a770731154515ddf34ad3eec49f5132657651  tests/test_aequitas_reference_integrity.py
```

## Evidence boundary

The verification runner could not perform a fresh GitHub clone. The commands above ran against an exact-byte mirror of the changed validator and test files plus an exact relevant-data fixture mirror of the Aequitas binding, Sprite oversight, schema-version source, and four genome fields consumed by this validator. This is reproducible candidate evidence, not independent clean-checkout or CI acceptance.

The compatibility manifest was not regenerated because this bounded change modifies validator and test code only, not any compatibility-set artifact bytes.

## Rollback

Revert commits `6c6ad0b02e83126c24411cc27e129cda8cc58bdc` and `aebedf5744211ed8cedcd3fd4f640211121d6351` to restore the prior validator and fixtures. No data migration or runtime rollback is required.

## Remaining gate

P0 remains in review. The next unblocked acceptance finding is to derive or verify manifest artifact IDs, versions, and other identity-bearing fields against their source documents. Exact-head clean-checkout or CI replay, review-thread disposition, and downstream read-only validation remain outstanding.
