/**
 * Map curriculum-relative links to app routes. Exercise paths stay external (terminal).
 */
export function resolveCurriculumHref(href: string): string | null {
  const normalized = href.replace(/\\/g, "/");
  if (normalized === "../00-start-here.md" || normalized.endsWith("00-start-here.md")) {
    return "/start";
  }
  if (normalized === "../glossary.md" || normalized.endsWith("glossary.md")) {
    return "/glossary";
  }
  const weekMatch = normalized.match(/week-(\d{2})\.md$/);
  if (weekMatch) {
    return `/week/week-${weekMatch[1]}`;
  }
  if (normalized.includes("curriculum/weeks/week-")) {
    const m = normalized.match(/week-\d{2}/);
    if (m) return `/week/${m[0]}`;
  }
  return null;
}

export function isExercisePath(href: string): boolean {
  return href.replace(/\\/g, "/").includes("exercises/week-");
}
