> **Platforms:** Fedora, Ubuntu, macOS, Windows — [setup guide](../../curriculum/setup-your-machine.md). Use `uv run` from this folder after `uv sync`. On Windows, `cd exercises\week-NN` or forward slashes both work.

# Week 1 exercise — port the test-result summarizer

C# sketch: `csharp-reference/TestResultSummary.cs`  
Python stubs: `src/summarize.py`  
Tests: `tests/test_summarize.py`  
Fixture data: `data/results.json`

```bash
cd exercises/week-01
uv sync
uv run pytest
```

Implement every `raise NotImplementedError` in `src/summarize.py`. Do not edit tests to make them pass unless a test is genuinely wrong — then fix the test and note why in your lab log.
