# kengaku — round 77 (hyaku run 15, attempt 1, 2026-11-04)

Lane: `kengaku-shokunin` · base `07c97fcd2fcca74f72df1d3c6b9dfe662fd75b59` (round-76 verifier
spot-check) · final lane tip `5eb74eed3aa3f0b70986867f560f34c1da4f3427` · report committed after that
tip. One v1 wave, 12 seats, 0 dead.

## Work performed

Two claims, one per axis, both admitted:

- **R77-C1 / coverage** (lowest non-retired axis, capped at 7 by the open L0 `kengaku | round-25`):
  one **canonical declared-surface inventory** (`PROVINCE.md` → `## Declared surfaces —
  canonical, machine-checked`, 28 rows) that carries every surface the three older tables declare,
  resolves each row live under one typed rule (`path`, loopback `http`, `tcp`, sha256 `hash` pin,
  `rows=` `count` pin, in-repo `exec` run receipt, dated no-egress `remote`), requires the row's
  dated declaration to agree with the live verdict, and reports `UNLISTED-SURFACE` for any
  declaration of the three superseded tables that no canonical row carries.
- **R77-C2 / calibration** (held at ceiling 10, exercised): the round-76 closure's seven routed ids
  (`R76-V1` … `R76-V7`) become ledger rows in `corpus/routed-findings.jsonl` whose discharges
  re-derive at the commit that carries their evidence (S252's three-state ancestry + evidence literal
  read from that tree), plus seven legs V1–V7 that re-read the registry rows, the correction blocks,
  the LOG block, the considerthese sweep, the capability name and three stamped rerun receipts.

Work items, each with its pointer:

- **Freeze.** `plans/round-77-claims.md` (claims, targets, controls, kill rules, causal separability),
  both counters, the canonical inventory and S253 committed as `9ebb8ed1`.
- **C1 instrument.** `plans/round77_c1_declared_surfaces.py` — 28-row typed resolver, supersession
  leg, identity manifest. Selftest `cases=6 red=5`, mutants `real=6 expected_matched=6 survived=0`,
  control `CONTROL rows=7 declared_verdicts=7 agree=7 live=0 target_reached=False`
  (`corpus/evidence/round77/c1-selftest.txt`, `c1-mutants.txt`, `c1-control-declared.txt`).
- **C2 instrument.** `plans/round77_c2_defect_discharge.py` — seven ledger legs + V1–V7. Selftest
  `cases=10 red=9`, git arms `3/3`, mutants `6/6`, control
  `rows_claimed_closed=7 trivial_checks=7 defects=7 target_reached=False`
  (`c2-selftest.txt`, `c2-selftest-git.txt`, `c2-mutants.txt`, `c2-control-status.txt`).
- **Evidence-minting driver.** `plans/round77_remint_r76_batteries.py` — runs a frozen instrument's
  own `--receipt` writer and prepends `LANE_TIP`/`TOOL_SHA`/`TOOL`/`WORKTREE`/`MINTED_BY`/`COMMAND`,
  appending `EXIT <n>`; used to re-mint the two round-76 battery receipts without editing the frozen
  round-76 counter (R76-V1).
- **Discharges (R76-V1…V7).** Re-minted batteries with `TOOL_SHA`; both round-76 `SKILL.md` rows
  re-pinned to `cases=12 red=11`/`9/9` and `cases=14 red=13`/`12/12` with the A5/A8/A9 classes; three
  dated appended correction lines (LOG, `corpus/lessons/round-76.md`, SCORECARD); the missing
  `### Second-reviewer classes` LOG block; the considerthese re-adjudication; one capability name
  (`province-surface-resolver-table-anchored`, `declared-surface-resolver` → 0 hits); three stamped
  rerun receipts.
- **Inherited drift repaired.** `corpus/README.md` gained the two missing lesson rows
  (`round-76-verifier-spotcheck`, `round-77`) and the `corpus/evidence/round77/` row (R75-C1 was red at
  base); `plans/round51-surfaces.json` `SF14`'s count pin re-pinned 244 → 245 after the S253 append
  (R51-C1 red at base); the new driver registered as a `probe` row so R74-C1/R74-C2 stay green.
- **Wave.** One v1 wave, 12 seats: executor 3 (`C1ReplayR77`, `C2ReplayR77`, `ReceiptMintR77`), scribe
  2 (`ScribeCorrectionsR77`, `ScribeRegistryR77`), scout 1 (`ScoutFrontierR77`), connector 1
  (`ConnectorR77`), reviewer 2 (`ReviewerC1R77`, `ReviewerC2R77`), critic 1 (`CriticR77`),
  mutation-tester 1 (`MutantR77`), sentinel 1 (`SentinelR77`) — attack share 4/12 = 33 %. Spec
  `.ufo/waves/round-77/w1/w1-spec.json`, dispatch `w1-dispatch.json` (`counts.spawn=12`), validator
  `w1-validate.rc` = 0, `w1-results.json` (12 seat records, every `output` non-empty, dead seats 0),
  seat reports under `.ufo/waves/round-77/w1/`, all 12 present and non-empty.
- **Wave-driven corrections (all committed).** A3 (critic): `DUPLICATE-IDENTITY`,
  `REMOTE-ANCHOR-MISMATCH`, `REMOTE-AS-<kind>`, `ID-NOT-IN-CHECK`, mandatory battery tallies in V1 and
  mandatory `TOOL_SHA` in V7. A4 (sentinel M1): redirects refused before following (private opener, no
  proxy), TCP loopback-only. A5 (reviewer C1): supersession credit follows only the anchors a kind
  resolves, `exec` receipts must be tracked at the measured revision and carry a `COMMAND` line,
  `CONTRADICTORY-VERDICT`, full-64-hex pin comparison, no worktree fallback in `--rev` count reads.
  Survivors kept as stated limits: row deletion visible only through `IDENTITIES`/`--expect-manifest`;
  `CHECK-TRIVIAL` and `--receipt` truncation are syntactic/wrapper-trust boundaries.

## Landed changes

Every change below is tied to the round-77 LOG entry (`LOG.md`, section "Round 77") and to the commit
that carries it. All commits are on the lane branch `master`; the final tip is `5eb74eed`.

| commit | change | LOG entry |
|---|---|---|
| `9ebb8ed1` | freeze: `plans/round-77-claims.md`, both counters, the canonical inventory section, S253, the round-77 lesson shell | "Round 77" — claims and freeze |
| `8da90eb7` | R76-V1…V7 discharge: re-minted round-76 batteries (`corpus/evidence/round76/c1-{selftest,mutants}.txt`), both SKILL registry rows, three dated corrections, the `Second-reviewer classes` LOG block, the one-name fix, three stamped reruns, README index repair, `SF14` 244→245, the remint driver | "What the discharges changed" + "Inherited drift repaired" |
| `6f0c7ad9` | seven ledger rows `R76-V1…V7` in `corpus/routed-findings.jsonl` + A1/A2 amendments + C2 counter | "R77-C2" |
| `d181e16b` | A3 hardening (critic) + C1/C2 battery receipts + `QUALITY.md` Q56 | "Wave-driven corrections (A3)" |
| `08309a5a` | A4 confinement (sentinel M1) + SCORECARD round-77 section + PROVINCE round-77 admission | "A4" |
| `4f2ff9be` | A5 fixes (reviewer C1) + C1 batteries | "A5" |
| `51ffc14f`, `d488f0cb` | before/after receipts regenerated from clean clones | "R77-C1/R77-C2 evidence" |
| `a5c81b76`, `7023db7e` | remint driver registry row (`probe`), R74-C1/C2 green | "Inherited drift repaired" |
| `a3299c33` | the round-77 `LOG.md` entry | this row |
| `113c7ef0` | wave evidence: spec, dispatch, validator output, 12 seat reports | "Wave (12 seats …)" |
| `5eb74eed` | the orchestrator's `w1-results.json` handoff (12 seat records, dead seats 0) | "Wave (12 seats …)" |

No axis harmed. The lane diff is append-only except: the dated corrections named above; the canonical
inventory section appended to `PROVINCE.md` (plus the one-name correction in its §Round 76); the two
`SKILL.md` round-76 rows re-pinned to their final tallies; the re-minted round-76 receipts (the R76-V1
repair); `plans/round51-surfaces.json` `SF14`'s count pin; and `corpus/README.md`'s three new index rows.
No file was deleted.

## Before → after measurements

**R77-C1** — counting command
`python3 plans/round77_c1_declared_surfaces.py --lane .` (before: the same command with
`--rev 07c97fcd`; both receipts minted from a clean clone, `WORKTREE clean`):

- before (`corpus/evidence/round77/c1-before.txt`, measured at base `07c97fcd`):
  `CANONICAL source=none rows=0`, `SURFACES total=0 present=0 absent=0 remote=0`, `UNLISTED n=33`,
  `RESOLVED live=0`, `AGREE agree=0 disagree=0`, `DEFECTS n=34`, `PREDICATE R77-C1 fail`, rc 1;
- after (`c1-after.txt`, stamped `4f2ff9be`, re-verified at the tip): `CANONICAL source=## Declared
  surfaces rows=28`, `SURFACES total=28 present=14 absent=13 remote=1`, `UNLISTED n=0`,
  `RESOLVED live=27`, `AGREE agree=28 disagree=0`, `IDENTITIES n=28 unique=28`, `DEFECTS n=0`,
  `PREDICATE R77-C1 pass`, rc 0.

**R77-C2** — counting command `python3 plans/round77_c2_defect_discharge.py --lane .` (before:
`--rev 07c97fcd`):

- before (`corpus/evidence/round77/c2-before.txt`): `SCOPE ids=7 registered=0 closed=0 open=0
  discharged=0 legs_passed=0 legs_pending=2 wrong=12`, `DEFECTS n=12`, `PREDICATE R77-C2 fail`, rc 1;
- after (`c2-after.txt`, stamped `4f2ff9be`): `SCOPE ids=7 registered=7 closed=7 open=0 discharged=7
  legs_passed=7 legs_pending=0 wrong=0`, `DEFECTS n=0`, `PREDICATE R77-C2 pass`, rc 0.

Both before receipts were re-measured under the final rules after the wave's A3/A4/A5 hardening, so the
before/after pair is measured by one rule in each claim. Other gates at the final tip:
`R76-C1 pass`, `R76-C2 pass`, `R75-C1 pass` (74/74, 127/127, 68/68), `R51-C1 pass`,
`R74-C1 pass`, `R74-C2 pass` (MISMATCH 0), `routed_open.py` → `ROWS total=93 open=31 blocked=1 closed=59
refused=2`.

## Sources & frontier

- **Registry rows before → after:** 244 → **245**
  (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`); census
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`
  → rc 0 at round start (`corpus/evidence/round77/census-before.txt`, measured on a scratch clone at
  `07c97fcd`) and rc 0 at round end (`census-after.txt`), 25 `W04` duplicate-URL warnings both times.
- **Rows added by tier:** one, tier **A** (`S253`, Git `git-cat-file` docs). **Rows touched
  old→new:** none (`status`/`recheck`/`used-by` unchanged on every pre-existing row). **Frontier rows
  advanced:** none — the round repairs the declaration inventory and the burn-down; no
  `corpus/README.md` §Frontier item moves to core this round.
- **S253** — https://git-scm.com/docs/git-cat-file, opened live 2026-11-04, capture
  `corpus/evidence/round77/sources/git-cat-file.html` (HTTP 200, 79 488 B, sha256
  `91805d9aec858f88581552fc1fe105a40a649544f872e72e6daff210a113e910`), quote at capture lines
  2584–2585, 15 words: "If <type> is specified, the raw (though uncompressed) contents of the
  <object> will be returned." It grounds both counters' at-revision reads; `used-by`
  `corpus/lessons/round-77.md` and `plans/round-77-claims.md`.
- **Assimilation: none.** `/home/vgpnk/Projects/shokuknow/merge/kengaku/` was not adopted; the mass id
  drift stays open at L0 `kengaku | round-54`. `considerthese/2026-10-26.md`: proposals 1 and 3 were
  already implemented in earlier rounds, proposal 2 (`tb2_grader_admit`) is recorded **open** and is
  not mined this round.

## Trend verdicts

- **expansion: improved.** One capability row set enters `SCORECARD.md`
  (`canonical-declared-surface-inventory`, `receipt-tool-binding-discharge`,
  `receipt-remint-with-tool-sha`), each demonstrated by a command and a committed receipt in this
  round, and the registry gained one opened, tiered, cited row (S253). No new `corpus/knowledge/`
  entry — the round admits no domain fact, and says so.
- **quality: improved.** Three gates that were red at base are green at the tip (`R75-C1` missing two
  lesson rows and the `round77` evidence row; `R51-C1` `SF14` count drift; `R74-C1`/`R74-C2` the
  unregistered driver), two new gates ship with selftest, git-arm, mutant and control batteries, and
  the round-76 battery receipts now carry a `TOOL_SHA` a reader can recompute.
- **discernment: improved.** The waveform attacked the claims in three classes and each class changed
  committed bytes rather than being smoothed: the critic's two false greens (A3), the sentinel's
  pre-contact confinement defect (A4) and the reviewer's five false greens (A5). Survivors are written
  down as limits, not claimed away.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer:
  `SKILL.md` (the registry table now carries `round77-c1-declared-surfaces`,
  `round77-c2-defect-discharge` and `round77-remint-r76-batteries` with exit maps, self-test lines and
  pinned values; `corpus/QUALITY.md` Q56 is the round's criterion). Lane-asserted; no named non-author
  verifier has written `[x]`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` section
  "Round 77" (two claims measured end to end; evidence under `corpus/evidence/round77/`).
- [~] Instructions executable by an agent without oral context — pointer: `plans/round-77-claims.md` +
  the three registry rows + `corpus/evidence/round77/*-after.txt`; a fresh agent can re-run both
  counters and the batteries from those bytes alone.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` §Round 77 admission
  (the same refusals stand: serving plane, benchmark runtime services, route resolution stay with
  kama / the benchmark images / kumitate) and the connector's sibling matrix in
  `.ufo/waves/round-77/w1/ConnectorR77.md`, which records report-outs for 14 lanes without absorbing
  any of their scope.

## Stale-lane

Respawn-per-round driver (hyaku-inline): this round's mission is the only one open for this lane; no
other mission of this lane is outstanding. Round prompted `2026-11-04T02:23:41-03:00`; the report lands
in the same session.

## Tool installs

None. No package was installed or upgraded this round (pacman stayed paused per the addendum guard; no
`uv tool`/`npx`/binary install was needed).
