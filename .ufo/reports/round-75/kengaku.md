# kengaku — round 75 (hyaku run 15, attempt 1, 2026-11-04)

Lane: `kengaku-shokunin` · base `4c4249a26a01aeb081915755076f74a7d6c88923` (round-74 verifier
spot-check) · freeze `e462a64975adc21c0319bb259878a92b200ada76` · Amendment A1
`43255758ed7d74ea05c8e03686dd9ad37837f0cd` · integration `08148cc49adcd4e114a4b934d423382313eea74b`
· evidence `66a93f6b4a4d645e320de14793d25e281f713cbb` · Amendment A5 `9f8f0f2180821d165f60e400277f192d92afbbce`
· **landing tip `b64203cffff789bd14112b1f7b40972fdc07b199`** (`git ls-remote origin
refs/heads/master` → `b64203cf…`, ahead=0 behind=0, worktree clean).

## Work performed

The round declares **two claims**: **R75-C1 on coverage** (the lane's lowest non-retired axis, held at
its L0 cap of 7) — a corpus index-parity gate over three universes enumerated from disk, plus the
repair of 59 drifted index surfaces; **R75-C2 on calibration** (held at ceiling 10, exercised) — an
attributed, revision-stamped registry audit that discharges the round-74 outside closure's R74-D1
(receipts with no measured revision), R74-D4 (any-defect mutant counting, literal tallies, no null
arm) and R74-D5 (no claim grounded on a source row), and implements S250's reject-flip for declared
options. Both are frozen in `plans/round-75-claims.md` with Amendments A1–A5.

- **Claim freeze.** `plans/round-75-claims.md` names both predicates, counting commands, before
  states, targets, controls and kill rules; freeze commit `e462a64` carries it with both instruments,
  two registry rows (SKILL.md rows 117–118 of the `## Gate/probe registry` block), S251 and the
  lesson's Gate/Mistakes.
- **R75-C1 gate** — `plans/round75_c1_index_parity.py` (297 lines, stdlib): enumerates
  `corpus/knowledge/*.md`, `corpus/lessons/*.md` and `corpus/evidence/*/` from disk, prices both
  directions, and reads only *rendered* rows (HTML comments and code fences stripped; cells split on
  unescaped pipes; non-empty description required; regular files only). Selftest `cases=8 red=7`,
  fake-completion control `NAIVE rows=6 surfaces=6 equal=True` while four `MISSING*` defects print.
- **R75-C2 instrument** — `plans/round75_c2_registry_audit.py` (360 lines) supersedes the round-74
  audit: ten mutants each priced against a declared expected finding id, one measured null arm,
  derived tallies, `LANE_TIP`/`WORKTREE` on every receipt, and a `--check-stamps` leg that resolves
  each stamp with `git rev-parse --verify <rev>^{commit}` and proves ancestry with
  `git merge-base --is-ancestor` (S251).
- **Index repair** — 36 lesson rows, 3 knowledge rows and 20 evidence rows added to `corpus/README.md`
  (`## Index repair — round 75`), the two pre-existing held knowledge rows given their
  `admission: hold` marker, and the malformed `tb2-distribution-search-grader` row's unescaped pipes
  escaped so it renders as three cells.
- **Wave w1** — one v1 wave, **13 seats**, all settled, **0 dead seats**, no residual call: executor 3
  (`IndexCensusR75`, `C1GateReplayR75`, `C2MutantReplayR75`), scribe 3 (`LessonRowsR75`,
  `EvidenceRowsR75`, `KnowledgeRowsR75`), reviewer 3 (`C1GateAuditR75`, `C2GateAuditR75`,
  `EntryFalsifyR75`), critic 1 (`ClaimsCriticR75`), mutation-tester 1 (`MutantBatteryR75`), scout 1
  (`SourcesHostR75`), connector 1 (`SiblingR75`); attack roles 5/13 = **38 %** (≥25 %), connector 1
  (≤2). Reports in `.ufo/waves/round-75/w1/`, registry/results in `.ufo/waves/round-75/`.
  **Planner seat:** the L1 holds the canonical planner seat; the bounded planning data-walk rode the
  scout item `SourcesHostR75` (§3 of its report lists the defects still open after this round).
- **Wave findings (reported, not smoothed).** `IndexCensusR75` independently re-derived the same 59
  missing names with its own parser (`receipt_match True`, 0 orphans). `ClaimsCriticR75` **challenged
  both claims** with executable counterexamples — a README whose only match was an HTML comment
  listing every filename printed `missing=0`, and `add_argument('--lane', help='--strict')` made a
  rejected option print `FLAGS ok n=0` — both closed by Amendment A3 and turned into permanent reject
  arms (A4). `C1GateAuditR75` filed one HIGH (non-rendered text) and one MEDIUM (`.md`-named directory
  counted as a file), both closed by A3. `C2MutantReplayR75` found a false pass with
  `LANE_TIP unknown`/`STAMPS files=0` (A2) and that the null arm renamed a row rather than editing
  whitespace (rewritten). `MutantBatteryR75` measured **C1 survivors 4/9 and C2 survivors 8/11**, all
  in the reporting surface; A5 added printed-verdict and printed-tally arms and the rest stay
  reported. `EntryFalsifyR75` found a held entry that fails Q1 placement and two evidence rows
  labelled without the hold marker. `SourcesHostR75` re-fetched S251 byte-identically and found
  `~/archive/bench-arena` **absent**. `SiblingR75` found kumitate's `readme-map.mjs` already does the
  knowledge/lessons parity and kotodama's `check-evidence-coupling.py` already compares
  `(exit, sorted finding ids)` — filed as a report-out, not absorbed.

## Landed changes

Every change below is a LOG.md round-75 entry or a documented amendment; hashes are the lane
`jj-lane.sh` `landed` lines.

| # | change | commit | LOG / note |
|---|---|---|---|
| 1 | freeze: claims doc, both instruments, two registry rows, S251 row + capture + anchor note, lesson Gate/Mistakes, R74-D2 correction in `corpus/lessons/round-74.md` | `e462a64` | LOG round 75; claims §Frontier |
| 2 | A1: every receipt mode stamps `LANE_TIP`/`WORKTREE`; Before values corrected by counting (`STAMPS files=11`, C1 lessons 36 / total 59) | `43255758` | claims Amendment A1 |
| 3 | integration: rendered-row index gate, positional-argument audit leg, the 59-surface README repair, PROVINCE surface row + round-75 report-out, wave evidence | `08148cc4` | LOG round 75; claims A3 |
| 4 | evidence: 8 before receipts (stamped at A1) and census-before (242 rows) | `66a93f6b` | `corpus/evidence/round75/` |
| 5 | evidence: after receipts + census-after (243 rows, rc 0) | `813b7403` | `corpus/evidence/round75/` |
| 6 | A5 + wave findings: printed-verdict/tally arms, SCORECARD round-75 section, LOG entry, README artefacts section, PROVINCE bench-arena correction | `9f8f0f21` | LOG round 75; claims A5; lesson M75-12…14 |
| 7 | evidence: after receipts regenerated at `9f8f0f21` (8-arm/5-arm selftests, K=15 stamps); SCORECARD tally correction | `b64203cf` | landing tip |

## Before → after measurements

**R75-C1 / coverage.** Counting command, both states:

    python3 plans/round75_c1_index_parity.py --lane .

| state | revision | printed | rc |
|---|---|---|---|
| before | `43255758` (`corpus/evidence/round75/c1-before.txt`) | `UNIVERSE knowledge files=74 indexed=71 missing=3 orphan=0`; `UNIVERSE lessons files=123 indexed=87 missing=36 orphan=0`; `UNIVERSE evidence dirs=66 indexed=46 missing=20 orphan=0`; 59 named `MISSING*` lines; `PREDICATE R75-C1 fail` | 1 |
| after | `b64203cf` (`corpus/evidence/round75/c1-after.txt`, measured at `9f8f0f21`) | `UNIVERSE knowledge files=74 indexed=74 missing=0 orphan=0`; `UNIVERSE lessons files=123 indexed=123 missing=0 orphan=0`; `UNIVERSE evidence dirs=66 indexed=66 missing=0 orphan=0`; `PREDICATE R75-C1 pass` | 0 |

Control (`c1-control-rowshuffle.txt`): a README whose index-row count equals the surface count
(`NAIVE rows=6 surfaces=6 equal=True`) still prints four `MISSING*` defects →
`PREDICATE R75-C1-control pass`. Selftest `c1-selftest-after.txt`: `SELFTEST cases=8 red=7
failures=0 ok=True`.

**R75-C2 / calibration.** Counting command, both states:

    python3 plans/round75_c2_registry_audit.py --lane . --mutants --check-stamps corpus/evidence/round75

| state | revision | printed | rc |
|---|---|---|---|
| before (stamp leg on the round-74 evidence) | `43255758` (`c2-stamp-red-before.txt`) | `STAMPS files=11 stamped=0 unstamped=11 unresolved=0 not_ancestor=0`, 11 `DEFECT UNSTAMPED` lines, `PREDICATE R75-C2 fail` | 1 |
| before (control, same fixture bytes) | `43255758` (`c2-control-attribute.txt`) | `R74-METRIC killed=10/10 (any-defect counting)` vs `R75-METRIC expected_matched=9/10 wrong_id=1`; `OFF-TARGET X-off-target expected=:entry:unbacked-flag: defects=1 matched=False`; `NULL-ARM defects=0`; `PREDICATE R75-C2-control pass` | 0 |
| after | `b64203cf` (`c2-after.txt`, measured at `9f8f0f21`) | `MISMATCH 0`, `DEFECTS n=0`, `FLAGS ok n=0`, `TEXT-FALLBACK n=0`, `MUTANTS real=10 expected_matched=10 wrong_id=0 survived=0 null_arms=1 null_survived=1 total=11`, `STAMPS files=15 stamped=15 unstamped=0 unresolved=0 not_ancestor=0`, `PREDICATE R75-C2 pass` | 0 |

Selftest `c2-selftest-after.txt`: `SELFTEST arms=5 failures=0 ok=True`. Both round-74 gates stay green
at the landing tip (`PREDICATE R74-C1 pass`, `PREDICATE R74-C2 pass`).

**Corrections disclosed rather than folded in.** A1 (stamp on every mode; counted Before values),
A2 (`TIPTAG:unresolved` + `STAMPS:empty-dir` after a seat's false pass), A3 (rendered rows only;
positional `add_argument` only, after two seat counterexamples), A4 (the two counterexamples became
reject arms: `cases=7`, `real=10`), A5 (printed-verdict/printed-tally arms: `cases=8`, `arms=5`). The
targets never narrowed; the batteries only grew. R74-D2 is closed by a dated correction in
`corpus/lessons/round-74.md`; R74-D3 is recorded (the round-74 section's "deletion column is 0" was
false — `SKILL.md` numstat `3 1`), so this report makes no such claim.

## Sources & frontier

- **Rows before → after:** 242 → **243**. Counting command, both states:
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`
  → rc 0 at both ends (before: `corpus/evidence/round75/census-before.txt`; after:
  `census-after.txt`), 25 `W04` duplicate-URL warnings at both ends.
  Row count: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 243.
- **Rows added by tier:** **S251**, tier **A** (Git `git-rev-parse` documentation; docs). Tier
  totals 212 A / 24 B / 6 C → **213 A** / 24 B / 6 C.
- **Rows touched old→new:** S251 absent → `mined`, `opened 2026-11-04`, `recheck on-release`,
  `used-by corpus/lessons/round-75.md, plans/round-75-claims.md`. No other row's status, recheck or
  used-by changed this round.
- **Frontier rows advanced:** the S251 row grounds R75-C2's stamp leg (the row is cited in the
  claim's §R75-C2 evidence, closing R74-D5's "no claim evidence cites a `S###`" gap). No
  `corpus/knowledge/` entry was admitted; the four held candidates stay held and now all carry
  `admission: hold` in the index.
- **Source re-verification:** seat `SourcesHostR75` re-fetched the URL (`http_code=200`, 122459
  bytes, sha256 `00e3b1aa…`, `cmp` rc 0 against the committed capture) and located the quote at
  capture line 2720 (18 words).
- **Assimilation: none.** No staged `merge/kengaku/` row was admitted; open L0 `kengaku | round-54`
  carried. `considerthese/` was not mined this round (no unimplemented proposal chosen inside the
  two-claim cap).

## Trend verdicts

- **expansion: improved.** The lane holds a new, re-runnable coverage surface it did not have: three
  disk-enumerated universes with both-direction parity, and an index that now matches the tree
  (59 surfaces repaired, 0 missing, 0 orphan). Evidence: `c1-before.txt` → `c1-after.txt`, the
  independent census (`IndexCensusR75.md`, identical 59 names), `PROVINCE.md` Corpus-index row.
- **quality: improved.** Two instruments supersede weaker forms with discriminating controls: the
  registry audit's kills are attributed and its null arm measured, its receipts carry a git-validated
  revision, and its flag leg follows S250's flip; the index gate rejects the non-rendered and
  row-counting false greens the seats built. Evidence: `c2-after.txt` (K=15 stamps),
  `c2-control-attribute.txt`, A3's rejection proofs, `SiblingR75.md`.
- **discernment: improved.** The round's own review seats falsified its claims twice and the fixes
  are in the counters, disclosed, not smoothed: the critic and the gate auditor each produced a
  passing counterexample, the mutation-tester measured 4/9 and 8/11 survivors in the reporting
  surface, and the round reports the remainder instead of claiming it away. It also recorded a stale
  surface (`~/archive/bench-arena` absent) and a held entry that fails Q1, and named a duplicate of
  its own instrument in a sibling lane.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` (118 registry rows; the two round-75 rows carry entry/verdict/self-test/pinned/scope cells), pointer `SKILL.md:587-708`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round-75 entry; the two frozen predicates run end to end (`corpus/evidence/round75/c1-after.txt`, `c2-after.txt`).
- [~] Instructions executable by an agent without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md:48`; this round's commands are absolute-path and self-contained in `plans/round-75-claims.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` (Corpus-index surface row, round-75 report-out, and the dated `~/archive/bench-arena` absence correction).

## Round shape, seats, tooling, L0

- **Shape:** one v1 wave, 13 seats, no residual call, **round total 13**; role mix executor 3 / scribe
  3 / reviewer 3 / critic 1 / mutation-tester 1 / scout 1 / connector 1; attack share 5/13 = 38 %;
  **dead seats: 0**. `w1-validate.rc` → `rc=0`; `w1-results.json` carries 13 settled seats.
- **Stale-lane:** none — respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none (no `pacman`, no new packages; `pacman` stayed paused per the addendum
  guard).
- **Open L0 questions carried unchanged:** `kengaku | round-25/33/51`, `round-54`, `round-56`,
  `round-63`, `round-65`, `round-66`, `round-67`. No new question appended: the bench-arena absence is
  operator-side and recorded in `PROVINCE.md` rather than routed as a decision request.
- **Inherited / non-lane state named:** no uncommitted lane leftovers existed at round start
  (`.ufo/waves/round-75/` was absent). The fleet root holds an untracked 24-byte file `after`
  (`== SCORECARD diff base-`) dated 2026-11-03 20:05 — not written by this lane's seats (it names no
  kengaku round), left untouched; `.scratch/*` is orchestrator-owned and untouched.
