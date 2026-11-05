# kaidoku — round 92 report (attempt 1)

Lane `kaidoku-shokunin`, round 92, attempt 1. L1 `KaidokuR92`. Base `73a882712907606eba074377b536c6dd82517e25`; declaration `11f8606178dfd9e72001b31daf412c5463106a63` (claims frozen before any wave data); measured revision `a3d3c649ddfef2b4c850ec950e9f633194f08efc` (the candidate commit); final lane hash `5815996883426673daeb8ba3c0e78eebb537f8f4` (`git ls-remote origin refs/heads/main` prints it).

## Work performed

**Declared claims (2; both frozen at `11f8606`; `plans/round-92-claims.md`, `.ufo/waves/round-92/claims.json`).**
- **R92-C1 — coverage (capability).** Target surface: the round-91 last-block stop-boundary class (packed UPX 5.2.0 `--best` ELF, last block `sz_cpr` moved by ±7), refused in Core in round 91, moves to a measured repair inside the declared window ±16, decided by the packer's verdict `upx -t`. Frozen label `repaired 10 of 10; wrong 0; unsafe 0; intact 5 of 5; far-refused 10 of 10`.
- **R92-C2 — calibration.** Target: the round-91 refusal label admitted three declared counterfeits (CHEAT-A carrier read, CHEAT-B hash table, CHEAT-C exit 1). A new counter v2 must admit none of them, with a typed rc-2 refusal and an unseen carrier. Frozen label `refused 10 of 10; typed 10; unsafe 0; intact 5 of 5`.
- **Axis choice.** Owned axes coverage, depth, calibration and freshness are all at 10.0 on their finite proxies (`SCORECARD.md` `## Saturation`), so the lowest-axis obligation is a tie; the claims sit on coverage and calibration. The stagnation waiver does not apply: a capability entered in round 91 (`SCORECARD.md` round-91 section). No exploratory claim.
- **Do-nothing controls, built and scored with the frozen counters before freeze** (`.ufo/waves/round-92/pre/`, `.ufo/waves/round-92/controls/`): round-91 repair under the C1 counter → `repaired 0 of 10 …`, met False (`c1-control-do-nothing-round91-repair.json`; the identity no-op also scores `repaired 0 of 10`, so the control is the predecessor refusal, as the critic noted); v2 positive control on the round-91 tool → met True (`c2-positive-v2-round91.json`); the three counterfeits under v2 → met False each (`c2-counterfeit-{A,B,C}-v2.json`); the same three under the round-91 label → met True each (`c2-do-nothing-v1-counterfeit-{A,B,C}.json`).
- **Wave `r92-w1`** (one v1 wave, 12 seats, inline spawn handoff; `WAVE-DONE` received; results `.ufo/waves/round-92/r92-w1-results.json`; dispatch `.ufo/waves/round-92/r92-w1-dispatch.json`; ready `.ufo/waves/round-92/r92-w1.ready`). Seat evidence in `.ufo/waves/round-92/w1/`:
  - **ExecRepair** (executor): built the candidate in a clone, ran the frozen C1 counter (met, exit 0) and a selftest (6 cases, 0 failures). Its first draft refused all 20 cells because it assumed the chain ends at the PackHeader; a probe showed it ends 1.1 KB to 343 KB earlier, and the draft was corrected before the counter was run (`ExecRepair/probe1-firstdraft-failure.json`, `ExecRepair.md`).
  - **ExecProbe** (executor): premise probe, independent of the candidate: on all five carriers exactly one packer-green value lies in `[stored±16]`, equal to the stored value; `stored±40` is red; packing is byte-deterministic (`ExecProbe/premise.json`).
  - **ExecCounterAudit** (executor): reproduced 8 of 8 control receipts with identical label, met and exit; every pin matches the claims file; CHEAT-B's table equals fresh packs; CHEAT-A/C equal the round-91 critic definitions except for the path (`ExecCounterAudit.md` §1–4).
  - **ScoutSource** (scout): re-opened S313 this round: HTTP 200, 24181 bytes, sha256 matches; lines match; master drifted at line 506; the row's "every executable carrier" wording is too broad, and the stop boundary is decided by the caller, not by the S313 loop (`ScoutSource.md`).
  - **ScribeKnowledge** (scribe): draft knowledge entry, with numbers left for the L1 (`ScribeKnowledge/knowledge-draft.md`); the landed entry uses the measured values.
  - **ScribeQuality** (scribe): drafts for QUALITY rows 184–187 and mistake M92-a; `sweep-w04.sh` with fixtures (`ScribeQuality.md`). The scribe advised folding rows 186 and 187 into 152 and 150; the rows stay separate, and the overlap is recorded in their attack notes.
  - **ReviewerRepair** (reviewer): HIGH: a pinned-image table (five packed images) passes the frozen C1 label without any packer call (named limit, M92-d). MED: `out == packed` is an identity check that does not call the packer (the candidate does call `upx -t` before writing).
  - **ReviewerContract** (reviewer): no mis-measurement in R92-C2; the parser is key-presence only (`refused: null` counts as typed; the arithmetic bounds it); the plan's `len(scored) == 10` guard is not spelled out next to the label (documentation nit) (`ReviewerContract.md`).
  - **CriticClaims** (critic): both claims are fair in their declared scope once narrowed: C1 "five pinned carriers, window ±16 as a coverage cap"; C2 "the three named round-91 counterfeits". The ±16 window was not fitted to a data cliff; the far arm measures the cap, not the packer. Dispositions adopted (`CriticClaims.md`).
  - **MutCounter** (mutation-tester): 9 of 11 assigned mutants killed; survivors M1, M2 (C2: five-carrier counterfeits) and N1i (C1: pinned-image table) are named limits; extras X1 and N4i killed; the controls behave (`MutCounter.md`, `kill-matrix.json`).
  - **SentinelRepair** (sentinel): HIGH F-C1 (the walker's cost is quadratic in fruitful records; not bounded by the 256 MiB cap in practice) is inherited from round 91 and recorded under QUALITY 183; MED F-A3 (ancestor-symlink escape, rc 0), F-B1 (missing `TMPDIR` falls back to `/tmp`), F-C2 (no aggregate budget over the 33 verdicts) are inherited and routed to round 93; LOW F-A1, F-A-TOCTOU, F-B2, F-B3, F-C-ok, F-D1 (`SentinelRepair.md`).
  - **ConnectorOverlap** (connector): no sibling lane claims the class; `search-repair`, `stop-boundary*` and `R92` names occur only in kaidoku or as other lanes' round numbers; adjacency is host-only (revenger's round-73 probe of `upx 5.2.0`) (`ConnectorOverlap.md`).
- **L1 integration.** The candidate was copied byte-exact (`cmp` equal, sha256 `ce1b1769d56c1d90fcf2ee0800ca508476b45eddc2e8a6d7e2f01aa8d12a70c1`) and landed at `a3d3c649`. Measurements at that revision came from the committed script `.ufo/waves/round-92/l1/measure-at-rev.sh`; receipts in `.ufo/waves/round-92/l1/scores/`.
- **Supplementary probe, not a frozen label.** `.ufo/waves/round-92/l1/supp-unseen-carriers.py` runs the candidate on `bzip2`, `gzip` and `patch`, which no table in the battery names: near ±7 repaired 2 of 2 on each, far ±40 refused 2 of 2 on each (`.ufo/waves/round-92/l1/scores/supp-unseen-carriers-at-a3d3c649….json`). This is the evidence that the search is not a table on the bytes the table cannot name.
- **Regression harm check.** Round-90 battery (`P1 6 of 6; P2 4 of 4; P3 4 of 4`) met at base with the round-91 tool and met at `a3d3c649` with the candidate (REA control true in both).
- **Round-91 defects and dispositions** (`corpus/lessons/round-91-verifier-spotcheck.md` §5): D-91-1 (report figure 7 vs receipt 29) fixed by M92-a, QUALITY 187 and the sweep, which fails on the round-91 report (`7 != 29`, rc 1) and passes on its fixture (rc 0); D-91-2 (vocabulary) handled in this report; D-91-3 (block 31 row 3 cites QUALITY 169) not fixed this round, on purpose: a correction needs a new craft-block revision, depth is not claimed, and the frozen block-31 predicate stays; routed to round 93; D-91-4 (label admits an rc-1 exit and two cheats) answered by R92-C2 and QUALITY 185–186; D-91-5 (README "six own errors") fixed, now eight.
- **Lesson mined:** `corpus/lessons/round-92.md` `## Mistakes`: M92-a (report figure), M92-b (geometry assumed; first draft refused 20/20), M92-c (claim headline wider than the measured set; narrowed), M92-d (pinned-image table passes the C1 label; named, not fixed), M92-e (pinned REA package absent on the host; provisioned), M92-f (L1 shell variables in a backgrounded chain; re-run).

## Landed changes

| commit | change | LOG.md entry |
|---|---|---|
| `11f8606178dfd9e72001b31daf412c5463106a63` | declaration: `plans/round-92-claims.md`, `.ufo/waves/round-92/claims.json`, `tools/round-92/stop-boundary-battery-v2.py`, `tools/round-92/stop-boundary-repair-battery.py`, controls `.ufo/waves/round-92/controls/`, pre-freeze receipts `.ufo/waves/round-92/pre/`, census-before | `## 2026-11-05 — round 92` (declaration bullet) |
| `a3d3c649ddfef2b4c850ec950e9f633194f08efc` | candidate `tools/round-92/upx-stop-boundary-search-repair.py` (measured revision) | round-92 entry, "Candidate" bullet |
| `97bb81ef22a7f9bff7d8cd02d8b891b151f9cc27` | wave evidence `.ufo/waves/round-92/` (dispatch, results, seat reports and receipts, L1 measurement script, scores, supplementary probe) | round-92 entry, "Candidate" and "Sources" bullets |
| `5815996883426673daeb8ba3c0e78eebb537f8f4` | knowledge `corpus/knowledge/2026-11-05-r92-stop-boundary-repair.md`; `corpus/SOURCES.md` (S317 added; S313 `used-by`); `corpus/QUALITY.md` rows 184–187; `corpus/lessons/round-92.md`; `corpus/README.md` (coverage row, knowledge row, lesson-index row, frontier note; D-91-5 count); `SKILL.md` (decision row; registry rows); `PROVINCE.md` (Core bullet; Frontier bullet); `SCORECARD.md` round-92 section; `LOG.md` round-92 entry and round-91 corrections | round-92 entry; SCORECARD round-92 section |

## Before → after measurements

Counting commands are the frozen counters; receipts are cited. Measured revision `a3d3c649` (no tool changed after it).

**R92-C1 (coverage).**
- Before (base `73a882712`, round-91 repair as the do-nothing control): `python3 -I -B tools/round-92/stop-boundary-repair-battery.py --root . --repair-cmd tools/round-91/upx-stop-boundary-repair.py --work <scratch> --rev 73a882712907606eba074377b536c6dd82517e25 --expect "repaired 10 of 10; wrong 0; unsafe 0; intact 5 of 5; far-refused 10 of 10" --json-out .ufo/waves/round-92/pre/c1-control-do-nothing-round91-repair.json` → `repaired 0 of 10; wrong 0; unsafe 0; intact 5 of 5; far-refused 10 of 10`, met False, exit 1.
- After (`a3d3c649`): same counter with `--repair-cmd tools/round-92/upx-stop-boundary-search-repair.py --rev a3d3c649ddfef2b4c850ec950e9f633194f08efc --json-out .ufo/waves/round-92/l1/scores/c1-at-a3d3c649ddfef2b4c850ec950e9f633194f08efc.json` → `repaired 10 of 10; wrong 0; unsafe 0; intact 5 of 5; far-refused 10 of 10`, met True, exit 0.
- Score: 10.0 → 10.0 (the finite proxy is saturated; the surface moved, from a Core refusal to a Core repair inside ±16). Verdict: **met on the frozen predicate**; admission subject to the non-author closure; named limits in the knowledge entry, Limits 1, 2, 5 and 6.

**R92-C2 (calibration).**
- Before (base, round-91 label admits the counterfeits): `python3 -I -B tools/round-91/stop-boundary-battery.py --root . --repair-cmd <cheat> --expect "refused 8 of 8; unsafe 0; intact 4 of 4" --json-out <receipt>` for CHEAT-A, -B, -C → met True, True, True: **admitted 3 of 3** (`pre/c2-do-nothing-v1-counterfeit-{A,B,C}.json`).
- After (`a3d3c649`): `python3 -I -B tools/round-92/stop-boundary-battery-v2.py --root . --repair-cmd <cheat> --rev a3d3c649ddfef2b4c850ec950e9f633194f08efc --expect "refused 10 of 10; typed 10; unsafe 0; intact 5 of 5" --json-out <receipt>` → A `intact 4 of 5` met False; B `intact 4 of 5` met False; C `typed 0` met False: **admitted 0 of 3** (`.ufo/waves/round-92/l1/scores/c2-counterfeit-{A,B,C}-v2-at-a3d3c649….json`). Positive control, the round-91 refusal tool under v2 → met True (`…c2-positive-v2-round91-at-a3d3c649….json`).
- Score: 10.0 → 10.0 (saturated proxy; the verdict is carried by the count). Verdict: **met on the frozen predicate for the three named counterfeits**; the five-carrier carrier read (CHEAT-D) and five-entry table (CHEAT-E) still pass v2 (met True, the critic's and MutCounter's M1/M2) and are named limits. The headline is therefore narrowed to "the three named round-91 counterfeits" (M92-c).

**Harm check.** Round-90 regression `P1 6 of 6; P2 4 of 4; P3 4 of 4`: met at base and at `a3d3c649`. No owned axis is harmed by any measurement.

## Sources & frontier

- **SOURCES before:** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku` → exit 0, `ok`, 221 rows, 29 `W04` (`.ufo/waves/round-92/census-before.txt`).
- **SOURCES after:** the same command → exit 0, `ok`, 222 rows, 30 `W04` (round-end run at `5815996`: exit 0, 222 rows, 30 `W04`; `.ufo/waves/round-92/l1/census-after.txt`). `E01/E03/E04` findings: none. The W04 increase is S317 sharing a URL with S311 under a distinct scope (a warning, not an error).
- **Rows added by tier:** A +1 (S317, `src/p_lx_elf.cpp`, end-of-file trailer check; `mined`); B +0; C +0.
- **Rows touched, old → new:** S313 `used-by`: `corpus/knowledge/2026-11-04-r90-interior-block-szcpr.md, corpus/knowledge/2026-11-05-r91-stop-boundary-refusal.md` → `…, corpus/knowledge/2026-11-05-r92-stop-boundary-repair.md`. S313 `status` mined → mined; `recheck` on-release → on-release; `opened` unchanged (2026-11-04). No row rejected this round.
- **Frontier rows advanced:** `2026-11-05-r92-stop-boundary-repair` (coverage-map row: Core repair within ±16; knowledge row); S317 (the caller's stop-boundary check, which the class's verdict needs).
- **Sourced claim:** the knowledge entry's C1 claim rests on S313 and S317, both opened this round (Gate block in the entry; `ScoutSource.md`).
- **Admit / reject:** S313 admitted (scope narrowed; the "every executable carrier" wording is not used); S317 admitted (both quotes located; lines re-read with `sed -n 8055,8070p`).
- **Assimilation:** none. `merge/kaidoku/` is absent and the lane has no `considerthese/` directory; no operator lesson file (`corpus/lessons/operator-*.md`) exists.
- **Misroot sweep** (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): no file of ours at the fleet root. Other owners' files are present (`.scratch/run15-state.json`, `.ufo/l0-questions.md`, and an earlier `report written` file of tabi's seat, since cleared); none was touched.

## Trend verdicts

- **expansion: improved.** A Frontier edge class (last-block stop boundary) moves to Core as a repair inside a declared window, with S317 entering the registry. Evidence: coverage-map row; knowledge entry; `.ufo/waves/round-92/l1/scores/c1-at-a3d3c649….json`. The window and the pinned-carrier scope are disclosed limits.
- **quality: improved.** Two instruments with frozen labels; QUALITY rows 184–187; D-91-1 repaired by a sweep proven able to fail on the round-91 report (`7 != 29`, rc 1) and to pass on its corrected fixture (rc 0) (`.ufo/waves/round-92/w1/ScribeQuality/sweep-w04.sh`).
- **discernment: improved.** The attack seats broke two claim headlines (the pinned-image table passes the C1 label; the C2 counterfeit set is narrower than the headline). Both were narrowed and recorded (M92-c, M92-d) rather than shipped. No non-author verifier has yet checked this round; the verdict is this lane's record, and the closure is pending.

## SHONEN
- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SKILL.md:48` (last-block decision row) and the round-92 registry rows (`SKILL.md` near line 1990); no non-author verifier yet, so not `[x]`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: the candidate run on five pinned carriers and three out-of-set carriers, with the frozen counters at `a3d3c649`; `LOG.md` `## 2026-11-05 — round 92`; `.ufo/waves/round-92/l1/scores/`.
- [~] Instructions executable by an agent without oral context — evidence: `tools/round-92/upx-stop-boundary-search-repair.py --selftest` (6 cases, rc 0); the counting commands in `corpus/knowledge/2026-11-05-r92-stop-boundary-repair.md` and `SKILL.md`; no `[x]` without a non-author check.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` Core bullet (round 92) and Frontier bullet; `.ufo/waves/round-92/w1/ConnectorOverlap.md` (no sibling claim on the class).

## Tool installs and updates (RULES.md read first; recorded)

- `rea-agents@6.5.0` — channel: npm registry (`npm pack rea-agents@6.5.0`, extracted to `~/.local/share/rea-agents/6.5.0`), then `npm install --omit=dev --ignore-scripts` in that directory for runtime dependencies. Reason: the regression counter's preflight requires the pinned package at that path; the pinned `package.json` sha256 `a500302319c1214a8bb6c9a8b4a4a090806e95eef884204a9d9fbb4003050a6c` matches the counter's pin, and `package.json` was unchanged after the install.
- No pacman, no sysctl or kernel parameter, no service change. No other installs. Seats installed nothing (`ExecCounterAudit`, `ConnectorOverlap`, `SentinelRepair` confirm).

## Wave shape, dead seats, residual

- One v1 wave `r92-w1` under `ufo-wave-policy.json` (band 8–16), 12 spawn seats, delivered by the inline handoff and settled (`WAVE-DONE`).
- Roles: executor 3, scout 1, scribe 2, reviewer 2, critic 1, mutation-tester 1, sentinel 1, connector 1. Attack share 4 of 12 = 33 % (reviewer 2, critic 1, mutation-tester 1). Connector seats 1. The planner seat is held by the L1 (validator refuses `planner`). Residual call: none. Round total: 12.
- Dead seats: none (12 settled with output; `r92-w1-results.json`).
- Earlier attempts: none (`.ufo/watchdog.log`: `launch kaidoku round=92 … attempt=1`, no `lane-dead-no-report` line for round 92).

## Stale-lane

Respawn-per-round driver. No other mission of this lane is open.

## Open items and routed to round 93

- Fresh-pack oracle in the repair counter (closes the pinned-image limit; a declared instrument revision).
- Walker cost bound and aggregate budget, the ancestor-symlink write escape and the `TMPDIR` fallback (SentinelRepair F-C1, F-C2, F-A3, F-B1; inherited from round 91).
- D-91-3 correction of craft block 31 (a superseding criterion or a new block revision).
- A two-green carrier, if one exists, to measure the ambiguity branch.
- PE and Mach-O packed inputs.
- L0 questions: none appended; nothing blocks the round.
