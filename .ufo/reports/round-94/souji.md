# souji — round 94 report (L1 SoujiR94, attempt 1)

Lane `souji-shokunin`, branch `master`. Lane base `eddb1be6c34c2e0bef8c1e8ae6ea2f4b381c5536` (r93 closed admitted).
Final lane tip `22060315c479e6af49e96fc23d84951752dd1f59`. Contract: `census/round-94/preregistration.txt` (freeze F `4ad74b9d`).

## Work performed

Declared claims (2): **C1 — calibration 7** (the lane's lowest owned non-retired axis; sourced claim, S357/S358) and
**C2 — operability 8**.

- **C1 — calibration 7.** The r93 survivor search scores a mutant whose counter raises an uncaught exception as
  killed: a Python crash exits 1, the counter's own "not every item resolved" code (r93 routed defect 2, R93Sentinel
  M1). The r94 search `census/round-94/c1-survivor-search.py` puts a `sitecustomize.py` on PYTHONPATH whose
  `sys.excepthook` exits 70 (S358 EX_SOFTWARE), inherited by the harness and every counter it spawns, and scores any
  harness exit 70 or ROW `rc=70` as `errored` (S357's Runtime error state). Counted quantity: crash fixtures scored
  killed, 2 → 0, with the two r93 semantic kills and one survivor unchanged (`census/round-94/records/c1-after.txt`).
- **C2 — operability 8.** The r93 forgery probe exits 1 ("a forgery survived") on 7 of 8 setup arms of the new arms
  counter `census/round-94/c2-setup-arms.py` (r93 routed defect 5 plus six more setup shapes). The r94 probe
  `census/round-94/c2-forgery-probe.py` runs on an existing empty `--work`, refuses the others with exit 2 and a
  `C2-FORGERY-FATAL:` line, and keeps its verdict exits 0/1: arms conform 3 → 10 (`records/c2-after.txt`).
- **Fresh-start prerequisites (addendum):** do-nothing and forgery controls for both claims executed and committed in
  P2 `39d4163a` before F: `controls/c1-control-r93-rule.txt` (`errored=0 killed=4 survived=1`),
  `controls/c1-forgery-controls.txt` (FA blanket-errored `killed=0`, FB no-sentinel `errored=0`; refused 2/2),
  `controls/c2-control-r93-probe.txt` (`conform=3`, EXIT 1), `controls/c2-forgery-controls.txt` (GA verdict-exit-2,
  GB refuse-empty-dir, conform=9 each; refused 2/2). Positive arms sit inside each control (semantic kills, survivor,
  verdict arms P1/P2), so blanket refusal is not a gain. Pre-freeze feasibility disclosed:
  `controls/prefreeze-feasibility-note.txt`.
- **Wave (12 seats) and amendments:** `plans/round-94.md` A1-A5. A1 (R94ScoutSources FW1, R94Sentinel F1): C1 stated
  limit (ii) omitted SystemExit and atexit/`__del__` exceptions — narrowed. A2: the knowledge entry's exit-1 premise
  had no source row — grounded by own receipts plus S359. A3 (R94Critic): a fitted no-sentinel rule also meets the
  five-target number — recorded as a reading; mechanism evidence is the `rc=70` rows and the census. A4 (R94Critic,
  R94ReviewerC2, R94Sentinel F6): the r94 probe docstring's "every setup failure exits 2" is false for non-UTF-8
  tool/before, a file-parent `--work` and a mid-run write failure — narrowed; the claim's "every other setup arm"
  holds. A5 (R94Critic, R94MutC2): arm-name fitting reaches 10/10; two guards unbound — reading.
- **Reported, not claimed — full census** (`.ufo/waves/round-94/w1/R94ExecCensus.md`): over 273 mutants on the r93
  population the r93 rule reads `errored=20 killed=167 survived=76`, the r94 search `errored=48 killed=139
  survived=76`; 28 verdicts change, all `yes`→`errored`, all with `rc=70` rows; 28 of 167 historical kills (16.8 %)
  were crashes; survivor sets identical.
- **Frontier step:** S357, S358, S359 admitted (`corpus/SOURCES.md`), knowledge entry
  `corpus/knowledge/mutant-crash-is-not-a-kill.md`, lesson `corpus/lessons/round-94.md` (Gate, Mistakes M1-M3, wave
  findings, routed), QUALITY Q171.

## Landed changes

All through `scripts/hyaku/jj-lane.sh` (author `souji-shokunin`); each tied to LOG.md `## Round 94 (2026-11-09)`:

- `24cd67b0eff2cf3ec98cbfe74e3f4ef3fdaab88a` — P1 instruments: r94 search, targets, r93-rule control wrapper, C1
  forgery runner, r94 probe, arms counter, C2 forgery runner, S357/S358 captures + rows, knowledge entry.
- `39d4163a66c350f219287530a5aed6ac9d5e7224` — P2 controls (both claims, do-nothing + forgeries), sources census
  before, pre-freeze feasibility note.
- `4ad74b9df466eff28bdf3785c33f6c5fc50bf966` — F preregistration alone.
- `b065b7f036b32aa2114f3dedd9d0ec88b43dfcb2` — A after receipts (`records/c1-after.txt`, `c2-after.txt`, per-mutant
  harness outputs, arm outputs).
- `0e5bc086563469f4b1074bd68e100181972f66d0` — integration: plan amendments A1-A5, S359 row + capture, entry wave
  corrections, lesson, Q171, SCORECARD r94 rows + `### Planned (r95)`, LOG, sources census after.
- `22060315c479e6af49e96fc23d84951752dd1f59` — wave evidence: spec builder, spec, dispatch, results, claims.json, seat reports and receipts,
  claim-falsification ledger, prefile gate receipt.

## Before → after measurements

- **C1** (measured at `b065b7f0`; instruments P1 `24cd67b0`, freeze F `4ad74b9d`). Command: `python3 -B
  census/round-94/c1-survivor-search.py --counter census/round-87/c1-pointer-counter.py --harness
  census/round-93/c1-false-row-harness.py --population census/round-93/c1-false-rows.tsv --lane . --fleet-root
  /home/vgpnk/Projects/shokunin --work <empty> --jobs 5 --ids census/round-94/c1-targets.json`.
  Before (do-nothing, `census/round-94/c1-control-r93-rule.py` = frozen r93 rule, same args):
  `SEARCH-SUMMARY generated=5 ambiguous=0 uncompiled=0 hung=0 scored=5 errored=0 killed=4 survived=1`, EXIT 0 —
  h-crash-late and h-crash-index `killed=yes` (2 mis-scored).
  After: `# crash-sentinel rc=70 check=pass`, `SEARCH-SUMMARY generated=5 ambiguous=0 uncompiled=0 hung=0 scored=5
  errored=2 killed=2 survived=1`, EXIT 0 — both crash fixtures `killed=errored`, h-ok-admits-one and a491c22-<-to-<=
  `killed=yes`, a127c26-True-to-False `killed=no` (0 mis-scored). Re-derived by R94ExecC1, R94ReviewerC1, R94Critic,
  R94Scribe, R94MutC1 (pristine copy).
- **C2** (measured at `b065b7f0`). Command: `python3 -B census/round-94/c2-setup-arms.py --probe <PROBE>
  --fixture-pass tests/fixtures/r93-k4-flagfail.py --fixture-fail tests/fixtures/r92-k4-flagfail.py --tool
  tools/souji-record-agreement.py --before census/round-92/controls/c2-before-tool.py --work <empty>`.
  Before (`<PROBE>` = `census/round-93/c2-forgery-probe.py`): `ARMS-SUMMARY arms=10 conform=3`, EXIT 1 (S1, S3-S8
  exit 1). After (`census/round-94/c2-forgery-probe.py`): `ARMS-SUMMARY arms=10 conform=10`, EXIT 0. Re-derived by
  R94ExecC2 (also a direct probe run: `FORGERY-SUMMARY forgeries=8 rejected=8 positive=pass`, EXIT 0).

## Sources & frontier

- Rows before → after: 278 → 281, counted by `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
  Added by tier: A ×3 (S357 Stryker mutant states, S358 sysexits(3), S359 Python `sys.excepthook`), all `mined`,
  `used-by` `corpus/knowledge/mutant-crash-is-not-a-kill.md`. Rows touched old→new: none
  (`git diff eddb1be6 -- corpus/SOURCES.md` → 3 added lines, 0 removed; R94Connector rule-2 check).
- Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`
  → round start `souji ok` EXIT 0 (`census/round-94/records/sources-census-before.txt`); round end `souji ok` EXIT 0
  (`census/round-94/records/sources-census-after.txt`); pre-existing W04 duplicate-URL warnings only.
- Live re-open (non-author): R94ScoutSources fetched S357/S358 live — byte-identical sha256, quotes 1× each, word
  counts match. Reject sample: PIT `DetectionStatus.java` @1.30.2 (out of province, no consuming entry; flip stated).
- Frontier advanced: crash classification of mutation verdicts (new ground; the lane held kill rules but no
  runtime-error state). Mistake mined: M1-M3 (`corpus/lessons/round-94.md` `## Mistakes`); M1 and M2 fixes are shown
  able to fail by the P2 controls.
- Assimilation: none (no `merge/souji/` theme taken). considerthese: the lane has no `considerthese/` dir.

## Trend verdicts

- **expansion: improved.** Three tier-A rows and a knowledge entry on ground the lane did not hold (runtime-error
  vs killed; sentinel exit status), plus two new capabilities (SCORECARD `### Round 94 capability rows`).
- **quality: improved.** Two instruments whose exit codes lied are fixed and measured against their predecessors on
  committed bytes (C1 2 → 0 mis-scored; C2 conform 3 → 10), with forgery controls refusing blanket fixes; the census
  shows 28 historical crash kills the old rule counted.
- **discernment: improved.** The wave falsified one prereg limit sentence, one instrument docstring and one unsourced
  premise; each was narrowed or grounded in `plans/round-94.md` before filing (A1, A2, A4) and two predicate-strength
  readings recorded (A3, A5) instead of being defended; one candidate source rejected with a flip condition.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `corpus/SOURCES.md`
  S357-S359; `corpus/QUALITY.md` Q171; `corpus/lessons/round-94.md` Gate.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md `## Round 94 (2026-11-09)`
  (controls and after receipts on committed bytes: `census/round-94/controls/`, `census/round-94/records/`).
- [~] Instructions executable by an agent without oral context — `census/round-94/preregistration.txt` commands
  reproduced by non-author seats (`.ufo/waves/round-94/w1/R94ExecC1.md`, `R94ExecC2.md`, `R94ReviewerC1.md`,
  `R94Critic.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `.ufo/waves/round-94/w1/R94Connector.md` §1: no sibling
  owns the surface; no credentials, history or sibling lane touched.

## Extras

- **Round shape:** one v1 wave (`w1`, policy `ufo-wave-policy.json`, `w1-dispatch.json` validated `spawn 12`), 12
  seats: 3 executor, 2 reviewer, critic, 2 mutation-tester, sentinel, connector (1), scout, scribe; planner held by
  the L1 (validator-frozen); the planning data-walk rode R94Connector. Residual call: none. Round total 12. Dead
  seats: none (12/12 settled with a report, `w1-results.json`). Ready file `l1` `SoujiR94`; WAVE-DONE received.
- **Attack share:** 5/12 = 42 % (reviewer ×2, critic, mutation-tester ×2); the prefile gate's broader set 7/12.
- **Pre-file falsification ledger:** `.ufo/waves/round-94/claim-falsification.tsv` (23 rows; 9 `falsifies-wording`,
  each pointing at `plans/round-94.md`). `python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py
  --lane souji --round 94` → `PREFILE-FALSIFICATION: pass claims=2 rows=23 attack_seats=7 findings=0`, EXIT 0 (receipt `.ufo/waves/round-94/prefile-gate.txt`).
- **Pre-report gate:** `git -C souji-shokunin ls-remote origin refs/heads/master` → `22060315c479e6af49e96fc23d84951752dd1f59	refs/heads/master`.
- **Inherited state:** none (attempt 1; lane clean at base, no `lane-dead-no-report souji round=94` line). Not
  authored by this lane and not edited: `corpus/lessons/round-93-verifier-spotcheck.md`, `.ufo/state/*`.
- **r93 spot-check routed defects:** item 2 answered by C1, item 5 by C2; items 1, 3, 4 carried to `### Planned
  (r95)` (R94Connector §3.1 table).
- **Misroot sweep:** fleet-root `git status --porcelain` shows no souji r94 file; only orchestrator `.scratch/`
  entries, never touched.
- **Seat hygiene defect:** R94ExecCensus left an empty scratch dir `/fast/scratch/hyaku/souji-r94/R94ExecCensus`
  (0 bytes); removed by the L1 with the round scratch (`/fast/scratch/hyaku/souji-r94`) after landing.
- **Stale-lane:** respawn-per-round driver, round 94 of the hyaku campaign; no other mission of this lane is open.
- **Tool installs:** none (no pacman, uv, npx or binary fetch; no sysctl or sudo).
- **L0 questions:** none opened this round.
