import Link from "next/link";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import {
  isExercisePath,
  resolveCurriculumHref,
} from "@/lib/markdown-links";

type Props = {
  markdown: string;
};

const proseClass =
  "lesson-prose prose prose-invert prose-slate max-w-none prose-headings:scroll-mt-20 prose-headings:font-semibold prose-headings:tracking-tight prose-headings:text-slate-50 prose-p:text-slate-300 prose-li:text-slate-300 prose-strong:text-slate-100 prose-a:font-medium prose-a:text-indigo-400 prose-a:no-underline hover:prose-a:text-indigo-300 prose-code:before:content-none prose-code:after:content-none prose-pre:p-4 prose-pre:shadow-inner prose-th:text-slate-200 prose-td:text-slate-300";

export function MarkdownLesson({ markdown }: Props) {
  return (
    <article className={proseClass}>
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          a: ({ href, children }) => {
            if (!href) return <span>{children}</span>;
            const route = resolveCurriculumHref(href);
            if (route) {
              return (
                <Link href={route} className="text-indigo-400 hover:text-indigo-300">
                  {children}
                </Link>
              );
            }
            if (isExercisePath(href) || href.startsWith("exercises/")) {
              return (
                <code className="font-mono text-sm text-emerald-200">
                  {href.replace(/^\.\.\/\.\.\//, "")}
                </code>
              );
            }
            if (href.startsWith("http://") || href.startsWith("https://")) {
              return (
                <a
                  href={href}
                  target="_blank"
                  rel="noreferrer"
                  className="text-indigo-400 hover:text-indigo-300"
                >
                  {children}
                </a>
              );
            }
            return (
              <code className="font-mono text-sm text-emerald-200">{href}</code>
            );
          },
        }}
      >
        {markdown}
      </ReactMarkdown>
    </article>
  );
}
