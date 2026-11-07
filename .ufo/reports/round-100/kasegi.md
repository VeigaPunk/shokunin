# kasegi — round 100 (graduation round), attempt 1

Lane: kasegi (`/home/vgpnk/Projects/shokunin/kasegi-shokunin`). Base
`6e63a7dc249ade9a3fc6d219b44049017bdb24a1`; freeze
`f04d63de2ab55e240472c31d551f6a2759a1d7fb`; C2 landing
`ff267d12e7c915986a62253bd40f9289ee6cec5d`; C1 landing
`1605775b0388b309ed05513f6862b669e80e3f30`; final lane tip
`__FINAL_TIP__`.

## Work performed

The round declares **two claims**, both landed before the wave was dispatched:

- **C1 — `depth:verifiability` (the lane's lowest non-retired axis, score 4
  held): the census of record reconciles with itself and the check enforces
  it.** The round-99 record passes its own check while its header
  (host-inclusive 2645/7624, 2683/8026) and its body (resolve.py 2646/7624,
  2684/8026) name different definitions; nothing compared the two. The
  instrument now emits a `confined:` header line and a host-inclusive label
  that names the instrument's definition, and `--check` requires the body's
  resolve.py numerator to equal the header's host-inclusive numerator plus the
  confined count per scope, the class table to sum to the distinct total, and
  INTERNAL − confined to equal the pinned numerator.
- **C2 — `coverage` (score 8 held; capability extension `capture-secret-scan`):
  the session-cookie separator becomes the bounded union, repairing the
  round-99 harm.** Round 99 replaced the round-98 whitespace/quote/operator
  class with S140's assignment-context window and lost 23 detection classes,
  the Netscape cookie jar among them (the round-99 closure: `rejected-harmed`).
  The union of the window and a 1-8 byte whitespace run (S152) recovers the
  three classes a capture actually carries while holding every window form and
  every frozen negative.

Work items, each with its evidence pointer:

- Read the round-99 verifier spot-check and its ten routed defects; closed six
  of them this round (1 the C2 harm, 2 the census reconciliation, 3 the
  correction sweep, 4 the redaction provenance, 7 the round-99 wave-evidence
  bullet, 8 the round-98 bullet-pointer correction), recorded the three that
  would require rewriting a closed record (5, 6, 9), and reported the
  operator-side template defect (10): `corpus/lessons/round-100.md`
  § Routed defects.
- Measured the base state and the do-nothing control before freezing:
  `.ufo/waves/round-100/controls/c1-reconcile-controls-r100.txt` (the
  round-99 instrument prints `CENSUS-CHECK pass` on the round-99 record; the
  round-100 instrument prints `fail reason=no-confined`),
  `controls/c2-check-before-after-r100.txt` (`regression_r98=23
  scanner_only=0 selftest_cases=192` at base; `20/3/195` at the candidate).
- Landed C2: `corpus/instruments/capture-secret-scan.py` (the union; three
  selftest positives, 192 → 195), `corpus/knowledge/gitlab-iam-ci-build-and-session-token-shapes.md`
  (the union and the residual bound), `corpus/SOURCES.md` (S152 admitted,
  S153 rejected), `SCORECARD.md` (capability row extended).
- Landed C1: `corpus/instruments/census-at-rev.py` (the `confined:` line, the
  instrument-definition label, four reconcile limbs, a round-free description
  line), `corpus/instruments/citation-survival.md` regenerated at `ff267d12`
  (SKILL 162/732, corpus 2588/7685, lane 2626/8087, host-owned 77, confined 1).
- Built the round's instruments: the 15-class tamper harness
  `.ufo/waves/round-100/c1/tamper-r100.py` (12 round-99 classes + T13
  `reconcile-confined`, T14 `reconcile-body`, T15 `reconcile-classes`), the C2
  counter `.ufo/waves/round-100/c2/c2-check.py` (stages an instrument at a
  revision, runs the 192-cell matrix, the probe and the selftest, prints one
  line), and the wave generator `make-wave.py`.
- Ran the correction sweep the round-99 spot-check routed: 53 → 57 in
  `SCORECARD.md`, `LOG.md` and `QUALITY.md` R160; the round-99 wave-evidence
  bullet and the round-98 bullet-pointer correction appended to `LOG.md`; the
  landed digests of the four round-99-redacted receipts recorded in
  `.ufo/waves/round-100/l1/r99-landed-digests.txt` (marker counts 8+12+18+19 =
  57, independently confirming the corrected count).
- Dispatched ONE v1 wave of 13 seats (below) and integrated its findings.
- Sources: S152 admitted (curl's cookie jar file format — the seven
  TAB-separated fields), S153 rejected (RFC 6265 states cookie semantics, not
  the on-disk format), S140/S148/S151 re-opened with no cell change.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Freeze: `claims.json`, the 15-class tamper harness, the C2 counter and every executed pre-freeze control | Round 100 bullet 2 (Freeze) | `f04d63de` |
| C2 landing: the bounded union, the knowledge entry, S152/S153, the capability row | Round 100 bullet 3 (C2 landing) | `ff267d12` |
| C1 landing: the reconcile limbs, the regenerated census of record, the instrument pin | Round 100 bullet 4 (C1 landing) | `1605775b` |
| Corrections to earlier entries (53 → 57, the round-99 wave bullet, the round-98 pointer, the landed digests) | Round 100 bullet 5 (Corrections) | `__CORR_COMMIT__` |
| Integration: QUALITY R162–R164, the lesson with the Gate and six mistakes | Round 100 bullet 7 (Integration) | `__INTEG_COMMIT__` |
| Wave evidence: spec, dispatch, ready/ready.dispatched, results, 13 seat reports and receipts | Round 100 bullet 8 (Wave evidence) | `__WAVE_COMMIT__` |

## Before → after measurements

### C1 — `depth:verifiability`

Counting command (frozen in `claims.json`):

```
python3 -B .ufo/waves/round-100/c1/tamper-r100.py --lane . \
  --rev 1605775b0388b309ed05513f6862b669e80e3f30 \
  --alt-rev a3db47e71fe292c03b00ba11f38cccbec45d3966 \
  --instrument corpus/instruments/census-at-rev.py --work <scratch>
```

- **Before** (`6e63a7dc`): the round-99 instrument passes the round-99 record
  (`CENSUS-CHECK pass`, rc 0) although the record's header and body disagree;
  the round-99 check has no limb that parses `confined:`, the body numerator or
  the class table. Tamper classes: 12, none of them a reconciliation class.
- **After** (`1605775b`): the round-100 instrument rejects the round-99 record
  (`CENSUS-CHECK fail reason=no-confined rc=1`) and passes the round-100 record
  (`CENSUS-CHECK pass rev=ff267d12 … confined=1`); the 15-class harness prints
  `TAMPER-RESULT killed=15 total=15 evaluated=15` with T13
  `reconcile-confined`, T14 `reconcile-body` and T15 `reconcile-classes`.
- Measured against `1605775b`; receipts
  `.ufo/waves/round-100/controls/c1-reconcile-controls-r100.txt`,
  `c1-write-candidate-r100.txt`, `c1-landing-r100.txt`,
  `c1-tamper-candidate-r100.txt`.

### C2 — `coverage` (capability `capture-secret-scan`)

Counting command (frozen in `claims.json`):

```
python3 -B .ufo/waves/round-100/c2/c2-check.py --lane . \
  --rev ff267d12e7c915986a62253bd40f9289ee6cec5d --work <scratch>
```

- **Before** (`6e63a7dc`): `regression_r98=23 scanner_only=0 mustfix=7 rune=4
  agree_hit=121 probe_mustfix=12/12 probe_negatives_extra=0
  selftest_cases=192`; end-to-end on a TAB jar and a space jar
  `hits=0 files=0`.
- **After** (`ff267d12`): `regression_r98=20 scanner_only=3 mustfix=7 rune=4
  agree_hit=121 probe_mustfix=12/12 probe_negatives_extra=0
  selftest_cases=195`; end-to-end `hits=2 files=2` (both jars).
- The three recovered classes are exactly `ctx-cookie-jar-tab`,
  `ctx-cookie-jar-space` and `geo-space`; the twenty remaining classes are the
  S140-faithful refusals (a newline between keyword and operator, gaps of 9-12
  bytes), stated in the capability row and the entry's Limits.
- Measured against `ff267d12`; receipts
  `.ufo/waves/round-100/controls/c2-check-before-after-r100.txt`,
  `c2-matrix-candidate-r100.txt`, `c2-probe-candidate-r100.txt`,
  `c2-selftest-candidate-r100.txt`, `c2-e2e-jar-r100.txt`.

### Guard — `depth:density`

`python3 corpus/instruments/density.py SKILL.md --label r100` prints **273.2**
(before and after); `git diff --stat 6e63a7dc 1605775b -- SKILL.md` is empty.

## Sources & frontier

- **Census before** (round start, `6e63a7dc`):
  `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`
  → `kasegi ok …/corpus/SOURCES.md`, exit 0, 152 rows, the seven inherited W04
  warnings (S028, S029, S072, S076, S080, S085, S143).
- **Census after** (round end): the same command → `kasegi ok`, exit 0, 153
  rows, the same seven W04 warnings.
- **Rows added by tier:** S152 (`docs`, tier B, `mined` — curl's cookie jar
  file format, the seven TAB-separated fields, the fact the round-99 harm
  turned on); S153 (`spec`, tier A, `rejected` — RFC 6265 states cookie
  semantics and names the Netscape specification but no on-disk format; flip:
  admit if a round needs cookie semantics rather than the file format).
- **Rows touched old→new:** S140 `mined` → `mined` (re-opened from its
  committed capture; the live `/-/raw/` answered HTTP 403 again), S148 `mined`
  → `mined` (re-opened), S151 `mined` → `mined` (re-opened). No status,
  recheck or used-by change; S152's used-by lists the instrument and the
  knowledge entry.
- **Frontier rows advanced:** none new — the round's frontier work is the
  knowledge entry's separator model (the union and its stated residual), which
  deepens the credential-shape frontier rather than adding a row.
- **Assimilation:** none adopted — the staged ids collide with the lane
  registry on 94/94 rows (`.ufo/waves/round-100/assimilation/collision-receipt-r100.txt`);
  package adoption waits for a later round.
- **Mistake mined:** `corpus/lessons/round-100.md` § Mistakes, M100-1…M100-6
  (six classes, each with the criterion that should have caught it and the
  fix; the sweep found them rather than none).

## Trend verdicts

- **expansion: improved** — one admitted entry on ground the coverage map did
  not hold (the cookie-jar separator model, S152), the registry 151 → 153 with
  one admit and one reject, and the capability row extended; the entry states
  the union and its residual rather than a wider claim.
- **quality: improved** — the round-99 harm is repaired on the axis it harmed
  (`regression_r98` 23 → 20, the jar recovered end-to-end, every window form
  and frozen negative held), the census of record now reconciles with itself
  and the check enforces it (15/15 tamper classes, three of them new), and the
  round-99 spot-check's textual defects are corrected in the living files.
- **discernment: improved** — the non-author spot-check of round 99 rejected
  the round for harm and named the measured union; this round took the union
  it named rather than re-arguing the choice, mined six mistakes into
  `QUALITY.md` criteria (R162–R164), and the Gate records one admit and one
  reject with located quotes.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `corpus/lessons/round-47-verifier-spotcheck.md:94`; SKILL.md untouched this round (`git diff --stat 6e63a7dc 1605775b -- SKILL.md` empty).
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — evidence: `corpus/practice/curl-h1-1913733/report.md` and `corpus/practice/curl-ibb-h1-1997312/report.md`, logged in LOG.md rounds 85-86; this round's end-to-end run is the jar scan (`controls/c2-e2e-jar-r100.txt`: `hits=0` → `hits=2 files=2`).
- `[~]` Instructions executable by an agent without oral context — evidence: `corpus/lessons/round-47-verifier-spotcheck.md` (declared-root recheck); the round's counters are self-contained (`c2-check.py`, `tamper-r100.py`).
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md`; live-target testing remains refused; S152/S153 are both credential-shape sources inside the province.

## Round shape

ONE v1 wave, 13 seats, `counts.spawn=13`, `resume=0`, policy band 8–16
(`scripts/hyaku/ufo-wave-policy.json`), attack seats 8/13 = 62 % (3 critic, 2
reviewer, 2 mutation-tester, 1 sentinel), plus 2 executor, 1 scout, 1
connector, 1 scribe. No planner seat: the L1 holds the canonical planner seat
per the fleet-wide 2026-10-19 ruling. Round total: 13 seats.

## Wave findings

Wave w1: 13 seats, one v1 wave, 11/13 settled at the time of writing (the two
remaining seats' findings are appended below when they settle). No seat
re-scores a claim; the findings that changed the round are marked.

- **C1 — P1–P3 stand; P4 was false as written and is fixed.** CriticClaimsC1
  reproduced P1 (`no-confined` vs the round-99 instrument's pass), P2 (a clean
  work dir passes and a fresh write reproduces the record), P3 (15/15 with
  T13–T15 attributed) and found P4's parenthetical false: `measured-at` was
  `ff267d12`, the C2 landing itself, not a strict descendant. Fixed by
  regenerating the record at `1605775` (a strict descendant) with the identical
  triple (`controls/c1-landing-fix-r100.txt`), not by amending the predicate.
  ExecC1Indep AGREED on P1–P4 and rejected an independent class-table-sum
  forgery; ReviewC1Record APPROVED the record and the limbs (re-derived
  `2627-1=2626`, `165+0 / 2665+1 / 2703+1`, `77+0+5383+2627=8087`) with F1:
  only T13 requires a new limb (T14/T15 are also caught by the pre-existing
  body-mismatch) and F3: the freeze's instrument pin named no committed blob
  (the landing commit carries the pin that matches).
- **C1 — the 15/15 harness is not limb-coverage evidence.** MutC1Reconcile
  killed 10 of 12 single-point *check* mutants only by the harness (i.e. 10
  survive it), showed T14/T15 do not isolate `reconcile-body` /
  `reconcile-classes`, and named four real defects (m08b/m10/m11/m12)
  invisible to it; the limbs themselves are load-bearing (m13/m14/m15 probes).
  Routed to round 101 (a limb-coverage harness, not a format harness).
- **C1 — the check reuses a verifier-controlled extract.** CriticClaimsC1's
  attack (a): a poisoned extract cache makes the check accept an unreconciled
  record; the smallest safe correction is a fresh extract (or a tree hash) in
  `--check`. Routed to round 101.
- **C2 — P1–P5 pass; the residual statement was wrong twice and is corrected.**
  CriticClaimsC2 passed P1–P4 and P5 literally, then showed the residual is
  broader: 4,378 variants tested, 439 hidden (r98 hit, landing miss) in four
  classes outside the 192-cell matrix (quote-only, semicolon-only, mixed
  quote/space/semicolon, >8-byte whitespace with no operator), and
  `scanner_only=3` is exactly the three recovered classes. ExecC2Matrix
  reproduced the claim independently over 224 cells (three instrument blobs
  sha-verified; zero cells the round-99 instrument hit are lost; the recovered
  set is exactly the jar and `_geo_` whitespace classes). SentinelCookie
  reproduced P1–P5 and measured two MUST-FIX classes (operand characters —
  six realistic export forms pass unseen; and the 9-10-byte gap family, since
  the pinned `assignmentOperand` bound is 10, not 8), four over-detection
  forms, and the oracle defect below. ReviewC2Scanner REQUEST-CHANGES on
  documentation only (F1 the round-98 class refused all twelve, not eight; F2
  the Limits still described the round-99 window; F3 the pinned operand class
  is not the round-100 target; F4 the residual omits newline-after-operator
  cells; F5 the residual is not "S140-faithful"). All five are fixed in the
  entry; F1–F5 changed no measured number.
- **C2 — the counter's S140 oracle is the superseded MR form.** SentinelCookie
  measured that `matrix.py`'s S140 translation is the MR !151 window, not the
  pinned `assignmentOperand` (S151): at the pinned commit 58/192 cells change
  verdict, the TAB jar is S140-detectable, and some "S140-faithful" residual
  cells are S140 detections. The frozen predicates are comparisons against one
  oracle on both sides and stand; the wording is corrected in the capability
  row and the entry's Limits, and the pinned operand class's other delimiters
  and its 10-byte bound are routed to round 101.
- **C2 — two mutation survivors.** MutC2Union killed 13/15 single-point
  mutants; m03 (`{1,8} -> {1,12}`) and m04 (newline allowed in the whitespace
  run) are byte- and behaviour-different yet identical to the landing on every
  frozen field and all 192 cells: the whitespace run's upper bound and its
  newline exclusion are unpinned by both detectors. Routed to round 101 (a
  boundary-negative pair). The union is load-bearing: m01 reverts exactly the
  three recovered cells and m02 collapses `agree_hit` to 0.
- **Harm — NO HARM on five checks.** CriticHarm: the five governance files are
  byte-identical base → C2 → C1; 38/39 compiled patterns are identical and the
  one change is a strict superset with 0 selftest cases removed (192 → 195);
  the round-99 instrument on the round-100 record reports a one-way
  header-schema break with no live consumer (expected, and the round-99
  instrument still writes and checks a round-99-format record at the new
  revision with the identical triple); no knowledge entry's instrument citation
  is out of range; the pinned numerator is INTERNAL only and no knowledge file
  was edited to move it.
- **Gate and corrections — ScribeGate.** PASS on the four 53 → 57 corrections
  and the mistake count (byte-exact, no stale `53` left); FAIL on the Gate
  block as written (six defects: two word counts, a missing access date, a
  false "committed capture" for S148, S151 quotes from the comment line, no
  registry delta) — the audited block is spliced in and the measured registry
  delta is 151 → 153; PASS on the S152 row schema (11 cells, `kasegi ok` rc 0);
  PASS with two low defects on the entry's S152 citations (anchor paraphrase,
  `verified-at` missing S152) — both fixed.


## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Tool installs

None this round (no install or upgrade was needed; pacman stays paused).

## Open L0 questions

None new. Carried: `kasegi | round-15` (PROVINCE re-point after the source-tree
loss) remains open and is routed around, not answered.
