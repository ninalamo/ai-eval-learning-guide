"""Inspect task. Implement reverse_word() after scoring.py is green."""

from __future__ import annotations

from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.solver import generate

from scoring import score_reverse

PROMPT = "Reverse the word 'ab'. Reply with only the reversed word."
TARGET = "ba"


@task
def reverse_word() -> Task:
    """
    Dataset: one Sample with input=PROMPT, target=TARGET.
    Solver: generate().
    Scorer: wrap score_reverse. If Inspect's exact() is strict-strip, you may
    use it *only if* it agrees with score_reverse on the tests in test_scoring.py.
    """
    raise NotImplementedError
    _ = (Sample, generate, score_reverse)
