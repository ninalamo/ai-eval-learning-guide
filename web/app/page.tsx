import Link from "next/link";
import { listWeeks } from "@/lib/curriculum";

function phaseAccent(phase: string): string {
  if (phase.startsWith("Phase 1")) return "border-l-indigo-500";
  if (phase.startsWith("Phase 2")) return "border-l-violet-500";
  if (phase.startsWith("Phase 3")) return "border-l-amber-500";
  return "border-l-rose-500";
}

export default async function HomePage() {
  const weeks = await listWeeks();
  const phases = Array.from(new Set(weeks.map((w) => w.phase)));

  return (
    <>
      <section className="bg-gradient-to-br from-slate-900 via-indigo-950 to-violet-900 text-white">
        <div className="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
          <p className="text-sm font-semibold uppercase tracking-widest text-indigo-300">
            Personal learning path
          </p>
          <h1 className="mt-3 max-w-2xl text-3xl font-bold tracking-tight sm:text-4xl">
            Agent evaluation engineer
          </h1>
          <p className="mt-4 max-w-xl text-lg text-slate-300">
            16 weeks — harnesses, graders, and gauntlet loops. Lessons from your
            repo; exercises in the terminal with{" "}
            <code className="rounded bg-white/10 px-1.5 py-0.5 text-sm text-indigo-100">
              uv run pytest
            </code>
            .
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Link
              href="/week/week-01"
              className="inline-flex items-center rounded-lg bg-brand-accent px-5 py-2.5 text-sm font-semibold text-white shadow-lg shadow-orange-900/30 transition hover:bg-brand-accent-hover"
            >
              Start week 1
            </Link>
            <Link
              href="/start"
              className="inline-flex items-center rounded-lg border border-white/25 bg-white/10 px-5 py-2.5 text-sm font-semibold text-white backdrop-blur transition hover:bg-white/20"
            >
              Read orientation
            </Link>
          </div>
        </div>
      </section>

      <div className="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
        {phases.map((phase) => (
          <section key={phase} className="mb-12">
            <h2 className="text-lg font-bold text-slate-900">{phase}</h2>
            <p className="mt-1 text-sm text-slate-500">
              {weeks.filter((w) => w.phase === phase).length} modules
            </p>
            <ul className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {weeks
                .filter((w) => w.phase === phase)
                .map((w) => (
                  <li key={w.id}>
                    <Link
                      href={`/week/${w.id}`}
                      className={`group flex h-full flex-col rounded-xl border border-slate-200/80 bg-white p-5 shadow-sm transition hover:border-indigo-200 hover:shadow-md border-l-4 ${phaseAccent(phase)}`}
                    >
                      <span className="text-xs font-bold uppercase tracking-wide text-indigo-600">
                        Week {w.number}
                      </span>
                      <span className="mt-2 flex-1 text-base font-semibold leading-snug text-slate-900 group-hover:text-indigo-700">
                        {w.title.replace(/^Week \d+ —\s*/i, "")}
                      </span>
                      <span className="mt-4 text-xs font-medium text-slate-400">
                        {w.exerciseDir}
                      </span>
                      <span className="mt-3 text-sm font-semibold text-indigo-600">
                        Open module →
                      </span>
                    </Link>
                  </li>
                ))}
            </ul>
          </section>
        ))}
      </div>
    </>
  );
}
