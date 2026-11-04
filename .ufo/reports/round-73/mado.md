# mado — round 73 (hyaku run 15, attempt 1)

lane: mado · repo: `mado-shokunin` · base `d3f6c9f5d8b3401c01f189e8cd4b8dbc917a2bce` ·
lane tip **`422ba69ae597f5bc81ae8bc7b8b7be45b748e988`** (pushed; `git ls-remote origin
refs/heads/master` prints it) · round shape: ONE v1 wave, 13 seats, 13 settled, 0 dead · round
total 13.

Declared claims (frozen at `87e4c61a`, before any candidate data):

- **C1 · calibration** — the frozen outcome case set separates four named mutations of the
  landing outcome rule; the held round-72 eight-case set separates two. **Verdict: improved**
  (`killed=4 base_killed=2`, TARGET_MET).
- **C2 · operability** — the guard census counts the `global`-declared guard and the mutated
  `os.environ` transport; the held round-71 classifier misses exactly those three cases.
  **Verdict: improved** (`controls=28/28 base_controls=25/28`, TARGET_MET).

Neither claim touches a desktop, compositor, service, session or sibling surface; no tool was
installed or upgraded; no pacman transaction ran.

## Work performed

1. **Freeze before data.** Two control sets, a two-claim declaration with predicates, counting
   commands, kill rules, targets and limits, and a pre-freeze do-nothing baseline produced by an
   uncommitted prototype — all committed before any instrument existed
   (`87e4c61a`; `.ufo/waves/round-73/claims-declaration-r73.md`,
   `controls/c1-outcomes-r73.json` sha256 `263b3c5a…`,
   `controls/c2-cases-r73.json` sha256 `65e94644…`, `control-baseline-r73.txt`,
   `proto/held-r73.py`). The baseline showed the held denominators miss the targets
   (held set kills 2/4; held classifier 25/28).
2. **C1 instrument.** `quality/counters/c1-r73-summary-mutants.py` extracts the round-72 outcome
   harness at `--rev`, asserts the eight held cases are carried byte-identically, applies four
   named literal mutations exactly once each (N1 the dropped `n > 0` guard, N2 the pre-repair
   prefix parse, N3 the relaxed comparison, N4 the kill-count-only verdict) and scores each on
   the ten-case set and the held eight-case set. Selftest 26/26.
3. **C2 instrument.** `quality/counters/c2-r73-shapes.py` is the round-71 guard census plus two
   carriers: a `global`-declared store handed as `env=`, and `os.environ[KEY] = "1"` before a
   launch whose `env=` copies the environment (`{**os.environ}`, `dict(os.environ)`). Twenty-eight
   frozen cases (23 carried byte-identically from round 71); population unchanged. Selftest 78/78.
4. **Measurement at the instrument commit `1459cca1`, re-measured at the repair commit
   `84fc266a`.** `measurement-c1-r73.txt` / `measurement-c2-r73.txt` carry the per-mutant and
   per-case lines plus the contract line; both `TARGET_MET`, rc 0.
5. **Curation (frontier step).** Three rows opened this round with three byte-identical fetches
   each — S447 (the `global` statement), S448 (`os.environ`), S449 (`subprocess.run` `env`). Two
   knowledge entries admitted, one lesson with `## Mistakes` and `## Gate`, two QUALITY
   criteria (118–119), README index 87 → 89, PROVINCE round-73 refinement, ledger 125 → 127,
   two SKILL Gate-registry rows.
6. **Wave (13 seats, one v1 wave).** Roles: executor 3, scribe 3, scout 2, reviewer 2, critic 1,
   mutation-tester 1, connector 1 — attack share 4/13 = 30.8 %. The L1 holds the planner seat (the
   validator rejects `planner`); no planner was dispatched. Per-seat deliverables below.
7. **Review-driven repair at `84fc266a`.** The wave's two reviewers and the critic found five
   defects; all repaired without touching a frozen predicate, label, control set, kill rule or
   target, with red-before/green-after receipts and two new selftest regressions per claim family
   (see *Landed changes* and the declaration's erratum E2).
8. **Harm watch at the content tip `fb8a3df6`** (`.ufo/waves/round-73/receipts/harm-watch-r73.txt`,
   each line carrying the command's own rc).

### Wave seats — what each delivered

| seat | role | deliverable | outcome |
|---|---|---|---|
| R73ExecC1 | executor | `.ufo/waves/round-73/w1/R73ExecC1/R73ExecC1.md` (120 L) | drove the frozen C1 command and selftest; reconciled with the receipt |
| R73ExecC2 | executor | `w1/R73ExecC2/R73ExecC2.md` (122 L) | drove the frozen C2 command and selftest; four independent snippets |
| R73ExecBattery | executor | `w1/R73ExecBattery/{R73ExecBattery.md,harm-watch-r73.txt}` | six-command harm watch with per-command rc |
| R73ScribeEntryC1 | scribe | `w1/R73ScribeEntryC1/draft/corpus/knowledge/control-set-mutant-kill-r73.md` (158 L) | draft entry; battery path and marginal-kill framing corrected mid-round |
| R73ScribeEntryC2 | scribe | `w1/R73ScribeEntryC2/draft/corpus/knowledge/guard-carrier-global-environ-r73.md` (159 L) | draft entry; provenance of the uncommitted receipts flagged correctly |
| R73ScribeLesson | scribe | `w1/R73ScribeLesson/draft/corpus/lessons/round-73.md` (91 L) + `gate-block.md` | draft lesson with Gate placeholders |
| R73ScoutSources | scout | `w1/R73ScoutSources.md` + `R73ScoutSources/fetch/*` (3 × 3 fetches) | quotes with line ranges and word counts |
| R73ScoutFrontier | scout | `w1/R73ScoutFrontier/R73ScoutFrontier.md` (200 L) | census, frontier items, considerthese pointer, id precondition |
| R73RevC1 | reviewer | `w1/R73RevC1/R73RevC1.md` (76 L) | **F1** missing `--controls` (reproducibility), **F2** `--base-rev` displayed not used, F3 lineage/wideness note |
| R73RevC2 | reviewer | `w1/R73RevC2/R73RevC2.md` (74 L) + five original fixtures | **F1** parameter shadow, **F2** over-broad cancellation, **F3** `del os.environ[KEY]`, F4 line-order limits |
| R73CriticClaims | critic | `w1/R73CriticClaims/R73CriticClaims.md` (59 L) | attacked both claims' receipts and do-nothing legs |
| R73MutBattery | mutation-tester | `w1/R73MutBattery/R73MutBattery.md` (149 L) | independent mutants of both counters (in-place copies, no git writes; the seat's conservative reading is recorded) |
| R73ConnSiblings | connector | `w1/R73ConnSiblings/R73ConnSiblings.md` (71 L) | sibling scan + corrected premise about `mado-verify.sh` (M73-4) |

No seat died and no seat was empty. All 13 wrote inside their own directory (the flat `Report:`
trailer is a path convention; the write bound held).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| frozen declaration, both control sets, the do-nothing baseline, the prototype | round-73 entry, first bullet | `87e4c61ac90e9ac587c9f65ac7844ded268d9046` |
| both counters, their ledger rows and Gate-registry rows | round-73 entry, instruments/registry bullets | `1459cca11fb5d3956a6e9a128217852dd0c28cb9` |
| receipts, three source rows, two knowledge entries, lesson, README/PROVINCE/QUALITY/SCORECARD/LOG records | round-73 entry, curation/knowledge bullets | `fb8a3df68ce026768bd5794c9ddca2dc99238b7c` |
| the reviewers' repairs (C1 base-rev leg + usage example; C2 scope-shadow, cancellation-scope, key-deletion) | round-73 entry, appended repair bullet | `84fc266a5bf6db6cf12b6aa6106ad33121f391be` |
| wave evidence (spec, dispatch, 13 seat dirs, results), re-measured receipts, erratum E2, lesson addendum | round-73 entry, wave bullet | `422ba69ae597f5bc81ae8bc7b8b7be45b748e988` |

`LOG.md` carries the round-73 entry; every change above is named in it. The declaration's
erratum E1 (the printed command's missing `--controls`) and E2 (the five review repairs) are
append-only in the same file.

## Before → after measurements

**C1 — calibration.** Command (verbatim; `REV` = `84fc266a5bf6db6cf12b6aa6106ad33121f391be`):

```sh
python3 -I quality/counters/c1-r73-summary-mutants.py --repo . --rev 84fc266a5bf6db6cf12b6aa6106ad33121f391be \
  --base-rev d3f6c9f5d8b3401c01f189e8cd4b8dbc917a2bce \
  --controls .ufo/waves/round-73/controls/c1-outcomes-r73.json --scratch-root DIR
```

Before: the held round-72 eight-case set separates `killed=2/4` (N1 and N2 survive;
`control-baseline-r73.txt`), bounded score 5.0000. After: `cases=10 mutants=4 killed=4
base_killed=2 verdict=TARGET_MET` rc 0, bounded 10.0000. `zero-denominator` is N1's only
separator and `valid-then-garbled` N2's only separator. Measured at `84fc266a`; identical counts
at `1459cca1` (`measurement-c1-r73.txt`, both runs).

**C2 — operability.** Command:

```sh
python3 -I quality/counters/c2-r73-shapes.py --repo . --rev 84fc266a5bf6db6cf12b6aa6106ad33121f391be \
  --base-rev d3f6c9f5d8b3401c01f189e8cd4b8dbc917a2bce \
  --controls .ufo/waves/round-73/controls/c2-cases-r73.json --scratch-root DIR
```

Before: the held round-71 classifier scores `25/28`, missing exactly `global-rebind-guard`,
`environ-splat-guard`, `environ-call-guard` (`control-baseline-r73.txt`), bounded 8.9286. After:
`population=20 readers=13 guarded=13 unguarded=0 controls=28/28 base_controls=25/28
verdict=TARGET_MET` rc 0, bounded 10.0000. Measured at `84fc266a` (`measurement-c2-r73.txt`).

**No-harm rows** (measured at `fb8a3df6`, `receipts/harm-watch-r73.txt`): gate
`MADO_SELFTEST: 460/460`; index `89/89`; ledger `127/127 uncovered=0`; axis
`checked=3 mismatched=0`; census exit 0; five frozen instruments byte-identical base → tip.

## Sources & frontier

Census command (frozen):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado
```

- Round start: **383 rows, exit 0** (no E-findings; held W04 warnings only).
- Round end: **386 rows, exit 0**; three new W04 warnings, one per new row (each shares its
  document with a held row at a different scope: S447/S440, S448/S113, S449/S442).
- Rows added by tier: **A/docs ×3, status `mined` ×3** (S447 `simple_stmts.rst` `global`,
  S448 `os.rst` `os.environ`, S449 `subprocess.rst` `env`).
- Rows touched old→new: none of the held rows changed any cell; only the three new rows entered.
  (Round 72's S444/S445/S446 stand unchanged.)
- Frontier rows advanced: the round-72 frontier bullet's "control set blind spots" line (GAP-1,
  the F1 parse) is now load-bearing cases in
  `corpus/knowledge/control-set-mutant-kill-r73.md`; the guard-census frontier (the r71 plan's
  widening) is entered by `corpus/knowledge/guard-carrier-global-environ-r73.md`. Still open and
  named in README: the stale/replay class, the `summary_fraction()` ambiguity, the line-order
  approximation, and the r72 `score()` None-guard (no absent-candidate case in either frozen set).
- `Assimilation: none` — `considerthese/` was mined by `R73ScoutFrontier` for a next-round
  candidate; no `merge/mado/` package entry was adopted (this round's claims are instrument work,
  and the package's material is domain ground for a later assimilation round).
- Registry cell changes and the Gate quotes (URL, access date, ≤25-word located quote) are in
  `corpus/lessons/round-73.md` `## Gate`.

## Trend verdicts

- **expansion: improved** — one admitted entry on ground the coverage map did not hold (the
  control set as a measured instrument) citing held `mined` rows and the lane's own re-runnable
  receipts, and one entry extending held carrier ground; both indexed. The frontier bullet in
  `corpus/README.md` moves the r72 blind spots from prose to cases. (The carrier entry is an
  extension of S-file ground already held, so it counts as quality, not expansion.)
- **quality: improved** — the census rule was repaired by review and re-verified (three fixtures
  flip, selftest 78/78), the outcome counter gained a real base-rev leg, both claims re-measured
  identically after repair, and no admitted entry was found false; the five frozen instruments
  are byte-identical base → tip.
- **discernment: improved** — the reviewers' five defects became four `## Mistakes` rows and two
  grounded QUALITY criteria (118, 119) plus three selftest regressions; the outside spot-check of
  this round's three admits is the closure's (LEARNING.md), so the outside half is pending, not
  claimed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the two new Gate-registry rows and the two entries extend it; outside-lane independence not established here (`.ufo/waves/round-73/claims-declaration-r73.md`, `SKILL.md` Gate registry).
- [~] At least one end-to-end domain task executed and logged — the two frozen counting commands ran end to end at two commits with receipts (`.ufo/waves/round-73/measurement-c{1,2}-r73.txt`); no desktop/compositor task this round.
- [~] Instructions executable by an agent without oral context — the wave's 13 seats executed from the declaration and the wave context alone; outside-lane independence not established (`.ufo/waves/round-73/w1-results.json`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round-73 refinement adds two counters and no config/compositor surface (`PROVINCE.md` round-73 block); no outside-lane approval claimed.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none (no package, tool or service was installed or upgraded this round).
Inherited state: the lane tree was clean at freeze (`tracked=0 untracked=0`); no inherited
uncommitted lane files. Fleet-root sweep: the only untracked fleet-root files are `.scratch/*`
(orchestrator-owned) and `after` (24 B, dated 2026-11-03 20:05, before this launch, naming no
lane or round) — no mado round-73 misroot. Non-author closure owns admission, the no-harm
judgment and promotion.
