from __future__ import annotations

import sys
from pathlib import Path

from adapter.agents import CliAgent, StubAgent
from adapter.harness import ROOT, run_task


def test_stub_solves_all_three(tmp_path: Path) -> None:
    agent = StubAgent()
    for task in ("reverse", "clamp", "write_ok"):
        _, reward = run_task(agent, task, tmp_path / task)
        assert reward == 1.0


def test_grade_uses_a_separate_tree(tmp_path: Path) -> None:
    agent = StubAgent()
    _, reward = run_task(agent, "reverse", tmp_path / "run")
    assert reward == 1.0
    grade_dir = tmp_path / "run" / "grade"
    agent_dir = tmp_path / "run" / "agent"
    assert grade_dir.resolve() != agent_dir.resolve()
    assert (agent_dir / "hidden").exists() is False


def test_cli_agent_invokes_argv_without_shell(tmp_path: Path) -> None:
    canned = ROOT / "src" / "adapter" / "canned.py"
    agent = CliAgent([sys.executable, str(canned)])
    result, reward = run_task(agent, "reverse", tmp_path)
    assert reward == 1.0
    assert result.argv[0] == sys.executable
    assert "canned.py" in result.argv[1]
