"""Intentionally bad harness. Study it; do not copy it into hardened."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[2]
TASK = ROOT / "suite" / "reverse"


def run_attack(agent: Callable[[Path], None], dest: Path) -> dict[str, float | bool]:
    if dest.exists():
        shutil.rmtree(dest)
    # Leak: copies hidden tests into the tree the agent (and pytest) see.
    shutil.copytree(TASK / "workspace", dest)
    shutil.copytree(TASK / "hidden", dest / "hidden")
    agent(dest)
    env = os.environ.copy()
    env["PYTHONPATH"] = str(dest / "src")
    visible = subprocess.run(
        ["pytest", "-q", str(dest / "tests")],
        cwd=dest / "src",
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    hidden = subprocess.run(
        ["pytest", "-q", str(dest / "hidden")],
        cwd=dest / "src",
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    return {
        "visible_reward": 1.0 if visible.returncode == 0 else 0.0,
        "hidden_reward": 1.0 if hidden.returncode == 0 else 0.0,
        "graded_in_agent_tree": True,
        "network_allowed": True,
        "hidden_leaked_to_agent": (dest / "hidden" / "test_hidden.py").is_file(),
    }
