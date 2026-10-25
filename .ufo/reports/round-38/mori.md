# mori round 38 — fleet & host observability (森) — report

Lane tip (HEAD when this report was written): `13f3db7e5c7163e7ef300259ff597a42a79f81f1` (branch `master`, local=remote, pushed; `jj-lane.sh state` ahead=0 behind=0). The counters were measured at `b6993744171a05efc627b5e0664489c31aa5214e`, an ancestor of HEAD; the final re-run at HEAD reproduced every verdict (section 3).

## Work performed

Declared claims (frozen contract `.ufo/waves/round-38/contract.md`, pins `evidence/freeze-r38-v3.txt`):

1. **C1 — calibration (5, tied lowest): the content half of the drift-corpus binding** (r37 M9): counter `.ufo/waves/round-38/count-c4.py` (P-C4).
2. **C2 — operability (7): instrument conformance and replayability** (r37 R1/R2/R4, SentTools MEDIUM/LOW, LabTimeoutBoundary): checker `.ufo/waves/round-38/conform.py` (P-C5).
3. **C3 — depth (5, tied lowest): timed supersede semantics in the append-only gate** + S226 (r37 ExecGateRound D3): `tools/mori-sources-appendonly.py` (P-C6).

Work items, each with an evidence pointer:

- **Inherited state resolution.** `.ufo/watchdog.log` carried `lane-dead-no-report mori round=38` (orchestrator froze twice mid-round, attempts 1–3); this attempt inherited the committed freeze/data/wave artifacts (`1f1e996`, `8d26150`, `daa1d4d`, `f725f30`) and the uncommitted wave-2 integration. Re-verified: all three counting commands re-run green at `b6993744` and again at HEAD; v3 freeze pins match the committed bytes; the working-tree hardening (M13/M14) was uncommitted and unscored — it was committed and scored here (`b6993744`).
- **Wave 1** (build/first falsifiers, 65 seats, dispatch `w1-dispatch.json`, validated under policy v2 band 64–128): 13 seat reports in `w1/`; 52 seats lost to orchestrator death with the parent session freeze (no reports; the freeze is the watchdog-logged termination, not per-seat errors).
- **Wave 2** (falsify, 43 seats, dispatch `w2-dispatch.json`): 40 reports in `w2/`; 3 seats never spawned (`CritC4Gaming`, `CritC5Gaming`, `ConnReceipts`, agentId null in `w2/swarm-registry.json`). Findings integrated: M7 claim-cell correction, M8 index-clean log, M12 label vocabulary, M13 bounded drains, M14 unique/one-row checks, M15 v3 pins.
- **Residual re-check** (one ordinary `task` call, 8 seats — 5 reviewer, 2 critic, 1 mutation-tester; operator steer time-box acknowledged mid-flight): all 8 returned, reports in `resid/`. Confirmed at the shipped bytes: C4 mutant kills (4/4), C5 M13 kill, five red receipts reproduce byte-identically, freeze pins + predicates byte-match, census/registry delta clean, C3 discriminator re-derived. New findings recorded, not silently fixed: fabricated-content clones can print `C4=met` (authenticity bound), `check_anchors`/`drift_kill` bypasses, conform `timeout=` name-not-value bypasses (M18/M19, routed to round 39).
- **Red receipts.** `w2/RevS226Row` found M1/M3/M4/M5/M6 lacked able-to-fail receipts; each pre-fix state was reconstructed by a one-spot mutation and run to a committed full-output receipt (`evidence/m1-red.txt`, `m3-red.txt`, `m4-red.txt`, `m5-red.txt`, `m6-red.txt`), reproducers committed under `.ufo/waves/round-38/scratch/red-receipts/`.
- **Misroot sweep** (fleet root): the wave-1 stray `{fleet}/0` (`NF=13 cells=11 double_quotes=0`, catalogued by `w1/ScoutMisroot.md:67`) copied byte-exact to the lane (`cmp` OK), fleet copy deleted, recorded as lesson M17; M9's relocated drift-tool copy committed at `evidence/m9-misroot-mori-source-drift-f725f30.py` (sha `453c5d8e…`). No other lane's files touched; `.ufo/state/*` untouched.
- **Frontier step**: S226 opened and admitted (the round's sourced claim — C3's S226 disposition and the containment entry cite it); census before/after exit 0; lesson M1–M19 mined.
- **L0**: debt (f) re-filed (earlier attempts died before appending it) — committed `93ec4c249d40f85f77aec3c1c16a1c6e3543a5d7` on the fleet repo.

## Landed changes

All commits through `scripts/hyaku/jj-lane.sh`, lane identity `mori-shokunin <mori@shokunin.local>`; each is tied to the round-38 entry in `LOG.md` (appended this round) and `dispatch-log.txt` carries the landing-time index-clean check after each line (QUALITY 103; the `13f3db7e` record's own check result is here: `MORI_INDEX_CLEAN staged=0 intent_to_add=0`, exit 0 — the record itself rides this commit, same disclosed pattern as M8).

| Commit | Content |
|---|---|
| `3501d4c` | round-37 erratum + LOG append-only amendment + inherited late seat reports (earlier attempt, re-verified) |
| `1f1e996` | freeze: contract C1–C3, count-c1 v4, count-c4, conform, fixtures, pins (earlier attempt, re-verified) |
| `8d26150` | before receipts (c4/c5/runnable before-arm) + witness-sandbox builder (earlier attempt, re-verified) |
| `daa1d4d` | data: S226 + content-anchor/containment entries, timed supersede gate, SCORECARD/QUALITY/SKILL, lesson, recipe fix (earlier attempt, re-verified) |
| `f725f30` | count-c1 v4.1 + freeze v2 pins, C4 byte cap, wave-1 spec/dispatch, attempt-2 evidence (earlier attempt, re-verified) |
| `b6993744` | instrument hardening (bounded drains, unique anchors/rows, exact-one capability row, S103 flip), w1+w2 seat reports, red receipts, lesson M16, LOG round-38 entry |
| `96f7f97e` | residual integration: 8 `resid/` reports, receipts re-emitted at `b6993744`, lesson M16–M19 repairs, misroot relocations (`0`, m9), reproducers committed |
| `13f3db7e` | dispatch-log landing record for `96f7f97e` |

Not landed (intentionally): `.ufo/waves/round-38/scratch/` runtime (3.9 GB, regenerated), lane-root `.scratch/` (646 MB of pre-round-23 operator/prior evidence — explicitly untouched per `corpus/lessons/round-23.md:72` and the round-29 spot-check).

## Before → after measurements

One command over committed bytes per claim; before receipts at the entering lineage, after receipts re-emitted at `b6993744` (and re-run at HEAD `13f3db7e`, identical verdicts).

- **C1 (calibration)** — command: `python3 .ufo/waves/round-38/count-c4.py <rev>`. Before: at `e37dcc6` `C4=unmet` exit 1 (`evidence/c4-before.txt`); the discrimination control — a clone of the scored tip with three fabricated token-satisfying witnesses — prints `C2=met` exit 0 under the round-37 token counter (`evidence/v3-token-control.txt`) while `count-c4.py` prints `C4=unmet` exit 1 (`evidence/c4-witness.txt`). After at `b6993744`: `C4=met` exit 0, all four content checks PASS, all three fabricated witnesses `rejected` (`evidence/c4-after.txt`). **Verified (measured).**
- **C2 (operability)** — commands: `python3 .ufo/waves/round-38/conform.py <rev> --counter .ufo/waves/round-38/count-c1.py --counter .ufo/waves/round-38/count-c4.py` and `… --selftest`. Before: `CONFORM=unmet` exit 1, six checks FAIL on the round-37 counters (`evidence/c5-before.txt`). After at `b6993744`: `CONFORM=met` exit 0 (6/6) and `CONFORM_SELFTEST pass=6 fail=0` exit 0 (`evidence/c5-after.txt`, `c5-after-selftest.txt`); the P-C1-of-record counter runs `C1=met` exit 0 at the tip (`evidence/c1-after-r38.txt`). **Verified (measured).**
- **C3 (depth)** — command: `python3 tools/mori-sources-appendonly.py <rev> --round-base f10a320d`. Before: no `supersede_timing` line (`evidence/gate-before.txt`, 0 occurrences), and at `e37dcc6` the shipped gate prints `stale_supersede=[S069]` (`evidence/gate-after-e37dcc6.txt:2`) — S069's only superseder S073 (`71abd41`) predates its in-place edit (`62db24c`). After at `b6993744`: `supersede_timing superseded_as_of=[S041,…,S193] (18 ids) stale_supersede=[]` (`evidence/gate-after.txt:22`); selftest `pass=9 fail=0` with the supersede-before-edit fixture (`evidence/gate-selftest-after.txt`); S226 (opened this round) lands the postdating `supersedes S069` row (`corpus/SOURCES.md:232`, landing `daa1d4d`). **Verified (measured).**

Axes held: coverage 6, operability 7, depth 5, calibration 5, freshness 5, adjacency 6 — no score moves, evidence pointers updated; the calibration and depth rows' evidence now name round 38 (SCORECARD round-38 section + axes-cell correction note). No axis harmed; the residual bypasses (M18/M19) bound what the new checks discriminate and are routed, not hidden.

## Sources & frontier

Counting command: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`.

- Before (round start, `evidence/census-start.txt`): exit 0, 225 rows, benign W04 duplicate-url lines only.
- After (round end, `evidence/census-end.txt`): exit 0, 226 rows, benign W04 lines only. `CENSUS_EXIT=0` both ends.
- Rows added by tier: +1 mined row **S226** (`docs`, tier A, opened 2026-10-23, `supersedes S069`, used-by `corpus/knowledge/containment-timed-supersede-r38.md`); plus the round-38 bounded-search log line (registry search-log append).
- Rows touched old→new: none (no existing row's `status`/`recheck`/`used-by` cell was edited; the gate's round-38-local verdict is `round_changed=[]` against the entering tip `e33bb561`, re-derived by `resid/ResidCensusRegistry.md`).
- Frontier rows advanced: none (FR1–FR14 unchanged; FR11's same-boot window from round 16 remains the only advance).
- Known imprecision: the S226 row's located-quote suffix reads `:657-658`; the quoted sentence runs to line 659 (lesson Gate table corrected to `657-659`; the registry row's cells are intentionally unedited to keep the round's append-only record clean — cosmetic, routed to round 39).
- Claim-source binding: C3 and the containment entry rest on S226 (this round's opened row) — the round's sourced claim.

## Trend verdicts

- **expansion — improved (bounded).** Evidence: +1 admitted source row (S226), two new knowledge entries (`corpus/knowledge/source-drift-content-anchor-r38.md`, `corpus/knowledge/containment-timed-supersede-r38.md`), the round-38 lesson; `resid/RevTrends`-style diff re-derived by `resid/ResidCensusRegistry.md` (delta = S226 + search log, no deletions). Bounded: one mined source, two entries on the existing source-drift line.
- **quality — improved (bounded).** Evidence: instruments now conformance-checked (`CONFORM=met`, selftest 6/6, each mutation flipping exactly its own check), receipts re-emitted at the landed tip, red receipts for every claimed able-to-fail state, bypasses bounded and routed (M18/M19). Bounded: content checks verify internal consistency, not authenticity; ancestry semantics of the gate's timing field is path-order on a linear history (routed R1).
- **discernment — improved (bounded).** Evidence: the calibration claim is measurement discrimination (the r37 counter admits a memoizer and a summary-only printer; the round-38 measurement rejects both while passing the honest gate — `evidence/c1-before-rerun-memo.txt`, `c1-before-rerun-summary.txt`, `c4-after.txt`); lesson M1–M19 mines nineteen mistakes with receipt-backed fixes. Bounded: every in-round reviewer is a dispatched seat (the lane per protocol), so the outside discernment check is the hyaku closure's non-author verifier — in-round spot-check disclosed as not performed (`corpus/lessons/round-38.md` Gate section).

## SHONEN

- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources — asserted by the lane; no named non-author verifier (`w2/RevSHONEN.md`: seed fidelity PASS, all four boxes `[ ]`, no unattested marks).
- [ ] At least one end-to-end domain task executed and logged in LOG.md — asserted; round-38 LOG entry names the three measured claims.
- [ ] Instructions executable by an agent without oral context — asserted; the counting commands run as printed from the lane root (receipts carry `command:` lines).
- [ ] No cross-domain bleed (PROVINCE.md still accurate) — asserted; scope-sentinel clean, detection/report only, tsukuroi/kumitate/kagi/souji boundaries intact.

All four remain `[ ]`: no `[x]` without a named non-author verifier exists; the closure session is the verifier of record.

## Round mechanics

- **Shape:** inherited two-wave (v1-style build/falsify, policy v2 band for the 65-seat wave 1, v1-validated 43-seat wave 2) + one 8-seat residual `task` call; total **116 seats** (≤128).
- **Wave sizes / role mix:** wave 1 — 65 seats (26 reviewer, 11 mutation-tester, 7 executor, 6 scout, 4 critic, 3 scribe, 2 revenger, 2 connector, 2 sentinel, 2 simplifier), 13 reports, 52 lost to the orchestrator freeze (watchdog-logged). Wave 2 — 43 seats (24 reviewer, 9 mutation-tester, 3 critic, 3 scribe, 2 scout, 1 connector, 1 simplifier), 40 reports, 3 never spawned. Residual — 8 seats (5 reviewer, 2 critic, 1 mutation-tester), 8/8 reports.
- **Dead seats:** wave 1 ×52 (orchestrator session froze mid-wave; last error text = the parent's freeze, watchdog `.ufo/watchdog.log` lane-dead-no-report lines), wave 2 ×3 (`CritC4Gaming`, `CritC5Gaming`, `ConnReceipts` — null agentId, never spawned). Residual ×0. No seat was replaced (per contract).
- **Routing:** all seats via the operator's `task.agentModelOverrides` route table; no `model` param passed; no routing files touched.
- **Tools:** no installs/upgrades this attempt (seats reported none; pacman guard respected — zero pacman transactions).
- **Misroot:** two mori files relocated from the fleet root (`0` → lane root, `RevC4Anchors` drift-tool copy → `evidence/m9-…`, byte-exact, `cmp`-verified, fleet copies deleted); recorded as M17 and M9.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open (this report is the round-38 completion signal).
- **Open L0:** debt (f) SIGTERM/grace/SIGKILL operator tradeoff (re-filed, `93ec4c2`).
- **Routed to round 39:** gate timing ancestry semantics (`w2/CritGateSemantics`, `resid/ResidGateTiming` F1/F2, M11); C4 fabricated-content/one-char-anchor/drift-kill bypasses (M18); conform timeout name-not-value bypasses + selftest blind spot (M19); contract's stale `c1-before-rerun.txt` citation (`w2/SimpR38`, frozen bytes — record-only); SOURCES S226 `:657-658` suffix.
