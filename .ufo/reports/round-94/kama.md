# kama — round 94 (attempt 2) report

Lane repo `/home/vgpnk/Projects/shokunin/kama-shokunin` (jj-colocated, branch `master`; lane tip at filing `32f8e347604856a8f2a3cbf73c54592c926b0bf4`, pushed — `git ls-remote origin refs/heads/master` matches).
Round base `e6f1dcce`; freeze `285f17832d0e26364366bbf19888d68f1838249b`; C1 measured
`a27656a454b1a2364f8b6e55f42fbca8c2e86ee4`; C2/C3 measured `6aa5fa6bd9bbf44c4b2ca3f1e2158e7d5aa92623`.
Declared claims (3, frozen in `plans/round-94-claims.md`, narrowed post-freeze in
`plans/round-94-amendment-1.md`): **C1 operability** — a per-file GGUF parse budget for the router file-state verdict (**not verified**:
predicate met on the frozen 19 cells, wording falsified by three seats; honest stop with the narrowing
as its deliverable);
**C2 depth** — every b12177 port/slot setter named per entry point, config.ini route included (**not
verified**: K2 fired); **C3 calibration** — the round's own census + lesson self-check (verified after
a one-token repair).

Attempt 1 (23:01–23:35) inherited: its three claim commits (`285f1783`, `a27656a4`, `6aa5fa6b`), the
13-seat wave spec/dispatch, `measured/c1.out`, `measured/c2.out`, and the lesson. All were re-verified
this attempt (both counters re-run against their measured revisions) and reused; nothing inherited was
discarded. Attempt 1 wrote `w1.ready` with L1 `KamaR94` and ended before a report; this attempt
rewrote the ready file with L1 `KamaR94a2` and the orchestrator dispatched it at 23:42:06.

## Work performed

- **C1 (operability, not verified — honest stop).** The inherited claim work — `tools/kama-probe.sh` `ROUTER_PY` gives
  every GGUF candidate its own 15.0 s wall slice reset inside `gguf_parse` (replacing the shared
  `DEADLINE = monotonic()+4.0`) and the `router_file_states` wrapper goes `timeout 8` → `timeout 60`
  (`tools/kama-probe.sh` at `a27656a4`), plus the frozen 19-cell two-load counter
  `tools/round94-router-budget.py` (`measured/c1.out`: `cells=19 mismatches=0 positive_mismatches=0
  load_cells=19 load_stable=1 probe=rev probe_sha256=27065a5c… rev=a27656a4 load1_nat=232.08
  burners=96`, exit 0). Re-measured this attempt at M1: `cells=19 mismatches=0 positive_mismatches=0
  load_cells=19 load_stable=1 … load1_nat=141.70 burners=32`, exit 0. Do-nothing control re-measured
  this attempt at base `e6f1dcce`: `cells=19 mismatches=3 positive_mismatches=0 load_cells=19
  load_stable=0 … load1_nat=197.96`, exit 0 (R04 and T01 flip) — receipt
  `.ufo/waves/round-94/controls/c1-base.out`; the counter's sanity gate then failed on later attempts
  at the same revision (exit 2, see C1 caveat below; receipt `controls/c1-base-load.out`).
- **C1 caveat, reproduced by the L1 (`w1/SC02BudgetSweep.md` F1–F4).** On this host the counter is
  frequently **unevaluable**: its sanity gate asks the round-93 base probe (shared 4.0 s deadline,
  `BASE = 5af79495`) to classify the counter's own 150 000-tensor fixture, and under load that loader
  answers `-`, so the counter exits 2 before any cell. Measured this attempt: two M1 runs at
  `--burners 32` passed (one saved above), a third M1 run at the default 96 burners and two base runs
  (32 and 8 burners) exited 2 with `could-not-evaluate: fixture slow.gguf: base loader state '-'`
  (`controls/c1-base.out`, `controls/c1-base-load.out`); SC02 measured 6/10 exit 2. SC02 F2/F3/F4
  further show the *wording* is wider than the instrument: a 400 000-tensor invalid file still flips
  `invalid`/undecided across the 15 s slice under load, a listing of ≥~40 distinct slow files
  truncates against `timeout 60` and grades `MODEL_OK` where `timeout 600` grades
  `MODEL_UNLOADED`, and a `/props` slower than 5 s grades `MODEL_UNLOADED`. All four are routed; the
  claim is narrowed in `plans/round-94-amendment-1.md` and filed as an honest stop, not an admission.
- **C1 corroboration on the live binary.** `w1/EX02LiveRouterBudget.md`: a lane-owned b12177 router
  child (13-entry preset, 32 burners) — base `--expect '*'` false-greens `MODEL_OK` for 8 distinct
  slow invalid files while the router oracle answers 500 (2/2 reps); M1 stays `MODEL_UNLOADED`
  (2/2). `w1/EX01HeldOutBudget.md`: N = 2…256 distinct slow files — per-file budget fixes starvation
  to N = 16, and the probe's 60 s wrapper ceiling is at N ≈ 21–24 (the disclosed limit).
  `w1/RV01ProbeDiff.md`: the C1 diff changes nothing else (single-candidate states, arg forms,
  identity memo, undecidable-loadable semantics identical to base).
- **C1 mutation test (`w1/MT01ProbeMutants.md`, settled seat, handle lost then returned).** 14 single-point mutants of the M1
  probe through the frozen counter: 7 killed, 7 survived; four survivors are coverage gaps with
  separating inputs (per-invocation budget M02 — the plan's F1 control is therefore **false**, that
  shape is green at load1 323; ctime-less memo key M12; count overflow M14; 60 s wrapper M10), and
  M04/M05/M11 are measured equivalents (the MAX_STEPS and wall bounds cross within ±10 %). Same seat:
  the plan's "20 s cell budget" is 30 s, K1 as worded is narrower than the counter's exit condition
  (`mismatches>0` also exits 1), and `round89-unloadable-cells.py` needs `LLAMA_CACHE`/`HF_HOME`
  pointed at an empty dir after another seat's cache-sourced router model appeared at 00:11.
- **C1 forgery battery (`w1/CR01BudgetCounter.md`).** 11 hand-broken probes run through the frozen
  counter: F1 basename memo, F2 path-string memo, F4a/F4b MAX_STEPS 900k/500k, F5 wrapper 8 and F9
  basename+size memo are caught; **F3 shared deadline, F6 no-inode memo, F7 NO_OPEN, F8 wrapper 30
  score `mismatches=0 positive_mismatches=0 load_stable=1`** while misgrading real listings —
  collected in `controls/c1-forgeries.out` and routed to round 95.
- **C2 (depth, not verified).** Inherited work — `SKILL.md` §Listen port and slot-count setters
  (round 94 revision): P01–P92 (one row per population line of the pinned b12177 archive, with the
  config.ini route and an Entry cell) and decisions R18/R19 superseding R16/R17, bound by
  `tools/round94-setter-sweep.py` (`measured/c2.out`: `SETTER_SWEEP 92 92 2 92 0 0 0 0
  derived_checked=47 derived_disagree=0 decisions=2/2 pop=92 met=True`, exit 0; re-run this attempt at
  M2 and at the new tip: identical, exit 0; base re-run `92 0 0 0 0 92 0 0 … met=False`, exit 1,
  `controls/c2-base.out`). **K2 fired**: `w1/SC01SetterSweep.md` F1 (R19 states no slot count for the
  `cli`/`router-child` entries the section itself defines, and its "1 slot" prose for `llama-cli` is
  falsified — measured 1/4/5/6/0 and auto→4) and F2 (a router child inherits the router's environment,
  so `AIP_HTTP_PORT` overrides its assigned free port — measured: child logged "overriding server port
  39547 with AIP_HTTP_PORT 18230" then failed to bind; `--port 18260` + `AIP_HTTP_PORT=18262` listened
  on 18262), F3 (the config.ini route reaches the process's own params only through `[default]`/`[*]`).
  `w1/RV02SetterRows.md` independently read all 92 rows against the archive and found no BLOCKER (four
  vocabulary NOTEs); `w1/CN01SiblingOverlap.md` F4 found the lane's own registry violating R18's
  citation duty (repaired). The corrected readings landed as `SKILL.md` §Round 94 correction (c1–c4),
  a dated block that does not rewrite the frozen rows; R20/R21 are routed.
- **C2 counter attack (`w1/CR02SetterCounter.md`, `w1/MT02SetterCounterMutants.md`).** 20/38 forged
  SKILL variants bind (value/entry/effect misstatements score perfectly — K2 is the only semantic
  gate); 25/29 behaviour-bearing counter mutants are killed and 4 are provably inert; the frozen
  counter reproduces `measured/c2.out` byte-for-byte and accepts no forged row.
- **Pre-report gate.** `python3 tools/pre-report-gate.py --repo . --round 94` →
  `PRE_REPORT round=94 arms=14 failed=2 uncommitted=0`, exit 1; receipt
  `.ufo/waves/round-94/measured/gate-final.out` (committed at `32f8e347`, header `rev=cc3cd82e…`
  `clean_at_grading=1`). The two red arms are carried and disclosed: `round75-instruments`
  (`APPEND_DEBT round=94 events=101 accepted=53 late=26 pending=3 unaccepted=22 bad_rows=19`, plus a
  late-line-96 hash mismatch — R1, L0 r87/r89 open) and `round78-instruments`
  (`LIVE_RECONCILE_SELFTEST pass=1 fail=3`, the host's non-lane Ollama listener on 127.0.0.1:8080).
- **C3 (calibration, verified).** Census 343 → 355 rows (`kama ok …/corpus/SOURCES.md`, exit 0; both
  outputs pasted below), S604–S615 opened this round (S604 cited by C2), one rejection with flip
  recorded, `## Gate` + `## Mistakes` present, plus the r93-closure dispositions R1–R7 and wave-1
  mistakes M4–M7. Repair landed: S604's located quote is at `common/preset.cpp:151`, not 150, in
  `corpus/SOURCES.md` and in the lesson Gate (`w1/CN02SourceFrontier.md` F1,
  `w1/SB01LessonDraft.md` DEFECT-1); census re-run after the repair, exit 0.
- **Frontier-step receipts landed.** The frozen plan named 12 control receipts; only three existed at
  the freeze commit (`w1/CN02SourceFrontier.md` F2, `w1/SB01LessonDraft.md` NOTE-8,
  `w1/SC02BudgetSweep.md` F6). This attempt lands `controls/census-start.out` (base-mirror census,
  exit 0), `controls/c1-base.out` + `controls/c1-base-load.out`, `controls/c2-base.out`,
  `controls/harm-base.out` (base clone: `check.py` 77/77, `test-snapshot.sh` 30/0), and
  `controls/sources-opened.out` (12 new + 9 re-opened raw URLs, sha256 each). The two forgery `.py`
  batteries are **withdrawn** and replaced by `controls/c1-forgeries.out` and
  `controls/c2-forgeries.out`, which collect this wave's real forgery receipts.
- **Adjacency/reuse.** `w1/CN02SourceFrontier.md` re-verified 12 new rows (11 byte-exact; S604 the
  exception, repaired) and confirmed no new duplicate-URL row; `w1/CN01SiblingOverlap.md` confirmed
  the sibling surface clean and the census W04 lines pre-existing.
- **Wave shape.** ONE v1 wave `w1`, 13 seats under `ufo-wave-policy.json` (band 8–16): 8 attack seats
  (RV01, RV02, CR01, CR02, MT01, MT02, CN01, CN02 = 62 % of the wave) + 2 executor (EX01, EX02) +
  2 scout (SC01, SC02) + 1 scribe (SB01); connector seats 2 (cap 2). 13 seat reports are in the tree;
  **MT01 (mutation-tester) is recorded dead in the wave census**: the orchestrator lost its handle in
  a kernel restart, settled it as dead at the wave close, and its `w1-results.json` row carries
  `<output unavailable: FileNotFoundError(...)>`. It was not a quality rejection and not a timeout,
  and it was never replaced. The agent nevertheless kept running and wrote its report and 129-file
  artifact at 01:43–01:45; that artifact is reconciled here and in the falsification ledger
  (`w1/MT01ProbeMutants.dead.md` records both facts). Round total: 13 seats, one wave, zero residual
  calls. The §3 L2 floor is met inside `w1`; the planner seat is held by the L1 (validator rejects
  `planner`), with the bounded planning data-walk riding CN01/CN02.
- **Assimilation:** none this round (no `merge/kama/` theme taken; `considerthese/` not mined).
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none this round (no pacman, uv, cargo or release-binary action; pacman guard
  respected).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only
  `.scratch/` (orchestrator-owned run state, not a misroot) — no seat wrote a lane file into the fleet
  root.

## Landed changes

| Commit | Change | LOG entry |
|---|---|---|
| `285f1783` (attempt 1) | frozen claims `plans/round-94-claims.md` | §Round 94 |
| `a27656a4` (attempt 1) | `tools/kama-probe.sh` per-file parse budget + `tools/round94-router-budget.py` (C1) | §Round 94 |
| `6aa5fa6b` (attempt 1) | `SKILL.md` round-94 setter section, `tools/round94-setter-sweep.py`, 12 SOURCES rows, lesson (C2/C3) | §Round 94 |
| `11d2770b` (attempt 1) | wave `w1` spec + dispatch + `claims.json` | §Round 94 |
| `fd50ae5f` | wave `w1` evidence: 12 seat reports, registry, spec/dispatch/ready, seat receipts; `plans/round-94-amendment-1.md`; S604 quote-line repair; `SKILL.md` §Round 94 correction c1–c4 + Effect vocabulary; `registry/endpoint-consumers.tsv` R18 citations; lesson dispositions R1–R7 + M4–M7; SCORECARD §Round 94 + authority row; LOG §Round 94 | §Round 94 |
| `76af34d7` | controls + falsification ledger + `w1-results.json` (receipts the frozen plan names, landed) | §Round 94 |
| `7f2968ca` | wave `w1` forged-table evidence completed (CR02 variants, MT02 M2 copies) so the round scope is clean | §Round 94 |
| `fe2a6717` | calibration row re-anchored to the round-93 closure (pre-report `newest-closure` arm) | §Round 94 |
| `8b3111bd` | remaining wave evidence (CR02/MT02 copies) | §Round 94 |
| `19101bc9` | MT01 late artifact reconciled, amendment addendum, red base-control receipt | §Round 94 |
| `d5a58ce3` | M1 `burners=0` receipt (matched pair with the red base) | §Round 94 |
| `ca391e05` | C1 filed not verified (honest stop), MT01 recorded as a settled seat with deliverables; scorecard/ledger/amendment corrected | §Round 94 |
| `9a147527` | live plan moves to round 95 (pre-report `selfdesc` arm); `__pycache__` removed from the wave dir | §Round 94 |
| `cc3cd82e` | depth row re-anchored to the edited `SKILL.md` (sha256, 2254 lines, 58 headings) | §Round 94 |
| `32f8e347` | `measured/gate-final.out` (pre-report gate receipt: arms=14 failed=2 uncommitted=0) | §Round 94 |

## Before → after measurements

**C1** — counting command
`python3 tools/round94-router-budget.py --repo . --rev <rev> --work <scratch> [--burners N] --runs 1`:

```
before (e6f1dcce, controls/c1-base.out): cells=19 mismatches=3 positive_mismatches=0 load_cells=19
        load_stable=0 probe=rev probe_sha256=1e21c1fb… rev=e6f1dcce load1_nat=246.26 burners=0   exit 1
        (R02 natural MODEL_OK vs loaded MODEL_UNLOADED; T01 rewrite run3 natural invalid vs loaded MODEL_OK)
after  (a27656a4, measured/c1-M1-burners0.out): cells=19 mismatches=0 positive_mismatches=0
        load_cells=19 load_stable=1 probe=rev probe_sha256=27065a5c… rev=a27656a4 load1_nat=249.15
        burners=0                                                                              exit 0
```

Matched pair at the same ambient band (load1 246.26 vs 249.15, both with no synthetic burners): base is
unstable, M1 is stable. A second base run in the same band was redder still
(`mismatches=7 positive_mismatches=2 load_stable=0`, exit 1). The frozen receipts are
`controls/c1-base.out` and `measured/c1.out` (M1 at `load1_nat=232.08 burners=96`); this attempt's
M1 re-runs add `load1_nat=141.70 burners=32` and `load1_nat=249.15 burners=0`. The counter is **not always
evaluable on this host**: a further M1 run at `--burners 96` and base runs at 32/8 burners exited 2
(`could-not-evaluate: fixture slow.gguf: base loader state '-'`), because the sanity gate runs the
round-93 base probe. Narrowed statement and routing: `plans/round-94-amendment-1.md`.

**C2** — counting command
`python3 tools/round94-setter-sweep.py --repo . --rev <rev> --work <scratch>`:

```
before (e6f1dcce): SETTER_SWEEP 92 0 0 0 0 92 0 0 derived_checked=0 derived_disagree=0 decisions=0/2 pop=92 met=False   exit 1
after  (6aa5fa6b): SETTER_SWEEP 92 92 2 92 0 0 0 0 derived_checked=47 derived_disagree=0 decisions=2/2 pop=92 met=True exit 0
after  (lane tip `32f8e347`): identical to 6aa5fa6b, exit 0
```

Predicate met; **claim not verified** (K2 fired by SC01 F1/F2 and CN01 F4 — see Work performed).

**C3** — census command
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`:

```
before (base mirror, controls/census-start.out): kama ok /fast/scratch/…/kama-shokunin/corpus/SOURCES.md
                                                 CENSUS_START_EXIT=0 ; kama rows 343
after  (measured/census-end.out):                kama ok /home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md
                                                 CENSUS_END_EXIT=0 ; kama rows 355
```

## Sources & frontier

- Census before → after: **343 → 355** rows, exit 0 both (`controls/census-start.out`,
  `measured/census-end.out`; the base figure is a mirror of the lane at `e6f1dcce` — `corpus/SOURCES.md`
  from that revision with every other lane path symlinked and `.ufo` linked for the `used-by` targets).
- Rows added by tier: 12 × tier A (S604–S615), all `mined`, `recheck on-release`, `used-by SKILL.md`;
  no row above appears in a W04/E04 finding.
- Rows touched old → new: none (`status`/`recheck`/`used-by` unchanged on existing rows); S593 and
  S596–S603 re-opened with digests equal to the archive members (`controls/sources-opened.out`).
- Frontier rows advanced: S604 (`common/preset.cpp`) is cited by C2's config.ini route; S605–S615
  ground the entry-point rows (cli embedded server, router-child env, preset mechanism, imatrix,
  perplexity, rpc-server).
- Repair: S604's quote line 150 → 151 (`corpus/SOURCES.md:359`, lesson Gate), found by CN02 F1/SB01
  DEFECT-1.
- Rejections: the codeload archive as a source row (rejected: input, not a teaching source; flip:
  GitHub stops serving per-file raw URLs for the tag).
- Assimilation: none.
- gate: `PREFILE-FALSIFICATION: pass claims=3 rows=14 attack_seats=8 findings=0` (exit 0),
  `python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane kama --round 94`.
  Ledger `.ufo/waves/round-94/claim-falsification.tsv`; every attack seat that produced an artifact
  appears (RV01, RV02, CR01, CR02, MT01, MT02, CN01, CN02).

## Open items / L0

- No L0 question filed this round. Carried: R1 (`round75-instruments` `bad_rows=19`,
  `unaccepted=22`, `APPEND_DEBT_FINDING` late line 96 hash mismatch; L0 r87/r89 open) and the
  `round78-instruments` live-reconcile red caused by the host's non-lane Ollama listener on 8080.

## Trend verdicts

- **expansion: unchanged** — no new lane surface this round beyond the corrected setter readings and
  the C1 capability; the 12 S-rows extend depth on an existing surface rather than opening one. The
  narrow claim is a narrower object than declared, so no expansion credit is taken.
- **quality: improved, with the round's headline claim unverified** — the probe change is
  demonstrated to help at a matched load band (base `mismatches=3 load_stable=0`, exit 1 at load1
  246.26 vs M1 `mismatches=0 load_stable=1`, exit 0 at load1 249.15) and on a live router (EX02:
  base false green 2/2, M1 correct 2/2); the S604 misstatement is repaired and the setter section's
  three falsified statements are superseded by dated corrections. But the counter that was supposed
  to certify load-independence does not: its F1 control is false (MT01 BLOCKER-1), four forgery
  families still pass (CR01 F3/F6/F7/F8 + MT01 M02/M12/M14/M10), and it is often unevaluable on this
  host (SC02 F1). The claim is filed not verified rather than upgraded; harm suites are unchanged at
  base and at the tip (`controls/harm-base.out`: 77/77, 30/0; `round89-unloadable-cells.py` 11/0/0
  with `LLAMA_CACHE`/`HF_HOME` isolation).
- **discernment: improved** — the round's own wave falsified its C1 wording and its C2 K2, and the
  lane took both readings: C1 narrowed with the four residual classes routed, C2 filed as not verified
  rather than admitted, the missing receipts landed, and the dead seat recorded as dead. The C2
  counter's semantic blindness (20/38 forgeries bind) is disclosed instead of papered over.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md`
  §Listen port and slot-count setters (round 94 revision) plus §Round 94 correction c1–c4; no named
  non-author verifier (wave seats are lane-dispatched, per LEARNING.md).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `w1/EX02LiveRouterBudget.md`
  (lane-owned b12177 router child, 13-entry preset, 32 burners, oracle completion check, base false
  green 2/2 vs M1 stable 2/2) and `w1/EX01HeldOutBudget.md` (N = 2…256 sweep); LOG §Round 94.
- [~] Instructions executable by an agent without oral context — `plans/round-94-amendment-1.md` +
  `SKILL.md` §Round 94 correction name every command, revision and receipt path; independent
  execution review remains open.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — registry/endpoint-consumers.tsv
  (lane-owned), `w1/CN01SiblingOverlap.md` reports sibling material without absorbing it; service
  repair, routing and credentials remain operator/sibling-owned.
