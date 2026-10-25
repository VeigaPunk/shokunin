# Round-3 findings — kake-shokunin (web properties & publishing)

Lane: kake. Commit: `ddf40e2 round-3` in kake-shokunin. Date: 2026-09-28.
No deploys; publish stays operator-gated.

## Gap chosen

Round-1 corpus cited only 2026-09-26 webzites evidence — nothing
independently verified. Highest-value move: run the playbook's own probes
and let live state correct the record.

## Probes run (fresh, this round)

- `webzites probe --all` @ 18:51Z — 12 OK, **6 failing**: plazir15,
  charter-ufo-fsd-kimi, charter-ghp, plazir27-kimi-pro, xsnapshot-app
  (fetch failed), lucario.
- `kimi-surface.mjs sync-check` — ds4cc-kimi-mirror + burnerchrome-kimi
  in-sync (stale-content blind, expected); ufofsd-charter, plazir27-kimi-page,
  plazir27runs-on, plazir15, charter-ufo-fsd-kimi, lucario = drift.

## New findings (not in any prior report)

1. **`lucario` config row is wrong.** `fleet.config.json` says
   `live/maintained`, `lastChecked 2026-09-27`. Reality: `lucario.kimi.page`
   returns 404 and was **never published** (repo README: "first publish
   pending — gated"). Canonical = `https://veigapunk.github.io/lucario/`
   (live 200, Pyodide/SymPy client-side engine; Pages branch deploy from
   `site/` + `src/lucario/engine.py` — `.github/workflows/pages.yml`
   assembles `_site/`). Registry needs a row split; filed as publish-queue
   class item in corpus.
2. **`charter-ghp` marker churn confirmed live.** Pin `2026-09-26 scribe
   beat` went absent within 48h; live now carries `2026-09-28 scribe beat`
   (commit `61d0ce6` in origin-work/charter-ufo-fsd, deployed via branch
   Pages — no Actions workflow file). PQ-12's re-pin burden is real.
3. **Trust hierarchy encoded:** live probe > config `status`/`lastChecked`;
   `in-sync*` never implies freshness. Added to SKILL.md checklist step 1 +
   step 6 marker re-pin procedure (extract live literal → publish-queue fix
   via webzites keeper, never silent edit).

## Landed in child repo

- SKILL.md: property map re-dated 09-28 (lucario split into GHP canonical +
  unpublished kimi slot; plazir27 staleness 09-18 vs 09-28), trust-hierarchy
  note, re-pin procedure with grep recipe.
- corpus: `fleet-registry.md` freshness warning + corrected lucario row;
  `drift-detection.md` fresh-probe delta table; `lessons/round-3.md`;
  README gaps updated. `LOG.md` round-3 entry.

## Publish-queue additions for operator/keeper (not executed)

- Fix `lucario` fleet row: kimi.page slot never published (404);
  canonical = GHP. Either recreate the kimi slot or re-status the row.
- Re-pin `charter-ghp` `expect.marker` to `2026-09-28 scribe beat` (will
  churn again on next beat — consider a stable literal or scripted re-pin).
- Standing: ds4cc.kimi.page stale (PQ-2), plazir15/charter-ufo-fsd 404 slots
  (PQ-4/5), all still open.

L2 routing: none dispatched; single-author synthesis round.
