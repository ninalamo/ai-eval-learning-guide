from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Task:
    id: str
    output: str
    expected: str
    schema_required: list[str] | None
    tools_called: list[str]
    required_tools: list[str]
    human_pass: int
    judge_keywords_any: list[str]


@dataclass(frozen=True)
class TaskScores:
    id: str
    exact: float
    schema: float
    trajectory: float
    judge: float
    human_pass: int


def load_tasks(path: Path) -> list[Task]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [Task(**row) for row in raw]


def grade_exact(task: Task) -> float:
    """1.0 iff stripped output == stripped expected. Case-sensitive."""
    raise NotImplementedError


def grade_schema(task: Task) -> float:
    """
    If schema_required is None, return 1.0 (not applicable, treat as pass).
    Else output must parse as JSON object containing every required key.
    Extra keys are allowed. Values are not checked (that is exact's job).
    """
    raise NotImplementedError


def grade_trajectory(task: Task) -> float:
    """1.0 iff every required tool appears in tools_called."""
    raise NotImplementedError


def grade_judge(task: Task) -> float:
    """
    FakeJudge: 1.0 if judge_keywords_any is empty (nothing to check)
    OR any keyword appears in output.lower().
    Offline on purpose. Do not call a model here.
    """
    raise NotImplementedError


def score_all(tasks: list[Task]) -> list[TaskScores]:
    raise NotImplementedError


def disagreement_report(scores: list[TaskScores]) -> list[dict[str, Any]]:
    """
    One row per task where exact, schema, trajectory, judge are not all equal
    OR any of them disagrees with human_pass (human is 0/1).
    Include the task id and the five numbers.
    """
    raise NotImplementedError
