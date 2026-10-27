from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

from adapter.agents import Agent, AgentResult

ROOT = Path(__file__).resolve().parents[2]
SUITE = ROOT / "suite"


def grade(task: str, agent_ws: Path, grade_ws: Path) -> float:
    if grade_ws.exists():
        shutil.rmtree(grade_ws)
    shutil.copytree(SUITE / task / "workspace", grade_ws)
    if (agent_ws / "src").exists():
        if (grade_ws / "src").exists():
            shutil.rmtree(grade_ws / "src")
        shutil.copytree(agent_ws / "src", grade_ws / "src")
    hidden = SUITE / task / "hidden"
    hidden_copy = grade_ws / "_hidden"
    shutil.copytree(hidden, hidden_copy)
    env = os.environ.copy()
    env["PYTHONPATH"] = str(grade_ws / "src")
    proc = subprocess.run(
        ["pytest", "-q", str(hidden_copy)],
        cwd=grade_ws / "src",
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    return 1.0 if proc.returncode == 0 else 0.0


def run_task(agent: Agent, task: str, work: Path) -> tuple[AgentResult, float]:
    ws = work / "agent"
    if ws.exists():
        shutil.rmtree(ws)
    shutil.copytree(SUITE / task / "workspace", ws)
    instruction = (SUITE / task / "instruction.md").read_text(encoding="utf-8")
    result = agent.run(instruction, ws)
    reward = grade(task, ws, work / "grade")
    return result, reward
