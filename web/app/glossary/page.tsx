import { Breadcrumbs } from "@/components/Breadcrumbs";
import { MarkdownLesson } from "@/components/MarkdownLesson";
import { readCurriculumDoc } from "@/lib/curriculum";

export default async function GlossaryPage() {
  const markdown = await readCurriculumDoc("glossary.md");
  if (!markdown) {
    return (
      <div className="mx-auto max-w-3xl px-4 py-12">
        <p className="text-slate-600">Glossary file not found.</p>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-3xl px-4 py-8 sm:px-6 lg:px-8">
      <Breadcrumbs
        items={[
          { label: "My learning", href: "/" },
          { label: "Glossary" },
        ]}
      />
      <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm sm:p-8">
        <MarkdownLesson markdown={markdown} />
      </div>
    </div>
  );
}
