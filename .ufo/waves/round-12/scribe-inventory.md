# scribe-inventory — round-12 artifact inventory + `.ufo/reports/round-12/protocol.md` skeleton

Seat `ScribeReport` (L2 wave 2, protocol lane), 2026-09-28 21:06–21:17 -03:00, cwd `/home/vgpnk/projects/shokunin`. Read-only git; exactly one file written (this one) — no `git commit`/`add`/`push`/`restore`/`checkout`, no tree mutation by this seat.

**Method.** Five samples — T1 21:06, T2 21:09, T3 21:13, T4 21:14, T5 21:16 — each `sha256sum <f> | cut -c1-16`, `stat -c %s <f>`, `wc -l <f>`, `git ls-files --error-unmatch <f>` (`T` = tracked, `U` = untracked); rows are the T5 sample unless a row names another. **No status is assigned anywhere in this file**: each row is a measurement or an attributed quote, never an admission or an adjudication.

## Artifacts

### `.ufo/waves/round-12/` — seat artifacts, gate, frozen inputs (all `U`; the dir is untracked as a whole)

| path | sha256[:16] | bytes | lines | T/U |
|---|---|---|---|---|
| `closure-check.py` | `feede25dd5d10d1f` | 63358 | 1342 | U |
| `__pycache__/closure-check.cpython-314.pyc` | `6f5c08af50c576de` | 75387 | 307 | U |
| `mutation-gate.md` | `5f42716108517e32` | 5970 | 33 | U |
| `closure-semantics.md` | `a6075e5c42ba569a` | 12639 | 66 | U |
| `connector-overlap.md` | `ed86bc78384a7164` | 11350 | 42 | U |
| `critic-approach.md` | `bd730c187dced06d` | 12603 | 210 | U |
| `exec-gate-standard.md` | `c946543ab25bdd7f` | 13404 | 130 | U |
| `labrat.md` | `0e90b33b0b9de879` | 6283 | 85 | U |
| `reviewer.md` | `3d9046d3fb823f18` | 20838 | 97 | U |
| `scout-closure.md` | `12bacac6c846b99f` | 15925 | 94 | U |
| `scout-gates.md` | `1c0c1d59436d4548` | 13757 | 63 | U |
| `sentinel-trust.md` | `181b891327c914f8` | 13029 | 184 | U |
| `mutants/pristine.json` | `bf1ba57e6950b6f8` | 35253 | 44 | U |
| `frozen/README.md` + `frozen/patch-entries.json` | `bf10ba2bc1766177` / `0c77165e6d141067` | 2898 / 10482 | 46 / 145 | U |
| `frozen/{pre,post}/MANIFEST.json` | `f252447f5d094f78` / `bf1ba57e6950b6f8` | 25322 / 35253 | 38 / 44 | U |
| `frozen/{pre,post}/expected.json` | `a905c439eb199f79` / `e56b31bc84c0d4d0` | 2459 / 132 | 46 / 5 | U |
| `frozen/{pre,post}/CLOSED_AT.txt` | `011867777dc621f5` / `6072b8396ec8c5be` | 470 / 470 | 7 / 7 | U |
| `frozen/{pre,post}/{prompts-index.txt,reports-index.txt}` | `ee19f98f69d8a787` / `d878c6643b6370c3` (identical pre=post) | 2342 / 3498 | 74 / 81 | U |
| `frozen/{pre,post}/state-counters.txt` | `5f6279cafadebf10` (both) | 84 | 8 | U |
| `frozen/{pre,post}/watchdog.log` | `785956c1b57274e1` (both) | 13494 | 206 | U |

`fixtures/closure-sample/` — 43 files in 10 dirs; one row per dir, `name=sha16/bytesB` per file (dir collapsed from 43 rows to honour the ≤130-line contract):

| fixture dir | files (`name=sha16/bytes`) |
|---|---|
| `contradiction` | `.ufo/watchdog.log=522b1a306a93fe7b/110`, `MANIFEST.json=6520c70dcc6e1477/223`, `expected.json=c2e7c03f514144aa/95` |
| `failed` | `.ufo/state/kagi.round=4355a46b19d348dc/2`, `.ufo/watchdog.log=7e0a248693dbbc59/170`, `MANIFEST.json=ba45b8c4b2fc4a65/215`, `expected.json=d8e81999a5f5345e/95` |
| `in-flight-live` | `.ufo/prompts/kagi-round-1.md=64db9e73880d4c32/30`, `.ufo/state/kagi.round=4355a46b19d348dc/2`, `.ufo/watchdog.log=522b1a306a93fe7b/110`, `MANIFEST.json=352b866ccf7e5594/218`, `expected.json=d8e81999a5f5345e/95` |
| `in-flight-terminated` | `.ufo/state/kagi.round=53c234e5e8472b6a/2`, `.ufo/watchdog.log=7e0a248693dbbc59/170`, `MANIFEST.json=352b866ccf7e5594/218`, `expected.json=c2e7c03f514144aa/95` |
| `legacy-unadjudicable` | `.ufo/state/kagi.round=4355a46b19d348dc/2`, `.ufo/watchdog.log=7e0a248693dbbc59/170`, `MANIFEST.json=09d127da7994c424/123`, `expected.json=d8e81999a5f5345e/95` |
| `marker` | `.ufo/reports/round-1/kagi.md=f4578596f91d62f1/55`, `.ufo/state/kagi.round=4355a46b19d348dc/2`, `.ufo/watchdog.log=7e0a248693dbbc59/170`, `MANIFEST.json=ef69a7283db0c5ca/211`, `expected.json=c2e7c03f514144aa/95` |
| `not-dispatched-without-lane_rounds` | `.ufo/watchdog.log=ca353a435d847f46/33`, `MANIFEST.json=b1a052ea62197a49/183`, `expected.json=c2e7c03f514144aa/95` |
| `ok` | `.ufo/prompts/kagi-round-1.md=64db9e73880d4c32/30`, `.ufo/reports/round-1/kagi.md=3f5ba550e1030a0c/1276`, `.ufo/state/kagi.round=4355a46b19d348dc/2`, `.ufo/watchdog.log=365b32b036211e89/203`, `MANIFEST.json=ef69a7283db0c5ca/211`, `expected.json=d8e81999a5f5345e/95` |
| `prompt-orphan` | `.ufo/prompts/kagi-round-3.md=6af7cc64d9a2d944/54`, `.ufo/state/kagi.round=1121cfccd5913f0a/2`, `.ufo/watchdog.log=ca353a435d847f46/33`, `MANIFEST.json=d84c941faa4ad96b/90`, `expected.json=5a7e5ab6662f92d9/95` |
| `unrowed` | `.ufo/state/kasegi.round=f0b5c2c2211c8d67/2`, `.ufo/watchdog.log=c9f33bd77a20fedf/114`, `MANIFEST.json=d84c941faa4ad96b/90`, `expected.json=3d808421c91863dc/95` |

### Main-repo files touched by the round, and the report band

| path | sha256[:16] | bytes | lines | T/U |
|---|---|---|---|---|
| `PROTOCOL.md` | `4398c2c2f7efbd26` @T5 → `171e2335f67deaac` @T6 21:20:11 | 47874 → 48608 | 514 → 521 | T |
| `MANIFEST.json` | `bf1ba57e6950b6f8` @T5 → `507bffc2fd8c9105` @T6 21:20:11 | 35253 → 37932 | 44 → 46 | T |
| `.ufo/l0-questions.md` | `6ca2a358cbfcdfff` | 10223 | 11 | T (modified) |
| `.ufo/prompts/kasegi-round-15.md` | `c6c2b12939ad793e` | 1324 | 11 | T |
| `.ufo/prompts/kotoba-round-13.md` | `0584b2acbda26623` | 1321 | 11 | T |
| `.ufo/prompts/kumitate-round-12.md` | `c7925f17700335e6` | 1335 | 11 | T |
| `.ufo/prompts/protocol-round-12.md` | `6111880138f21072` | 1299 | 11 | T |
| `.ufo/prompts/kagi-round-13.md` | `20539d73ae8ee151` | 1316 | 11 | U |
| `.ufo/prompts/kotoba-round-14.md` | `afd3d63d26c6ba5f` | 1321 | 11 | U |
| `.ufo/prompts/aggregator-round-9.md` | `23b16065310c9195` | 1307 | 11 | U |
| `.ufo/reports/round-7/aggregator.md` | `6d7728c32703b6ef` | 10695 | 121 | T |
| `.ufo/reports/round-11/protocol.md` | `44a80d5293726c77` | 29338 | 382 | T |
| `.ufo/reports/round-11/kagi.md` | `3e31c4e98d23c657` | 10163 | 164 | T |
| `.ufo/reports/round-11/kake.md` | `faf9ceb446b93e3b` | 5504 | 96 | T |
| `.ufo/reports/round-11/kasegi.md` | `66b8943e5bc57b8b` | 2992 | 51 | T |
| `.ufo/reports/round-12/kagi.md` | `9ecd9b5a3fa40c4d` | 13620 | 220 | U |
| `.ufo/reports/round-12/kotoba.md` | `490552ab73d4800d` | 14009 | 224 | U |
| `.ufo/reports/round-12/kake.md` | `9c281c995dbed480` | 15348 | 245 | T |
| `.ufo/reports/round-12/kasegi.md` | `b6fe4ebb820e800b` | 7287 | 116 | T |
| `.ufo/reports/round-13/kake.md` | `60d51a2f31ae8647` | 5878 | 102 | T (modified) |
| `.ufo/reports/round-13/kasegi.md` | `01d26a97502c7092` | 9964 | 158 | T |
| `.ufo/reports/round-14/kasegi.md` | `5748f6fa791bafc3` | 7338 | 127 | T |
| `.ufo/reports/round-11/kengaku-DRAFT.md` → `round-11/kengaku.md` | `cd96a7c97f7220a5` / `214934b2c44bc0ee` | 15922 → 18585 | 144 → 106 | U → T |
| full graded set, 81 rows (incl. the DRAFT row above) | `d878c6643b6370c3` | 3498 | 81 | U (`frozen/{pre,post}/reports-index.txt`, see Gaps) |

**Still moving during this inventory (two-pass, then five-pass, comparison).** Only `closure-check.py` changed bytes between T1 and T2; across all five samples it read `5e33707caa38cf4a` (60475 B, 1299 L) → `ae72d22ef8b5a228` (60846, 1304) → `d10dcd005a525864` (62819, 1335) → `923c2e6dfb95b82e` (63134, 1340) → `feede25dd5d10d1f` (63358, 1342). Every other non-fixture path was byte-identical T1→T5 except the cases below; `frozen/**` and `fixtures/**` bytes were identical at every sample. `MANIFEST.json` was caught mid-mutation at T3: `956990bdf72881d7`, 39649 B, 693 lines — while `jq '.' MANIFEST.json | wc -lc` prints `693 39656`, i.e. a jq-pretty-printed manifest 7 bytes shorter than the committed one; `.ufo/waves/round-12/mutation-gate.md:26` documents mutant m5 as exactly `in-flight`→`ok` (7 bytes) [INFERENCE: shape+delta match]. Files that *appeared* mid-inventory: `mutants/pristine.json` (mtime 21:12:09), `mutation-gate.md`, `frozen/README.md`, `.ufo/prompts/kotoba-round-14.md`, `.ufo/prompts/aggregator-round-9.md`. Files that *changed ownership state* at 21:11:43: `PROTOCOL.md`, `MANIFEST.json` and the four named prompts went uncommitted → committed (`7c56d1e`, `dddb4ec`, both `protocol-shokunin protocol@shokunin.local`); at T6 21:20:11 both moved again — `PROTOCOL.md` = `171e2335f67deaac` (48608 B, 521 L, mtime 21:18:45), `MANIFEST.json` = `507bffc2fd8c9105` (37932 B, 46 L, mtime 21:15:36) — so every main-repo value here is labelled with its instant rather than chased. The prompt set is as of T6 21:20:11 (7 rows: `kasegi-round-15`/`kotoba-round-13`/`kumitate-round-12`/`protocol-round-12` committed, `kagi-round-13`/`kotoba-round-14`/`aggregator-round-9` untracked, mtimes 21:06:05–21:14:11). **Resolution of the DRAFT row:** `.ufo/reports/round-11/kengaku-DRAFT.md` was present at T5 and gone at T5+1 because its owner promoted it — the live kengaku r11 lane committed its child work as `f09ff1f` under `kengaku-shokunin` identity at 21:15:23 (`git -C kengaku-shokunin log -1`: `f09ff1f kengaku-shokunin 2026-09-28T21:15:23-03:00 round-11`) and the DRAFT was replaced at 21:17:49 by a conforming `.ufo/reports/round-11/kengaku.md` (18585 B); that file is **tracked**, added by main-repo commit `e0170cd Joao Pedro Veiga <jpveigao10@gmail.com> 2026-09-28T21:18:11-03:00 kengaku round-11 report` (operator identity, not lane identity).

## Dispatch digest

Round-12 L2 wave, from the artifacts on disk. "Outcome" = the artifact's own summary text, attributed; artefact existence measured at T5.

**Wave 1 (10 seats)**

| seat | role | artifact (bytes) | exists | outcome it reported |
|---|---|---|---|---|
| `ScoutClosure` | closure evidence sweep | `scout-closure.md` (15925) | yes | read-only lane-round band map; `§Required appends` (line 78) demands 5 `closure-correction` entries with `closed_at ≥ 20:45:10`, and `§Debt` (line 60) flags `rounds[19]`'s kagi note text as false vs `029c474` 20:09:05 |
| `ScoutGates` | sibling verdict-gate survey | `scout-gates.md` (13757) | yes | 9 concrete divergences in the 14 committed gates (`§Divergences` line 34), incl. kotoba's `3 = no baseline` self-disagreement (`--json` 0 vs text 3); `transcript-scan.sh` is the one gate with no in-repo baseline (`§Pinned-baseline status` line 48) |
| `ExecChecker` | closure gate author | `closure-check.py` (63358, moving) | yes | the executable closure gate + `fixtures/`, `frozen/`, `mutants/`; per `mutation-gate.md:31-33` its `--selftest` printed `closure-check: ok selftest passed=10/10 failed=0` exit 0, `--frozen pre` printed `closure-check: debt debt=5 …` exit 1, `--frozen post` printed `closure-check: ok debt=0 …` exit 0 (quoted, not re-run by me) |
| `ExecGateStd` | §Gate standard draft | `exec-gate-standard.md` (13404) | yes | candidate §Gate standard text; `§Enforcement at closure — measured` (line 72): all five hermetic self-tests pass as a non-owner from the main repo in ≈8.4 s, and kengaku's gate reads `n=280 mismatches=1 FAIL` on the worktree vs `n=149 mismatches=0 PASS` over cited commit `06cdc98` |
| `RevengerSem` | recovered closure semantics | `closure-semantics.md` (12639) | yes | rounds 10/11 reconstructed as 15 checker acceptance criteria (`§Semantics spec` line 26), each with an on-disk example and a `PROTOCOL.md`/report pointer |
| `CriticApproach` | plan falsifier | `critic-approach.md` (12603) | yes | `§Must-fix` (line 8) MF-1: the obvious checker is "confidently wrong 15 ways", prototyped inline; **durability**: this seat first returned its critique without writing the file (header line 3-6 records "No sibling drafts existed: `ls .ufo/waves/round-12/` → empty … commands + observed outputs inline") and had to be asked to persist it — an inline-only delivery is not reachable by the integrator or by a later round |
| `ConnectorOverlap` | cross-lane scope map | `connector-overlap.md` (11350) | yes | `§Contested scope` (line 12) six ownership bullets (gate contract, registry, `round-gate.mjs` vs `report_of()`, `fleets/registry.json`, kake probes, UFO runtime) + `§Synthesis` (line 25) proposing `0`/`1`/`2` |
| `ReviewerStep1` | independent step-1 verification | `reviewer.md` (20838) | yes | per-report hash/ancestry/ordering verification + `§Status recommendations` (line 74) table over round-11/12/13 lane-rounds; `§Stale-lane actuator re-verification` (line 57) at 20:40 |
| `SentinelTrust` | trust-boundary analysis | `sentinel-trust.md` (13029) | yes | `§Spoofable inputs` (line 10) 4 classes, `§Durability-commit hazards` (line 45), `§Secret screen` (line 86), `§Gate-standard abuse` (line 102), and 6 `§Mitigations` (line 142) |
| `LabratLiveness` | read-only falsification probes | `labrat.md` (6283) | yes | `§Verdicts` (line 75): H1 `confirmed` — all 4 post-20:10 completed runIds still MATCH the driver's own live grep, so `in-flight` stays an absence test; H2 `confirmed (no termination)` — no `complete .*round=14` line, `rounds[14]` absent at probe time |

**Wave 2 (4 seats)**

| seat | role | artifact (bytes) | exists | outcome it reported |
|---|---|---|---|---|
| `CriticCandidate`, `ReviewerCitations` | candidate critique; citation verification | expected `critic-candidate.md` / `reviewer-citations.md` | **no** | no artifact on disk at T5 for either; the roster shows both seats running — nothing to transcribe |
| `MutationGate` | mutation testing of the closure gate | `mutation-gate.md` (5970) + `mutants/pristine.json` (35253) | yes | 7 mutants run with `--no-citations`; `§Verdict` (line 27): 4 of 5 determinate mutants killed (m2, m5, m6, m7 = **80%**), m1/m4 survived, m3 inconclusive because the gate raised `KeyError: 'protocol'`; `§Method` (line 3) records the gate-script hashes it observed (`d10dcd005a525864…` for m1-4, `4f53fcc0…` for m5-7) so the concurrent edits are visible |
| `ScribeReport` | this seat | `scribe-inventory.md` | yes (this file) | artifact inventory + dispatch digest + report skeleton; no status assigned |

## Report skeleton

Section list for `.ufo/reports/round-12/protocol.md` — one line each; prose is not drafted here. Contract: `PROTOCOL.md:112-125` (report path `.ufo/reports/round-<N>/<id>.md`, minimum content) and `PROTOCOL.md:168-182` (integrator duties; closure record).

| section | what goes in it | source artifact(s) |
|---|---|---|
| `## Work performed` | the round-12 axis-move as trigger → action → outcome → pointer, with paths/commands/diffs | `PROTOCOL.md:117`; gate text `dddb4ec`; `closure-check.py` + `frozen/`; the 10 wave-1 seat files |
| `## Changes landed` | every landed change tied to its `LOG.md` entry | `PROTOCOL.md:118`; `dddb4ec`, `7c56d1e`; `LOG.md`; `.ufo/l0-questions.md` commit |
| `## Cross-domain evidence` | evidence about other domains, each named with its owning domain | `PROTOCOL.md:119`; `scout-gates.md`, `connector-overlap.md`, `sentinel-trust.md` |
| `## SHONEN` | one line per box — `[x] <verifier-id>` / `[ ]` / `[~]` + resolvable pointer; main-repo lanes assess against the four `SHONEN.md` boxes | `PROTOCOL.md:120-125`; seed `PROTOCOL.md:386-396` (SKILL.md decision tables / end-to-end task in LOG.md / executable without oral context / no cross-domain bleed) |
| `## Closure record` | statuses written this pass, or why none was writable — the record is a gate, not prose | `PROTOCOL.md:176-182`; `MANIFEST.json` `rounds[22..27]`; `closure-check.py --frozen pre` / `--frozen post` |
| `## Stale-lane listing` | every mission open > 2 driver ticks (age from launch ts) graded *progressing* / *silent*, with the sibling-attribution limit | `PROTOCOL.md:130-146`; `reviewer.md §Stale-lane actuator re-verification`; `labrat.md`; `frozen/pre/state-counters.txt` |
| `## Routing` | one routed-defect line per defect, **including defects a lane owes its own repo** | `PROTOCOL.md:202-204` (step 2); `sentinel-trust.md §Mitigations`, `scout-gates.md §Divergences`, `mutation-gate.md §Gaps`, `exec-gate-standard.md §Rejection alternative` |
| `## Contested-scope rulings` | the arbitrator's ruling for each contested scope, recorded in the round notes | `PROTOCOL.md:404-408`; `connector-overlap.md §Contested scope` + `§Synthesis` |
| `## L0 side channel` | the L0 entries this round files or answers (append-only; the integrator owns durability) | `PROTOCOL.md:465-473`; `.ufo/l0-questions.md` (11 rows); the §Gate standard ruling of rows `kengaku\|round-10` and `kumitate\|round-10` |

## Gaps

- **43 fixture files are collapsed to 10 dir rows** (per-file `sha16`+bytes kept inline) to respect the ≤130-line output contract; no bytes were measured for the fixture trees' mtimes, only content hashes.
- **Two seats have no outcome to transcribe**: `CriticCandidate` and `ReviewerCitations` had no artifact at T5 and both are still running, so no evidence exists for a digest line beyond their absence. `ExecChecker`'s delivery is a moving script, not a seat file, and its frozen verdicts are quoted from `mutation-gate.md`, **not re-run by me** — I read `feede25dd5d10d1f` (63358 B) and any later patch is unmeasured.
- **`.ufo/reports/round-11/kengaku-DRAFT.md` (RESOLVED, not lost).** Absent at T5+1 is explained by owner promotion, not deletion: the live kengaku r11 lane committed child work `f09ff1f` under `kengaku-shokunin` identity at 21:15:23 and the non-contract DRAFT was replaced at 21:17:49 by `.ufo/reports/round-11/kengaku.md` (18585 B, `214934b2c44bc0ee`); that path is inside the lane's own write scope, so no other seat's act reaches it. Ledger consequence is Main's ruling, not mine (I assign no status): entry #24's kengaku r11 `in-flight` row **stands**, and `PROTOCOL.md` now pins that `in-flight` ends only on a complete line, the counter passing N, or a *landed* report at the contract path. **CONFLICTS_RELAY (verbatim, unresolved):** Main's message states "the new `kengaku.md` is still untracked and the mission is still live (no `complete kengaku round=11` line, counter 11)"; my measurement agrees on liveness (`grep -c 'complete kengaku round=11' .ufo/watchdog.log` → `0`, `.ufo/state/kengaku.round` → `11`) but not on tracking: `git ls-files --error-unmatch .ufo/reports/round-11/kengaku.md` succeeds and `git status --porcelain` on it is empty — committed `e0170cd` (operator identity, 21:18:11), i.e. landed by the operator, not by the lane.
- **The frozen index listing the DRAFT is correct, not stale.** `frozen/{pre,post}/reports-index.txt:17` records `.ufo/reports/round-11/kengaku-DRAFT.md` with tracked=`0` because that is what existed at `closed_at` 20:55:00: a frozen snapshot is a pinned past, not a live mirror, so it must keep naming the path its checks ran against.
- **The brief's line numbers for the candidate do not match the measured `PROTOCOL.md`** (`4398c2c2f7efbd26` @T5, 514 lines): `## Gate standard` is at `339-373`, not `319-352`; the §Appendix r12-tagged rows are `508-514`, not `447-452`+`512-514` (`awk 'NR>=440 && NR<=520 && /^\|/'` shows table rows only from 495). Net drift after T5 is measured, not reconciled: `171e2335f67deaac` @T6 = 521 lines.
- **Two measurement limits.** (a) The 81-row "graded report" set is pinned by one hash per snapshot (`d878c6643b6370c3`, identical pre and post) rather than 81 individual measurements; I hashed the 12 band reports above plus the DRAFT-row path, so 69 index rows are unhashed here. (b) `MANIFEST.json` has two observed byte-states in one session (T3 mutant jq-print vs T1/T5 `bf1ba57e6950b6f8`); the T3 state is explained by MutationGate's documented restore loop but the specific mutant is `[INFERENCE]` from a 7-byte delta, not reproduced (I re-ran no mutant).