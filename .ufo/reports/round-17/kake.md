# kake — round 17

- Axis move: **freshness — HOLD 10**
- Domain: web properties / publishing
- Lane commit: `72eb112` (`round-17`) — pushed to `VeigaPunk/kake-shokunin` `master`
- Main evidence: `kake-shokunin/LOG.md` round 17; `SCORECARD.md` row 17;
  `corpus/knowledge/freshness-sweep.md` §r17;
  `corpus/lessons/round-17.md`; `/tmp/kake-r17/`

## Axis-move

Freshness was tied with operability at 10. The planned standing sweep was run
first. It caught a real between-sweep world change before any prose repair:
lowercase `~/projects` had been consolidated into `~/Projects` and removed,
turning a previously resolving descendant report citation into an unannotated
miss. Critic verdict: **MOVE-ELIGIBLE — score holds at 10**. The live drift catch
is the freshness trigger; instrument hardening alone remains operability.

| Measure | Before (03:20:19Z) | After (final pass) |
|---|---:|---:|
| scanned files | 38 | 39 |
| absolute-path targets | 65 | 66 |
| resolving | 47 | 49 |
| declared absent | 10 | 10 |
| unannotated drift | **1** | **0** |
| miss set | 11 live / 9 pinned | 10 live = 10 pinned |
| file-set evaluator | inert (`pathsFiles: 38`, wrong type) | evaluated 39-entry list, `+0/-0` |
| `~/Projects` child visibility | none | 36-entry informational set, MATCH |
| malformed pins | silently degraded to defaults | fail closed, exit 2 |
| selftest | 9/9 | **10/10** |

The score does not exceed 10. The scorecard records a hold with demonstrated
live-drift detection and separately records stronger instrument integrity.

## Evidence

### L2 concurrency

A valid batched dispatch launched **9 L2s in one call**: planner; claim and pin
scouts; revenger; labrat; critic; connector; reviewer; scribe. A live-surface
scout also ran separately after the first attempted batch was rejected at
preflight for an invalid agent name. Route overrides visible in effective config
matched the mission map: planner/connector `@m_lunamax`; scout/scribe
`@m_flash`; reviewer/critic/revenger/labrat `@m_zfl`.

Artifacts: `/tmp/kake-r17/{planner.md,scout-claims.md,claims-delta.tsv,
scout-pins.md,scout-live.md,revenger-w6.md,labrat-timers.md,critic.md,
connector.md,reviewer-cites.md,reviewer-final.md,scribe-draft.md}`.

### Complete claim-class re-verification

The r16 inventory was re-run read-only:

- 117/117 standing HOLD claims re-confirmed.
- 15/15 r16 stale repairs still match live state.
- 7 UNVERIFIABLE claims carried honestly; 21 dated HISTORICAL-OK claims retained.
- 16/16 newly introduced r16/r17 claims HOLD.
- 9 new deltas found and repaired or qualified in the same commit:
  W6 path/inode/mtime and `magga-2`→`magga`; ETag edge flip; the r17
  38/380 and 38-file self-stale literals; wrong inode wording; nonexistent
  `corpus/claims`; unnamed charter-scribe ledger locus; README lesson-range
  gloss.

The ETag finding confirms the existing rule: r16 observed `6ab49127-1365d` in
7/7 same-round fetches; r17 observed `6ab49126-1365d` in 8/8. ETag is an
edge-unstable identifier; the content sha remains the freeze metric.

The real charter-scribe ledger is
`~/Projects/origin-work/ufo-fsd-alpha/.ufo/charter-scribe/ledger.jsonl`: 28 rows,
newest `2026-09-29T00:06:19.897Z`, `pushed:true`.

### Instrument hardening

1. `projectsChildrenSet` records 36 direct `~/Projects` children and prints
   removals/additions. Informational, never blanket-gating: operator churn is
   not automatically property failure. A future required web root should enter
   a separately gated protected set.
2. `pathsFiles` changed from a bare count (`38`) to the real 39-file list.
   `Array.isArray` had made the old pin inert-by-type.
3. A present-but-invalid pins file now exits 2 instead of degrading to defaults
   with every gate inert. Permanent malformed-pins fixture added.
4. A5's six consumed plazir pins no longer appear under `pins._unused`; only
   genuinely unevaluated pins remain in that header.
5. Old citation drift found by final review was repaired:
   round-1 audit rows and the `SKILL.md` operator-push rule.

### Final verification

| Check | Observed |
|---|---|
| `node scripts/freshness-sweep.mjs --offline` | exit 0; 39 files / 160 occurrences / 66 targets / 49 resolve / 10 declared-absent / 0 drift / 7 unresolved; file `+0/-0`; children 36 MATCH; history MATCH |
| `node scripts/freshness-sweep.mjs` | exit 1 **only** for expected `plazir-live-source-gap` |
| `node scripts/freshness-sweep.mjs --selftest` | **10/10 passed**, including malformed pins → exit 2 |
| state sentinel | all 33 `~/Projects/webzites/state/` sha256 rows byte-identical before/after |
| final reviewer | PASS; final literals reproduced live; residual numeric and old line-pin nits fixed before commit |
| LSP | no JavaScript language server installed; runtime/selftest supplied syntax and behavior proof |

## Armed watches

| Watch | Final state | Evidence |
|---|---|---|
| PQ-12 charter marker | `PERSIST` | config `2026-09-26`; live `2026-09-29`; GHP 200 / 53,386B / `fb365e38…` |
| PQ-5 kimi dead slot | `PENDING` | 404 / 13,409B / `93ddca9a…`; E1 never fired |
| PQ-2 ds4cc push | `GATE-CLOSED` | remote `e6bd071`; HEAD `f3d2ecd`; 20 unpushed; sitemap+robots 404 / 9,379B |
| PQ-14 plazir15 GHP | `GATE-CLOSED + LIVE-SOURCE-GAP` | remote `bd02d10`; HEAD `c814526`; 5 unpushed; live/source sitemap 8/7 |
| PQ-3 prerequisite | clear | `origin-work/charter-ufo-fsd` `main...origin/main`, HEAD `9c28d29`; no fetch/pull |
| probe history | MATCH | 78 rows / 67 full / 11 spot; 6 events / 0 phantom; last ENTER lucario |
| keeper timer | still inert | disabled/inactive; empty LastTriggerUSec; keeper reports frozen 2026-09-21 |

The next scheduled probe is 06:00:59Z; row 79 had not landed by final
verification. No history floor was speculatively re-pinned.

## Drift ledger

W6 is now sourceable cleanup rather than an unexplained deletion:

- r16: `~/Projects` inode 27238; lowercase `~/projects` inode 101125103.
- r17: capital inode remains 27238; lowercase path absent.
- `~/DIRMAP.md:1,7,27` records that lowercase children were absorbed into the
  existing capital root, then `~/projects` was removed.
- Parent mtimes narrow the transition to 03:13:18–03:14:07Z.
- `magga-2`→`magga` also moved in-window.
- The cited report survived at
  `~/Projects/shokunin/.ufo/reports/round-1/web-properties-publishing.md`.

This is the sixth mutation instant in the broader W1–W5 cleanup/prune regime,
but it preserved the cited artifact. Exact command and actor remain unproven.

## Sibling / hazard

- No sibling's latest report independently reported W6.
- Kake has zero citations into kasegi's lost groknight descendants.
- Kagi r16 cites a line range in kake's round-1 audit that shifted after the W6
  note insertion; report to kagi/integrator, do not edit the sibling lane.
- `origin-work/*` remains read-only for this lane: no fetch/pull performed.
- No L0 answer arrived for keeper enable-vs-retire or the earlier prune reports.

## L0

Updated `.ufo/l0-questions.md` with a corrected W6 corroboration line:
children absorbed, capital inode unchanged, cited report preserved, exact
command/actor unproven. No new operator decision requested.

## Operator relay — effective fallback config

Read effective `cfg://` after the in-round operator relay:

- `modelRoles.m_swe = "devin/swe-2:max"` — visible.
- `retry.fallbackChains.m_swe = null` — visible.
- Therefore the requested exact/final-only chain
  `m_swe → openai-codex/gpt-daybreak-blue-latest:max` is **not visible in the
  effective config**.
- Daybreak is assigned to other roles (`slow`, `plan`, `advisor`, `deduper`),
  but that does not establish it as m_swe's fallback.
- No genuine m_swe capacity failure occurred, so advancement to Daybreak was
  not observed. No failure was forced; no config or frozen mission contract was
  changed.

## Next

1. Run the standing sweep first. Exit 1 is expected only while PQ-14 remains
   `GATE-CLOSED + LIVE-SOURCE-GAP`; any second reason is new drift.
2. Re-run the 160-claim prose recipes; repair and re-pin in the same commit.
3. After 06:00:59Z, inspect row 79 and `probe-delta`; re-pin history floors only
   after the row exists.
4. Continue PQ-12/PQ-5/PQ-2/PQ-14/PQ-3 watches.
5. Observe — never force — any genuine m_swe capacity failure and record whether
   runtime advances to Daybreak.
