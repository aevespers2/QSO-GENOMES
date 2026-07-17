#!/usr/bin/env python3
"""Validate the reviewed QSO-GENOMES schema set without executing artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_GENOME_FILENAMES = (
    "atlas.json",
    "lyra.json",
    "nova.json",
    "orion.json",
)
REQUIRED_SPRITE_FILENAMES = (
    "aequitas.json",
    "socrates.json",
)

VALIDATION_SETS = (
    (
        ROOT / "schema" / "qso-genome.schema.json",
        tuple(ROOT / "genomes" / name for name in REQUIRED_GENOME_FILENAMES),
    ),
    (
        ROOT / "schema" / "qso-sprite.schema.json",
        tuple(ROOT / "sprites" / name for name in REQUIRED_SPRITE_FILENAMES),
    ),
)


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a key."""


class ArtifactSetError(ValueError):
    """Raised when a schema-bound directory contains the wrong artifacts."""


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(f"duplicate JSON object key: {key}")
        value[key] = item
    return value


def reject_nonfinite(value: str) -> None:
    raise ValueError(f"non-finite JSON number is not allowed: {value}")


def load_json(path: Path) -> Any:
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicate_keys,
        parse_constant=reject_nonfinite,
    )


def assert_exact_json_artifact_set(
    directory: Path,
    required_filenames: Iterable[str],
    *,
    label: str,
) -> None:
    """Fail closed unless ``directory`` contains exactly the required JSON files."""

    required = frozenset(required_filenames)
    actual = frozenset(
        path.name
        for path in directory.iterdir()
        if path.is_file() and path.suffix == ".json"
    )
    missing = sorted(required - actual)
    unexpected = sorted(actual - required)

    findings: list[str] = []
    if missing:
        findings.append(f"missing required {label} artifacts: {', '.join(missing)}")
    if unexpected:
        findings.append(f"unexpected {label} artifacts: {', '.join(unexpected)}")
    if findings:
        raise ArtifactSetError("; ".join(findings))


def main() -> int:
    validated = 0
    failures: list[str] = []

    for directory, required, label in (
        (ROOT / "genomes", REQUIRED_GENOME_FILENAMES, "genome"),
        (ROOT / "sprites", REQUIRED_SPRITE_FILENAMES, "sprite"),
    ):
        try:
            assert_exact_json_artifact_set(directory, required, label=label)
        except (ArtifactSetError, OSError) as error:
            failures.append(f"{directory.relative_to(ROOT)}: {error}")

    for schema_path, documents in VALIDATION_SETS:
        try:
            schema = load_json(schema_path)
            Draft202012Validator.check_schema(schema)
            validator = Draft202012Validator(schema)
        except (OSError, ValueError) as error:
            failures.append(f"{schema_path.relative_to(ROOT)}: {error}")
            continue

        for document_path in documents:
            if not document_path.is_file():
                continue

            try:
                document = load_json(document_path)
            except (OSError, ValueError) as error:
                failures.append(f"{document_path.relative_to(ROOT)}: {error}")
                continue

            errors = sorted(validator.iter_errors(document), key=lambda error: list(error.path))
            if errors:
                for error in errors:
                    location = ".".join(str(part) for part in error.absolute_path) or "<root>"
                    failures.append(
                        f"{document_path.relative_to(ROOT)}:{location}: {error.message}"
                    )
            else:
                validated += 1
                print(
                    "PASS: "
                    f"{document_path.relative_to(ROOT)} against "
                    f"{schema_path.relative_to(ROOT)}"
                )

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print(f"PASS: {validated} schema-bound artifacts validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
