from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from gauntlet.agent import solve

ROOT = Path(__file__).resolve().parents[2]
LOCK = json.loads((ROOT / "suite.lock.json").read_text(encoding="utf-8"))


def load_config(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def changed_keys(a: dict[str, Any], b: dict[str, Any]) -> list[str]:
    keys = set(a) | set(b)
    return sorted(k for k in keys if a.get(k) != b.get(k))


def run_config(config: dict[str, Any]) -> dict[str, float]:
    return {task: 1.0 if solve(task, config) else 0.0 for task in LOCK["tasks"]}
