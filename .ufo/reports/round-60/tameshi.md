# tameshi — round 60

Lane `tameshi` (`/home/vgpnk/Projects/shokunin/tameshi-shokunin`), round 60,
attempt 1, L1 `TameshiR60`, hyaku run 13 — fresh-start round. Lane base
`9806562c7efc816bd979923e702ef39bc41cade7` (= `origin/master`, clean tree);
final lane commit `9bc9b20b5d6723a19d1b69c8edd7246f82ea3d78` (pushed:
`git ls-remote origin refs/heads/master` prints the same hash; `jj-lane.sh
state` → `local=remote ahead=0 behind=0 tracked=0 untracked=0`).

## Work performed

Declared claims (2, distinct axes, both aimed at the round-59 closure's routed
defects; fresh-start duty discharged by reading the last three rejected
closures — r57 honest-stop, r58 not-admitted, r59 honest-stop — and the
round-59 spot-check before declaring):

1. **C1 — operability, capability re-certification (sourced S290).** The
   round-59 executor-source-pin capability is re-certified on an *installed
   discriminating* counter, and the tool's blob-read plumbing arm is
   reconciled to exit 2. Before-state: the capability was **not admitted**
   (honest stop, closure round 59) — the frozen counter passed a fingerprint
   cheat at 24/24.
2. **C2 — calibration.** The round-59 closure's eight routed defects and its
   five uncaptured mistakes become tree-checkable records (ledger rows,
   QUALITY criteria, SCORECARD annotations, a cold-read precheck at the
   round's content revision, a pointer sweep).

Work items, each with its evidence pointer:

- Installed the discriminating counter `tools/executor-source-pin-measure.py`
  — 8 class cells (`equal`, `unrelated`, `execbit`, `changed`, `missing`,
  `symlink`, `corrupt`, `unresolvable`) over 5 declared paths in ONE tool
  invocation per cell, per-run nonce fixtures, shuffled class order, an
  empty-blob declared path and a corrupt-blob cell expecting exit 2
  (`tools/executor-source-pin-measure.py:1-34`, digest `c136561d…`); closes
  routed defects 1 (cheat-passable counter) and 2 (one-`--path`-per-call blind
  spot).
- Amended `tools/executor-source-pin.py` v2: a blob read that fails at
  plumbing level now returns `EXECUTOR_SOURCE_UNAVAILABLE` (exit 2) instead
  of DRIFT (exit 1) — `tools/executor-source-pin.py:249-266` at
  `da2ae6b3…`; closes routed defect 7 and decides defect 4 (the exec-bit
  boundary is now a tested cell).
- Wrote and froze the pre-data control family (do-nothing tool-absent, the
  unfixed v1 tool as red-before, always-accept, fingerprint, sequence,
  hash-only, first-path-only, empty-blob-unsound):
  `.ufo/evidence/round-60/controls/` — every arm `C1_R60_PASS=false`.
- Froze the claims before any data run: `plans/round-60.plan.md`,
  `.ufo/evidence/round-60/contract.json` (carries the `coldread_forecast`
  key criterion 110 requires) and `.ufo/evidence/round-60/freeze.json`
  (digests) — commit `da2ae6b3`.
- Landed the C2 dispositions: `corpus/routed-defects.json` rows
  `R59.1`–`R59.8`; `corpus/QUALITY.md` criteria 111–117 (one per round-59
  mistake whose `captured-by` was `none`, plus the mined `considerthese`
  proposal 5 and the freeze-digest criterion); `SCORECARD.md` annotations
  (`not admitted (honest stop, closure round 59)` on the round-59 capability
  row; saturation premise restated on the scored axes; the round-60
  measured-claim rows); `corpus/knowledge/executor-source-binding.md`
  amendment (new decision-table row, exec-bit boundary, the standing
  counter); `corpus/README.md` coverage-map addendum and F11 frontier
  correction; `corpus/lessons/round-60.md` (Claims, Gate, 5 mined Mistakes,
  wave record, Verdicts, next-round carry).
- Opened and admitted two source rows this round (S290 Python `secrets`,
  S291 Git `index-format`), rejected the `git-ls-tree` page as the mode
  ground with reason and flip condition, and updated S103's `used-by`
  (old → new logged in the lesson) — `corpus/SOURCES.md:165-166`, `:112`.
- Ran the criterion-116 pointer sweep (21/21 added pointers resolved at the
  final revision) and the criterion-117 freeze classification
  (`INSTRUMENT-OK (receipts re-run)`) — `.ufo/evidence/round-60/pointer-sweep-final.json`,
  `.ufo/evidence/round-60/freeze-verify.json`.

## Landed changes

| Change | Lane commit |
|---|---|
| freeze contract + plan + control family + installed counter + tool v2 + planned-claims block | `da2ae6b361de2d6294c6324a02ae141ff6cb482f` |
| QUALITY criteria 111–116, SOURCES S290/S291 + S103 `used-by`, knowledge-entry amendment, README coverage-map addendum + F11 correction, SCORECARD annotations, lesson, C1 certification receipts (`cert.out`, `cert-repeat.out`), source extracts | `68ac8ac03adb60841457702978b31bbc40871796` |
| pointer sweep (script + receipt), freeze verifier (script + receipt), QUALITY criterion 117, lesson mistake 5, control receipts re-run at the certified revision | `b1ba0ebc434fb0c73fef693e3eda20fd1e17ab02` |
| routed-defect ledger rows `R59.1`–`R59.8`, cold-read precheck receipt at the content revision, wave w1 evidence (spec, dispatch, ready + markers, registry, 2 seat reports, `w1-results.json`), lesson wave record, LOG entry | `e13e0324e048377d7ca5d296294f6f4089240aa0` |
| SCORECARD round-60 measured-claim rows + round-61 plan; pointer-sweep receipt at the final revision | `9bc9b20b5d6723a19d1b69c8edd7246f82ea3d78` |

Every change is tied to a `LOG.md` entry (`## 2026-10-30 — round 60`) and to
the commit above that carries it.

## Before → after measurements

### C1 — operability (capability re-certification)

Counting command:
`python3 -I tools/executor-source-pin-measure.py --lane /home/vgpnk/Projects/shokunin/tameshi-shokunin --rev <rev> --work <empty scratch dir>`

- **Before** (the round-59 verdict at base `9806562c…`): the capability was
  **not admitted** — the round-59 frozen counter passed a fingerprint cheat
  (`passed=24/24 C1_R59_PASS=true`,
  `.ufo/evidence/round-59/controls/cheat-cheat-fp.out`); under the round-60
  counter the unfixed v1 tool scores `passed=7/8 C1_R60_PASS=false`, failing
  exactly one cell — `corrupt`, expected 2 and observed 1
  (`.ufo/evidence/round-60/controls/v1-tool-red.out`) — the red-before for the
  exit-2 reconciliation.
- **After** (at `da2ae6b361de2d6294c6324a02ae141ff6cb482f`, exit 0):
  `C1_R60 rev=da2ae6b3… passed=8/8 C1_R60_PASS=true`
  (`.ufo/evidence/round-60/after/cert.out`); a repeat run at the same
  revision with a different nonce and class order also scores 8/8
  (`.ufo/evidence/round-60/after/cert-repeat.out`).
- **Controls** (all `C1_R60_PASS=false`,
  `.ufo/evidence/round-60/controls/`): do-nothing tool-absent `0/8`
  (`reason=tool-absent`) · unfixed v1 tool `7/8` (corrupt only) ·
  always-accept `3/8` · fingerprint `3/8` · sequence `3/8` (3–5/8 across
  runs) · hash-only `3/8` · first-path-only `6/8` · empty-blob-unsound `4/8`.
- **Freeze integrity**:
  `python3 .ufo/evidence/round-60/freeze-verify.py --lane LANE --freeze
  .ufo/evidence/round-60/freeze.json --work WORKTREE` →
  `FREEZE_VERIFY instrument=10/10 receipt=9/16 verdict=INSTRUMENT-OK
  (receipts re-run)` — every frozen instrument digest still matches; the
  seven drifted digests are nonce-bearing receipts re-run at the certified
  revision (their pre-data bytes remain at
  `git show da2ae6b3…:.ufo/evidence/round-60/controls/ctl-fingerprint.out`).

### C2 — calibration

Counting commands, run against the committed bytes of the final revision
`e13e0324…`:

- `python3 -c "import json;d=json.load(open('corpus/routed-defects.json'));rows=[x for x in d['defects'] if x['id'].startswith('R59.')];print(len(rows), sum(1 for x in rows if x['status']=='fixed'))"`
  → before (base `9806562c…`): `0 0` → after: **`8 7`** (R59.4 `open` with
  its reason: the seat-result completeness check lives in the ufo-fsd-alpha
  wave validator, outside this lane's write scope).
- `grep -c 'corpus/lessons/round-59\.md' corpus/QUALITY.md` → before `0` →
  after **`8`** (criteria 111–117 each cite the lesson).
- `grep -c 'not admitted (honest stop, closure round 59)' SCORECARD.md` →
  before `0` → after **`2`**.
- Cold-read precheck at the round's content revision:
  `bash .ufo/evidence/round-48/quality/coldread-precheck.sh LANE
  9806562c7efc816bd979923e702ef39bc41cade7 b1ba0ebc434fb0c73fef693e3eda20fd1e17ab02`
  → `COLDREAD_PRECHECK floor=9806562c7efc floor_credited=50
  cand=b1ba0ebc434f cand_credited=50 lost=0 ok` (exit 0) —
  `.ufo/evidence/round-60/after/coldread-precheck-final.out`. The candidate
  is the last revision touching monitor-pinned files: `git diff --quiet
  b1ba0ebc… e13e0324… -- SKILL.md PROVINCE.md corpus/QUALITY.md
  corpus/SOURCES.md corpus/README.md corpus/knowledge/ tools/` exits 0.
- Pointer sweep at the final revision:
  `python3 .ufo/evidence/round-60/pointer-sweep.py --lane LANE --rev
  e13e0324… --receipt .ufo/evidence/round-60/pointer-sweep-final.json` →
  `POINTER_SWEEP rev=e13e0324e03 resolved=21/21 unresolved=none` (exit 0).

**Falsification credit is limited.** The wave was dispatched as ONE batched
call of 32 seats; the host usage cap settled it after 2 seats ran
(`w1-results.json`: `seats: 32, settled: 2, dead_or_never_spawned: 30`).
The 30 were cancelled before spawning and are reported as cap-cancelled, not
as failed seats. The two that ran: `T60W1S01` independently reproduced the
red-before on a fixture it built itself (v1 exits 1 `EXECUTOR_SOURCE_DRIFT` on
a plumbing failure, and genuine drift produces the same token — v1 cannot
tell them apart) and `T60W1S02` ran the green probe twice over the amended
tool (both runs `passed=8/8`, nonces `8e61bb8702ebd036` ≠ `4bde7d5306c5f89e`,
different class orders, five-path invocation evidenced by the tool's
`5 declared source blob(s) equal trusted blobs` line). Every planned
reviewer, critic, mutation-tester, connector, scout and sentinel seat was
among the 30 — so the round's claims rest on the L1's own instruments and
their eight-arm control family, with independent confirmation from two seats
only. The closure may read this as under-falsified; the round says so rather
than counting unrun seats as credit.

## Sources & frontier

- **Registry rows: 149 → 151.** Rows added this round: **S290** (Python
  `secrets` documentation, tier A `docs`, opened 2026-10-30) and **S291**
  (Git `index-format` documentation, tier A `docs`, opened 2026-10-30) — 2
  rows added by tier, both tier A. Rows touched old → new: **S103** `used-by`
  `corpus/lessons/round-36.md` → `corpus/lessons/round-36.md,
  corpus/knowledge/executor-source-binding.md`. No row was rewritten; no
  `status` or `recheck` changed.
- **Census** (the frozen command from `CORPUS.md` §SOURCES):
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin tameshi`
  → **before** (round start): exit **0**, 149 rows, 16 W04 duplicate-URL
  warnings + 1 W01 (S101), all pre-existing; **after** (round end): exit
  **0**, **151 rows**, malformed rows 0, warning set unchanged (no new W04 or
  W01 from S290/S291). `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  corpus/SOURCES.md` → 151; `awk -F'|' … NF!=13` → `malformed: 0`.
- **Id collision check** before the append: `grep -c 'S290' corpus/SOURCES.md`
  → 0, `grep -c 'S291' corpus/SOURCES.md` → 0 (registry maximum was S289).
- **Rejected this round** (kept as evidence, with flip condition):
  `https://git-scm.com/docs/git-ls-tree` as the mode ground — the page
  documents `%(objectmode)` but enumerates no octal mode values; flip: a
  page that enumerates them. The row was re-targeted to `index-format`
  (S291), which does.
- **Frontier rows advanced:** F11 (trusted-executor binding) — status
  correction appended to `corpus/README.md`: the counter class is **held**
  (multi-path cell, nonce fixtures, empty-blob cell, corrupt cell, red-before
  on the unfixed tool); what remains outside the lane's claims is
  author-independent trust, which this lane does not claim.
- **Assimilation: none** — no `merge/tameshi/` package entry matches this
  round's claims (counter discrimination, routed-defect dispositions); the
  staged package's counter/mutation entries concern mutation-score semantics,
  not counter discrimination. No shokuknow registry row was appended and no
  campaign file was written.
- **`considerthese/`**: mined — `considerthese/2026-10-28.md` proposal 5
  (stale-closure-pointer sweep) landed as QUALITY criterion 116 plus the
  pointer-sweep receipt; the reflection was opened and grounded in this
  round's own drift evidence.

## Trend verdicts

- **expansion: improved.** New sourced ground admitted on the binding's
  coverage ground: `corpus/knowledge/executor-source-binding.md` gains S290
  (per-run nonce fixtures) and S291 (the index-entry mode field), each a
  `mined` row opened this round; the coverage-map row and the F11 correction
  are in `corpus/README.md`. The capability table gains no admitted row (the
  capability stays "lane demonstrated; admission pending"), so expansion rests
  on the corpus ground only.
- **quality: improved.** The round-59 entry's decision table gains the
  reconciled row (plumbing failure → exit 2) with a red-before witness, and
  the round-59 capability verdict ("not admitted") is now recorded on the row
  that carried it instead of living only in a closure note; the round-59
  lesson's word-count drift is recorded as an erratum. No admitted entry was
  found false.
- **discernment: unchanged.** The round's admits (S290, S291) and its one
  rejection (`git-ls-tree`) are recorded with reasons, quotes and flip
  conditions, but no outside spot-check of this round's gate decisions
  exists yet, and a dispatched seat is still the lane — so no `improved` is
  claimed. The cap-cancelled wave left the round without the independent
  attack seats its own plan called for; that is a limit of this round's
  evidence, not an improvement.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — [lane assertion, no independent promotion verifier](reports/round-1-calibration.md#box-1)
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  [lane assertion, no independent promotion verifier](reports/round-1-calibration.md#box-2)
- [~] Instructions executable by an agent without oral context —
  [lane assertion, input-keyed monitor only; no independent promotion verifier](.ufo/evidence/round-21/coldread/ledger.json)
- [~] No cross-domain bleed (PROVINCE.md still accurate) —
  [lane assertion, no independent promotion verifier](reports/round-1-calibration.md#box-4)

## Round shape, seats and dead seats

- **Shape: one v1 wave** of **32 seats**, dispatched as a single batched
  `taskCall` (policy band 32–48; the operator's final ruling fixed the band
  at exactly 32, which this wave matched — no reshape was needed). Residual
  call: none. Round total: **32 seats**.
- Planned role mix: executor 9 · reviewer 7 · scribe 4 · mutation-tester 3 ·
  scout 3 · critic 2 · connector 2 · sentinel 2 — attack seats (reviewer,
  critic, mutation-tester, sentinel) **14/32 = 43.75 %** (≥25 % required),
  2 connector seats.
- **Settled: 2** (`T60W1S01`, `T60W1S02`). **Never spawned: 30** — the host
  usage cap halted the tranche fill; `w1-results.json` records
  `dead_or_never_spawned: 30`. No seat died with an error; no seat output is
  missing for a seat that ran (criterion 114's check: both settled seats
  wrote a `.md` and a `.json`).

## Stale-lane

Stale-lane: none — this lane's only open mission is the round reported here;
no other lane mission is open.

## Tools installed

None. The round needed only tools already present (`git`, `python3`, `node`,
`curl`); no pacman transaction (pacman is paused host-wide by operator
ruling), no `uv`/`npx` install, no tool version changed.
