import Link from "next/link";

const nav = [
  { href: "/", label: "My learning" },
  { href: "/setup", label: "Setup" },
  { href: "/start", label: "Start here" },
  { href: "/glossary", label: "Glossary" },
];

export function SiteHeader() {
  return (
    <header className="sticky top-0 z-50 border-b border-white/10 bg-brand-950 text-white shadow-lg shadow-black/20">
      <div className="mx-auto flex h-14 max-w-7xl items-center justify-between gap-6 px-4 sm:px-6 lg:px-8">
        <Link href="/" className="flex items-center gap-2.5 font-semibold tracking-tight">
          <span
            className="flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-to-br from-indigo-500 to-violet-600 text-sm font-bold"
            aria-hidden
          >
            AE
          </span>
          <span className="hidden sm:inline">AI Evaluation Engineer</span>
        </Link>
        <nav className="flex items-center gap-1 text-sm font-medium">
          {nav.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="rounded-md px-3 py-2 text-slate-300 transition hover:bg-white/10 hover:text-white"
            >
              {item.label}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
