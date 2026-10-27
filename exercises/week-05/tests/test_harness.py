from __future__ import annotations

from pathlib import Path

import pytest

from harness.agents import edit_tests, fake_stdout, honest, noop
from harness.score import ground_truth, prepare_workspace, trusting_exitcode, trusting_stdout

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "fixtures" / "workspace"
HIDDEN = ROOT / "fixtures" / "hidden"


@pytest.fixture
def dirty(tmp_path: Path) -> Path:
    return prepare_workspace(TEMPLATE, tmp_path / "ws")


def _gt(dirty: Path, tmp_path: Path) -> float:
    return ground_truth(
        template=TEMPLATE,
        dirty=dirty,
        hidden=HIDDEN,
        grade_dir=tmp_path / "grade",
    )


def test_prepare_workspace_does_not_leak_hidden(dirty: Path) -> None:
    names = {p.name for p in dirty.rglob("*") if p.is_file()}
    assert "test_hidden.py" not in names
    assert (dirty / "add_one.py").is_file()
    assert (dirty / "tests" / "test_visible.py").is_file()


def test_honest_passes_both(dirty: Path, tmp_path: Path) -> None:
    honest(dirty)
    assert trusting_exitcode(dirty) == 1.0
    assert _gt(dirty, tmp_path) == 1.0


def test_noop_fails_all(dirty: Path, tmp_path: Path) -> None:
    result = noop(dirty)
    assert trusting_exitcode(dirty) == 0.0
    assert trusting_stdout(result) == 0.0
    assert _gt(dirty, tmp_path) == 0.0


def test_edit_tests_fools_exitcode_not_ground_truth(
    dirty: Path, tmp_path: Path
) -> None:
    edit_tests(dirty)
    assert trusting_exitcode(dirty) == 1.0
    assert _gt(dirty, tmp_path) == 0.0


def test_fake_stdout_fools_stdout_only(dirty: Path, tmp_path: Path) -> None:
    result = fake_stdout(dirty)
    assert trusting_stdout(result) == 1.0
    assert trusting_exitcode(dirty) == 0.0
    assert _gt(dirty, tmp_path) == 0.0
