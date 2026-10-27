import { Breadcrumbs } from "@/components/Breadcrumbs";
import { MarkdownLesson } from "@/components/MarkdownLesson";
import { readCurriculumDoc } from "@/lib/curriculum";

export default async function SetupPage() {
  const markdown = await readCurriculumDoc("setup-your-machine.md");
  if (!markdown) {
    return (
      <div className="mx-auto max-w-3xl px-4 py-12">
        <p className="text-slate-400">Setup guide not found.</p>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-3xl px-4 py-8 sm:px-6 lg:px-8">
      <Breadcrumbs
        items={[
          { label: "My learning", href: "/" },
          { label: "Setup" },
        ]}
      />
      <div className="rounded-xl border border-slate-700 bg-slate-900/60 p-6 shadow-sm sm:p-8">
        <MarkdownLesson markdown={markdown} />
      </div>
    </div>
  );
}
