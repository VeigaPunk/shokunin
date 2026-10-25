# kake — round 39 report (attempt 3, L1 `KakeR39A3`)

Lane repo `/home/vgpnk/Projects/shokunin/kake-shokunin`, base `2909f1dc`, lane tip **`f841a48d`**
(pushed; `jj-lane.sh state`: `local=remote=f841a48d… ahead=0 behind=0 tracked=0 untracked=0`).

## Work performed

**Declared claim (one):** **C1 — operability, capability acquisition: a new tool
`scripts/sitemap_audit.py` that audits local sitemap and sitemap-index files against
`.ufo/waves/round-39/c1-contract.md`** (declared by attempt 2 at `ceecb1b1`, frozen counter
`sealed_count.py` sha256 `f3a0cd60…`, key `16440f62…`, predicate `met: passed >= 24 of 24 sealed cases`).
Its frozen kill rule (1) fired before any build, so **C1 is exploratory**. The round makes no other
claim. Robots_audit is not claimed (anti-loop). Both owned axes sit at 10, so the stagnation nudge
applies (declaration, `SCORECARD.md` "Round 39 — C1 declared").

- Inherited state. Attempt 1 landed nothing. Attempt 2 landed `ceecb1b1` (declaration) and `915e9e87`
  (drafting-defect record), and both stand unchanged. Attempt 2's uncommitted lane files
  (`make_w2_spec.py`, `verification/c1-at-*.json`, `w1/`) were moved unread to
  `/fast/scratch/hyaku/kake-r39a3/attempt2-leftovers/` and nothing here cites them. The key was re-hashed
  (`16440f62…`) and moved to a private path; its hash is unchanged.
- Pre-wave controls (`72edf212`). The L1 scored the twelve tools left by attempt 2's dead control
  seats with the frozen counter: max 23 (CodeGuess), then 19, 19, 13 down to 1. Tool absent at
  `915e9e87` gives 0. The reference re-scores 24. (j) check v2 is content-based (routed defect 4),
  selftest 14/14 (`verification/a3-jcheck/`).
- Wave 1, the adversarial control wave (32 seats). The L1 scored every returned tool
  (`verification/a3/w1a3-*.json`). **15 of 54 single-sentence reference mutants and a parser-free
  regex reader (`w1a3-CtlRegexTweak`) meet 24 of 24.** Kill rule (1) is recorded at `4c080d3d` and
  `57bdd802`, before any build. (j) v2.1 (`77b2a86e`) is red under both readings of the `915e9e87`
  defect: A gives 17 controls, B gives 16 (`a3-jcheck/v21-{A,B}.txt`).
- Wave 2 (39 seats). The build `565ef4c9` was written by the key- and reference-blind seat
  `BuildSitemapAudit`. Selftest 150/150. The copy guard against the reference and 21 controls stays
  under 0.29. The counter gives 24 of 24, which is information only (`verification/c1-at-565ef4c9.json`).
  Reveal `aa73d919` (`c1-keyrev-at-565ef4c9.json` 24, base 0, reveal revision refused). All 15 met
  mutants were checked as **valid controls** (`w2a3/Verify*.md`) and all 8 new controls as faithful
  shortcuts (`w2a3/Fidelity*.md`). Five fresh scouts re-opened S105–S109.
- Residual call (5 seats). Non-author verdict **`unprovable-but-better`** by
  `KakeR39A3.ExploratoryVerdictC1` (`resid/ExploratoryVerdictC1.md`). The build matches 18 of 18
  contract-decided witnesses (`resid/ReviewBuildWitnesses.md`). Real run on 6 public sitemaps: build
  = reference on 6/6, and sampled findings are right (fsf.org 212 http-vs-https, nodejs.org 8 cross-host;
  `resid/ReviewRealRun.md`). The contract review finds 4 deviations and 1 ambiguity, carried
  (`resid/ReviewBuildContract.md`). The framing critique gave three fixable objections, all corrected
  by append (`resid/CriticRoundFraming.md`).
- Non-claim repairs. Robots selftest grows 194 → 204 (routed defect 3; tool bytes unchanged;
  `f2b70119`). `source_recheck.py`: an evaluate-time input fault now gives one uncounted
  `check_invalid` (carried defect; `b78a1ea4`). The round-38 wave-2 evidence was committed by attempt 2
  (routed defect 5).

## Landed changes

| Commit | Change | LOG.md entry |
|---|---|---|
| `ceecb1b1`, `915e9e87` | (attempt 2) C1 declaration, contract, counter, S102–S104, r38 closure correction, r38 wave-2 evidence; drafting-defect record | LOG "Round 39", bullet 1 |
| `72edf212` | dead-seat controls scored, (j) v2, census before | bullet 1 |
| `4c080d3d`, `57bdd802` | wave-1 receipts; kill rule (1) fired; SOURCES S105–S109 | bullet 2 |
| `77b2a86e` | (j) v2.1, materialized control diffs | bullet 2 |
| `bb4a1e1e` | wave-1 reports, lesson Mistakes 1–3, QUALITY (o)(p), route check, wave-2 spec | bullet 5 |
| `f2b70119` | robots selftest +10 fixtures, harm receipts | bullet 4 |
| `b78a1ea4` | source_recheck fix + hardening fixture g36 | bullet 4 |
| `565ef4c9` | build: `scripts/sitemap_audit.py`, `scripts/sitemap_audit_selftest.py` | bullet 3 |
| `167bb61e`, `aa73d919`, `d8a20a99` | build receipt, mutant bytes, key reveal, key-revision receipts, real run | bullet 3 |
| `b56433bb`, `f841a48d` | C1 verdict, corrections, PROVINCE/SKILL/LOG/README, census after; lesson Gate rejects | bullets 1–5 |

## Before → after measurements

- **C1 is exploratory, so no counting command decides it.** Information under the frozen counter
  `python3 -B .ufo/waves/round-39/sealed_count.py --root . --revision <rev> --key-revision aa73d919`:
  0 of 24 at `2909f1dc` → 24 of 24 at `565ef4c9`. This does not count: the regex control scores 24
  (`c1-keyrev-CtlRegexTweak.json`), and so do 15 mutants. The command that would show the surface
  unmoved is `git ls-tree -r --name-only <rev> scripts/ | grep -c sitemap_audit`: 0 at `2909f1dc`,
  1 at `565ef4c9`.
- Kill-rule evidence: `jq -s 'map(select(.met))|length' .ufo/waves/round-39/verification/a3/w1a3-Mut*.json`
  → 15 (of 54 receipts, 53 distinct tools). (j) v2.1 at `77b2a86e` → exit 1, A 17 and B 16.
- Harm, measured at `b78a1ea4` (`verification/harm/`): robots selftest 194/194 before and 204/204
  after (robots tool sha `f4d057c4…` unchanged). Source_recheck selftest 106/106 before and after;
  hardening 9/9 → 10/10. No axis harmed.

## Sources & frontier

Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`:
- **Round start.** Base, attempt 2, `census-before.txt`: exit 0, 5 W04, rows 101. Attempt 3 at
  06:47:28Z: exit 0, 6 W04 (S102 duplicates S012's URL), `kake ok` (`census-before-a3.txt`).
- **Round end.** 08:05:27Z, exit 0, the same 6 W04, `kake ok` (`census-after-a3.txt`).
- Rows **101 → 109** (`grep -c '^| S[0-9]' corpus/SOURCES.md`). Added by tier: A 8 (spec 6: S102,
  S103, S104, S105, S106, S107; docs 2: S108, S109). Rejected 0.
- Touched old→new: none. S012 stays `mined`, superseded in scope by S102.
- The L1 re-opened S102–S104 at 06:47Z (sha equal to retained bytes). The L1 re-opened S105–S109
  before writing each row, and fresh wave-2 scouts re-opened them again. Corrections to S106, S107
  and S109 are in the lesson's "Wave-2 corrections".
- Frontier advanced: sitemap files move to an exploratory capability (`corpus/README.md` "Round-39
  frontier step", `PROVINCE.md` "Round-39 sitemap file audit step").
- Sourced claim: C1 rests on S102–S104, opened this round (contract and capability row cite them).
- Mined mistakes: `corpus/lessons/round-39.md` `## Mistakes` 1–3. They cover the thin key, the
  control class covering the pre-declaration oracle, and control builds routed to critics. Each has
  a check shown able to fail ((j) v2.1 red; `route_check.py` red on both wave-1 specs, green on wave 2).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no file written by a
  kake seat.

## Trend verdicts

- **expansion: unprovable-but-better.** New surface: sitemap files. The new tool has a 150-fixture
  selftest, 18/18 contract witnesses and a 6/6 real run, plus five new sources. The claim is
  exploratory, so no counter shows the move; a non-author reviewer judged it better.
- **quality: improved.** (j) check v2 → v2.1 decides on receipt content: 20/20, and its mutants are
  killed. Robots selftest grows 194 → 204, and each new fixture kills its mutant. The source_recheck
  defect is fixed with a red-then-green fixture. QUALITY gains (o) and (p) with checks.
- **discernment: improved.** The frozen kill rule was applied against the L1's interest before any
  build, and no rule was changed after data. Each of the 15 met mutants was independently verified as
  a valid control. Three Gate rejects are recorded with reasons. Against this: two of the round's own
  mistakes (thin key, critic misroute) were caught only by this round's waves, not before the
  declaration.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Pointer:
  SKILL.md "Sitemap file audit — round 39" (registry row, procedure, S102–S109).
- [~] At least one end-to-end domain task executed and logged in LOG.md. Pointer: LOG "Round 39"
  bullet 3 (real run on six public sitemaps, `verification/realrun/`).
- [~] Instructions executable by an agent without oral context. Pointer: SKILL procedure plus
  `scripts/sitemap_audit_selftest.py`, checked by non-author `ExploratoryVerdictC1`.
- [~] No cross-domain bleed (PROVINCE.md still accurate). Pointer: PROVINCE "Round-39 sitemap file
  audit step", boundary line (tabi keeps client-side crawling).

## Round shape, seats, holds

- Shape: **two v1 waves plus one residual call** (policy v1). The L1 holds the planner seat.
- **Wave 1** `kake-r39a3-w1`: 32 seats (critic 12, mutation-tester 6, scout 6, executor 3, reviewer 2,
  scribe 2, connector 1).
  - **Refused (provider `cyber_policy`, item ended, not retried):** `CtlLaneToolWrapper`,
    `CtlNamespaceBlind`, `CtlStructureOnly`. The text is in `w1a3-dispatch-log.txt`.
    `CtlStructureOnly` left a file that was scored as a control (16).
  - Seven critic seats said their role forbids running code and returned source or diffs. The L1
    materialized these byte-for-byte; wave-2 fidelity reviewers confirmed it.
- **Wave 2** `kake-r39a3-w2`: 39 seats (reviewer 28, scout 5, mutation-tester 4, critic 1, executor 1).
  It was validated as one wave and dispatched in four gated chunks (10/12/12/5) under Main's 07:10Z
  ruling, because the fleet gate had ≤10 free seats (`w2a3-chunks.log`). All returned.
- Residual: 5 seats (reviewer 4, critic 1). **Round total 76 seats.** Dead seats 0; 3 refused.
- No attempt-2 seat task was resent. The wave-1 items were new shapes, and attempt 2's twelve dead
  control tools were scored, not re-run.

## Gate

At least one real reject with its reason (lesson `## Gate — rejects (attempt 3)`):
- The sealed counter is rejected as C1's admission instrument: 16 controls meet it.
- The draft criterion-(o) checker is rejected for adoption: 5 of 15 adversarial samples were falsely
  accepted.
- S106's "ignored comes from S102" is rejected as wrong.

## Extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (all seats reported none).
- Open L0 questions: none.
- Carried: the five build deviations (UTF-16 without BOM is the medium one), (j) survivor M06,
  `MutRecheckOversize` boundary survivors, and round-38 routed defect 6 items 2–10.
