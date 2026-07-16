#!/usr/bin/env python3
"""Validate the reviewed QSO-GENOMES schema set without executing artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]

VALIDATION_SETS = (
    (
        ROOT / "schema" / "qso-genome.schema.json",
        tuple(
            ROOT / "genomes" / name
            for name in ("atlas.json", "lyra.json", "nova.json", "orion.json")
        ),
    ),
    (
        ROOT / "schema" / "qso-sprite.schema.json",
        (ROOT / "sprites" / "aequitas.json",),
    ),
)


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a key."""


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


def main() -> int:
    validated = 0
    failures: list[str] = []

    for schema_path, documents in VALIDATION_SETS:
        schema = load_json(schema_path)
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)

        for document_path in documents:
            document = load_json(document_path)
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
