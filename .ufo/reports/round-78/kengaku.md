# kengaku — round 78 report

Lane: `kengaku-shokunin` · Round 78 (hyaku run 15, attempt 1) · 2026-11-04 UTC
Base `3ae0ab54` (round-77 verifier spot-check) · Freeze `2f9eeafb` · Lane tip `148801a6`
(remote verified: `git -C kengaku-shokunin ls-remote origin refs/heads/master` → `148801a67aebe7bf062932556083131fe96a2d39`)

## Work performed

**Declared claims (2, distinct axes, causally separable — each measured without the other landing).**

- **R78-C1 — coverage** (lowest non-retired axis, L0-capped at 7): the three grader classes
  `SKILL.md` declares *partially executed* (`network-service` 8, `process-environment` 3, `db-state`
  2 — 12 distinct members over 13 member-class pairs) become a machine-checked member ledger: every
  member accounted once, every `executed` member naming a tracked receipt whose own bytes carry its
  passing verdict **and the task's name**, every `unexecuted` member naming a typed reason whose
  frozen detector fires on that task's stored grader bytes, and the three class rows carrying
  `executed k of n` + `ledger=plans/grader-selected-members.json`.
- **R78-C2 — calibration** (held at ceiling 10, exercised): every verdict-bearing receipt under
  `corpus/evidence/round77/` and `corpus/evidence/round78/` becomes self-locating at **its own
  stamped revision** — `LANE_TIP` (ancestor of `master`), `WORKTREE`, `TOOL` + full `TOOL_SHA`
  recomputed in that tree (or `TOOL-SUPPLIED` + `WORKTREE dirty`), `COMMAND` — and the round-77
  closure's D1/D2/D5 are repaired through it, D3/D4 corrected in prose.

Both predicates are the frozen sentences in `plans/round-78-claims.md`; Amendment A1 (below) only
adds defects and moved no target, control or kill rule.

- **C1 counter + ledger.** `plans/round78_c1_class_member_ledger.py` (frozen `2f9eeafb`, amended
  `b47dbea8`) derives its universe from `SKILL.md` §Decision table (rows matching
  `executed k of n`, fenced blocks skipped) and the round-62 census receipt's `CLASS … members=`
  lines; `plans/grader-selected-members.json` carries the 12 rows (7 executed / 5 unexecuted).
  Evidence: `corpus/evidence/round78/c1-before.txt`, `c1-after.txt`, `c1-selftest.txt`,
  `c1-mutants.txt`, `c1-control-prose.txt`.
- **C2 counter + repair driver.** `plans/round78_c2_stamp_location.py` (frozen `2f9eeafb`, amended
  `b47dbea8`) audits every verdict-bearing receipt in the two directories (26 at the tip);
  `plans/round78_restamp.py` + `plans/round78-restamp.json` (landed `cd2e25bb`) re-mint a receipt at
  a clean tip or append a last-wins re-stamp block to a historical one. Evidence:
  `corpus/evidence/round78/c2-before.txt`, `c2-after.txt`, `c2-selftest.txt`, `c2-mutants.txt`,
  `c2-control-stamp-only.txt`.
- **Repairs landed.** 12 round-77 receipts re-minted at `cd2e25bb` (the two after receipts, both
  selftest/mutants/control pairs, the three reruns) and 4 re-stamped append-only
  (`c1-before`, `c2-before`, `exec-attrib-calibration`, `exec-state-check`) — `f20a2f6f`; the three
  reruns re-minted again at `bbf4f36c` once the index repair made R75-C1 green (`a0e86c10`); the two
  executed receipts whose bytes never named their task gained a dated `TASK-UNDER-TEST` annotation
  (`b47dbea8`).
- **Inherited drift repaired (not claimed).** `corpus/lessons/round-77-verifier-spotcheck.md` was
  missing from the README index (R75-C1 red at base), and R76-C2's scope derivation emptied on the
  round-77 closure's bare `D1…D5` labels (`EMPTY-SCOPE ids=0`); Amendment A1 to that gate qualifies
  a bare `D<n>` with the closure's round number — it can only add ids to the scope. Evidence:
  `corpus/evidence/round78/gates` lines in `.ufo/waves/round-78/gates-tip.txt`; commits `bbf4f36c`,
  `b2d4635b`.
- **Wave (one v1 wave, 11 seats, 0 dead, no residual call, round total 11).** executor 3
  (C1Replay, C2Replay, RestampFeas), scribe 2 (Sources, Lesson), scout 1 (RosterScout),
  critic 1 (CriticC1, 7 findings / 4 high), reviewer 1 (ReviewerC2, 4 findings / 2 high),
  mutation-tester 1 (MutantR78, 6/6 frozen kills + 3 hand mutants), sentinel 1 (SentinelR78,
  6 findings), connector 1 (ConnectorR78, 20 lanes, 0 duplicates, 22 adjacent). Attack roles
  3/11 = 27 % (≥25 %); connector 1 (≤2). Spec/dispatch/results and all 11 seat reports:
  `.ufo/waves/round-78/w1/`; `gates-tip.txt` beside it.
- **What the wave changed.** Amendment A1 (both counters) came from CriticC1 findings 2/3/4/6/7,
  ReviewerC2 findings 1/2/3/4 and SentinelR78 F1/F2/F3: per-receipt revision resolution, full
  64-hex pins only, `TOOL-SUPPLIED` recoverability, `STAMP-CONFLICT`, `TASK-MISMATCH`,
  `CLASS-NOT-PARTIAL`, duplicate-JSON-key rejection, ≥2-line vector tables, `RECEIPT-ESCAPE`/
  `RECEIPT-SYMLINK`/`MEMBER-NAME-ESCAPE`. Survivors are written down as limits, not smoothed: the
  reason detectors are syntax-backed (`network-install-required` fires on the executed `pypi-server`
  too), and `TOOL-SUPPLIED` proves the bytes are recoverable and unmodified, not who ran them.

## Landed changes

Every change is one LOG.md round-78 entry (append-only section "Round 78") and one commit:

| commit | content |
|---|---|
| `2f9eeafb` | freeze: both claims (`plans/round-78-claims.md`), both counters, `plans/grader-selected-members.json`, the three `SKILL.md` class-row ledger pointers |
| `cd2e25bb` | `plans/round78_restamp.py` + `plans/round78-restamp.json` (repair driver and its 16-entry spec) |
| `f20a2f6f` | the 16 round-77 receipts located (12 re-minted, 4 re-stamped append-only); driver stamps the real worktree state |
| `bbf4f36c` | claims/sources (S254, S255)/lesson/SCORECARD/LOG/PROVINCE/README rows, three registry rows, routed `R77-D1…D5`, `SF14` re-pin 245 → 247, first round-78 receipts |
| `a0e86c10` | three rerun receipts re-minted green; census before/after; routed checks observed pass |
| `e4c661ab` | C2 parser: last stamp block governs; `TOOL-UNPINNED` |
| `3cc5cecb` | round-78 receipts re-produced by the final counters; before values restated under the final rule |
| `749c2a40`, `2aa6c4e4` | the C2 after receipt (self-count stable at 26) |
| `b47dbea8` | Amendment A1 (nine defect-only legs) + `TASK-UNDER-TEST` annotations on `round68/pypi`, `round71/hf` |
| `04fdd644` | round-78 receipts re-measured under Amendment A1 |
| `49d4f0e1` | wave w1 evidence (11 seats, 0 dead) |
| `63fb46ba` | R76-C2 Amendment A1 (bare-`D<n>` scope), routed `R77-D1…D5` rename with id-naming checks, canonical count row 247 |
| `148801a6` | the gate block re-run from the clean tree at `63fb46ba` (12 gates green) |

Also landed in `bbf4f36c`: `SKILL.md` registry rows `round78-c1-class-member-ledger`,
`round78-c2-stamp-location`, `round78-restamp`; `PROVINCE.md` §Round 78 admission; the canonical
inventory's core row re-pinned `rows=245 → 247`; `corpus/README.md` index rows for
`lessons/round-78.md`, `lessons/round-77-verifier-spotcheck.md` (inherited) and
`evidence/round78/`.

## Before → after measurements

| claim | counting command | before | after | measured commit |
|---|---|---|---|---|
| **R78-C1** | `python3 plans/round78_c1_class_member_ledger.py --lane .` | (`--rev 3ae0ab54`) `UNIVERSE classes=3 members=12 pairs=13`, `LEDGER rows=0`, `DEFECTS n=21`, `TARGET … unaccounted=12 unbacked=0`, rc 1 | `LEDGER rows=12 executed=7 unexecuted=5`, `DEFECTS n=0`, `TARGET classes=3 members=12 executed=7 unexecuted=5 unaccounted=0 unbacked=0`, rc 0 | before @`3ae0ab54`, after @`04fdd644` (`c1-before.txt`, `c1-after.txt`) |
| **R78-C2** | `python3 plans/round78_c2_stamp_location.py --lane .` | (`--rev 3ae0ab54`) `UNIVERSE dirs=2 receipts=16`, `DEFECTS n=29` (11 `TOOL-UNNAMED`, 10 `COMMAND-ABSENT`, 4 `PASS-UNLOCATED`, 2 `WORKTREE-ABSENT`, 2 `TOOL-UNPINNED`), `TARGET receipts=16 located=2 unlocated=14`, rc 1 | `receipts=26 located=26 unlocated=0`, `DEFECTS n=0`, rc 0 | before @`3ae0ab54`, after @`04fdd644` (`c2-before.txt`, `c2-after.txt`) |

Controls (both must lose, and do): C1 `--control-prose` → `CONTROL prose_rows=2
prose_claimed_executed=3 members_named=0 receipts_resolved=0 reasons_backed=0 defects=9
target_reached=False`; C2 `--control-stamp-only` → `CONTROL receipts=6 stamped=6 located=6
real_defects=4 target_reached=False`. Batteries: C1 `SELFTEST cases=8 red=7`, `MUTANTS real=6
killed=6 survived=0`; C2 `SELFTEST cases=7 red=6`, `MUTANTS real=6 killed=6 survived=0`.

Gates at the tip (measured at `63fb46ba`, block committed in `148801a6`, `.ufo/waves/round-78/gates-tip.txt`): `grader.py` `CHECKS n=733
mismatches=0`, and `R51-C1`, `R52-C2`, `R74-C1`, `R74-C2`, `R75-C1`, `R76-C1`, `R76-C2`, `R77-C1`,
`R77-C2`, `R78-C1`, `R78-C2` all `pass`, `routed_open.py` `ROWS total=98 open=31 blocked=1
closed=64 refused=2` — all exit 0.

## Sources & frontier

- **Registry rows before → after:** 245 → **247**
  (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`); census
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`
  → rc 0 at round start (`corpus/evidence/round78/census-before.txt`) and rc 0 at round end
  (`census-after.txt`), 25 `W04` duplicate-URL warnings both times.
- **Rows added by tier:** two, both tier **A** — `S254` Git `git-status` documentation (`docs`;
  untracked-file semantics, the rule behind `WORKTREE clean`), live fetch 2026-11-04 with capture
  `corpus/evidence/round78/sources/git-status.html` (HTTP 200, 100 062 B, sha256 `22ff28ff…1b0180`),
  quote at capture lines 2322–2324, 17 words: "Show untracked files. The mode parameter is used to
  specify the handling of untracked files."; `S255` the lane's own round-62 class census receipt
  (`own-work`; sha256 `ee30c698…d45613`, anchor its `CLASS … members=` and `EXECUTED-COVERAGE`
  lines). **Rows touched old→new:** none (`status`/`recheck`/`used-by` unchanged on every
  pre-existing row). **Frontier rows advanced:** none — the round makes the partially-executed
  member map accountable; it replays no new member, so no `corpus/README.md` §Frontier item moves to
  core.
- **Rejected this round:** "a class count in a prose table is evidence of class membership" (flip:
  name every member and resolve one receipt per execution — R78-C1); "a `LANE_TIP` line locates a
  receipt" (flip: `TOOL` + full digest recomputed in that tree — R78-C2; the stamp-only control
  reaches `located=6` with 4 real defects left).
- **Assimilation: none.** `/home/vgpnk/Projects/shokuknow/merge/kengaku/` was not adopted; the mass
  id drift stays open at L0 `kengaku | round-54`. **considerthese** `2026-10-26.md`: proposals 1 and
  3 remain implemented from earlier rounds; proposal 2 (`tb2_grader_admit`) stays open
  (`grep -rn 'tb2_grader_admit' plans corpus SKILL.md` → only `corpus/lessons/round-66.md:332`) and
  is not mined — it serves neither frozen claim and has no implementing artifact.

## Trend verdicts

- **expansion: improved.** Three capability rows enter `SCORECARD.md`
  (`grader-class-member-ledger`, `receipt-stamp-location-gate`, `receipt-restamp-append-only`), each
  with a command demonstrated in this round and a committed receipt, and the registry gained two
  opened, tiered, cited rows (S254, S255). No new `corpus/knowledge/` entry — the round admits no
  domain fact, and says so.
- **quality: improved.** Eight gates that were red or unmeasured at base are green at the tip under
  one rule: R75-C1 (inherited missing index row), R51-C1 + R77-C1 (the SOURCES count pin moved 245 →
  247 with the canonical row corrected in place), R76-C2 (inherited `EMPTY-SCOPE`), and the two new
  gates; the 16 round-77 receipts now carry a digest that recomputes **in the tree their stamp
  names**, and both new gates ship with selftest, mutant and control batteries.
- **discernment: improved.** The wave attacked the claims in four classes and every class changed
  committed bytes rather than being smoothed: the critic's four high findings, the reviewer's two,
  the sentinel's three, the mutation tester's survivors. Amendment A1 is nine defect-only legs, the
  two executed receipts gained a dated task-binding annotation, and the counterexamples that were
  *not* closed are written down as limits (syntax-backed detectors; `TOOL-SUPPLIED` proves
  recoverability, not authorship).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer:
  `SKILL.md` §Gate/probe registry rows `round78-c1-class-member-ledger`,
  `round78-c2-stamp-location`, `round78-restamp`; the class table's three rows now carry
  `executed k of n` + `ledger=plans/grader-selected-members.json`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: LOG.md §Round 78
  (both claims measured end to end) and `corpus/evidence/round78/`.
- [~] Instructions executable by an agent without oral context — pointer: `plans/round-78-claims.md`,
  the three registry rows, and `corpus/evidence/round78/*` — a fresh agent can re-run both counters
  and both contract drivers from those bytes alone (the wave's `C1ReplayR78`/`C2ReplayR78` did).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` §Round 78 admission
  (serving plane, benchmark runtime services and route resolution stay with kama / the benchmark
  images / kumitate) and the connector's 20-lane matrix in `.ufo/waves/round-78/w1/ConnectorR78.md`
  (0 duplicates, 22 adjacent, all routed not absorbed).

## Stale-lane

Respawn-per-round driver (hyaku-inline): round 78 is this lane's only open mission; no other mission
of this lane is outstanding. No earlier attempt of round 78 existed (`.ufo/watchdog.log` carries no
`lane-dead-no-report kengaku round=78`; `.ufo/waves/round-78/` was created by this attempt), so there
was no inherited uncommitted state to reuse or discard.

## Tool installs

None. No package was installed or upgraded this round (pacman stayed paused per the addendum guard;
no `uv tool`/`npx`/binary install was needed).

## Open L0 questions

Carried unchanged, none blocking this round: kengaku rounds 25/33/51/54/56/63/65/66/67/72/74/76.
