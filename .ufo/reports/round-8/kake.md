# kake-shokunin — round 8 report

**Gap closed:** README residual "kimi subpaths (byte compare meaningless —
needs per-path title+marker)". First per-path baseline for the live kimi
fleet. Commit `9544914 round-8` in `kake-shokunin/`.

## Evidence (all read-only HTTP + local git; zero publishes, zero metered/browser ops)

- **Link sweep, 10 live kimi rows:** 44 same-origin links GET'd — 0 real
  non-200. Non-200s observed were sweep noise: inline-JS template literals
  (`${p.url}`, `${esc(...)}`) and Cloudflare `/cdn-cgi/` paths.
- **ds4cc.kimi.page sitemap parity:** canonical `sitemap.xml` (93 locs) →
  mirror: **19 served, 74 missing.** `git log --diff-filter=A` on every miss:
  all added post-publish (63×09-23, 10×09-22, 1×09-08) vs ~Aug-29 vintage
  (index max embedded date 2026-08-21). **Zero rot — pure staleness.** PQ-2
  is now quantified: republish delta = 74 canonical paths (all of magga/,
  burnerchrome/, infinizoom, omarchy-usage, omegag).
- **`dir/` href rot live-proofed:** mirror index links `omarchy-usage/`,
  `omegag/`, `speedrun/` → 404 on kimi; `*/index.html` twins → 200
  (`speedrun/index.html` = 200, 11 153B). Same hrefs work on GHP (`/dir`→301).
  Permanent until republish-with-rewrite — landed under the dir-index pitfall.
- **New structural fact** (`kimi-surface.mjs` :459-466 vs :903-908): `update`
  sends an index.html-only prompt ("replace the site files … verify zero
  residue"); `recreate`/`rebuild` zip the whole sourceDir minus
  `.git`/`.github`/`--zip-exclude`. Subpath richness depends on which verb
  last built a version; the orphaned 09-26 update fire (journal code 7) never
  touched live since publish is human.
- **Blind spot recorded:** vault/veigapunk-page render PROPERTIES[]
  client-side — static sweep sees only the `${p.url}` template; PQ-1-style
  rot needs rendered DOM.

## Files landed

- `corpus/knowledge/kimi-subpath-audit.md` — method, baseline tables,
  re-run recipe, vintage-classification rule.
- `corpus/lessons/round-8.md` — lesson.
- `SKILL.md` — drift-table row (kimi subpaths) + dir-index pitfall live proof.
- `corpus/README.md` — coverage row + gap closure (new residual: JS-rendered
  link surfaces).
- `LOG.md` — round-8 entry with evidence citations.

## Fleet state unchanged

No probes re-run beyond audit GETs; charter-ghp marker pin still stale
(keeper's queue, per round-7); dead rows untouched.
