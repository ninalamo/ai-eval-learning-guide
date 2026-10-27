#!/usr/bin/env python3
"""Run oracle then verifier for each task without Harbor. Reward must be 1."""

from __future__ import annotations

import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TASKS = ["write-hello", "fix-clamp"]


def run_oracle(task_dir: Path) -> float:
    work = Path(os.environ.get("TMPDIR", "/tmp")) / f"harbor-local-{task_dir.name}"
    if work.exists():
        shutil.rmtree(work)
    app = work / "app"
    logs = work / "logs" / "verifier"
    app.mkdir(parents=True)
    logs.mkdir(parents=True)

    env_src = task_dir / "environment"
    if env_src.is_dir():
        for item in env_src.iterdir():
            dest = app / item.name
            if item.is_dir():
                shutil.copytree(item, dest)
            else:
                shutil.copy2(item, dest)

    env = os.environ.copy()
    env["APP_DIR"] = str(app)
    env["LOGS_DIR"] = str(logs)

    solve = task_dir / "solution" / "solve.sh"
    test = task_dir / "tests" / "test.sh"
    for script in (solve, test):
        script.chmod(script.stat().st_mode | stat.S_IEXEC)

    subprocess.run(["bash", str(solve)], cwd=app, env=env, check=True)
    subprocess.run(["bash", str(test)], cwd=app, env=env, check=True)

    reward_path = logs / "reward.txt"
    if not reward_path.is_file():
        raise SystemExit(f"{task_dir.name}: missing {reward_path}")
    return float(reward_path.read_text(encoding="utf-8").strip())


def instruction_leaks_canary(task_dir: Path) -> bool:
    text = (task_dir / "instruction.md").read_text(encoding="utf-8")
    return "hidden-canary-7f3a" in text


def main() -> None:
    failed = False
    for name in TASKS:
        task_dir = ROOT / "tasks" / name
        if instruction_leaks_canary(task_dir):
            print(f"{name} FAIL instruction leaks hidden-canary-7f3a")
            failed = True
            continue
        try:
            reward = run_oracle(task_dir)
        except Exception as exc:
            print(f"{name} oracle ERROR {exc}")
            failed = True
            continue
        status = "ok" if reward == 1.0 else "FAIL"
        print(f"{name} oracle={reward} {status}")
        if reward != 1.0:
            failed = True
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
