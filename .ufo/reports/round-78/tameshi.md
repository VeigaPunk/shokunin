# tameshi — round 78 (hyaku run 15, attempt 1)

Lane: `tameshi-shokunin` (verification-fixture craft; axes depth + calibration).
Base `5bcb13ea7cc08bb0b594fcd0c2bb770cb8fe64a0` (= `origin/master`, the round-77
non-author closure verdict commit). Lane tip at report time:
`00ddee5fe6b4a47595c5ff1869ffd42f4408825e` (`ls-remote origin refs/heads/master`
prints it; `jj-lane.sh state` reads `ahead=0 behind=0`, tree clean). Report
commit: the fleet commit that carries this file.

Round shape: **one v1 wave, 12 seats** under
`scripts/hyaku/ufo-wave-policy.json` (band 8–16) — 3 executor, 1 scribe, 1
scout, 2 reviewer, 1 critic, 1 mutation-tester, 1 connector, 1 sentinel, 1
simplifier; attack seats 4/12 = 33.3 %. Round total 12 seats; **dead seats: 0**
(`w1-results.json`: 12 seats, 12 results, every seat wrote its report); no
residual call. Frozen plan `plans/round-78.plan.md` at declaration `c1c220d4`.

## Work performed

Two claims on distinct axes, both landed and both measured; C1 is the
**capability acquisition** the stagnation nudge directs (rounds 75, 76 and 77
entered no capability row, window N = 2, all scored axes 10/8/9 ≥ the line 8).
The nudge waives the lowest-axis obligation this round; C2 works coverage anyway
because two axes were wanted (the plan's "not waived" wording is corrected
append-only in `SCORECARD.md`).

- **R78-C1 — operability, capability acquisition (sourced on S306, opened this
  round).** `tools/selfstate-freshness.py` executed every instrument under a
  hardcoded `python3 -I -X utf8` prefix, so the lane's bash mutation runner
  could never be a live row (round-77 carry; criterion 127). Landed: a frozen
  interpreter tuple table (`python` default unchanged, `bash` added; an unknown
  or non-string name is a setup refusal before any row effect) and the live row
  `mutation-runner-selftest` binding `MUTATE_SELFTEST: 107/107 pass` to
  `tools/mutate-and-run.sh --selftest` at the base revision. The capability row
  `non-Python instrument freshness row` enters `SCORECARD.md`'s `## Capabilities`
  table in this round.
  Evidence: `.ufo/evidence/round-78/c1-landed-sweep.txt` (`rows=21`, bash row
  `measured=match`), `c1-landed-selftest.txt` (`13/13`),
  `c1-control-bash-row-on-base-runner.txt` (base runner + new row = setup
  refusal), `c1-base-sweep.txt` (base `rows=20`), `c1-cache-kill.txt` (cache-key
  mutant `12/13`), `design/SHA256SUMS`.
- **R78-C2 — coverage (sourced on S091, re-opened this round).** The two
  survivors the round-77 wave named become fixture coverage:
  `tools/wave-reconcile.py` arm20's leftover post-condition (per-fixture, not a
  shared-dir scan) and arm21's TWO-commit fixture (rev1 carries the record and
  `wave/one.md`, rev2 = HEAD adds `wave/two.md`; the row is measured at rev1, so
  a HEAD-resolving listing drifts). `SELFTEST_ARMS` 20 → 21;
  `tools/wave-reconcile-mutants.spec` 8 → 10 defects.
  Evidence: `.ufo/evidence/round-78/c2-landed-selftest.txt` (`21/21`),
  `c2-landed-battery.txt` (`defects=10 killed=10 survived=0`, `CONTROL: GREEN`,
  `MUTATE_RESTORE: OK`), `battery/` per-defect streams,
  `c2-base-control-battery.txt` (base bytes: `survived=2`),
  `c2-base-selftest.txt` (`20/20`), `c2-concurrency-prepost.txt` (the flake and
  its fix).
- **Registry curation (§2b).** S306 appended (GNU Bash manual, *Invoking Bash*,
  tier A) and S091 re-opened for the revision-name ground (`used-by` old → new
  only; rule 2 forbids in-place anchor/teaches rewrites; the HEAD ground is
  recorded in the round-log append block and the lesson Gate).
  `corpus/QUALITY.md` gains criterion 129 (a registry row lands with its round's
  log entry) from a mined mistake; `corpus/lessons/round-78.md` carries the Gate
  block, four mistakes and the wave findings.
- **Wave attacks that changed the artifacts** (all disclosed, none argued away):
  the reviewer reproduced an interpreter-cache bypass in the declared C1 design
  (`T78W1R1`; independently `T78W1C1`, `T78W1E2`, `T78W1CN1`) — a `bash` row's
  stdout could satisfy a python-defaulted row on the same path/rev/argv; the L1
  fixed the cache key, first as a 14th arm, the reviewer voted FAIL because the
  frozen kill rule (iii) names `13/13`, so the assertion was folded into arm13
  (`ARM13_bash_interpreter_row_and_cache`, same coverage, count unchanged) and
  the reviewer re-measured the final bytes and voted PASS. The simplifier found
  the leak post-condition was not concurrency-safe (shared temp-dir scan): four
  concurrent `--selftest` runs on the pre-fix bytes fail 4/4 with a spurious
  `leak:2`/`leak:3`; the per-fixture `if os.path.exists(fix)` check passes 4/4
  with the battery matrix byte-for-byte unchanged. The critic found the plan
  cited a control receipt its declaration commit did not carry, and the L1's own
  first settlement ran a copied run-book tool whose hardcoded round-63 trace
  path produced `51/65` until batch 2 rebuilt it.
- **No-harm.** Arms 1–19 byte-identical between base and landed selftests; arm20
  `meet` on both; the base 20 selfstate rows identical (landed sweep minus the
  new row); the bash instrument unchanged (`MUTATE_SELFTEST: 107/107 pass` at its
  pinned rev). Standing sweeps at the final tip:
  `WAVE_RECONCILE: rows=6 met=6 unexpected=0` and
  `SELFSTATE: rows=21 match=19 stale=2 unexpected=0`
  (`standing-sweep-wr-r78.txt`, `standing-sweep-ss-r78.txt`, both headed with
  the measured rev and tool sha as round 77's routed defect 4 asked).

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Frozen plan + declaration receipts (base/landed receipts, controls, source snapshots, candidate bytes) | Round 78, base + declaration | `c1c220d475a04aa0e9c28be4f632c03e20d30116` |
| `tools/selfstate-freshness.py` + `.json` (interpreter tuple table, bash row), `tools/wave-reconcile.py` (arm20 post-condition, arm21 two-commit fixture), `tools/wave-reconcile-mutants.spec` (8 → 10 defects); `corpus/SOURCES.md` (S306, S091 re-open, round-77 correction, round-78 entry), `corpus/QUALITY.md` (criterion 129), `corpus/lessons/round-78.md`, `SCORECARD.md` (capability row + round-78 block), `LOG.md` | Round 78 entry | `6f5327526738a38f921ec243bcbace2dc3b398dd` |
| Wave artifacts (spec, dispatch, ready, results, 12 seat reports), cache-key fix folded into arm13, per-fixture leak post-condition, manifest note count removed, disclosures, lesson wave section, `SCORECARD.md` appended block | Round 78, wave close | `091d50e47bfea5a38d97671934ae0127ef760edc` |
| Cold-read settlement batch 1 (superseded: the copied tool's hardcoded round-63 trace path; see below) | Round 78, settlement | `4a8d10787ae79bfac509ce159f97b20ef227053d` |
| Cold-read settlement batch 2 (final): 14 sections re-keyed from the content tip with round-78 trace paths, ledger 948 → 962; the 14 tracked round-63 trace files batch 1 overwrote are restored from the branch | Round 78, settlement | `c4281f3961833bdc94e640bbb420ba00a690865d` |
| Settlement receipt at `c4281f39`; end census; monitor receipt at `0e088684` | Round 78, evidence | `a38944b2`, `ef1587bd`, `00ddee5f` (see `git log`) |
| Lesson mistake 4 (the copied-runbook trace path) | Round 78, wave close | `0e0886841958445c3060ca25c990d10da59abaa3` |

## Before → after measurements

Measured commits: before at the base `5bcb13ea`; after at the landing commit
`6f532752` for the tool state (later arm13/leak fixes at `091d50e4`, receipts
re-measured there) and at the settlement commit `c4281f39` for the record state.
Every receipt names the revision and tool sha it measured (round 77 routed
defect 2).

- **R78-C1.** Counting commands:
  `python3 -I -X utf8 tools/selfstate-freshness.py --repo . --doc-rev 5bcb13ea7cc08bb0b594fcd0c2bb770cb8fe64a0`
  and `python3 -I -X utf8 tools/selfstate-freshness.py --selftest`.
  Before (`5bcb13ea`, base manifest): `SELFSTATE: rows=20 match=18 stale=2
  unexpected=0` exit 0; the do-nothing control (base runner + the new row)
  prints `SELFSTATE error=setup figure-absent:mutation-runner-selftest` exit 2.
  After: `SELFSTATE: rows=21 match=19 stale=2 unexpected=0` exit 0 with
  `SELFSTATE_ROW mutation-runner-selftest capability=mutation sweep runner
  expect=match measured=match ok` and `SELFSTATE_SELFTEST: 13/13 pass` exit 0.
  Natural scalar: registered counter-defects surviving the interpreter/cache
  surface 1 → 0 (the cache mutant survives the declared design `13/13`, dies
  `12/13` after the fold).
- **R78-C2.** Counting commands:
  `python3 -I -X utf8 tools/wave-reconcile.py --selftest` and
  `bash tools/mutate-and-run.sh --target tools/wave-reconcile.py --defects
  tools/wave-reconcile-mutants.spec --suite 'python3 -I -X utf8 "$MUTANT"
  --selftest' --workdir <scratch> --label wave-reconcile-arms-r78`.
  Before (`5bcb13ea`): `WAVE_RECONCILE_SELFTEST: 20/20 pass`; the 10-defect spec
  on base bytes reads `MUTATE: DONE (target=wave-reconcile-base-control-r78
  defects=10 killed=8 survived=2 inconclusive=0 kill-rate=80%)`, survivors
  exactly `git-listing-uses-head` and `arm20-cleanup-removed`. After:
  `WAVE_RECONCILE_SELFTEST: 21/21 pass` exit 0; `MUTATE: DONE
  (target=wave-reconcile-arms-r78 defects=10 killed=10 survived=0
  inconclusive=0 kill-rate=100%)` with `CONTROL: GREEN` and byte-identical
  restore (`sha256 f8071c8ad8dc…`). Kill matrix as frozen; the eight base
  defects keep their arms, `git-listing-recursion-removed` now also fails arm21
  (disclosed intrinsic collateral), `git-listing-uses-head` → arm21 only,
  `arm20-cleanup-removed` → arm20 only. Natural scalar: surviving registered
  defects 2 → 0.
- **Monitor (settlement).** `python3 -I tools/coldread-precheck-portable.py
  --repo . --rev c4281f3961833bdc94e640bbb420ba00a690865d --work <scratch>`
  → `COLDREAD_PORTABLE rev=c4281f396183 credited=65/65 elapsed=3.9s
  probe_sampled=20 probe_mismatches=0`, `sections_covered=65
  sections_total=65 box3_full_page=true`
  (`.ufo/evidence/round-78/coldread-after-r78.json`). At the final tip
  `00ddee5f` the same command prints `credited=65/65` (measured by the L1; the
  commits after `c4281f39` add only evidence files, which change no pinned
  input — criterion 128), and the tip commit itself carries the receipt for
  `0e088684` (`coldread-at-lesson-commit.json`).

## Sources & frontier

Census command, both runs exit 0:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi
```

- Before: exit 0, **165 rows** (`.ufo/evidence/round-78/census-before.txt`, taken
  at round start before any registry edit).
- After: exit 0, **166 rows** (`.ufo/evidence/round-78/census-end.txt`), standing
  W04 warning set, no E-findings.
- Rows added by tier: **A +1** (S306, GNU Bash manual *Invoking Bash*,
  https://www.gnu.org/software/bash/manual/html_node/Invoking-Bash.html,
  fetched 2026-11-04 05:50:32 GMT, 12,377 B,
  sha256 `ea86a64cd2d2cbc338fa911c73bcf81aac23da1910d54ba8ab76c20f5d0497c4`,
  quote page line 249, 10 words); B 0; C 0.
- Rows touched old → new: **S091** — `used-by`
  `corpus/knowledge/oracle-anchored-survivors.md` → the same plus
  `corpus/lessons/round-78.md`; anchor/teaches/opened/status unchanged; the HEAD
  ground is recorded in the round-log append block and the lesson Gate (quote
  page line 2225, 13 words; `HEAD` label page line 2223), snapshot
  `sources/s091-gitrevisions.html` (74,654 B). One rejected candidate recorded:
  the kernel.org mirror of the same manual (same document, same quote). Quote
  proofs: `sources/quote-proofs.txt` (`grep -Fc` = 1 per quote at the named
  line).
- Round-77 correction: S305's per-round log entry was missing; the append-only
  correction is written this round (lesson mistake 1, criterion 129).
- Frontier rows advanced: **none** — `corpus/README.md` §Frontier F1–F10 is
  byte-identical; this round's ground is the lane's instruments, and its named
  survivors are listed below.
- **Assimilation: none.** The connector's searches of
  `/home/vgpnk/Projects/shokuknow/merge/tameshi/` (A, B, B_precise, B_lifecycle)
  found no entry on the frozen-interpreter freshness capability or the
  leak/pinned-rev fixture ground; nearest in-province entries are named in
  `.ufo/waves/round-78/w1/T78W1CN1.md`. Its id check reads registry=166,
  staged=103, **8 collisions** — a future adoption needs renumbering by
  document; nothing was appended.

## Trend verdicts

- **expansion — improved.** A capability is admitted to `SCORECARD.md`
  (`non-Python instrument freshness row`, first-working round 78, evidence the
  live sweep + `13/13` selftest), which is expansion's own observable ("a
  capability admitted to `SCORECARD.md`"); the registry gains one tier-A row on
  a page the lane did not hold (S306) and re-opens one (S091). No admitted entry
  fails its bar.
- **quality — improved.** Both named round-77 survivors become measured coverage
  (10/10 kills, control GREEN, byte-identical restore, frozen matrix); two real
  defects found by the wave (the cache-key bypass, the non-concurrency-safe leak
  post-condition) are closed and their regression arms discriminate (`12/13`,
  `4/4` concurrent passes vs `4/4` pre-fix failures); every C1/C2 receipt names
  the revision and tool sha it measured (round 77 routed defects 2 and 4 paid);
  the standing sweeps, the census and the cold-read monitor are green at the
  final tip.
- **discernment — improved.** Round 77's non-author spot-check agreed with the
  gate on both admits and rejects, and this round pays its routed defects
  (receipt headers, tip measurement, exact pointers, Godspeed literal — the
  dispatch carries 12 `/skill:godspeed` heads); four wave findings are adopted
  as disclosures, and mined mistakes add grounded criterion 129. Self-caught,
  not argued away: the plan cited a receipt its declaration did not carry, the
  first shape of the cache fix violated the frozen count until the reviewer's
  FAIL forced the fold, and the first settlement run named uncommitted traces
  until the monitor exposed it.

## SHONEN

One line per box of `SHONEN.md` (four boxes; the file is byte-identical
base→tip):

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane assertion; pointer `reports/round-1-calibration.md#box-1` (no independent promotion verifier this round).
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer `LOG.md` Round 78 entries + `SCORECARD.md` capability row.
- [~] Instructions executable by an agent without oral context — pointer `.ufo/evidence/round-21/coldread/ledger.json` (input-keyed monitor); no independent verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` byte-identical base→tip; pointer `reports/round-1-calibration.md#box-4`.

## Metadata

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (no package, tool or binary was installed or upgraded).
- L0 questions: none; no operator decision blocks the round.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows
  no untracked file this lane's seats wrote at the fleet root (the only
  untracked non-`.ufo`/non-`.scratch` path, `after`, predates the round and
  belongs to another lane — named, untouched).
- Wave read: 12 seats, 12 results, 0 dead; votes on record — `T78W1R1` C1 PASS
  on the final bytes (pre-fold FAIL retained), `T78W1R2` C2 PASS with an empty
  matrix diff, `T78W1C1` no admission judgment with the count deviation and the
  absent-receipt finding recorded.
- Named survivors for round 79: the leak detector is a nested closure and
  `return set()` survives 21/21; dropping `-I` from the python tuple survives;
  arm21's `HEAD != rev` self-guard removal survives; the unguarded
  `isinstance(interp, str)` clause; the simplifier's builder de-duplication; the
  scout's table of 9 selfstate and 11 wave-reconcile unprotected rules with a
  measured single-edit mutant each (`.ufo/waves/round-78/w1/T78W1SC1.md` §1).
