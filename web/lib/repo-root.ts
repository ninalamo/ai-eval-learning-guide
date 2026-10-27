import fs from "node:fs";
import path from "node:path";

/**
 * Course repo root (parent of web/). `npm run dev` runs with cwd = web/.
 *
 * Do not use import.meta.url here — Next bundles server code under .next/ and
 * relative paths from __dirname/import.meta break in dev.
 */
function resolveRepoRoot(): string {
  if (process.env.COURSE_REPO_ROOT) {
    return path.resolve(process.env.COURSE_REPO_ROOT);
  }
  const fromCwd = path.resolve(process.cwd(), "..");
  const weeksDir = path.join(fromCwd, "curriculum", "weeks");
  if (fs.existsSync(weeksDir)) {
    return fromCwd;
  }
  // Fallback when cwd is already the repo root (e.g. some IDE run configs).
  const here = path.resolve(process.cwd());
  if (fs.existsSync(path.join(here, "curriculum", "weeks"))) {
    return here;
  }
  return fromCwd;
}

export const REPO_ROOT = resolveRepoRoot();
