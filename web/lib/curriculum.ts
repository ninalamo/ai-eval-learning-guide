import fs from "node:fs/promises";
import path from "node:path";
import { REPO_ROOT } from "./repo-root";

const WEEKS_DIR = path.join(REPO_ROOT, "curriculum", "weeks");

export type WeekSummary = {
  id: string;
  number: number;
  title: string;
  phase: string;
  exerciseDir: string;
};

export function phaseForWeek(number: number): string {
  if (number <= 4) return "Phase 1 — Python for evals";
  if (number <= 8) return "Phase 2 — Eval science";
  if (number <= 12) return "Phase 3 — Harnesses";
  return "Phase 4 — Gauntlet loops";
}

function parseTitle(markdown: string, fallback: string): string {
  const line = markdown.split("\n").find((l) => l.startsWith("# "));
  if (!line) return fallback;
  return line.replace(/^#\s+/, "").trim();
}

export async function listWeeks(): Promise<WeekSummary[]> {
  const names = await fs.readdir(WEEKS_DIR);
  const files = names
    .filter((n) => /^week-\d{2}\.md$/.test(n))
    .sort((a, b) => a.localeCompare(b));

  const weeks: WeekSummary[] = [];
  for (const file of files) {
    const id = file.replace(/\.md$/, "");
    const number = Number.parseInt(id.replace("week-", ""), 10);
    const markdown = await fs.readFile(path.join(WEEKS_DIR, file), "utf-8");
    weeks.push({
      id,
      number,
      title: parseTitle(markdown, id),
      phase: phaseForWeek(number),
      exerciseDir: `exercises/${id}`,
    });
  }
  return weeks;
}

export function parseDefinitionOfDone(markdown: string): string[] {
  const match = markdown.match(
    /## Definition of done\s*\n([\s\S]*?)(?=\n## |\s*$)/i,
  );
  if (!match) return [];
  const block = match[1];
  const items: string[] = [];
  for (const line of block.split("\n")) {
    const m = line.match(/^- \[ \]\s+(.+)$/);
    if (m) items.push(m[1].trim());
  }
  return items;
}

export function stripDefinitionOfDone(markdown: string): string {
  return markdown.replace(
    /## Definition of done\s*\n[\s\S]*?(?=\n## |\s*$)/i,
    "",
  );
}

export async function readWeekMarkdown(weekId: string): Promise<string | null> {
  if (!/^week-\d{2}$/.test(weekId)) return null;
  const file = path.join(WEEKS_DIR, `${weekId}.md`);
  try {
    return await fs.readFile(file, "utf-8");
  } catch {
    return null;
  }
}

export async function readCurriculumDoc(
  relativePath: string,
): Promise<string | null> {
  const safe = path.normalize(relativePath).replace(/^(\.\.(\/|\\|$))+/, "");
  const file = path.join(REPO_ROOT, "curriculum", safe);
  if (!file.startsWith(path.join(REPO_ROOT, "curriculum"))) return null;
  try {
    return await fs.readFile(file, "utf-8");
  } catch {
    return null;
  }
}

export async function readExerciseReadme(weekId: string): Promise<string | null> {
  if (!/^week-\d{2}$/.test(weekId)) return null;
  const file = path.join(REPO_ROOT, "exercises", weekId, "README.md");
  try {
    return await fs.readFile(file, "utf-8");
  } catch {
    return null;
  }
}
