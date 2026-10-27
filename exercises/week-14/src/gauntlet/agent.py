"""Scripted subject. Do not tune hidden thresholds to fake a win — change configs/."""

from __future__ import annotations

from typing import Any

# Hidden thresholds (not levers). Leave these numbers alone.
SLOW_NEEDS_TIMEOUT = 20
CLAMP_NEEDLE = "be careful with ranges"
TOOL_NEEDLE = "read_file is required"


def solve(task: str, config: dict[str, Any]) -> bool:
    timeout = int(config["timeout_sec"])
    prompt = str(config["system_prompt"])
    tools = str(config["tool_description"])
    if task == "reverse":
        return True
    if task == "write_ok":
        return True
    if task == "slow":
        return timeout >= SLOW_NEEDS_TIMEOUT
    if task == "clamp":
        return CLAMP_NEEDLE in prompt
    if task == "toolish":
        return TOOL_NEEDLE in tools
    raise KeyError(task)
