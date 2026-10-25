# kake-shokunin — round 7

Domain: web properties & publishing (ds4cc.com, kimi.page/pro mirrors, Pages deploys).
Commit: `83d08e4 round-7` in `kake-shokunin/`. Zero publishes, zero metered ops — fetches, config/probe reads, git state only.

## Gap closed

README's residual "live-only orphan paths (needs sitemap crawl, not source walk)" — closed with a baseline sweep **and** a proof the defect class can't exist on GHP.

## Evidence produced (live, 2026-09-28 ~20:20Z)

- **Sitemap sweep baseline: 103 `<loc>`s, 0 orphans, 0 dead listings, 0 listed-but-404.** ds4cc-com 93 locs read from the *staged, unpushed* `sitemap.xml` (live copy still 404 — deploy lag, local HEAD 20 ahead of `origin/main`); every listed path already serves 200, so the push lists only what's already there. plazir15-ghp 8 locs + charter-ghp 2 locs from live sitemaps — all healthy.
- **GHP live-only orphans are impossible by construction.** `ds4cc-marketplace/.github/workflows/pages.yml` and `plazir-15-site/.github/workflows/pages.yml` both run `upload-pages-artifact` over the repo root → `deploy-pages` ships a fresh full-tree artifact per push; no carryover. The served set ≡ `origin/main` tree, so round-6's origin/main comparison already covered this direction. The scary residual ("deleted file stays served") was disproved by reading the deploy mechanism, not enumerated.
- **`/`→`index.html` classifier edge** — membership check needs `rel`, `rel/index.html`, and root `index.html`; first pass false-flagged all three bare roots.
- **`probe-latest.json` 18:51Z re-verified** — `charter-ghp` marker FAIL on second consecutive probe: pin `2026-09-26 scribe beat` vs live literal `2026-09-28 scribe beat (the-scribe via local-fallback)`. Beat pins die ~daily while the daily scribe lands; the round-3 pin was extracted but never landed in `fleet.config.json` — keeper owns that file, recorded as publish-queue evidence, not edited. Standing dead rows unchanged (`plazir15`, `charter-ufo-fsd-kimi`, `lucario` 404s; `plazir27-kimi-pro` preview-404; `xsnapshot-app` armed NXDOMAIN). `lucario` config `status:"live"` still contradicted by live 404 — staleness lesson holding.

## Files

- `corpus/knowledge/sitemap-orphan-audit.md` — coverage matrix, impossibility proof, sweep procedure + classification table, baseline, marker day-2 churn, limits.
- `SKILL.md` — new "URL lists (sitemap)" row in drift-detection table; marker-repin bullet updated with two-consecutive-FAIL evidence and ~daily cadence.
- `corpus/README.md` — coverage row added; orphan gap rewritten as closed with residuals.
- `corpus/lessons/round-7.md`, `LOG.md` — full evidence trail.

## Residual gaps (next rounds)

- 5 sourceless kimi artifacts → extraction is operator-gated.
- kimi subpath coverage — per-path title+marker needed; update-verb bundle replacement makes live-only orphans unlikely but unverified.
- `charter-ghp` marker re-pin + `lucario` config-status fix are queued keeper edits (operator-gated file).
- kimi `apiv2` authenticated ops — recorded, intentionally unwired.
- Alerting on `violated[]` deltas vs silent log — undecided operator preference.
- Standing: `ds4cc-marketplace` 20 commits ahead of `origin/main`; next operator push ships robots.txt + 93-loc sitemap + 404.html + infinizoom bundle (all pre-verified live-consistent this round).
