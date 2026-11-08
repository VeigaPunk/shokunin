# souji — round 88 report

Lane: `souji-shokunin` (lane repo `/home/vgpnk/Projects/shokunin/souji-shokunin`). Round 88, attempt 1.
Lane base `7defe9c5fee3df07e403666bdeccfb88428ef729`. Instruments/controls P
`e60ea25f6dc6d988bbdd713a2d00718f5915e29d`; preregistration alone F
`f74092b24bbddf2e5259977c254c91b7a6b71160`. Wave evidence `.ufo/waves/round-88/w1/`.

Round shape: one v1 wave of 10 seats under `scripts/hyaku/ufo-wave-policy.json` (band 8–16), 5 attack seats
(critic, reviewer, mutation-tester, sentinel, connector), 2 executors, 1 scribe, 1 scout, 1 simplifier; no residual
call; round total 10. The L1 (`SoujiR88`) holds the canonical planner seat; no `planner` seat was dispatched.

## Work performed

Declared claims: **C1 (calibration 7)** — the two clauses the r87 population left reachable-and-unrowed get one
frozen binding each (NF6g the `_whole` before-byte half, LD1 the `_ledger` duplicate-id refusal), the third named
clause (`_capture_ok`'s `len(want) <= len(have)`) is measured dead and recorded as a belt; **C2 (operability 8)** —
the K4 delegation's index-flag failure detail becomes one escaped physical line that keeps both ends of the writer's
stderr.

- **C1 instruments landed (P).** `census/round-88/c1-false-rows.tsv` (53 rows = the r87 51 byte-for-byte, in order,
  plus NF6g at fixture revision R11 and LD1), `c1-mutants.json` (12 members), `c1-mutants-dead.json` (13, the belt
  member m19), `c1-false-row-harness.py` (r88 pin, R11, `where=ledger` row type),
  `c1-clause-battery.py` (r88 pin). The counter under test is the **unchanged** r87 counter,
  `census/round-87/c1-pointer-counter.py` sha256 `fd0a8e24…` (verified at P and F).
- **C1 binding rows.** NF6g: the R11 declaration names the L06 token only as the suffix of `xtests/…/.git`, so the
  byte before it is a path character; only `_whole`'s before-byte half refuses the row (`m18-whole-before` drops it).
  LD1: the harness appends a second `P01` row to the frozen r77 ledger and expects `LEDGER-REFUSED id=P01` and exit
  1 (`m17-duplicate-id` drops `r[0] in ledger`). Evidence: `census/round-88/records/c1-after.txt`,
  `controls/c1-before.txt`, `records/c1-dead-belt.txt`.
- **C1 do-nothing control committed before F.** `census/round-88/controls/c1-before.txt`: the same battery and the
  same twelve mutants on the r87 51-row population kill ten and leave m17/m18 alive, EXIT 0.
- **C2 repair.** `tools/souji-record-agreement.py`: the embedded bootstrap now ships the delegated `ls-files` read's
  raw stderr base64-framed; the parent decodes it (`validate=True`, fail-closed on invalid base64) and renders it
  through the new `_one_line` (`_escape_text` first, then head-100/`…`/tail-99 at a 200-character excerpt bound). The
  `WRITER`-line/ REFUSED/ FORGED/ CLEAN branches are unchanged. Evidence: `census/round-88/records/c2-after.txt`,
  `controls/c2-before.txt`, `records/c2-k4-regression.txt`.
- **C2 control.** `census/round-88/controls/c2-before-tool.py` is the r87 tool byte-for-byte
  (`e1b00e8a…`); `tests/fixtures/r88-k4-flagfail.py` runs seven cases through a tool copy beside a fake writer and
  scores both tool versions.
- **Sources and docs.** S348 (Python `str.splitlines` boundary list) admitted, S349 (Python `base64`) rejected with a
  flip; `corpus/knowledge/one-escaped-diagnostic-line.md`; `corpus/QUALITY.md` Q163; `plans/round-88.md`;
  `corpus/lessons/round-88.md`; `SCORECARD.md` r88 rows, two capability rows and the r89 planned block; `LOG.md`
  round-88 entry.
- **Wording narrowings before filing.** The wave falsified six sentences; they are narrowed in `plans/round-88.md`:
  the harness's `where=ledger` branch IS judgement code for LD1 and the belt is empirical, not a proof (A1); the
  200-character bound is the excerpt, not the whole 259-character K4 cell (A2); the escape set is C0/DEL/NEL/LS/PS,
  not every C1 control (A3); LD1's kill is the missing marker, not an exit-code delta (A7); and each new row binds
  ONE spelling of its clause — NF6g the alnum predecessor, LD1 the target-equal duplicate, with NF6h/NF6i/LD1b/LD2
  carried (A8). Documentation fixes (A4–A6): the provenance quote is checked against the rendered capture, S348's
  `teaches` cell no longer asserts a list its quote does not enumerate, Q163 corrects Q161's stale tail-only clause,
  and S349's word count is 15.
- **Wave.** `.ufo/waves/round-88/w1/` — 10/10 seats settled (`w1-results.json`), no dead seat: executor ×2
  (`S88ExecC1` re-derived both C1 arms and the per-row attribution; `S88ExecC2` re-derived both C2 arms, ran the r87
  regression and five frame attacks, all pass), mutation-tester (`S88MutCounter`: both new rows load-bearing; two HIGH
  spelling gaps and two MEDIUM unrowed legs → A8), critic (4 NARROW → A1–A3), reviewer (AGREE on all five ends), sentinel
  (NEUTRAL; F1/F2 → A9, F3/F4 carries), connector (separability PROVEN with two scratch clones; carry audit;
  D4/D6 → S350 and the K4 docstring), scout (S348/S349/S350 open, the C1-control repro → A3, the S278 overlap → A4),
  scribe (F1/F3 documentation corrections → A6), simplifier (deletion audit; `_one_line`/`_stderr_tail` dedup and the
  battery defaults' patches carried to r89). Spec `w1-spec.json`, validated dispatch `w1-dispatch.json`, ready handoff
  `w1.ready` (`.dispatched` 08:27:34).

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| C1 population (53 rows), 12+1 mutants, harness (R11 + `where=ledger`), battery, the C2 fixture, controls and both before receipts, S348/S349, Q163, the knowledge entry | round-88 entry, bullets "Claims", "Sources", "Docs" | `e60ea25f6dc6d988bbdd713a2d00718f5915e29d` (P) |
| the preregistration, alone | round-88 entry, "Claims" | `f74092b24bbddf2e5259977c254c91b7a6b71160` (F) |
| wave-1 spec, validated dispatch and the ready handoff | round-88 entry, "Wave" | `ce29e5bca6f862dcb341170dfd80e9bf0b2bd8eb` |
| C2 repair (base64 frame + `_one_line`), the C2 after receipt and the r87 12-row regression | round-88 entry, "Measured" | `01a2fa559a0d900e28b4b3dda8a504ca935b584c`, docstring corrections and re-run receipts `72edae40…` and `f62eeb85…` |
| C1 after and belt receipts | round-88 entry, "Measured" | `486826df9da614bb6619e90748b7e9014bf266b1` |
| wave evidence (10 seat reports + receipts), plan amendments A1–A9, lesson, SCORECARD/LOG/QUALITY, pre-file ledger | round-88 entry, all bullets | `ac61ca1ec52fd451a1393bddb6736466004d627a` (final lane commit, pushed) |

## Before → after measurements

### C1 — calibration 7

Counting command (one, both ends; run from the lane root, `WORK` an empty dir outside `/tmp`):

```
after:  python3 -B census/round-88/c1-clause-battery.py --counter census/round-87/c1-pointer-counter.py \
          --work WORK --only r87,r88 --expect-killed 22
before: the same battery/counter/mutants with --only r87 --expect-killed 10
belt:   the after command with --mutants census/round-88/c1-mutants-dead.json
```

| end | receipt | observed | exit |
|---|---|---|---|
| before (do-nothing: twelve mutants on the r87 51 rows) | `census/round-88/controls/c1-before.txt` | `ARM pristine pop=r87 rows=51 mismatches=0 errors=0 exit=0`; `m17-duplicate-id killed=no`; `m18-whole-before killed=no`; `SUMMARY mutants=12 sets=r87 pristine_r87=ok killed_r87=10 killed_total=10` | 0 |
| after (53 rows) | `census/round-88/records/c1-after.txt` | `ARM pristine pop=r87 rows=51 mismatches=0 errors=0 exit=0`; `ARM pristine pop=r88 rows=53 mismatches=0 errors=0 exit=0`; twelve `killed=yes` on r88; `SUMMARY mutants=12 sets=r87,r88 pristine_r87=ok pristine_r88=ok killed_r87=10 killed_r88=12 killed_total=22` | 0 |
| belt (13 members) | `census/round-88/records/c1-dead-belt.txt` | `m19-len-half killed=no` on both sets; `SUMMARY mutants=13 … killed_r87=10 killed_r88=12 killed_total=22` | 0 |

Measured against the instruments at P `e60ea25f` (identical bytes at F `f74092b2`); receipts landed at
`486826df9da614bb6619e90748b7e9014bf266b1`.

### C2 — operability 8

Counting command (one, both ends):

```
after:  python3 -B tests/fixtures/r88-k4-flagfail.py --tool tools/souji-record-agreement.py \
          --before census/round-88/controls/c2-before-tool.py --work WORK
before: the same fixture with the r87 tool bytes as BOTH --tool and --before
```

| end | receipt | observed | exit |
|---|---|---|---|
| before (r87 tool `e1b00e8a…`) | `census/round-88/controls/c2-before.txt` | `SUMMARY cases=7 tool_pass=3 before_pass=3`; KFF2/KFF3/KFF4/KFF5 fail | 1 |
| after (filed tool `4042218f…`) | `census/round-88/records/c2-after.txt` | seven `CASE … tool=pass`; `SUMMARY cases=7 tool_pass=7 before_pass=3` | 0 |
| regression (r87 12-row counter on the filed tool) | `census/round-88/records/c2-k4-regression.txt` | `SUMMARY rows=12 mismatches=0 errors=0` | 0 |

Measured against the filed tool at `f62eeb852250e6bd5fc48af428b2800df1999dc6` (the after and regression receipts were re-run there after the `_one_line` docstring correction, A5).

| claim | counting command | measured commit |
|---|---|---|
| C1 | `python3 -B census/round-88/c1-clause-battery.py --counter census/round-87/c1-pointer-counter.py --work WORK --only r87,r88 --expect-killed 22` | `486826df9da614bb6619e90748b7e9014bf266b1` |
| C2 | `python3 -B tests/fixtures/r88-k4-flagfail.py --tool tools/souji-record-agreement.py --before census/round-88/controls/c2-before-tool.py --work WORK` | `f62eeb852250e6bd5fc48af428b2800df1999dc6` |

## Sources & frontier

`SOURCES.md` rows: before **270**, after **273** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md`; registry `270 → 272`). Rows added by tier: tier A `docs` 3 (S348 admitted `mined`; S349 and
S350 rejected). Rows touched old→new: S348 new `mined` (used-by `corpus/knowledge/one-escaped-diagnostic-line.md`),
S349 and S350 new `rejected` (no used-by); no existing row's status/recheck/used-by changed. Frontier rows advanced: F4? none —
this round is instrument masonry, not a PROVINCE frontier promotion; F1–F5 keep their statuses.

Census commands and outputs: before (reconstructed at the lane base; method disclosed in `plans/round-88.md` A0.4)
`census/round-88/records/sources-census-before.txt` → `file ok`, `EXIT=0`, 87 pre-existing W04 warnings; after
`census/round-88/records/sources-census-after.txt` → `souji ok`, `EXIT=0`, 88 W04 (the new S350 duplicate-URL line). Full form:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`.

Assimilation: none this round (no `merge/souji/` theme admitted); `considerthese/` is absent in this lane.

Curation: S348 overlaps S278 (Python 3.12 page, hidden-line-numbering consumer) by page content; the scout
re-fetched both and the boundary tables are byte-identical. S348 is kept because it is the host interpreter's page
(3.14.8, the version the entry's recheck names) for the escaping consumer; no third row for the same page was added
(`plans/round-88.md` A4).

r87 spot-check routed defects: **D4** (a rejected Gate row was not written for `core.quotePath`) is closed by S350,
a rejected SOURCES row with its flip opened this round from the installed page and landed at `f62eeb85`; **D6** (a roff line citation) is
answered by S346's scope cell (roff 211-217 vs 698), and the connector's second D6 (the K4 docstring said
`--porcelain`, not `--porcelain -z`) is corrected on the final tool bytes (`plans/round-88.md` A5/A6).

## Trend verdicts

- **expansion: improved.** Two sources opened and one admitted (`S348`), one rejected with a flip (`S349`), and one
  new knowledge entry (`corpus/knowledge/one-escaped-diagnostic-line.md`); registry 270 → 272. The C1 population
  gains two rows (53) and the mutant set two members (12 filed, 13 with the belt).
- **quality: improved.** C2's delegated failure detail is now one escaped line with both ends kept, measured through
  the public path (7/7 after, 3/7 before) with the r87 12-row counter unchanged; Q163 records the rule; the C1
  instrument keeps one pin per population and the unchanged counter.
- **discernment: improved.** A carried clause was measured dead rather than rowed (m19 survives both sets), the
  do-nothing control is committed before F and beats nothing (10 < 22), and the wave's critic forced four wording
  narrowings (A1–A3) that the round now carries instead of the wider sentences.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. The r88 round is the lane's only in-flight work.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the classify/removal tables
and the Q163 rule this round adds are grounded in S348 and the r88 records under `census/round-88/`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round-88 entry with the two frozen
commands and their receipts; `.ufo/waves/round-88/w1/S88ExecC1.md`, `S88ExecC2.md`.
- [~] Instructions executable by an agent without oral context — `census/round-88/preregistration.txt` carries both
commands, both controls and the kill rules; the wave seats re-derived them from the files alone.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the connector's sibling-overlap section
(`.ufo/waves/round-88/w1/S88Connector.md`) and PROVINCE.md's boundary notes; no credential, host-repair or orchestration
work was absorbed.

## Extras

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Inherited state:** the round directory was absent at start (attempt 1, no `lane-dead-no-report` line for r88);
  nothing was inherited and nothing was reverted. Seats wrote no file into the fleet root (misroot sweep before the
  report: no untracked fleet path names this lane or round).
- **Dead seats:** none — all 10 seats settled and wrote reports (`w1-results.json`); no substitute or duplicate seat was
  spawned.
- **Pre-file falsification:** `python3 scripts/hyaku/prefile-falsification.py --lane souji --round 88` →
  `PREFILE-FALSIFICATION: pass claims=2 rows=13 attack_seats=5 findings=0`, EXIT 0 (`.ufo/waves/round-88/
  claim-falsification.tsv`); every attack seat appears in the artifact column (critic, mutation-tester, reviewer,
  sentinel, connector).
- **Tool installs:** none. No pacman (paused host-wide), no uv/npx/binary fetch, no sysctl, sudo or kernel change.
- **L0 questions:** none opened this round.
