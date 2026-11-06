# kaidoku — round 100 report (attempt 1, L1 KaidokuR100)

Lane `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, branch `main`. Base `6371c88633f6ce6692eaeff17e256b80ad21ece0` → final `7aeba805f43061a274e9bedfbdf2b625b97ebb77`. `git ls-remote origin refs/heads/main` prints `7aeba805f43061a274e9bedfbdf2b625b97ebb77`.

## Work performed

Two claims were declared and frozen at `8e24c29a37ca81a0bd1ff5ec73c96a949885322e` (`plans/round-100-claims.md`). Both counters, the red fixtures and the C2 do-nothing and forgery controls were committed there. The C1 controls were scored at the freeze before the candidate was committed.

- **R100-C1: coverage, frontier → core, also a capability; the sourced claim.**
  - A UPX 5.2.0 PE pack whose compressed data was altered without changing its length is now refused `checksum`. The rule is the packer's own Adler-32 `c_adler` test, from S327 `src/packhead.cpp` `ph_decompress` (lines 334-338), opened this round.
  - Before, the round-99 repair answered `ok intact` with exit 0 on these packs.
  - The battery also gains a process-level `exec` guard. It answers the round-99 limit that an aliased `os` call evades the text screen.
- **R100-C2: calibration.** The SKILL.md registry self-test case counts were checked against what the tools actually print. Mismatches went from 7 to 0 across the 93 rows that state a count. This answers the round-99 named limit 1 (presence and shape, not truth).
- **Lowest axis:** every owned axis was recorded at 10.0, a tie. A capability entered at round 99, so the stagnation nudge does not waive the lowest-axis duty. C2 works calibration, because the base measurement showed seven false registry counts, which contradicts the recorded 10.0.

Work items:
- **Pre-freeze survey** of the 93 count-bearing registry rows at base, run in a scratch archive and clone.
  - The first counter draft misread a date (`2026-10-28 cases=12` read as 28) and a flag argument as counts.
  - This was fixed before the freeze and pinned by selftest cases (M100-a).
- **Frozen counters:**
  - `tools/round-100/pe-upx-corrupt-battery.py`: the round-99 arms plus `corrupt` (40 cells) and `exec` (strace).
  - `tools/round-100/registry-selftest-truth.py`: 93 rows with tool sha256 pins and their documented self-test argv; selftest 22 cases, `.ufo/waves/round-100/pre/c2-selftest.txt`.
- **Red fixtures and controls:**
  - C1: `tools/round-100/gen-forgeries.py` and `tools/round-100/forgeries/h0…h6`.
  - C2: forgery fixture bytes `.ufo/waves/round-100/pre/forgery/` (F-drop, F-tool, F-dup), committed as bytes rather than diffs (M99-j).
- **C1 candidate:** `tools/round-100/upx-pe-repair.py`, landed at `a610671d7a01e1d762eb7103e6ee9f8a2be287ed`.
- **C2 landing:** seven registry rows corrected to the counts the tools print, at `cbd224ef9b9d2271f415d823bdc4d1e70a0d281c`. Each corrected row keeps its old figure as "this cell said …".
- **Knowledge landing** `b0a7bb8ca5ef66d459d786b9d2705c7fd866d502`:
  - entry `corpus/knowledge/2026-11-05-r100-pe-upx-payload-checksum-refusal.md`;
  - S327, plus the S324/S326 `used-by` widening;
  - README coverage-map, index and Round-100 frontier note;
  - capability row; QUALITY rows 202 and 203;
  - coverage head 184/184, now also stating recipe A (closure defect 5);
  - four round-100 registry rows with full sha256 (QUALITY 201).
- **Integration 1** `a9bc193cea972c51daa01420d8aa86b4014e0369`:
  - S328 (`src/check/dt_check.cpp`, the Adler-32 self-test constants) added;
  - round-99 and round-100 search-log notes (closure defect 1);
  - the entry rebuilt from ScribeEntry's draft (carrier table, not-examined section, the 20/20 `upx -t` message split);
  - pointers appended to the r98/r99 entries, and a PROVINCE round-98–100 PE section (ConnectorOverlap F4–F8);
  - registry exit 1 added for the repair (F11);
  - `corpus/lessons/round-100.md`.
- **Integration 2** `9a054c17998e089ff534711042f63b31baa6e118`: wave evidence (14 reports in `.ufo/waves/round-100/w1/`), the lesson's wave results and named limits, the SCORECARD round-100 section and the LOG entry.
- **Final commit** `7aeba805f43061a274e9bedfbdf2b625b97ebb77`: receipts at `9a054c17`, census-end, `r100-w1-results.json`.

## Landed changes

| commit (`landed` line of `jj-lane.sh`) | content | LOG.md entry |
|---|---|---|
| `8e24c29a37ca81a0bd1ff5ec73c96a949885322e` | freeze: plan, both counters, generator, h0–h6, C2 controls and fixture bytes, S327 copy, census-start | `LOG.md` `## 2026-11-05 — round 100` (Declaration and landing) |
| `b3f41553e201e0e5ea76dd9e5b90285a97069a5b` | C1 controls scored at the freeze (round-99 repair + h0–h6, all exit 1) | same entry (Before → after R100-C1) |
| `a610671d7a01e1d762eb7103e6ee9f8a2be287ed` | C1 candidate | same entry |
| `cbd224ef9b9d2271f415d823bdc4d1e70a0d281c` | C2: seven registry rows corrected | same entry (Before → after R100-C2) |
| `b0a7bb8ca5ef66d459d786b9d2705c7fd866d502` | C1 knowledge, S327, README, capability, head, QUALITY 202–203, registry rows, landing receipts | same entry (Sources, Capability, Housekeeping) |
| `a9bc193cea972c51daa01420d8aa86b4014e0369` | integration 1 (S328, search log, entry from wave, pointers, PROVINCE, lesson) | same entry (Wave, Mistakes) |
| `9a054c17998e089ff534711042f63b31baa6e118` | integration 2 (wave evidence, lesson results, SCORECARD section, LOG) | same entry |
| `7aeba805f43061a274e9bedfbdf2b625b97ebb77` | final receipts, census-end, wave results | same entry |

## Before → after measurements

### R100-C1

- **Command:** `python3 -I -B tools/round-100/pe-upx-corrupt-battery.py --root . --repair tools/round-100/upx-pe-repair.py --rev <rev> --work <scratch> --json-out <receipt>`.
- **Before:** controls at the freeze `8e24c29a`, all exit 1 (`.ufo/waves/round-100/pre/c1-controls-at-freeze.txt`):
  - round-99 repair: `corrupt 0 of 40`, all other arms full;
  - h0 identity;
  - h1 refuse-all;
  - h2 off-by-header;
  - h3 `u_adler`;
  - h4 aliased-`os` oracle: `corrupt 20 of 40; exec 0 of 1`;
  - h5 length-only: `corrupt 0`;
  - h6 the candidate plus one aliased exec: only `exec 0 of 1`.
- **After:** `recovered 30 of 30; decoy 9 of 9; intact 10 of 10; overlay 20 of 20; truncated 40 of 40; corrupt 40 of 40; refused 2 of 2; cli 3 of 3; static 1 of 1; exec 1 of 1; effective 119 of 119`, exit 0, at `a610671d`, `b0a7bb8c` and `9a054c17` (`.ufo/waves/round-100/l1/scores/c1-at-*.json`).
- **Verdict: met on the frozen predicate, with named limits.** The counter witnesses refusal behaviour, not the rule. Two wave forgeries also meet the full label with exit 0:
  - CriticC1's pristine-cache forgery (UPX packing is deterministic);
  - ReviewerCounter F6's filename-keyed forgery.
  - MutationC1 found that the repair's compressed-data bound branch is never reached by the battery.
- **Substance outside the predicate:**
  - ExecHeldOut ran nine further PE files packed `--best`, `--lzma` and `-1`: sound 45/45, complete 54/54, no over-refusal.
  - ExecReproC1 refused 50 of 50 flips at its own offsets.
  - ReviewerRepair approved the repair: packer-faithful, with the round-99 battery label unchanged.

### R100-C2

- **Command:** `python3 -I -B tools/round-100/registry-selftest-truth.py --root . --rev <rev> --work <scratch> --json-out <receipt>`.
- **Before:**
  - At base `6371c886`: `rows 93; claimed 93 of 93; green 93 of 93; counted 93 of 93; agree 86 of 93; mismatches 7`, exit 1 (`.ufo/waves/round-100/pre/c2-do-nothing-at-base.json`).
  - Forgery controls F-drop, F-tool and F-dup: each `mismatches 7`, exit 1 (`pre/c2-forgery-controls.txt`).
- **After:** `rows 93; claimed 93 of 93; green 93 of 93; counted 93 of 93; agree 93 of 93; mismatches 0`, exit 0, at `cbd224ef`, `b0a7bb8c` and `9a054c17` (`.ufo/waves/round-100/l1/scores/c2-at-*.json`).
- **Separability:** C2 is measured at `cbd224ef`, which changes only `SKILL.md`. C1's battery reads only the candidate bytes.
- **Verdict: met on the frozen predicate, with named limits.**
  - CriticC2 found seven edit classes outside the first stated count that pass (L1–L7).
  - MutationC2 killed 22 of 29 non-equivalent mutants through the frozen predicate and the other 7 by probe.
  - ExecReproC2 found five false or red rows outside the population (F1–F5); they are routed.

### Harm check

- Round-66 coverage self-check: head 10.0 at 183/183 true at base, and 10.0 at 184/184 true at `b0a7bb8c` and `9a054c17`.
- Recipe A: 142 of 184, 7.72, now stated in the head.
- Depth: `citation_resolved_rules 36` at both (`.ufo/waves/round-100/l1/scores/coverage-selfcheck-at-*.json`).
- Freshness was not re-measured, because the receipt corpus did not change.
- No earlier claim row was edited. No axis is harmed.

## Sources & frontier

- **Registry size:** SOURCES rows went from 231 to 233. Counting command: `grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md`, run at base and at the final commit.
- **Rows added by tier:** A 2, B 0, C 0.
  - S327: UPX 5.2.0 `src/packhead.cpp`, `mined`; located quote at lines 336-338.
  - S328: UPX 5.2.0 `src/check/dt_check.cpp`, `mined`; line 1154; the `zlib.adler32` cross-check is committed.
- **Rows touched (old → new):** `used-by` widened to add the r100 entry on S324 (`r98, r99` → `r98, r99, r100`) and on S326 (`r99` → `r99, r100`).
- **Rejections:** ten candidate files opened by ScoutSources were rejected as rows, recorded in the lesson Gate and the search log. The round-99 rejection was appended (closure defect 1).
- **Census:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`.
  - Start: exit 0, `kaidoku ok`, 33 W04 (`.ufo/waves/round-100/pre/census-start.txt`).
  - End: exit 0, `kaidoku ok`, 34 W04 (`.ufo/waves/round-100/l1/census-end.txt`).
  - The added W04 is S327, which shares S308's URL. This is a deliberate scope split: S308 covers the header checksum and S327 the compressed-data checksum.
  - This answers round-99 closure defect 2 with figures. The round-99 count was 32 → 33, not "already there".
- **Frontier advanced:**
  - The Round-100 note moves "payload corruption at intact length" to Core as a refusal for the ten pinned PE carriers.
  - PROVINCE gains a round-98–100 PE section.
  - Still Frontier: forged `c_adler` (`u_adler` needs the codec), header versions below 10, non-PE formats, Mach-O, and carriers outside the pinned set.
- **Mistake mined:** M100-b, seven stale registry counts, each written in rounds 46, 47, 71, 76 or 89, with three causes.
  - Fix: QUALITY 203 and the counter, shown able to fail (base exit 1; three forgery controls exit 1).
  - M100-a and M100-c through M100-g are also in `corpus/lessons/round-100.md` `## Mistakes`.
- **Assimilation: none.** `test -e /home/vgpnk/Projects/shokuknow/merge/kaidoku` → 0, but the claim cap was spent. `considerthese/` is absent (`test -e` → 1). No `corpus/lessons/operator-*.md` exists.
- **Round-99 spot-check:**
  - Defects 1, 2, 4 and 5 are done.
  - Defect 3: the landing receipts were committed with their citing commit.
  - Defect 6: carried limits are partly closed (process guard, mkstemp); the round-97 defects 2–5 and 7 remain open.

## Trend verdicts

- **expansion: improved.** Altered compressed data at intact length enters the coverage map, the entry, PROVINCE and the capabilities table, grounded by two new packer-source rows (S327, S328).
- **quality: improved.** The round-99 repair's exit-0 false green on corrupted payloads is closed and holds out of population (ExecHeldOut 54/54, 0 over-refusal). The battery's exec guard kills the aliased-`os` oracle class that the round-99 screen admitted (h4, h6).
- **discernment: improved.** The lane measured seven of its own false registry counts by running the tools, rather than by reading the rows. The wave named the forgeries that both new counters still admit, and they are recorded as named limits. No outside spot-check of this round exists yet.

## SHONEN

- [~] box 1 "SKILL.md contains real decision tables, error patterns, checklists, cited sources": the four round-100 registry rows and seven corrected rows (`SKILL.md` instrument registry); entry `corpus/knowledge/2026-11-05-r100-pe-upx-payload-checksum-refusal.md` (rule, measured table, carrier table, limits, S327/S328). Lane-asserted; no non-author verifier.
- [~] box 2 "At least one end-to-end domain task executed and logged in LOG.md": `LOG.md` `## 2026-11-05 — round 100`, End-to-end domain task (pack → corrupt, tamper, cut or overlay → repair or refuse → `upx -t`/`upx -d`; 99-cell held-out run). Lane-asserted.
- [~] box 3 "Instructions executable by an agent without oral context": ExecReproC1, ExecReproC2 and ScribeLesson re-ran both frozen commands from clean clones using the plan alone (`.ufo/waves/round-100/w1/ExecReproC*.md`). These are lane-dispatched seats, so they are not non-author.
- [~] box 4 "No cross-domain bleed (PROVINCE.md still accurate)": ConnectorOverlap found no sibling overlap (F1/F2) and stale PE wording in PROVINCE (F8). A round-98–100 PE section was added at `a9bc193c` (`PROVINCE.md` last section). Lane-asserted.

## Round shape and housekeeping

- **Round shape:** one v1 wave `r100-w1` of 14 seats, validated under `ufo-wave-policy.json` (band 8–16, `counts {spawn 14, resume 0, total 14}`), dispatched through the inline handoff (`r100-w1.ready`, `WAVE-DONE`, `r100-w1-results.json`).
  - Role mix: executor 3, scout 1, connector 1, scribe 2, reviewer 2, critic 2, mutation-tester 2, sentinel 1.
  - Attack share: 6/14 (43 %).
  - I held the planner seat myself, because the validator rejects `planner`.
  - No residual call. Round total: 14 seats.
- **Dead seats:** none. All 14 settled with reports.
- **Inherited state:** attempt 1. There is no `lane-dead-no-report kaidoku round=100` line, and the lane was clean at base.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists only `.scratch/run15-kernel.py`, `.scratch/run15-state.json` and `w4lines.txt`. These are pre-existing and not this lane's, so nothing was touched.
- **Disclosures:**
  - The C1 candidate was dry-run once in worktree mode before the freeze; this is disclosed in the plan.
  - The coverage head names its record receipt by pattern.
  - ExecReproC2 F4 found that two round-82 self-tests exit 1 silently. This is routed, not fixed.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none by the L1 or by any seat (per their reports). No pacman, sysctl or namespace change.
- **Scratch:** `/fast/scratch/hyaku/kaidoku-r100/` is removed at landing.
- **Open L0 questions:** none appended.
