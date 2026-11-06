# kama — round 88 report (fresh start)

L1 `KamaR88`, attempt 1. Lane `kama-shokunin`, branch `master`. Base `9b4c7af16fdd4bba9e4815f4615f4b003f340747`,
freeze `fb76e7f26d6582bd087935a00f8dc43af4db912f`, measured commit `138a75437bcd11b72446087e970f5dfc5abf9ccd`,
final lane tip `64eaf5969e11e8955636dfb52c13eb089f731d9a` (`git ls-remote origin refs/heads/master` prints this hash).

## Work performed

Declared claims (frozen in `plans/round-88-claims.md` at `fb76e7f2`; two claims, distinct axes, no exploratory claim):

- **C1 — operability (capability `router-mode-readiness`, sourced S581):** `tools/kama-probe.sh` grades llama.cpp
  router-mode `/v1/models` entries by their `status` object instead of grading any listed id `MODEL_OK`.
- **C2 — calibration (lowest assigned axis, 7):** SCORECARD self-description vs repo state, counted by the unedited
  round-42 reconciler and the round-69 newest-closure counter.

Work items:

- Fresh-start reads before declaring: round-85/86/87 verifier spotchecks (all `rejected-honest-stop`), r83 closure
  (`rejected-harmed`); the r83–r87 rendered-cell calibration line is dropped, not re-frozen (`corpus/lessons/round-88.md` M1, Gate row 4).
- Protocol re-read (r87 R9): `MISSION.md`, `AXES.md`, `LEARNING.md`, `CORPUS.md` §SOURCES, `skill://swarm`, lane SCORECARD/PROVINCE/SKILL (`corpus/lessons/round-88.md:6-7`).
- Real domain discovery: the base probe printed `MODEL_OK matched` for a model a lane-owned pinned b11755 router reports `unloaded` and refuses with
  `400 model is not loaded` (`.ufo/waves/round-88/controls/c1-base.out` L01/L03; `.ufo/waves/round-88/measured/router-lifecycle.out`),
  and for the operator's live router at 127.0.0.1:1234 (GET only; `controls/pilot-live-1234.out`).
- Do-nothing and forgery controls executed and committed **before** freeze (`fb76e7f2`): C1 base `mismatches=11`, F1 always-unloaded `8`,
  F2 any-loaded `4` (`controls/c1-{base,f1,f2}.out`); C2 base `mismatches=4`, newest-closure `STALE_CALIBRATION`, pointer-only partial
  control still `mismatches=4` (`controls/c2-{base,newest-base,pointer-only}.out`); harm baselines (`controls/harm-base-*.out`).
- C1 implementation `68ab526e` (`tools/kama-probe.sh` `router_entries`/`router_refine`, `MODEL_UNLOADED` in VOCAB, listeners, baseline whitelist;
  `tools/round79-unregistered-census.py` vocabulary consumer).
- C2 work `138a7543`: duplicated live calibration row moved verbatim to `SCORECARD.md` §Axes "Superseded calibration rows"; live row re-pointed to
  round-87 closure; canonical capability list as of round 88 (55 rows); SKILL/PROVINCE hashes re-anchored.
- Prerequisite restore (not a claim): pinned fixture model absent on this host → `round78-live-reconcile --selftest` `pass=0 fail=4`
  (`controls/r78-selftest-before.out`); new `tools/fetch-pinned-model.py` restored it at sha256 `270cba1b…` (`controls/fetch.out`) → `pass=4 fail=0`
  (`controls/r78-selftest-after-fetch.out`); gate arm `round78-instruments` red → ok.
- Wave 1 (12 seats) attacked both claims. **CR01 (and independently SC01) found harm in the frozen C1 rule**: `sleeping` and default-autoload
  `unloaded` were graded `MODEL_UNLOADED` drift while the round's own completion oracle answered 200 (`repair/oracle-cells-M.out` mismatches=2;
  base got both right, `repair/oracle-cells-B.out`). Repaired at `8b5bb69d` (`router-sleeping`, `router-unloaded-autoload` via bare `GET /props`
  `models_autoload`), `repair/oracle-cells-repair.out` `ORACLE_CELLS cells=3 mismatches=0`. The frozen counter is not edited.
- Other wave fixes at `eb664062`: newline-in-id false drift (RV01), fetcher `.part` symlink clobber and digest→rename TOCTOU (SN01;
  `repair/fetch-hardening.out`), knowledge admission reason corrected to cite prior art (CN01; M4), unreceipted rows receipted (RV02;
  `repair/pilot-live-1234-after.out`, `measured/router-lifecycle.out`), round79 registered command re-run B vs tip identical
  (`repair/round79-census-B-vs-tip.out`).
- Frontier step: S581 admitted, S582 rejected (source-level reject, r87 R7); knowledge entry `corpus/knowledge/router-mode-readiness.md`;
  QUALITY KQ141–KQ143; README round-88 coverage/frontier; lesson `corpus/lessons/round-88.md` (M1–M5, wave and r87 dispositions).

## Landed changes

All commits by `kama-shokunin <kama@shokunin.local>` via `jj-lane.sh`, each tied to `LOG.md` §"Round 88":

| Commit | Content | LOG.md |
|---|---|---|
| `fb76e7f26d6582bd087935a00f8dc43af4db912f` | freeze: plan, `tools/round88-router-cells.py`, `tools/fetch-pinned-model.py`, controls | Round 88 intro + C1/C2 bullets |
| `68ab526ee64795e52afd8c34ec7252e36d0a42e2` | C1 implementation (`tools/kama-probe.sh`, round79 census vocabulary) | C1 bullet |
| `138a75437bcd11b72446087e970f5dfc5abf9ccd` | C2 SCORECARD; knowledge entry; S581/S582; SKILL/PROVINCE; lesson; LOG (measured commit) | C2, knowledge bullets |
| `f77d2ae9f2797a19e7548989fb9e64d8f9411d3f` | measured receipts at `138a7543` | C1 bullet ("Measured result") |
| `8b5bb69df0f7cd7302db2964354f5d7a0ba8f4b7` | C1 harm repair + oracle-cell receipts | Wave 1 bullet |
| `eb6640622a1d9c2d61f84669ee0466ec54aa728f` | wave integration: newline-id fix, fetcher hardening, corpus corrections, KQ141–143, README, SCORECARD measured subsection | Wave 1 bullet |
| `f7be6d473b3538254b41e217ff32ca584093bcbc`, `12eedc6b7a5ca11c53fe520c7d40e4568fb19fa0` | wave-1 evidence (reports, out dirs, spec/dispatch/results) | Wave 1 bullet |
| `64eaf5969e11e8955636dfb52c13eb089f731d9a` | terminal gate + census-end receipts | — (receipts only) |

Inherited, not authored: operator commits `3f3846a1`, `cdc9a5f6` (`considerthese/2026-11-05.md`, `2026-11-06.md`) entered the branch during the round; not edited. No `lane-dead-no-report kama round=88` line in the watchdog log; no inherited round-88 leftovers.

## Before → after measurements

**C1 (operability)** — `python3 tools/round88-router-cells.py --repo . --rev <R> --work <scratch>`:

| Revision | Output | Receipt |
|---|---|---|
| base `9b4c7af1` | `ROUTER_CELLS cells=17 mismatches=11 canned=14 live=3 probe=rev`, exit 1 | `controls/c1-base.out` |
| measured `138a7543` | `ROUTER_CELLS cells=17 mismatches=0 canned=14 live=3 probe=rev`, exit 0; counter identical to freeze | `measured/c1.out` |
| tip (`8b5bb69d` onward) | `mismatches=2` (C05, C12: frozen expectations `sleeping → MODEL_UNLOADED`, falsified by the oracle) | `repair/c1-frozen-at-repair.out`, `measured/harm-tip.out` |

Oracle cells (repair receipt, `python3 .ufo/waves/round-88/repair/oracle-cells.py --repo . --rev <R> --work <scratch>`; live, completion = ground truth):
base `mismatches=1` (no-autoload unloaded graded OK), measured `138a7543` `mismatches=2` (sleeping, autoload-unloaded graded drift),
repair `8b5bb69d` `mismatches=0`. Harm conjunct (`tests/probe-verdicts/check.py`, `tools/test-snapshot.sh`): `tests=72 passes=72 failures=0`,
`RESULT pass=30 fail=0` at base, measured and tip (`controls/harm-base-*.out`, `measured/harm.out`, `measured/harm-tip.out`; EX01 20 checks identical B/M/T).

Author verdict: frozen predicate **met at `138a7543`**; the measured commit carried a harm on two router states (oracle-proven, found by the
wave), repaired in-round; the final tip harms nothing relative to base by the oracle and the harm suites. The frozen counter reads red (2) at
the tip by construction. This is a met-then-repaired claim, not a clean admission — **operator/closure rules**.

**C2 (calibration)** — `python3 tools/round42-selfdesc-reconcile.py --repo . --tip <R>` and
`python3 tools/round69-newest-closure-counter.py --repo . --rev <R> --since-round 63`:

| Revision | Output | Receipt |
|---|---|---|
| base `9b4c7af1` | `mismatches=4 met=False`; `STALE_CALIBRATION` exit 1 | `controls/c2-base.out`, `controls/c2-newest-base.out` |
| measured `138a7543` | `mismatches=0 met=True`; `NEWEST_CLOSURE … row_current=true` exit 0; instruments identical to base; both moved rows verbatim | `measured/c2.out` |
| tip `eb664062` | `mismatches=0 met=True`; newest-closure ok (re-run after integration) | gate `measured/gate-final.out` arms `selfdesc`, `newest-closure` ok |

Author verdict: **met**. Score held at 7.

Terminal gate at clean tip `12eedc6b`: `PRE_REPORT round=88 arms=14 failed=1 uncommitted=0` (only `round75-instruments`, carried r87 R4;
it was exit 2 could-not-evaluate at base) vs base `failed=5` (`measured/gate-final.out`).

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`.
Start: exit 0, `kama ok` (`controls/census-start.out`). End: exit 0, `kama ok`, non-W04 warnings only the pre-existing W01 S481 (`measured/census-end.out`).

- Rows 320 → 322 (tier A 305 → 307, B 11, C 4; mined 287 → 288, queued 8, rejected 25 → 26).
- Added: **S581** (A, docs, mined) llama.cpp server README @ `704366d7` (b11755), router mode / status object; **S582** (A, docs, rejected)
  same README @ master `954de248` — newer than the pinned binary; flip when the pinned build moves past b11755.
- Rows touched old→new: none (S581/S582 new).
- Sourced claim: C1 rests on S581 (`corpus/knowledge/router-mode-readiness.md` `source:` line).
- Frontier: router mode moves from "source reads only" (`corpus/README.md:1532`) to live-verified verdict rule; remaining frontier listed in
  `corpus/README.md` §"Coverage and frontier — round 88" (per-request `?autoload`, memory-margin eviction, other engines, harness).
- Mistake mined: `corpus/lessons/round-88.md` `## Mistakes` M1–M5 (M2 reaped fixture cache; M4/M5 from wave disagreements, criteria KQ143/KQ141).
- Assimilation: none (no `merge/kama/` theme this round). considerthese: none mined this round (`considerthese/2026-11-05.md`, `2026-11-06.md` arrived mid-round, unread for proposals).

## Trend verdicts

- **expansion: improved** — two capabilities admitted to `SCORECARD.md` (`router-mode-readiness`, `pinned-fixture-restore`; demonstrated by
  `measured/c1.out`, `repair/oracle-cells-repair.out`, `controls/fetch.out`). The knowledge entry is **not** counted as new ground (M4: prior art
  `served-identity-crosswalk.md:28`, `unregistered-listener-census.md`).
- **quality: improved** — the router `status` vocabulary held as source-only (S001, crosswalk:28; README:1532 "source reads only") re-verified live on
  b11755 children (`measured/router-lifecycle.out`: unloaded, loaded, sleeping observed). Disclosed: the new entry's first version over-claimed
  receipts (RV02) and was corrected in-round before closure.
- **discernment: improved** — one admit (S581) and one source-level reject (S582) on record; two wave disagreements (CN01 admission reason, CR01
  rule vs oracle) became lessons M4/M5 with grounded criteria KQ143/KQ141. Non-author agreement on admit/reject awaits the closure spot-check.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources → author assertion: `SKILL.md` §"Round-88 router-mode readiness" adds a 5-row decision table and the `400 model is not loaded` signature (S581); no named non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md → author assertion: `LOG.md` §Round 88 and `.ufo/waves/round-88/measured/router-lifecycle.out` (live pinned b11755 router: load, sleep, unload, real completions); no non-author mark.
- [~] Instructions executable by an agent without oral context → author assertion: `SKILL.md` §Round-88 gate/oracle commands; wave seats ran them unaided (`w1/CR01ClaimC1.md`, `w1/RV03CounterReview.md`), seats are the lane, not non-authors.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → author assertion: `PROVINCE.md` round-88 paragraph; `w1/CN01SiblingOverlap.md` found no contested scope (kengaku:57, kagi:43 corroborate); operator router observed GET-only.

## Round shape and seats

One v1 wave `w1`, 12 seats, validated under `scripts/hyaku/ufo-wave-policy.json` (band 8–16), dispatched by the orchestrator's inline handoff
(`w1.ready` → `w1.ready.dispatched`; `WAVE-DONE kama r88 w1: all 12 seats settled`). Roles: reviewer 3, critic 2, mutation-tester 1 (attack 6/12 = 50 %),
executor 2, scout 1, sentinel 1, connector 1, scribe 1. Dead seats: 0 (all 12 reports present; `w1-results.json`). Residual call: none. Round total: 12.
§3 planner seat held by the L1 (validator rejects `planner`). Routes per amendment 46 (`reviewer` @m_zfl, `scout` @m_mim, others @m_flash);
answering model per seat is not recorded in `w1-results.json` (r87 R11 carried).

## Mistakes (lesson `corpus/lessons/round-88.md` `## Mistakes`)

M1 five rounds on a self-referential calibration instrument · M2 reaped fixture cache turned a selftest red · M3 listing read as readiness ·
M4 "new ground" asserted without own-corpus sweep (captured by CN01; fix KQ143) · M5 frozen rule vs own oracle on sleeping/autoload (captured by
CR01/SC01; repaired `8b5bb69d`; KQ141). Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → only ` M .scratch/run15-state.json`
(orchestrator-owned); no seat misroots.

## Limits and open items

- Carried to round 89 (`SCORECARD.md` §Planned (round 89)): router-cells successor with held-out cells (MT01's 6 escapes, CR01 overfit table), SN01
  counter defects (oracle socket identity, SIGTERM leak, env faults exit 1), `tests/probe-verdicts/check.py` cannot grade `MODEL_UNLOADED` rows,
  `round75-instruments` `bad_rows=19` (r87 R4), MT02 battery (r87 R5), S580 `teaches` (r87 R10).
- L0 questions appended this round: none. Open from round 87: `round75-instruments` ruling (still red); `selfdesc` ruling — the arm is now green
  without any population change (C2), so that question may be closed by the operator.
- Tool installs: none. Scratch `/fast/scratch/hyaku/kama-r88` removed after landing; no lane-started llama-server children remain.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
