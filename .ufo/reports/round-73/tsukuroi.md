# tsukuroi — round 73 report (hyaku run 15, attempt 1)

Lane: `tsukuroi-shokunin` · round 73 · one v1 wave, 12 seats · declaration
`749371321c00f04d98c29d2c26b57d75a92d7e37` (base `eb1057575d5d8b940c4846e21611674cf5571aea`) · measured
revision `3cfa23ac4da7129fa8a614909af52fdfeae5c143` (the claim states were first measured at `583eea87`
and re-measured unchanged at the final tip `8985a817`, whose only delta is the after-receipt file).

**Claims.** C1 **depth** (lowest tied, 8): the systemd unit-load merge plane enters the corpus as
`corpus/knowledge/systemd-unit-load-plane-r73.md` (rows UL1-UL6, sources S304-S306). C2 **freshness** (9): the
three round-72 closure defects close in committed bytes (the round-72 lesson correction, the instrument-digest
erratum and the `gate-selftest` count refresh). Two claims, two axes, causally separable (separate counters,
separate files).

## Work performed

- **C1 — the plane.** Opened systemd **v262** (`man/systemd.unit.xml`, `src/core/unit.c`,
  `src/shared/install.c`) as the release the host's 262.1-1-arch build descends from, committed byte-exact
  with `SHA256SUMS`/`SOURCES.json` (`.ufo/waves/round-73/before/src/`), and landed six rule rows: the compiled
  load path with earlier-directory override and the `SYSTEMD_UNIT_PATH` override including its
  trailing-empty-component append case (UL1); drop-in merge with `/etc` > `/run` > `/usr/lib` for same-named
  files, one cross-directory lexicographic pass and drop-ins under those directories outranking the unit file
  (UL2); the daemon-reload condition with masked drop-ins omitted (UL3); the still-masked test on the file at
  the fragment path (UL4); the `/dev/null` mask symlink, `masked` vs `masked-runtime`, and the unmaskable
  generator mask (UL5); enable-time `[Install] Alias=` creation even for a missing target, with the
  dangling-alias change reported on removal paths (UL6). Evidence: `corpus/knowledge/systemd-unit-load-plane-r73.md`;
  enumeration `w1/S1Scout/report.md` (`ROUTE2_OK=3/3`, six located quotes, `HOST_DELTAS=0`);
  per-row verdicts `w1/R1Reviewer/report.md`; host readings `.ufo/waves/round-73/before/host.txt` re-measured
  by three seats with no delta.
- **C1 — the instrument.** `tools/count-ul-rows-r73.py` (final sha256 `1f22c26b…`): thirteen-case `--selftest`,
  per-row id/words/grounding/source-kind/digest/map/anchor/quote/reuse clauses, `$TMPDIR`-only writes.
  Evidence: `.ufo/waves/round-73/after/measure-583eea87.txt` (`met=1`, rc 0); attacks `w1/E1Counter/report.md`
  (empty-quote defect, clause isolation), `w1/R1Reviewer/report.md` (word-salad, unrelated-region quote,
  anchor-without-range), `w1/K1Critic.md` D2.
- **C2 — the three repairs.** Appended the round-72 lesson correction naming both superseded sentences and
  the ten-case landed state (`corpus/lessons/round-72.md`); appended the instrument-digest erratum with the
  digest history `df8a59c7…` → `53bcddef`(`2610ff43…`) → `123e1c57`(`b17fddfa…`) → `2610ff43…`, plus a
  same-instrument 3 → 0 pair (`SCORECARD.md`, receipt `after/r72-c3-same-instrument-before.txt`); appended the
  `gate-selftest` count refresh restating ten cases with its receipt. Evidence:
  `tools/check-r72-routed-r73.py --revision 583eea87` → `ROUTED_STALE=0 ROUTED_OK=3/3` rc 0;
  the base control `--revision eb105757` → `ROUTED_STALE=3` rc 1 (`after/c2-before-final-instrument.txt`).
- **C2 — the instrument.** `tools/check-r72-routed-r73.py` hardened from the wave's attacks (whole-token and
  path-token matching, digest direction, receipt existence with a ≥10-case line, supersession verb; five →
  fourteen selftest cases). Evidence: `w1/R2Reviewer/report.md` F1-F7; `w1/E2Routed/receipts/`; SCORECARD
  "Round 73 — C2 instrument repair" and "final instrument digests".
- **Docs.** `SKILL.md` (repair decision table T1-T6 + registry continuation rows), `PROVINCE.md` (R73
  Core entry with still-Frontier and operator-owned boundaries), `corpus/README.md` (round-73 coverage index).
  Evidence: the committed files; drafts `w1/SC3Index/deltas.md`.
- **Boundary scan.** No sibling lane owns this plane; the twelve held `drop-in` mentions are observations of
  named files, not rules (`w1/C1Connector/report.md`). Reported, nothing absorbed.
- **Frontier step.** `corpus/SOURCES.md` curated (308 rows, three mined + two refused), one mistake mined per
  class into `corpus/lessons/round-73.md` (ten `## Mistakes`), and C1 is the round's SOURCED claim.
- **Wave.** One v1 wave, **12 seats** — scout 1 (`S1Scout`), executor 3 (`E1Counter`, `E2Routed`,
  `E3HostProbe`), scribe 3 (`SC1Entry`, `SC2Sources`, `SC3Index`), connector 1 (`C1Connector`), reviewer 2
  (`R1Reviewer`, `R2Reviewer`), critic 1 (`K1Critic`), mutation-tester 1 (`M1Mutation`); strict attack 4/12 =
  33 %; connector 1; the L1 held the planner seat; residual 0. Seat outputs under `.ufo/waves/round-73/w1/`.
  `M1Mutation` closed last: 38 clause-isolated mutants (21 counter, 17 checker), 6 survivors — all dead or
  entailed clauses — and two further instrument defects (a non-map `snapshots` crash, a token passed from a block
  heading) that were repaired before this write (`w1/M1Mutation/report.md`, `w1/M1Mutation/{counter_matrix.json,c2_matrix.json}`).
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only orchestrator-owned
  `.scratch/` changes and a pre-existing 24-byte `after` file (timestamp 20:05, content "== SCORECARD diff
  base-", authored by an earlier lane's redirect); no round-73 seat file sits in the fleet root. Nothing moved.

## Landed changes

| commit | what | LOG entry |
|---|---|---|
| `74937132` | round-73 declaration: two frozen claims, the three v262 snapshots with `SHA256SUMS`/`SOURCES.json`, host readings, held-ground sweep, do-nothing controls, both instruments and their selftests, the instrument-change rule | LOG "Round 73" |
| `8eeadcb9` | wave w1 evidence: 12-seat spec, validated dispatch (`spawn 12`, band 8-16), ready handoff | LOG "Round 73" (wave) |
| `09dac09f` | C1+C2 landing: the note, five registry rows, `corpus/README.md`, the r72 lesson correction, `SCORECARD.md`, `SKILL.md`, `PROVINCE.md`, both instruments, the same-instrument receipts | LOG "Round 73" |
| `583eea87` | registry placement fix: the five new rows moved inside the Registry table (census E12), after receipt at `09dac09f` | LOG "Round 73" (R73-REGISTRY-ROWS-OUTSIDE-TABLE) |
| `3efb9b24` | measured outcome, lesson (`corpus/lessons/round-73.md`, ten mistake classes) and LOG entry, with the final-check receipt and the same-instrument control regenerated on the final instrument bytes | LOG "Round 73" |
| `b15f5167` | the checker's final bytes (absolute-path/FAIL-receipt/placeholder traps closed, thirteen selftest cases), the r72 digest-order correction and the count corrections in SKILL/README/lesson | LOG "Round 73" |
| `65cc1f17` | after receipt at the final tip (`met=1`, `ROUTED_STALE=0`, census rc 0, selftests 12 and 13) | LOG "Round 73" |
| `3cfa23ac` | the wave's 12 seat reports, matrices and `w1-results.json`; the instruments at their final bytes (counter 13 cases, checker 14) with the MAPLIST/TITLE-TOKEN repairs and the count corrections | LOG "Round 73" (wave) |
| `8985a817` | after receipt at the final tip (`met=1`, `ROUTED_STALE=0`, census rc 0, selftests 13 and 14) | LOG "Round 73" |

## Before → after measurements

| Claim | Before (base `eb105757`) | After (`3cfa23ac`) | Command |
|---|---|---|---|
| C1 | `UL_NOTE absent`, rc **128**; 0 UL rows; registry **303**; notes **90** | `UL_ROWS=6 UL_VERIFIED=6 UL_SOURCES=3 UL_SNAPSHOTS=3 UL_MALFORMED=0`, `met=1`, rc **0**; registry **308**; notes **91**; census rc **0** | `python3 tools/count-ul-rows-r73.py --revision <REV>`; `git show <REV>:corpus/SOURCES.md \| grep -cE '^ {0,3}\| *S[0-9]{3,}'`; `git ls-tree --name-only <REV>:corpus/knowledge \| grep -c '\.md$'` |
| C2 | `ROUTED_STALE=3`, rc **1** (all three items stale) | `ROUTED_STALE=0 ROUTED_OK=3/3`, rc **0** | `python3 tools/check-r72-routed-r73.py --revision <REV>` |

Receipts: `.ufo/waves/round-73/after/{measure-09dac09f,measure-583eea87,measure-b15f5167,c2-before-final-instrument,c2-final-instrument,r72-c3-same-instrument-before,final-checks}.txt`;
pre-data controls `.ufo/waves/round-73/before/{absence-controls,held-ground,host}.txt`. Selftest tallies at
the final bytes: counter `SELFTEST: PASS (13 cases, 13 passed, 0 failed)`; checker
`SELFTEST: PASS (14 cases, 14 passed, 0 failed)`.

## Sources & frontier

- **Census, before → after.** Round start: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate
  --root /home/vgpnk/Projects/shokunin tsukuroi` → rc **0**, **303** rows, **90** notes (W04 duplicate-URL
  warnings only). Round end at `583eea87`: rc **0**, **308** rows, **91** notes; every new row is `NF=13`.
- **Rows added:** **5** — tier A ×5 (three `mined` S304-S306: docs, code, code; two `rejected` S307-S308, the
  rendered Arch man page and the core package page, each refused with reason and flip after an opened fetch;
  measurement log in `w1/SC2Sources/rows.md`, refusals in `corpus/lessons/round-73.md` §Gate).
- **Rows touched old→new:** none — no existing row's `status`, `recheck` or `used-by` changed; the registry is
  append-only this round.
- **Frontier advanced:** the merge/precedence plane moved from unheld to Core for the documented reading; the
  entry's Frontier keeps the effective merged value of a named unit, the multi-directory mask decision
  (`load-fragment.c`, outside the snapshots), the instance `.d/` leg, `SYSTEMD_UNIT_PATH` and any host alias
  symlink unread.
- **Assimilation: none** — the open L0 `tsukuroi | round-64` keeps the `merge/tsukuroi/` package quarantined
  (the collision set S200-S281 against a registry now at S308). **considerthese:** no proposal is still
  unimplemented; the five items of `considerthese/2026-10-26.md` are accounted for (scoreboard r41+, seat-harm
  tally r66, patch-offset QUALITY 103 r69, burst-aware reading r46 record, propagation map r43/r54 partial).
- **Sourced claim:** C1 rests on S304-S306, all opened this round.

## Trend verdicts

- **expansion: improved.** Three admitted tier-A rows on ground the held-ground sweep reads as unheld, one
  admitted entry (UL1-UL6) citing them, registry 303 → 308, notes 90 → 91, and two opened refusals kept as
  taste evidence.
- **quality: improved.** The three round-72 routed defects close in committed bytes (`ROUTED_STALE=3` → 0)
  with a same-instrument 3 → 0 pair; both round-73 instruments were hardened by the wave's own attacks and
  carry thirteen and fourteen named selftest cases; four overreaching note rows were corrected before landing
  (`ROWS_HOLD` 2/6 → 6/6); the registry placement defect the census caught (E12) was fixed inside the round.
- **discernment: unchanged (author-side).** The wave found defects in every claim (R1Reviewer 2/6 rows on the
  first draft; E1Counter's `quote=""`; R2Reviewer/E2Routed's five checker survivors; K1Critic D1-D11;
  SC3Index F1-F4; S1Scout's mid-wave instrument-drift observation) and all are repaired or recorded as named
  limits. The outside admit/reject spot-check is owed by the closure judge, so no author-side uplift is
  claimed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the round-73 repair
  table T1-T6 rests on UL1-UL6 and cites `systemctl show -p NeedDaemonReload -p DropInPaths`, `systemctl cat`,
  `readlink -f` and `stat -c %s`; evidence `SKILL.md` "Round 73 — the systemd unit-load merge plane".
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round executed the plane
  end-to-end on this host (search path, masks, template/serial drop-ins, `is-enabled`) and logged it in
  `LOG.md` round 73 and `corpus/knowledge/systemd-unit-load-plane-r73.md` §Host readings.
- [~] Instructions executable by an agent without oral context — the note's Host readings carry the exact
  commands and observed values, and the SKILL table carries a read-only check per symptom; the whole-SKILL
  no-oral-context retest remains unexecuted (open L0 `tsukuroi | round-60`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round-73 Core entry names what is Core, what
  stays Frontier and what is operator-owned; the connector scan found no sibling owner
  (`w1/C1Connector/report.md`); the kaidoku/revenger arbitration stays open and is not absorbed.

**Stale-lane:** no — the respawn-per-round driver dispatched round 73 as the lane's next round; no other
mission of this lane is open.

**Tool installs:** none (curl, python3, git and the existing lane tools were sufficient); pacman untouched.
