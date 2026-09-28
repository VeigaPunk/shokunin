# kake-shokunin — round 9 report

**Gap closed:** two coupled residuals — (a) the publish queue (PQ-1..PQ-13)
existed only as dedupe-report prose with no per-item readiness mapping; (b)
README residual "JS-rendered link surfaces need rendered DOM" (false premise —
the vault surface is a static literal). Commit `ed0b632 round-9` in
`kake-shokunin/`. 10 read-only L2 probes dispatched in one batch; zero fires,
zero pushes to fleet sources, zero browser ops.

## Evidence (read-only HTTP + git/journal reads; key claims self-verified by L1)

- **PQ-5 = shortest path to green.** `charter-ufo-fsd-kimi` rebuild already
  produced verified version card `efc1830` (preview 8,323B, markerPresent,
  `liveAfter.stillDead`) — only the human Publish + slug click remains.
  Chat `1a0de32f-3f12-8611-8000-0907d06bd2f2` holds 2 unpublished versions.
- **Vault rot quantified without a browser.** `const PROPERTIES = [...]` is a
  static literal in the served body (self-verified: 13 entries, 10 URLs). 3/10
  live-claimed links dead: `charter-ufo-fsd.kimi.page` + `plazir15.kimi.page`
  → 404 (13,409B sentinel, sha `93ddca9a…` — same dead-slot hash across all
  slots), `plazir27.kimi.pro` → 302→preview-404. `lucario` absent from the
  array entirely. `fleet/vault-properties.json` (09-20) still matches live —
  drift is upstream claims, not page churn.
- **Sourceless rows: `sourceDir:null` is the single hard blocker** —
  `cmdUpdate` refuses `kimi-surface.mjs:483`, `cmdRecreate` refuses `:845-849`
  on any live-200 slot. Per-row extraction recipe landed
  (body→index.html→sourceDir→`update`; vault needs `recreate --new-chat
  --canonical=`; plazir27runson needs `--zip-exclude='assets/*.mp4'` vs the
  32MB `fetchLive` cap at `:339`; ufo-fsd.kimi.pro needs html+assets).
- **Chat-binding truth = `state/kimi-map.json` publishedUrl**, not hosts[]
  text. plazir15 binding is UNRESOLVED (vessel `1a0c2186` pristine vs emergent
  `1a0de2ed` 1 unpublished version) — resolve before any refire; last recreate
  consumed a fire (code 6 post-`fired`). lucario: no bound chat, zero consumed
  fires (3× lease-refusal code 1).
- **25 unpushed source commits** = GHP publish bottleneck: ds4cc-marketplace
  +20 (incl. sitemap `f3d2ecd` = **75** new locs — "74" in older docs is off
  by one; the cited 477-line revenger diff has no on-disk artifact),
  plazir-15-site +5, charter *behind* 2 (pull first). Render `app.ds4cc.com`
  healthy: `/` 200 (801B), `/mcp` 400-correct on sessionless GET.
- **Platform shifts since 09-26:** `sdk-seed.js` tag grew exactly +157B on
  every kimi row (post-publish digests MUST normalize; bytes carry no
  freshness); website-id `1a0acf59…` serves on BOTH ufo-fsd.kimi.pro AND
  .kimi.page — config's "fleet-unique 1/17" note is stale (2/18).
- **Fleet state unchanged:** probe-latest 18:51Z = 12 ok / 5 violated / 1
  error, all FAILs match known-stale markers or documented dead slots — 0 new.

## Keeper handoffs (prepared, not applied — operator owns)

- `fleet.config.json:256` charter-ghp pin `2026-09-26`→`2026-09-28 scribe
  beat` — ready diff in `webzites/reports/r9-stale-markers.md`.
- `ufo-fsd-kimi-pro` marker re-pin (id collision) + `plazir27runson` marker
  case `Nightcall`→`NIGHTCALL` (passes today only via title regex).
- plazir15 chat-binding resolution before refire.

## Cross-lane note (reported, not absorbed)

Shared burner-chrome lease (CDP 9222) ownership between kake and kagi lanes
is unresolved — kagi corpus flags it; needs orchestrator decision.

## Files landed

- `corpus/knowledge/publish-queue.md` — PQ-1..13 readiness ledger: gate
  class, bound chats, source freshness, ordering DAG (PQ-3→PQ-12,
  PQ-8→PQ-13), cheapest wins.
- `corpus/knowledge/vault-properties.md` — no-DOM audit method, rot baseline,
  extraction recipes, +157B seed shift, site-id collision.
- `corpus/lessons/round-9.md`; SKILL.md (drift-table vault row, PATH fix,
  dead-slot readiness, 4 new pitfalls); corpus README + ops-automation +
  kimi-subpath-audit corrections; LOG.md round-9 entry.

## L2 dispatch

10 subagents one batch (scout/labrat×3/scribe/sentinel/connector/reviewer/
planner): evidence reports under `~/Projects/webzites/reports/`
(`r9-publish-queue.md`, `r9-stale-markers.md`,
`dead-slot-recreate-readiness-r9.md`, `sentinel-sourceless-extract-r9.md`).
