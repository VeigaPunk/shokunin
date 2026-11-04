# kengaku — round 80 (hyaku run 15, attempt 1)

Lane: `kengaku-shokunin` · axes: **novelty + calibration** (LLM/model research and evaluation)
Date: 2026-11-04 · L1 seat: `KengakuR80` · genre: instrument + measurement
Base `dce7c275381c669e6489f1b795b1505d0824c262` (round-79 verifier spot-check)
Freeze `af51132d8919cedd14d3d3407ae5abc966d5d427`; amendments A1 `6250e94b`, A2 `5b11bc5f`,
A3 `bb3d6555`; final lane tip `507d249b32eb90863cd0dc78a5672f777ce9d658`
(`git -C kengaku-shokunin ls-remote origin refs/heads/master` prints the same hash).

## Work performed

The round declares **two claims** (frozen in `plans/round-80-claims.md`): **R80-C1** on **coverage**
(the lane's lowest non-retired axis, held at its L0 cap of 7) — the six members the round-79 ledger
priced `executed-unlocated` become located, reproducible `executed` replays; and **R80-C2** on
**calibration** (held at its ceiling of 10, exercised) — the round-79 verifier spot-check's six
routed defects `V1`…`V6` are discharged, not restated. Both verify; no axis is harmed.

- **R80-C1 freeze.** `plans/round-80-claims.md` (predicate, universe derived from the base ledger,
  target, controls, kill rule), `plans/round80_probes.json` (frozen member → historical receipt,
  instrument, argv, timeout), `plans/round80_c1_located_replay.py` (gate: subject shape, stamp
  hashes, block, ledger, reproduction), `plans/round80_c1_remint.py` (mint driver), the before
  receipt and three losing controls — `af51132d`; amendment A1 (the block is the instrument's
  verbatim stdout with `REV` stripped) `6250e94b`.
- **Six re-mints executed on real domain work.** `python3 plans/round80_c1_remint.py --lane <clean
  checkout at bb3d6555> --work /fast/scratch/hyaku/kengaku-r80/remint4-work` → `REMINT minted=6
  failed=0`; receipts `corpus/evidence/round80/{cancel-async-tasks,chess-best-move,
  distribution-search,largest-eigenval,openssl-selfsigned-cert,protein-assembly}-probe.txt`
  (committed `446b157f`). Each block is the instrument's stdout; the openssl divergence
  (`HISTORICAL-DIVERGENCE 8` under the projection) and the protein environment drift
  (`HISTORICAL-DIVERGENCE 2`, biopython 1.88 vs 1.85) are disclosed in the receipt.
- **Ledger flip.** The six rows go `executed-unlocated` → `executed` with `subject=tb2-header`, the
  receipt's own verdict form, `round=80`; every `classes` list and every other member unchanged
  (audited by `LedgerFlipAuditR80`; only the allowed keys dropped plus an EOF newline) —
  `6669fe72`. The round-79 population gate prints `executed=24 unlocated=0`, `DEFECTS n=0`.
- **R80-C2 discharge.** Six rows `R79-V1`…`R79-V6` appended to `corpus/routed-findings.jsonl`;
  V1's repair receipt `corpus/evidence/round80/v1-r78-c1-at-148801a6.txt` (`PREDICATE R78-C1 pass`
  at the historical revision); V2–V5 corrections in `corpus/lessons/round-80.md`; V6's stamped
  re-mints `r79-c1-after.txt` / `r79-c2-after.txt` (`plans/round80-restamp.json`) — `6669fe72`,
  `446b157f`, `84a89e4e`, `0cb34bf2`.
- **Frontier step.** S258 registered (`corpus/SOURCES.md`), the census run before and after, two
  mistakes mined (M80-1, M80-2), the round lesson `corpus/lessons/round-80.md`; the round's evidence
  cites S258. Commits `e985e56a`, `28f8e4c8`.
- **Wave.** One v1 wave `kengaku-r80-w1` (14 seats) — spec `6669fe72`, ready/dispatch and 13 seat
  reports plus `w1-results.json` (`e985e56a`, `28f8e4c8`, `507d249b`). The attack seats changed
  committed bytes: the sentinel's mint-provenance finding produced A3 (HEAD + `MINTED_BY_SHA` +
  pre-write cleanliness), the mutation-tester's four isolated checks grew the mutants battery 6 → 10,
  the reviewer's two P1s are recorded as limits (see **Trend verdicts**), the C2 auditor corrected
  V3/V4 wording.
- **Clean-tree gate block.** `corpus/evidence/round80/gates-clean.txt` (`2763c581`): `python3
  grader.py` → `CHECKS n=733 mismatches=0`; R79-C1 → `DEFECTS n=0`; `routed_open.py` → `ROWS
  total=111 open=31 blocked=1 closed=77 refused=2`; R80-C2 → pass; R80-C1 → pass, every `EXIT 0`,
  `WORKTREE clean`.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only other
  lanes' files and `.scratch/`; no file from this round's seats landed in the fleet root (`after`
  predates the round, 2026-11-03 20:05; untouched). No fleet-root deletion made.

## Landed changes

- **Freeze + predicates/controls:** `plans/round-80-claims.md`, `plans/round80_probes.json`,
  `plans/round80_c1_located_replay.py`, `plans/round80_c1_remint.py`,
  `corpus/evidence/round80/{c1-before,c1-selftest,c1-mutants,c1-control-*}.txt` — LOG.md §Round 80
  bullet 1 — `af51132d`, `6250e94b`.
- **Six located replays + ledger flip:** `corpus/evidence/round80/*-probe.txt`,
  `plans/grader-population-ledger.json` — LOG.md §Round 80 bullet 1 — `6669fe72`, `bb3d6555`,
  `446b157f`.
- **V1–V6 discharge:** `corpus/routed-findings.jsonl` (six rows), `plans/round80_c2_spotcheck_debt.py`,
  `corpus/evidence/round80/v1-r78-c1-at-148801a6.txt`, `plans/round80-restamp.json`,
  `plans/round80-restamp-c2-only.json`, `corpus/evidence/round80/{r79-c1-after,r79-c2-after}.txt` —
  LOG.md §Round 80 bullet 2 — `6669fe72`, `446b157f`, `14cfe3d0`, `84a89e4e`, `0cb34bf2`.
- **Corrections, lesson and indexes:** `corpus/lessons/round-80.md`, `corpus/README.md`
  (round-79 spot-check + round-80 lesson rows, Round-80 artifacts section), `SCORECARD.md`
  (round-80 section + capability row + planned 81), `LOG.md` §Round 80 — `6669fe72`, `e985e56a`,
  `28f8e4c8`.
- **Registry:** `corpus/SOURCES.md` S258 (own-work, tier A) + census receipts — `e985e56a`.
- **Wave evidence:** `.ufo/waves/round-80/` (spec, dispatch, registry, 13 reports, results) —
  `6669fe72`, `e985e56a`, `28f8e4c8`, `507d249b`.
- **Gate block:** `corpus/evidence/round80/gates-clean.txt` — `2763c581`.

## Before → after measurements

**R80-C1 / coverage.** Counting command (the gate; before uses `--rev` at the base):

```
python3 plans/round80_c1_located_replay.py --lane . --rev dce7c275   # before
python3 plans/round80_c1_located_replay.py --lane .                  # after
```

- Before (`corpus/evidence/round80/c1-before.txt`, measured at `dce7c275`):
  `TARGET members=6 located=0 reproduced=0 ledger_flipped=0 diverged=0 defects=6`, `DEFECTS n=6`
  (six `RECEIPT-UNTRACKED`), `PREDICATE R80-C1 fail`, rc 1.
- After (`corpus/evidence/round80/c1-after.txt`, measured at `446b157f`):
  `TARGET members=6 located=6 reproduced=6 ledger_flipped=6 diverged=2 defects=0`,
  `LEDGER-GATE rc=0 executed=24 unlocated=0 defects=0`, `PREDICATE R80-C1 pass`, rc 0.
- Batteries (`c1-selftest.txt`, `c1-mutants.txt`, `c1-control-*.txt`): `SELFTEST cases=19 red=15
  failures=0`, `MUTANTS real=10 killed=10 survived=0`, three controls `target_reached=False`.

**R80-C2 / calibration.** Counting command:

```
python3 plans/round80_c2_spotcheck_debt.py --lane . --rev dce7c275   # before
python3 plans/round80_c2_spotcheck_debt.py --lane .                  # after
```

- Before (`corpus/evidence/round80/c2-before.txt`, measured at `dce7c275`): six
  `DEBT-UNREGISTERED`, `INDEX … indexed=no`, `DEFECTS n=7`, rc 1.
- After (`corpus/evidence/round80/c2-after.txt`, measured at `0cb34bf2`, `WORKTREE clean`):
  `TARGET ids=6 closed=6 checks_passed=6 indexed=yes`, `DEFECTS n=0`, `PREDICATE R80-C2 pass`, rc 0.
- Batteries (`c2-selftest.txt`, `c2-mutants.txt`, `c2-control-presence.txt`): `SELFTEST cases=9
  red=8 failures=0`, `MUTANTS real=4 killed=4 survived=0`, control `target_reached=False`.

**Both claims against a do-nothing control.** C1's cheapest skips (ledger-only flip, header-only
stamp, copied block) each lose at the frozen counter; C2's cheap skip (register/close with the
spot-check as `close` and `true` as `check`) dies on `CLOSE-NOT-REPAIR` ×6 + `CHECK-TRIVIAL` ×6.

## Sources & frontier

Counting command (run at round start and round end):

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku
```

- Before (`corpus/evidence/round80/census-before.txt`): rc 0, **249** rows, **26** `W04` warnings.
- After (`corpus/evidence/round80/census-after.txt`): rc 0, **250** rows, **26** `W04` warnings.
- Rows added by tier: **1 tier-A** row — **S258**, `own-work`: the six located-replay receipts, the
  frozen probe table and the gate; quote at `corpus/evidence/round80/cancel-async-tasks-probe.txt`
  line 1; six receipt sha256s in the lesson's Gate. No tier-B/C rows added.
- Rows touched old→new: **S258 absent → `mined`** (recheck `90d`, used-by
  `corpus/lessons/round-80.md`, `SCORECARD.md`). No existing row's `status`/`recheck`/`used-by`
  changed. **S256 is kept with its duplicate-URL `W04` stated** (V5): the same URL as S180 for a
  distinct scope (the harness execution model vs the grader bytes), so scoping it out would leave
  the R79 blocker taxonomy unsourced; the warning is written in the lesson's census reading.
- Frontier rows advanced: **none of the five `## Frontier` bullets is discharged this round.** The
  round moves the population ledger's located set (18 → 24 `executed` members) and leaves
  `considerthese` proposal 3 (batch sweep + class histogram) as the next frontier-adjacent move.
  `Assimilation: none` — `/home/vgpnk/Projects/shokuknow/merge/kengaku/` stays unadopted at open L0
  `kengaku | round-54`. `considerthese/2026-10-26.md`: proposal 1 (routed-findings burn-down) used;
  proposal 2 (`tb2_grader_admit`) stays open; proposal 3 named as round-81 work.
- Mistakes mined: **M80-1** `unverified-reproducibility-claim` (round-79's "all six re-runnable
  today" was false on this host: `ModuleNotFoundError: No module named 'Bio'`; fix = the frozen
  probe table's interpreter prefix, which the driver and gate both use) and **M80-2**
  `historical-observation-drift` (the openssl receipt's two historical mismatches no longer
  reproduce; fix = keep the historical receipt and its sha, state `HISTORICAL-DIVERGENCE`; the fix
  fails when the note is removed — selftest case `divergence-unnoted`). Both in
  `corpus/lessons/round-80.md` `## Mistakes`.

## Trend verdicts

- **expansion: improved.** The located-replay population grows 18 → 24 `executed` members (six
  receipts, six ledger rows); a new capability row (`located-replay-mint`) enters `SCORECARD.md`
  with a demonstrated command and committed receipt; S258 adds a tier-A row; the mutants battery
  doubles (6 → 10). Evidence: `c1-after.txt`, `SCORECARD.md` §Round-80 capabilities,
  `census-after.txt`.
- **quality: improved.** Two attack-driven hardenings landed as amendments with evidence
  (A2 projection, forced by six eigen runs whose full-block hashes alternate while the projection
  hash is identical; A3 mint provenance, forced by the sentinel), the mutants battery now kills every
  committed mutant, all four controls lose, and the clean-tree gate block is green at `e985e56a`.
  Evidence: `c1-selftest.txt`, `c1-mutants.txt`, `c1-control-*`, `gates-clean.txt`.
- **discernment: improved.** Thirteen seat reports; four attack seats changed committed bytes; the
  reviewer's two P1s are recorded honestly rather than argued away — (a) the eigen receipt failed
  strict byte equality at its measured tip, which is exactly what A2 answers with its six-run
  evidence; (b) A1–A3 are contract edits made before landing, recorded as a limit and raised to L0
  (`kengaku | round-80`). `CriticC1R80` settled without a report (truncated progress note) and is
  recorded as one undelivered seat, not as a pass. The divergence disclosures (openssl 8, protein 2)
  and the stamp-field limit (`WORKTREE clean` and `LANE_TIP` are producer assertions; the gate
  proves the re-run, not the past) are stated, not hidden. Evidence: `.ufo/waves/round-80/w1/`,
  `corpus/lessons/round-80.md` §Wave findings.

## SHONEN

- [~] **SKILL.md contains real decision tables, error patterns, checklists, cited sources** —
  `SKILL.md` §Decision table — grader class → offline replay recipe (16 derived `executed k of n`
  rows), anti-patterns, production checklist, cited-source bullets; unchanged this round except the
  population/ledger pointer rows round 79 landed.
- [~] **At least one end-to-end domain task executed and logged in LOG.md** — six real offline
  replays executed at `bb3d6555` and logged in `LOG.md` §Round 80 (`REMINT minted=6 failed=0` in
  `corpus/evidence/round80/*-probe.txt`).
- [~] **Instructions executable by an agent without oral context** — `plans/round-80-claims.md`
  fixes the predicate, universe, controls and kill rule; the gate's docstring carries the exact
  commands; the wave's 13 seats exercised them from the freeze commit alone.
- [~] **No cross-domain bleed (PROVINCE.md still accurate)** — no new surface absorbed; the
  connector's per-lane scan (`ConnectorR80.md`) routed siblings rather than adopting; `PROVINCE.md`
  unchanged.

## Round shape and seats

One v1 wave (`kengaku-r80-w1`, policy band 8–16): **14 seats**, **0 residual calls**, round total
**14**. Roles: executor 6, scribe 2, reviewer 1, critic 1, mutation-tester 1, sentinel 1,
connector 1, scout 1. Attack roles (reviewer, critic, mutation-tester, sentinel) **4/14 = 29 %**
(≥ 25 %); connector seats 1 (≤ 2). The canonical planner seat is held by the L1 (no planner seat in
the wave, per the orchestrator ruling). **13 seats delivered a report; `CriticC1R80` settled with a
truncated progress note and no report** — recorded as undelivered, not as a pass. Dispatch evidence:
`.ufo/waves/round-80/w1/{w1-spec.json,w1-dispatch.json,w1-results.json}` + 13 seat reports.

## L0 questions

- Carried unchanged: `kengaku | round-25/33/51/54/56/63/65/66/67/72/74/76`.
- New: `kengaku | round-80` — a closure reviewer held that A1–A3 changed the frozen reproduction
  predicate before landing; a ruling on whether L1 pre-landing amendments with evidence (and a
  selftest case) are acceptable, or must wait for a successor round's frozen predicate, would settle
  it. The round routed around it: the amendments are documented in the plan with their evidence and
  a round-81 successor rule is planned.

## Tooling

- `biopython 1.88` — fetched per invocation through `uv run --no-project --with biopython`
  (uv 0.13.0, uv-managed CPython 3.15), no host install; reason: the `protein-assembly` replay
  imports `Bio`, which the host Python 3.14.8 does not provide (M80-1). Recorded in
  `plans/round80_probes.json` and `ScoutHostR80.md`. No pacman transaction was run (pause respected).

**Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
