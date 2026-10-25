# Round-1 findings — kake-shokunin (web properties & publishing)

Lane: web-properties-publishing. Commit: `cd5b381 round-1` in kake-shokunin.
Date: 2026-09-28. No deploys performed; publish stays operator-gated.

## What shipped in the child repo

- `SKILL.md` rewritten: property map, audit→source-fix→operator-gated-publish
  checklist, live-vs-source drift table, mirror pitfalls, cited paths.
- `corpus/` minted per `CORPUS.md`: `README.md` index, 4 `knowledge/` entries
  (fleet-registry, publish-channels, drift-detection, mirror-pitfalls),
  `lessons/round-1.md`. All entries cite file paths or observed output.
- `LOG.md` round-1 entry appended with evidence list.

## Key findings

1. **The real fleet lives in `~/Projects/webzites/`**, not the `~/Projects`
   shortlist. `fleet/fleet.config.json` tracks 20 rows; `webzites/repos/`
   holds ~40 clones. Task-brief grep (`site|ds4cc|ufofsd`) found only 4.
2. **Site repos found**: `ds4cc-marketplace` (ds4cc.com, GHP Actions on push;
   `CNAME`, `deploy-github-pages.sh` is setup-only; `render.yaml`+`apps-sdk`
   → app.ds4cc.com on Render), `plazir-15-site` (GHP project site),
   `origin-work/charter-ufo-fsd` (charter-ghp canonical), `lucario/site`.
   `ufofsdbeta` is the UFO-FSD runtime, not a site source;
   `ufofsdbeta-kimi-review` is a non-git snapshot — neither publishes.
3. **Publish surface split**: GHP rows publish by `git push origin main`;
   kimi rows (14 of 20) have no non-GUI channel — browser lane on CDP :9222
   (musketeer burner profile), `kimi-surface.mjs` verbs
   (`sync-check`/`kimi-map`/`update`/`recreate`/`rebuild`), metered fires, and
   the version-card Publish click is human. apiv2 `PublishApp` exists but is
   banned from fleet code.
4. **Drift detection works, byte-compare doesn't**: kimi rewrites bytes
   (sdk-seed.js, cfemail) → use title+marker+vintage. `200` ≠ live
   (kimi-pro preview-404 body). Freshness cannot be proven by digest.
5. **Observed stale/broken state** (2026-09-26 evidence):
   `ds4cc.kimi.page` ~18+ revs stale (PQ-2), `plazir27.kimi.page` stale vs
   charter-ghp (PQ-3), `plazir15.kimi.page` + `charter-ufo-fsd.kimi.page`
   404 dead slots (RECREATE), `plazir27.kimi.pro` preview-404.
6. **Copy trap**: `plazir-15-site/speedrun/` is a frozen 3-run copy of
   `ds4cc.com/speedrun/` (`rel=canonical` in its index.html) — edits belong
   in `ds4cc-marketplace/speedrun/`.

## Evidence paths

- `~/Projects/webzites/fleet/{fleet.config.json,fleet.dedupe-report.md,kimi-surface-ops.md}`
- `~/Projects/webzites/{bin/webzites.mjs,scripts/kimi-surface.mjs,src/probe.mjs}`
- `~/Projects/ds4cc-marketplace/.github/workflows/pages.yml`, `deploy-github-pages.sh`, `CNAME`, `render.yaml`
- `~/Projects/plazir-15-site/.github/workflows/pages.yml`, `speedrun/index.html`
- `~/Projects/ufofsdbeta/.ufo/prompts/wz{0,1}-*.md` (mission specs + ownership)

## Open items for the integrator / next round

- Operator-gated: ds4cc.kimi.page `update` fire + publish click; plazir15 /
  charter-ufo-fsd `recreate` fires + slug clicks.
- `probe.mjs` content-level assertions (marker-inside rot stays invisible).
- Marker re-pins required on every republish (beat-dated + UUID pins churn).

L2 routing note: no task subagents dispatched this round (scope was
read-synthesize-write); recorded fleet-local map, scout lanes → `m_flash`.
