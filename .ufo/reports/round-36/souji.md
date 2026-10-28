# souji — round 36 report

author: souji L1 (SoujiR36) · lane `/home/vgpnk/Projects/shokunin/souji-shokunin` · base
`94b5e96ab72b40622449af2dfe7c5b6d73118176` · freeze `42ea92e999cd8f1a01d2c28f5f7c9b884321ef78`
· C1 landing `af7d51a180eaf2424e064e8e9f19085beff3637e` · round landing `007ab539df228d760d176ba95ae73e799b27143a`
(and later commits named where they carry a claim) · fresh-start round (r30–r35 closures rejected).

## Work performed

Declared claims (frozen in `census/round-36/preregistration.txt` before any after-data, with four
tighter-only amendments A1–A4 each recorded after the wave seat that produced it):

- **C1 — calibration (score 7, the lowest non-retired axis).** The coverage map must name every
  `ground: F<k>` knowledge entry at the landing revision, and every backticked entries-column path
  must resolve there (the second clause carried by a named strict probe, see below). Counter:
  `tools/souji-coverage-agreement.py --rev <landing> --base-rev <base>`.
- **C2 — operability (score 8).** The pre-report gate must enforce the round-report contract in
  seven new predicates (canonical section order, one SHONEN line per box, one verdict line per
  trend, the stale-lane line, a measurement row with a command and a measured commit, 1–3 claim
  ids, an evidence pointer) and a fixture must prove each predicate discriminates. Counters:
  `tests/fixtures/r36-report-gate.py`, the frozen r27 regression.
- **C3 — coverage (score 8, capability acquisition).** F1's fleet worktree-registration numerator
  becomes a re-runnable surface: `tools/souji-worktree-drift.py` re-measures every repository a
  committed census record names, read-only, and reports the drift; its run against the committed
  r35 record must reproduce the r35 spot-check's corrected numerator and name the record's four
  phantom paths. Counters: `tests/fixtures/r36-worktree-drift.py`, the live run.

Work items (each with its evidence pointer):

- **C1 instrument and control.** `census/round-36/records/c1-control-base.txt` — the do-nothing
  reading `grounded=19 mapped=18 dangling=0 mismatches=1`, rc 1 (MISSING-FROM-MAP
  `corpus/knowledge/fleet-prune-numerator-r35.md`, `ground=F1`, `map_rows_F1=2`).
- **C1 landing.** `corpus/README.md` at `af7d51a`: the F1 coverage-map row names the r35 numerator
  entry; the F1 `## Frontier` bullet records the numerator held (2026-10-28) and re-runnable.
- **C1 after + kill arm.** `census/round-36/records/c1-after.txt`:
  `grounded=19 mapped=19 dangling=0 mismatches=0 kill_tested=19 kill_violations=0`, rc 0.
- **C1 strict arm.** `census/round-36/records/c1-strict-paths.txt`: every backticked
  entries-column `knowledge/` span in all 28 map rows resolves (`distinct=27 missing=0
  nested_entries=0`, rc 0) — the clause the counter's basename-only check does not test
  (wave seat SwarmCritic07 W2/W3).
- **C2 instrument.** `tools/souji-report-contract.py` (new; seven predicates, `--selftest` 9 cases)
  and `tools/souji-pre-report-gate.sh --contract` (predicate 6; without the flag the run prints
  `check-report-contract=SKIPPED (no --contract)` so the omission is visible).
- **C2 control.** `census/round-36/records/c2-control-base.txt`: the base revision has no checker
  (`git cat-file -e` rc 128) and the base gate scores the same fixture `cases=11 pass=0 fail=11`.
- **C2 discrimination on real reports.** `census/round-36/records/c2-filed-reports.txt`: the
  checker flags the filed r35 report on `sections`, `trends`, `stale-lane` and `measurements`
  (4/7) — exactly the defect set the r35 spot-check recorded by hand; wave seat SwarmExecutor16
  re-ran r20–r35 and found every recorded defect class flagged and none unflagged.
- **C2 after.** `census/round-36/records/c2-after.txt`: `cases=21 pass=21 fail=0
  control=STUB-REJECTED`, r27 regression `cases=4 pass=4 control=FALSE-GREEN-REJECTED`, selftest
  9/9, and all five measured mutants dead on a named case.
- **C3 instrument.** `tools/souji-worktree-drift.py`: record parser with typed refusals
  (`RECORD-MISSING`/`RECORD-MALFORMED`/`RECORD-EMPTY`, TOTAL-vs-REPO consistency), per-repo
  read-only measurement (`worktree list --porcelain`; `worktree prune --dry-run -v`, candidates
  counted from **stderr** — the r35 record counted stdout), drift classes
  REGS-CHANGED/PRUNABLE-CHANGED/ABSENT/UNREACHABLE/UNRECORDED, `--timeout`, `--json`.
- **C3 control.** `census/round-36/records/c3-control-base.txt`: the tool is absent at the base
  revision (`git cat-file -e` rc 128).
- **C3 first live run.** `census/round-36/records/c3-live-run.txt`: `record_repos=26 record_regs=27
  record_prunable=0 live_repos=22 live_regs=23 live_prunable=1 drift_rows=5 unreachable=0`, with
  ABSENT exactly `ok`, `research`, `scripts`, `templates` — the four phantom paths the r35
  spot-check named — plus `PRUNABLE-CHANGED mado-shokunin record=0 live=1`.
- **C3 after.** `census/round-36/records/c3-after.txt`: fixture `cases=12 pass=12 fail=0
  control=STUB-REJECTED`; live run unchanged at the landing tip.
- **Frontier step.** `census/round-36/sources/` holds the two fetched snapshots; `corpus/SOURCES.md`
  gained S233 (bash, mined), S234 (GNU grep 3.12, mined) and S235 (the agent-shell `grep` builtin,
  rejected); three rejected rows' `used-by` cells were corrected old→new
  (`corpus/lessons/round-36.md` `## Registry corrections`); the round lesson carries `## Gate`
  (URL, access date, located quote) and two `## Mistakes` rows plus a third recorded in the report.
- **Repairs after wave-1 attacks (amendments A1–A4).** A1: the checker raised `IndexError` on an
  empty code span (SwarmExecutor17) → guarded, selftest 8→9. A2: the gate's contract verdict was
  rc-only (SwarmCritic19 H3) → binds on rc **and** the absence of a printed `=FAIL`, and forwards
  the checker's `SUMMARY`/`ERROR` lines; the drift tool refused `--json` inside the measured root
  and scrubbed `GIT_TRACE*`/`GIT_FLUSH` (SwarmSentinel24 F1/F2). A3: `sections` became
  fence/comment-aware and exact-normalized at `##` depth (SwarmReviewer09 accepted a fully fenced
  report), and the fixture gained isolated cases killing five measured mutants
  (SwarmMutationTester13/14). A4: `live_repos` could go negative (SwarmExecutor22 F1). A5: a
  vacuous checker (prints nothing, exits 0) read as a pass and the forwarded lines shared the gate's
  `check-*` namespace (SwarmExecutor15) → the verdict now also requires at least one checker line and
  forwarded lines are prefixed `contract-`, with a second fixture control
  (`control=VACUOUS-CHECKER-REJECTED`). A7: the trend verdict is now the first token after its
  label, not any verdict word in the line ("expansion: not improved" scored as improved;
  SwarmConnector39) → fixture 21 cases.
- **QUALITY bar.** Three criteria appended with their witnesses: Q80 (a claim clause must name the
  code path that tests it), Q81 (a staged mirror copies bytes, never links), Q82 (a counter whose
  subject can be removed must be run with its base-rev kill arm).
- **Hygiene census.** Wave seat SwarmExecutor36 / `HygieneW2` (see the wave reports) — the lane's
  stray top-level files, `__pycache__` and wave-evidence tracking status are recorded there; nothing
  was deleted.
- **Incident (disclosed).** Wave seat SwarmExecutor35's symlinked scratch mirror followed the link
  and overwrote `corpus/SOURCES.md` for ~1.5s; the seat restored it and `cmp`-verified, and the L1
  re-verified the registry (159 rows, md5 `fc60f0119d2793e1a5c8e42760594caf`, census exit 0). The
  class is QUALITY Q81; the seat's own report is `.ufo/waves/round-36/w1/SwarmExecutor35.md`.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| freeze: instruments, fixtures, preregistration, controls, source snapshots | `Round36` (freeze bullet) | `42ea92e999cd8f1a01d2c28f5f7c9b884321ef78` |
| C1 landing: F1 map row + frontier bullet | `Round36` (C1 bullet) | `af7d51a180eaf2424e064e8e9f19085beff3637e` |
| C2/C3 instruments after A1–A4, receipts, SCORECARD rows, QUALITY Q80–Q82, lesson, SOURCES rows + registry corrections, SKILL registry rows | `Round36` (C2/C3/frontier bullets) | `007ab539df228d760d176ba95ae73e799b27143a` |
| lesson rebuilt in full after a truncated write (recorded in `## Mistakes`) | `Round36` (Mistakes bullet) | `92a65fa169158c6a470bbde8175d9caad59df436` |
| A5 (vacuous checker, forwarded-line namespace), SCORECARD supersessions, census before/after receipt | `Round36` (C2 bullet) | `bc9a3bbbe2d66940ebf67eb99f37b4a28d467811` |
| A7 (trend-verdict parsing), refreshed C2 receipt, SCORECARD supersession counts, LOG entry | `Round36` (C2 bullet) | `1e771ed59301ed10f68e22d4edf35d5218bacf1a` |
| wave evidence and the final receipts | `Round36` (waves bullet) | committed with the final landing commit |

## Before → after measurements

| claim | axis | before | after | counting command | measured commit |
|---|---|---|---|---|---|
| C1 coverage-map binding | calibration 7 | `grounded=19 mapped=18 dangling=0 mismatches=1`, rc 1 (`census/round-36/records/c1-control-base.txt`) | `grounded=19 mapped=19 dangling=0 mismatches=0 kill_tested=19 kill_violations=0`, rc 0, and the strict arm `distinct=27 missing=0 nested_entries=0` (`census/round-36/records/c1-after.txt`, `c1-strict-paths.txt`) | `python3 -B tools/souji-coverage-agreement.py --root . --rev <landing> --base-rev 94b5e96ab72b40622449af2dfe7c5b6d73118176` | `af7d51a`; re-read at `1e771ed` |
| C2 report-contract gate | operability 8 | no checker at base (`git cat-file -e 94b5e96:tools/souji-report-contract.py` rc 128); base gate `cases=11 pass=0 fail=11` (`census/round-36/records/c2-control-base.txt`) | `cases=21 pass=21 fail=0 control=STUB-REJECTED` + `control=VACUOUS-CHECKER-REJECTED`, rc 0; r27 `cases=4 pass=4 control=FALSE-GREEN-REJECTED`, rc 0; selftest 9/9; five mutants dead on named cases (`census/round-36/records/c2-after.txt`) | `python3 -B tests/fixtures/r36-report-gate.py`; `bash tests/fixtures/r27-pre-report-gate.sh` | `1e771ed` |
| C3 F1 drift surface | coverage 8 (capability acquisition) | tool absent at base (`git cat-file -e 94b5e96:tools/souji-worktree-drift.py` rc 128, `census/round-36/records/c3-control-base.txt`) | `cases=12 pass=12 fail=0 control=STUB-REJECTED`, rc 0; live `record_repos=26 record_regs=27 record_prunable=0 live_repos=22 live_regs=23 live_prunable=1 drift_rows=5 unreachable=0`, ABSENT set exactly `ok,research,scripts,templates` (`census/round-36/records/c3-after.txt`) | `python3 -B tests/fixtures/r36-worktree-drift.py`; `python3 -B tools/souji-worktree-drift.py --root /home/vgpnk/Projects/shokunin --record census/round-35/records/prune-census.tsv --timeout 20` | `1e771ed` |

## Sources & frontier

- Census before → after: `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`
  — before (round start, 2026-10-28): 156 registry rows, exit **0** (W04 duplicate-URL warnings
  only); after: 159 rows, exit **0**. Counting command:
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 156 → 159.
- Rows added by tier: **A: 2** (S233 Bash Reference Manual — Bash Conditional Expressions, mined;
  S234 GNU Grep 3.12 manual § 2.3 Exit Status, mined), **C: 1** (S235 the agent-shell `grep`
  builtin pi-uu-grep 0.2.0 — rejected: undocumented, and no lane tool executes it).
- Rows touched old→new (rule 2, `used-by` only): S090 `corpus/lessons/round-20.md` → `—`; S097
  same → `—`; S127 `corpus/knowledge/git-repo-structure-common-dir.md` → `—`. Logged in
  `corpus/lessons/round-36.md` `## Registry corrections`; census exit 0 afterwards.
- Frontier rows advanced: **F1** — the numerator re-census is recorded as held
  (`knowledge/fleet-prune-numerator-r35.md`, 2026-10-28) and F1 now has a re-runnable surface
  (`tools/souji-worktree-drift.py`, capability row in `SCORECARD.md`); the r35 record's two
  counting defects are reported, not rewritten. F2/F3/F4 unchanged.
- Sourced claim: **C2** rests on S233 (the gate's non-empty-report predicate is bash `-s`) and S234
  (its `grep -c` heading counts read GNU grep's exit-status contract) — both opened this round.
- `Assimilation: none` — this is a fresh-start round restricted to claims a do-nothing control
  cannot reach; no `merge/souji/` theme was adopted and no package row was appended.
- `considerthese/` does not exist in this lane (`ls` → No such file or directory; wave seat
  SwarmScout37), so no proposal was mined.

## Trend verdicts

- expansion: improved — F1 gained a re-runnable surface and a dated numerator
  (`tools/souji-worktree-drift.py`, `census/round-36/records/c3-after.txt`) plus two mined sources
  S233/S234 and three QUALITY criteria Q80–Q82 with running witnesses.
- quality: improved — three instruments were re-verified against named wave attacks and repaired
  (A1–A4), the report gate now flags the exact r35 report defects, and every mutant the wave
  measured now dies on a named fixture case (`census/round-36/records/c2-after.txt`).
- discernment: improved — the round's own prose was caught wider than its counter (Q80), a false
  green was found and answered by a second named probe (`c1-strict-paths.txt`), and the r35 Gate's
  missing quote/access records were repaired with re-opened sources.

## SHONEN

`SHONEN.md` is unchanged this round; no box earns `[x]` (a `[x]` needs a named non-author verifier,
and the round's non-author closure has not run yet). One line per box of `SHONEN.md`:

- [~] SKILL.md decision tables / error patterns / checklists with cited sources — `SKILL.md` `## Gate registry` now carries five r36 rows (`souji-report-contract`, `r36-report-gate`, `r36-worktree-drift`, `souji-worktree-drift`, and the `--contract` clause on `souji-pre-report-gate`), each with its entry command, verdict map, self-test and write scope; every row's command was run this round.
- [~] At least one end-to-end domain task executed and logged — the F1 numerator re-derivation: `census/round-36/records/c3-live-run.txt` reproduces the corrected 22-repository / 23-registration numerator and localizes the r35 record's four phantom paths and its stdout-counting defect.
- [~] Instructions executable by an agent without oral context — the three instruments are exercised only by committed commands (`census/round-36/records/c2-after.txt`, `c3-after.txt`, `c1-after.txt`), and the preregistration names each counter with its target and kill rule.
- [~] No cross-domain bleed (PROVINCE.md accurate) — C1–C3 stay inside repo/workspace hygiene (coverage map, report gate, worktree-registration census); wave seat SwarmConnector29 found no sibling lane owning the F1 census and the fleet-root overlaps are operator surfaces, reported not absorbed.

## Waves and round shape

- **Shape:** two v1 waves under `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy.json`
  (band 32–64), one batched dispatch each, inline via the orchestrator's ready-file handoff.
- **w1 (build + first falsifiers): 39 seats** — 12 executor, 6 reviewer, 5 scout, 5 scribe,
  3 critic, 3 mutation-tester, 2 sentinel, 2 connector, 1 revenger (30.8 % attack roles).
  38 of 39 seat reports landed under `.ufo/waves/round-36/w1/` before this report was filed;
  `SwarmReviewer20` (registry-schema audit) and `SwarmConnector39` (cross-claim scan) ran long and
  `SwarmConnector39` landed late in the round. The wave's `-results.json` handoff had not arrived
  when the report was filed (the operator's budget stop pre-empted the wait), so seat status here
  comes from the committed report files, not the results manifest; no seat is reported dead.
- **w2 (falsify + independent re-measurement): 32 seats** — 11 executor, 8 reviewer, 5 critic,
  2 mutation-tester, 2 scribe, 1 sentinel, 1 connector, 1 revenger, 1 simplifier (47 % attack
  roles). Spec validated and rendered (`w2-spec.json`, `w2-dispatch.json`), `w2.ready` written;
  the launcher had not yet taken it when the report was filed, so **no w2 report exists yet** and
  no w2 claim is cited anywhere in this report.
- **Round total: 71 seats**, inside the 64–128 band and far under the 256 ceiling.
- The §3 L2 floor is met inside w1 (39 ≥ 8, one batched call); the canonical planner seat is held
  by the L1 (the validator rejects a planner role).

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. Age from launch: this round began
2026-10-28 with the round-36 prompt and is still progressing at filing (commits `42ea92e`, `af7d51a`,
`007ab53` inside the lane).

---

## Erratum (appended after filing; supersedes nothing above)

- **Wave evidence is not committable in this lane.** `.ufo/waves/` is listed in
  `souji-shokunin/.gitignore:1`, so `jj-lane.sh commit -- .ufo/waves/round-36` prints
  `nothing to commit` and `git ls-files .ufo/waves/round-36` prints 0. The specs, dispatch
  payloads, ready markers and 38 seat reports exist only in the working tree under
  `/home/vgpnk/Projects/shokunin/souji-shokunin/.ufo/waves/round-36/`. Earlier rounds carry a few
  tracked files there (round-35: 8), so the ignore line and the tracked legacy disagree; this is
  reported as a conformance gap, not repaired (`.gitignore` is not this round's write scope).
- **Final lane tip cited above:** `1e771ed59301ed10f68e22d4edf35d5218bacf1a`, confirmed equal to
  `git ls-remote origin refs/heads/master` immediately before the report commit
  `1eb8632a0a7719e8f45061f0f913be391b615c07`.
