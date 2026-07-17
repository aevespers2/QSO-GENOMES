# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product
- 2026-07-16 — Defined the MVP as a complete, deterministic Atlas/Nova/Orion/Lyra compatibility set with immutable ethics, Aequitas references, canonical hashes, and an independent consumer manifest.
- 2026-07-16 — Confirmed this repository remains declarative and data-only; executable behavior and payment authority are out of scope.
- 2026-07-16 — Advanced the next objective from creating the missing compatibility set to independently accepting or rejecting PR #2. This preserves QSO-GENOMES as the highest portfolio unblocker while requiring evidence rather than accepting self-reported results.
- 2026-07-16 — Retained the same portfolio priority after partial review progress: four earlier provenance threads are resolved/outdated, but eleven review threads remain unresolved and acceptance is still blocked.
- 2026-07-16 — Refined P0 to require one canonical submitted review head before further acceptance work. Exact-set, immutable-migration, and Aequitas-integrity remediations currently exist on a fifteen-commit chain ahead of PR #2, so branch-only progress cannot close PR findings or unlock independent acceptance.

### Architecture
- QSO-GENOMES is the highest upstream contract blocker for the four-QSO portfolio and must publish schema/version/hash boundaries before runtime integration proceeds.
- The accepted set identity must bind all consumer-relevant manifest metadata, or explicitly distinguish an artifact-only digest from the full compatibility-manifest identity.
- Immutable protections must be derived from or proven equivalent to the approved immutable-ethics protocol; a weaker parallel baseline is not acceptable.
- All accepted remediations must converge on one submitted commit lineage so workflow, provenance, review-thread, manifest, and downstream evidence refer to the same immutable candidate.

### Candidate implementation
- PR #2 proposes the missing Atlas genome, an immutable baseline, an Aequitas review binding, deterministic canonicalization, a nine-artifact manifest, conformance tests, reports, and a workflow.
- PR #2 reports sixteen passing tests, a nine-artifact replay, and set digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`.
- Subsequent candidate work adds exact four-genome enforcement, an explicit immutable-ethics migration, and Aequitas reference/invariant validation on remediation head `8c3d4ad3a8fc8cae864586d873cca319225c3e1d`, which is fifteen commits ahead of PR #2 head `5a435807487fd713c87465f3d23aaf9cd7cdd2b4`.
- These remain candidate claims: the remediation chain is not the submitted PR head, no release approval exists, exact-head CI and downstream validation are not accepted, and review findings remain unresolved.

### Review findings
- Reachable submitted-state provenance must replace references to inaccessible, sibling, or non-ancestor source states.
- Validation must assert the exact Atlas/Nova/Orion/Lyra set rather than whatever JSON files happen to be present.
- Immutable tests must compare complete approved statements or explicit versioned variants and must not validate a weaker baseline than the published protocol.
- Aequitas tests must validate the published invariants, reject duplicate/stale references before de-duplication, and prove source consistency.
- Schema-validation dependencies must be declared or removed; the conformance workflow must not enable pip caching without a dependency file.
- Pull-request CI must check out or explicitly record the submitted head rather than silently certifying only a synthetic merge commit.
- Review-thread state currently records fifteen total threads, four resolved/outdated and eleven unresolved.
- The Architect must choose whether PR #2 advances to the consolidated remediation head or is superseded by a replacement PR with preserved review provenance; no additional remediation branch should be treated as accepted until that path is recorded.

### Release
- The candidate remains blocked until one canonical submitted head contains the intended fixes, review findings are resolved against it, clean-checkout/CI replay passes at that exact head, remaining fail-closed fixtures pass, downstream consumers validate the accepted set, and provenance/checksum/rollback evidence is retained.
- No release, tag, or downstream compatibility claim is authorized from the current PR or side-branch evidence alone.

### Deployment
- No deployment surface is authorized; consumers retrieve versioned declarative artifacts only.

## Entry Format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
