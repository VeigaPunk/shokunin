# kumitate — round 74 report

Lane: kumitate-shokunin · host: Linux plazir27 (the run-15 restored omp/jj host; rounds 70–73 ran on Windows) ·
base `3c369336218329e30248b5d69c41348c02658169` · scaffolding `c5bb8a31d6d1e32b260cdc87583c79b2715cf842` ·
plan Amendment 1 `50baaea0f7b4b6fa73bc477c7d9b08862a8c1870` (pre-data) ·
work rev `0d2185b3df5705fda8212177924e215d72a38147` · close rev `e6a6cd43afe523753212ca28ec61479bfccde6a6`
(lane branch master; `ls-remote origin refs/heads/master` = `e6a6cd43…` at filing).

## Work performed

Declared claims (2, distinct axes, both pre-registered round 73 and re-measured at open on this host):

- **C1 — operability (lowest non-retired axis) — capability acquisition `origin-pin-restore`, sourced on S223.**
  Re-establish the pinned immutable origin clone per the `kumitate-origin-pin-v1` contract and run the
  full proxy recompute on the restored host.
- **C2 — coverage:kimi-layer — declare the two drifted kimi-plane members**
  (`plugins/installed.json.bak-pre-shokunin`, `plugins/managed/kimi-shokunin`), uncensusable during the
  Windows rounds.

Work items (each with an evidence pointer):

- Frozen plan + open receipts: `.ufo/waves/round-74/plan.md` (predicates, kill rules, controls frozen
  before any data seat), `open/gates-open.txt` (C1 `SRC_NOT_A_DIR` exit 2; C2 `DRIFT (UNLISTED ×2)`
  exit 1), `open/proxy-open-src.txt` (`SRC_REV_MISMATCH`), `open/maps-open.txt` (readme-map DRIFT),
  `open/prereqs.txt` (pin rev present; upstream at `fb7157fc`), `open/checklists-BEFORE.txt` (29/33),
  `open/census-start.txt` (exit 0).
- Wave: one v1 wave, 10 seats + the L1 planner seat (orchestrator ruling 2026-10-19: the L1 holds the
  canonical planner seat; the validator rejects `planner` as a swarm role) — `w1-spec.json`,
  `w1-plan.json`, `w1-dispatch.json`, `w1.ready(.dispatched)`, `w1-results.json`, 10/10 seat reports
  under `w1/`, 0 dead seats; attack 3/10 by the wave-census gate taxonomy (30 %, ≥25 % met; 4/10 = 40 %
  counting the sentinel), connectors 1, executors 3, scribe 1, scout 1, reviewer 1, critic 1,
  mutation-tester 1, sentinel 1 (`close/wave-census.txt` → `WAVE_CENSUS: CLEAN`).
- C1 mechanism: pinned clone re-established verbatim per `.ufo/pins/origin.json` `recreate`
  (`--no-hardlinks`, detach checkout `31c465f15669…`, `chmod -R a-w`) — HEAD/a-w/clean verified
  (`build/K74ExecPinRestore/recreate-transcript.txt`, seat report `w1/K74ExecPinRestore.md`).
- C2 declaration: both members declared in `scripts/kimi-census.mjs` (MEMBERS/ENUMERABLE/FROZEN 27→29)
  and `scripts/proxy-check.mjs` `K_MEMBER_RULES` (+2 fixture cases), bound by `## ` sections in
  `corpus/knowledge/kimi-skills-plugins.md` (patch `build/K74ExecKimiMembers/K74ExecKimiMembers.patch`,
  apply-check clean; seat report `w1/K74ExecKimiMembers.md`).
- S223 opened this round by the scout seat: `corpus/SOURCES.md` row, capture pinned
  (`build/captures/git-clone.html`, sha256 `d31b6c9f…`, gate `SOURCE_CAPTURE: CLEAN captures=55`);
  C1's knowledge entry `corpus/knowledge/origin-pin-restore.md` cites it; man-page agreement verified.
- Routed repairs: readme-map inheritance (rows + covered entries for the r73 spotcheck file, the
  round-74 lesson and the new knowledge entry → `README_MAP: CLEAN files=179 rows=179 covered=179`);
  considerthese proposal 1 → `corpus/QUALITY.md` Q70; REPORT_RECEIPT self-reference dispositioned
  (receipt computed against final bytes, lane-side companion file, measurement point stated below).
- Attack results: reviewer `w1/K74ReviewFreeze.md` → FREEZE-FIX ×3, all landed pre-data as plan
  Amendment 1 (items 7/8/9) before any measurement; critic `w1/K74CriticClaims.md` → attacks A1/A3/A4/A5/A6
  PASS, its "decisive flaw" is the same pre-amendment trio; mutation seat 5/7 killed directly, 2
  "survivors" re-verified **killed** against the applied patch (`close/mutant-verify.txt` — the seat had
  tested its own hand-built declaration); sentinel 5/5 fail-closed arms held (`w1/K74LabratFailClosed.md`).
- Same-commit stanza re-measure authorized by Amendment 1 item 7 (A 687→821 from rounds 70–73 probe
  accrual while the proxy fail-closed on Windows; C2/C2_total 167→167→179/179 with the readme repair)
  and 3 gate-pin registrations (item 8: `pin.control-replay`, `pin.harm-matrix`, `pin.routed-ledger`,
  keyed in `GATE_PINS`) — `close/proxy-check.txt` default and `--strict` both `PROXY: MATCH` exit 0,
  zero warnings.

## Landed changes

All committed via `jj-lane.sh --as kumitate`; LOG.md round-74 entry carries the narrative.

- `0d2185b3df5705fda8212177924e215d72a38147` (work): C1 recreate + receipts; C2 member declarations +
  knowledge sections + selftest arms; stanza re-measure (`A=821 C2=179 C2_total=179 K_members=55
  K_sections=55`); re-pins `pin.kimi-census` → `73bea81c…`, `pin.proxy-check` → `aabf389e…`; 3 gate pins;
  S223 row + capture + `origin-pin-restore.md`; readme-map repair; QUALITY Q70; lesson round-74;
  wave evidence + close receipts. Blob identity verified at close
  (`close/blob-identity.txt`: committed blobs hash to the re-pinned pins).
- `e6a6cd43afe523753212ca28ec61479bfccde6a6` (close): SCORECARD round-74 section work-rev fill +
  blob-identity receipt.
- `close/wave-census.txt` receipt + `close/report-receipt.txt` (this report's hash, lane-side):
  committed in the follow-up receipt commit `receipts` (see Limits).

## Before → after measurements

**C1 (operability; capability `origin-pin-restore`).** Counting command (frozen, plan.md):
`node scripts/proxy-check.mjs; echo exit=$?` — before: `PROXY: FAIL-CLOSED (SRC_NOT_A_DIR) --src
/fast/scratch/hyaku/kumitate-pin/src is absent` exit 2 at `3c369336…` (`open/gates-open.txt`);
after: `PROXY: MATCH (A=821 C=33 operability=9; C1=19/19 C2=179/179 coverage=10; S=88/88
coverage:script-layer=10; R=92/92 coverage:runtime-layer=10; K=55/55 coverage:kimi-layer=10;
pins=6 match; src-rev=31c465f15669)` exit 0, and `node scripts/proxy-check.mjs --strict` →
`PROXY: MATCH` exit 0, measured at the work rev `0d2185b3…` (`close/proxy-check.txt`). Companion:
`git -C /fast/scratch/hyaku/kumitate-pin/src rev-parse HEAD` → `31c465f15669f744848bd9f5d56191c5085670f7`.

**C2 (coverage:kimi-layer).** Counting command (frozen, plan.md Amendment 1 item 9 shape):
`node scripts/kimi-census.mjs; echo exit=$?` — before: `KIMI_CENSUS: DRIFT (UNLISTED
plugins/installed.json.bak-pre-shokunin; UNLISTED plugins/managed/kimi-shokunin)` exit 1, members=53
at `3c369336…` (`open/gates-open.txt`); after: `KIMI_CENSUS: CLEAN (members=55 checked=55 chain=22
info=4)` exit 0 with `TOTALS: members=55 checked=55 errors=0 info=4 chain=22`, measured at the work
rev `0d2185b3…` (`close/kimi-census.txt`); selftests `KIMI_CENSUS_SELFTEST: 56/56 pass`
(`close/kimi-selftest.txt`), `PROXY_SELFTEST: 124/124 pass` (`close/proxy-selftest.txt`);
`node scripts/proxy-check.mjs --json` re-derives `K_members=55`, `K_sections=55`,
`coverage_kimi=10`. Kill-rule honesty: both members re-verified present on the live root by shape at
measure time; five census mutants killed + the two proxy survivors re-verified killed
(`close/mutant-verify.txt`); the declared move holds on the gate's own counting rule.

## Sources & frontier

`bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate` → exit 0 at
round start (`open/census-start.txt`, six carried W04) and round end (`close/census-end.txt`, exit 0,
same six W04). SOURCES rows **161 → 162** (`grep -cE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md`).
Rows added by tier: **A +1** (S223, git clone docs, scoped to local-path object hardlink semantics;
capture pinned, man-page agreement verified). Rows touched old→new: none (append-only; no
status/recheck/used-by edits to existing rows). Frontier rows advanced: none — S223 grounds the
lane's own instrument (the origin-pin contract), expansion credit is not claimed for it; frontier
bands unchanged. Assimilation (§10): **none this round** — the `merge/kumitate/` package (155 rows,
70 entries) is out of proportion to the two host-restore claims; flip (a dedicated assimilation
round) recorded in the round-74 lesson Gate. considerthese/2026-10-26.md proposal 1 mined into
QUALITY.md Q70. Mistake mined into `corpus/lessons/round-74.md ## Mistakes` (2 rows: stale-premise
host-predicate-less pre-registration; the spotcheck-coverage recurrence class). New routed red
pre-registered for round 75: `omp-census` DRIFT (39 findings, `open/checklists-BEFORE.txt`).

## Trend verdicts

- **expansion: unchanged** — no admitted `knowledge/` entry on uncovered frontier ground
  (`origin-pin-restore.md` governs the lane's own instrument; the K-layer declaration extends an
  already-covered family). SOURCES +1 grounds a claim, not new ground.
- **quality: improved** — the proxy recompute and both census layers run green end-to-end on the
  restored host for the first time since round 64; five fail-closed arms re-proved; five census
  mutants killed; the two mutation survivors re-verified killed against the applied patch with the
  receipt committed; every green receipt carries a committed transcript (Q70 discipline).
- **discernment: improved** — the pre-data freeze review caught three real defects (A-term re-measure
  authorization, `--strict` gate pins, predicate shape) and all three were fixed as a dated plan
  amendment BEFORE any measurement; the critic's "claims-broken" verdict was the same pre-amendment
  trio, recorded transparently rather than silently absorbed; the Windows-era stanza backlog (A/C2/
  pins) was receipted as maintenance, not hidden inside the claims; the new omp-plane drift is
  disclosed red and pre-registered, not silently skipped.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the gate
  registry + 33-item verifiable checklist are unchanged this round and now run 32/33 green on the
  restored host (`close/checklists-AFTER.txt`); the one red is the disclosed omp-plane drift. Verifier:
  pending non-author closure judge.
- [~] At least one end-to-end domain task executed and logged in LOG.md — C1 (pin restore + full
  proxy recompute) and C2 (member declaration + census green) are both end-to-end domain tasks,
  logged in LOG.md round 74 (`0d2185b3…`). Verifier: pending non-author closure judge.
- [~] Instructions executable by an agent without oral context — every checklist item names a command,
  an accepted exit set and an expected verdict substring; the round's own wave ran from the committed
  spec/dispatch alone. Verifier: pending non-author closure judge.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the connector seat scanned 20 siblings:
  zero overlap on all three round surfaces (kimi plugin plane, origin pin path, pin contract);
  adjacent findings reported, not absorbed (`w1/K74ConnectorOverlap.md`). Verifier: pending non-author
  closure judge.

## Limits

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **REPORT_RECEIPT measurement point:** this report's sha256 is computed against these final bytes,
  stored lane-side at `.ufo/waves/round-74/close/report-receipt.txt` (the file is not edited after
  the measurement; the r73 self-reference defect is thereby avoided).
- **omp-census carried red:** `OMP_CENSUS: DRIFT (entries=63 findings=39)` at open and close
  (checklist 32/33; the red item is SKILL.md:731) — a Windows-era + run-15 host-restore accrual on
  the OMP plane, pre-registered as a round-75 candidate, disclosed, not a claim.
- **Origin upstream drift:** local origin repo HEAD is `fb7157fc…` while the pin holds `31c465f1…`;
  the layer terms were re-verified at the pinned rev (unchanged); a future re-measure is
  pre-registered.
- **Critic/reviewer seat timing:** both attack seats analysed the pre-amendment plan; every finding
  they raised is either an Amendment-1 item (landed pre-data) or a PASS; the mutation seat's two
  "survivors" were re-verified killed against the applied patch (`close/mutant-verify.txt`).
- **Round-gate at filing:** `node scripts/round-gate.mjs --round 74` reads only
  `REPORT_MISSING` (`close/round-gate.txt`) — satisfied when this report lands; all other checks
  (SCORECARD row, LOG entry, round commit) green.
- **Tool installs/updates:** none this round (curl, sha256sum, git, node already installed; every
  seat reported no installs; pacman guard respected — no transactions attempted).
- **Open L0 questions:** none new this round (the round-42 R41-2 gate-pins ruling stays open with the
  operator; this round's three gate-pin registrations follow the block's existing purpose).
- Wave shape: one v1 wave (band 8–16), 10 seats, 0 dead seats, 10/10 reports, 0 residual calls;
  round total 11 seats including the L1 planner seat.
