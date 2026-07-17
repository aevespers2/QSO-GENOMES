# P0 Manifest Source-Identity Validation

## Scope

This bounded Builder change addresses the first unresolved PR #2 acceptance finding: derive or verify manifest artifact IDs, versions, and other identity-bearing fields against their source documents.

The manifest generator now fails closed unless every declared artifact identity resolves from the source artifact and matches the compatibility-set declaration:

- Aequitas binding: `binding_id` and `contract_version`
- immutable baseline: canonical path stem plus source `schema_version`
- immutable migration: `migration_id` and `migration_version`
- Atlas, Lyra, Nova, and Orion: `genome_id` and `schema_version`
- immutable ethics protocol: `protocol_id`, including its positive `-vN` version suffix
- genome and Sprite schemas: `$id` path plus `properties.schema_version.const`
- Aequitas Sprite: `sprite_id` and `schema_version`

Duplicate manifest paths and duplicate source-derived artifact IDs are rejected before manifest construction. Missing fields, non-positive versions, surrounding whitespace, malformed protocol version suffixes, source/declaration disagreement, and schema `$id` path drift are rejected.

## Candidate provenance

- Canonical PR: #2
- Base candidate head reviewed for this item: `46f3248d8f67b7f0cc734159d2fa0a27e6051ea7`
- Implementation and focused-test ancestor: `76b2c461e226bb18de152da5fba828ec313bad18`
- Canonicalization profile: `qso-canonical-json-v1`
- Candidate compatibility-set digest remains: `99f33227247ef39fef3e1c3206c8ea49b9be9af86148298f07bdbf00b0cd6921`

No artifact source bytes or committed manifest bytes were changed by this item. The generator resolves the same eleven artifact IDs and versions already present in the candidate manifest, so the existing path/hash set identity is preserved.

## Verification performed

Environment:

```text
CPython 3.13.5
Linux x86_64
standard library only
```

Commands:

```bash
python -m py_compile scripts/generate_contract_manifest.py tests/test_manifest_source_identity.py
python -m unittest -v tests/test_manifest_source_identity.py
python scripts/generate_contract_manifest.py
python scripts/generate_contract_manifest.py --check
```

Focused result:

```text
test_all_manifest_ids_and_versions_are_source_derived ... ok
test_genome_identity_drift_fails_closed ... ok
test_path_version_identity_drift_fails_closed ... ok
test_protocol_id_supplies_both_identity_and_version ... ok
test_schema_id_path_drift_fails_closed ... ok

Ran 5 tests in 0.044s
OK
```

The write/check replay reported eleven artifacts and identical generated/checked output in the local fixture. File SHA-256 values for the exact focused implementation content were:

```text
b8572ed2d1a803434a1de162faf49d19a42d4a4a91f83ce63add61f42d3420f6  scripts/generate_contract_manifest.py
05bbc873241fac17e48169074d5c5a84a12f2781e690eb5b76b67a21bde55101  tests/test_manifest_source_identity.py
```

The existing manifest test's stale hard-coded set digest was also corrected from an earlier candidate value to the current committed candidate digest `99f33227247ef39fef3e1c3206c8ea49b9be9af86148298f07bdbf00b0cd6921`.

## Evidence boundary

Direct GitHub cloning remained unavailable in the runner because DNS resolution for `github.com` failed. Verification therefore used the exact implementation/test bytes and a standard-library artifact fixture containing the same identity-bearing fields and path conventions. This is candidate evidence only; it is not the required exact-head clean-checkout or GitHub Actions acceptance replay.

## Residual gates

- run the complete suite from a clean checkout of the final reviewed head
- retain exact-head workflow URLs, logs, supported Python versions, and exit codes
- resolve the next manifest digest-scope finding
- disposition all review threads against the final head
- perform downstream read-only replay only after acceptance and publication gates pass
