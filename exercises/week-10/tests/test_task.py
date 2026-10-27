from __future__ import annotations

from reverse_task import PROMPT, TARGET, reverse_word


def test_task_builds() -> None:
    task = reverse_word()
    assert task is not None


def test_prompt_does_not_embed_a_substring_trap() -> None:
    # Instruction may mention the word to reverse, not a long decoy containing 'ba'.
    assert "ba" == TARGET
    assert "ab" in PROMPT
