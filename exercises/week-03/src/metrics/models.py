from __future__ import annotations

from pydantic import BaseModel, Field


class Trial(BaseModel):
    task_id: str
    tag: str
    trial_index: int = Field(ge=0)
    passed: bool
