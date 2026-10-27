# Glossary

Terms as an eval engineer uses them. If a week file uses a word without defining it, it lives here.

## Task

A single, versioned unit of work for an agent: instruction, environment, and a way to score the result. In Harbor: a directory with `instruction.md`, `task.toml`, `environment/`, `tests/`, optional `solution/`. A task is not a prompt snippet in a notebook.

## Instruction

The text the agent is allowed to see. States outcomes (files, commands, schemas), not hidden tests. If the instruction leaks the verifier, the task is contaminated.

## Gold / oracle / reference solution

A known-good way to complete the task (`solution/solve.sh`, a gold patch, a labeled answer). Used to prove the **task and verifier are solvable**, not to prove the model is good. If the oracle fails, you do not have an eval — you have a broken test.

## Trial

One attempt by one agent configuration on one task. Produces a trajectory (tool calls, files, stdout) and artifacts (patch, logs). Trials are the rows you later aggregate.

## Run

A batch of trials under a **frozen** configuration: same suite, model, prompt, tools, timeouts, harness version. Changing any of those starts a new run. Comparing two runs that silently differ in timeout is not an experiment.

## Suite / gauntlet

A frozen list of tasks you re-run. Small on purpose while you learn (3–10). A gauntlet is the suite plus the **loop**: run, score, diagnose, mutate one lever, rerun, keep or revert.

## Harness

The machinery that: provisions an isolated environment, gives the agent the instruction, captures artifacts, and invokes the grader **without trusting the agent’s own claim of success**. If the agent and the grader share a writable test tree, you do not have a harness.

## Trusting harness

Scores by running tests *in the workspace the agent just edited*, or by believing stdout (“all tests passed”). A cheating agent wins. Week 5 exists to make this visceral.

## Ground-truth / separate verifier / patch replay

Capture what the agent changed (usually `git diff` / `model.patch`). Apply that patch to a **clean** copy of the environment. Run tests the agent never saw, or at least never got to keep edits to. SWE-bench Pro V2’s locked protocol is this idea at scale.

## Grader / scorer / verifier

The function that turns a trial into a number (often 0/1, sometimes a vector of metrics). Kinds you will implement:

- **Deterministic:** unit tests, exact match, JSON schema, file exists, command output.
- **Trajectory:** which tools ran, in what order, whether a forbidden tool ran.
- **LLM-as-judge:** a model grades with a rubric. Cheap and noisy; must be calibrated against humans.

## Reward

Harbor’s name for the verifier output: `/logs/verifier/reward.txt` (one number) or `reward.json` (named metrics). `1`/`0` is pass/fail. Do not invent a 0–100 “quality score” until you can defend the rubric.

## Leakage

The agent saw something it should not: gold patch in git history, hidden tests on disk, grader source, future commits, network to GitHub. Leakage inflates scores without inflating capability.

## Contamination

Training or prompt data includes the benchmark. Canaries (comments in `instruction.md`) exist so you can detect it later. You cannot fully prevent contamination; you can detect and version.

## Reward hacking

The agent optimizes the **grader**, not the **task**: edits tests, stubs checkers, writes the answer into the scorer, disables assertions. Hidden tests and separate verifiers exist because of this.

## Pass@1 / pass@k

Pass@1: fraction of tasks the agent solved on a single trial. Pass@k: fraction solved at least once in k independent trials. Coding agents are noisy; pass@1 from one sample is a weak claim.

## Confidence interval (CI)

A range around a pass rate that would often contain the “true” rate if you repeated the experiment. Bootstrap CI on trials is enough for this course. A 3-point gain on n=5 with overlapping CIs is not a win.

## Paired comparison

Score the **same tasks** under baseline vs candidate. Do not compare 8 tasks on model A to 8 different tasks on model B. Pairing is how you attribute the change.

## Holdout

Tasks (or hidden tests) the agent and the hill-climb process did not iterate on. A suite that only goes up is a warning: you may be fitting the suite.

## Trajectory

The ordered record of messages and tool calls. Outcome graders ask “did tests pass?” Trajectory graders ask “did it get there by a path we accept?” Both can lie; they lie differently.

## Failure taxonomy

Labels on failed trials. A label is only useful if it maps to a **repair surface** (what you would change): prompt, tool contract, harness, grader, task wording, environment, model ceiling. “It failed” is not a class. Catch-all buckets fail week 8.

## Repair surface / lever

The one thing you change in a gauntlet iteration: system prompt, tool description, timeout, model, context policy, verifier bug. Bundling two levers makes attribution impossible.

## Hill-climb

Local search over levers: hypothesize, change one, rerun the frozen suite, keep only if the targeted class improves and regressions do not appear. Not “tweak until the demo looks good.”

## Inspect AI

UK AISI eval framework. Building blocks: **dataset**, **solver** (how the model/agent produces an answer), **scorer**, **sandbox**. Logs are the product; `inspect view` is how you read them.

## Harbor

Task *format* and runner from the Terminal-Bench authors. Tasks are directories other runners can consume. Inspect Harbor is one way to run Harbor tasks inside Inspect.

## Subject vs judge

**Subject:** the agent/model you are measuring. **Judge:** a model used as a grader. Never silently use the same model as both without saying so; you will grade its own style as correctness.

## Scripted agent / stub agent

Deterministic behavior (honest patch, noop, cheat). Used to test the **harness**, not the model. If your harness cannot fail a cheat, no model score from it is publishable.
