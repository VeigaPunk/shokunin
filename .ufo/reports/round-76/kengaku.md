# kengaku — round 76 report (hyaku run 15, attempt 1)

Lane: `kengaku-shokunin`. Base `fda63968f29f8f58dc2b28831acac879405b8326`; lane tip at filing
`a6a2a7b83fd424b3e1d163b082281d9fb052a259` (pushed; `ls-remote` equals it). Round shape: ONE v1 wave,
14 seats, no residual call, round total 14.

## Work performed

The round declared **two** claims, each on a distinct axis with its own falsifiable before→after:

- **R76-C1 — coverage** (lowest non-retired axis, L0-capped at 7): every row of `PROVINCE.md`'s
  `## Surfaces` table is resolved live from the table's own bytes and the row's dated declaration must
  agree with the host (the claim is table-scoped: `## Province map` → `### Core` declares a separate
  older table that the census does not read — Amendment A8, routed as a future claim). Counter `plans/round76_c1_surface_resolver.py` (legs: per-row `SURFACE` verdict, `SURFACES`
  tallies, `IDENTITIES` manifest, `AGREE`); defects `UNDECLARED-ABSENT`, `STALE-ABSENT`, `STALE-TEXT`,
  `NOANCHOR`, `MALFORMED`, `MALFORMED-DATE`, `DUPLICATE-SURFACE`, `NONLOCAL-ANCHOR`, `ESCAPE-ANCHOR`,
  `OVERFLOW-ANCHOR`, `TALLY-MISMATCH`, `MANIFEST-DRIFT`.
- **R76-C2 — calibration** (held at 10, exercised): the newest closure's routed defects become a
  burn-down — each id a ledger row, each close an ancestor commit that *contains* its evidence, each
  discharge re-derived by a leg. Counter `plans/round76_c2_defect_discharge.py` (legs D1–D7 + ledger).

Work items (each with its evidence pointer):

- **Freeze** — claims, both counters, the before receipts and the two counters' controls committed at
  `42fad482`; spec/dispatch/validate under `.ufo/waves/round-76/` (w1, 14 seats).
- **R76-C1 measurement** — before `corpus/evidence/round76/c1-before.txt` (rc 1, `agree=8 disagree=3`),
  after `c1-after.txt` (rc 0, `agree=11 disagree=0`); selftest `c1-selftest.txt` (`cases=12 red=11`),
  mutants `c1-mutants.txt` (`9/9`, `wrong_id=0`), control `c1-control-declared.txt`
  (`disagreements=1 target_reached=False`).
- **R76-C2 measurement** — before `c2-before.txt` (rc 1, `registered=0 open=7`), after `c2-after.txt`
  (rc 0, `discharged=7 legs_passed=7`); batteries `c2-selftest.txt` (`cases=14 red=13`),
  `c2-selftest-git.txt` (`3/3`), `c2-mutants.txt` (`12/12`), `c2-control-status.txt`
  (`rows_claimed_closed=7 trivial_checks=1 failed_legs=3`).
- **Sourced claim** — S252 opened live (`corpus/evidence/round76/sources/git-merge-base.html`, HTTP 200,
  41 397 B, sha256 `46d106b7…`), quote at capture line 1703, 25 words; it grounds C2's three-state
  ancestry leg and its reject.
- **Inherited repairs** — the round-75 index gate was red at base (missing lesson row for
  `round-75-verifier-spotcheck.md`) and went red again for `round-76.md` until its README row landed;
  `round74_c1_registry.py` was red at base with `MISSING 2` (the round's own instruments unregistered)
  and is green after their SKILL rows; **`round51_surfaces.py` was red at base** (`UNCOVERED 1`) and my
  row-2 repair broke a second anchor — repaired (SF02 re-anchored, SF21 added, SF14 count re-pinned to
  244) so it prints `UNCOVERED 0`, `RESOLVE observed_present=15 floor=13`, `PREDICATE R51-C1 pass`.
- **Wave** — 14 seats; findings that changed the round: `ReviewerC1R76` (scope shrink, anchor/endpoint
  substitution, duplicate rows, opaque dates), `SentinelR76` (unrestricted endpoint destination and
  redirects, `..` traversal, brace bomb, malformed-host abort, receipt overwrite), `LabratR76` (H1
  confirmed: any non-000 status is `present`; identity is not checked — kept as a stated limit),
  `ConnectorR76` (close-commit ancestry is not evidence-at-commit; sibling primitives inventory),
  `ScoutFrontierR76` (the burn-down predates the round; the ledger's 167/175 staged-id collision),
  `C1ReplayR76` (the control ignored `--lane/--rev`; row 3 stale prose unflagged), `C2ReplayR76` and
  `ScribeLessonR76` (mis-frozen Before line), `ScribeCorrectionsR76` (hard-coded scratch in `emit()`),
  `ReceiptMintR76` (the round-74 C1 gate red at the freeze — the reason the receipt is minted at A),
  `MutantR76` (survivor report), `ScribeSourcesR76` (S252 byte-identical re-fetch, census math),
  `CriticR76` (C1's heading overreaches the table; a re-derived literal can sit in an explicit non-discharge) and `ReviewerC2R76` (an empty scope passes; markdown legs read raw bytes; a PENDING leg could pass) — all four classes closed by Amendments A8/A9 except the stated limits.
- **Prior-art honesty** — R76-C1 is an **increment** of round 51's manifest-based resolver
  (`plans/round51_surfaces.py`), not a first acquisition; the connector's sibling table (kagi,
  kumitate, kama, kotoba, kake, kasegi, mado) is reported, not absorbed.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: claims + two counters + before/control receipts | round-76 entry, "Trigger → action → outcome" | `42fad482` |
| A: PROVINCE rows 2/4 repaired, resolver declared (§Round 76), Q55, SCORECARD D2/D3 corrections, SKILL round-75 rows corrected + two new gate rows, round-74 lesson appended correction, README index rows | "Inherited drift repaired"/"**R75-D5 correction**" | `6977019b` |
| B: seven R75 ledger rows, S252 row (243→244), round-76 lesson, LOG entry, D6 tip receipts, claims A1 | "**R75-D5 correction**", "Learning" | `f0d52322` |
| C: C2 `emit()` honours `--work` (seat finding), claims A2 | "Trigger → action → outcome" | `d76db01c` |
| D: after receipts at `d76db01c`, SCORECARD round-76 section | "Verification boundary" | `218a277b` |
| E: C1 control reads `--lane/--rev` (seat finding), A3, receipts | "Verification boundary" | `447f177a` |
| F: whole-row stale-prose scan + row-3 repair, A4 with the re-measured before, receipts, README lesson row | "Learning"; M76-5 | `26c6dfa6` |
| G: after receipts at `26c6dfa6`, SCORECARD addendum | "Verification boundary" | `c8c116b4` |
| H: resolver confinement/manifest + ledger evidence-at-close, A5, receipts | "Trigger → action → outcome" | `4b884412` |
| I: after receipts at `4b884412`, addendum 2 | "Verification boundary" | `57a0438d` |
| J: provenance corrections (burn-down predates r76), ledger source pointers, A6 | "**R75-D5 correction**"; lesson §Correction | `7f2cd3b9` |
| K: round-51 resolver repaired, A7 prior-art correction, receipts | "Inherited drift repaired" | `e551cec2` |
| L: Round-76 capability rows, final after receipts at `e551cec2`, addendum 3 | "Learning" | `6445a726` |
| M: wave evidence (spec/dispatch/validate and the seat reports that had landed) | "Verification boundary" | `cc91fcf3` |
| N: wave findings as stated limits (lesson + LOG) | "Round-76 wave (appended)" | `1ce25089` |
| O: `NEGATED-DISCHARGE` leg, C1 claim table-scoped, A8 | "Learning" | `dddc1712` |
| P: after receipts at `dddc1712`, addendum 4 | "Verification boundary" | `cdabb951` |
| Q: wave results (14 settled seats) + the critic and reviewer-C2 reports | "Round-76 wave (appended)" | `84fc4b10` |
| R: `EMPTY-SCOPE`, rendered-text legs, `LEG-PENDING`, A9 | "Second-reviewer classes" | `d31feec9` |
| S: after receipts at `d31feec9`, addendum 5 | "Verification boundary" | `d68c1143` |
| T: `SCOPE` tally counts the new defects | "Verification boundary" | `a47a5530` |
| U: final after receipts at `a47a5530`, addendum 6 | "Verification boundary" | `a6a2a7b8` |

## Before → after measurements

Both claims, one rule per pair (R75-D3 class): the before and after receipts were produced by the same
final counter revision.

**R76-C1.** `python3 plans/round76_c1_surface_resolver.py --lane .`
- before (`--rev fda63968`, `c1-before.txt`, rc 1): `SURFACES total=11 present=4 absent=7 prose=0`,
  `AGREE agree=8 disagree=3`; `DEFECT STALE-TEXT 2` (bench-arena "relocated intact"), `DEFECT
  STALE-TEXT 3` (`:34113` "identity re-probed"), `DEFECT UNDECLARED-ABSENT 4` (`:45669` answers 000,
  no marker); `PREDICATE R76-C1 fail`.
- after (`c1-after.txt`, stamped `a47a5530`, rc 0): `SURFACES total=11 present=4 absent=7 prose=0`,
  `IDENTITIES n=11 unique=11 sha256=7f41f588…`, `AGREE agree=11 disagree=0`, `PREDICATE R76-C1 pass`.
- control (`c1-control-declared.txt`): `PROVINCE_REV fda63968`, `CONTROL-SKIP rows=11
  disagreements=1 target_reached=False` — a declaration-trusting counter cannot reach `disagree=0`.

**R76-C2.** `python3 plans/round76_c2_defect_discharge.py --lane .`
- before (`--rev fda63968`, `c2-before.txt`, rc 1): `SCOPE ids=7 registered=0 closed=0 open=7
  discharged=0 legs_passed=0 legs_pending=2 wrong=13`, seven `LEDGER … MISSING-ROW`, `PREDICATE
  R76-C2 fail`.
- after (`c2-after.txt`, stamped `a47a5530`, rc 0): `SCOPE ids=7 registered=7 closed=7 open=0
  discharged=7 legs_passed=7 legs_pending=0 wrong=0`, `PREDICATE R76-C2 pass`; ledger lines name
  `close_commit=6977019bdf56` (D1–D4, D7) and `f0d5232208d4` (D5, D6), each with
  `evidence_path`/`evidence_literal` read from that commit's tree.
- control (`c2-control-status.txt`): `rows_claimed_closed=7 trivial_checks=1 failed_legs=3` — a
  status-only skip cannot reach the target.
- Amendments: A1 (Before prose → receipt), A2 (`emit --work`), A3 (control revision), A4 (whole-row
  stale scan, before re-measured), A5 (confinement/manifest + evidence-at-close), A6 (burn-down
  provenance), A7 (prior art + round-51 repair), A8 (`NEGATED-DISCHARGE`; C1 claim scoped to the
  `## Surfaces` table), A9 (`EMPTY-SCOPE`, rendered-text legs, `LEG-PENDING`). Predicate, target, control and kill rules never moved;
  A4/A5/A8/A9 only add defect classes (harder), and the before was re-measured under the final rule.

**Capability rows** (SCORECARD §Round-76 capabilities): `province-surface-resolver-table-anchored`
(increment of round 51) and `routed-defect-discharge-binding`.

**Census.** `sources-census.sh validate --root … kengaku` → rc 0 at both ends; rows 243 → 244, tiers
A 214 / B 24 / C 6, 25 `W04` duplicate-URL warnings unchanged (`census-before.txt`,
`census-after.txt`).

**Registered gates at the landing tip** (`a47a5530`, clean clone): `R76-C1 pass`, `R76-C2 pass`,
`R51-C1 pass`, `R75-C1 pass` (74/125/67, 0 missing), `R74-C1 pass`, `R74-C2 pass`; `routed_open.py`
`ROWS total=86 open=31 blocked=1 closed=52 refused=2`, `--selftest 12/12`.

## Sources & frontier

- `SOURCES.md` rows **243 → 244** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`),
  rc 0 both ends. Rows added by tier: **A +1** (S252, Git `git-merge-base` docs), B +0, C +0. Rows
  touched old→new: **S252 absent → `mined`** (opened 2026-11-04, recheck `on-release`, used-by
  `corpus/lessons/round-76.md, plans/round-76-claims.md`). Re-verified this round: S251 (round 75) not
  re-opened; no row changed status other than S252.
- S252 was re-fetched by seat `ScribeSourcesR76`: HTTP 200, 41 397 B, sha256 identical to the capture,
  `cmp` identical; quote at line 1703, 25 words.
- **Rejected row:** "a commit id in a row's `close` text proves the discharge is on the branch" — flip
  recorded in the lesson's Gate block. **Rejected row:** "a declaration is evidence of resolution" —
  flip is the `AGREE` leg.
- Frontier: no new frontier ground entered; the round repairs/deepens two instruments.
  `corpus/README.md` §Frontier items are untouched.
- **Assimilation: none.** `/home/vgpnk/Projects/shokuknow/merge/kengaku/` is present but unadopted; the
  scout measured 175 staged rows against the lane's 244-row registry with **167 id collisions** (only
  S087–S099 subset and S235 free) and 61 of 65 staged knowledge targets absent — adoption needs
  re-iding, which the frozen scope does not fund this round. Open L0 `kengaku | round-54` carried.
- `considerthese/`: the latest file (`2026-10-26.md`) has **no still-unimplemented proposal** — proposal 1
  was implemented in round 41 (`plans/routed_open.py`); R76-C2 extends it (seven rows, evidence-at-close
  legs). Recorded in the lesson's appended correction; no proposal mined this round.

## Trend verdicts

- **expansion: improved.** Two capability rows entered `SCORECARD.md` (`province-surface-resolver-table-anchored`,
  `routed-defect-discharge-binding`) and the SOURCES registry gained S252; **no knowledge entry was
  admitted** and the resolver is an increment of round 51's, said plainly rather than sold as new.
- **quality: improved.** Three registered gates that were red at base are green at the tip
  (`R51-C1` unrecovered-row repair, `R74-C1` unregistered-instrument repair, `R75-C1` index drift),
  the PROVINCE registry count is re-pinned to the census, and both new counters carry selftest, mutant,
  git-state and skip-control batteries with zero survivors.
- **discernment: improved.** Seats falsified both claims with executable counterexamples (scope shrink,
  anchor/endpoint substitution, destination escape, brace bomb, close-commit-without-evidence,
  control-not-replayable, mis-frozen Before), and every one became a committed amendment or a stated
  limit — none was smoothed. The outside closure's agreement is not yet on record; that duty is the
  non-author spot-check's.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md`
  (two new gate rows; corrected round-75 rows).
- `[~]` At least one end-to-end domain task executed and logged — `LOG.md` round-76 entry; both gates
  run on a clean clone at the tip.
- `[~]` Instructions executable by an agent without oral context — `plans/round-76-claims.md` (frozen
  sentences, amendments A1–A9) plus the counters' `--selftest`.
- `[~]` No cross-domain bleed — `PROVINCE.md` §Refusals unchanged; the connector's sibling inventory is
  reported out (`ConnectorR76` finding 2), not absorbed.

## Round shape, seats, dead seats

One v1 wave (`w1`, policy band 8–16, `maxLanes` 14), validated `rc=0` (`.ufo/waves/round-76/w1/w1-validate.rc`)
and dispatched inline through `.ufo/waves/round-76/w1.ready`.

| role | seats | names |
|---|---|---|
| executor | 4 | `C1ReplayR76`, `C2ReplayR76`, `ReceiptMintR76`, `LabratR76` |
| scribe | 3 | `ScribeCorrectionsR76`, `ScribeSourcesR76`, `ScribeLessonR76` |
| scout | 1 | `ScoutFrontierR76` |
| connector | 1 | `ConnectorR76` |
| reviewer | 2 | `ReviewerC1R76`, `ReviewerC2R76` |
| critic | 1 | `CriticR76` |
| mutation-tester | 1 | `MutantR76` |
| sentinel | 1 | `SentinelR76` |

Attack roles (reviewer, critic, mutation-tester) = 4/14 = 28.6 % (≥25 %); connector 1 (≤2). The
`labrat` role is not a swarm role (the validator refuses it), so the H1 probe rides executor seat
`LabratR76`, which held the one permitted read-only labrat spawn. **Dead seats: 0** — `w1-results.json`
records 14 settled seats, every one with non-empty output; no seat died and no slot was left unfilled.



**Misroot sweep (before filing).** `git -C /home/vgpnk/Projects/shokunin status --porcelain -uall |
grep -iE 'kengaku|round-?76'` → one match, this report (`?? .ufo/reports/round-76/kengaku.md`), which is
the file being committed — no seat wrote into the fleet root. The other untracked entries (`.scratch/*`,
`after`) are orchestrator-owned run state, not seat output; nothing was copied or deleted.

## Stale-lane

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Tool installs

None. No package manager ran; no tool was installed or upgraded.
