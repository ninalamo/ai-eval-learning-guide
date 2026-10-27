"""Port of csharp-reference/TestResultSummary.cs. Fill in the stubs."""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator


@dataclass(frozen=True)
class TestResult:
    __test__ = False  # pytest would otherwise collect this as a test class
    name: str
    status: str
    tag: str | None
    duration_ms: int


@dataclass(frozen=True)
class Summary:
    total: int
    passed: int
    failed: int
    pass_rate_by_tag: dict[str, float]


def load_results(path: Path) -> list[TestResult]:
    """Read a JSON array of test results. Let parse errors propagate."""
    raise NotImplementedError


def pass_rate_by_tag(results: list[TestResult]) -> dict[str, float]:
    """Passed / (passed + failed) per tag. Skip skipped. Omit untagged rows."""
    raise NotImplementedError


def summarize(results: list[TestResult]) -> Summary:
    raise NotImplementedError


def write_summary(path: Path, summary: Summary) -> None:
    """Write Summary as JSON. Use Path.write_text and utf-8."""
    raise NotImplementedError


@contextmanager
def timed() -> Iterator[dict[str, float]]:
    """
    with timed() as t:
        ...
    t["elapsed_ms"] is set when the block exits.

    Implement with time.perf_counter() and yield a dict you mutate on the way out.
    """
    raise NotImplementedError
