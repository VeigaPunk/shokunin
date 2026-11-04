# kasegi — round 68 report (attempt 3)

Lane: `kasegi-shokunin` · round 68 · base `d0f48405e7fe44a53a28305785dc4d881a414194` · final lane hash
`b0b9fb871e3cf45a51febd7671e2331c4f54637a` · measured implementation
`82b3b7d4704e914eb224e7bb24e57aa9cbd8603f` (gate sha256 `10c8710080078fe07534eae8fcc1344ade9ae852be500e66a2804eb68b74fee8`).

**Declared claims (2), frozen at `7c4f9f7ec096298b1edd1912249e5864ee73d985` before any implementation
byte landed** (`.ufo/waves/round-68/claims.json`):

- **C1 — depth:verifiability (lowest non-retired axis, 4).** The derive gate must refuse, at parse
  time, the two program-execution flags the round-67 sentinel measured as admitted-and-executing
  through allow-listed heads (`sort --compress-program`, `git show --textconv`), and execute neither
  named program. Nominal under QUALITY R58: the axis's citation-resolution metric is not read by this
  gate, so the score is reported **4 → 4 (delta 0)**.
- **C2 — coverage (8).** Admit frontier **F46** on one new source row **S102**, the OpenSSF Scorecard
  API swagger 2.0 contract, as the machine interface to published scorecard results.

## Work performed

1. **C1 repair landed.** `corpus/instruments/figure-audit.py` gained `--compress-program` in sort's
   denied-flag tuple and `--textconv` in `git show`'s, four selftest cases (pin 73 → 77), a docstring
   amendment and a comment naming the measured base behaviour — commit `82b3b7d4`; gate sha256
   `10c87100…74fee8`; diff read by SentinelGate (`w1/SentinelGate.md`).
2. **C1 frozen counter built before the freeze and pinned.** `.ufo/waves/round-68/controls/c1-probe-run-r68.py`
   (sha256 `785e38fd…496b4b`, pinned in `claims.json`): eight measurements over a self-built fixture —
   parse refusal plus marker runs for each flag, five legitimate read-only controls, the selftest,
   the committed mutant battery, the real 35-figure ledger, a red fixture, and a no-write-side-effect
   snapshot. Committed in `3dfe6f16`.
3. **C1 no-work control measured and committed before the freeze.** The same counter on the base gate
   bytes (`controls/base-gate-d0f48405.py`, sha256 `8147350c…7ad247`) prints
   `VERIFY measurements=8 failures=4` exit 1: base admits both flags, runs the compressor **18288**
   times and the textconv driver **once**, pins 73 selftest cases and fails the write-side-effect
   measurement (`controls/c1-base-donothing-r68.txt`).
4. **C2 source opened, captured and refused-where-wrong.** S102 captured with the lane instrument
   (`corpus/source-snapshots/round-68/S102.txt`, 429 lines, sha256 `6ebb8552…c2caa0`, HTTP 200,
   11802 fetched bytes, 2026-11-04T21:49:46Z) and a manifest with 8 pinned quotes; a served project
   instance (`/projects/github.com/ossf/scorecard`) was opened the same instant and **refused** as an
   entry source (single-line JSON, instance values only). ScoutS102 re-captured independently and got
   the identical snapshot digest (`w1/ScoutS102.md`).
5. **C2 corpus text landed.** Entry `corpus/knowledge/openssf-scorecard-api-contract.md` (173 lines,
   G1–G8 ground table, "what the document does NOT say" with measured zeros, 13 located Gate quotes,
   its own access date), README F46 row, SOURCES row S102, `knowledge-expected.txt` 83 → 84 — commit
   `29f1ff59`; connector screen SCOPE CLEAR (`w1/ScopeF46.md`).
6. **One v1 wave, 12 seats, all settled** (WAVE-DONE received; `w1-results.json`): reviewer ×2, scribe
   ×2, executor ×2, critic, mutation-tester, sentinel, revenger, scout, connector; attack seats 5/12
   (42 %), one connector, no dead seat, no replacement, no residual call. L1 `KasegiR68a3` holds the
   planner seat (the validator rejects a planner role). Reports under `.ufo/waves/round-68/w1/`.
7. **Attack result accepted and recorded, not hidden.** CriticC1 **defeated the repair as a class**
   while the frozen predicate passed: unique long-option prefixes of `--compress-program`
   (`--compress-prog=`, `--compress=`, `--co=`) are admitted by this host's uutils sort and run the
   compressor (18288 runs each), `git show <commit>` runs a config-declared textconv driver through
   `.gitattributes` with **no flag at all**, and `git cat-file --textconv/--filters` still execute
   (`w1/CriticC1.md`, `w1/SentinelGate.md` F1 HIGH, `w1/RevengerC1.md`, `w1/ReviewC1.md`). These are
   named residuals for round 69, outside the claim's declared spelling set.
8. **Independent reproduction.** ReviewC1 reproduced the frozen predicate from a `git archive` export
   at `82b3b7d4`; ExecHarness reproduced **both ends** from clean exports byte-identically
   (`controls/seat-reproduction-r68.txt`); MutationC1 killed 5/5 one-limb mutants with 2 equivalents
   and 1 invalid control; SentinelGate's 40+-derive admission parity found no widening and no new
   execution path.
9. **Round-67 routed defects worked.** V67-1 (stale quote count), V67-3 (C15 anchor), V67-4
   (driver-pins note) fixed as appended corrections; V67-2 reduced — `citation-ground-check.py
   --root .` findings **10 → 6** and `class-lane-bare` **5 → 1**; V67-5 partially (inherited
   `recheck-audit.py` exit 1 with 9 `cwd_fail` recorded); V67-6 untouched (operator-owned
   `.ufo/state`). See lesson § "Round-67 routed defects — disposition".
10. **Inherited state (attempts 1–2).** `.ufo/watchdog.log` records `lane-dead-no-report kasegi
    round=68` at 18:36:33 and 18:42:43; the lane repo was byte-clean at `d0f48405` when this attempt
    started, so **nothing was inherited** — no uncommitted outputs existed to reuse or discard. That
    is recorded as M68-5 in the lesson.
11. **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no file any
    round-68 seat wrote into the fleet root; the only untracked fleet-root file (`after`, 24 bytes,
    2026-11-03) predates this round and does not name this lane, so it was left untouched.
12. **Scratch discipline.** Every seat worked under `/fast/scratch/hyaku/kasegi-r68/<Seat>/`; three
    `strace` traces above 1 MiB were skipped by the commit helper and deleted rather than committed;
    `/fast/scratch/hyaku/kasegi-r68` holds no live work.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| pre-freeze C1 counter, base gate export, base no-work and candidate-trial receipts, S102 capture + manifest | round-68 bullet 2–4 | `3dfe6f162c9cec8fdbb629738b36fc53a7ce6128` |
| frozen claims (`.ufo/waves/round-68/claims.json`) | round-68 bullet 5 | `7c4f9f7ec096298b1edd1912249e5864ee73d985` |
| C1 gate repair + four selftest cases + docstring (pin 73 → 77) | round-68 bullet 6 | `82b3b7d4704e914eb224e7bb24e57aa9cbd8603f` |
| C2 entry, README F46 row, SOURCES S102 row + registry bullet + lead retirement, `knowledge-expected.txt` 83 → 84, round-67 corrections, SKILL registry fact + r68 amendment, LOG, SCORECARD, lesson | round-68 bullets 5–12 | `29f1ff59007731ca94cb0869209e8bf60626b563` |
| wave spec/dispatch/ready, `w1-results.json`, 12 seat reports and receipts, C1 final measurement, C2 after-counters, seat reproductions | round-68 bullets 7–10 | `b0b9fb871e3cf45a51febd7671e2331c4f54637a` |

## Before → after measurements

### C1 — depth:verifiability, 4 → 4 (delta 0, nominal per R58)

Counting command (frozen, counter sha256 `785e38fd…496b4b`):

```
python3 -B .ufo/waves/round-68/controls/c1-probe-run-r68.py --gate <gate> \
        --work /fast/scratch/hyaku/kasegi-r68/L1/FINAL --mode candidate
```

Measured commit **`82b3b7d4704e914eb224e7bb24e57aa9cbd8603f`**; receipt
`.ufo/waves/round-68/controls/final-verification-r68.txt`:

```
MEASURE sort-compress-refused ok rc=2 marker_runs=0
MEASURE git-textconv-refused ok rc=2 marker_runs=0
MEASURE read-only-controls-admitted ok controls=5 failed=0
MEASURE selftest ok selftest cases=77 failures=0 rc=0
MEASURE mutbat ok rc=0 mutbat killed=5/5 survivors=0 invalid=0 controls=pass
MEASURE real-ledger ok FIGURE-AUDIT figures=35 ok=35 stale=0 exit=0 rc=0
MEASURE red-fixture ok rc=1
MEASURE no-write-side-effect ok fixture_changed=0 marker_runs=0
VERIFY measurements=8 failures=0 gate_sha256=10c87100…74fee8 mode=candidate
```

Before (same counter, base gate bytes, measured and committed **before the freeze**;
`controls/c1-base-donothing-r68.txt`):

```
MEASURE sort-compress-refused FAIL rc=1 marker_runs=18288
MEASURE git-textconv-refused FAIL rc=1 marker_runs=1
MEASURE read-only-controls-admitted ok controls=5 failed=0
MEASURE selftest ok selftest cases=73 failures=0 rc=0
MEASURE mutbat ok rc=0 mutbat killed=5/5 survivors=0 invalid=0 controls=pass
MEASURE real-ledger ok FIGURE-AUDIT figures=35 ok=35 stale=0 exit=0 rc=0
MEASURE red-fixture ok rc=1
MEASURE no-write-side-effect FAIL fixture_changed=0 marker_runs=18289
VERIFY measurements=8 failures=4 gate_sha256=8147350c…7ad247 mode=base
```

The do-nothing control (base bytes, no work) fails 4 of 8 measurements, so the target is one a
no-work round cannot reach. **Verdict: verified on the frozen predicate; class-level residual open.**

### C2 — coverage, 8 → 8 (delta 0)

Counting commands (frozen in `claims.json`), measured at the landed lane tip
(`29f1ff59` for the corpus bytes); receipt `.ufo/waves/round-68/controls/c2-after-counters-r68.txt`:

```
python3 corpus/instruments/frontier-recheck-count.py
FRONTIER-CENSUS rows=46 admitted=46 closed=46 problem-rows=0 registry=102
FRONTIER-PASS F46 ids=S102
entries=49 pass=49 exit=0

python3 corpus/instruments/capture-binding-check.py
records=82 bound=82 unbound=0

wc -l corpus/instruments/knowledge-expected.txt        -> 86
grep -vc '^#' corpus/instruments/knowledge-expected.txt -> 84
LC_ALL=C sort -c corpus/instruments/knowledge-expected.txt -> exit 0

scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi -> exit 0
kasegi	ok	/home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/SOURCES.md
```

Before (`controls/c2-base-counters-r68.txt`, base `d0f48405`): `rows=45 admitted=45 closed=45
problem-rows=0 registry=101`, `entries=48 pass=48`, `records=81 bound=81 unbound=0`, knowledge 85
lines / 83 entries, census exit 0. **Verdict: verified.**

## Sources & frontier

`SOURCES.md` rows **101 → 102** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` over
`corpus/SOURCES.md`: 101 at base → 102 at the tip). Counting command for the whole section:

```
python3 corpus/instruments/frontier-recheck-count.py   # rows=46 admitted=46 closed=46 registry=102
python3 corpus/instruments/capture-binding-check.py    # records=82 bound=82 unbound=0
scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi   # exit 0
```

- **Rows added by tier:** one row, tier **A**, kind `docs`, status `mined`, `used-by`
  `corpus/knowledge/openssf-scorecard-api-contract.md` — **S102** (OpenSSF Scorecard API swagger 2.0
  contract). Tier histogram A 89 → 90, B 5 → 5, C 5 → 5.
- **Rows touched old → new:** S102 added (new); the `## Leads (unopened)` line "OpenSSF Scorecard
  aggregate-score/API documentation" retired **as opened** (old → new: lead line removed, row S102
  added, F46 in `corpus/README.md`); the Fuzzilli lead stays open. One `## Registry changes` bullet
  appended. No existing row's status, recheck or `used-by` changed.
- **Frontier rows advanced:** F46 admitted (rows 45 → 46, `FRONTIER-PASS F46 ids=S102`); knowledge
  entries 83 → 84; capture records 81 → 82; `knowledge-expected.txt` 83 → 84 entries.
- **Capture evidence:** `corpus/source-snapshots/round-68/S102.txt` (429 lines, sha256
  `6ebb8552…c2caa0`), 8 pinned quotes, longest 9 words, every anchor verified
  (`source-recheck.py --source S102` exit 0). An independent seat re-capture reproduced the identical
  snapshot digest.
- **Assimilation: none.** `merge/kasegi/` was not used this round (its staged material does not serve
  either frozen claim); `considerthese/`'s latest still-unimplemented proposal remains the six-file
  end-to-end domain task, which this round did not run, so no consideration is claimed implemented.

## Trend verdicts

- **Expansion — improved.** F46 admitted on ground the lane did not hold (ScopeF46: no held row,
  capture or sibling province carries the swagger route family or the aggregate-score field; F35
  explicitly left the API out), registry 101 → 102, knowledge 83 → 84, frontier 45 → 46, capture
  records 81 → 82, census exit 0.
- **Quality — improved.** A measured program-execution path through allow-listed heads is closed at
  parse time with a base control proving it executed (18288 + 1 runs → 0), the selftest pin moved
  73 → 77 with 5/5 mutants killed, and six round-67 routed defects were worked (three fixed as
  appended corrections, one reduced, two recorded). No knowledge entry was superseded and no admitted
  row was harmed; the ledger still re-derives 35/35.
- **Discernment — improved.** The wave's attack seats defeated the repair **as a class** before the
  round closed and their receipts were landed rather than buried (CriticC1, SentinelGate F1 HIGH,
  RevengerC1, ReviewC1); the round's own candidate mistake (M68-1, a residual that does not
  reproduce) and its wrong-observable mistake (M68-2) are in the lesson with the receipts that
  caught them; the round reports a delta-0 score on both axes instead of claiming movement.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  resolvable pointer: `SKILL.md` registry row `figure-audit.py` (selftest pin 73 → 77) and the r68
  current-execution amendment; author-asserted, outside promotion verification still required.
- `[ ]` At least one end-to-end domain task executed and logged in LOG.md — untouched: no authorized
  end-to-end bounty task this round; both domain roots remain absent and live-target testing is
  refused (`corpus/lessons/round-61.md`).
- `[~]` Instructions executable by an agent without oral context — resolvable pointer: the frozen
  counter and the wave context executed end to end by 12 seats and by two independent reproductions
  (`controls/seat-reproduction-r68.txt`).
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — resolvable pointer: `PROVINCE.md`
  unchanged this round; ScopeF46 found no sibling-lane claim on the Scorecard API ground
  (`w1/ScopeF46.md`).

## Round shape, dead seats, tools, stale lane

- **Shape:** one v1 wave, 12 seats (`w1-dispatch.json` spawn=12, band 8–16), attack seats 5/12
  (42 %), connector 1, no residual call; **round total 12 seats**. **Dead seats: 0.**
- **Tool installs:** none; no routing, alias, concurrency or host change; pacman untouched (guard
  honoured).
- **Stale-lane:** respawn-per-round driver; no other kasegi mission open. `.ufo/state/kasegi.round`
  still reads `17` (operator-owned stale driver state, routed as V66-4/V67-6; the MANIFEST closure
  ledger is the round authority).
- **Open L0 questions:** none added this round; the earlier unanswered rows (r15 source restoration,
  r57 R67/R69 counter-substance, r59/r60 derive-gate security boundary) stay open and are routed
  around, not answered.
