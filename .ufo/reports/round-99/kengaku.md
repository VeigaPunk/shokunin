# kengaku — round 99 (hyaku run 15, attempt 1)

## Work performed

Declared claims (frozen at F `24a5a5554130065917d55618ae10309403abf60d`, `plans/round-99-claims.md`):

- **R99-C1 — coverage** (the lowest non-retired axis, L0 cap 7). A seventeenth located offline replay of
  a pinned Terminal-Bench 2.0 grader, `bn-fit-modify`. It is the first replay whose decisive test is a
  distribution test (one-sample KS), and the first whose positive control is a committed R/bnlearn fixture.
- **R99-C2 — freshness** (ceiling 10, exercised). Twelve SOURCES rows whose sha256 already equalled
  committed bytes are bound by eight new three-column, URL-free `corpus/evidence/round<N>/PROVENANCE.md`
  files. A symmetric, finding-level census shows that no outside row's gate findings or bindings moved; this closes the round-98 provenance-URL side
  channel (r98 spot-check routed defect 1).

Round work:

- Protocol load: the lane prompt; the SKILL registry tail; SCORECARD r97/r98 sections and the round-99
  Planned rows; `corpus/lessons/round-98.md`; `round-98-verifier-spotcheck.md` (routed defects 1–4 are
  dispositioned in `corpus/lessons/round-99.md` §Round-98 routed defects); QUALITY Q76–Q83; `considerthese/2026-11-06.md`; `skill://godspeed`.
- Round status: the last three closures are r96 rejected-harmed, r97 rejected-honest-stop and r98
  admitted, so no pause and no fresh-start rule applies. The watchdog shows no `lane-dead-no-report
  kengaku round=99` line, so there is no inherited attempt. Untracked `.ufo/waves/round-97/w1.ready{,.dispatched}`
  are orchestrator markers and were left untouched.
- P0 `f9d29eb3`:
  - Eight bn-fit-modify files opened 2026-11-06 10:28 -03 (HTTP 200) and captured flat in
    `corpus/evidence/round99/tb2-bn-fit-modify/` with `SHA256SUMS`. This includes the dataset pinned at
    `gdreiman1/t_bench_bn_dataset@62ce2364`, which was byte-equal to the Dockerfile's unpinned `main`.
  - The maintainer R script was run once offline to build the fixture `corpus/evidence/round99/bn-fit-modify-solution/`.
    Its fitted D coefficients equal the grader's hard-coded constants (`run.log`).
  - Mechanism predictions (`L1/predictions-mechanism.txt`) and census start rc 0 (`L1/census-start.txt`).
- P1 `e219e785`:
  - Instruments: `plans/round99_bnfit_probe.py`, `plans/round99-cases.json`, `plans/round99_c1_replay.py`,
    `plans/round99_c2_rowscoped_bind.py`, `plans/round99_provenance_build.py`.
  - Dry runs: run 1 got 12/13, because C11's seeded-draw prediction failed (lesson M1). Runs 2–3 got
    13/13 with identical observations, after `L1/predictions-amendment-1.txt` made C11/C12
    deterministic grids.
  - C2 population derived at BASE: 12 rows (`L1/c2-pop.txt`).
- P2 `b08a0192`: 21 controls, each run twice with agreeing verdict lines (`L1/controls/README.md`). One
  control (`partial`) was invalid because of a harness defect. It was re-run fixed as `partial-fixed` (lesson M2).
- F `24a5a555`. C = T `f72a8bc7`: 18/18 frozen instruments and 11/11 candidate bytes match, and
  `git diff F T` is exactly the candidates plus the receipt (`L1/freeze-tip.txt`). Receipts `23d58036`.
- Dated correction after T, `b71b990a`: five typed word counts in S334/S336–S339 were recomputed;
  `anchor_line_check` went live 5 → 0 (lesson M3, a Q76 recurrence). Disclosed as a departure from the
  claims file's no-in-round-repair clause. It is a curation cell that no counter reads; the round-94 S299
  precedent applies.
- Integration `fc65aa9a`: `corpus/knowledge/tb2-bn-fit-modify-grader.md`, `corpus/README.md`
  coverage-map rows, `corpus/lessons/round-99.md`, QUALITY Q84–Q86, wave spec and dispatch.
- Harm battery `182a40bc` (`L1/harm/README.md`, `summary-fc65aa9a.txt`).
- Wave w1, dispatched through the inline handoff (`.ufo/waves/round-99/w1.ready`; WAVE-DONE from Main):
  12 seats, all settled, no dead seats (`.ufo/waves/round-99/w1-results.json`). Reports are in
  `.ufo/waves/round-99/w1/`; findings are in `corpus/lessons/round-99.md` §Wave findings.
- Dated correction after the wave, `3fdecf31`: the four `round99-*` registry selftest cells now read
  `none declared`. This puts the round82-c1 DEFECT set back to BASE's 13 (ExecHarm finding; lesson M5).
- Settlement `c329f955`: seat reports and results, knowledge and lesson corrections (ScribeLesson,
  CriticClaims wording), SCORECARD, LOG and census end.
- Final verification `64be3b7e` (`L1/final-verification.txt`): C1 passes at T and at the tip; C2 passes
  at the tip; `anchor_line_check` live 0; census ok.
- No new L0 question. Carried and open: `kengaku | round-98` (coverage cap) and `kengaku | round-54` (hold).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| P0 flat capture, solution fixture, predictions, census start | `LOG.md` Round 99, bullet 1 | `f9d29eb3df9cfec26fd11feac8695a6d26a871c1` |
| P1 instruments, dry runs, amendment 1, C2 population | bullet 1 | `e219e785281703058f05bec9c29d81c943d35596` |
| P2 controls ×2 | bullet 1 | `b08a01923361cdfc6ecd1366028630b0db7c9f6e` |
| F frozen claims | bullet 1 | `24a5a5554130065917d55618ae10309403abf60d` |
| C ledger flip, SKILL cell and registry rows, S334–S341, eight PROVENANCE.md files, probe receipt | bullets 2–3 | `f72a8bc710b12473b5c768004e2581f980d924f4` |
| measurement receipts (C1/C2 at T and BASE, freeze integrity) | bullets 2–3 | `23d580366db2a3462c9bbfc3b0ff71bce5837374` |
| dated correction: word counts (M3) | dated-corrections bullet | `b71b990ad1e9af0aacde23b1f5fc51bb86723531` |
| knowledge entry, README rows, lesson, Q84–Q86, wave spec and dispatch | bullet 4 | `fc65aa9a7e1c9661df846e956376898b6abf0e52` |
| L1 harm battery, round-98 counters at T and at their own T | harm bullet | `182a40bcb3a38070c916ae9314754bf6db2fa2d2` |
| dated correction: registry selftest cells (M5) | dated-corrections bullet | `3fdecf312cadced85d8868baa728761a5424bdfb` |
| wave settlement, corrections, SCORECARD, LOG, census end | wave bullet | `c329f95525e3cfecd8b6dd1cd17b460fa388ddb4` |
| final verification | wave bullet | `64be3b7ed3b7189ffb13664647e832a35477425d` |

The lane HEAD is `64be3b7ed3b7189ffb13664647e832a35477425d`, and
`git ls-remote origin refs/heads/master` prints that hash.

Disclosed departures:
- The two dated corrections after T (`b71b990a`, `3fdecf31`) edit C1 candidate files (SOURCES.md word
  cells; SKILL.md selftest cells) that no round-99 counter reads.
- The frozen claims file says a defect found after F is "never repaired in round". These corrections
  depart from that clause, following the round-94 S299 precedent, so that no standing gate is left
  redder than at BASE.
- Both claims are judged at T `f72a8bc7`, where the frozen-instrument and candidate bytes match.

## Before → after measurements

**R99-C1 (coverage).**
- Command: `python3 plans/round99_c1_replay.py --lane . --rev REV --work DIR --grader-venv G`, where G is
  `uv venv -p 3.13` plus pytest 8.4.1, pandas 2.3.2 and scipy 1.16.1 (numpy 2.5.4 resolved).
- BASE `2233a661`: `PREDICATE R99-C1 fail`, rc 1 (`L1/c1-base.txt`); ledger 42 executed,
  `file-artifact` 33/76.
- T `f72a8bc7`: `REV f72a8bc7…`, `LEGS L1..L11=pass`, `TARGET executed_rows=43 member=bn-fit-modify
  cells=file-artifact:34 set_equals_base_plus_member=1 located=1 executed=1 cases=13 legs=130
  mismatches=0 new_rows=8 new_rows_flagged=0 defects=0`, `PREDICATE R99-C1 pass`, rc 0 (`L1/c1-tip.txt`).
  The same result holds at the tip `c329f955` (`L1/final-verification.txt`).
- Do-nothing control: fail, in both runs (`L1/controls/c1-do-nothing-run{1,2}.txt`).
- Independently reproduced by ExecC1 (two probe reruns byte-equal; C03/C07/C11/C12 rebuilt with its own
  code under real pytest), ExecKS, ReviewC1 (offline R re-run, same fit) and ScoutSources.
- Located grading gaps:
  - Only column D is tested. A marginal-only sample passes (C03; 1998/2000 seeds), and so does a
    deterministic grid (C13).
  - The KS rule admits a mean shift up to 0.0487 sd (C11 passes at +0.045, C12 fails at +0.050).
  - Duplicate edges and an extra column pass (C07).
- Attacks: CriticClaims F1–F5 and MutC1 found 10/40 survivors (receipt run identity, F..C file set,
  new-row count). These are routed; none changes the value at T.
- Verdict: **met** on the frozen predicate. Score 7 → 7, held at the L0 cap.

**R99-C2 (freshness).**
- Command: `python3 plans/round99_c2_rowscoped_bind.py --lane . --rev REV --work DIR`.
- BASE: `TARGET pop=12 cleared=0 still=12 …`, `PREDICATE R99-C2 fail`, rc 1 (`L1/c2-base.txt`).
- T: `LEGS K1..K7=pass`, `TARGET pop=12 cleared=12 still=0 outside_rows=313 outside_removed=0
  outside_added=0 outside_rebound=0 url_channel_files=0 rows_changed=0 captures_changed=0`,
  `PREDICATE R99-C2 pass`, rc 0. Anchor-digest gate 45 → 33 (`L1/c2-tip.txt`). The same result holds at
  the tip `c329f955`.
- Controls (two runs each): the url-channel forgery re-binds S256 and fails; duplicate-line, sha-column,
  outside-rebind, row-edit, gate-edit, capture-edit, counter-edit and partial-fixed all fail.
- Independently reproduced by ExecC2 (its own checker; per-row gate diff over BASE rows = exactly the
  12), ReviewC2 (re-derived population; bindings semantically right) and ScoutSources (12 rows re-opened
  upstream).
- Attacks: CriticClaims F6/F7 and MutC2 M17 show that K7 is finding-level, not row-level: deleting an
  outside row that carries no gate output passes, and 105/313 outside rows carry none. MutC2 has 6/24
  survivors. Wording outside the frozen file was corrected to "finding-level", and the gaps are routed.
  CriticClaims F10 disputes the axis name `freshness`; this is left to the closure and operator.
- Verdict: **met** on the frozen predicate. Score 10 → 10, held at the ceiling.

## Sources & frontier

- SOURCES rows: **325 → 333**.
  - Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`, run at
    `2233a661` and `64be3b7e`.
  - Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`.
    Start: `kengaku ok …/corpus/SOURCES.md`, rc 0, 30 W04 (`L1/census-start.txt`). End: `kengaku ok`,
    rc 0, 31 W04 (`L1/census-end.txt`; again at `64be3b7e`). The new W04 is S334, whose URL equals S181's
    across scopes.
- Added by tier: A 7 (S334–S340), B 1 (S341).
- Added by status: 6 mined (S334–S339); 2 rejected (S340, S341), each with its flip stated.
- Rows touched old→new: no row present at BASE (C2 `rows_changed=0`, insert-only diff). Within-round:
  S334/S336–S339 word cells were corrected after T (`b71b990a`, lesson M3).
- Frontier advanced:
  - `bn-fit-modify` moved from unexecuted to executed (ledger 42 → 43).
  - 12 digest claims moved from gate-unbound to gate-verified (45 → 33).
- Sourced claim: R99-C1 rests on S334–S339, opened 2026-11-06 10:28 -03. `corpus/lessons/round-99.md`
  §Gate records the URL, access date and a ≤25-word located quote for each row, and
  `corpus/knowledge/tb2-bn-fit-modify-grader.md` cites them.
- ScoutSources re-opened all 8 new rows and the 12 population rows live; they agree on bytes (19/19).
- Mistakes mined: `corpus/lessons/round-99.md` M1–M5 (stochastic-verdict prediction, git-rm harness
  false pass, typed word counts, member class selection, registry-cell convention). QUALITY Q84–Q86 are
  added.
- Assimilation: none (inherited `merge/kengaku/` hold, L0 `kengaku | round-54`).
- considerthese: `2026-11-06.md` §1 proposal 2 → QUALITY Q86.

## Trend verdicts

- **expansion: improved.** A new knowledge entry, `corpus/knowledge/tb2-bn-fit-modify-grader.md`, covers
  ground not held at BASE: grading a causal pipeline through a one-column distribution test, and the
  first R/bnlearn positive-control fixture. It is indexed in `corpus/README.md` §Round-99, with ledger
  42 → 43 and S334–S339 mined.
- **quality: improved.**
  - 12 previously gate-unverifiable digest claims now re-verify against committed bytes, with no outside
    row's gate findings or bindings changed (C2).
  - The round-98 provenance-URL side channel is closed by construction.
  - Q84–Q86 are lesson-grounded.
  - Disclosed: two post-T curation corrections were needed (M3, M5).
- **discernment: unprovable-but-better.**
  - The lane self-grades this pending the closure's spot-check of the §Gate admit (S334) and rejects
    (S340, S341).
  - ScoutSources, a non-author seat dispatched by the lane, agrees with all 8 decisions on bytes and quotes.
  - LEARNING.md requires an outside check, so the lane claims no `improved`.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:74` (`file-artifact` executed 34 of 76) and the `round99-*` registry rows at `3fdecf31`; the grading lessons in `corpus/knowledge/tb2-bn-fit-modify-grader.md`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the official bn-fit-modify replay, `corpus/evidence/round99/bnfit-probe.txt`, and `LOG.md` Round 99. ExecC1 reproduced it (`.ufo/waves/round-99/w1/ExecC1.md`).
- [~] Instructions executable by an agent without oral context — the frozen commands in `plans/round-99-claims.md` were re-run unaided by nine wave seats (`.ufo/waves/round-99/w1/*.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` is unchanged, and ConnectorOverlap (a) finds no sibling-lane overlap (`.ufo/waves/round-99/w1/ConnectorOverlap.md`).

Round shape: one v1 wave under `ufo-wave-policy.json` (band 8–16), 12 seats.
- Role mix: 4 executor, 2 reviewer, 1 critic, 2 mutation-tester, 1 scout, 1 connector, 1 scribe.
- Attack seats: 5/12 (reviewer, critic, mutation-tester). The validator refused `labrat`, so the
  hypothesis probe ran as executor ExecKS.
- There was no residual call, so the round total is 12 seats. Dead seats: none.
- The L1 held the planner seat, and ConnectorOverlap (c) carried the bounded round-100 planning data-walk.

Stale-lane: respawn-per-round driver; no other kengaku mission is open.

Inherited state:
- Untracked at start: orchestrator markers `.ufo/waves/round-97/w1.ready{,.dispatched}`. They are not
  lane-authored and were left untouched.
- The watchdog shows no `lane-dead-no-report kengaku round=99` line, so there is no inherited attempt.

Misroot sweep: the fleet `git status --porcelain` shows only the orchestrator's `.scratch/run15-kernel.py`
and `.scratch/run15-state.json`, plus the unattributed `w4lines.txt` that predates this round. No seat
wrote a file at the fleet root.

Tooling:
- micromamba 2.10.0 was installed as the official release binary in `~/.local/bin` (channel:
  github.com/mamba-org/micromamba-releases latest; sha256 `701f39c0…e8bd`). The reason was to run the
  maintainer's R/bnlearn solution offline.
- It built a scratch conda-forge env (r-base 4.4.3, r-bnlearn 5.2.1) under `/fast/scratch/kengaku-r99/`.
- Preinstalled uv staged CPython 3.13.16 with pytest 8.4.1, pandas 2.3.2, scipy 1.16.1 and numpy 2.5.4
  (plus chess 1.11.2 for the r98 harm re-run) from PyPI.
- pacman, sysctls and services were untouched.

Open L0: none new. Carried: `kengaku | round-98` (coverage cap) and `kengaku | round-54` (assimilation hold).
