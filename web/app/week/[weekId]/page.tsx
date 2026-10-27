import Link from "next/link";
import { notFound } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { DefinitionOfDone } from "@/components/DefinitionOfDone";
import { MarkdownLesson } from "@/components/MarkdownLesson";
import { WeekSidebar } from "@/components/WeekSidebar";
import {
  listWeeks,
  parseDefinitionOfDone,
  readExerciseReadme,
  readWeekMarkdown,
  stripDefinitionOfDone,
} from "@/lib/curriculum";

type Props = {
  params: Promise<{ weekId: string }>;
};

export default async function WeekPage({ params }: Props) {
  const { weekId } = await params;
  const markdown = await readWeekMarkdown(weekId);
  if (!markdown) notFound();

  const weeks = await listWeeks();
  const current = weeks.find((w) => w.id === weekId);
  const checklist = parseDefinitionOfDone(markdown);
  const body = stripDefinitionOfDone(markdown);
  const exerciseReadme = await readExerciseReadme(weekId);

  const title = current?.title ?? weekId;
  const shortTitle = title.replace(/^Week \d+ —\s*/i, "");

  return (
    <div className="flex min-h-[calc(100vh-3.5rem)]">
      <WeekSidebar weeks={weeks} currentWeekId={weekId} />
      <div className="min-w-0 flex-1">
        <div className="border-b border-slate-800 bg-slate-900/80">
          <div className="mx-auto max-w-3xl px-4 py-6 sm:px-6 lg:px-8">
            <Breadcrumbs
              items={[
                { label: "My learning", href: "/" },
                { label: shortTitle },
              ]}
            />
            <h1 className="text-2xl font-bold tracking-tight text-slate-50 sm:text-3xl">
              {title}
            </h1>
            {current ? (
              <p className="mt-2 text-sm text-slate-400">{current.phase}</p>
            ) : null}
            <div className="mt-4 flex flex-wrap gap-2 lg:hidden">
              <Link
                href="/"
                className="text-sm font-medium text-indigo-400 hover:text-indigo-300"
              >
                ← All modules
              </Link>
            </div>
          </div>
        </div>

        <div className="mx-auto max-w-3xl px-4 py-8 sm:px-6 lg:px-8">
          <MarkdownLesson markdown={body} />
          <DefinitionOfDone weekId={weekId} items={checklist} />
          {exerciseReadme ? (
            <section className="mt-10 rounded-xl border border-slate-700 bg-slate-900/60 p-6 shadow-sm">
              <div className="flex items-center justify-between gap-4">
                <h2 className="text-lg font-bold text-slate-50">Lab exercise</h2>
                <span className="rounded-full bg-indigo-500/20 px-3 py-1 text-xs font-semibold text-indigo-300 ring-1 ring-indigo-500/30">
                  Terminal
                </span>
              </div>
              <p className="mt-2 text-sm text-slate-400">
                Work in{" "}
                <code className="rounded bg-slate-950 px-1.5 py-0.5 font-mono text-xs text-emerald-200 ring-1 ring-slate-600">
                  exercises/{weekId}/
                </code>
              </p>
              <div className="mt-4 rounded-lg border border-slate-700 bg-slate-950 p-4">
                <MarkdownLesson markdown={exerciseReadme} />
              </div>
            </section>
          ) : null}

          <nav className="mt-12 flex justify-between border-t border-slate-800 pt-8">
            {current && current.number > 1 ? (
              <Link
                href={`/week/week-${String(current.number - 1).padStart(2, "0")}`}
                className="text-sm font-semibold text-indigo-400 hover:text-indigo-300"
              >
                ← Previous week
              </Link>
            ) : (
              <span />
            )}
            {current && current.number < weeks.length ? (
              <Link
                href={`/week/week-${String(current.number + 1).padStart(2, "0")}`}
                className="text-sm font-semibold text-indigo-400 hover:text-indigo-300"
              >
                Next week →
              </Link>
            ) : null}
          </nav>
        </div>
      </div>
    </div>
  );
}
