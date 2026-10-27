from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Protocol


class Completer(Protocol):
    async def complete(self, prompt: str) -> str: ...


class FakeCompleter:
    """Return a canned string. Must not read `expected`."""

    def __init__(self, response: str) -> None:
        self.response = response
        self.prompts: list[str] = []

    async def complete(self, prompt: str) -> str:
        raise NotImplementedError


@dataclass(frozen=True)
class TrialRecord:
    prompt: str
    completion: str
    command: list[str]
    command_stdout: str
    command_returncode: int
    expected: str
    reward: float


def score_exact(completion: str, expected: str) -> float:
    """1.0 if stripped completion equals stripped expected, else 0.0."""
    raise NotImplementedError


def run_command(command: list[str], cwd: Path, timeout_sec: float) -> tuple[str, int]:
    """
    subprocess.run with shell=False, capture_output, text, cwd, timeout.
    Return (stdout, returncode). Do not raise on non-zero returncode.
    """
    raise NotImplementedError


async def run_trial(
    *,
    completer: Completer,
    prompt: str,
    expected: str,
    command: list[str],
    cwd: Path,
    timeout_sec: float = 10.0,
) -> TrialRecord:
    """
    1. completer.complete(prompt)  — gold is NOT passed in
    2. run_command(command, cwd)
    3. score_exact(completion, expected)
    """
    raise NotImplementedError


def write_trial(path: Path, record: TrialRecord) -> None:
    path.write_text(json.dumps(asdict(record), indent=2), encoding="utf-8")


class AzureOpenAICompleter:
    """Optional. Tests do not construct this."""

    def __init__(
        self,
        endpoint: str,
        api_key: str,
        deployment: str,
        api_version: str,
    ) -> None:
        self.endpoint = endpoint.rstrip("/")
        self.api_key = api_key
        self.deployment = deployment
        self.api_version = api_version

    async def complete(self, prompt: str) -> str:
        raise NotImplementedError
