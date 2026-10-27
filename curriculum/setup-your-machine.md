# Setup your machine

This course runs on **Fedora**, **Ubuntu** (and similar Linux), **macOS**, and **Windows 10/11**. The exercises are the same everywhere; only how you open a terminal and install tools differs.

## What you need

| Tool | Why |
|------|-----|
| [uv](https://docs.astral.sh/uv/) | Python version + `.venv` per exercise (like `dotnet` + NuGet per project) |
| Python **3.12+** | Installed and managed by `uv` — avoid relying on the OS “system” Python |
| [git](https://git-scm.com/) | Clone and track the repo |
| [Node.js 20+](https://nodejs.org/) | Optional: local [course viewer](../web/README.md) (`web/`) |
| [Docker Desktop](https://www.docker.com/products/docker-desktop/) | Weeks 10–12 stretch and Harbor-style tasks; Linux can use engine only |

Azure OpenAI or another API key is only required for some **optional** live-model runs (weeks 4, 10, 15). Oracle/stub agents and pytest should work offline.

## Pick a terminal

Use a terminal where `uv` and `git` are on your `PATH`.

| OS | Good defaults |
|----|----------------|
| **Fedora / Ubuntu** | Default terminal (`bash` or your shell of choice) |
| **macOS** | Terminal.app or iTerm — `zsh` is fine |
| **Windows** | **Windows Terminal** with **PowerShell** or **Git Bash** ([Git for Windows](https://git-scm.com/download/win)) |

**Windows note:** All command snippets in lessons use Unix-style paths (`exercises/week-01`). In PowerShell you can `cd exercises\week-01` or `cd exercises/week-01` — both work. Python code must use **`pathlib.Path`**, never `dir + "\\" + file`.

**WSL2 (optional on Windows):** If you already use Ubuntu on WSL for Docker and shell scripts, run the exercises inside WSL. You do not *have* to use WSL for weeks 1–10; week 11 Harbor `test.sh` files are exercised locally via `verify_local.py` on every OS.

## Install `uv`

Follow the official installer for your OS: [Installing uv](https://docs.astral.sh/uv/getting-started/installation/).

Quick checks (any OS):

```bash
uv --version
```

On Windows, if `uv` is not found after install, open a **new** terminal window so `PATH` refreshes.

## First exercise (smoke test)

From the **repo root**:

```bash
cd exercises/week-01
uv sync
uv run pytest
```

You should see tests run (they fail until you implement the stubs — that is expected on first open).

### Windows (PowerShell) equivalent

```powershell
cd exercises\week-01
uv sync
uv run pytest
```

## Course viewer (optional)

From the repo root:

```bash
cd web
npm install
npm run dev
```

Open http://localhost:3000. If paths break, run dev from `web/` (see [web/README.md](../web/README.md)).

## Docker

- **macOS / Windows:** Install Docker Desktop; enable WSL2 backend on Windows if prompted.
- **Fedora / Ubuntu:** Docker Engine or Docker Desktop — either is fine as long as `docker ps` works for your user.

Inspect and Harbor stretches assume a working Docker daemon. If Docker is not available, stay on pytest/oracle paths and note it in your lab log.

## Paths, encoding, and line endings

- **Paths in Python:** `Path("data") / "results.json"` works on Linux, macOS, and Windows.
- **Encoding:** Always `encoding="utf-8"` when reading eval artifacts. Do not depend on the OS locale.
- **Git on Windows:** `git config core.autocrlf true` (or `input` on macOS/Linux) avoids surprise `^M` in shell scripts inside Harbor tasks.

## Secrets

Copy each week’s `.env.example` to `.env` when you need live API calls. Never commit `.env`. Use the same Key Vault / env patterns you already use on Azure — the course does not special-case one cloud.

## CI vs laptop

Week 2’s sample workflow targets **Linux** (`ubuntu-latest` in GitHub Actions). That is intentional: most eval harnesses run in Linux containers. If pytest is green on your machine (any OS), it should be green in CI when paths and encoding are portable.

## When something only works on Linux

Harbor verifiers often use `bash` and paths like `/app/out.txt` **inside a container**, not on your host. For this repo:

- **Week 11:** `uv run python verify_local.py` simulates the verifier on **all** platforms.
- **Stretch:** Running `test.sh` directly may require Git Bash, WSL, or Docker — optional.

## Getting unstuck

| Problem | Try |
|---------|-----|
| `uv: command not found` | Reopen terminal; confirm install PATH (Windows: user env vars). |
| Wrong Python version | Run commands with `uv run …` from the exercise folder after `uv sync`. |
| Viewer 500 / missing curriculum | `cd web`, `rm -rf .next`, `npm run dev` again. |
| Docker permission denied (Linux) | Add user to `docker` group or use `sudo` per your distro docs. |

Then continue with [Start here](00-start-here.md) and [week 1](weeks/week-01.md).
