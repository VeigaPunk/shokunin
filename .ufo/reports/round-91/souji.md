# souji round 91 — report

Lane `souji-shokunin`, branch `master`. Attempt 2 (L1 `SoujiR91a2`); attempt 1 (`SoujiR91`) died after landing the
after receipts (`.ufo/watchdog.log` `lane-dead-no-report souji round=91`, 13:51:17). Lane base
`681f6c72b242d410d0e8654efadb2a1553fb111d`. Final lane hash: `9deaefda2853a0b78482f714166523c654b128eb` (see Extras for `ls-remote`).

## Work performed

Declared claims (frozen in `census/round-91/preregistration.txt`, freeze F `a703bcb7`; claim file
`.ufo/waves/round-91/claims.json`, `test -f` → present):

- **C1 — calibration (7, the lane's lowest owned non-retired axis):** five new population rows bind the six mutant
  edits that survived every population the lane had pinned; target `killed_r90=16 killed_r91=22 killed_total=38`.
- **C2 — operability (8):** the excerpt tool's 200-octet window cuts land on UTF-8 sequence boundaries and the r91
  fixture binds the four clauses the r90 wording claimed; target `cases=15 tool_pass=15 before_pass=14`,
  `variants=3 detected=3`, K4 regression `rows=12 mismatches=0 errors=0`. Sourced claim: rests on **S354** (RFC 3629
  §3), opened this round.

Work items:

- Instruments P1 (C1 population/harness/battery/mutants; C2 boundary repair, fixture, variants, controls) —
  commit `7fb865d8`.
- C1 do-nothing control committed before freeze — `d287d3de`
  (`census/round-91/controls/c1-control-r90.txt`: `killed_r90=16 killed_total=16`, the six new members `killed=no`).
- Preregistration frozen before any after-data — `a703bcb7`.
- After receipts, S354 row, knowledge entry `corpus/knowledge/utf8-window-sequence-boundary.md`, QUALITY Q166 —
  `28368806` (`census/round-91/records/c1-after.txt`, `c2-after.txt`, `c2-variants-r91.txt`, `c2-k4-regression.txt`).
- One v1 wave `w1`, 13 seats, settled by the driver (`.ufo/waves/round-91/w1-results.json`); nine reports and four
  dead-seat records committed by explicit path — `db0a904a` (212 wave files).
- Attempt-2 replay of every predicate and control at lane tip `28368806` —
  `.ufo/waves/round-91/l1a2-replay.txt`: C1 `SUMMARY mutants=22 sets=r90,r91 pristine_r90=ok pristine_r91=ok
  killed_r90=16 killed_r91=22 killed_total=38` EXIT=0; C2 (a) `SUMMARY cases=15 tool_pass=15 before_pass=14`
  EXIT=0, (b) `SUMMARY variants=3 fixture=r91 detected=3` EXIT=0, (c) `SUMMARY rows=12 mismatches=0 errors=0`
  EXIT=0, control (ii) `SUMMARY variants=3 fixture=r90 detected=0` EXIT=0.
- Pre-file narrowings recorded before filing — `plans/round-91.md` A1 (C1 STATED LIMITS (iii) premise false: the
  LD4 base run is 35/35 resolved, rc 0), A2 (C2: `_cut_tail` over-advances on a truncated/invalid lead before the
  tail cut; the length test is structural, not RFC-validity; KFF13 is a literal substring scan), A3 (four attack
  seats dead; their attacks did not happen).
- r90 non-author spot-check answered (`corpus/lessons/round-90-verifier-spotcheck.md`): its five routed defects
  are each addressed in `plans/round-91.md` A0.1 (claims path, single attack-share definition, settlement
  provenance, superseded r89 capability row annotated in `SCORECARD.md`, narrowed instrument work carried as C2).

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| C1/C2 instruments, mutant set, r91 population, C2 tool boundary repair (`tools/souji-record-agreement.py` sha `21e5c740…`), fixture, variant probe | `## Round 91` Claims | `7fb865d8` |
| C1 do-nothing control | `## Round 91` Measured | `d287d3de` |
| preregistration (freeze F) | `## Round 91` Claims | `a703bcb7` |
| after receipts; S354; knowledge entry; Q166 | `## Round 91` Measured / Sources / Docs | `28368806` |
| wave evidence, dead-seat records, pre-file ledger, replay, census-before receipt; LOG/SCORECARD/plan A3/lesson M4 | `## Round 91` Wave | `db0a904a` |
| census-after receipt, pre-file gate negative control | `## Round 91` Wave | `9deaefda` |

## Before → after measurements

- **C1** — counting command: `python3 -B census/round-91/c1-clause-battery.py --counter
  census/round-87/c1-pointer-counter.py --mutants census/round-91/c1-mutants.json --work <scratch> --only r90,r91
  --expect-killed 38`. Before (control on the r90 58-row population, committed `d287d3de`): `SUMMARY mutants=22
  sets=r90 pristine_r90=ok killed_r90=16 killed_total=16`, six new members `killed=no`, EXIT 0. After (measured at
  `a703bcb7`/`28368806`, replayed at `28368806`): `SUMMARY mutants=22 sets=r90,r91 pristine_r90=ok pristine_r91=ok
  killed_r90=16 killed_r91=22 killed_total=38`, EXIT 0. Counter `census/round-87/c1-pointer-counter.py` sha
  `fd0a8e24…` unchanged. **Verdict: verified**; STATED LIMITS (iii) wording narrowed (A1), no number moved.
- **C2** — counting commands: (a) `python3 -B tests/fixtures/r91-k4-flagfail.py --tool
  tools/souji-record-agreement.py --before census/round-91/controls/c2-before-tool.py --work <scratch>`; (b)
  `python3 -B census/round-91/c2-variant-probe.py --fixture r91 --work <scratch>`; (c) `python3 -B
  census/round-87/c2-k4-counter.py --tool tools/souji-record-agreement.py --work <scratch>`. Before (r90 tool as both
  arms, P1 `7fb865d8`): `SUMMARY cases=15 tool_pass=14 before_pass=14`, KFF11 red, EXIT 1; variants on the r90
  fixture `detected=0`. After (filed tool `21e5c740…`, measured at `28368806`, replayed at `28368806`): (a)
  `cases=15 tool_pass=15 before_pass=14` EXIT 0; (b) `variants=3 fixture=r91 detected=3` EXIT 0; (c) `rows=12
  mismatches=0 errors=0` EXIT 0. **Verdict: verified as narrowed** (A2): exact on valid-UTF-8 payloads (R91ExecC2Tool
  1137-row sweep, 0 splits); on a truncated/invalid lead before the tail cut `_cut_tail` can re-create the
  byte/character collision (`.ufo/waves/round-91/w1/R91ExecC2Tool/repro-cut-tail-split.txt`); KFF13 enforces the
  literal substrings only (`w1/R91ReviewerC2/kff13-spaced-name-tool.py` scores 15/15). Both residuals routed to r92.

## Sources & frontier

- Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin souji`; rows `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- **Before → after:** 275 → 276 rows. Before (lane base `681f6c72`, `census/round-91/records/sources-census-before.txt`):
  `rows=275`, `ok`, EXIT=0. After (`census/round-91/records/sources-census-after.txt`): `rows=276`, `souji ok`,
  EXIT=0 (W04 cross-scope duplicate-URL warnings only).
- **Rows added by tier:** 1 — tier A `docs`, `mined`: **S354** (RFC 3629 §3, https://www.rfc-editor.org/rfc/rfc3629.txt,
  opened 2026-11-08, capture `census/round-91/srcs/rfc3629.txt` sha `a2a3a394…`, 25-word quote at LF lines 183-185,
  occurrence 1; used by `corpus/knowledge/utf8-window-sequence-boundary.md`). Reject sample, not filed: RFC 3629 §10
  (reason + flip condition in `corpus/lessons/round-91.md` `## Gate`).
- **Rows touched old→new:** S354 locator cell "capture lines 183-185" → "LF capture lines 183-185 (splitlines
  186-188)" within the round (R91Connector F2), logged in the lesson Gate. No other row changed.
- **Frontier rows advanced:** the UTF-8 sequence-boundary cut moves from frontier to core via the S354-backed entry;
  the invalid-lead residue is named as the next frontier item (lesson `## Routed to round 92` 1).
- **Assimilation: none.** Collision check re-run: staged ids 134, lane registry 276, collisions **58**
  (`.ufo/waves/round-91/assimilation/{reg-ids,staged-ids,collisions}`), so nothing is appended; renumbering stays a
  later round's work.
- **considerthese:** `souji-shokunin/considerthese/` does not exist; nothing mined.
- **Mined mistake:** `corpus/lessons/round-91.md` `## Mistakes` M1–M4 (M4: spawned-seat attack share reported for a
  wave whose four attack seats died; fix shown able to fail by the gate's negative control).

## Trend verdicts

- **expansion: improved.** S354 (tier A) and one admitted knowledge entry citing it; registry 275 → 276, census
  EXIT 0 both ends; the C1 population grows by five rows on ground the r90 population did not hold.
- **quality: improved.** The filed tool now places both cuts on sequence boundaries for valid UTF-8 (15/15 vs the r90
  tool's 14/15; three wording variants detected 3/3 vs 0/3 on the r90 fixture), the K4 regression stays green, and six
  previously surviving mutant edits are killed. The invalid-lead and KFF13 residuals are named, not hidden.
- **discernment: improved.** The round's own wave falsified one C1 limit sentence and two C2 sentences; all were
  narrowed in `plans/round-91.md` before filing; four dead attack seats are recorded as non-attacks
  (`w1/dead-seats/`) and the settled attack share (2/13) is reported beside the planned one (4/13).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` Decision
  tables/Error patterns/Checklists; `corpus/SOURCES.md` S354; `corpus/QUALITY.md` Q166; `corpus/lessons/round-91.md` Gate.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md `## Round 91` (battery, fixture,
  variant probe, K4 regression run on committed bytes; replay `.ufo/waves/round-91/l1a2-replay.txt`).
- [~] Instructions executable by an agent without oral context — `census/round-91/preregistration.txt` commands
  reproduced by non-author seats (`w1/R91ExecC1Battery.md`, `w1/R91ExecC2Fixture.md`) and by the attempt-2 L1.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `w1/R91Connector.md` §2 sibling-ownership verdict: no
  sibling owns the surface; no credentials, history or sibling lane touched.

## Extras

- **Round shape:** one v1 wave (`w1`, policy `ufo-wave-policy.json`), 13 seats: 4 executor, 2 reviewer, critic,
  mutation-tester, sentinel, connector (1), scout, scribe, revenger; planner held by the L1 (validator-frozen seat).
  Residual call: none. Round total 13. Launched by attempt 1 (`w1.ready` l1 `SoujiR91`, dispatched 13:19:35, results
  13:48); attempt 2 launched no wave.
- **Attack share:** planned 4/13 = 30.8 % (addendum roles reviewer ×2 + critic + mutation-tester); settled 2/13
  (two reviewers). Gate `ATTACK_ROLES` seats 7/13 planned.
- **Dead seats (4, never replaced; `.ufo/waves/round-91/w1/dead-seats/`):** R91Critic — `429 Rate limit exceeded`
  (opencode-go/crouton-alpha-free); R91Revenger — same; R91Sentinel — `429 … Token Plan usage limit reached (2056)`
  (minimax-code); R91MutCounter — `400 [code=tier_limit_exceeded] membership concurrency limit exceeded: 11/10`
  (amr) then `Devin stream error permission_denied: This model is no longer available for your account`.
- **Pre-file falsification ledger:** `.ufo/waves/round-91/claim-falsification.tsv` (18 rows).
  `python3 scripts/hyaku/prefile-falsification.py --lane souji --round 91` →
  `PREFILE-FALSIFICATION: pass claims=2 rows=18 attack_seats=7 findings=0`, `EXIT=0` (run at lane tip `9deaefda`).
  Negative control (ledger copy without the four dead-seat rows → `FAIL … findings=4`, four `attack-seat-unread`,
  EXIT=1; full ledger on the same copy → `pass`, EXIT=0): `.ufo/waves/round-91/prefile-negative-control.txt`.
- **Pre-report gate:** `git -C souji-shokunin ls-remote origin refs/heads/master` →
  `9deaefda2853a0b78482f714166523c654b128eb	refs/heads/master`.
- **Inherited state (attempt 1):** reused after re-verification — commits `7fb865d8`, `d287d3de`, `a703bcb7`,
  `28368806`; the wave `w1` and its results; uncommitted LOG/SCORECARD/SOURCES/plan/lesson edits (kept). Corrected:
  SCORECARD r92 planned line and LOG wave line, which cited R91MutCounter as if it had run. Discarded: nothing.
  Not authored by this lane and not edited: `corpus/lessons/round-90-verifier-spotcheck.md`, `.ufo/state/*`.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` — untracked entries are
  orchestrator `.scratch/` files only; no souji r91 misroot.
- **Stale-lane:** respawn-per-round driver, round 91 of the hyaku campaign; no other mission of this lane is open.
- **Tool installs:** none. No pacman, no uv/npx/binary fetch, no sysctl/sudo/kernel change.
- **L0 questions:** none opened this round.
