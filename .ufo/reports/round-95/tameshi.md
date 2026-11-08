# tameshi round 95 — the reader's literal classes (coverage) and the audit's receipt bytes (calibration)

Lane `tameshi` (verification-fixture craft), round 95, attempt 1. Base `02ff6290945dde18062a366799a774abb50fb365`;
lane tip `cc41a31bf6e3a0241ab06ab6eb9011fde734e8f1` (branch `master`). Report filed by
`fleet-commit.sh --as tameshi`.

**Declared claims (2).** R95-C1 targets the **coverage** axis: the note reader now governs
five presentation classes it did not govern (indented code, a literal backslash before a
cell boundary, a one/two-hyphen delimiter, an exactly-one-pin-line rule). R95-C2 targets
the **calibration** axis: the disposition audit reads receipt bytes from the object store
and binds each receipt to the counter digest. Both were frozen before any scored receipt:
`plans/round-95.plan.md` (declarations + amendments A1-A9) and
`.ufo/waves/round-95/claims.json`, freeze commit `3ca1981a2265880ae3ce9b88d316e71741b02426`
(`.ufo/waves/round-95/freeze-rev.txt`).

## Work performed

- **Protocol load.** Read `skill://shokunin`, `kimi-shokunin/skills/shokunin/SKILL.md`,
  `protocol/` PROTOCOL, MISSION.md, AXES.md, CORPUS.md (SOURCES contract), LEARNING.md,
  the lane's SKILL.md, PROVINCE.md, SCORECARD.md, corpus/QUALITY.md, corpus/README.md
  `## Frontier`, and the newest lessons including the round-94 non-author spot-check
  (`corpus/lessons/round-94-verifier-spotcheck.md`) whose eight routed defects this round
  answers (`plans/round-95.plan.md` §Round-94 routed defects).
- **R95-C1 — coverage.** Built the successor reader
  `.ufo/evidence/round-95/c1/measure-v95.py` (sha256 `5f0d1770…`) with exactly the five
  plan changes: `^ {4,}\S` indented-code exemption (S323), `\\` before `\|` in
  `split_cells`, `-{1,}` delimiter (S321), a one-pin-line rule with the new setup token
  `self-pin-line-count`, and round-95 paths. Built the battery
  `.ufo/evidence/round-95/c1/controls-v95.py` (sha256 `b1a94edd…`) with the four new note
  states, the `double-pin` control, and a `counter_sha=` line in every receipt. The
  battery prints `C1_CONTROLS states=50 matched=50 mismatches=0 missing=0`, exit 0
  (`.ufo/evidence/round-95/pre-freeze/controls-run.log:52`).
- **R95-C2 — calibration.** Built the sealed checker
  `.ufo/evidence/round-95/conjunct-disposition-v95.py` (sha256 `d6cf94b4…`) and its
  19-row manifest (`c7328379…`): receipts read with `git cat-file blob <rev>:<path>`,
  `counter_sha=` bound to the counter blob, scrubbed `GIT_*`, `refs/replace` refusal,
  selftest 11/11. Built `c2-forge.py` for the three pre-registered forged artifacts.
- **Frontier step (§2b).** S320/S321/S322 re-opened and S323 admitted with fetch headers,
  snapshots and located quotes (`corpus/lessons/round-95.md` §Gate); one mistake class
  mined into `## Mistakes` (M1 the round-94 tally miss; M2/M3 the round's own two
  non-discriminating fixtures) and the records defects the wave found (R95SC1 D1-D3) fixed
  at `16cf0d58`. Census before/after in `.ufo/waves/round-95/census-before.txt` and below.
- **Wave `w1`, one v1 wave, 13 seats** (`.ufo/waves/round-95/w1-dispatch.json`
  `counts.total=13`): executor 4 (R95E1-E4), scribe 1 (R95SC1), scout 1 (R95S1),
  reviewer 2 (R95R1, R95R2), critic 1 (R95C1), mutation-tester 1 (R95M1), sentinel 1
  (R95SN1), connector 1 (R95CN1), revenger 1 (R95L1). Attack share 5/13 by the policy's
  role set, 7/13 including sentinel and connector. All 13 settled, no dead seat;
  `.ufo/waves/round-95/w1-results.json` records 13 results with `output: null` after the
  orchestrator kernel restart mid-wave, so the seat reports under
  `.ufo/waves/round-95/w1/` are the retained evidence. The L1 holds the planner seat
  (§3 mapping: planner → L1); no planner seat was dispatched.
- **Adversarial outcome.** R95R1 falsified the honest-note sentence at the first
  instruments commit `0685c358` (Gate quotes on lines that did not name their sid →
  `source=false`); the Gate was reflowed at `20fabad4` and the five fixtures were re-scored
  exit 0 (amendment A9). R95C1 falsified the summary token order (amendment A4). R95SN1
  measured 12 findings, two HIGH (hostile `PATH`; ambient non-`GIT_*` environment) and the
  driver/tool defects F2-F7 — declared in A6/A7 and routed to round 96, not silenced.
  R95E4 and R95M1 independently show the twelve round-94 rule-level survivors do not move
  (8 subsumed, 1 invariant-pinned, 3 ungraded): the round did not claim them.
- **Pre-file falsification ledger.** `.ufo/waves/round-95/claim-falsification.tsv`, 12 rows,
  both claims, all seven attack seats present; three `falsifies-wording` rows pointed at
  A4/A7/A9. Gate: `PREFILE-FALSIFICATION: pass claims=2 rows=12 attack_seats=7 findings=0`,
  exit 0 (command and exact line below).

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Plan + w1 spec (13 seats) + dispatch + census before | Round 95 §Shape | `0d3fc99b36a8ea1f18356066425ecdb56fdad748` |
| Pre-data amendments A1-A3 + five before-state receipts (round-94 counter at `6a2a1fdd`) | Round 95 §R95-C1 before | `fea478197238cbd1842c580046191edb9f0fecdf` |
| Instruments: `measure-v95.py`, `controls-v95.py`, `conjunct-disposition-v95.py`, manifest, `c2-forge.py`, S320-S323 snapshots, lesson, S323 row + used-by appends | Round 95 §R95-C1/§R95-C2 | `0685c3586805a2f2aed07e0038239cf384c38c4c` |
| Lesson Gate reflow (R95R1 falsifier, A9) | Round 95 §Motivating evidence | `20fabad4dc64b2feff16853a4cce01d9b324f821` |
| Lesson S323 anchor names no S322 (source fixtures discriminate) | Round 95 §Frontier | `f219fb0c8c1eb09d53b44d5542ce9be90014cf8a` |
| Claims freeze (C1/C2 wording, shas, kill rules) + A4/A5 | Round 95 §Shape | `3ca1981a2265880ae3ce9b88d316e71741b02426` |
| Records fix: Gate line/word numbers, S323 row counts, A8 roster | Round 95 §R95-C1 after | `16cf0d583d79d780d0ed44a12d22d0fc1de5cf8b` |
| Pre-freeze records: 50/50 battery receipts with `counter_sha=` | Round 95 §R95-C1 after | `4bd1e88f3f488fa7d14fa3b2fb4943b80acfcf01` |
| Landing receipts (C1 honest, C2 positive/selftest/forges) + wave records + A9 | Round 95 §R95-C2 after | `3610b46c4168fba8b9b0a03b462c12e5f264f898` |
| Lesson Measurements, LOG r95, QUALITY 169-172, SCORECARD r95 + capability, nowork controls, ledger | Round 95 (whole entry) | `cc41a31bf6e3a0241ab06ab6eb9011fde734e8f1` |

LOG.md entry: `## Round 95 (2026-11-08) — two claims: the reader's literal classes
(coverage) and the audit's receipt bytes (calibration)` (`LOG.md`, appended at the last
commit). QUALITY 169-172 appended; SCORECARD round-95 record appended.

## Before → after measurements

### R95-C1 (coverage) — verified under the amended wording (A1-A4, A9)

Counting command (counter):

    python3 -I .ufo/evidence/round-95/c1/measure-v95.py --repo /home/vgpnk/Projects/shokunin/tameshi-shokunin --rev 4bd1e88f3f488fa7d14fa3b2fb4943b80acfcf01 --work <empty dir>

Before: round-94 counter at `6a2a1fdd` on the five fixtures —
`.ufo/evidence/round-95/pre-freeze/before-v94/` — exit 1 / 1 / 1 / 1 / 0:
`indent-code-row` `verdict_tables=false` + `dup:` badrows; `indent-token` `ids=false`
(`stray-verdict`); `escaped-backslash-pipe` `ids=false` (`width:9:cells=4`); the
two-hyphen delimiter `ids=false` (stray verdicts); the double-pinned counter runs to
`C1_R94_PASS=true`. The v95 counter at base prints `C1_SETUP spec-absent-at-rev`, exit 2
(`.ufo/evidence/round-95/pre-freeze/nowork/c1-nowork-base.out`).

After: `.ufo/evidence/round-95/landing/c1-at-records.out` prints
`C1_SUMMARY rev=4bd1e88f n=12 killed=5 survived=7 inconclusive=0 unstable=0 invalid=0
trivial=0 witnessed=7/7 note=present mismatched=0 badrows=0 verdict_tables=1`,
`C1_SOURCE S320=row:1,quote:1 S321=row:1,quote:1 S322=row:1,quote:1 S323=row:1,quote:1`,
`C1_R95_PASS=true`, exit 0. The five added receipts
(`.ufo/evidence/round-95/pre-freeze/controls/`) print exit 0 `C1_R95_PASS=true` for the
four presentation states and exit 2 `C1_SETUP self-pin-line-count` for `double-pin`.
Battery command:

    python3 -I .ufo/evidence/round-95/c1/controls-v95.py --lane /home/vgpnk/Projects/shokunin/tameshi-shokunin --rev f219fb0c8c1eb09d53b44d5542ce9be90014cf8a --base 02ff6290945dde18062a366799a774abb50fb365 --work <empty dir> --outdir <dir> --jobs 6

prints `C1_CONTROLS states=50 matched=50 mismatches=0 missing=0`, exit 0
(`.ufo/evidence/round-95/pre-freeze/controls-run.log:52`).

Measured commit: `4bd1e88f3f488fa7d14fa3b2fb4943b80acfcf01` (counter receipts; battery
receipts produced at `f219fb0c`, committed in the same records commit). The do-nothing
controls (`c1-nowork-base`, and the round-94 counter on the same five fixtures) do not meet
the target.

### R95-C2 (calibration) — verified under the amended wording (A5-A7)

Counting command (checker):

    python3 -I .ufo/evidence/round-95/conjunct-disposition-v95.py --lane /home/vgpnk/Projects/shokunin/tameshi-shokunin --rev 4bd1e88f3f488fa7d14fa3b2fb4943b80acfcf01 --min-falsifiable 17

Before: the round-94 checker at `6a2a1fdd` prints `findings=0`, exit 0 on
`forge-handwritten` (a receipt present only in the working tree) and `forge-counter-sha`
(a committed receipt with `counter_sha=` = 64 zeros), and on `forge-replace-ref` prints
`DISPOSITION_INSTRUMENT sha256=5f0d1770…` after reading the substituted counter
(`.ufo/evidence/round-95/pre-freeze/c2/forge-matrix.txt`). The v95 checker at base prints
`DISPOSITION_SETUP counter-absent-at-rev`, exit 2
(`.ufo/evidence/round-95/pre-freeze/nowork/c2-nowork-base.out`).

After: `.ufo/evidence/round-95/pre-freeze/c2/c2-pos.out` prints
`DISPOSITION rows=19 falsifiable=17 unfalsifiable=2 findings=0`, exit 0;
`c2-selftest.out` prints `DISPOSITION_SELFTEST: 11/11 pass`, exit 0. The forge matrix
prints 8 checks / 0 failed: `forge-handwritten` v95 exit 1
`DISPOSITION_FINDING receipt-absent-at-rev figure`; `forge-counter-sha` v95 exit 1
`DISPOSITION_FINDING receipt-counter-sha-mismatch mismatched0`; `forge-replace-ref` v95
exit 2 `DISPOSITION_SETUP replace-refs-present`; the round-94 checker prints `findings=0`
on both receipt forgeries in the same matrix. Every receipt the manifest's seventeen state
rows name carries `counter_sha=` equal to the counter blob at the records revision (the
`selfpin` row's receipt names the frozen counter whose pin is under test — plan §A6).

Measured commit: `4bd1e88f3f488fa7d14fa3b2fb4943b80acfcf01` (forges at the same revision).

## Sources & frontier

Census command (run from the fleet root):

    /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi

Before (round start, `exit=0`; `.ufo/waves/round-95/census-before.txt`): rows 182; tiers
A=164 B=14 C=4; status mined=148 queued=23 rejected=11.
After (round end, `exit=0`): rows **183**; tiers **A=165** B=14 C=4; status
**mined=149** queued=23 rejected=11.

Rows touched (old → new, logged in `corpus/lessons/round-95.md` §Registry changes):
S320, S321, S322 `used-by` += `corpus/lessons/round-95.md` (status unchanged, `mined`);
S323 added (`mined`, `used-by` = the lesson). The census prints one new `W04 S323 duplicate
url spec.commonmark.org/0.31.2 across scopes` warning — the round-95 snapshot is the same
page bytes as S322 under a different scope (§4.4 vs §4.5); the existing W04 class does not
fail the gate.

Frontier rows advanced: S323 (CommonMark §4.4 indented code) enters as a mined row and
grounds the new literal-class rule; the indented class moves from ungoverned to governed on
the lane's own reader. No `corpus/knowledge/` entry was added, so no frontier ground moved
to `held` (see the expansion verdict).

Sources: 1 new row (S323), 3 re-opened (S320/S321/S322), 0 rejected. Each new row has its
URL, access date 2026-11-08 and a ≤25-word located quote in the lesson's `## Gate`.

Assimilation: none — no `merge/tameshi/` theme was adopted this round (the round's claim
slots went to the routed instrument items).

## Pre-file falsification gate (Amendment 59)

    python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane tameshi --round 95
    PREFILE-FALSIFICATION: pass claims=2 rows=12 attack_seats=7 findings=0

Exit 0. Ledger: `.ufo/waves/round-95/claim-falsification.tsv` (12 rows; C1 and C2 both
covered; all seven attack seats — R95R1, R95R2, R95C1, R95M1, R95SN1, R95CN1, R95L1 —
appear; three `falsifies-wording` rows pointed at `plans/round-95.plan.md` §A4, §A7, §A9).

## Trend verdicts

- **expansion: unchanged.** No `corpus/knowledge/` entry was added (`git diff
  --name-status 02ff6290 cc41a31b --diff-filter=A -- corpus/knowledge/` → empty); the one
  new source row is a registry row, and CORPUS.md rule 4 counts expansion as admitted
  knowledge entries on uncovered ground, which this round did not land. Frontier ground
  advanced: S323 (indented literal class) is now mined and governs the reader.
- **quality: improved.** Two instruments were strengthened with measured before/after:
  the note reader's battery grew 45 → 50 states (50/50) and the audit now reads receipt
  bytes from the object store, refusing both forged sets that the round-94 checker
  accepted (`findings=0` there, exit 1 here). QUALITY 169-172 appended, each with an
  "Able to fail" receipt. Caveat: the round adds no rule-level kill (R95M1/R95E4 show the
  twelve survivors do not move), and the sentinel's F2-F7 remain open and routed.
- **discernment: improved.** The round's own wave falsified two sentences of the record
  before filing (Gate layout → A9 and reflow; summary token order → A4), and three
  record-number defects the scribe found (D1-D3) were fixed at `16cf0d58` rather than
  glossed. The do-nothing controls caught two non-discriminating fixtures (M2/M3). The
  honest part: R95SN1's two HIGH findings (hostile `PATH`, ambient environment) are real
  and are declared as limits (A7), not claimed as protected.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  pointer: `corpus/lessons/round-95.md` §Gate (four sourced rules) and QUALITY 169-172;
  the round-95 reader itself is the executable checklist. No independent promoter review.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer:
  `LOG.md` `## Round 95` (wave `w1`, 13 seats; battery 50/50; C2 11/11; forge matrix 8/8).
  No independent promoter review.
- [~] Instructions executable by an agent without oral context — pointer:
  `plans/round-95.plan.md` §Controls + `.ufo/waves/round-95/w1/specs/R95E1.md`-`R95L1.md`
  (13 seats executed from the written specs; no oral context). No independent promoter
  review.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: the round edits only
  `tameshi-shokunin` (`corpus/`, `.ufo/`, `plans/`); R95CN1 records sibling parsers as
  read-only divergences and edits none. No independent promoter review.

## Wave accounting

- **Shape:** one v1 wave `w1`, 13 seats, under `scripts/hyaku/ufo-wave-policy.json`
  (band 8-16, `counts.total=13`); attack share 5/13 by the policy's role set, 7/13 with
  sentinel and connector. No residual call; round total 13 seats.
- **Dead seats:** none. All 13 seats settled and wrote their reports; the wave results
  file records `output: null` after the kernel restart, and the reports are the evidence.
- **Seat verdicts:** R95E1 `reproduced`; R95E2 `reproduced`; R95E3 `reproduced`; R95E4
  `classified` (8 subsumed, 1 invariant-pinned, 0 killed-by-state, 3 ungraded); R95SC1
  `drafted` + D1-D3; R95S1 `agree`; R95R1 `FALSIFIES-WORDING` (fixed A9, re-scored); R95R2
  `conforms-with-findings`; R95C1 `falsified 2 / holds 9` (A4/A9); R95M1 `26 killed / 12
  survived / 0 inconclusive`; R95SN1 `findings:12` (F1-F8 routed, F9-F12 limits); R95CN1
  `diverges`; R95L1 `inert:4/4`.

**Stale-lane:** respawn-per-round driver; no other mission of this lane is open. No L0
question was opened this round. Tool installs: none (python3 3.14.8, git 2.56.0, curl were
already present; pacman untouched).

## Addendum — filing record

- Lane tip at filing: `cc41a31bf6e3a0241ab06ab6eb9011fde734e8f1` (branch `master`;
  `git -C tameshi-shokunin ls-remote origin refs/heads/master` prints that hash).
- This report was first committed on the fleet repo as
  `dfe5d4d6ac0e1c013889574b7ba4610e96621eda` (`fleet-commit.sh --as tameshi`), after the
  lane tip and after the pre-file gate passed.
- Pre-file gate at filing: `PREFILE-FALSIFICATION: pass claims=2 rows=12 attack_seats=7
  findings=0`, exit 0.
