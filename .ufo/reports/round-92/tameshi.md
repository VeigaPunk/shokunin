# tameshi — round 92 report

Lane: `tameshi` (`tameshi-shokunin`, verification-fixture craft: mutation testing of gates).
Round 92, attempt 1, L1 `TameshiR92`. Base `63172b9889475103aeca976d37389d204010dd11`.
Fleet repo `/home/vgpnk/Projects/shokunin`; lane repo `/home/vgpnk/Projects/shokunin/tameshi-shokunin`.

## Work performed

**Declared claim: R92-C1 — coverage — the third attempt at certifying the round-90
fleet-gate mutation case note under a sealed, self-pinned successor counter.** One claim,
one axis (coverage, verdict-only; no numeric score). The round is an **honest stop**: the
frozen predicate is met at the freeze and at the landing revision, and the claim is killed
by its own kill rule (a) branch 2 — an honest note is refused by a rule the claim states —
on the round's own wave artifacts. No capability row enters; no axis score moves.

- **Freeze.** `plans/round-92.plan.md` + `.ufo/waves/round-92/claims.json` at
  `25f976625501663f2ea3336cc3e40499580ea59c` (freeze), instrument revision
  `84904d41a31fb5ddde49e8bf1ad6fc2b489671a0`, driver of record
  `f144da2b4332425909c120c5129d50b1d0ca028e` (A7; the state and D01/D01D02 receipts were
  produced by A6 `f0ece7a3`). Predicate:
  `selfpin ∧ pin ∧ spec ∧ green ∧ canary ∧ invalid0 ∧ trivial0 ∧ inconclusive0 ∧ unstable0
  ∧ note ∧ ids ∧ mismatched0 ∧ figure ∧ witnessed ∧ source ∧ coverage ∧ n_min`, label
  `C1_R92_PASS=true`.
- **Instrument.** `.ufo/evidence/round-92/c1/measure-v92.py`, sha256
  `be5a9221b36983d6c45e983c398ee9c9c088b374d36fb17e2ae67f50ad749ea9`, successor to round
  91's frozen counter (never edited). New over v91: (1) a self-pin, `SELF_SHA256` being the
  sha256 of the file's own bytes with the pin line removed, re-derivable by one command and
  asserted before any read (`C1_SETUP self-pin-mismatch`, exit 2); (2) an id-set refusal —
  any table row whose first cell is id-shaped or that carries a verdict token must be
  exactly one spec id `C01`–`C12` carrying exactly one verdict token in the header-named
  column, refusing duplicates, out-of-set ids, unkeyed verdict rows, a second verdict
  column and a second `verdict` header. Seal unchanged (QUALITY 139).
- **Control battery.** `.ufo/evidence/round-92/c1/controls-v92.py` + 25 committed receipts
  under `.ufo/evidence/round-92/pre-freeze/controls/`; `C1-summary.txt` is derived from the
  receipts on disk and `C1-run.log` is the driver's own witness:
  `CONTROL_INSTRUMENT sha256=be5a9221…`, `C1_CONTROLS states=25 matched=25 mismatches=0`,
  exit 0. States include the hidden `C001`–`C012` table (`ids=false`, `badrows=12`), an
  `X1`–`X12` table, an unkeyed row, a duplicate, a token outside the named column, an
  inverted presented table, a wrong `measured:`, a demoted source row, a removed coverage
  row, an edited spec, no-op/syntax/trivial mutants, a same-witness survivor, a wrong gate
  pin, a post-freeze instrument edit and both `git replace` states; the removal mutants
  D01, D01D02 and D03 each turn a refusal into `C1_R92_PASS=true`.
- **Wave `r92-w1`** (one v1 wave, 11 seats, attack 5/11 = 45 %, all settled, no dead seat,
  no residual call): T92E1 `reproduced-12/12` (the twelve verdicts re-derived outside the
  counter, `.ufo/waves/round-92/w1/T92E1.md`); T92E2 `no-regression` (standing sweeps at
  base and freeze, `T92E2.md`); T92E3 `reproduced` (battery re-run from committed bytes,
  stable lines equal, `T92E3.md`); T92SC1 draft addendum + four measured probes
  (`T92SC1.md`); T92S1 `agree` (S320 re-fetched byte-identically; the Gate's word counts
  corrected from 7/10 to 6/8 on its finding); T92S2 `premise-holds` (row census of the real
  note, `T92S2.md`); T92R1 `findings:2` (SF-1 fenced contradiction, SF-2 `verdict`-cell
  collision, `T92R1.md`); T92R2 `defects:4` (freeze conformance, `T92R2.md`); T92C1
  `killed:A13-id-keyed-2b-reformat` (`T92C1.md`); T92M1 `killed:25/30`
  (`T92M1.md`); T92SN1 `findings:8` (driver safety, `T92SN1.md`).
- **The kill.** T92C1's `A13` is the committed note with its own §2b impact table
  reformatted so each id is a cell of its own (`| C12 | used-by trim | 20 | … |`) — no
  verdict changed, the twelve verdict rows byte-identical to the passing note's. The frozen
  counter refuses it: `ids=false`, `badrows=5`, `mismatched=0`, exit 1
  (`.ufo/waves/round-92/w1/T92C1-A13-id-keyed-2b-reformat.out`). That is kill rule (a)
  branch 2, "an honest note is refused by a rule stated above". T92R1 SF-2 records the same
  class for a data cell exactly equal to `verdict` and for bolded ids; T92R1 SF-1 records the
  opposite textual defect — the kill rule lists "a fenced table" while the declared limits
  say fenced blocks are not keyed, and a fenced inverted table PASSes (T92C1 A1; HTML A2 and
  prose A3 likewise). Amendment A5 in the plan withdraws the claim to honest stop and names
  the enforceable successor properties.
- **r91 routed defects closed.** Defect 1 (stale counts): append-only corrections in
  `LOG.md:4993` and `corpus/lessons/round-91.md:130`, with the frozen
  `plans/round-91.plan.md:201` cell named and not edited. Defect 2 (`claims.json` freeze
  rev): plan and `claims.json` name the same instrument and driver revisions.
- **Sources.** S320 (sha256sum(1), Arch manual pages) admitted this round after being
  fetched (`corpus/SOURCES.md`, mined, used-by the round-92 lesson and the case note);
  `corpus/lessons/round-92.md` `## Gate` carries the URL, the access date and two located
  quotes. Re-opened: none.
- **Assimilation:** none (no staged `merge/tameshi/` theme serves a sealed-counter
  successor). **considerthese:** `2026-11-07.md` idea 1 (inherited-hardening lint) mined and
  landed as `tools/hardening-lint.py`, with `lint-v91.out` (5/8, exit 1) as the failing case
  and `lint-v92.out` (8/8, exit 0) as the positive case.

## Landed changes

Every change is recorded in `LOG.md` `## Round 92` and carried by the commit named here.

| Change | Commit |
|---|---|
| Sealed counter v92, control battery, round-92 spec copy, S320 row, lesson Gate | `884a4dc1` (instrument A) |
| Driver syntax repair (A2) | `3119c0ea` |
| `selfpin` conjunct derived from the check, not a literal; battery runs every state and mutant (A3) | `84904d41` |
| Battery driver repairs A4/A5/A6 (mutant selection, receipt naming, receipt-derived summary) | `7da303df`, `33b90d48`, `f0ece7a3` |
| D03 completes its removal (header rule), self-pin edit control (A7) | `f144da2b` |
| Freeze: plan + `claims.json` + 25 control receipts + summary | `25f97662` |
| Wave spec + dispatch (11 seats) | `dae295de` |
| Records: QUALITY 150-158, `corpus/lessons/round-92.md` (Gate, claim/kill, wave, M1-M8), r91 corrections, S320 used-by, note status block, README map position, SCORECARD, LOG, plan amendments A1-A5, wave artifacts/results, `tools/hardening-lint.py` + receipts | `d92136f8` |
| Landing receipt (`measure-at-d92136f8.txt`, `census-end.txt`) + §8 ledger | `4a7e259b` |

## Before → after measurements

One claim, one counting command pair.

**R92-C1 (coverage).**

    python3 -I .ufo/evidence/round-92/c1/measure-v92.py --repo <lane> --rev <REV> --work <empty dir>

- Before (do-nothing), measured at base `63172b98`:
  `C1_SETUP spec-absent-at-rev`, `C1_R92_PASS=false`, exit 2
  (`.ufo/evidence/round-92/pre-freeze/controls/nowork-base.out`).
- After, measured at the freeze `25f97662`:
  `C1_SUMMARY … n=12 killed=5 survived=7 inconclusive=0 unstable=0 invalid=0 trivial=0
  witnessed=7/7 note=present mismatched=0 badrows=0 headers=1`;
  `C1_CONJUNCTS` all 17 `true`; `C1_R92_PASS=true`, exit 0
  (`.ufo/evidence/round-92/pre-freeze/measure-at-freeze.txt`).
- After, measured at the landing `d92136f8`: identical summary and `C1_R92_PASS=true`,
  exit 0 (`.ufo/evidence/round-92/landing/measure-at-d92136f8.txt`).
- Battery (same round): `C1_CONTROLS states=25 matched=25 mismatches=0`, exit 0
  (`.ufo/evidence/round-92/pre-freeze/controls/C1-summary.txt`, `C1-run.log`).

**Verdict: predicate met; claim not admitted.** The wave's `A13` receipt above shows an
honest note refused by the stated id-set rule; under the frozen kill rule (a) branch 2 the
claim does not verify. The measured table itself is unchanged and independently reproduced
(T92E1). This is the third round in which the certificate, not the measurement, failed.

## Sources & frontier

Census (the frozen command from `CORPUS.md` § *SOURCES.md — where a shokunin learns*):

    /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi

- Round start (base `63172b98`): 179 rows, exit 0 (21 warnings, all pre-existing W04
  duplicate-URL families).
- Round end (`d92136f8`, receipt `.ufo/evidence/round-92/landing/census-end.txt`):
  `tameshi ok …/corpus/SOURCES.md`, exit 0; rows 180 (`grep -c '^ *| S[0-9]' corpus/SOURCES.md`
  → 180 at `d92136f8`; 179 at `63172b98`).
- Rows added by tier: 1 × tier A (S320, `mined`). Rows touched old→new: S320 `used-by`
  `corpus/lessons/round-92.md` → `corpus/lessons/round-92.md,
  corpus/knowledge/mutation-case-fleet-sources-census.md`. No status or recheck change.
- Frontier rows advanced: none — S320 grounds the round's instrument (the self-pin's
  digest semantics), not a `corpus/README.md` frontier row. The case note's map position is
  restated at `corpus/README.md` § *Round 92*: Core / recorded case, **not admitted**.
- Source verified independently: T92S1 re-fetched S320 byte-identically (12 127 B,
  sha256 `b968bc09…277b`) and re-measured both Gate quotes (6 and 8 whitespace tokens).

## Trend verdicts

- **expansion: unchanged** — one mined source row and no admitted knowledge entry; the
  coverage claim that would have certified the case note was killed by its own rule, so it
  carries no expansion credit. Evidence: `git diff 63172b98 d92136f8 -- corpus/SOURCES.md
  corpus/README.md corpus/knowledge/` (one row, one status block, one map section).
- **quality: unchanged** — no held entry was re-verified or superseded; the round repaired
  record defects (r91 routed item 1, the driver's of-record revision, the Gate word counts)
  and added a runnable lint, but the certification instrument it was built around was
  withdrawn. Evidence: `corpus/lessons/round-92.md` `## Claim and kill`,
  `.ufo/evidence/round-92/hardening/lint-v92.out`.
- **discernment: improved** — the round's own wave killed the claim before filing, with
  committed counterexamples (A13, A1) and two reviewer findings that name the textual
  defect; the kills became QUALITY 154-158, each with a state shown able to fail, and the
  plan carries the withdrawal (A5) and the record-mechanics corrections (A1-A4). Evidence:
  `.ufo/waves/round-92/w1/T92C1*.out`, `T92R1.md`, `T92R2.md`,
  `.ufo/waves/round-92/claim-falsification.tsv`.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane assertion; the round's decision surfaces are `corpus/QUALITY.md` 150-158 and `corpus/lessons/round-92.md`, no independent promotion verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 92`; the round's coverage claim is an honest stop, so this is a pointer, not a promotion.
- [~] Instructions executable by an agent without oral context — the frozen plan and the wave dispatch were executed by 11 seats without oral context; no independent promotion verifier (input-keyed monitor unchanged).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round read the fleet gate read-only and wrote nothing outside the lane; no independent promotion verifier.

## Round shape, seats, dead seats, installs, open questions

- Shape: one v1 wave (`r92-w1`), 11 seats — executor 3, scribe 1, scout 2, reviewer 2,
  critic 1, mutation-tester 1, sentinel 1; attack seats 5/11 = 45 %; L1 held the planner
  seat; no residual call. All 11 settled with reports; dead seats: none; round total 11.
- Tool installs: none.
- Open L0 questions: none. `Stale-lane`: respawn-per-round driver; no other mission of this
  lane is open.
- Inherited state: none — the lane was clean at base (`.ufo/waves/round-92/` did not exist;
  `git status --porcelain` empty).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` after the wave
  showed no tameshi-seat file at the fleet root.

## Pre-file falsification ledger

    python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane tameshi --round 92 --wave r92-w1

PREFILE-FALSIFICATION: pass claims=1 rows=12 attack_seats=5 findings=0
exit=0

(The ledger is `.ufo/waves/round-92/claim-falsification.tsv`; the three `falsifies-wording`
rows name T92C1's A13/A1 receipts and T92R1's findings, each narrowed by
`plans/round-92.md` § Amendments A5. Every attack seat — T92R1, T92R2, T92C1, T92M1,
T92SN1 — appears in the artifact column.)

## Lane tip and report commit

- Lane tip: `4a7e259b407d582d2010197f32d7524d6bed5370` (committed via `jj-lane.sh`, verified
  with `git -C /home/vgpnk/Projects/shokunin/tameshi-shokunin ls-remote origin refs/heads/master`).
- Report commit: the `fleet-commit.sh --as tameshi` commit that carries this file (a report
  cannot name its own hash; the lane tip above is the hash that matters for the round).
