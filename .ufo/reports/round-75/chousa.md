# chousa — round 75

## Work performed

Declared **C1 operability** (lowest scored non-retired axis, 3/10) and **C2 calibration**, frozen in
`corpus/evidence/round75/claims.md` at base `8022f72c…` / freeze `43a7a0db…`. **C1**: the lane may bind a
candidate-running loader matrix only after a committed detection-forger battery passes it (QUALITY 126),
and the successor matrix kills the r74 source-blind invocation-order oracle and the diff-only oracle that
the r74 matrix accepted 9/9. **C2**: the r74 spot-check's routed status-neutral defect — the round-74
lesson's located-quote token counts recorded as 18/13 instead of the derived 16/11 — corrected
append-only. Both frozen predicates are met; no target was narrowed after landing.

- Fresh-start reads before declaring: the rejected closures r72/r73/r74 and their non-author spot-checks,
  plus the r75 binding prerequisites (QUALITY 126, the surviving order oracle, real committed
  appends/deletions through `load()`, public-path expected rc/check IDs). R73's completed battery/preflight
  was **not** re-claimed; no Windows-host question is treated as answered.
- Frozen instruments, digest-pinned in the receipts: `corpus/evidence/round75/loader-matrix-v2.py`
  (`95bdd49363e475316c5f5a9e200f039fcc1611f6fbd52848af8e078be0268ee7`), `matrix-battery.py`
  (`c35e937b…`), `ref-counter.py` (`909987ce…`), `c2-count.py` (`bf0250e7…`), five forgers under
  `corpus/evidence/round75/forgers/`, the r74 order oracle byte-unchanged (`180d1a3d…`).
- C1 before (do-nothing state, executed and committed before the freeze): the same battery over the r74
  matrix — `BATTERY=FAIL forgers_rejected=2/5 positive=2/2`, exit 1; the invocation-order oracle, diff-only
  and naive-grep forgers all reach 9/9. `corpus/evidence/round75/controls/before-battery-r74-matrix.txt`.
- C1 after (measured at the landing): `BATTERY=PASS forgers_rejected=5/5 positive=2/2`, exit 0, matrix
  digest equal to the frozen one. `controls/after-battery-at-landing.txt`; further runs
  `controls/{after-battery-v2-matrix,battery-stability-r75,order-oracle-through-v2}.txt`; the frozen r73
  counter still fails 3/12 (`controls/negative-r73-counter-on-v2.txt`); the shuffle shown load-bearing by a
  twelve-entry oracle that reaches 12/12 only on a fixed-order scratch copy and 4/12 on the frozen matrix
  (`controls/shuffle-necessity-r75.txt`).
- C2 before: `DERIVED=S182:16 S183:11 RECORDED=S182:18 S183:13`, `C2=FAIL checks=1/4`, exit 1
  (`controls/before-c2.txt`). C2 after at the landing: `C2=PASS checks=4/4`, exit 0
  (`controls/after-c2.txt`), with the block appended to `corpus/lessons/round-74.md`.
- The successor matrix writes one disposable repository per run with twelve case commits and drives the
  candidate through its public `--lane --base --rev` CLI: unchanged, three appends, three deletions,
  equal-line replacement, receipt change, and three append-only-but-structurally-wrong cases (a second
  anchored heading appended to each protected file). Case order is drawn from `secrets.randbits(64)` per
  run; every case prints `expected_rc=` and `expected_failed=`. A seat independently re-derived all twelve
  expectations from the frozen contract before running
  (`.ufo/waves/round-75/w1/R75ExecB/derived-expectations.md`).
- One v1 wave: **10 settled seats** (`3 executor, 1 scout, 1 scribe, 1 connector, 2 reviewer, 1 critic,
  1 mutation-tester`), 4 attack seats (40%), L1 holding the canonical planner seat, no residual call, no
  dead seat. WAVE-DONE delivered before this report; `.ufo/waves/round-75/w1-results.json`.
- Attack-seat findings integrated as recorded limits, not amended post-scoring: a twelve-entry declared-order
  oracle reaches 12/12 on a fixed-order copy (`R75Mutation` M2); a patch-text-only counter reaches 12/12
  (`R75Review` F4); four content-blind metadata counters reading commit subject, tree ids or byte sizes
  reach 12/12 without opening a blob (`R75Critic` §2–§3), so the claim's "decidable only from
  protected-file content" sentence is false as written; harness-source, memorised-fixture, seed-leak and
  unbounded-child forgers also survive (`R75Scout` F6–F12); the C2 counter is a presence test — an
  insertion above the authored bullets rebinds `RECORDED`, and negating, wrong-magnitude and comment-only
  blocks pass 4/4 (`R75Review2` F1–F5); both positives are lane-authored (`R75Review` F7); `SEED=` is not
  replayable (`R75Review` F8); the controls share the freeze commit rather than strictly preceding it
  (sibling precedent `souji` QUALITY Q120, via `R75Connect`).
- Mined into `corpus/lessons/round-75.md` `## Mistakes`: a control that re-created the defect it isolated
  (the forgers' numstat column), a summary parser narrower than the union of its inputs (the battery's
  `MATRIX=`-only regex, guard shown able to fail by `controls/mutation-battery-parser-slip.txt`), and a
  frozen claim that described its fixture topology from memory (`R75Review` F3). QUALITY 135–137 record
  the matrix/battery, correction-counter and answer-key criteria.

Stale-lane: respawn-per-round; no other mission of this lane is open. Tool installs/updates: none. No
external fetch, source-tree mutation, sibling-repo write or package adoption. Carried operator questions
(external-fetch approval, historical Windows flock/load questions, SHONEN promotion and non-author
entailment review) stay open and are routed around, not presumed answered. No inherited uncommitted lane
work at start. Fleet misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed no
chousa-r75 seat file at the fleet root (the pre-existing `after` file and `.ufo/reports/round-63/tabi.md`
belong to other lanes and were left untouched); lane `git status --porcelain` is empty.

## Landed changes

- Freeze A: `43a7a0db52c8aabdf32735f58e09610e05200e79` — claims, matrix, battery, reference counter, C2
  counter, five forgers, five control receipts, parser-slip guard, stability receipt, census-start,
  SCORECARD planned section; named by the `LOG.md` Round 75 entry.
- Landing (content): `ad57562215a1a729e6ab8c7e13ef713c4e5843d1` — `corpus/SOURCES.md` S184–S186,
  `corpus/lessons/round-75.md`, the `corpus/lessons/round-74.md` correction block, `corpus/QUALITY.md`
  criteria 135–137, `LOG.md`, `SCORECARD.md`, and the wave directory (spec, dispatch, ready/dispatched
  markers, results, ten seat reports, census-end).
- Final tip (receipts): `e515c9624278cef906671d76188cb44e2a3445fe` — the two predicates' after-receipts,
  the guard receipts and `source-counts-after.json`.
- Pre-report remote gate: `git -C /home/vgpnk/Projects/shokunin/chousa-shokunin ls-remote origin
  refs/heads/master` → `e515c9624278cef906671d76188cb44e2a3445fe  refs/heads/master`, exit 0; both commits
  produced helper `landed` lines.

## Before → after measurements

C1 (one command, two matrices; run from the lane root with an existing scratch directory):

```sh
python3 -B corpus/evidence/round75/matrix-battery.py --matrix corpus/evidence/round74/loader-matrix.py --work /fast/scratch/hyaku/chousa-r75/L1/before --runs 2
# BATTERY=FAIL forgers_rejected=2/5 positive=2/2 ; exit 1
python3 -B corpus/evidence/round75/matrix-battery.py --matrix corpus/evidence/round75/loader-matrix-v2.py --work /fast/scratch/hyaku/chousa-r75/L1/landing --runs 2
# BATTERY=PASS forgers_rejected=5/5 positive=2/2 ; exit 0
```

C2 (one command):

```sh
python3 -B corpus/evidence/round75/c2-count.py --lane . --rev e515c9624278cef906671d76188cb44e2a3445fe --base 8022f72c889c904b5657d52c7f29e1643392a216
# DERIVED=S182:16 S183:11 RECORDED=S182:18 S183:13 ; C2=PASS checks=4/4 ; exit 0
```

Measured at: freeze `43a7a0db…` for the before receipts; landing `ad57562215a1…` for the after receipts
(the C2 receipt's own `rev=` line names it; the predicate named `<landing>`, and its bytes are unchanged
at the final tip). No numeric axis score moved (historical operability 3/10, delta 0); no capability row.

## Sources & frontier

Registry rows **183 → 186**, census exit 0 at both ends. Counting command (before:
`git show 43a7a0db…:corpus/SOURCES.md`; after: `cat corpus/SOURCES.md`):

```sh
python3 -c 'import sys,re; print(sum(bool(re.match(r"^ {0,3}\|\s*S\d{3,}\s*\|", x)) for x in sys.stdin))'
```

Added B=2 (S184, S186 mined), C=1 (S185 rejected), A=0. Tier totals A123/B46/C14 → A123/B48/C15;
statuses mined148/queued19/rejected16 → mined150/queued19/rejected17. No existing status/recheck/used-by
cell touched; all first 183 row bytes are identical. The lesson `## Gate` records the pinned revision,
access date 2026-11-04 and located ≤25-word quotes for every new row. Frontier rows advanced: 0 (no
knowledge entry or capability added). `corpus/README.md` unchanged.

Required census command, run at both ends:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa
```

Before (`census-start.txt`, exit 0):

```text
chousa	W04	S051 duplicate url www.w3.org/TR/2017/REC-html52-20171214/syntax.html across scopes
chousa	W04	S053 duplicate url docs.python.org/3/library/socket.html across scopes
chousa	W04	S073 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa	W04	S074 duplicate url docs.python.org/3/library/hashlib.html across scopes
chousa	W04	S075 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa	ok	/home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
EXIT=0
```

After (`census-end.txt`, exit 0): the same five W04 warnings and `chousa ok
…/corpus/SOURCES.md`; `EXIT=0`. No new E or W finding (`R75Scribe` proved the rows add none on a scratch
copy before the append).

Assimilation: none — no package bytes adopted, so the id-collision check is not run.
`considerthese/2026-10-26.md` was opened; no proposal was adopted this round (the two claims are frozen and
the round is at its cap), recorded in the lesson Gate rather than implemented.

## Trend verdicts

- **expansion: unchanged** — no knowledge entry, capability or coverage-map advance; three curated registry
  rows are curation, not expansion.
- **quality: improved** — the candidate-running matrix is now bound to a committed forger battery that
  rejects the surviving order oracle and a diff-only oracle, with real committed appends/deletions through
  the public loader path; the surviving forgery classes the wave found are measured and recorded rather
  than certified away (`corpus/lessons/round-75.md` `## Instrument limits`, QUALITY 135–137).
- **discernment: improved** — the r74 spot-check's routed count defect is corrected append-only and
  re-derived by one command; six attack-seat findings are integrated as limits, and this round's own three
  slips are mined with a committed guard that can fail. The outside non-author admit/reject spot-check is
  requested, not self-granted.

## SHONEN

- [~] Decision tables, error patterns, checklists and cited sources: `SKILL.md` Gates registry; `corpus/QUALITY.md` criteria 135–137; `corpus/evidence/round75/claims.md`; lane assertion, no non-author promotion verifier.
- [~] End-to-end task executed/logged: `LOG.md` Round 75; `controls/before-battery-r74-matrix.txt` → `controls/after-battery-at-landing.txt`; `controls/before-c2.txt` → `controls/after-c2.txt`.
- [~] Executable without oral context: frozen `claims.md` predicates and the two counter commands run from the lane root; limits disclosed in `corpus/lessons/round-75.md`.
- [~] No cross-domain bleed: `PROVINCE.md` unchanged; sibling material read read-only by the connector seat (`R75Connect`), nothing absorbed; lane assertion, no non-author promotion verifier.
