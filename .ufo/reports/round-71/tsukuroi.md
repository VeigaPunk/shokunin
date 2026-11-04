# tsukuroi — round 71 report

Lane: `/home/vgpnk/Projects/shokunin/tsukuroi-shokunin` (hyaku run 15, round 71, attempt 1).
Lane tip at filing: `b0c784e0d35c0116e6deff4a34b509af16d5d7c2` (`ls-remote origin refs/heads/master`
prints the same hash). Report filed last, after every wave settled.

## Work performed

Round 71 declared **two claims on two distinct axes** (SCORECARD "Round 71 — declaration", frozen at
`0fcfca31` before any data): **C1 depth** — the kernel module-parameter surface, a SOURCED capability on
the lane's lowest non-retired axis (depth 8, tied with adjacency 8), carried by six rule rows MP1-MP6 in
`corpus/knowledge/module-parameter-plane-r71.md` over four new registry rows S297-S300; and **C2
operability** — a per-case timeout harness for the census selftest, entering the repertoire as the
capability `selftest-case-timeout`. Saturation line 9 / window 3; a capability entered at round 70, so the
stagnation nudge did not waive the lowest-axis duty.

- **Claim C1 — the note and its rows.** `corpus/knowledge/module-parameter-plane-r71.md` (MP1-MP6:
  `perm == 0` hides a parameter; the mode **is** `perm` and a store exists only with a write bit; the
  `kernel_param_ops` contract; an unknown parameter is warned and ignored; `module_blacklist=` refuses the
  load; the two specification routes with built-ins needing the cmdline). Evidence: the frozen counter
  `tools/count-mp-rows-r71.py` prints `MP_ROWS=6 MP_VERIFIED=6 MP_SOURCES=4 MP_SNAPSHOTS=4
  MP_MALFORMED=0`, `met=1`, rc 0 at `2b358d2d`; registry rows S297-S300 in `corpus/SOURCES.md`
  (`NF=13` each, `malformed=0`); sources opened and committed at `.ufo/waves/round-71/before/src/`
  (`SHA256SUMS` 4/4 OK, `SOURCES.json`).
- **Claim C2 — the harness.** `tools/tsukuroi-census.sh` now bounds every selftest case child: own
  process group, `/proc`-state liveness (a zombie counts as exited), per-case bound
  `TSUKUROI_SELFTEST_CASE_TIMEOUT` (default 60 s), TERM then KILL, rc 124 and a FAIL line naming the case
  and `timeout`, and an unconditional group kill after every run so a daemonizing child leaves no
  descendant. Evidence: `after/selftest-after.txt` → `PASS (218 cases, 218 passed, 0 failed)` rc 0 with
  four `R71-C2` case labels; red-before `before/redbefore-timeout.txt` → rc 124, 0 verdict lines;
  live rollup byte-identical and rc 1 (`after/census-live-after.txt`).
- **Wave w1 — one v1 wave, 14 seats, 0 dead** (`.ufo/waves/round-71/w1-results.json`): scout 1 /
  executor 3 / scribe 4 / connector 1 / reviewer 2 / critic 1 / mutation-tester 1 / sentinel 1; strict
  attack seats 4/14 = 29 % (≥ 25 %); one connector (≤ 2); residual 0; the L1 held the planner seat. Seat
  reports under `.ufo/waves/round-71/{w1,probes}/`.
- **Source re-open by a second route.** `S1Scout` re-fetched all four snapshots from
  raw.githubusercontent.com/gregkh/linux at the same tag: `ROUTE2_OK=4/4`, byte-identical, every planned
  quote located with line numbers (`probes/S1Scout/{route2.txt,quotes.tsv}`).
- **Independent C1 falsification.** `R1Reviewer` re-implemented the grammar (no import of the lane
  counter) and agreed on **105/105** parsed row occurrences and **18/18** whole-input return codes,
  reporting three P2 precision findings on the note's prose (MP6's built-in constraint, MP3's `get`
  return, MP2's visibility-vs-store wording); all three are corrected in the note at `2b358d2d`.
- **Counter attack.** `E2CounterAttack` built 13 source-level clause removals: 2 killed, **11 survive**
  because another clause still rejects the matched fixture — the fixture set does not isolate clauses
  even though the predicate does (`probes/E2CounterAttack/score.md`). `K1Critic` reproduced 20/24
  declaration receipts and filed four defects, all recorded as errata (battery count, modprobe.d count,
  the "census validate" label, the duplicate-id case's attribution).
- **C2 attack and repair.** `R2Reviewer` found that `arm_run()` and the six `--identity` case children
  were still unbounded, and that a daemonizing child left a live descendant; both are repaired (an
  `id_run` wrapper and an unconditional post-wait group kill) and a fourth `R71-C2` arm asserts the
  descendant is gone. `M1Mutation` scored 8 harness mutants: 7 killed, 1 survivor (capture moved to
  `/tmp`; no case asserts where the capture lives), and showed that deleting the four `R71-C2` cases makes
  all 8 mutants invisible — only the count target notices.
- **Harness lineage.** `N1Sentinel` F3 flagged that the committed C2 bytes are byte-identical to the L1's
  own prototype (`/fast/scratch/…/L1/proto/census.sh`) and predate E1Harness's patch; the round therefore
  names the lineage (L1 implementation; E1Harness's patch as the independent alternative) instead of
  claiming a seat artifact was applied.
- **Sentinel audit.** `N1Sentinel`: `SECRETS=0 SUDO_NONREADONLY=0 TMP_EVIDENCE=0 MISROOT=0
  LANE_DIRTY_SEAT_AUTHORED=0`; 73 in-wave writes, all inside the wave dirs; one receipt recorded as not
  replayable as written (relative paths, F2).
- **Routed repairs (work, not claims).** D1 the r70 stale selftest tallies corrected append-only in
  `PROVINCE.md`, `corpus/README.md`, `SKILL.md`; D2 the r70 final-revision receipt line corrected; D3 the
  `count-xs-rows-r70.py` shebang (`#!/usr/bin/env python3`); D4 the r70-planned counter amendments carried
  into this round's counter; plus the r70 tool's missing operative registry row (QUALITY 70).
- **Assimilation: none** — the open L0 `tsukuroi | round-64` addendum still rules the `merge/tsukuroi/`
  package quarantined. `considerthese`: no proposal mined; the measured status of the five proposals in
  `considerthese/2026-10-26.md` is recorded in the lesson.
- **Stale-lane:** this is a respawn-per-round driver round; no other mission of this lane is open.
- **Tool installs:** none this round (no package, binary or service was installed or upgraded).

## Landed changes

Every change is tied to the round's LOG entry (`LOG.md`, "Round 71 — landing") and to the commit that
carries it on `master`.

| Commit | Carries | LOG tie |
|---|---|---|
| `0fcfca31` | declaration: frozen counter + 11-case battery, snapshots, host capture, novelty sweep, absence controls, red-before, SCORECARD declaration | LOG r71 (declaration, erratum (a)-(e)) |
| `db58e7c9` | C2 harness first landing (bounded `check`/`check_cli`, three `R71-C2` arms) + r70 shebang + after receipts | LOG r71 C2 paragraph (D3) |
| `2959254a` | C1 note MP1-MP6, registry rows S297-S300, search-log paragraph, unopened lead | LOG r71 C1 paragraph |
| `bdaec573` | PROVINCE R71-MODPARAM-VIEW, coverage rows, SKILL decision table + round-71 cumulative registry, QUALITY 105, `tools/check-selftest-tally.py`, r70 tally corrections | LOG r71 routed repairs (D1, D4) |
| `2b358d2d` | C2 repair (arm_run/identity bounded, `/proc` liveness, 2 s grace, rc 124, post-wait group kill, daemonizing arm) + C1 precision corrections from R1Reviewer | LOG r71 wave paragraph; lesson R71-C2-* rows |
| `391565af` | wave evidence: spec, dispatch, results, 14 seat reports, probes | LOG r71 wave paragraph |
| `5ab72e45` | SCORECARD measured outcome + declaration errata, lesson `round-71.md`, LOG entry, final-figure corrections | LOG r71 landing entry |
| `ccfc7e8f` | annotated pre-report tally sweep receipt | LOG r71 (QUALITY 105) |
| `b0c784e0` | `check-selftest-tally.py` scope/skip rule matching the committed sweep receipt | LOG r71 (QUALITY 105) |

## Before → after measurements

**C1 — depth (SOURCED).** Counting command:
`python3 tools/count-mp-rows-r71.py --revision <REV>` (plus
`git show <REV>:corpus/SOURCES.md | grep -cE '^\| S[0-9]{3,}'`).

| | Base `930d5530` | Measured `2b358d2d` |
|---|---|---|
| note | `git cat-file -e` rc 128 | present |
| counter | `git cat-file -e` rc 128 | present |
| `MP` rows | 0 | 6 |
| counter verdict | — | `MP_ROWS=6 MP_VERIFIED=6 MP_SOURCES=4 MP_SNAPSHOTS=4 MP_MALFORMED=0`, `met=1`, rc 0 |
| registry rows | 296 | 300 |
| knowledge notes | 88 | 89 |
| canonical census | rc 0 | rc 0 |

Axis verdict: depth **8 → 8** (unchanged ordinal; one new mechanism on ground the province never held, plus
one capability).

**C2 — operability (capability `selftest-case-timeout`).** Counting commands:
`bash tools/tsukuroi-census.sh --selftest | tail -1` and `grep -c 'R71-C2' <receipt>`.

| | Base `930d5530` | Measured `2b358d2d` |
|---|---|---|
| `R71-C2` case labels emitted | 0 | 4 |
| `R71-C2` lines in the tool | 0 | 15 |
| selftest | `PASS (214 cases, 214 passed, 0 failed)` | `PASS (218 cases, 218 passed, 0 failed)` |
| blocking probe | hangs (external bound rc 124, 0 verdict lines) | killed at the case bound, FAIL line names the case and `timeout` |
| live rollup / rc | `TSUKUROI_CENSUS: DEGRADED (…)`, rc 1 | byte-identical, rc 1 |

Axis verdict: operability **9 → 9** (no uplift; the capability enters the repertoire table).

**No axis harmed.** The round diff is additive in `PROVINCE.md`, `corpus/README.md`, `SKILL.md`,
`corpus/QUALITY.md`, `corpus/SOURCES.md`, `SCORECARD.md`, `LOG.md`; the census's live line set and exit
code are unchanged; the declared ordinals stay depth 8 / coverage 9 / operability 9 / freshness 9 /
calibration 9 / adjacency 8.

## Sources & frontier

`corpus/SOURCES.md` rows: **296 → 300** (counting command
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; round start rc 0 at 296, round end
rc 0 at 300 under `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`).

- **Rows added by tier:** four, all **tier A**: S297 `kernel/params.c`, S298 `include/linux/moduleparam.h`,
  S299 `kernel/module/main.c` (kind `code`), S300 `Documentation/admin-guide/kernel-parameters.rst`
  (kind `docs`); all `status=mined`, `opened=2026-11-04`, `recheck=on-release`.
- **Rows touched old→new:** none — no existing row's `status`, `recheck` or `used-by` changed this round.
- **Frontier rows advanced:** none. The new surface enters as Core ground (PROVINCE "Round-71 entry —
  R71-MODPARAM-VIEW"); the kmod `modprobe.d(5)` precedence question is recorded as an unopened lead, not a
  row, because its source path 404d this round.
- **Search log:** one bounded-search paragraph (question, sources searched, identified/screened/included/
  excluded, stop rationale) appended to `corpus/SOURCES.md`.
- **Gate record:** the four URLs, the access date 2026-11-04 and ≤ 25-word located quotes are in
  `corpus/lessons/round-71.md` `## Gate`, with the second-route receipt `probes/S1Scout/route2.txt`.
- **Non-author spot-check:** OWED by the closure judge; no author-side `[x]`.

## Trend verdicts

- **expansion: improved.** Four admitted tier-A rows on ground the lane never held (0 file hits at base for
  `modprobe.d`, `kernel-parameters`, `module_blacklist`, `NVreg`, `module_param`, `kernel_param_ops`,
  `param_attr_store`; no note naming the surface), one admitted entry citing them, registry 296 → 300,
  notes 88 → 89, and one capability (`selftest-case-timeout`) entering the table.
- **quality: improved.** Two attack-found C2 gaps repaired with the suite able to fail (218/218 after;
  `FAIL (219 cases, 217 passed, 2 failed)` is the red state the stdin regression produced), the C1 note's
  three precision findings corrected, three r70 routed defects landed with a committed tool for D1's class
  (QUALITY 105: 4 mismatches red on r70 bytes, 0 on the corrected control), and the round's own declaration
  defects kept as errata rather than smoothed.
- **discernment: unchanged (author-side).** The wave caught seven of the lane's own defects and the L1's
  self-attack named the lexical-substance channel; the outside non-author admit/reject spot-check is owed
  by the closure judge.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — round 71 adds the
  module-parameter decision table (S1-S9, every row citing MP1-MP6) and the round-71 cumulative gate/probe
  registry; evidence `SKILL.md` round-71 block at `b0c784e0`, sources S297-S300.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the C1/C2 pair is executed end to
  end: sources opened, note admitted under a frozen counter, harness landed and attacked; evidence
  `LOG.md` "Round 71 — landing", commits `2959254a` and `2b358d2d`.
- [~] Instructions executable by an agent without oral context — the decision table maps an observed
  `/sys/module/<name>/parameters/<p>` shape to a verdict and an operator action with no write capability;
  evidence `SKILL.md` round-71 table, `PROVINCE.md` "Round-71 entry".
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the entry states what is Core (reading the
  parameter surface), what is operator-owned (every write, modprobe edit, load/unload, blacklist change) and
  what is not claimed (module internals, RE → kaidoku/revenger); `C1Connector` quoted the sibling ownership
  sentences that cede the surface to tsukuroi (`probes/C1Connector/overlap.md`).

No `[x]` is written by the author; promotion review remains operator/closure-owned.
