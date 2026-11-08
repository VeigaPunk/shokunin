# souji round 87 — two clauses r86 measured reachable-but-unrowed get their rows (calibration); K4 reads NUL status records, names its writer delegation and keeps the exception line (operability)

Attempt 1 (`SoujiR87`). Lane base `5e288bb3152328f371325d0bf4fee7309d629991` (r86 closed `admitted`; non-author
spot-check `corpus/lessons/round-86-verifier-spotcheck.md`, its routed defects 5–10 and status-neutral list D1–D3).
Frozen claims, instruments, predicates, kill rules and stated limits are in `census/round-87/preregistration.txt`
(F `6ed2d368dc416f6409ac181e0ea45e23da82f89e`); the round's amendments are in `plans/round-87.md` (A0.1–A0.4 and the
wave-driven ones) and the pre-file ledger in `.ufo/waves/round-87/claim-falsification.tsv`.

**Declared claims (1–3, each one axis-move).**
- **C1 — calibration 7** (the lane's lowest owned non-retired axis): the false-row population certifies a counter
  clause only when a frozen row turns a clause-dropping single-edit mutant red. The two clauses r85/r86 measured
  reachable-and-unrowed — the R0 guard's token-on-line half (`S85MutCounter` m12) and `_whole`'s sentence-end
  punctuation disjunct (m16) — get one row and one mutant each (TQ1 at fixture revision R10; NE1 at the harness's
  frozen `BASE e65538e7…`, its R0 blob read at the item population's base `705fa138…`); a third candidate
  (`_capture_ok`'s suffix comparison) was measured **already bound** by the r86 row NF12c and is reported, not added.
  Each new row binds one spelling of its clause, and the limits are narrowed in `plans/round-87.md` A4/A7.
- **C2 — operability 8**: `tools/souji-record-agreement.py` K4 (a) reads `git status --porcelain -z`, escapes each
  record path injectively and skips a rename/copy's second NUL field by the status letters, (b) prints the receipt
  writer's path and sha256 so its delegation is named, and (c) reports the last non-empty line of the writer's stderr
  (or of its output when stderr is empty), compacted from both ends when that line exceeds the bound — closing the
  three residual defects the r86 wave measured in the same key (S86ExecK4 §2b, §2e, §3b2). Final limits: `plans/round-87.md` A3/A5/A7.

## Work performed

- **C1 instruments (calibration).** Built the r87 clause battery (`census/round-87/c1-clause-battery.py`), the
  false-row harness successor (`c1-false-row-harness.py`, fixture revision R10), the counter successor
  (`c1-pointer-counter.py`, one population pin + `ERROR` in the forged-expectation set) and the ten-member mutant set
  (`c1-mutants.json`); population `c1-false-rows.tsv` is the r86 49 rows byte-for-byte plus `TQ1` (TRUE
  `QUARANTINED`, item L06, target `.ufo/quarantine/round-17/tests/vault/vadv54-run/p/p6repo/lemma-stub`, declaration
  ending `.git.`) and `NE1` (item `I87E`, `LOG.md:3166` where its token is absent — the row expects the diagnostic
  class `ERROR`). Evidence: P `77ccef7c5de2ad015f28da70fd58e1156c0f5b73`; population sha256 `b066fa0f…` (51 rows),
  mutants `9368b342…` (10 members), items `ce80195d…` (5 items, base `705fa138`).
- **C1 wave measurement (A4).** `S87MutCounter` scored eight alternative single edits of the two clauses plus four
  further drops from the r85 survivor list. The two new rows are the unique r87 killers of their filed mutants
  (m12 → NE1 only, m16 → TQ1 only; both alive on all 49 r86 rows), and four survivors the frozen limits did not name
  are reachable-and-unrowed — p2 (token-on-line at basename granularity), p3 (`_whole`'s `after[1]` lookahead), p7
  (`_regular`'s symlink leg), p8 (`token_ok`'s hyphen marker) — while p6 (`bool(want)`) is measured dead over 161,472
  pairs. All four are carried; the claim's limits are amended accordingly (`plans/round-87.md` A4).
- **C1 negative result (Q162).** Scored the planned third candidate mutant before adding its row:
  `c8-capture-suffix` is already killed on the r86 49-row population by row NF12c
  (`census/round-87/records/c1-c8-measured.txt`, `rows=49 mismatches=1`, the mismatching row named). The row was
  dropped before the freeze; the prereg records it (`plans/round-87.md` A0.1).
- **C1 measurement.** Before arm `census/round-87/controls/c1-before.txt` (same counter, same ten mutants, r86
  population): `killed_r86=8`, `m12-token-on-line killed=no`, `m16-nf6b-punct killed=no`, EXIT 0. After arm
  `census/round-87/records/c1-after.txt`: both pristine arms green, ten `killed=yes` on r87,
  `killed_r86=8 killed_r87=10 killed_total=18`, EXIT 0.
- **C2 repair (operability).** `tools/souji-record-agreement.py` (final sha256 `aac9a9ed…`): `_stderr_tail()` reports
  the last non-empty stderr line and keeps both ends of an over-long one; `writer_binding()` prints
  `# writer path=… sha256=…`; K4's status arm runs `git status --porcelain -z` over bytes, escapes each path
  injectively (`\\` doubled, LF/TAB/CR → `\n`/`\t`/`\r`, other non-printable bytes → `\xNN`), and skips a
  rename/copy's second NUL field by the status letters. Committed `6e502c5c`, then the wave repairs `578cbf2c` and
  `89d36922` (plans/round-87.md A1/A3).
- **C2 counter and arms.** Twelve-row counter `census/round-87/c2-k4-counter.py` (the r86 nine rows byte-identical
  plus KN1 silent writer, KN2 writer binding, KN3 untracked newline path). Before arm
  `census/round-87/controls/c2-before.txt` on the lane-base tool `cf875367…` with its byte-identical writer
  `70bbf1c2…` beside it: `mismatches=3` (KN1/KN2/KN3), EXIT 1. After arm `census/round-87/records/c2-after.txt`:
  `mismatches=0`, KN1 `named=yes`, KN2 `named=yes` (digest `70bbf1c2…` → `1b8ecf32…` on one appended comment byte),
  KN3 record exactly `bad\nname2.txt`/`uncommitted-path`/`??`, the nine r86 rows unchanged, EXIT 0.
- **C2 real-lane check.** On a `--shared` clone at `6e502c5c` the repaired tool reports the inherited K3 tally row
  only (`MISMATCH K3 corpus/README.md:1017 tally-disagree 3 refused != receipt 0 refused`, r86 A4) and **no K4 row**
  (`census/round-87/records/c2-real-lane.txt`) — the kill rule's last clause.
- **Frontier / sources.** Opened S346 (git-status(1) `-z`, roff line 698) and S347 (git-grep(1) `-F`, roff line 212)
  from the installed git 2.56.0-1 pages, captured under `census/round-87/srcs/`; one duplicate-scope candidate
  rejected with its flip condition. New knowledge entry `corpus/knowledge/machine-parsed-path-spelling.md` (grounds
  both claims) and an append-only correction to `corpus/knowledge/own-tree-pointer-binding.md` naming the r86
  fixture-only target paths (three `LG-DANGLING-PTR` findings are that class).
- **QUALITY.** Q161 (a delegated failure is reported from the tail of stderr) and Q162 (score the candidate mutant
  before adding the row).
- **Wave.** One v1 wave, 12 seats, policy `scripts/hyaku/ufo-wave-policy.json` (band 8–16): executor ×3,
  mutation-tester, simplifier, scribe, scout ×2, connector, reviewer, critic, sentinel. Attack seats 5/12 (42 %, over
  the 25 % floor, connector counted); one connector. **Dead seats: 0** — `.ufo/waves/round-87/w1-results.json` lists
  all 12 settled with no failure status. The L1 holds the canonical planner seat (the validator's `SWARM_ROLES` has no
  `planner`); the wave's planning data-walk rode the two scouts and the connector. The wave produced five repairs the
  round would not have found alone (plans/round-87.md A1/A3/A5/A8/A9) and four new carried limits (A4/A7/A10); the
  falsification ledger is `.ufo/waves/round-87/claim-falsification.tsv` (10 rows, 5 attack seats, gate
  `PREFILE-FALSIFICATION: pass claims=2 rows=10 attack_seats=5 findings=0`).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| r87 instruments, populations, mutants, controls and both before receipts | `## Round 87` bullet 1–2 | P `77ccef7c5de2ad015f28da70fd58e1156c0f5b73` |
| preregistration (frozen claims, predicates, kill rules, limits) | `## Round 87` bullet 1 | F `6ed2d368dc416f6409ac181e0ea45e23da82f89e` |
| C2 repair: `-z` status arm, writer binding header, stderr tail | `## Round 87` bullet 3 | `6e502c5c05fd3ca4193883921ef0c9b79a7d36a7` |
| C2 wave repair 1 (bytes read, status-letter skip, CR) + 3-row byte arm | `## Round 87` bullet 3–4 | `578cbf2c9e5f88aa3e264fdee718b89062e3c034` |
| C2 wave repair 2 (injective record escape, both-ends stderr, delegated bytes) | `## Round 87` bullet 3 | `89d369227ae8d89f9f014ff72cc1eb61ed606706` |
| C2 reviewer corrections (stderr preference, comment, c8 mutant filed) | `## Round 87` bullet 4 | `b0a64c943e22acc70da46ec8c9e688e842a42be4` |
| C2 byte arm mechanism rows KB6/KB7 + lane-base layer; A8 | `## Round 87` bullet 4 | `1556010bcd91bb803f4859135047329572948392` |
| C2 sentinel repairs (TOCTOU, CLEAN gate, REFUSED escape, U+2028) + A9 | `## Round 87` bullet 3 | `f36fcf55f6dcdadc4998d2f6c985e2351aaadb9e` |
| wave evidence (12 seat reports + receipts), after receipts, sources, knowledge, QUALITY, SCORECARD, PROVINCE, plans, lesson, LOG | `## Round 87` bullets 2–6 | `749c7829c98a379d4ebe60ae83226a096d48972d`, `c23a4b529a30195ad828ee653dbe39cf65ff4920` |

The final tool bytes are `e1b00e8a…`; the final counter/battery/harness bytes are the ones pinned at P and cited in
the prereg's instrument block (unchanged since P), so the C1 numbers have one anchor and the C2 numbers one tool. A
third planned C1 row was measured already bound and dropped before the freeze (A0.1); the review's and the wave's
wording gates are recorded in A4/A7/A8/A10.

## Before → after measurements

**C1 — calibration 7.** Counting command (frozen, one per end):
`python3 -B census/round-87/c1-clause-battery.py --counter census/round-87/c1-pointer-counter.py --work WORK --only r86,r87 --expect-killed 18`
(after) and the same with `--only r86 --expect-killed 8` (before).

| end | receipt | observed | exit |
|---|---|---|---|
| before (do-nothing: ten mutants on the r86 49 rows) | `census/round-87/controls/c1-before.txt` | `ARM pristine pop=r86 rows=49 mismatches=0 errors=0 exit=0`; eight `killed=yes`; `m12-token-on-line killed=no`; `m16-nf6b-punct killed=no`; `SUMMARY mutants=10 sets=r86 pristine_r86=ok killed_r86=8 killed_total=8` | 0 |
| after (51 rows) | `census/round-87/records/c1-after.txt` | `ARM pristine pop=r86 rows=49 mismatches=0 errors=0 exit=0`; `ARM pristine pop=r87 rows=51 mismatches=0 errors=0 exit=0`; ten `killed=yes`; `SUMMARY mutants=10 sets=r86,r87 pristine_r86=ok pristine_r87=ok killed_r86=8 killed_r87=10 killed_total=18` | 0 |

Measured against the instrument bytes at P `77ccef7c`. The delta is exactly the two rows: TQ1 kills
`m16-nf6b-punct` through `_whole`'s punctuation disjunct, NE1 kills `m12-token-on-line` through the R0 diagnostic
expectation, and neither mutant is killed by any of the 49 r86 rows.

**C2 wave-repair arm (outside the frozen 12 rows).** `python3 -B census/round-87/c2-byte-arm.py --tool TOOL --work WORK`
over seven shapes the frozen counter does not carry (non-UTF-8 name, CR name, rename whose source looks like a status pair,
400-character `AttributeError`, LF-vs-backslash-n injectivity, a name holding `"`, and a `ValueError` last line).
Three layers, one command: the lane-base tool reads `mismatches=8` of 10 (`controls/c2-byte-arm-lane-base.txt`), the
first repair bytes `6e502c5c` read `mismatches=8` (`controls/c2-byte-arm-before.txt`), and the filed bytes read
`rows=10 mismatches=0` (`records/c2-byte-arm-after.txt`). KB1/KB6/KB7 exist because the 12-row counter cannot certify
(a)'s mechanism or (c) (`S87ExecEvade` F4-F6; `plans/round-87.md` A8), and KB8-KB10 (a VT name, and a LF vs a literal
backslash under the index-flag arm) because the sentinel's F4 and the scribe's F8/F9 measured the same tear/collision
on the detail arm (`plans/round-87.md` A9).

**C2 — operability 8.** Counting command:
`python3 -B census/round-87/c2-k4-counter.py --tool tools/souji-record-agreement.py --work WORK` (after) and the same
with `--tool census/round-87/controls/c2-before-base-tool.py` (before).

| end | receipt | observed | exit |
|---|---|---|---|
| before (lane-base tool `cf875367…`, writer `70bbf1c2…` beside it) | `census/round-87/controls/c2-before.txt` | `SUMMARY rows=12 mismatches=3 errors=0`; KN1 `named=no` (detail truncated before the exception), KN2 `named=no` (no header), KN3 `named=no` (record `"bad\nname2.txt"` — git's quoted spelling); nine r86 rows unchanged | 1 |
| after (filed tool `e1b00e8a…`) | `census/round-87/records/c2-after.txt` | `SUMMARY rows=12 mismatches=0 errors=0`; KN1 `named=yes`, KN2 `named=yes` (`writer_sha=70bbf1c2a92e appended_sha=1b8ecf328ed3`), KN3 record `bad\nname2.txt`; nine r86 rows unchanged | 0 |

Measured against the tool bytes at `f36fcf55` (`e1b00e8a…`) and the counter sha256 `4e2b7c06…`; the lane's own
fixtures stay green on the repaired tool (`records/c2-regression-fixtures.txt`: r23 15/15, r24 8/8, r25 1/1).

## Sources & frontier

Census command (frozen): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`.
Before: `census/round-87/records/sources-census-before.txt` — `souji ok`, EXIT 0 (88 lines: 87 pre-existing W04
cross-scope duplicate-URL warnings and the ok line). After: `…-after.txt` — `souji ok`, EXIT 0, no `E0x` finding.
Registry `268 → 270` (`grep -cE '^\| *S[0-9]{3,}' corpus/SOURCES.md`): two rows added, one rejected, zero removed.

Rows added by tier: **tier A 2** (S346 git-status(1) `-z`; S347 git-grep(1) `-F`). Rows touched old→new: none (no
status/recheck/used-by change to an existing row). Frontier rows advanced: none — F1–F5 keep their statuses; the new
ground is instrument operability, not frontier movement, and `PROVINCE.md`'s r87 note says so.

`Assimilation: none` — this lane has no `corpus/`-external `merge/souji/` package taken this round and no
`considerthese/` directory exists in this repo. The lane is a child lane, so its frontier step is the `corpus/`
curation above (one sourced claim: C2 rests on S346, C1's declaration search on S347) plus the mined mistakes below.

## Trend verdicts

- **expansion — unchanged.** No PROVINCE move, no frontier row to Core, no new receipt class; the round adds
  instrument power (two rows, three K4 properties) and two registry rows on ground the lane already held.
- **quality — improved.** C2 turns three invisible fail-opens into measured rows (KN1 the exception line, KN2 the
  unnamed delegation, KN3 the quoted spelling) with the nine r86 rows as the no-regression arm and the real-lane run
  clean for K4; C1's two rows bind two clauses whose mutants survived every earlier population, and the third
  candidate's negative measurement keeps the population unpadded.
- **discernment — improved.** The round measured its own plan down before freezing (A0.1) instead of shipping a
  redundant row; it disclosed two pre-freeze after-runs and did not file them as evidence (A0.2); and it caught its
  own counter defect (A0.4) before the receipts were treated as data.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` classify rows
  and Gate registry as of r86, plus this round's `corpus/knowledge/machine-parsed-path-spelling.md` (S346/S347);
  no SKILL.md rule text changed this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 87` (measured arms,
  receipts, commits) and `census/round-87/records/`.
- [~] Instructions executable by an agent without oral context — `census/round-87/c1-clause-battery.py` and
  `census/round-87/c2-k4-counter.py` run from the frozen commands in this report; `plans/round-87.md` A0.1–A0.4 record
  the decisions a rerun needs.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` `## Round 87 boundary note`: two instrument
  behaviours in Core, no authority, no receipt class; credential-shaped content remains kagi's.

## Extras

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none this round (no pacman transaction; nothing installed or upgraded).
- **Open L0:** none raised this round.
- **Wave handoff:** `WAVE-DONE souji r87 w1` at 12/12 settled; no dead seat, no replaced seat, no second dispatch.
- **Gates run before filing:** `PREFILE-FALSIFICATION: pass claims=2 rows=10 attack_seats=5 findings=0` (exit 0);
  `tools/souji-landing-gate.py --rev 64079f21 --round 87` `findings=31 checked_reports=16` (all 31 inherited, none from
  this round); `tools/souji-pre-report-gate.sh` report/SHONEN/prereg PASS; `sources-census.sh validate` exit 0.
- **Trend/marker honesty:** a report that names real committed work but skips sections is `ok` plus a conformance
  defect; this report carries every required section.
