# P0 Manifest Identity Digest Validation

Date: 2026-07-16

## Builder claim

This bounded task resolves the open compatibility-set digest semantics finding. The candidate set digest now identifies the complete versioned identity manifest rather than only artifact paths and artifact-byte hashes.

## Identity decision

Digest profile `qso-genomes-manifest-identity-v1` hashes one QSO Canonical JSON v1 payload containing:

- `manifest_version`;
- `compatibility_set_id`;
- the complete `canonicalization` object;
- the complete `set_digest` rules, including algorithm, profile, scope, and exclusions;
- every artifact descriptor and all of its identity-bearing fields: `artifact_id`, `canonical_bytes`, `kind`, `path`, `schema_version`, and canonical artifact `sha256`.

The only declared exclusions are:

- `status`, because candidate-to-accepted lifecycle promotion must not silently create a different compatibility set; and
- `set_sha256`, because including the digest value in its own input would be recursive.

The previous digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac` represented only the set ID plus artifact paths and artifact hashes. It is superseded for this candidate by complete-manifest identity digest:

`3583dd05506c8d2921554676f80140cd66efa23a83154dbf4536ed51e56d5ed6`

The canonical identity payload is 2,314 bytes.

## Changed artifacts

- `scripts/generate_contract_manifest.py`
- `manifests/qso-genomes-compatibility-v1.json`
- `tests/test_contract_manifest.py`
- `tests/test_manifest_identity_digest.py`

Reachable implementation and focused-test ancestor: `1ae9979fafe5211d8b3f7df0476f675f12e7e884`.

## Verification

Environment:

```text
CPython 3.13.5
Linux 4.4.0 x86_64
```

Commands:

```bash
python3 -m unittest -v tests/test_manifest_identity_digest.py
python3 -m py_compile scripts/generate_contract_manifest.py tests/test_manifest_identity_digest.py
```

Result:

```text
test_artifact_fields ... ok
test_excluded ... ok
test_identity_sections ... ok
test_replay ... ok
test_scope ... ok
Ran 5 tests in 0.002s
OK
digest 3583dd05506c8d2921554676f80140cd66efa23a83154dbf4536ed51e56d5ed6
identity_bytes 2314
```

The focused tests prove that changes to the manifest version, set ID, canonicalization rules, digest semantics, artifact list, or any artifact descriptor field change the set digest. They also prove that lifecycle status and the digest value itself are excluded exactly as declared.

## Limitations and residual gates

Direct GitHub cloning remained unavailable in the verification runner because DNS resolution for `github.com` failed. The focused test was therefore replayed in a repository-shaped local tree using the committed generator logic and manifest identity data. This is deterministic Builder evidence, not clean-checkout or CI acceptance.

This task does not add the later immutable-ethics migration artifact to the nine-artifact manifest, declare the schema-validation dependency, repair workflow caching or PR-head checkout semantics, resolve review threads, publish a tag, or authorize downstream runtime behavior. Those gates remain open.

## Rollback

Revert the four implementation/test commits beginning with `49051fb648f96ab2c8308c6b3a0772fb152dafc0` through `1ae9979fafe5211d8b3f7df0476f675f12e7e884`, restore the prior manifest, and retain this report as failed-candidate evidence. Do not reuse either digest for a different manifest identity.
