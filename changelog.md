# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product
- 2026-07-16 — Defined the MVP as a complete, deterministic Atlas/Nova/Orion/Lyra compatibility set with immutable ethics, Aequitas references, canonical hashes, and an independent consumer manifest.
- 2026-07-16 — Confirmed this repository remains declarative and data-only; executable behavior and payment authority are out of scope.
- 2026-07-16 — Advanced the next objective from candidate creation to independent acceptance because PR #2 now contains the missing Atlas genome, immutable baseline, Aequitas review binding, canonicalization profile, and candidate compatibility manifest.
- 2026-07-16 — Preserved QSO-GENOMES as the highest portfolio priority; no downstream repository is unblocked until clean-checkout or CI replay, fail-closed fixtures, provenance, and explicit publication approval pass.
- 2026-07-16 — Chose the existing PR #2 as the single canonical acceptance path and fast-forwarded its branch to include the full remediation lineage, preserving the original review record rather than opening a competing pull request.

### Architecture
- QSO-GENOMES remains the highest upstream contract blocker for the four-QSO portfolio and must publish accepted schema/version/path/reference/hash boundaries before runtime integration proceeds.
- Corrected the acceptance sequence so negative and boundary fixtures precede publication rather than depending on a published manifest.
- The canonical submitted head is now the sole review target; branch-local or detached remediation commits are evidence only until reachable from that head.

### Implementation
- PR #2 adds candidate Atlas, immutable-baseline, Aequitas-binding, canonicalization, manifest-generator, manifest, tests, and validation reports.
- Branch-local evidence reports four schema validations, sixteen combined tests, a nine-artifact manifest replay, and candidate set digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`.
- The 15-commit remediation sequence was fast-forwarded from original PR head `5a435807487fd713c87465f3d23aaf9cd7cdd2b4` to `8c3d4ad3a8fc8cae864586d873cca319225c3e1d`, adding exact-set enforcement, immutable-ethics migration, Aequitas reference-integrity validation, and supporting evidence.
- The verification environment was repository-shaped rather than a direct clean checkout because GitHub DNS resolution was unavailable; no GitHub status check or independent release acceptance is claimed.

### Release
- The candidate remains blocked until clean-checkout or CI replay succeeds at the exact submitted head, required adversarial and migration fixtures pass, manifest identity and dependency semantics are accepted, review threads are dispositioned, the data-only security boundary and provenance are reviewed, one downstream consumer validates the exact set, and explicit approval promotes the manifest from candidate to accepted.
- Consolidating the PR head is a review-path correction, not a release promotion.

### Deployment
- No deployment surface is authorized; consumers may retrieve only an approved, versioned declarative compatibility set.

## Entry Format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
