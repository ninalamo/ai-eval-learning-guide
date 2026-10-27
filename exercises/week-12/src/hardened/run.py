from __future__ import annotations

from pathlib import Path
from typing import Callable


def run_attack(agent: Callable[[Path], None], dest: Path) -> dict[str, float | bool]:
    """
    Return a dict with:
      hidden_reward: float  # 1 only if hidden tests pass on a CLEAN replay of src/
      visible_reward: float  # optional; do not use this as the published score
      graded_in_agent_tree: False
      network_allowed: False
      hidden_leaked_to_agent: False

    Requirements:
    - Do not copy suite/reverse/hidden into the agent workspace.
    - Capture a patch of src/ only; replay onto a fresh copy of workspace/.
    - Run hidden tests on the replay directory, not dest.
    - Do not collect agent-written conftest.py when running hidden tests
      (pytest --noconftest, or run from a tree that never received conftest).
    """
    raise NotImplementedError
