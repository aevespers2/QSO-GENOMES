# P0 Aequitas Review-Binding Validation

Date: 2026-07-16

## Scope

This bounded Builder task defines and validates the reference from the four declarative genomes to the Aequitas supervisory Sprite and its external human-review activation rules.

The binding is declarative data only. It grants no execution, network, credential, package-installation, repository-write, self-replication, genome-mutation, or immutable-ethics override authority.

## Added artifacts

- `contracts/aequitas-review-binding.json`
- `tests/test_aequitas_review_binding.py`

## Validated rules

- the Aequitas Sprite and Sprite schema paths resolve and identify schema version `1`;
- Atlas, Lyra, Nova, and Orion references resolve to the expected genome identifiers;
- the review surfaces cover input, interpretation, ontology, proposed-edit, and communication review;
- every enabled Aequitas oversight key is referenced by at least one review surface;
- Aequitas may annotate and block pending review but may not execute, modify a genome, write the repository, or override immutable ethics;
- activation is external-controller-only and requires a human reviewer;
- missing review fails closed to `block_pending_review`;
- only an `approve` decision permits an external controller to commit;
- all four genomes require hashes, rollback on violation, external commits, and prohibit purpose or immutable-field mutation.

## Verification command

```bash
python3 -m unittest tests/test_aequitas_review_binding.py -v
```

Environment:

```text
CPython 3.13.5
standard-library unittest and json only
```

Result:

```text
test_activation_is_external_human_review_and_fails_closed ... ok
test_all_genomes_keep_commit_and_mutation_outside_qso_control ... ok
test_references_resolve_and_match_identifiers ... ok
test_review_surfaces_cover_enabled_sprite_oversight ... ok
test_sprite_requires_review_and_has_no_execution_authority ... ok

Ran 5 tests in 0.002s
OK
```

Direct cloning was unavailable in the verification runner, so the command was replayed in a repository-shaped local tree populated from the fetched branch artifacts and preserving every field inspected by the test. A clean-checkout rerun or CI run remains a release gate; this task does not claim repository-wide CI evidence.

## Reachable submitted-state evidence

- submitted source state: `9de3db6a33308346d09b7004e6702e997dce9ba8`
- provenance record: `reports/submitted-state-provenance.md`

## Git blob set

- `contracts/aequitas-review-binding.json`: `53134c0e23752e99bda3f32712cf2dd72ae113bc`
- `tests/test_aequitas_review_binding.py`: `416b3ba7358090f8810bf53e0f9fea36912770e6`
- `sprites/aequitas.json`: `3503d58c2516435c7437783932b603a2a9bd99fe`
- `schema/qso-sprite.schema.json`: `d479c7b9c654072c0739dcf36ec81adb3c413977`
- `genomes/atlas.json`: `17b422726da0e6ca352f877daefa4244add7082f`
- `genomes/lyra.json`: `55e363b4e26fee4f237199f8d8b07117b85f3224`
- `genomes/nova.json`: `13bfe7b2e9e4c2779d6bf2050770cc2d5b68982f`
- `genomes/orion.json`: `b9ca3d010b01bf7cc75f8792e5c18a6542e4de43`

## Outcome

`PASS` for the bounded recorded run. Separate review findings for published invariant equivalence and duplicate/stale/path-inconsistent reference rejection remain open.
