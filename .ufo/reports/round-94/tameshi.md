# tameshi — round 94

Lane `tameshi` (verification-fixture craft), L1 `TameshiR94`, attempt 1.
Base `a8f0e14bd400002324793d82030431696435d9a7`; instrument revision
`7084358c732ebe1334c2eb9a352c3ed96b547f7c`; freeze
`fdbd18c672afb0474a72ad90f9ba6604ddc34001`; pre-freeze records `33279f40`;
amendments A1-A8 `67b1ab85`, `6b19eb92`, `93164a68`.

## Work performed

Two declared claims, each an axis-move with its own falsifiable before→after:

- **R94-C1 (coverage)** — the fifth attempt at certifying the round-90 fleet-gate mutation
  case, under a reader that anchors the gate identity in its own self-pinned bytes
  (QUALITY 163), whose `coverage` scan is fence-aware with the note path as its own cell
  (QUALITY 164), and which reads the delimiter row and decides the remainder-row policy
  (QUALITY 165).
- **R94-C2 (calibration)** — conjunct disposition with a reason test that must name a
  declared battery state or a hex digest, plus a frozen `--min-falsifiable 17` floor
  (QUALITY 166).


**Wave accounting.** One v1 wave `r94-w1`, 12 seats: executor 3 (R94E1, R94E2, R94E3),
scribe 1 (R94SC1), scout 2 (R94S1, R94S2), reviewer 2 (R94R1, R94R2), critic 1 (R94C1),
mutation-tester 1 (R94M1), sentinel 1 (R94SN1), connector 1 (R94CN1). Attack share by the
policy's role set 4/12 = 33 %; counting sentinel and connector 6/12 = 50 %. All twelve
seats settled with deliverables, no dead seat:
`r94-w1-results.json` names all twelve. Attack share by the policy's role set
4/12 = 33 % (reviewer, critic, mutation-tester, 2 reviewers); counting sentinel and connector
6/12 = 50 %. No seat was replaced and no residual call was made. R94SC1 (scribe) drafted
three blocks — the note's status block (integrated as § Part 2, fixture-verified to move no
conjunct), a QUALITY criterion for the manifest binding, and the round-93 M2 correction —
and its block-3 work is the erratum mined this round (round-93 M2's receipt pointer names
no committed byte; QUALITY 168).

Frontier step (inside the 1–3 claim cap, not a fourth claim): S320, S321 and S322 re-opened
with byte-identical snapshots (`s321.html` sha256 `b153d814…a220` = round 93's); census
182 → 182 content rows, exit 0; four mistakes mined before the wave (M1-M4) and three after
it (M5-M7); R94-C1 rests on the re-opened S321 (delimiter and remainder rules) and S322
(fence rule extended to `coverage`).

Evidence pointers:
- Frozen plan, predicates, kill rules, state table, limits and amendments A1-A8:
  `plans/round-94.plan.md`.
- Frozen claims: `.ufo/waves/round-94/claims.json` (its `freeze` field reads `null` because
  a file inside the freeze commit cannot name that commit — `freeze-rev.txt` carries the
  revision; QUALITY 167).
- C1 instruments: `.ufo/evidence/round-94/c1/measure-v94.py` (sha256
  `a22563b0c2b4a2b43922cec3d1ab3fa511110e035b9edfdfdc6eaebb97023010`),
  `.ufo/evidence/round-94/c1/controls-v94.py` (sha256
  `9a0870c2e33b8634dcd9dbd28adbec3fe5178ba76cce9a94a16e9e063b4c6ecf`).
- C2 instruments: `.ufo/evidence/round-94/conjunct-disposition-v94.py` rev 3 (sha256
  `6d4d270644b036cdd7106a5ab24be05b5d05ed01919f7f9ce24090977bdf9b7e`) and
  `.ufo/evidence/round-94/conjunct-disposition.json`.
- Wave: `w1-spec.json`, `w1-dispatch.json`, `r94-w1.ready(.dispatched)`, seat reports under
  `w1/`, and the prefile ledger `claim-falsification.tsv`.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Instruments: counter rev (QUALITY 163-166), driver with sealed env / `O_NOFOLLOW` receipts / canary, C2 checker, spec+pins copies, source snapshots | Round 94 | `7084358c` |
| Freeze: `plans/round-94.plan.md` + `claims.json` | Round 94 | `fdbd18c6` |
| QUALITY 163-166, wave spec/dispatch/ready, first receipts | Round 94 | `33279f40` |
| Battery 45/45 + C2 19/17/2/0 + records (lesson, note block, README row, LOG) | Round 94 | `4dc919ac` |
| C2 checker rev 2 (state/digest reason test) | Round 94 | `67ce02ba` |
| C2 checker rev 3 (round-94 manifest default) | Round 94 | `6a2a1fdd` |
| C2 receipts at rev 3 | Round 94 | `2ad7ebb0` |
| Battery run log (`CONTROL_INSTRUMENT`, `states=45 matched=45`) | Round 94 | `b98b0864` |
| Plan amendment A1 | Round 94 | `67b1ab85` |
| rev-1 witness receipts (prose-word cheat `findings=0`) | Round 94 | `cdf669cf` |
| Landing receipts (`C1_R94_PASS=true`, `DISPOSITION 19/17/2/0`) | Round 94 | `02b43cad` |
| Amendments A2-A6 | Round 94 | `6b19eb92` |
| Amendments A7-A8 | Round 94 | `93164a68` |
| SCORECARD section | Round 94 | `bfd79afd` |
| Lesson Wave + Mistakes M5-M7 | Round 94 | `069a5055` |

## Before → after measurements

**R94-C1 (coverage).** Counting command:

    python3 -I .ufo/evidence/round-94/c1/measure-v94.py --repo <lane> --rev <REV> --work <empty dir>

- before, base `a8f0e14b`: `C1_SETUP spec-absent-at-rev`, `C1_R94_PASS=false`, exit 2
  (`.ufo/evidence/round-94/pre-freeze/controls/nowork-base.out`).
- after, instrument revision `7084358c`: `C1_R94_PASS=true`, exit 0,
  `n=12 killed=5 survived=7 inconclusive=0 unstable=0 invalid=0 trivial=0 witnessed=7/7
  note=present mismatched=0 badrows=0 verdict_tables=1`, `C1_SOURCE S320=row:1,quote:1
  S321=row:1,quote:1 S322=row:1,quote:1` (`.ufo/evidence/round-94/pre-freeze/controls/pos-real.out`).
- after, landing revision `cdf669cf`: same twelve rows and `C1_R94_PASS=true`, exit 0
  (`.ufo/evidence/round-94/landing/c1-at-landing.out`).
- battery: `python3 -I .ufo/evidence/round-94/c1/controls-v94.py --lane <lane> --rev
  7084358c --base a8f0e14b --work <dir> --outdir <dir> --jobs 12` →
  `CONTROL_INSTRUMENT sha256=a22563b0…`, `C1_CONTROLS states=45 matched=45 mismatches=0
  missing=0`, exit 0 (`.ufo/evidence/round-94/pre-freeze/controls-run.log`; receipts
  `.ufo/evidence/round-94/pre-freeze/controls/`, summary `C1-summary.txt`). R94E3 replayed
  the same battery from committed bytes twice into one outdir: `states=45 matched=45` both
  times, stable lines identical (`w1/R94E3.md`).
- canary: `python3 -I .../controls-v94.py --canary-selftest` → `CANARY_SELFTEST: PASS`,
  exit 0 (`.ufo/evidence/round-94/pre-freeze/canary-selftest.out`).

**R94-C2 (calibration).** Counting command:

    python3 -I .ufo/evidence/round-94/conjunct-disposition-v94.py --lane <lane> --rev <REV> --min-falsifiable 17

- before, base `a8f0e14b`: `DISPOSITION_SETUP counter-absent-at-rev`, exit 2
  (`.ufo/evidence/round-94/pre-freeze/c2-nowork-base.out`).
- after, `6a2a1fdd`: `DISPOSITION rows=19 falsifiable=17 unfalsifiable=2 findings=0`, exit 0
  (`.ufo/evidence/round-94/pre-freeze/c2-pos.out`); landing `cdf669cf`: same
  (`.ufo/evidence/round-94/landing/c2-at-landing.out`).
- selftest: `DISPOSITION_SELFTEST: 9/9 pass`, exit 0
  (`.ufo/evidence/round-94/pre-freeze/c2-selftest.out`).
- controls: rev 1 on a 96-character mechanism-only manifest prints
  `rows=19 falsifiable=0 unfalsifiable=19 findings=0` — a false green
  (`c2-cheat-mechanism-word.rev1.out`); rev 3 prints `findings=20` (19
  `reason-names-no-state-or-digest` + the floor) exit 1
  (`c2-cheat-mechanism-word.out`).

## Sources & frontier

`SOURCES: unchanged in count (182 → 182 content rows); three rows re-opened.` Command:

    /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi

→ `tameshi ok …/corpus/SOURCES.md`, exit 0, before and after (W04 duplicate-URL warnings
unchanged). Rows by tier (unchanged): A 150, B 17, C 4, rejected 11. Rows touched old→new:
S320, S321, S322 each gained `corpus/lessons/round-94.md` in `used-by`; no status, tier,
scope, anchor or recheck change. Frontier rows advanced: none — the round sharpens ground
the case note already holds. Assimilation: none — no staged `merge/tameshi/` theme serves a
table-shape reader.

## Trend verdicts

- **expansion: unchanged.** No knowledge entry admitted on uncovered ground; the three
  sources were already held and their re-open adds no row. The new rules are narrower
  statements of ground S321/S322 already carry.
- **quality: improved.** Four new QUALITY criteria (163-167) each ship a failing case
  (`gate-foreign` → `gate-identity-mismatch`; the fenced-denial and denial controls; the
  `delim` finding; the rev-1 mechanism-word cheat; the post-freeze edit). The reader now
  enforces the delimiter and remainder rules it claimed, and the disclosure contract binds
  the C2 checker to the round's own manifest. Battery 45/45 with an independent replay
  (R94E3) and every standing sweep byte-identical (R94E2).
- **discernment: improved.** The round's own wave falsified six sentences of the record
  before filing (A1-A5, A7) and the mutation matrix named twelve rule-level survivors
  (A8); each became a written amendment citing its artifact, and the nine sentinel findings
  are routed rather than reported as passes. No disagreement was left unlearned.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  [lane assertion; `SKILL.md` + `plans/round-94.plan.md`]
- [~] At least one end-to-end domain task executed and logged in LOG.md
  [lane assertion; `LOG.md` Round 94 entry; the wave's twelve seats executed the task]
- [~] Instructions executable by an agent without oral context
  [lane assertion; seats ran the frozen commands from the plan alone]
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  [lane assertion; no sibling file edited; R94CN1 `no-overlap`]

## Stale-lane

Respawn-per-round driver: this round is the lane's only open mission; no other mission of
this lane is open. No tool installs this round (all instruments are in-tree Python).

## Pre-file falsification ledger (Amendment 59)

    python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane tameshi --round 94 --wave r94-w1
    → PREFILE-FALSIFICATION: pass claims=2 rows=14 attack_seats=6 findings=0      (exit 0)

Ledger: `.ufo/waves/round-94/claim-falsification.tsv` (14 rows). Six attack seats are read:
R94R1, R94R2, R94C1, R94M1, R94SN1, R94CN1 — each appears for both claims (6 × 2 = 12
seat rows, plus the R94R1 probe/demo artifacts for the extra C1 findings). Four rows are
`falsifies-wording`, each naming the amendment that narrows the record to what the
instrument enforces (A2, A3, A4, A5 for C1; A1 for C2); the rest are `neutral` with the
reason the artifact does not move the claim's wording.

**Adjudication of the `falsifies-wording` rows.** All five are real and reconciled before
filing: the wave falsified presentation-class sentences and provenance readings of the
*record*, not the claim's numbers. No hostile-state expectation moved, no counter blob
changed after the freeze, and the battery and disposition predicates re-derive at the
landing revision (`.ufo/evidence/round-94/landing/c1-at-landing.out`,
`c2-at-landing.out`). Verdict: the claims verify under the amended wording; the wider
sentences are withdrawn rather than filed.

## Addendum — the three commits landed after this report's first filing

Appended after `fc241b5f`; the sections above are unchanged. These rows complete the
Landed-changes table (the round's last three lane commits) and state the final lane tip.

| Change | LOG entry | Commit |
|---|---|---|
| Erratum + QUALITY 168: round-93 M2's receipt pointer names no committed byte | Round 94 | `70fcf8b0` |
| Note § Part 2 — what the reader certifies and does not, with the three located quotes (R94SC1's block, fixture-verified) | Round 94 | `5abf500c` |
| Wave records: 12/12 seats, seat reports and probes, `r94-w1-results.json`, prefile ledger | Round 94 | `507adb5c` |

**Final lane tip:** `507adb5cc3ed610c209791ad07dbb2ed75961cd9`, pushed and verified with
`git -C …/tameshi-shokunin ls-remote origin refs/heads/master` → the same hash
(`jj-lane.sh state`: `ahead=0 behind=0 tracked=0 untracked=0`). The report's own fleet
commit is `fc241b5f6cf97b21868305e2dc56aabbcbb0e546` plus this addendum's commit.

Scratch: `/fast/scratch/hyaku/tameshi-r94` (3.7 GB, the battery clones and seat probes) is
removed after landing; every receipt a claim rests on is committed in the lane.
