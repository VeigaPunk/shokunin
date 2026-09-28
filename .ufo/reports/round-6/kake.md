# kake-shokunin — round 6

Domain: web properties & publishing (ds4cc.com, kimi.page/pro mirrors, Pages deploys).
Commit: `8755018 round-6` in `kake-shokunin/`. Zero publishes, zero metered ops — reads, fetches, and git state only.

## Gap closed

The README's residual "GHP subpath rot beyond `index.html` is still invisible" gap — closed with a procedure + first live baseline, not new tooling (a gap in *coverage definition*, not just tooling).

## Evidence produced (live, 2026-09-28 ~16:45Z)

- **Baseline spotcheck: 2 352 sourceDir paths across the three GHP rows** (ds4cc-com 1 874, plazir15-ghp 35, charter-ghp 443), GET live + sha256 vs source *and* vs `git show origin/main:<rel>`. Result: **0 true rot**.
- **126 non-clean results — all decomposed to git state, none to deploy rot.** This produced the core deliverable: a classification table where `live ≠ origin/main` is the only actionable class. At audit time ds4cc-marketplace was 20 commits ahead (incl. live-404 `robots.txt`/`sitemap.xml`/`404.html`/`marketplace/plugins/infinizoom/main.js` — all unpushed additions), plazir-15-site 5 ahead, charter-ufo-fsd 2 behind (`b74190e` static-index bake → 8.6 KB vs 50.9 KB index gap).
- **`reconcile` coverage corrected from source** (`~/Projects/webzites/src/reconcile.mjs:55-107`): it scores `index.html` candidates (marker+2, title+1, depth ≤2) and compares **ONE** file — SKILL.md's old "subpaths beyond index" blind spot was understated; even additional `index.html` files are invisible.
- **`in-sync` on GHP masks byte drift** — `in-sync` = title+marker parity, a kimi affordance misapplied to a verbatim-byte surface. charter-ghp logged `in-sync` while index differed 6×. Documented as "treat `in-sync` on GHP as `git fetch` + spotcheck," with 09-21 keeper-log precedent (`git pull` → `match`).
- **GHP path semantics live-verified**: `/dir` → 301 → `/dir/` → `index.html` (inverse of kimi's no-dir-indexes); `.md` served raw (charter `beats/*.md` → 200); missing path = real 404 status + stock body (unlike kimi soft-200 preview-404).

## Files

- `corpus/knowledge/ghp-subpath-spotcheck.md` — coverage table per verb, `in-sync` masking, procedure, classification table, GHP-vs-kimi semantics, limits.
- `SKILL.md` — reconcile blind spot corrected; new "GHP subpaths" row in drift table; dir-index bullet now contrasts verified GHP behavior.
- `corpus/README.md` — coverage row + rewritten gap entry (residual: live-only orphans need sitemap crawl; kimi subpaths need per-path title+marker).
- `corpus/lessons/round-6.md`, `LOG.md` — full evidence trail.

## Residual gaps (next rounds)

- 5 sourceless kimi artifacts → extraction is operator-gated.
- Live-only orphan subpaths (file deleted from source stays served until redeploy) — needs sitemap/live-side crawl, not source walk.
- kimi subpath coverage — same blind spot, but byte compare meaningless (kimi rewrites bytes); needs per-path title+marker.
- kimi `apiv2` authenticated ops — recorded, intentionally unwired.
- Alerting on `violated[]` deltas vs silent log — undecided operator preference.
- Operator-actionable finding surfaced: `ds4cc-marketplace` is 20 commits ahead of `origin/main` — next `git push` will publish robots.txt/sitemap.xml/404.html/infinizoom bundle + ~120 byte deltas.
