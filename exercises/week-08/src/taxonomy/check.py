from __future__ import annotations

import json
from pathlib import Path
from typing import Any

SURFACES = {
    "prompt",
    "tool_contract",
    "harness",
    "grader",
    "task",
    "environment",
    "model_ceiling",
}

REQUIRED = {"trace_id", "symptom", "suspected_cause", "repair_surface", "proposed_mutation", "notes"}


def load_answers(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def check_answers(rows: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    ids = [r.get("trace_id") for r in rows]
    if ids != [f"{i:02d}" for i in range(1, 9)]:
        errors.append(f"expected trace_id 01..08 in order, got {ids}")
    for row in rows:
        missing = REQUIRED - set(row)
        if missing:
            errors.append(f"{row.get('trace_id')}: missing {sorted(missing)}")
            continue
        if row["repair_surface"] not in SURFACES:
            errors.append(
                f"{row['trace_id']}: repair_surface {row['repair_surface']!r} not in closed set"
            )
        if row["repair_surface"] in {"other", "misc"}:
            errors.append(f"{row['trace_id']}: catch-all surface forbidden")
        if not str(row["proposed_mutation"]).strip():
            errors.append(f"{row['trace_id']}: proposed_mutation empty")
        if row["trace_id"] == "07" and row["repair_surface"] == "prompt":
            errors.append("07: grader bug labeled as prompt")
        if row["trace_id"] == "08" and row["repair_surface"] != "model_ceiling":
            if "rebuttal" not in str(row["notes"]).lower():
                errors.append("08: expected model_ceiling (or notes containing 'rebuttal')")
    return errors


def grade_answers(rows: list[dict[str, Any]], gold: list[dict[str, Any]]) -> dict[str, Any]:
    gold_by = {g["trace_id"]: g for g in gold}
    matches = []
    diffs = []
    for row in rows:
        g = gold_by[row["trace_id"]]
        ok = row["repair_surface"] == g["repair_surface"]
        matches.append(ok)
        if not ok:
            diffs.append(
                {
                    "trace_id": row["trace_id"],
                    "yours": row["repair_surface"],
                    "gold": g["repair_surface"],
                    "gold_rationale": g.get("notes", ""),
                }
            )
    return {"n": len(rows), "surface_matches": sum(matches), "diffs": diffs}
