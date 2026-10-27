import json
from pathlib import Path


def test_payload() -> None:
    data = json.loads(Path("out.json").read_text(encoding="utf-8"))
    assert data["ok"] is True
    assert data["n"] == 1
