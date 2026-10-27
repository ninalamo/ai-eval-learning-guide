import Link from "next/link";

type Crumb = { label: string; href?: string };

export function Breadcrumbs({ items }: { items: Crumb[] }) {
  return (
    <nav aria-label="Breadcrumb" className="mb-6 text-sm text-slate-400">
      <ol className="flex flex-wrap items-center gap-1.5">
        {items.map((item, i) => (
          <li key={i} className="flex items-center gap-1.5">
            {i > 0 ? <span className="text-slate-600">/</span> : null}
            {item.href ? (
              <Link
                href={item.href}
                className="font-medium text-indigo-400 hover:text-indigo-300"
              >
                {item.label}
              </Link>
            ) : (
              <span className="font-medium text-slate-200">{item.label}</span>
            )}
          </li>
        ))}
      </ol>
    </nav>
  );
}
