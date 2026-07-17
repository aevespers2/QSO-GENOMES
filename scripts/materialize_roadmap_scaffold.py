"""Materialize the roadmap scaffold declared in roadmap/scaffold-plan.json.

Phase: foundation-to-release planning.
Stages: manifest validation, path generation, unique roadmap rendering, collision review, human-approved commit.
Tasks: create every declared folder/file; tailor each header to its path; preserve existing work by default; support auditable dry runs.
Steps: run without --write; inspect output; run with --write; review git diff; execute repository validation before commit.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "roadmap" / "scaffold-plan.json"


def purpose(path: Path) -> str:
    text = path.as_posix().lower()
    name = path.stem.replace("_", " ").replace("-", " ")
    if "schema" in text:
        return f"Define the machine-readable validation contract for {name}."
    if "/roles/" in f"/{text}" or "/genomes/" in f"/{text}":
        return f"Define the bounded declarative identity, purpose, outputs, and constraints for {name}."
    if "workflow" in text:
        return f"Define deterministic sequencing, review gates, and stopping conditions for {name}."
    if "policy" in text or "security" in text or "governance" in text:
        return f"Define or verify fail-closed governance controls for {name}."
    if "test" in text:
        return f"Verify positive, negative, boundary, and tamper behavior for {name}."
    if "manifest" in text or "checksum" in text or "release" in text:
        return f"Record compatibility, provenance, and release evidence for {name}."
    return f"Implement or document the repository responsibility represented by {name}."


def roadmap(path: Path) -> dict[str, object]:
    return {
        "file": path.as_posix(),
        "purpose": purpose(path),
        "phase": "scaffold",
        "stages": ["contract", "implementation", "verification", "integration", "release"],
        "tasks": [
            "Specify ownership, inputs, outputs, invariants, and failure behavior.",
            "Implement the smallest deterministic and bounded behavior.",
            "Add positive, negative, boundary, and tamper-oriented tests.",
            "Connect provenance, freeze-point, and human-review requirements.",
            "Document compatibility, migration, rollback, and release evidence."
        ],
        "steps": [
            "Review upstream schemas, policies, and dependent interfaces.",
            "Replace the scaffold with typed implementation or normative content.",
            "Add fixtures and fail-closed validation.",
            "Run deterministic replay and exact-head CI.",
            "Obtain human review and record acceptance evidence."
        ],
        "status": "planned"
    }


def render(path: Path) -> str:
    data = roadmap(path)
    suffix = path.suffix.lower()
    if suffix == ".json":
        return json.dumps({"roadmap": data}, indent=2) + "\n"
    body = "\n".join([
        f"Roadmap: {data['file']}", f"Purpose: {data['purpose']}", f"Phase: {data['phase']}",
        "Stages: contract -> implementation -> verification -> integration -> release",
        "Tasks:", *[f"- {item}" for item in data["tasks"]], "Steps:",
        *[f"{index}. {item}" for index, item in enumerate(data["steps"], 1)]
    ])
    if suffix == ".py":
        return f'"""\n{body}\n"""\n\nfrom __future__ import annotations\n\n# TODO: Replace roadmap scaffold with tested implementation.\n'
    if suffix in {".ts", ".tsx"}:
        return "/**\n * " + body.replace("\n", "\n * ") + "\n */\n\nexport {};\n"
    if suffix in {".yml", ".yaml", ".toml"} or path.name in {"requirements.txt", "CODEOWNERS"}:
        return "# " + body.replace("\n", "\n# ") + "\n"
    return f"# {path.stem.replace('-', ' ').title()}\n\n" + body.replace("Tasks:\n", "## Tasks\n").replace("Steps:\n", "\n## Steps\n") + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Create missing scaffold files.")
    parser.add_argument("--force", action="store_true", help="Replace existing files; requires --write.")
    args = parser.parse_args()
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    paths = [Path(folder) / name for folder, names in plan["groups"].items() for name in names]
    for relative in paths:
        target = ROOT / relative
        action = "replace" if target.exists() else "create"
        print(f"{action}: {relative.as_posix()}")
        if not args.write or (target.exists() and not args.force):
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(relative), encoding="utf-8")


if __name__ == "__main__":
    main()
