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


def test_reconciliation_notices_are_keyed_to_exact_state() -> None:
    source = text()
    assert '<!-- nonmerge-reconciliation:fork-head:$HEAD_SHA -->' in source
    assert '<!-- nonmerge-reconciliation:conflicts:$HEAD_SHA:$BASE_SHA -->' in source


def test_workflow_remains_fail_closed() -> None:
    source = text()
    assert 'automatic_merge_authorized": False' in source
    assert 'Human review under Jacob Elias Redmond is required.' in source
