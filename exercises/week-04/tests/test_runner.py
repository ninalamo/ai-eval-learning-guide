from __future__ import annotations

import json
from pathlib import Path

import pytest

from trial_runner.runner import (
    FakeCompleter,
    run_command,
    run_trial,
    score_exact,
    write_trial,
)


def test_score_exact_strips() -> None:
    assert score_exact("4\n", "4") == 1.0
    assert score_exact("5", "4") == 0.0


def test_fake_completer_does_not_see_expected() -> None:
    fake = FakeCompleter("hello")
    # complete() must return the canned string regardless of prompt content.
    import asyncio

    out = asyncio.run(fake.complete("the gold is SECRET"))
    assert out == "hello"
    assert "SECRET" not in out
    assert fake.prompts == ["the gold is SECRET"]


def test_run_command_no_shell(tmp_path: Path) -> None:
    stdout, code = run_command(
        ["python", "-c", "print(2+2)"],
        cwd=tmp_path,
        timeout_sec=10,
    )
    assert code == 0
    assert stdout.strip() == "4"


def test_run_command_timeout(tmp_path: Path) -> None:
    with pytest.raises(Exception):
        run_command(
            ["python", "-c", "import time; time.sleep(5)"],
            cwd=tmp_path,
            timeout_sec=0.2,
        )


@pytest.mark.asyncio
async def test_run_trial_writes_full_artifact(tmp_path: Path) -> None:
    fake = FakeCompleter("4")
    record = await run_trial(
        completer=fake,
        prompt="n=?",
        expected="4",
        command=["python", "-c", "print(2+2)"],
        cwd=tmp_path,
    )
    assert record.reward == 1.0
    assert record.completion == "4"
    assert record.prompt == "n=?"
    assert "4" not in fake.prompts[0] or fake.prompts[0] == "n=?"
    path = tmp_path / "trial.json"
    write_trial(path, record)
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert set(payload) >= {
        "prompt",
        "completion",
        "command",
        "command_stdout",
        "command_returncode",
        "expected",
        "reward",
    }


@pytest.mark.asyncio
async def test_run_trial_scores_model_not_command() -> None:
    fake = FakeCompleter("wrong")
    record = await run_trial(
        completer=fake,
        prompt="n=?",
        expected="4",
        command=["python", "-c", "print(2+2)"],
        cwd=Path("."),
    )
    assert record.command_returncode == 0
    assert record.reward == 0.0
