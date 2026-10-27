from __future__ import annotations

from gauntlet.loop import ROOT, changed_keys, load_config, run_config


def test_lock_has_five_tasks() -> None:
    lock = load_config(ROOT / "suite.lock.json")
    assert lock["tasks"] == ["reverse", "clamp", "slow", "toolish", "write_ok"]


def test_baseline_is_not_perfect() -> None:
    scores = run_config(load_config(ROOT / "configs" / "baseline.json"))
    assert scores["reverse"] == 1.0
    assert scores["write_ok"] == 1.0
    assert scores["slow"] == 0.0
    assert scores["clamp"] == 0.0
    assert scores["toolish"] == 0.0


def test_one_lever_timeout_flips_slow_only() -> None:
    cfg = load_config(ROOT / "configs" / "baseline.json")
    cand = dict(cfg)
    cand["timeout_sec"] = 30
    assert changed_keys(cfg, cand) == ["timeout_sec"]
    base = run_config(cfg)
    new = run_config(cand)
    assert new["slow"] == 1.0
    for task in base:
        if task != "slow":
            assert new[task] == base[task]
