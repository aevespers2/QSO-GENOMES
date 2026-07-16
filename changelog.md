# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product
- 2026-07-16 — Defined the MVP as a complete, deterministic Atlas/Nova/Orion/Lyra compatibility set with immutable ethics, Aequitas references, canonical hashes, and an independent consumer manifest.
- 2026-07-16 — Confirmed this repository remains declarative and data-only; executable behavior and payment authority are out of scope.
- 2026-07-16 — Advanced the next objective from candidate creation to independent acceptance because PR #2 now contains the missing Atlas genome, immutable baseline, Aequitas review binding, canonicalization profile, and candidate compatibility manifest.
- 2026-07-16 — Preserved QSO-GENOMES as the highest portfolio priority; no downstream repository is unblocked until clean-checkout or CI replay, fail-closed fixtures, provenance, and explicit publication approval pass.

### Architecture
- QSO-GENOMES remains the highest upstream contract blocker for the four-QSO portfolio and must publish accepted schema/version/path/reference/hash boundaries before runtime integration proceeds.
- Corrected the acceptance sequence so negative and boundary fixtures precede publication rather than depending on a published manifest.

### Implementation
- PR #2 adds candidate Atlas, immutable-baseline, Aequitas-binding, canonicalization, manifest-generator, manifest, tests, and validation reports.
- Branch-local evidence reports four schema validations, sixteen combined tests, a nine-artifact manifest replay, and candidate set digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`.
- The verification environment was repository-shaped rather than a direct clean checkout because GitHub DNS resolution was unavailable; no GitHub status check or independent release acceptance is claimed.

### Release
- The candidate remains blocked until clean-checkout or CI replay succeeds, required adversarial and migration fixtures pass, the data-only security boundary and provenance are reviewed, one downstream consumer validates the exact set, and explicit approval promotes the manifest from candidate to accepted.

### Deployment
- No deployment surface is authorized; consumers may retrieve only an approved, versioned declarative compatibility set.

## Entry Format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable