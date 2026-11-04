# tameshi-shokunin — round 74

Lane: `tameshi-shokunin` (verification-fixture craft; axes depth + calibration).
Base `3d6ea1ee8e551e3baf94904384890e3a112088f0` (the admitted round-73
non-author closure). Lane tip at this report: `ef57dc2ae0511ecbc608ec66719421ebe0ad5f4a`
(`= origin/master`, `ahead=0 behind=0`, clean tree). One round, one v1 wave,
12 seats, 0 dead.

## Work performed

Two claims, frozen before any data in `plans/round-74.plan.md` (declaration
`a7cd78ae`), both verify measured; the round also curates one source row and
mines three of its own mistakes.

- **R74-C1 — operability (verdict-only): the three arm gaps round 73 named
  become measured arms.** `tools/wave-reconcile.py` gains arm13
  (delimited-token rule), arm14 (record-span substring rule) and arm15
  (`seat_reports` top-level-only counting) — the three rules round 73 measured
  as carried by NO arm and surviving as mutants (`corpus/lessons/round-73.md`
  §Named coverage gaps; seats T73W1S02/T73W1S10). Evidence: selftest
  `WAVE_RECONCILE_SELFTEST: 15/15 pass` and the committed runner spec
  `tools/wave-reconcile-mutants.spec` scoring `killed=3 survived=0` with each
  mutant dying on its named arm only (`.ufo/evidence/round-74/battery-r74.txt`,
  `final-tip-r74.txt`).
- **R74-C2 — calibration (the lowest scored numeric axis at 8): append-only
  claims are measured over a whole commit range with a declared claim class.**
  `tools/additivity-range.py` + `tools/additivity-range.json` walk a declared
  range per file (`commits` kind, first-parent walk) or one pair (`pair` kind),
  judge each row on `append-only-raw` or `append-only-content`, and carry
  `expect: hold|violated` so a standing red row measures its mismatch.
  Evidence: `ADDRANGE: rows=11 met=11 unexpected=0` and
  `ADDRANGE_TOTALS kind=commits-union keys=8 raw_old_only=5079 norm_cr_old_only=7`
  (`.ufo/evidence/round-74/addr-r74.txt`), selftest
  `ADDITIVITY_RANGE_SELFTEST: 8/8 pass`, and the frozen six-row predicate
  re-run byte-identically at its frozen commit
  (`.ufo/evidence/round-74/frozen-six-row-r74.txt`).
- **Sourced half (inside the claim cap).** S304 (Git `git-diff` page,
  `--ignore-cr-at-eol`, tier A) is opened and S294 (`gitattributes`) re-opened;
  the Gate block with URL, access date, byte counts, sha256, ≤25-word located
  quotes and the admit/reject pair is `corpus/lessons/round-74.md` `## Gate`.
- **Records and defence.** `corpus/QUALITY.md` criterion 124 (range-declared
  append-only claims) lands; four gate-registry rows for the two round-74
  instruments hold `4/4` (`tools/registry.json`), paying round-73 closure
  defect 5 for these instruments.
- **Frontier step.** Census start exit 0, 163 rows
  (`.ufo/waves/round-74/census-start-r74.txt`); end exit 0, 164 rows
  (`.ufo/waves/round-74/census-end-r74.txt`); three mistakes mined in
  `corpus/lessons/round-74.md` `## Mistakes` (unsubstituted-template,
  fixture-prefix-drift, frozen-control-unattainable).
- **Round shape.** One v1 wave, 12 seats, policy
  `scripts/hyaku/ufo-wave-policy.json` (band 8–16): 4 executor · 2 reviewer ·
  1 scribe · 1 scout · 1 critic · 1 mutation-tester · 1 connector · 1 sentinel.
  Attack seats = 2 reviewer + 1 critic + 1 mutation-tester = 4 = 33.3 % (floor
  25 %). Connector seats 1 (≤2). `labrat` is a frozen-topology seat the
  validator rejects, so the planner/probe seats stay with the L1. Wave
  evidence: `.ufo/waves/round-74/w1-spec.json`, `w1-dispatch.json`,
  `w1.ready`, `w1-results.json` (12 records, 0 dead) and 12 seat reports under
  `.ufo/waves/round-74/w1/`. **Round total 12 seats, residual call: none.**
- **Wave findings adopted as work.** T74W1R1: arms 13/14 must assert their
  *named* refusal (landed at `ee395675`). T74W1C1: every frozen `commits` row
  spanned one commit, so the range mode was carried by no row; the manifest
  gained two whole-range walks and the three missing commit-pairs (landed at
  `eb677017`), plus the totals-union and `walked=` fixes. T74W1R2/T74W1S1:
  the lesson's corrections (quote line numbers, arm15 path, frozen-control
  clause). T74W1M1: an independent mutant (`M-C`) survives all fifteen arms —
  named carry. T74W1SN1: `SECRETS=0`, `TMPDIR` honoured, `SCOPE` 0/12.
  T74W1SC1: the registry's `source` anchor is format-only and `scratch_root`
  is unread prose (disclosed).
- **No inherited work.** The lane was clean at base and no earlier attempt of
  this round exists (`.ufo/watchdog.log` has no
  `lane-dead-no-report tameshi round=74` line). Misroot sweep: the fleet root
  holds no file this round's seats wrote — `git -C /home/vgpnk/Projects/shokunin
  status --porcelain` lists `.scratch/*` (orchestrator-owned) and a 24-byte
  `after` file dated 20:05, before this round's launch; nothing we own.
- **Tool installs: none.** Nothing was installed or upgraded this round;
  pacman was not touched.

## Landed changes

Every change ties to a `LOG.md` entry and to the commit that carries it.

| Commit | Change | LOG entry |
|---|---|---|
| `a7cd78ae` | frozen plan, SCORECARD/LOG declaration, pre-data before-state receipts | `## Round 74 — declared (frozen before data)` |
| `2bbf9796` | C1 arms 13/14/15 + `tools/wave-reconcile-mutants.spec` + battery receipt | measured entry (C1) |
| `2e0ac486` | C2 `tools/additivity-range.py` + six-row manifest + sweep/controls receipts | measured entry (C2) |
| `9fe58b40` | S304 row, S294 re-open (`used-by`), lesson with Gate/measures/mistakes, source extracts | measured entry (sourced half) |
| `607b96d8` | QUALITY criterion 124, four registry rows, rekey forecast | measured entry |
| `141dead0` | **superseded** bracket: rekey batch-1 written with the round-73 script copy (traces under the r73 path) | floor-sequence correction |
| `ee395675` | C1 hardening — arm13/14 assert their named refusal; lesson corrections/attacks | measured entry (C1 hardening) |
| `1c3a428e` | SCORECARD claim rows + capability row + carries; LOG measured entry | measured entry |
| `9d9ab7d3` | rekey batch-1 corrected (16 sections, round-74 traces) | floor-sequence correction |
| `47cd112f` | wave settlement evidence (spec/dispatch/ready/results, 12 seat reports) | post-wave append |
| `eb677017` | C2 counter extension (11 rows, two range walks), totals/walked fixes, frozen six-row re-run | post-wave append |
| `906303c7` | rekey batch-2 (2 sections) for the records commits | floor-sequence correction |
| `e84728d6` | post-rekey green receipt | floor-sequence correction |
| `5f2f88aa` | registry needle re-pinned to the extended manifest line | post-wave append |
| `9c27267b` | rekey batch-3 (11 sections) for the registry needle | floor-sequence correction |
| `e3fb9358` | SCORECARD floor-sequence correction | post-wave append |
| `f5e9f9e2` | rekey batch-4 (2 sections) for that correction | floor-sequence correction |
| `2eb49f9a`, `ef57dc2a` | final green receipt; final tip receipts + end census | post-wave append |

## Before → after measurements

| Claim | Counting command | Before | After | Measured commit |
|---|---|---|---|---|
| R74-C1 | `python3 -I -X utf8 tools/wave-reconcile.py --selftest \| tail -1` | `WAVE_RECONCILE_SELFTEST: 12/12 pass`; the three named mutants survive 12/12 (`base-measure-r74.txt`, seat T74W1E1/E3) | `WAVE_RECONCILE_SELFTEST: 15/15 pass`; `MUTATE: DONE (target=wave-reconcile-arms defects=3 killed=3 survived=0 inconclusive=0 kill-rate=100%)`, each on its named arm | `2bbf9796`; hardened and re-run at `ee395675` and the tip |
| R74-C2 | `python3 -I tools/additivity-range.py --repo . --manifest tools/additivity-range.json \| tail -2` | no range mode (`grep -c rev-list tools/additivity-receipt.py` → `0`); the per-pair tool's default judgement exits **0** on the LOG rewrite pair with `raw_old_only=3484 norm_cr_old_only=0` | `ADDRANGE: rows=11 met=11 unexpected=0` + `ADDRANGE_TOTALS kind=commits-union keys=8 raw_old_only=5079 norm_cr_old_only=7`; frozen six-row line re-run at its own commit → `rows=6 met=6 unexpected=0` | `2e0ac486` (frozen predicate), `eb677017` (extension) |

The two round-73 closure defects now stand as measured rows at their own
commits: `LOG.md` at `862e8844` (3484 raw / 0 normalized) and
`corpus/QUALITY.md` at `21a7332f` (1593 / 5) — independently re-derived by
seats T74W1E4 (same numbers with its own code) and T74W1S1 (its own predicate:
3801/3759 and 1925/1920 across the range, 42/0 and 10/5 CR-blind at the same
commits; different predicate, same defect class).

Controls (`controls-r74.txt`): class control (`append-only-content` reads
`hold` for the LOG rewrite and `violated` where content changed: `rows=11 met=7
unexpected=4`); range flip (`r73-log-range-walk` with `expect: hold` →
`unexpected=1` exit 1, worst named `862e8848`); pair-vs-walk (a pair over the
same endpoints names the tip, never the middle commit); do-nothing (the
existing per-pair tool exits 0 with no `ADDRANGE` line); echo stub prints the
summary and the typed totals (disclosed: no printed line is an authenticator;
the defence is per-row re-derivation).

No-harm: depth 10, calibration 8, freshness 9 unchanged as numbers. Monitored
bytes: 16 sections staled by the SOURCES/QUALITY/registry edits, measured RED
at `607b96d8` (`credited=48/64`, `live-red-r74.out`), rekeyed; the records
commits re-staled 2 sections (`credited=62/64` at `1c3a428e`,
`live-red2-r74.out`) and the registry needle re-staled 11; four EOL-preserving
batches (ledger 852 → 883) end green: `credited=64/64` at `ef57dc2a`
(`live-green4-r74.out`, re-measured at the tip).

## Sources & frontier

Census command (both runs):
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`
— start exit **0**, 163 rows (`census-start-r74.txt`); end exit **0**, 164 rows
(`census-end-r74.txt`); warnings only (18 × W04, 1 × W01 S101).

- **Rows before → after:** 163 → 164.
- **Rows added by tier:** 1 × tier A (`S304`, Git `git-diff` docs).
- **Rows touched old → new:** `S294` `used-by` `corpus/lessons/round-63.md` →
  `corpus/lessons/round-63.md, corpus/lessons/round-74.md` (re-open, logged in
  the lesson's Gate).
- **Frontier rows advanced:** none — no `corpus/README.md` `## Frontier` row
  moved this round; the round says so rather than borrowing coverage credit.
- **Assimilation: none** — `shokuknow/merge/tameshi/` was not adopted this
  round; the claim set carried no theme slot.
- **considerthese:** `considerthese/2026-10-28.md` proposals 1, 2, 3 and 5 are
  already implemented instruments (`receipt-exists.py`, `arm-liveness.py`,
  `rekey-cost.py`, `pointer-recheck.py`); proposal 4 (assimilation backlog
  burn-down) remains unimplemented and is carried, not mined this round.

## Trend verdicts

- **expansion — improved.** A capability entered the repertoire through its own
  demonstration (`round-range additivity sweep`, `SCORECARD.md` `## Capabilities`,
  first-working round 74) and the registry grew by one tier-A row with a
  re-opened second (S304, S294).
- **quality — improved.** Three unguarded rules became load-bearing arms proven
  by a committed mutant battery; the instrument gained a range mode that no
  pair recipe reproduces, exercised by two 21/24-commit walks; two wave-caught
  defects (row-sum totals, `walked=`) and one hardening (named refusals) landed
  with the frozen counters unchanged; criterion 124 records the rule.
- **discernment — improved.** Four seat attacks were adopted as work rather
  than argued away (R1's diagnostic specificity, C1's unexercised range mode
  and totals double-count, R2's echo-stub analysis, S1's line-number
  correction), two frozen-text defects and one unattainable control clause are
  reported and not repaired after data, `M-C`'s survival is named as a gap, the
  superseded rekey commit `141dead0` is disclosed, and three of the round's own
  mistakes are mined in the lesson.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — carried `[~]`; this round did not edit `SKILL.md` (blob unchanged since round 73), and the tables/sources it reads are the ones admitted through rounds 1–73; evidence `corpus/knowledge/` + `corpus/SOURCES.md` (164 rows, census exit 0).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `tools/wave-reconcile.py` and `tools/additivity-range.py` ran end-to-end on committed bytes this round, logged in `LOG.md ## Round 74 — measured` and `## Round 74 — appended after the wave settlement`; receipts `.ufo/evidence/round-74/final-tip-r74.txt`.
- [~] Instructions executable by an agent without oral context — input-keyed cold-read monitor reads `credited=64/64` at the tip after four rekey batches (`.ufo/evidence/round-74/live-green4-r74.out`); no independent promotion verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged this round; sibling scan read-only (T74W1CN1), no sibling gate edited or executed; the range-additivity pattern is NOT claimed general (one lane only).

## Fleet notes

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is
  open.
- **L0 questions: none.** No operator decision was needed; nothing was routed
  around.
- **Routed for the next round (status-neutral):** `M-C` (printed integer bound
  to the record instead of the span) survives all fifteen arms; a selective
  `_record_claim` bypass on roles/attack_share alone survives; the six older
  standing instruments still carry no gate-registry row; the round's frozen
  plan text carries two defects (the `MUTANTS:` token the runner never prints;
  control clause (iv) unattainable for `corpus/QUALITY.md`) and one typo
  (`eight-row` for a six-row manifest) — reported, never repaired after data.
