# souji — round 92 report (hyaku run 15, attempt 2, L1 SoujiR92a2)

Lane repo `souji-shokunin`, branch `master`. Lane base `5339b2ac79f81aa446f6a2cd4700321cf4982fd3` (r91 closed).
Final lane tip `e112cc73756d480dc2699fcaa202cab88c38cfbc` (pushed; `ls-remote` below).

## Work performed

Declared claims (frozen in `census/round-92/preregistration.txt`, commit F `e8d31f06`):

- **C1 — calibration 7** (the lane's lowest owned non-retired axis): a single-token mutation census of the frozen r87
  counter on the r91 population leaves 124 survivors because no r91 row asserts exit 0 on success; one appended row
  LD4r (LD4 + expect_rc 0) kills 47 of them. **Verifies as narrowed** (`plans/round-92.md` A3).
- **C2 — operability 8** (sourced claim, S355): the K4 excerpt cut moves only across a well-formed UTF-8 sequence
  (Unicode Table 3-7), repairing the r91 invalid-lead collision. **Verifies as narrowed** (`plans/round-92.md` A1).

Work items:

- Adopted attempt 1's uncommitted instruments after re-running each (fixture 20/20 vs 16/20, forgery 5/5, capture
  re-fetched byte-identical) — `plans/round-92.md` A0.1; P1 `44d45b44`.
- Built the C1 survivor census (`census/round-92/c1-survivor-search.py`) and amended it before freeze: per-mutant
  clone deletion (attempt 1's run held 185 GB on /fast), `--ids`, a process-group `--timeout` after mutant
  `a272c34-1-to-0` looped forever — A0.2/A0.3; P2 `1d015a2d`. Census
  `census/round-92/records/c1-search-r91-full.txt`: `SEARCH-SUMMARY generated=270 ambiguous=9 uncompiled=0 hung=1
  scored=260 killed=136 survived=124`.
- Built the r92 population (r91 63 rows byte-for-byte + a comment line naming the r90/r91/r92 rows + LD4r;
  sha256 `f66341fc…`) and the r92 harness (one pin); discarded the NF1r draft row that was red on the pristine
  counter (`census/round-92/controls/nf1r-draft-probe.txt`, A0.4).
- Committed the do-nothing controls before F: C1 `controls/c1-control-r91-population.txt` (`killed=0 survived=47`),
  C2 `controls/c2-control-r91-tool-both-arms.txt` (`tool_pass=16`, EXIT 1).
- C2 repair `tools/souji-record-agreement.py` (`_straddling_sequence`, strict decode) with fixture
  `tests/fixtures/r92-k4-flagfail.py` (KFF14–KFF18, `ast` KFF13 with self-check) and forgery probe
  `census/round-92/c2-forgery-probe.py` — P1 `44d45b44`.
- After receipts post-F (`census/round-92/records/c1-after.txt`, `c1-pristine-after.txt`, `c2-after.txt`,
  `c2-forgery-after.txt`, `c2-k4-regression.txt`) — `e5059168`.
- S355 opened, row + knowledge entry `corpus/knowledge/utf8-window-well-formed-cut.md` — `e5059168`; anchor corrected
  after the wave (A4) — `d64c0260`.
- One v1 wave of 13 seats; integrated every seat (`.ufo/waves/round-92/w1/`, driver `w1-results.json`); amendments
  A1/A3/A4 recorded before filing; pre-file ledger `.ufo/waves/round-92/claim-falsification.tsv` — `d64c0260`.
- Lesson `corpus/lessons/round-92.md` (Gate, five mistakes, wave findings, routed items), QUALITY Q167/Q168, LOG and
  SCORECARD rows, `### Planned (r93)` — `d64c0260`, `a3bcd9d6`.
- Misroot sweep: one seat report found in the fleet root, moved byte-exact into the lane — `a3bcd9d6`.

## Landed changes

| commit | what | LOG.md entry |
|---|---|---|
| `44d45b449408c48f249314e6f574eb5a9371688f` | P1: survivor search, r92 population + harness pin, 47-target set, C2 repair, r92 fixture, forgery probe, C2 controls, S355 capture | `## Round 92` Claims |
| `1d015a2d7ea03008310c48069d04ae7c3e5b4cd3` | P2: C1 control (`killed=0 survived=47`), full census 270/9/1/260/124, search `--timeout`, sources census before | `## Round 92` Claims |
| `e8d31f06c381249bdeaa8ea1a8f2bebe3f5bf81e` | F: preregistration alone | `## Round 92` Claims |
| `e505916878db54107bdd92c65b195659fca52321` | after receipts; S355 row; knowledge entry | `## Round 92` Claims, Sources |
| `d64c026050402c9180c104a93f55faea24f1dbf7` | wave evidence (13 seats), ledger, plan A0–A4, lesson, Q167/Q168, LOG/SCORECARD, census after | `## Round 92` Narrowed, Mistakes, Wave |
| `a3bcd9d6a18ec50b23471e75473735bce53d3785` | misroot sweep, lesson M5 | `## Round 92` Mistakes |
| `e112cc73756d480dc2699fcaa202cab88c38cfbc` | pre-file ledger format fix (gate pass) | `## Round 92` Narrowed |

## Before → after measurements

- **C1** (measured at `e5059168`; instruments `44d45b44`/`1d015a2d`, F `e8d31f06`). Command:
  `python3 -B census/round-92/c1-survivor-search.py --counter census/round-87/c1-pointer-counter.py --harness
  census/round-92/c1-false-row-harness.py --population <POP> --lane . --fleet-root /home/vgpnk/Projects/shokunin
  --work WORK --jobs 8 --ids census/round-92/c1-targets.json`.
  Before (POP = r91): `SEARCH-SUMMARY generated=47 ambiguous=0 uncompiled=0 hung=0 scored=47 killed=0 survived=47`,
  EXIT 0. After (POP = r92): `… scored=47 killed=47 survived=0`, EXIT 0; pristine harness `SUMMARY rows=64
  mismatches=0 accepted=0 refused_true=0 errors=0`, LD4r `rc=0 match=yes`, EXIT 0. Narrowed (A3): the row binds the
  47 listed edits (each a row mismatch, rc 1, none a crash), not their clauses — `R92MutC1` E1 (`ok >= len(pop)-1`)
  survives both populations.
- **C2** (measured at `e5059168`). Command: `python3 -B tests/fixtures/r92-k4-flagfail.py --tool <TOOL> --before
  census/round-92/controls/c2-before-tool.py --work WORK`. Before (TOOL = the r91 tool): `SUMMARY cases=20
  tool_pass=16 before_pass=16`, KFF14/15/16/18 red, EXIT 1. After (TOOL = `tools/souji-record-agreement.py`,
  sha256 `fc0e35c2…`): `SUMMARY cases=20 tool_pass=20 before_pass=16`, EXIT 0; forgery probe `FORGERY-SUMMARY
  forgeries=5 rejected=5 positive=pass`, EXIT 0; K4 `SUMMARY rows=12 mismatches=0 errors=0`, EXIT 0. Narrowed (A1):
  surrogatepass / multi-character-span / forward-head forgeries pass 20/20 (`R92MutC2`), so the one-sequence
  property rests on source reading and `R92ExecC2Sweep` (0 counterexamples in 200,000 payloads), not on the frozen
  predicate.

## Sources & frontier

- Rows before → after: 276 → 277 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`).
  Added by tier: A +1 (S355, `docs`, `mined`, Unicode 18.0.0 ch. 3 §3.9 D86 / Table 3-7). Rows touched old→new: S355
  anchor cell `id="G7404"` → `id="G27506"` (A4, same round). Frontier: the cut rule moves from a sequence-unit source
  (S354, RFC 3629 §3) to a well-formedness source (S355); reject sample D93b recorded with a flip condition.
- Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`:
  round start `souji ok`, EXIT 0 (`census/round-92/records/sources-census-before.txt`); round end `souji ok`, EXIT 0
  (`census/round-92/records/sources-census-after.txt`); W04 warnings only.
- Mined mistakes: `corpus/lessons/round-92.md` `## Mistakes` M1–M5 (M1 and M2 shown able to fail:
  `census/round-92/records/m1-cleanup-fail-check.txt` 44 KB vs 369,072 KB; Q167 count 0/0/1).
- Sourced claim: C2 rests on S355 (opened this round; cited by the tool docstring and the knowledge entry).
- Assimilation: none — `merge/souji/` exists but no theme was taken this round. considerthese: the lane has no
  `considerthese/` directory.

## Trend verdicts

- **expansion: improved.** S355 admitted (277 rows) with a new knowledge entry on ground the lane did not hold
  (well-formedness vs sequence unit); a new capability (a bounded mutation census) and two capability rows with
  passing demonstrations (`SCORECARD.md` Round 92 capability rows).
- **quality: improved.** The r91 invalid-lead collision is repaired and measured (20/20 vs 16/20; 0 counterexamples in
  200,000 wave payloads vs 21,074 property violations on the r91 tool); 47 previously surviving counter edits are now
  bound; Q167/Q168 land with able-to-fail checks. Residuals (over-moving forgeries, 77 survivors, search robustness)
  are named and routed.
- **discernment: improved.** The wave falsified two claim sentences and one source-locator cell; each was narrowed in
  `plans/round-92.md` (A1, A3, A4) before filing rather than defended; the target-selection construction is stated
  (limit vi) and answered with a committed control and a per-target attribution.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` tables;
  `corpus/SOURCES.md` S355; `corpus/QUALITY.md` Q167/Q168; `corpus/lessons/round-92.md` Gate.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md `## Round 92` (census, controls,
  after receipts on committed bytes: `census/round-92/records/`).
- [~] Instructions executable by an agent without oral context — `census/round-92/preregistration.txt` commands
  reproduced by non-author seats (`.ufo/waves/round-92/w1/R92ExecC1Search.md`, `R92ReviewerC1.md`,
  `R92ExecC2Fixture.md`, `R92ReviewerC2.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `.ufo/waves/round-92/w1/R92Connector.md` §1: no sibling
  owns the surface; no credentials, history or sibling lane touched.

## Extras

- **Round shape:** one v1 wave (`w1`, policy `ufo-wave-policy.json`, `w1-dispatch.json` validated `spawn 13`), 13
  seats: 4 executor, 2 reviewer, critic, 2 mutation-tester, sentinel, connector (1), scout, scribe; planner held by
  the L1 (validator-frozen); the planning data-walk rode R92Connector. Residual call: none. Round total 13. Dead
  seats: none (all 13 settled with an artifact, `w1-results.json`). Ready file `l1` `SoujiR92a2`; WAVE-DONE received.
- **Attack share:** 5/13 = 38.5 % (reviewer ×2, critic, mutation-tester ×2); the gate's broader set 7/13.
- **Pre-file falsification ledger:** `.ufo/waves/round-92/claim-falsification.tsv` (21 rows; 5 `falsifies-wording`,
  each pointing at `plans/round-92.md` A1/A3/A4). `python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane souji --round 92` →
  `PREFILE-FALSIFICATION: pass claims=2 rows=21 attack_seats=7 findings=0`, EXIT=0 (first run FAIL findings=7 on an
  uncommented header and `#A1`-style pointers; fixed in `e112cc73`).
- **Pre-report gate:** `git -C souji-shokunin ls-remote origin refs/heads/master` →
  `e112cc73756d480dc2699fcaa202cab88c38cfbc	refs/heads/master`.
- **Inherited state (attempt 1, SoujiR92, died before any wave):** reused after re-verification — the tool repair,
  r92 fixture, survivor search, forgery probe, r91-tool control copy, S355 capture (all in P1). Discarded: attempt
  1's scratch trees only (deleted for the fleet disk limit). Not authored by this lane and not edited:
  `corpus/lessons/round-91-verifier-spotcheck.md`, `.ufo/state/*`.
- **Misroot sweep:** fleet-root `git status --porcelain` showed `?? .ufo/waves/round-92/` holding
  `w1/R92ScoutSources.md` (this round's seat); copied byte-exact into the lane (`cmp` equal), fleet copy deleted
  (lesson M5). No other souji r92 file in the fleet root.
- **Stale-lane:** respawn-per-round driver, round 92 of the hyaku campaign; no other mission of this lane is open.
- **Tool installs:** none (no pacman, uv, npx or binary fetch; no sysctl or sudo).
- **L0 questions:** none opened this round.
