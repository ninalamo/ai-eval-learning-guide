# Week 3 — Eval data shapes

**Time box:** ~8 hours (2 read, 4 build, 2 write-up)

## Goal

Load a JSONL trial log into pydantic models and compute the numbers you will quote for the rest of the course: pass@1, pass@k, pass rate by tag. Refuse to compute them from a half-parsed dict.

## Non-goal

pandas-as-a-lifestyle, notebooks as source of truth, or a dashboard. If you want a table, print it. polars/pandas is stretch.

## C# → Python map

| You already | This week |
|-------------|-----------|
| DTO + `JsonSerializer` + DataAnnotations | pydantic `BaseModel` + `model_validate` |
| EF Core entity vs API contract | **trial log schema** vs in-memory aggregates |
| `IGrouping<T>` / LINQ | `dict[str, list[Trial]]` then functions |
| CSV dumps from SQL | JSONL (one JSON object per line) |

## Readings

1. [pydantic — models](https://docs.pydantic.dev/latest/concepts/models/) — validation, `model_dump`, JSON. This is your DTO layer.
2. [OpenAI evals cookbook — evals](https://platform.openai.com/docs/guides/evals) — skim what a “test” row looks like in industry docs: input, expected, graders. Do not buy their product.
3. Glossary: [pass@1 / pass@k](../glossary.md) in this repo.

## Lesson

### JSONL is the eval filesystem

A JSON array is one document. JSONL is a stream of trials you can append. Harnesses write one line per trial. You will grep it, you will tail it, you will check it into `data/` versioned next to the suite.

```text
{"task_id": "t01", "tag": "parser", "trial_index": 0, "passed": true}
{"task_id": "t01", "tag": "parser", "trial_index": 1, "passed": false}
```

Never pretty-print JSONL. One object, one line.

### pydantic at the boundary

```python
class Trial(BaseModel):
    task_id: str
    tag: str
    trial_index: int = Field(ge=0)
    passed: bool
```

`Trial.model_validate_json(line)` on each line. A missing `passed` must raise, not become `False`. Silent defaults in logs are how pass rates drift.

Inside the module, after validation, you may use dataclasses or plain functions. Do not pydantic-all-the-way through a hot loop of 10 rows — that is not the issue. Do not skip pydantic at the file edge — that *is* the issue.

### pass@1 vs pass@k

Group by `task_id`.

- **pass@1:** use trial_index `0` only (first sample). Fraction of tasks whose first trial passed.
- **pass@k:** a task counts if *any* of the first k trials passed (you may have fewer than k; then “any of what exists”).

If you average the boolean `passed` column across *all rows*, you are counting extra trials as extra tasks. That number is not pass@1. Eval papers get this wrong in internal decks every week.

### Slices

A headline pass rate that hides “parser 90%, harness 10%” will send you to the wrong lever. Always ship a by-tag table next to the headline. Same discipline as slicing App Insights by operation name.

### Failure mode this week: dropping bad lines

`if not line.strip(): continue` is fine. `except Exception: continue` is how you report pass@1 = 1.0 on a file that failed to parse 19 of 20 rows. Count `n_tasks` from **validated** trials and report `n_skipped_lines` separately. If skipped > 0, the headline is qualified.

## Must-do exercise

Folder: [exercises/week-03](../../exercises/week-03/)

1. Implement `metrics.load_trials`, `pass_at_1`, `pass_at_k`, `pass_rate_by_tag`.
2. `uv run pytest`.
3. Run the CLI against `data/trials.jsonl` and paste the table into your lab note.

The 20-row file is constructed so that row-average ≠ pass@1 ≠ pass@k. If those three numbers come out equal, your grouping is wrong.

## Stretch

- Load the same file with polars or pandas and reproduce pass@1. Keep pydantic as the validator; the dataframe is a view.
- Add a `bootstrap_ci` stub signature (implement for real in week 7).

## Definition of done

- [ ] All tests green.
- [ ] You can explain why averaging the `passed` column is not pass@1, using this week’s file as the example.
- [ ] Invalid lines raise or are counted as skipped — they do not become `passed=False`.
- [ ] By-tag rates use **tasks**, not trial rows, as the denominator.

## What breaks if you skip it

Weeks 7, 13, and 16 quote pass@k and CIs. If your aggregator is wrong, you will hill-climb a lie.

## Lab note

*What would make this number a lie?* Treating 20 trial rows as 20 tasks, or computing pass@k with `k=3` while silently dropping trial_index ≥ 1 because you loaded a JSON array instead of JSONL.
