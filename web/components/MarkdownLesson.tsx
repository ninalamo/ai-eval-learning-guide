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
  "prose prose-slate max-w-none prose-headings:scroll-mt-20 prose-headings:font-semibold prose-headings:tracking-tight prose-a:font-medium prose-a:text-indigo-600 prose-a:no-underline hover:prose-a:text-indigo-800 prose-code:rounded prose-code:bg-slate-100 prose-code:px-1 prose-code:py-0.5 prose-code:text-sm prose-code:before:content-none prose-code:after:content-none prose-pre:bg-slate-900 prose-pre:text-slate-100";

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
                <Link href={route} className="text-indigo-600 hover:text-indigo-800">
                  {children}
                </Link>
              );
            }
            if (isExercisePath(href) || href.startsWith("exercises/")) {
              return (
                <code className="font-mono text-sm text-slate-700">
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
                  className="text-indigo-600 hover:text-indigo-800"
                >
                  {children}
                </a>
              );
            }
            return (
              <code className="font-mono text-sm text-slate-700">{href}</code>
            );
          },
        }}
      >
        {markdown}
      </ReactMarkdown>
    </article>
  );
}
