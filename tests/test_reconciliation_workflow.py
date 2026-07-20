from pathlib import Path

WORKFLOW = Path('.github/workflows/automatic-nonmerge-reconciliation.yml')


def text() -> str:
    return WORKFLOW.read_text(encoding='utf-8')


def test_open_pr_enumeration_is_explicitly_bounded_and_deduplicated() -> None:
    source = text()
    assert 'gh pr list --repo "$GITHUB_REPOSITORY" --state open --limit 100' in source
    assert 'sort -n -u /tmp/prs.txt -o /tmp/prs.txt' in source


def test_comment_history_is_paginated_before_deduplication() -> None:
    source = text()
    assert 'gh api --paginate "repos/$GITHUB_REPOSITORY/issues/$pr_number/comments?per_page=100"' in source
    assert 'grep -Fq "$marker"' in source


def test_conflict_notices_use_semantic_fingerprints_not_volatile_heads() -> None:
    source = text()
    assert 'CONFLICT_FINGERPRINT="$(python - "$BASE_SHA" "reports/pr-${PR_NUMBER}-conflicts.txt"' in source
    assert 'conflicts = sorted({' in source
    assert 'payload = (base_sha + "\\n" + "\\n".join(conflicts) + "\\n").encode("utf-8")' in source
    assert '<!-- nonmerge-reconciliation:conflicts:$BASE_SHA:$CONFLICT_FINGERPRINT -->' in source
    assert '<!-- nonmerge-reconciliation:conflicts:$HEAD_SHA:$BASE_SHA -->' not in source


def test_conflict_evidence_records_exact_head_and_semantic_fingerprint() -> None:
    source = text()
    assert '"head_sha": head_sha' in source
    assert '"conflict_fingerprint": conflict_fingerprint' in source
    assert 'the same unresolved conflict set remains' in source


def test_workflow_remains_fail_closed() -> None:
    source = text()
    assert 'automatic_merge_authorized": False' in source
    assert 'Human review under Jacob Thomas Redmond is required.' in source
    assert 'jacob_elias_redmond' not in source


def test_privileged_workflow_does_not_execute_candidate_code() -> None:
    source = text()
    assert 'pull_request_target:' in source
    assert 'git merge --no-ff --no-commit' in source
    assert 'pytest' not in source
    assert 'python scripts/' not in source
