"use client";

import { useEffect, useState } from "react";

const STORAGE_PREFIX = "ai-eval-dod:";

type Props = {
  weekId: string;
  items: string[];
};

export function DefinitionOfDone({ weekId, items }: Props) {
  const [checked, setChecked] = useState<Record<number, boolean>>({});

  useEffect(() => {
    const raw = localStorage.getItem(`${STORAGE_PREFIX}${weekId}`);
    if (!raw) return;
    try {
      const parsed = JSON.parse(raw) as Record<string, boolean>;
      const next: Record<number, boolean> = {};
      for (const [k, v] of Object.entries(parsed)) {
        next[Number(k)] = v;
      }
      setChecked(next);
    } catch {
      /* ignore corrupt storage */
    }
  }, [weekId]);

  function toggle(index: number) {
    setChecked((prev) => {
      const next = { ...prev, [index]: !prev[index] };
      const serial: Record<string, boolean> = {};
      for (const [k, v] of Object.entries(next)) {
        if (v) serial[k] = true;
      }
      localStorage.setItem(
        `${STORAGE_PREFIX}${weekId}`,
        JSON.stringify(serial),
      );
      return next;
    });
  }

  if (items.length === 0) return null;

  const doneCount = items.filter((_, i) => checked[i]).length;
  const pct = Math.round((doneCount / items.length) * 100);

  return (
    <section
      className="mt-10 overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm"
      aria-labelledby="dod-heading"
    >
      <div className="border-b border-slate-100 bg-gradient-to-r from-indigo-50 to-violet-50 px-6 py-4">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <h2
              id="dod-heading"
              className="text-lg font-bold text-slate-900"
            >
              Definition of done
            </h2>
            <p className="mt-1 text-sm text-slate-600">
              Check off each item before you move on. Saved in this browser.
            </p>
          </div>
          <div className="text-right">
            <p className="text-2xl font-bold tabular-nums text-indigo-600">
              {pct}%
            </p>
            <p className="text-xs font-medium text-slate-500">
              {doneCount} of {items.length}
            </p>
          </div>
        </div>
        <div className="mt-4 h-2 overflow-hidden rounded-full bg-white/80 ring-1 ring-slate-200/80">
          <div
            className="h-full rounded-full bg-gradient-to-r from-indigo-500 to-violet-600 transition-all duration-300"
            style={{ width: `${pct}%` }}
          />
        </div>
      </div>
      <ul className="divide-y divide-slate-100 px-2 py-2">
        {items.map((label, index) => {
          const isOn = Boolean(checked[index]);
          return (
            <li key={index}>
              <label
                className={`flex cursor-pointer gap-3 rounded-lg px-4 py-3 transition hover:bg-slate-50 ${
                  isOn ? "bg-emerald-50/50" : ""
                }`}
              >
                <input
                  type="checkbox"
                  checked={isOn}
                  onChange={() => toggle(index)}
                  className="mt-1 h-4 w-4 shrink-0 rounded border-slate-300 text-indigo-600 focus:ring-indigo-500"
                />
                <span
                  className={`text-sm leading-relaxed ${
                    isOn ? "text-slate-700 line-through decoration-slate-400" : "text-slate-800"
                  }`}
                >
                  {label}
                </span>
              </label>
            </li>
          );
        })}
      </ul>
    </section>
  );
}
