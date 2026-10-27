# AGENTS.md

Guidance for AI coding agents working in this repository.

## What this repo is

A **personal 16-week curriculum** (markdown + Python exercise starters) and a **local Next.js course viewer** (`web/`). The learner completes exercises in the terminal; the viewer reads `curriculum/` and exercise READMEs from disk — it is not a second source of truth for lessons.

**Non-goals:** auth, quizzes, in-browser Python, hosted progress APIs, copying curriculum into the app bundle.

## Layout

| Path | Purpose |
|------|---------|
| `curriculum/` | Lessons (`weeks/week-NN.md`), `00-start-here.md`, `glossary.md` |
| `exercises/week-NN/` | Per-week Python packages (`pyproject.toml`, `src/`, `tests/`); starters often raise `NotImplementedError` for the learner |
| `web/` | Next.js 15 App Router viewer (Tailwind v4) |
| `.cursor/plans/` | Planning artifacts — do not edit unless the user asks |

## Platforms

Curriculum targets **Fedora, Ubuntu, macOS, and Windows**. Cross-platform setup lives in `curriculum/setup-your-machine.md` (viewer route `/setup`). Exercise code should use `pathlib`; Harbor `.sh` oracles are validated via `verify_local.py` on all hosts.

## Commands

**Viewer (always from `web/`):**

```bash
cd web && npm install && npm run dev
```

If catalog/week routes 500 after errors or hot reload: `rm -rf web/.next` and restart dev.

**Exercises (per week directory):**

```bash
cd exercises/week-NN
uv sync
uv run pytest
uv run ruff check .
```

Optional: `COURSE_REPO_ROOT=/absolute/path/to/repo npm run dev` when cwd is not `web/`.

## Web app conventions

- **Repo root resolution:** `web/lib/repo-root.ts` uses `process.cwd()` and optional `COURSE_REPO_ROOT`. **Do not use `import.meta.url` or `__dirname` for curriculum paths** — bundled server code breaks under `.next/`.
- **Tracing:** `web/next.config.ts` sets `outputFileTracingRoot` to the parent of `web/` so production builds can read `../curriculum`.
- **Routes:** `/` catalog, `/week/[weekId]`, `/start`, `/glossary`. Week IDs match filenames (`week-01` … `week-16`).
- **Progress:** Definition-of-done checklists only — `localStorage` key prefix `ai-eval-dod:` in `DefinitionOfDone`. No server persistence.
- **Markdown:** `MarkdownLesson` + link rewriting (`lib/markdown-links.ts`). Do not serve `exercises/**/.env` or secrets.
- **Styling:** Tailwind in `web/app/globals.css` (`@import "tailwindcss"`, `@tailwindcss/typography`). Prefer existing components under `web/components/`.

## Curriculum and exercises

- Week markdown may include a **Definition of done** section; the viewer parses it for checklists. Keep that heading consistent if you edit weeks.
- Exercise **answers** and local lab notes stay out of git (see `.gitignore`: `exercises/week-08/answers.json`, `lab-notes/*.local.md`, `.env`).
- When adding a week: pair `curriculum/weeks/week-NN.md` with `exercises/week-NN/` and ensure `listWeeks()` in `web/lib/curriculum.ts` still discovers the week (filename pattern).

## Change discipline

- **Minimize scope.** This is a learning repo; avoid drive-by refactors across all 16 exercise folders.
- **Do not** run `npm audit fix --force` in `web/` (pulls Next 16; project targets Next 15).
- **Do not** commit secrets, learner answer files, or `node_modules` / `.next`.
- **Commits:** only when the user explicitly asks.
- If the user is doing the curriculum as a learner, **do not implement their exercise solutions** unless they ask for hints or review — prefer explaining and pointing at tests.

## Security

- Viewer is local-only; treat any future network or file upload features as out of scope unless specified.
- Never log or embed API keys from exercise `.env` files in the web app.

## Quick debugging

| Symptom | Likely cause |
|---------|----------------|
| `scandir .../web/curriculum/weeks` | Dev server not run from `web/`, or broken `REPO_ROOT` — fix `repo-root.ts`, not duplicate curriculum under `web/` |
| Missing `.next` manifests | Corrupt cache — delete `web/.next` |
| Week 404 | `weekId` must match `week-NN` and file must exist under `curriculum/weeks/` |
