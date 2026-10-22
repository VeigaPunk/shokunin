# kotoba — round 52 report (hyaku campaign, attempt 2)

Lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, branch `master`. Base `c8579a4c5b48789e56fb9060ddd48f33569e1215`
(round 51 closed `rejected-honest-stop`). Lane head after this round: `a44196d8a654fcb32491964c846e986122f9c51b`
(helper `landed a44196d8a654fcb32491964c846e986122f9c51b`; `jj-lane.sh state` → `local=remote=a44196d8… ahead=0 behind=0`).
L1 attempt 2: `KotobaR52a2`. Scope frozen by Main at 18:41Z; nothing was added after the freeze.

## Work performed

Declared claims (plan `plans/round-52.md`, committed at `4c003a4b` together with both counters, before any data):

- **C1 — freshness** (the lowest non-retired axis, tied with adjacency at 8): the omp loader-registration extraction in
  `verifiers/verify_surfaces.py` survives a pure callee rename on the 4 pinned omp fixtures:
  `callee-rename robust 0 of 4 fixtures` → `4 of 4`.
- **C2 — coverage** (the learning claim and the sourced claim): `corpus/knowledge/mcp-server-instructions-round52.md`
  backs K of 7 pinned clients with a located quote about MCP server `instructions`: `backed 0 of 7` → at least `3 of 7`.

Work items:

- Inherited from attempt 1 (died in an omp restart at 17:26Z): pushed commits `4c003a4b` (plan, frozen counters), `c2107ecf` (C1),
  `c8407a45` (C2, routed repairs, M36 fix). The attempt-2 L1 re-verified them before reuse (LOG.md § Round 52, bullet 2): the
  counters are byte-identical from `4c003a4b` to `c8407a45` (`git diff` empty); C1 0 → 4 of 4 and C2 0 → 5 of 7 reproduce.
- Inherited uncommitted leftovers, both resolved by commit `a44196d8`: (1) `SCORECARD.md`. Its round-52 cells and blocks had three
  defects found by the falsify wave: "the falsify wave ran", "completed", and a stale "pass 7". They were rewritten before the
  commit. (2) `.ufo/waves/round-52/`: attempt-1 build and falsify specs, dispatch payloads, empty gate files and two registries with
  no seat reports. They are committed as evidence. Nothing was reverted.
- The repair-first rule from the round-51 verifier spot-check: each routed item became a fix or a criterion. Items 1 and 2 were fixed
  in attempt 1, and the pointer was corrected in attempt 2. Item 3 was not re-declared. In item 4, S038 (supersedes S031) came from
  attempt 1. Attempt 2 added S039 (supersedes S024) and the fixture labels for lines 9, 15 and 33. D2 F1–F5, D7, R1 and R5 are
  carried with reasons (`corpus/lessons/round-52.md:111-116`). The session rule (a target missed on frozen tables is an honest stop,
  never a widened table) is held by Q28 plus Q15 (seat `ReviewSpotcheckRouting`). On this round's frozen counters: `git diff
  4c003a4b a44196d8 -- verifiers/check_callee_rename.py verifiers/check_mcp_instructions.py` is empty.
- The attempt-2 falsify wave had 34 seats. All 34 reports except `ExecGateMatrix` are committed at
  `.ufo/waves/round-52/falsify-a2/`; `ExecGateMatrix` was still running at the report time, see below. Corrections by seat:
  `corpus/lessons/round-52.md` § Falsify-wave corrections (attempt 2).
- C2 false negatives (`CriticLearning`, `SweepOpencode`, `SweepCopilotCli`). opencode documents server instructions
  (`mcp-servers.mdx:429`) and so does Copilot CLI (`changelog.md:1157`, `:2895`), but attempt 1 had recorded both as "silent".
  This was fixed with rows S041 and S042, the entry, the `SKILL.md` table, `PROVINCE.md:19` and `corpus/README.md:78`. It is
  mistake M38, and criterion Q30 now covers it.
- Counter described wider than its code (M39, Q31): the entry and SCORECARD said the C2 counter checks location and Gate placement,
  which it does not. Corrected.
- New spec revision (`ConnSiblingOverlap`): row S040 records MCP 2026-07-28, which removes `initialize`; `instructions` now sits on
  `server/discover`.
- C1 fixes after the wave, in `verify_surfaces.py`:
  - **Unresolved-group admission** (`CriticC1Escape` P4): a callee whose group the extractor cannot resolve is now admitted.
  - **Empty-baseline fallback** (`ReviewC1Diff`): an empty baseline no longer passes. Repro: `FAIL … 8 loader class(es)
    undeclared`, exit 1.
  - The self-test stays at 0 failures over 129. Neither fix has a self-test arm yet; that is carried.
- Sweep registry: rows `r52-c2-*` were added to `verifiers/check_correction_sweep.py`. The sweep is red at `c8407a4` (3 stale
  blocks) and green at `a44196d8`; its self-test grew from 5 to 7 assertions.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `4c003a4b` (attempt 1) | plan; frozen counters `check_callee_rename.py`, `check_mcp_instructions.py` | § Round 52, bullet 1 |
| `c2107ecf` (attempt 1) | C1: declared-pair admission in `verify_surfaces.py`; self-test 119 → 129, floor 129 | § Round 52, bullets 1-2 |
| `c8407a45` (attempt 1) | C2 entry, rows S032–S038, `SKILL.md` table, PROVINCE Core; routed defects 1-2; M36 fix `check_correction_sweep.py`; Q29 | § Round 52, bullets 1-2 |
| `a44196d8` (attempt 2) | falsify corrections (S039–S042, entry, SKILL.md, PROVINCE, README, Q30, Q31, M38–M40), fixture labels, two C1 fixes, sweep rows, SCORECARD leftover rewritten, LOG, wave evidence | § Round 52, bullets 3-6 |

## Before → after measurements

- **C1:** `python3 -B verifiers/check_callee_rename.py --rev <rev>` (frozen at `4c003a4b`). Before: `callee-rename robust 0 of 4
  fixtures`, exit 1 @ `c8579a4c` and @ `4c003a4b`. After: `4 of 4`, exit 0 @ `c2107ecf`, @ `c8407a45` and @ `a44196d8`, with seeds
  52, 7 and 1234 (L1 runs at 17:44Z and 18:41Z). The remote clone gives the same result (`ExecPushedBytes`). **Verdict: verified as
  declared.** Limits found by the wave: the counter does not catch a widened lookbehind (`MutCalleeCounter` M4, caught by a self-test
  arm instead), and admission keyed on the group alone survives every gate (M5).
- **C2:** `python3 -B verifiers/check_mcp_instructions.py --rev <rev>` (frozen at `4c003a4b`). Before: `mcp instructions backed 0
  of 7 clients`, exit 1 @ `c8579a4c`. **Declared after-state:** `5 of 7`, exit 0 @ `c8407a45` (`--fetch` 5 of 5; the target was
  "at least 3"). **Verdict: verified as declared.** After the M38 correction, the same frozen counter gives `7 of 7`, exit 0 @
  `a44196d8` (working tree with `--fetch`: 7 of 7 found live, 18:01Z). That is a later measurement on unchanged tables. It is
  reported beside the declared value and does not replace it (Q28). `CriticC2Sizing` notes that the target was a floor, not one
  value. `MutMcpCounter` notes that the counter's host-path pins and its Gate check (any substring of the lesson) are loose: 8 of 8
  data mutations were killed, and M12 and M16 survived.
- **M36 fix, shown able to fail:** `python3 -B verifiers/check_correction_sweep.py --rev <rev>`:
  - `c8579a4c`: exit 1, 3 stale blocks (r51 rows).
  - `c8407a45`: exit 0 on the attempt-1 registry. On the attempt-2 registry it is exit 1 with 3 stale blocks (the `r52-c2-*` rows).
  - `a44196d8`: exit 0.
  - The check covers only the phrases in its registry (`MutSweepCheck`).
- **No-harm guards:**
  - `verify_surfaces.py --json` gave pass 7, exit 0, at 17:45Z.
  - The host's opencode then moved from 1.19.3 to 1.19.4 at 17:50:30Z. This round did not cause that. Since then the gate gives
    pass 6 (`surfaces.opencode_extract` FAIL), and `check_substrate_pins.py` gives DRIFT 1/3, at base and head alike. With the
    committed opencode fixture the gate is pass 7.
  - `verify_surfaces.py --self-test`: 0 failures over 129. `check_assertion_floors.py`: PASS. `verify_skill_checklist.py --json`:
    pass 11, fail 0.
  - `verify_corpus_integrity.py`: 5 of 9, the same count as base. Its `tracked_files` and `commit_total` drift are this round's new
    files and pointers; the baseline re-record is carried.

## Sources & frontier

- Census at attempt-2 start (17:46Z) and at round end (18:43Z): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate
  --root /home/vgpnk/Projects/shokunin kotoba` → exit 0 both times, with the same output both times (`W04 S018`, `W04 S019`, `W04
  S021` duplicate URL across scopes, then `kotoba ok`).
- Rows, counted with `git show <rev>:corpus/SOURCES.md | awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13'` per
  tier: `c8579a4c` 31 rows (A 30, C 1) → `c8407a45` 38 rows (A 36, B 1, C 1) → `a44196d8` 42 rows (A 40, B 1, C 1).
- Rows added, all tier A unless noted: S032–S036, S037 (tier B) and S038 in attempt 1; S039–S042 in attempt 2. Every new row was
  opened 2026-10-22, and each lesson Gate entry carries the URL, the access time, the bytes, the sha256 and a located quote of at most
  25 words (`corpus/lessons/round-52.md` § Gate).
- Rows touched: S024 status mined → mined, recheck 90d → 90d, no cell changed; its `teaches` is superseded by S039. S031 is
  superseded by S038 the same way.
- The two attempt-1 rejections (opencode, Copilot CLI) are kept as found, and a correction is appended beside them.
- Frontier: "MCP/plugin instruction surfaces" advanced in part. MCP server `instructions` per client moved to `PROVINCE.md` Core.
  Plugin surfaces, measured client behaviour, and omp's own handling stay in Frontier.
- Sourced claim: C2 (S032–S036, S041, S042). Mined mistakes: M36–M40 (`corpus/lessons/round-52.md` § Mistakes), with the M36 and
  M38 fixes shown able to fail as stated above.

## Trend verdicts

- **expansion: improved.** `git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'` goes up by one at `c8407a45` (the
  new MCP instructions entry). Six clients and the current spec revision are now recorded, and the Frontier → Core move is in
  `PROVINCE.md:19`.
- **quality: improved.** The attempt-2 wave found and corrected two false negatives, a counter description wider than the code, a
  stale spec premise, two C1 extraction escapes, and the inherited SCORECARD claims. Every correction is listed by seat. The cost is
  that the C1 limits M4/M5/P2 and the C2 counter's loose pins stay open, recorded and carried.
- **discernment: unchanged.** The lane's own attempt-1 sweep produced a false negative, and its record overclaimed (M38, M39, M40).
  The drift sentinel trips: rounds 50–52 each routed "a record wider than what was verified". The lane caught these only through its
  own falsify wave, and an outside spot-check is still owed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SKILL.md:86-95` (MCP
  `instructions` table, sources S032–S042); `verify_skill_checklist.py --json` pass 11 at the attempt-2 tree.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `corpus/knowledge/cold-run-round11.md`
  (unchanged this round).
- [~] Instructions executable by an agent without oral context — evidence: `corpus/lessons/round-8-aggregator-box3-coldrun.md`
  (no fresh non-author run this round).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `.ufo/waves/round-52/falsify-a2/ConnSiblingOverlap.md` (0
  adjacent, 0 contested MCP hits across 20 sibling lanes).

## Round shape, seats, holds

- Shape: the default two-wave v1 shape. Its build wave was the attempt-1 L1 working inline (0 seats: no grant, route outage, M37).
  The attempt-1 falsify wave (36 seats) was cut off by the restart with no report, and is not counted.
- Attempt-2 falsify wave: 34 seats, v1, validated. Role mix: reviewer 9, scout 10, critic 7, mutation-tester 3, executor 3, scribe 1,
  connector 1; 19 attack seats.
  - A 46-item spec was validated first. It was cut to 34 before dispatch so the wave fit under the shared cap (live 51 of 85).
  - The gate printed `granted … seats=34 live=50`.
- Round total: 34 seats. No seat died, no seat was refused, and no residual call was made.
- Planner seat: held by the L1, which wrote no planning items.
- `ExecGateMatrix` had not returned when this report was written. Its report is not part of this report's evidence.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked fleet-root file written by this lane's
  seats.
- Installs: none, by the L1 or by any seat that reported (every seat report says none).
- L0 questions: none.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
