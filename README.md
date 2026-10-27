# AI Evaluation Engineer — personal curriculum

A 16-week path from senior .NET/Azure full-stack to **agent / coding-agent Evaluation Engineer**.

The job is not “learn ML.” It is **making a number about an agent trustworthy, then using that number to improve one lever at a time.**

This repo is the course: weekly lessons, glossary, and exercise starters. A **local Next.js viewer** under [`web/`](web/) gives you a catalog, week reader, and definition-of-done checklists (browser `localStorage`). Python exercises still run in the terminal with `uv`.

```bash
cd web && npm install && npm run dev
```

Work in the files or the viewer; keep a lab notebook; ship a capstone report at week 16.

## Who this is for

Built for [Nin Alamo](curriculum/00-start-here.md): senior C# / ASP.NET Core / Azure, TDD, Docker, CI/CD, production Azure OpenAI, PR review, teaching OOP. Python weeks are a **language transfer**, not CS 101.

Target role: harnesses, gauntlet loops, SWE-bench-style tasks, graders, failure analysis, iterating the agent.

## How to use a week

1. Read [curriculum/00-start-here.md](curriculum/00-start-here.md) once, then that week’s file under [curriculum/weeks/](curriculum/weeks/).
2. Do the must-do exercise in `exercises/week-XX/`. Stretch is optional.
3. Write a short lab note (the prompt is at the bottom of every week). Keep notes outside git or in a private file — they are for you, not for the repo.
4. Do not start the next week until the definition of done is honestly true.

Time box: **~8 hours** (2 read, 4 build, 2 write-up). Compression path: 12 weeks — merge 1–2, 7–8, and 15–16 if Python clicks fast.

## Assumptions

- **OS:** Fedora, Ubuntu (or similar Linux), macOS, or Windows 10/11 — see [Setup your machine](curriculum/setup-your-machine.md).
- Python 3.12+ via [uv](https://docs.astral.sh/uv/), Docker (for later harness weeks), git.
- One model API for later weeks: Azure OpenAI (you already shipped this) or OpenAI/Anthropic. Cheap models for loops. Scripted/oracle agents when the lesson is the harness, not the model.
- Do **not** run all of SWE-bench Verified. Tiny frozen suites (3–10 tasks) until the process is muscle memory.

## Non-goals

Transformers from scratch, RAGAS-heavy product RAG evals, hosted auth/quizzes, training models, full public leaderboards.

The viewer reads `curriculum/` in place — it is not a second copy of the course.

## 16-week map

```text
Phase 1  Python for evals     weeks 1–4
Phase 2  Eval science         weeks 5–8
Phase 3  Harnesses            weeks 9–12
Phase 4  Gauntlet loops       weeks 13–16
```

| Week | Lesson | Exercise |
|------|--------|----------|
| [1](curriculum/weeks/week-01.md) | Runtime and idioms (`uv`, types, `pathlib`, dataclasses) | Port a test-result summarizer |
| [2](curriculum/weeks/week-02.md) | Quality bar (pytest, ruff, mypy, CI) | Tiny `grader` package + workflow |
| [3](curriculum/weeks/week-03.md) | Eval data shapes (pydantic, JSONL, slices) | 20-row dataset → pass@1 / pass@k |
| [4](curriculum/weeks/week-04.md) | Models and processes (`httpx`, asyncio, subprocess) | One trial artifact + exact-match score |
| [5](curriculum/weeks/week-05.md) | Trustworthy eval anatomy | Trusting harness vs ground-truth; cheats |
| [6](curriculum/weeks/week-06.md) | Graders (tests, schema, judge, trajectory) | Three graders, five tasks, disagreement |
| [7](curriculum/weeks/week-07.md) | Statistics that survive noise | False “win” on n=3 |
| [8](curriculum/weeks/week-08.md) | Failure taxonomy → repair surface | Classify eight traces |
| [9](curriculum/weeks/week-09.md) | Mini-harness from scratch | Three toy tasks; patch replay |
| [10](curriculum/weeks/week-10.md) | Inspect AI | One sandbox coding task; read the log |
| [11](curriculum/weeks/week-11.md) | Harbor task format | Author two tasks (terminal + unit-test) |
| [12](curriculum/weeks/week-12.md) | Hardening | Attack week 9; close holes; threat model |
| [13](curriculum/weeks/week-13.md) | Public slice | Five-task run report |
| [14](curriculum/weeks/week-14.md) | Gauntlet loop | Two iterations; one lever each |
| [15](curriculum/weeks/week-15.md) | Real agent as subject | Stub vs CLI/Cursor SDK; explain the delta |
| [16](curriculum/weeks/week-16.md) | Capstone | 10-task gauntlet + hill-climb + report |

Gauntlet loop you will be able to defend at week 16:

```text
freeze suite → run trials → score verifiers → taxonomy from traces
  → change one lever → rerun the same suite → keep or revert
```

## Week 16 bar

You can author a Harbor-format task, explain why a trusting harness is worthless, grade a patch on a clean environment, classify failures into repair surfaces, run a frozen gauntlet, change one lever, and defend the before/after number (n, CI, holdouts). Python was only the language the job is written in.

## Docs

- [Setup your machine](curriculum/setup-your-machine.md) — Fedora, Ubuntu, macOS, Windows
- [Start here — profile gap and C# maps](curriculum/00-start-here.md)
- [Glossary](curriculum/glossary.md)
- [Weeks](curriculum/weeks/)
