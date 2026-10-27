import Link from "next/link";
import type { WeekSummary } from "@/lib/curriculum";

type Props = {
  weeks: WeekSummary[];
  currentWeekId: string;
};

export function WeekSidebar({ weeks, currentWeekId }: Props) {
  const current = weeks.find((w) => w.id === currentWeekId);

  return (
    <aside
      className="hidden w-72 shrink-0 border-r border-slate-200 bg-white lg:block"
      aria-label="Course outline"
    >
      <div className="sticky top-14 max-h-[calc(100vh-3.5rem)] overflow-y-auto p-4">
        <p className="text-xs font-semibold uppercase tracking-wider text-slate-500">
          Course outline
        </p>
        {current ? (
          <p className="mt-2 text-sm font-medium text-slate-900">
            Week {current.number}
          </p>
        ) : null}
        <ul className="mt-4 space-y-0.5">
          {weeks.map((w) => {
            const active = w.id === currentWeekId;
            return (
              <li key={w.id}>
                <Link
                  href={`/week/${w.id}`}
                  className={`block rounded-lg px-3 py-2.5 text-sm transition ${
                    active
                      ? "bg-indigo-50 font-medium text-indigo-700 ring-1 ring-indigo-200"
                      : "text-slate-600 hover:bg-slate-50 hover:text-slate-900"
                  }`}
                >
                  <span className="text-xs text-slate-400">W{w.number}</span>
                  <span className="mt-0.5 line-clamp-2 block leading-snug">
                    {w.title.replace(/^Week \d+ —\s*/i, "")}
                  </span>
                </Link>
              </li>
            );
          })}
        </ul>
      </div>
    </aside>
  );
}
