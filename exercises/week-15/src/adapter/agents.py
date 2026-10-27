from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol


@dataclass
class AgentResult:
    stdout: str
    argv: list[str] = field(default_factory=list)
    tool_call_count: int = 0


class Agent(Protocol):
    def run(self, instruction: str, cwd: Path) -> AgentResult: ...


class StubAgent:
    """Honest stub: write the correct src files for reverse/clamp/write_ok. No shell."""

    def run(self, instruction: str, cwd: Path) -> AgentResult:
        raise NotImplementedError


class CliAgent:
    """
    Run `self.argv` with cwd=cwd, instruction on stdin.
    shell=False. Capture stdout. Timeout 30s.
    Does not interpret the instruction itself — the CLI (or canned.py) does.
    """

    def __init__(self, argv: list[str]) -> None:
        self.argv = argv

    def run(self, instruction: str, cwd: Path) -> AgentResult:
        raise NotImplementedError
