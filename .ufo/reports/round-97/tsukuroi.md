# tsukuroi — round 97 report

Lane: `tsukuroi-shokunin` (operability + freshness; host operability and repair). Campaign: hyaku,
run 15. Round 97, attempt 1. Pre-round tip `f48d16428d8bb92fd6cf546a745bff5b624e3f18`; freeze
`a57e88cd`; wave `dafcd5df`; settle `b492f17f`; header repair `5eb475cd`; measured `b3db56a4`;
L1 receipts `9c4b7b16` (lane tip at filing — `git ls-remote origin refs/heads/master` prints
`9c4b7b164f926ee2cb1f8683b4fe8f3f5796b1a9`).

Declared claims — **C1 depth 8** (the tie-lowest non-retired axis): the Limine version gate's
published 1-9-digit component cap certified at its THIRD component, and the accepted leading-zero
spelling; **C2 freshness 9**: a `SKILL.md` registry row's declared values re-derived from the bytes
of the tool each row names. Adjacency (8, tied lowest) carried no claim: the kaidoku/revenger
reverse-engineering ownership is operator-owned and unruled.

## Work performed

- **C1 — depth.** `tools/limine-pin-battery-r97.py` (roster 103 → 105) adds `REFUSAL-VERSIONS-9DIGIT-Z`
  (`12.9.999999999` era B, `0.9.999999999` era A) and `LEADING-ZERO-NORMALIZE` (`12.09.4`,
  `000000012.9.4`, `12.000000009.000000005`, `000000000.000000000.000000000`); `tools/make-r97-bends.py`
  emits the two one-clause bends. Evidence: `before/dev/c1-battery-gate.txt` (`105/105 met`),
  `w1/ExecBattery/report.md` (×3 canonical + ×3 `git clone --shared`, 0 error rows),
  `w1/ExecBend.md` (N05 `103/105`, two families, 6 rc-64 rows; N06 `104/105`, one family, 4 rows; ×3
  both layouts; single-hunk diffs), `w1/ExecDoNothing.md` (control `f06d90ae…` byte-identical to
  `f48d1642:tools/limine-pin-battery-r96.py`, `met 103/103` ×3 on the gate and both bends),
  `after/c1/l1-c1-gate-runs3.json` (L1 re-run ×3 at `b492f17f`), `after/c1/isolation-check.json`
  (lane and battery invisible inside the sandbox).
- **C2 — freshness.** `tools/check-registry-content.py` binds seven cells over four rows
  (`limine-pins` argparse default, `--selftest` tally re-derived by running it, JSON schema token;
  `limine-pin-battery-r96` roster in two cells by AST; `check-r96-calibration` selftest tally;
  `make-r96-bends` variant span) and fails one `RC-VALUE-MISMATCH` per doctored cell. Evidence:
  `w1/ExecRegistryContent/report.md`, `w1/ReviewRegistryContent.md` (constant-derivation patch flips
  the doctored leg `FAIL → PASS`; six fail-closed paths), `w1/MutRegistry.md` (6/8 mutants killed),
  `w1/ScoutDrift/report.md` (the binding-coverage decomposition: of the other 150 rows, 21 carry a
  bindable cell shape, 15 re-derive today, 11 are machine-checkable but unbound).
- **Frontier step.** S392 opened and admitted (CPython `int()` docs, byte-level locator 157767 /
  153202 / 159315); S389/S391 re-opened byte-identical (no drift); one candidate rejected
  (`man.archlinux.org/man/python.1`, HTTP 200, 41 788 bytes, no `int()` or Limine behaviour).
  `corpus/lessons/round-97.md` carries `## Gate` (3 admits, 1 reject), five mined mistakes, the
  census block, the counter-attack scoreboard and the routed table; QUALITY 141 added from the
  locator mistake.
- **Wave.** One v1 wave, 14 seats under `ufo-wave-policy.json` (band 8-16): 5 executors, 2 scouts,
  2 scribes, 2 reviewers, 1 critic, 1 mutation-tester, 1 connector; attack roles by the prefile
  gate's set = 5/14 = **36 %** (floor 25 %), connector seats 1 (limit 2). Validator counts
  **14 spawn / 0 resume / 14 total**, `w1-validate.err` 0 bytes; `.ready` taken 08:48:42; all 14
  settled (`w1-results.json`), **0 dead seats**. Residual call: none (14 ≥ the 8 protocol floor).
- **Ledger.** `.ufo/waves/round-97/claim-falsification.tsv`, 16 rows: 5 `falsifies-wording`
  (A3, A7 ×2, A6, A4), 0 `falsifies-number`, 11 `neutral`; every attack seat appears
  (`ReviewBattery`, `ReviewRegistryContent`, `CriticClaims`, `MutRegistry`, `ConnectorOverlap`).
  Gate: `PREFILE-FALSIFICATION: pass claims=2 rows=16 attack_seats=5 findings=0`, exit 0 (pasted
  below).
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open. The wave's
  `.ready` was taken 08:48:42 and every seat settled; nothing stayed open past the driver's two-tick
  window at filing.
- **Inherited state.** The r96 leftover `.ufo/waves/round-96/after/registry-final.json`
  (spot-check routed 1) is committed under the freeze. No `round-*-aggregator-*` or
  `round-*-verifier-spotcheck.md` file was edited.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows 13 paths; none
  names tsukuroi or round 97, so none is this lane's misroot (`docs_placeholder` and `plans/round-88.md`
  are another lane's r88 plan copies; `.scratch/` is orchestrator-owned; `.ufo/reports/round-97/kama.md`
  is another lane's report). Nothing was copied or deleted.
- **Tool installs:** none (python3, git, curl, bwrap already present; pacman untouched and paused).
- **L0:** no new question. The r86 host incident line stays open (operator-owned repair); the r92
  GH013 line was answered in-file by the lane.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: r97 battery + bends generator + registry-content checker, plan, claims, controls, dev receipts, amended-fixture recipe, r96 leftover receipt | `Round 97 — freeze` | `a57e88cd` |
| wave evidence: spec + dispatch + ready, 14 seat dirs and reports, `w1-results.json`, amendments A1-A7, ledger draft, L1 receipts | `Round 97 — wave` | `dafcd5df` |
| settle: S392 + `knowledge/limine-bound-9digit-z-r97.md` + `lessons/round-97.md` (5 mistakes, QUALITY 141), README § Round 97, SCORECARD declaration, three registry rows, r96 docstring correction | `Round 97 — settle` | `b492f17f` |
| provenance-header repair: r95 trio line-initial, r95/r96/r97 `recheck:` cadences (QUALITY 8/121 green) | `Round 97 — settle` | `5eb475cd` |
| measured outcome: SCORECARD table + capability row, LOG measured line | `Round 97 — measured` | `b3db56a4` |
| L1 receipts: ×3 landed-gate run, battery `--selftest --reference` 18/18, C2 content/coverage at the tip, knowledge-header gate 113/113 | `Round 97 — measured` | `9c4b7b16` |

Every commit above is a `jj-lane.sh` `landed <hash>` line after remote verification; the lane tip
equals `git ls-remote origin refs/heads/master` (below).

## Before → after measurements

### C1 (depth 8)

Counting command: `python3 tools/limine-pin-battery-r97.py --gate <GATE> --runs 3 --work <scratch>
--json <out>`, parsed by `python3 .ufo/waves/round-95/before/controls/count-runs.py <out> --family
REFUSAL-VERSIONS-9DIGIT-Z --family LEADING-ZERO-NORMALIZE`; bends via
`before/controls/bends/<bend>.py`; do-nothing via `before/controls/do-nothing-battery-r96.py`.

| leg | before (r96 instrument `f06d90ae…`) | after (r97) | measured at | receipt |
|---|---|---|---|---|
| landed gate, canonical | `met 103/103` ×3, 0 error rows | `met 105/105` ×3, `[]`, 0 error rows | `a57e88cd`, re-run `b492f17f` | `w1/ExecBattery/c1-gate-canonical.json`, `after/c1/l1-c1-gate-runs3.json` |
| landed gate, clone | — | `met 105/105` ×3, 0 error rows | `a57e88cd` | `w1/ExecBattery/c1-gate-clone.json` |
| `N05-z-cap-8` | `met 103/103` ×3 (blind) | `103/105` ×3, `[LEADING-ZERO-NORMALIZE, REFUSAL-VERSIONS-9DIGIT-Z]`, 6 rc-64 rows/run | `a57e88cd` | `w1/ExecBend/c1-bend-N05-*-{canonical,clone}.json` |
| `N06-leading-zero-reject` | `met 103/103` ×3 (blind) | `104/105` ×3, `[LEADING-ZERO-NORMALIZE]`, 4 rc-64 rows/run | `a57e88cd` | `w1/ExecBend/c1-bend-N06-*-{canonical,clone}.json` |
| roster | 103 | 105 (`len(FAMILY_ROSTER)=105`, `tuple(FAMILIES)==FAMILY_ROSTER: True`, `cases_expected 420`) | `a57e88cd` | `w1/ReviewBattery/roster.txt` |
| instrument self-check | — | `--selftest --reference tools/check-limine-pins.py` → 4 negative controls unmet-of-target, reference gate `105/105`, 12 one-field lie wrappers each unmet, `selftest PASS 18/18`, rc 0 | `9c4b7b16` | `after/c1/battery-selftest-reference.txt` |

### C2 (freshness 9)

Counting command: `python3 tools/check-registry-content.py --revision <REV> --json <out>` and
`--selftest`; the doctored leg is `sh .ufo/waves/round-97/before/fixtures/build-doctored-fixture.sh`
(base pinned `f48d1642`).

| leg | before | after | measured at | receipt |
|---|---|---|---|---|
| landed revision | no such checker; coverage gate row-presence only | `status PASS`, `bindings 7`, `findings []` | `a57e88cd`, `b492f17f`, `b3db56a4` | `w1/ExecRegistryContent/01-landed-content.txt`, `after/c2/content-tip.json` |
| selftest | — | `PASS 12/12`, each one-cell doctor id-exact | `a57e88cd` | `w1/ExecRegistryContent/02-selftest.txt` |
| doctored revision (base `f48d1642`) | coverage gate `PASS 154/154` on the same table | content `FAIL`, six `RC-VALUE-MISMATCH`, rc 1 | `46fae1ba`, `9e052291` | `before/dev/c2-content-doctored.txt`, `w1/ExecRegistryContent/05b-doctored2-content.txt` |
| coverage on the doctored revision | `PASS 154/154 findings 0` (blind) | `PASS 154/154 findings 0` (still blind — the blindness leg) | same | `before/dev/c2-coverage-doctored.json`, `w1/ExecRegistryContent/06b-doctored2-coverage.txt` |
| settled tip | — | content `PASS 7/7`; coverage `PASS 157/157 findings 0` | `b3db56a4` | `after/c2/content-tip.json`, `after/c2/coverage-tip.json` |
| fail-closed | — | missing tool rc 1 / 3 `RC-DERIVE-FAILED`; missing row rc 1 / `RC-ROW-MISSING`; 7-column table rc 2; non-ancestor rc 2; unresolvable rc 2 | clone fixtures | `w1/ReviewRegistryContent/receipts/04-*` |

Instrument integrity at scoring: `sha256sum -c before/instruments.sha256` → **19 OK, 1 FAILED**
(`before/fixtures/build-doctored-fixture.sh`, the A1 recipe correction);
`sha256sum -c before/instruments-r97-after-fixture-pin.sha256` → **20 OK**. The four scoring
instruments (`check-limine-pins.py 7d79ac29…`, `limine-pin-battery-r97.py e678c34f…`,
`make-r97-bends.py 972c672b…`, `check-registry-content.py 2daf5926…`), both bends and the three
do-nothing copies are byte-identical to the freeze manifest.

C1's do-nothing byte-identity is bound to the **control copy**
(`before/controls/do-nothing-battery-r96.py`, `f06d90ae…` = `f48d1642:tools/limine-pin-battery-r96.py`),
not to the live `tools/limine-pin-battery-r96.py`: that live file moved at `b492f17f` by the r96
routed docstring correction (8 +/− 2 lines, wording only), so `.ufo/waves/round-96/before/instruments.sha256`
no longer holds for it in the worktree; its scored bytes are re-derivable at `f48d1642`, and the
control copy keeps them. If a closure checks the r96 manifest against the live tree, that one line
is expected to fail and is accounted for here and in `corpus/lessons/round-97.md` (Routed).

## Sources & frontier

`SOURCES.md` rows before → after: **391 → 392**
(`grep -cE '^\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`; before from `git show
f48d1642:corpus/SOURCES.md`). Rows added by tier: one A (S392 — CPython `int()`, opened 2026-11-08,
quote "have leading zeros, be surrounded by whitespace," at BYTE 157767 of the 331022-byte pin
sha256 `d92580dd…`, `id="int"` at BYTE 153202). Rows touched old→new: none — S389/S391 were
re-opened byte-identical (`6bf2ce2b…`, `a7e00587…`) and their `status`/`used-by` did not change.
Frontier rows advanced: the r96 Frontier's "Z component's 9-digit boundary is uncertified" and "a
9-digit component with leading zeros is unsent" are now families with their own bends; the r95/r96
"registry gate certifies row presence, not content" is closed for seven cells and quantified for the
rest (21 bindable / 15 re-derivable / 11 unbound-but-checkable). Census command and both exits:
`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi` → start `exit 0`
(391 rows), end **`exit 0`** (392 rows, 0 E findings).

Assimilation: none — the `shokuknow` package was not adopted this round (its staged ids still
collide with the lane registry, and no claim here needs it).

## Trend verdicts

- **expansion — improved.** One admitted knowledge entry on ground the coverage map did not hold
  (`corpus/knowledge/limine-bound-9digit-z-r97.md`: the Z leg of the published bound, the
  leading-zero spelling, and the registry-content proposition), its `source:` citing S392 — a row
  opened and admitted this round with a located quote — plus S389/S391 re-opened. S392 is the only
  new row; no row was removed.
- **quality — improved.** Two named r96 Frontier limits are closed by families whose bends fail
  exactly them (`N05` two families / 6 refusal rows, `N06` one family / 4 rows), the r96 Y-family
  docstring defect is corrected in both the successor and the r96 tool with its manifest relation
  stated, the provenance-header gate is green at the tip (113/113, from 110/112 + 5 findings), and
  C2 adds a drift gate that catches six content-only doctors while the coverage gate certifies the
  same table.
- **discernment — improved.** The wave falsified or narrowed five claim clauses (A3, A4, A6, A7 ×2)
  and left three C2 scope gaps and one mutation survivor named rather than smoothed (A4, A5); the
  lane's own locator error was caught by an independent seat's byte-level measurement and turned
  into QUALITY 141 (a criterion, not just a correction). No disagreement was left unlearned; the
  prefile ledger passes with 5 wording rows and 0 number rows.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointers
  SKILL.md:38 (health-verdict decision table), :90 (update-safety checklist), :2028 (error patterns),
  :179 (Sources); this round adds the three r97 registry rows at SKILL.md:5941-5943, each with its
  entry command, verdict map, self-test and pinned values.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the historical pointer is
  `corpus/knowledge/host-health-report-r3.md` + LOG round 3; this round's executable end-to-end check
  is the doctored-fixture discrimination: `before/fixtures/build-doctored-fixture.sh` runs from a
  clean clone to a `FAIL`/`PASS` pair (doctored `46fae1ba`), and the wave reproduced it independently
  (`w1/ExecRegistryContent`, `9e052291`).
- [~] Instructions executable by an agent without oral context — the two recipes
  (`before/dev/run-dev.sh`, `before/fixtures/build-doctored-fixture.sh`) were executed end-to-end
  this round with no oral context and are self-contained (absolute paths, pinned base, asserts); the
  whole-SKILL replay remains unexecuted (unchanged from prior rounds).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` ADJ-01..07 unchanged;
  `w1/ConnectorOverlap.md` swept all 20 sibling repos (`registry-content`, `leading zero`,
  `leading-zero`, `9-digit`, `FAMILY_ROSTER`, registry-cell checkers): 0 duplicate claims,
  0 contradictions, 0 collisions with the open L0 lines it read. (Its report labels the new row
  S393; the registry's actual id is S392 at `corpus/SOURCES.md:403`. Its sweep counts stand.)

## Prefile falsification gate

```
$ python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane tsukuroi --round 97
PREFILE-FALSIFICATION: pass claims=2 rows=16 attack_seats=5 findings=0
exit 0
```

Ledger: `.ufo/waves/round-97/claim-falsification.tsv` (16 rows; 5 `falsifies-wording`, 11
`neutral`). Narrowing pointers: A3/A6/A7 ×2 in `before/plan-amendments-r97.md` for C1, A4 for C2.

## Round shape, dead seats, L0

One v1 wave of 14 seats (validator `counts` 14/0/14, `w1-validate.err` 0 bytes), attack share 36 %,
1 connector seat, 0 dead seats, no residual call. Open L0 questions: none added by this lane.
