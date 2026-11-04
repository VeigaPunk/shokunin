# kaidoku round 74 — report

Lane: kaidoku-shokunin · round 74, attempt 1 · base `04fdc2c4dbedbe5ee50a069af14310068393233e`
· lane tip `fb8229de9a92b8b97ae8cab1130d05e91fed84ff` (pushed; `git ls-remote origin
refs/heads/main` prints it).

**Declared claims (frozen in `plans/round-74-claims.md` and `.ufo/waves/round-74/claims.json`;
freeze `021914c0`):** R74-C1 on **operability** — a probe-mutation closure that kills the six A12
selftest survivors round 73's MutProbe reported, each by a declared case; R74-C2 on
**calibration** — a sixteen-atom record audit that binds the round-73 non-author routed-defect
set, the before-arm selection, the capability table, the registry's rejected rows, the census
erratum, the runner binding and the freeze pins. `lowest-axis: calibration` (tied-lowest axis,
no nudge waiver claimed).

## Work performed

- **Frozen instruments built before data.** `tools/round-74/seam-probe.py` (A1–A12 retained;
  `kernel_witness` takes injectable `/proc` readers and a pid list with one deterministic pass,
  `forged_subrun` takes its spawner and witness, `assemble_arm` is the genuine→forged→verdict
  wiring; six new selftest cases, 20 total), `tools/round-74/probe-mutation.py` (ten defect
  classes per patch set, exact-once anchors, declared-case kills, wrong-case refusal, printed
  target pin), `tools/round-74/record-audit.py` (16 atoms, `--validate`, 12 parser selftest
  cases), `tools/round-74/freeze-pins.py`, `tools/round-74/controls.py`. Declaration
  `b3a7e280`; freeze `021914c0` audits **CLEAN** (planned item (d)) —
  `.ufo/waves/round-74/l1/scores/gate-at-record.json`.
- **R74-C1 measured.** `r73probe` on the landed round-73 probe: four killed, the six MutProbe
  survivors survive (`pre/c1-base-arm.json`, rev `b3a7e280`). `r74probe` at the record revision:
  ten mutants, **0 survivors**, each killed by its declared case, pristine 20 cases green,
  target pinned `81d6a432…` (`l1/scores/c1-at-landing.json`, rev `5cea760e`; repeat at the tip
  `l1/scores/c1-at-tip.json`, rev `9aa0f18f`).
- **R74-C2 measured.** 11 mismatches at base naming `D3, D6, D7b, D8, D9, D10, D11, D12, D13,
  D14, D15` (`pre/c2-at-base.json`, rev `04fdc2c4`) → **0 over 16 atoms** at the record revision
  (`l1/scores/c2-at-landing.json`, rev `5cea760e`), `--validate` clean; also 0 at the tip
  (`l1/scores/c2-at-tip.json`, rev `9aa0f18f`).
- **Runtime preservation.** The refactored probe re-runs A1–A12 at the record revision: 12/12
  with `A12_kernel_witness` true (`l1/scores/c1-runtime-at-landing.json`).
- **Controls.** Four arms met (`l1/scores/controls-at-landing.json`): base world six survivors;
  renamed cases scored `killed_wrong_case` with no kill; base audit with every new atom false;
  the audit's red parser cases present and passing.
- **Round shape.** One v1 wave `r74-w1`, 15 seats in one batched call: 5 executor, 3 scribe, 2
  reviewer, 1 critic, 1 mutation-tester, 1 sentinel, 1 scout, 1 connector; attack roles
  (reviewer/critic/mutation-tester) 4/15 = 27%; one connector; no residual call; **0 dead
  seats** (15/15 settled, non-empty outputs, `.ufo/waves/round-74/r74-w1-results.json`). The L1
  held the planner seat. Round total 15.
- **Wave findings that bound the claims** (all in `.ufo/waves/round-74/w1/*.md`): ExecProbeCases
  reproduced five one-case bindings and one cross-binding (the canary-field mutant also fails
  `a12-kernel-multiple-samples`); CriticClaims found three further A12 survivors outside the
  frozen ten classes and four cosmetic-passes for D9–D12; MutationTester found D8/D11/D14 atom
  mutants surviving both the base receipt and the parser selftest (the atoms have no red-arm
  coverage); ExecAuditRun named D14's receipt substitution and D15's coverage limit;
  SentinelScope routed four code items and one carried item; ScoutSource verified S278 and
  identified the D11 token as a round-73 label rather than an opened URL (the row registers
  `dir_section_5.html` and says so); ExecRepairs/ScribeRows/ScribeLesson wrote the record
  repairs, the registry rows and the lesson.
- **Honest bounds on the claim verdicts.** C1's predicate is bounded to the frozen ten classes;
  it does not claim saturation (three further survivors are named debt). C2's zero is a
  presence/pointer check per atom, not a semantic repair: the four cosmetic counterexamples are
  recorded debt, and D11 is satisfied by a label string the row explicitly marks as not an
  opened URL.

## Landed changes

| change | commit | record |
|---|---|---|
| five round-74 instruments, the plan, the census-start receipt | `541d574e` | LOG round-74 entry; `plans/round-74-claims.md` |
| pre-freeze instrument revision (receipts bind their runners; selftest case names) | `b3a7e280` | LOG round-74 entry |
| freeze container, pre receipts, pin check | `021914c0` | `SCORECARD.md` round-74 section; `corpus/claim-freezes-v2.tsv` |
| wave evidence: spec, dispatch, ready | `5ba6a218` | LOG round-74 entry |
| record repairs: 3 r73 + 2 r74 capability rows, the R73-C1 before-arm selection block, S275 used-by, S278 + four rejected rows, round-73/74 search-log notes, README newline, PROVINCE Core additions, the entry, the lesson, the wave reports | `3c2dae33` | `SCORECARD.md`, `corpus/SOURCES.md`, `corpus/README.md`, `PROVINCE.md`, `corpus/knowledge/2026-11-04-r74-probe-mutation-closure.md`, `corpus/lessons/round-74.md` |
| freeze ledger row: `round-74 CLEAN -` | `5cea760e` | `corpus/claim-freezes-v2.tsv` |
| landing receipts: both claims, the runtime arms, the gate, the controls, the census end | `9aa0f18f` | `.ufo/waves/round-74/l1/scores/` |
| post-report corrections and the tip receipts | `fee4c2b9` | `.ufo/waves/round-74/w1/ScoutSource.md`, `ScribeRows.md`, `l1/scores/c1-at-tip.json`, `c2-at-tip.json` |
| the lesson's wave synthesis and planned debt | `37194e3e` | `corpus/lessons/round-74.md` |
| the wave results and the handoff marker | `fb8229de` | `.ufo/waves/round-74/r74-w1-results.json` |

No axis other than the two claimed ones moved; the record edits are appends (the filed round-73
claim rows are untouched; the selection block supplements them).

## Before → after measurements

**R74-C1 — operability (probe-mutation closure).** Counter: `survivor_count`.

```
python3 -I -B tools/round-74/probe-mutation.py --root . --rev <rev> \
  --tool tools/round-74/seam-probe.py --patch-set r74probe --work <scratch> \
  --expect-survivors 0 --expect-target-sha256 <blob at rev> --json-out <receipt>
python3 -I -B tools/round-74/probe-mutation.py --root . --rev <rev> \
  --tool tools/round-73/seam-probe.py --patch-set r73probe --work <scratch> \
  --expect-survivors 6 --json-out <receipt>
```

before 6 (`a-drop-genuine-canary, b-unreadable-empty, b-first-sample-only, b-drop-canary-field,
c-swap-verdict-inputs, c-skip-forged-subrun`) → after **0**; measured against `b3a7e280`
(`pre/c1-base-arm.json`, `pre/c1-post-at-declaration.json`), `5cea760e`
(`l1/scores/c1-at-landing.json`, `c1-base-arm-at-landing.json`) and `9aa0f18f`
(`l1/scores/c1-at-tip.json`). Each of the ten kills names its declared case; pristine 20 cases
green both sides.

**R74-C2 — calibration (record audit v2).** Counter: `mismatch_count`.

```
python3 -I -B tools/round-74/record-audit.py --root . --rev <rev> --json-out <receipt>
```

before 11 → after **0** over 16 atoms; measured against `04fdc2c4`
(`pre/c2-at-base.json`), `5cea760e` (`l1/scores/c2-at-landing.json`) and `9aa0f18f`
(`l1/scores/c2-at-tip.json`); `--validate` reports no defect on the landing receipt.

**Runtime arms (corroboration, not a claim).** `python3 -I -B tools/round-74/seam-probe.py
--root . --rev 5cea760e --tool tools/round-73/packed-elf.py --battery
tools/round-73/mutation-check.py --pkg <REA 6.5.0> --work <scratch> --receipt
.ufo/waves/round-73/pre/route-at-declaration.json --receipt-rev d36c6ee0 --expect-upx
/fast/scratch/hyaku/kaidoku-r73/l1/upx-r73 --nonce-commitment <commitment>` → `arms_passed 12`
of `target 12`, `A12_kernel_witness` true (`l1/scores/c1-runtime-at-landing.json`).

## Sources & frontier

- **Census before → after.** `scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kaidoku`: start exit **0**, 184 rows
  (`.ufo/waves/round-74/l1/census-start.txt`, 23 W04 lines); end exit **0**, **189 rows**
  (`.ufo/waves/round-74/l1/census-end.txt`, 23 W04 lines). Rows before 184 → after 189.
- **Rows added by tier:** one tier-A mined row (S278), four tier-A rejected rows (S279–S282).
  **Rows touched old→new:** S275 `used-by` gained
  `corpus/knowledge/2026-11-04-r73-kernel-witness-record.md` (old value recorded verbatim in
  `w1/ScribeRows.md`); S282's source cell records the round-73 label `index.html#_section_5` as
  a label, not an opened URL, and cites `dir_section_5.html` as the page opened.
- **Frontier rows advanced:** the kernel-side witness's selftest closure (the six conjunct
  cases) moves into Core for `tools/round-74/seam-probe.py` (`PROVINCE.md ## Round-74 additions
  to Core`); still Frontier: a wrapper that never runs a sampled process, `PR_SET_MM_ENV_START`
  relocation, non-Linux substrates, signed receipts.
- **Sourced claim.** R74-C1's `a12-proc-environ-unreadable` case rests on **S278**
  (`ptrace(2)`'s `PTRACE_MODE_READ_FSCREDS`, opened this round: HTTP 200, 104 833 B, sha256
  `69cd309e…`, 15-word located quote at "Ptrace access mode checking"), cited through
  `corpus/knowledge/2026-11-04-r74-probe-mutation-closure.md`.
- **Mistake mined.** `corpus/lessons/round-74.md ## Mistakes`: a record value written from a
  plan rather than from bytes (round 73's 11-vs-8 comparator and its two wrong producer pins),
  captured by the pre-freeze pin procedure and D7b, fixed by computing pins from the blobs and
  appending a selection block.
- **Assimilation:** none — `merge/kaidoku/` does not serve these claims and `considerthese/` is
  absent in this lane.

## Trend verdicts

- **expansion: improved.** The registry gained five rows on ground the lane did not hold (the
  `PTRACE_MODE_READ_FSCREDS` read gate plus four registered rejections), and `PROVINCE.md`
  moves the selftest case closure into Core for the measured probe.
- **quality: improved.** The six A12 survivors are closed by declared cases and the runtime
  arms reproduce 12/12; the record repairs are mechanical and audited. Bounded honesty: three
  further A12 survivors, three atom mutants and four cosmetic atom passes are named debt, not
  smoothed.
- **discernment: improved.** The wave falsified parts of both claims' instruments
  (case cross-binding, atom shallow tokens, control laxness), the scout caught a label presented
  as an anchor, and every finding is routed with the case or predicate it needs next round; no
  frozen rule was edited after scoring.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SKILL.md` decision/error tables plus the round-74 registry rows and S278/S275/S277 citations.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the A1–A12 run at
  `5cea760e` (12/12) is logged in `LOG.md`'s round-74 entry with its receipt.
- [~] Instructions executable by an agent without oral context — `plans/round-74-claims.md` plus
  the frozen instruments; ExecBattery/ExecProbeCases re-ran the predicates from the text alone.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` round-74 additions;
  `w1/ConnectorCross.md` names the sibling owners and absorbs nothing.

## Extras

- **Stale-lane:** none — respawn-per-round driver; this is the lane's only open mission.
- **Tool installs:** none; no pacman transaction ran (host-wide pause respected).
- **Open L0 questions:** none filed; no operator decision was needed.
- **Scratch:** `/fast/scratch/hyaku/kaidoku-r74` removed after the close; the r73 receipt path
  recreated for the runtime arm was left to the reaper.

Report: .ufo/reports/round-74/kaidoku.md
