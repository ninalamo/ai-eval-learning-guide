from __future__ import annotations

from pathlib import Path
from typing import Callable

AgentFn = Callable[[Path, str], None]


def prepare_agent_workspace(template: Path, dest: Path) -> Path:
    """
    Copy template (the agent-visible workspace) to dest.
    git init, git add -A, git commit so later diffs work.
    Must not copy a sibling hidden/ directory.
    """
    raise NotImplementedError


def capture_patch(workspace: Path) -> str:
    """
    Return git diff of workspace vs the baseline commit.
    Prefer src/ only so test edits are not replayed.
    """
    raise NotImplementedError


def replay_patch(template: Path, patch: str, dest: Path) -> Path:
    """
    Copy template to dest, git init + commit, apply patch.
    Return dest. Must not be the same path the agent used.
    """
    raise NotImplementedError


def grade_task(grade_ws: Path, hidden: Path) -> float:
    """
    Run hidden tests against grade_ws.
    Copy hidden tests into the grade tree at verify time (do not leave them
    in the agent copy). Set PYTHONPATH to grade_ws/src so `from reverse import
    reverse` resolves to the replayed source.
    Reward 1.0 if pytest returncode is 0.
    Do not run tests from the agent workspace.
    """
    raise NotImplementedError


def run_suite(
    suite_root: Path,
    agent: AgentFn,
    work_root: Path,
) -> dict[str, float]:
    """
    For each subdirectory of suite_root (reverse, clamp, write_ok):
      prepare workspace from <task>/workspace
      run agent(ws, task_name)
      patch = capture_patch(ws)
      grade_ws = replay_patch(template, patch, ...)
      scores[task] = grade_task(grade_ws, <task>/hidden)
    """
    raise NotImplementedError
