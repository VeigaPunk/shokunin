# Round 24 — F2 write-safety census, coverage-map agreement, receipt verify/run symmetry

Author: SoujiR24 (lane identity `souji-shokunin <souji@shokunin.local>`). Lane base
`a65fac98964b445758e94c805728c9a19d302ff8`; preregistration
`.ufo/waves/round-24/preregistration.txt` (frozen before data, commit `f9db218`), append-only
amendment 1 (`.ufo/waves/round-24/preregistration-amendment-1.txt`). Inbound: the r23 verifier
spot-check's routed defect (README F2 coverage-map table vs its prose) and SCORECARD's `r24 — planned`
row (F2 `/var/tmp` write-safety fixture excluding `git fsck --lost-found`; residual C1/C2 limits).
Lane HEAD `2e7efcf929c7fb15c63d9190a5d81c0dc63395ea` (final receipts commit). All receipted
figures verify at their revision (`python3 -B tools/souji-receipt-run.py verify --root . <receipt>`).

## Work performed

Three declared claims, one per axis, each frozen with a control and an after-value.

- **C1 — coverage (8). F2 debris census.** `tools/souji-size-census.py` reads `count-objects -v`
  (+ `fsck --unreachable --no-reflogs`) against the resolved COMMON git dir with an allowlisted,
  timeout-guarded read-only envelope (SentinelSizeEnvelope overrides; promisor/partialClone/`--lost-found`
  refused exit 2; `--repo` must be the repository top level). Fixture `tests/fixtures/r24-size-census.py`
  fences 8 frozen cases with a common-dir `.git` manifest and a real blobless-clone refusal arm.
  Do-nothing control: stub emitter `cases=8 pass=4` (receipt `c1-control-stub.tsv`); after at tip
  `cases=8 pass=8 control=FALSE-GREEN-REJECTED lost_found=WRITE-DETECTED` (`c1-final.tsv`).
  Lane-bound measurement `census/round-24/size-census-lane.txt` (garbage=0 size_garbage=0 unreachable=1093
  alternates=0) is about this repo only; unreachable=1093 is jj keep-refs/cruft-pack/side-tree debris,
  not a fleet or cleanup figure.
- **C2 — calibration (7, lowest non-retired). Coverage-map agreement.** `tools/souji-coverage-agreement.py`
  re-derives at a full revision every `ground: F<k>` entry's presence in the README coverage-map entries
  column plus dangling map paths. Control at base: `grounded=4 mapped=2 mismatches=2` (`c2-control-base.tsv`);
  after at tip: `grounded=6 mapped=6 dangling=0 mismatches=0` (`c2-final.tsv`); fixture 9/9
  `control=FALSE-GREEN-REJECTED` (`c2-fixture-final.tsv`). Per-entry kill rule (amendment 1) held:
  all four base-grounded entries present with the same F-number at tip (W2C2Rerun).
- **C3 — operability (8). Receipt verify/run symmetry (r23 residuals).** `verify` now refuses a
  non-durable rev and a `tool=` absent from `cmd=` argv; `run` mirrors the argv/redaction/newline
  refusals so every receipt `run` writes parses; counts are read from the last stdout line that starts
  with a counts line. Control base runner `refusals=0/2` (`c3-control-base-runner.tsv`); after
  `cases=8 pass=8 refusals=2/2 regress=5/5` (`c3-final.tsv`); all 19 committed receipts verify.

Frontier step (inside the claim cap): S120–S123 opened and appended; the r23 routed defect became
Q56 (coverage-map agreement) in `corpus/QUALITY.md`; one mistake mined and fixed with a failing
witness (below).

### Round shape

Default two v1 waves, both validated under wave policy v1 and dispatched as ONE `task` call each
(validator `taskCall` unchanged). Wave 1 (build, 38 seats): scout 12, executor 10, scribe 4,
critic 4, reviewer 3, sentinel 1, simplifier 1, revenger 1, mutation-tester 1, connector 1.
Wave 2 (falsify, 35 seats): reviewer 10, critic 10, scout 6, mutation-tester 4, sentinel 3,
scribe 2. Round total 73; dead seats 0 (one seat auto-switched to Claude Opus 4.8 after a safety
filter; no death). L1 held the planner seat (validator excludes `planner` as a swarm role). All
seat reports committed under `.ufo/waves/round-24/w1|w2/` with the specs/dispatch payloads/registries.

## Landed changes

- `f9db218` — preregistration (frozen), assimilation id-collision scratch (reg 119 / staged 134 /
  collisions 11), census-start output (`souji ok`, 119 rows).
- `1efe406` — instruments: `tools/souji-size-census.py`, `tools/souji-coverage-agreement.py`,
  `tests/fixtures/{r24-size-census,r24-coverage-agreement,r24-receipt-verify}.py`, C1 stub control,
  preregistration amendment 1, wave-1 spec/dispatch.
- `ce5971c` — do-nothing control receipts (C1 stub 4/8, C2 2 mismatches, C3 0/2) before any after-data.
- `778747e` — after-state: C1 envelope hardening (allowlist, absolute git, `core.fsmonitor=false`,
  timeout, top-level refusal, `.promisor`-pack refusal), C3 verify clauses + COUNTS_RE widening,
  assimilated entry `corpus/knowledge/count-objects-linked-worktree-garbage.md` (S120–S123),
  SOURCES 119→123, README Round 24 coverage map (F2 row + frontiers), git-repo-structure re-verified
  on git 2.56.0, snapshots `census/round-24/sources/` + SHA256SUMS, quarantine-slice + verdicts.
- `ca7fc1c` — after-receipts at 778747e (C1 8/8, C2 0, C3 2/2+5/5, gate `entries=1 ok=1 fail=0`,
  r13 recheck `selftest=PASS ids=5/5`) and the lane-bound size census.
- `c3ca7ad` — wave-1 seat reports (38) and drafts.
- `d3666c3` — inherited round-23 late seat updates `W2K1.md`/`W2D3.md` (written 06:08/06:09 after
  r23 filed; committed verbatim, superseding the `2f96bf4` text; not r24 claim evidence).
- `315422ba` — post-wave-2 repairs: r23 F4 stdout-section fix in `tools/souji-record-agreement.py`
  (R24-M12), counts-line anchoring in the runner (R24-M13), redaction symmetry closures incl.
  `CMD-SECRET-SHAPED`/`CMD-NEWLINE`/`TOOL-CHECKOUT-DIFFERS` (R24-M16/M25), `--out` restricted to
  `/var/tmp/` (R24-M15), C1 bare-repo fix (R24-M24), entry/README/S118/S115/S123 corrections,
  `corpus/lessons/round-24.md` (Mistakes R24-M1..M25, Gate, Q56), Q56 in QUALITY.md, SCORECARD/LOG
  appends.
- `2e7efcf` — final after-receipts at 315422ba plus r23 fixture regressions (`selftest=8/8`,
  `control=FALSE-GREEN-REJECTED`).

## Before → after measurements

| claim | axis | before (control) | after (tip 315422ba) | counting command |
|---|---|---|---|---|
| C1 debris census | coverage 8 | stub `cases=8 pass=4`, no target line | `cases=8 pass=8 control=FALSE-GREEN-REJECTED lost_found=WRITE-DETECTED` | `python3 -B tests/fixtures/r24-size-census.py --tool tools/souji-size-census.py` |
| C2 coverage-map agreement | calibration 7 | `grounded=4 mapped=2 dangling=0 mismatches=2` | `grounded=6 mapped=6 dangling=0 mismatches=0` | `python3 -B tools/souji-coverage-agreement.py --root . --rev <full40>` |
| C3 verify/run symmetry | operability 8 | `refusals=0/2` (base runner) | `refusals=2/2 regress=5/5` | `python3 -B tests/fixtures/r24-receipt-verify.py --tool tools/souji-receipt-run.py` |

Lane-bound C1 measurement: `census/round-24/size-census-lane.txt` (`garbage=0 size_garbage=0
unreachable=1093 alternates=0`, `invoked_from=main`; this repo only, no fleet figure). All numbers
name their receipts (Q55); every receipt verifies.

## Sources & frontier

- Census: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` — start exit 0
  (119 rows, 30 W04), end exit 0 (123 rows, 31 W04, no E). Rows added: S120 (git.git path.c@v2.56.0),
  S121 (path.c@v2.30.0), S122 (builtin/count-objects.c@v2.56.0), S123 (git-worktree § REFS + § DETAILS),
  all tier A, mined, opened 2026-10-25, recheck on-release. Rows touched: S115 `used-by` old→new
  (+ `count-objects-linked-worktree-garbage.md`); S123 scope widened to cover the § DETAILS quote it is
  cited for. Gate snapshots `census/round-24/sources/` with sha256.
- Assimilation (§10), theme F2 linked-worktree `garbage` false positive: ADMIT r27 (re-sourced to
  S120–S123; reader-decides + `refs` unflagged at both tags) and r25's five-mode matrix (lane-measured;
  C1 case 4 is the committed witness for one spelling, five modes seat-observed). REJECT r26 (central
  claim falsified), r23 (fleet claims, id collisions, wrong "only two fields"), r25 headline and the
  staged provenance cells, each with a flip. Id collisions 11 → 15 (S109–S123); renumbering is by
  document (URL), never arithmetic — map in `.ufo/waves/round-24/assimilation/renumber-map.tsv`.
  Quarantine slice: 8 rows hand-checked `present` (S118 re-graded `accepted` per round-22 definitions;
  its cited DOI is unreachable from here, re-cited to the IEEE record). `considerthese/` absent.
- Frontier: F2 advanced (a single-repo debris census tool and fixture now exist; size attribution and
  concurrency stay owed); F1/F3/F4 unchanged; F5 list-only, reap protocol + NAMESPACE pin operator-held.
  PROVINCE.md's unreachable-census line stays frontier (W2C1Axis).

## Trend verdicts

- **expansion — `unprovable-but-better`.** Entry files 3 → 4 on held F2 ground (+1 front-matter
  normalisation); a new debris-census capability, no new map ground, no SKILL/core move.
- **quality — `improved` (bounded).** `git-repo-structure-readonly.md` re-verifies on git 2.56.0
  (`selftest=PASS ids=5/5`, receipt `r13-recheck-receipt.tsv`; `verified-at` refreshed). The admitted
  `repo-size-census-readonly.md` was marked with a `## Round 24 narrowing` (the linked-worktree read and
  the sequential fixture; concurrency still owed), and the new entry's overstated/false sentences were
  corrected after wave 2 found them (R24-M20/M21).
- **discernment — pending the non-author spot-check** (sample: 2 admits, 3 rejects, 8 slice verdicts;
  two reject reasons were corrected after W2Rejects/W2EntryGate found them false as first written).

## SHONEN

- `[~]` SKILL.md tables and sources — W1 ScoutRegistry/ScoutPathC + SOURCES rows (S120–S123).
- `[~]` End-to-end task in LOG.md — `Round24` block (scorecard/LOG append, receipted figures).
- `[~]` Executable without oral context — C1/C2/C3 tools and fixtures, each with a frozen CLI and receipt.
- `[~]` No cross-domain bleed — ConnSiblings sweep; no sibling overlap; HARD BOUND held (W2Scope).

## Extra items

- **Stale-lane**: respawn-per-round driver; no other mission of this lane is open.
- **Tooling**: no installs or upgrades this round (no pacman transactions; seats installed nothing).
- **Misroot sweep**: no souji round-24 file at the fleet root (W1 ScoutMisrootEarly, W2 W2Misroot);
  tabi has one fleet-root misroot, not ours. Leftover `/var/tmp/souji-r24-ScribeEntry{2,3}` scratch
  removed by the L1 (reported by W2Misroot; the seat's claim of removal was false — R24-M14).
- **Open L0 questions**: none filed. Residuals routed to r25: automated per-entry C2 kill rule
  (W2C2Rerun F3), C2 status-column blindness, C1 fixture cases for bare/subdirectory/partialClone-only
  and the 778747e envelope hardening, three record-agreement fixture cases, counter coverage gaps
  (W2C1MutTool uncovered=7, W2C3Mut uncovered=9).
