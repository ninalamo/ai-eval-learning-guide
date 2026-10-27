# Course viewer

Local Next.js app over `../curriculum` and exercise READMEs only. No `exercises/**/.env` is served.

```bash
npm install
npm run dev
```

Run these from **`web/`** (so the app can find `../curriculum`). If the catalog 500s after hot reload, stop dev and `rm -rf .next`, then `npm run dev` again.

Optional: `COURSE_REPO_ROOT=/path/to/AI Beginner npm run dev` if your cwd is not `web/`.

`npm audit` may report PostCSS issues inside Next.js. Avoid `npm audit fix --force` (it jumps to Next 16). For local dev, upgrading Next when a patched 15.x ships is enough.

Open http://localhost:3000 — catalog, weeks, start here, glossary. Checklists persist in `localStorage`.
