from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[2]
SUITE = ROOT / "suite"
TASKS = ["reverse", "clamp", "write_ok", "is_even", "greet"]


def _grade(task: str, agent_ws: Path, grade_root: Path) -> float:
    grade = grade_root / task
    if grade.exists():
        shutil.rmtree(grade)
    shutil.copytree(SUITE / task / "workspace", grade)
    if (agent_ws / "src").is_dir():
        if (grade / "src").exists():
            shutil.rmtree(grade / "src")
        shutil.copytree(agent_ws / "src", grade / "src")
    hidden = SUITE / task / "hidden"
    hidden_copy = grade / "_hidden"
    shutil.copytree(hidden, hidden_copy)
    env = os.environ.copy()
    env["PYTHONPATH"] = str(grade / "src")
    proc = subprocess.run(
        ["pytest", "-q", str(hidden_copy)],
        cwd=grade / "src",
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    return 1.0 if proc.returncode == 0 else 0.0


def run(agent: Callable[[Path, str], None], work: Path) -> dict[str, float]:
    scores: dict[str, float] = {}
    for task in TASKS:
        ws = work / "agent" / task
        if ws.exists():
            shutil.rmtree(ws)
        shutil.copytree(SUITE / task / "workspace", ws)
        agent(ws, task)
        scores[task] = _grade(task, ws, work / "grade")
    return scores
