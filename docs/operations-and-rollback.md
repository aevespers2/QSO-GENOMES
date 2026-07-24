# Operations and rollback

## Operational scope

QSO-GENOMES does not operate a production service. Its operational responsibilities are artifact integrity, evidence preservation, publication correctness, incident triage, supersession, and rollback coordination with downstream consumers.

## Normal operating cycle

1. Maintain one authoritative task chain and release record.
2. Review bounded contract changes on the correct path.
3. Freeze the candidate head before final evidence collection.
4. Reproduce validation from a clean environment.
5. Obtain independent review and downstream replay.
6. Publish a versioned artifact and evidence bundle only after approval.
7. Monitor reports from consumers for identity, parsing, digest, migration, or rejection disagreements.
8. Supersede or roll back through an explicit versioned record.

## Incident severity

| Severity | Example | Required response |
|---|---|---|
| Critical | released immutable rule is weakened; unapproved authority is accepted; source or evidence is compromised | stop consumption, preserve evidence, revoke or supersede release, notify downstream owners |
| High | set digest mismatch; wrong-head evidence; consumers disagree; missing required artifact | block new use, quarantine release, reproduce independently, prepare rollback |
| Medium | incomplete documentation, ambiguous metadata, non-release fixture defect | block promotion, correct candidate, renew affected evidence |
| Low | editorial defect with no contract or lifecycle effect | correct through normal review and record in changelog |

## First response

When an integrity concern is reported:

1. Record the report time, reporter, affected version, manifest identity, source commit, and observed digest.
2. Preserve the exact artifact bundle, logs, consumer state, and error output.
3. Stop publication or promotion of the affected candidate.
4. Determine whether existing consumers must halt, quarantine, or continue in a restricted safe state.
5. Reproduce the issue from a clean checkout without modifying the evidence source.
6. Classify whether the defect affects source contracts, manifest identity, validation, evidence, documentation, or downstream interpretation.
7. Open a bounded repair or rollback path with explicit owner and approval requirements.

## Quarantine conditions

Quarantine a candidate or release when:

- the source commit cannot be confirmed;
- artifact or set checksums differ;
- the manifest contains an undeclared artifact;
- a required artifact or reference is missing;
- a supervisory identity or authority is not approved;
- immutable policy differs from the accepted version;
- strict parsers disagree;
- canonicalization cannot be reproduced;
- CI evaluated a different head;
- downstream consumers produce different acceptance decisions;
- evidence or review disposition is incomplete.

Quarantine is not deletion. Preserve all relevant material for diagnosis and audit.

## Rollback strategy

### Candidate rollback

For an unreleased candidate:

- return the pull request to draft if necessary;
- stop head movement while the defect is assessed;
- preserve the failing head and review threads;
- revert or supersede the bounded change on the same canonical review path;
- update fixtures, documentation, task chain, release plan, and changelog;
- freeze a new head and repeat all affected evidence.

### Released-version rollback

For a published version:

1. Mark the version rejected, withdrawn, or superseded in an immutable record.
2. Publish a machine-readable notice identifying the affected manifest, digests, reason, and effective time.
3. Direct consumers to the last accepted compatible version or a safe halted state.
4. Verify that consumers reject the withdrawn identity.
5. Preserve the original bundle and all incident evidence.
6. Produce a corrected version through the full release gate sequence.
7. Record migration and compatibility impact; do not silently replace files under the old version.

## Supersession

A new release should not erase the history of an earlier one. A supersession record should state:

- old and new manifest identifiers and versions;
- source commits and digests;
- reason for supersession;
- breaking or compatible classification;
- required consumer action;
- migration and rollback steps;
- evidence bundle locations;
- approval record.

## Reconciliation recovery

When a canonical pull request diverges from `main`:

- capture old base, old head, current default head, merge base, ahead/behind state, and review-thread state;
- choose a provenance-preserving merge strategy;
- document every conflict and resolution;
- list retained, excluded, quarantined, and superseded paths;
- preserve the original branches and commits;
- produce one mergeable result head;
- freeze it before renewed evidence collection;
- map earlier findings to the new head;
- repeat exact-head validation and downstream replay.

Do not force-rewrite reviewed history merely to make the branch appear clean.

## Evidence retention

Retain at minimum:

- source commit and archive;
- compatibility manifest;
- source artifacts and canonical bytes;
- checksums;
- validation reports and logs;
- tool and dependency versions;
- fixtures;
- reconciliation and scope-disposition records;
- review-thread disposition;
- downstream replay;
- approval, release, rollback, and supersession records.

Retention periods should be long enough to support downstream migration and incident investigation. An evidence artifact that expires before review or consumer adoption is complete should not be treated as durable release proof.

## Recovery validation

A rollback or repair is complete only when:

- the affected version is no longer accepted by designated consumers;
- the selected safe version is accepted consistently;
- immutable and forbidden-capability rules remain intact;
- canonical bytes and digests reproduce;
- all affected hostile fixtures pass;
- evidence is tied to the final head;
- task chain, release plan, changelog, and documentation agree;
- an authorized reviewer closes the incident or approves the superseding release.

## Communication template

```text
Incident identifier:
Detected at:
Affected manifest/version:
Source commit:
Observed artifact/set digests:
Affected consumers:
Severity:
Immediate containment:
Evidence preserved:
Root-cause status:
Rollback or supersession target:
Validation required:
Approval owner:
Residual risk:
```

## Operational non-goals

This repository does not remotely disable consumers, rotate credentials, deploy patches, or edit downstream repositories automatically. Those actions remain with the respective human-controlled repository and deployment owners.

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
