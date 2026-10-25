# tabi — round 25 (2026-10-25, hyaku run 6; attempt 1)

## Summary

Two frozen-before-data claims landed and measured clean at the measurement commit
`3e213bea7363a2aad3f92af86afb3a95699cf9a7` and are re-run green at the lane tip
`8769b2e06119ac9d58ea57ddf66cfa476608ace2` (ls-remote confirms remote = local).
C1 (depth) observes a real bfcache restore on loopback — closes round-24 U1
(docs-held → runtime-held on this host). C2 (freshness) re-opens six on-release
rows with fresh fetches. Two new gates ship (eight-field registry rows; selftests
17/17 and 18/18). No scalar axis promoted. Assimilation: none (candidate refused
with reasons).

## Work

- **C1 — bfcache runtime observation (depth).** Loopback journey probe A→B→A
  with the CDP history primitive `Page.navigateToHistoryEntry` (the frozen claim's
  `Page.goBack` wording was amended pre-data: the method does not exist on this
  build — observed -32601 in four runs; revision in `claims.json`). Positive run:
  one `Page.frameNavigated` BackForwardCacheRestore on A's original loaderId,
  history-index drop 2→1, `pageshow.persisted`, surviving JS state
  (`window.__counter` 42→42, same nonce), zero network requests back to A, no
  `Page.backForwardCacheNotUsed`. Negative controls both 0 restores: no-history
  step; `--disable-back-forward-cache`. Evidence pointer:
  `corpus/evidence/round-25/bfcache/receipt.json` (sha256 `250767649fa1…`),
  `events.jsonl`, `controls.json`, screenshots `1-a.png/2-b.png/3-a-back.png`.
- **C2 — on-release source re-verification (freshness).** Six on-release rows
  (S013/S015/S016/S020/S023/S024) fetched fresh 2026-10-25 (HTTP 200); held
  quotes located exactly once each in today's bytes; 0 supersessions; S020 anchor
  drift recorded per round-18 precedent. Evidence pointer:
  `corpus/evidence/round-25/freshness/reopened.json` (sha256 `609ab7c4eb36…`)
  + committed byte files `S0{13,15,16,20,23,24}.html`.
- **Counters.** `scripts/check-bfcache-receipt.mjs` (selftest cases=17/17),
  `scripts/check-source-reopen-receipt.mjs` (cases=18/18); registry rows in
  `SKILL.md` §"Round 25"; `check-gate-registry` nonconformant=0 at tip (25 rows).
- **Mistakes mined (lesson).** M1: round-24 receipt-pinned measurement revision
  `4722dbaf8efc…` vs the report's cited commit `8bc1d32…` (reference-drift;
  fix: receipts record the exact measured rev, the report cites the same hash —
  QUALITY 66; red fixture fails `check-measurement-binding.mjs`). M2: harness
  liveness bug (Node exit 13 awaiting a finish signal; fixed within the seat;
  red before/green after recorded).
- **Frontier step.** S106 opened this round (Chromium 154 `content_features.cc`
  BackForwardCache `FEATURE_ENABLED_BY_DEFAULT`); S104/S105 re-opened; search-log
  appended; one mined mistake per above.

## Changes → LOG tie

All lane changes are append-only: `SCORECARD.md` round-25 declared/executed/
capability/waves blocks; `LOG.md` round-25 entry (claims, measured values,
next-iterations); `corpus/README.md` round-25 frontier rows; `SKILL.md` round-25
gate section; `corpus/QUALITY.md` criterion 66; `corpus/SOURCES.md` S106 + search
log; knowledge entries `bfcache-runtime-observed-round-25.md` and
`source-recheck-round-25.md`; lesson `corpus/lessons/round-25.md`. LOG entry
carries the measured numbers and next-iterations (b–e).

## Cross-domain

Connector sweep (W1 `ConnSiblings`): no sibling holds a bfcache restore
observation or a `chrome-devtools-mcp` row; none of the six C2 URLs appear in any
sibling registry. Kotoba's omp strings bundle driver code branching on
`BackForwardCacheRestore` with `Page.getNavigationHistory` + `navigateToHistoryEntry`
(static code, adjacency only — refused-route via `corpus/adjacency.tsv` row 2).
No sibling writes; no overlaps absorbed.

## Sources & frontier

Rows 105 → 106 (S106 opened 2026-10-25; quote located at decoded lines 186–187).
Census before → after, same command:
`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`
→ exit 0 at baseline `9e136667` and exit 0 at tip `8769b2e0` (rows 105 → 106;
same W04 known duplicate-URL warnings). Frontier: bfcache surface runtime-held on
this host; on-release source freshness held; two new gates held.

## Assimilation

None. Candidate `webmcp-devtools-agent-surface-r25.md` (staged S242) refused: its
tool-behavior claims (what `list_webmcp_tools`/`execute_webmcp_tool` do) are not
supported by the current en/zh-TW DevTools bytes, and its staged row carries an
unscannable 14-column cell. Refusal recorded in the lesson Gate with flip
condition. Quarantine slice (38 tabi rows, round 22) stays closed; verdicts
carried. Collision guard proven: staged S102–S106 vs lane S001–S106, intersection
S102–S106 (by-document; no staged row adopted).

## Waves

W1: 34 seats, all 34 reports landed — 9 scout, 7 executor, 5 scribe, 4 reviewer,
4 critic, 1 connector, 1 revenger, 2 mutation-tester, 1 simplifier, 1 sentinel.
Spec validated under v1 policy (32–64 band); dispatch payload byte-identical
under v1 re-validation. W2 (falsify): spec generated and v1-validated (34 items)
but **NOT dispatched** — the session budget forced wrap-up before dispatch;
falsification coverage instead comes from W1 adversarial seats plus the gates'
own mutation-matrix selftests. `planner` held by L1; `labrat`/`distiller` ride
executor/reviewer seats.

## Trend verdicts

- depth: frontier entry added (runtime observation); no scalar change → **improved**
- freshness: on-release verification practice extended; no scalar change → **improved**
- operability: two new gates added (capabilities); no scalar change → **improved**
- coverage, calibration, adjacency: unchanged; no harm observed (pure appends)

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Approval table (`:697`), §Evidence ladder, §Runbook, `:1598-1617` kaika decision rows; prior `[x]` named lane-dispatched TABI-B4/TABI-R3-4 — not non-author (orchestrator ruling, kaika round 1) — **unchanged this round; gate section appended (`:2480` onward)**
- [~] At least one end-to-end domain task executed and logged in LOG.md — `corpus/knowledge/multi-step-journey.md` §1–§2, §7 (4-page loopback journey, 2 cold runs byte-identical); logged in `LOG.md` round-3 entry — **unchanged; this round adds the bfcache journey receipt (C1) logged in `LOG.md` round-25 entry**
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/executor-test-sufficiency.md` §0, §4 (verdict SUFFICIENT; the executor was a lane-dispatched seat) — **unchanged**
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:3-19`; refusal routes revenger/kaidoku/kake/kagi held (`corpus/evidence/user-20261015-r02/boundary/refusal-receipt.txt`) — **unchanged; connector sweep confirms no overlap absorbed**

## Carried items

(b) extend calibration m1 window to non-revision-bound LOG.md entries (LOG.md:1664
still reads twelve); (c) decide adjacency-map row kind cell; (d) re-run C1 journey
probe at the next browser bump and characterize restore rate under load; (e) headed
mode / cross-origin A→B→A probes. Routed observation: require
`cdpMethod="Page.navigateToHistoryEntry"` in the goBack step with a selftest
mutation (currently enforced via `history_result.ok` + index-drop checks; noted
for next round).
