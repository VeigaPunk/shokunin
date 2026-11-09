# souji round 98 — report (attempt 2, SoujiR98a2; inherited from attempt 1, SoujiR98)

Lane HEAD on origin/master: `ec93b642a4b5bdddd7087f0099d5fde37bf0abc0` (pre-report `ls-remote` gate passed).
Lane base: `ff254387005e35ff442555451374ff079dafc2db`. Commits this round: `ca98ad08` (instruments, lesson,
Q175/Q176, knowledge corrections, SCORECARD/LOG) and `ec93b642` (corrected decoy driver, decoy records, late
lesson/scorecard/LOG evidence).

## Work performed

Declared claims (2; both falsifiable, causally separable, distinct axes):

- **C1 (calibration 7).** An object-keyed latch (per-exception event stamp `exc._souji98_last`; `WeakKeyDictionary`
  is unavailable for `SystemExit` on CPython 3.14.8) makes the 17-shape declared-exit table print
  `SHAPES-SUMMARY shapes=17 mismatched=0`, with q1o and q1q at 70 and every caught shape keeping its plain exit.
  Verdict: measured pass; non-author closure pending.
- **C2 (operability 8).** The arms counter reaps by ownership (spawn pid + ppid chain, starttime-verified; plus an
  orphan branch for the counter's own subreaper net). A foreign own-uid decoy carrying the counter's own T1 reap
  token survives under r98, is killed under r97 and under the CM8 mutant. Verdict: **measured, not admitted**
  (see the C2 section below).

Work items (evidence pointers):

- C1 latch build: `census/round-98/c1-survivor-search.py` (sha256 e8ba780a…); `census/round-98/declared-shapes.py`
  (dcec0c9e…); `census/round-98/declared-shapes.expected` (23111a3d…, with the q1i freeze note).
  Seat evidence: `.ufo/waves/round-98/w1/R98ExecC1.md`.
- C1 do-nothing controls on the same 17 shapes: r97 hook `SHAPES-SUMMARY shapes=17 mismatched=3`; r95 hook
  `mismatched=3`. Receipts `census/round-98/records/shapes-r97.txt`, `shapes-r95.txt`, `shapes-r98.txt`.
- C1 no-harm: `SEARCH-SUMMARY generated=278 ambiguous=9 uncompiled=0 hung=1 scored=268 errored=53 killed=139
  survived=76` in both r97 and r98 searches; survivor id lists identical (76 ids). Receipts
  `census/round-98/records/search-r97.log`, `search-r98.log`, `survivors-r98.json`.
- C2 instrument repairs: `census/round-98/c2-setup-arms.py` (ownership reap; `conform` binds `survivors=0` on
  T1; survivor count by descendant relation); `census/round-98/c2-cm8-mutant.py` (argv-only reap, the CM8
  mutant; the committed-at-ca98ad08 version signalled nobody, per R98ScoutSources F2, and was repaired before
  the mutant was measured); `census/round-98/c2-decoy-test.py` (plain sleeper carrying the counter's own T1
  token; polls each planted sleeper's pid; corrected driver at `ec93b642`, see below).
- C2 driver correction after WAVE-DONE: the committed driver (a) fed the pipe-holder as the P1/P2/S1 fixtures,
  which made those arms hang (`conform=13`), so the earlier runs measured the driver, not the reap; (b) killed the
  counter on the test's own 420 s timer, producing `counter_exit=-9` and a false `verdict=spared`; (c) raced the
  T1 arm's 120 s timeout against the probe's own 120 s. The corrected driver uses the lane's real fixtures for the
  non-T1 arms, does not kill the counter, uses `--arm-timeout 200`, and prints `verdict=inconclusive` (exit 2)
  when the counter does not finish with exit 0 or 1.
- Wave w1: 12 seats (5 attack: 2 reviewer, 1 critic, 2 mutation-tester; 1 connector; 1 scout; 1 scribe; 3
  executor). The L1 holds the canonical planner seat. `.ufo/waves/round-98/w1-results.json` records all 12 seats
  settled (WAVE-DONE received). Seat reports present: ExecC1, ExecC2 (status `partial`), ExecCensus, Reviewer1,
  Reviewer2, Critic, MutC1, MutC2, Sentinel, Connector, ScoutSources, Scribe.
- Live source re-open (S075, S372, S368; each byte-identical to its committed capture, occurrence 1):
  `.ufo/waves/round-98/w1/R98ScoutSources/reopen-sources.out`.
- Incident: R98Connector's cleanup loop SIGKILLed 26 live processes of sibling seats (~12:33:50Z). Any `rc=-9`
  result from that window is void. Several earlier seat decoy runs were affected; the L1 re-ran every decoy
  measurement cited here after the incident.

## Landed changes

Each change is tied to a LOG.md entry (`## Round 98` and `Round 98 late`) and to the commit that carries it.

- `ca98ad08`: `census/round-98/` (instruments, shapes, controls, srcs, records); `corpus/lessons/round-98.md`
  (`## Gate`, `## Mistakes` M6–M8, `## Frontier`); `corpus/QUALITY.md` Q175, Q176; knowledge corrections in
  `corpus/knowledge/crash-channels-beyond-excepthook.md` and `deadline-owned-reaping.md`; `plans/round-98.md`
  A0.1 freeze amendments; `SCORECARD.md` round-98 rows and planned r99; `LOG.md` round-98 entry.
- `ec93b642`: `census/round-98/c2-decoy-test.py` (corrected driver); `census/round-98/records/decoy-{r98,r97,cm8}-final.txt`
  and `decoy-{r98,r97,cm8}-counter.out`; lesson `## Late evidence and corrections`; SCORECARD late C2 row; LOG late entry.
- No registry row added (`corpus/SOURCES.md` stays 294 rows; `scripts/sources-census.sh validate --root … souji`
  exit 0 at report time).

## Before → after measurements

C1 (calibration 7):

- Before (r97 instrument on the 17-shape table): `python3 -B census/round-98/declared-shapes.py --search
  census/round-98/controls/c1-r97-search.py --scripts census/round-98/shapes --work <empty>` →
  `SHAPES-SUMMARY shapes=17 mismatched=3` (q1o 1, q1q 1, q1i 70).
- After (r98 instrument): `python3 -B census/round-98/declared-shapes.py --search census/round-98/c1-survivor-search.py
  --scripts census/round-98/shapes --work <empty>` → `SHAPES-SUMMARY shapes=17 mismatched=0`, EXIT 0.
- No-harm: the 278-mutant search is identical in summary and survivor set between r97 and r98 (76 survivors each).

C2 (operability 8), decoy predicate on the corrected driver (`census/round-98/c2-decoy-test.py`, `--arm-timeout 200
--plant-delay 2`, lane fixtures for non-T1 arms):

| counter | `ARMS-SUMMARY` | T1 arm | decoys planted / dead / alive | `DECOY-SUMMARY` | counter exit |
|---|---|---|---|---|---|
| r98 (`census/round-98/c2-setup-arms.py`) | `arms=20 conform=20` | `exit=2 want=2 survivors=0` | 83 / 0 / 83 | `verdict=spared` | 0 |
| r97 (`census/round-98/controls/c2-r97-arms.py`, argv-only) | `arms=20 conform=20` | `exit=2 want=2 survivors=0` | 83 / 60 / 23 | `verdict=killed` | 0 |
| CM8 (`census/round-98/c2-cm8-mutant.py`, ownership removed) | `arms=20 conform=20` | `exit=2 want=2 survivors=0` | 83 / 82 / 1 | `verdict=killed` | 0 |

Receipts: `census/round-98/records/decoy-r98-final.txt`, `decoy-r97-final.txt`, `decoy-cm8-final.txt` (with the
`*-counter.out` files). Counting command: the `c2-decoy-test.py` line above with `--counter` set to each counter.
Superseded and void: the pre-correction runs (`counter_exit=-9`, `verdict=spared` from the killed counter;
the pipe-holder-driver runs with `conform=13`). A separate r97 decoy run with the pre-correction driver measured
`dead=60 alive=61` in one earlier window; it is superseded by the corrected run above.

### C2 verdict: measured, not admitted

Three conditions are not yet met, and the admission decision is not the L1's to make alone:

1. The non-author closure has not run. The seats that judged C2 (Sentinel, Scout, Connector, Critic) are
   attack seats, not the closure.
2. Reap branch (c) — any process in the counter's tree carrying the token, including the T1 escapee via the
   `PR_SET_CHILD_SUBREAPER` net — is wider than the claim wording, which names only the spawn pid and its
   ppid-chain descendants (R98Sentinel FINDING 4, MEDIUM; `cross_arm_probe.py` shows a sibling-arm carrier reached
   by branch (c)). Branch (c) is needed to keep the escapee owned; the operator must decide whether a
   counter-descendant kill is in-claim, or the claim wording must name branch (c).
3. `survivors` is not a witness for the escapee's reap: it counts the spawn-pid chain, and the escapee reparents
   to the counter (R98ScoutSources F3, R98ExecC2 F-2). The decoy predicate is the witness.

The operator decision on (2) is recorded as an L0 question below. This is an open decision, not a verdict
pending a seat.

## Sources & frontier

- SOURCES rows before→after: 294→294. Rows added: none. Rows touched old→new: none. Counting command:
  `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` (EXIT 0).
- Re-opened live this round (not new rows; no status/recheck/used-by change): S075 `proc_pid_stat(5)`
  (man7.org, HTTP 200, sha256 0f04d789…); S372 sys.monitoring RERAISE (docs.python.org, HTTP 200, sha256 2b281793…);
  S368 setsid(2) (man7.org, HTTP 200, sha256 52cbc190…). Scout receipt: `.ufo/waves/round-98/w1/R98ScoutSources/reopen-sources.out`.
- Frontier: C1's sourced claim rests on S372 (re-opened); C2's ownership rule rests on S075 fields 4/22 and S368,
  re-opened this round. No `merge/souji/` theme assimilated (Assimilation: none). `considerthese/`: the lane has
  no `considerthese/` dir.
- The S075 field-4 attribution was corrected in the lesson `## Gate` (kernel-side S332; scope fields 5/6/22).

## Trend verdicts

- **expansion: unchanged.** No registry row added; no new admitted entry on uncovered coverage ground.
- **quality: unchanged.** Two knowledge entries gained r98 corrections superseding withdrawn r97 sentences; no
  falsified sentence is left standing in the entries touched this round.
- **discernment: harmed.** The pre-freeze gate missed the decoy-token mismatch (M7), the survivor-metric defect (M8)
  and the do-nothing count movability (M6). All three were caught by attack seats, not by the lane's own gate.
  The late driver defects (fixture misuse, the counter timer kill, the T1 timeout race) were also caught only
  after WAVE-DONE, by a measurement that disagreed with the committed claim wording.

## L0 questions

- souji | round-98 | C2 reap branch (c): may the counter kill any process in its own tree that carries the arm's
  fixture token (the T1 escapee via PR_SET_CHILD_SUBREAPER, and any sibling-arm carrier), or must the reap be
  restricted to the spawn pid and its ppid-chain descendants? The claim wording and the measured decoy verdict
  depend on this. Open; route-around is "not admitted, measured".

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  (evidence: SKILL.md Decision tables/Error patterns/Checklists/Gate registry; corpus/SOURCES.md S100-S103; non-author verifier pending)
- [~] At least one end-to-end domain task executed and logged in LOG.md
  (evidence: LOG.md:362 (2026-10-19 operator sweep); round-98 decoy and census runs in LOG.md `## Round 98` and `Round 98 late`)
- [~] Instructions executable by an agent without oral context
  (evidence: census/round-98/c2-decoy-test.py and c1-survivor-search.py run commands recorded in this report; census/round-21/run-acceptance.py; non-author verifier pending)
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  (evidence: PROVINCE.md Round21 privacy boundary; .ufo/waves/round-98/w1/R98Connector.md (no sibling owns the crash-sentinel or probe-timeout surface); non-author verifier pending)

Stale-lane: no other mission of this lane is open. Tooling: none installed or upgraded this round (no pacman, which
is paused host-wide; no uv/npx/binary fetch; no sysctl or sudo). Misroot sweep: `git status --porcelain` at the
fleet root shows no untracked file naming this lane or round 98 (6 untracked files, none from this lane).
