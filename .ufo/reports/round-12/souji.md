# souji — round 12 report (kaika campaign, 2026-10-19)

Lane: souji-shokunin. Worktree `.tower/worktrees/kaika/souji-shokunin`, branch `kaika/round`, base `dcc8b9e`.
Lane commits: **d7266c5e9493a3c78687af68d438c2584f75b3c0** (round work; after-numbers measured here) and
**de9187e** (records the measured commit in SCORECARD and LOG). Both commits use the lane identity, `-c maintenance.auto=false` and a pathspec. The credential sweep printed nothing.
**No push.** The standing operator rule "No push" overrides MISSION.md's commit-then-push (PROTOCOL.md §Invariants, operator-gated hold; §Fleet-2 conventions, PROTOCOL wins on process).

## Work performed

This round declared three claims:
- **C1 (calibration, the lowest axis at 7):** mine souji's own mistakes and give every class a lane rule that could catch it.
- **C2 (coverage, plus the *sources registry* capability):** `corpus/SOURCES.md` and 5 knowledge entries on three new frontier rows.
- **C3 (operability, plus the *maintenance-guard gate* capability):** a registered gate for git's own receipt-less deleter, plus executable checklist rows.

Round identity: steered r12 (`fleet-ledger/.ufo/waves/kaika/steer.md:31`). No report collision: `souji.md` was absent from both round-12 report dirs. The r11 carry (no-relay re-certification) was not worked this round. It is Planned for r13 (`SCORECARD.md` Planned), and certification stays OFF (`SCORECARD.md` correction note under "Tool certification").

- **L2 swarm.** One batched call dispatched 10 seats: planner, connector, scout, 3 executors, labrat, scribe, reviewer and critic. Every prompt led with `/skill:godspeed` plus the verbatim `directive.md` bytes, and no seat was given a model. Three later spawns followed:
  - Re-dispatch batch: two `task` seats (R12SourcesExec2, R12ExecFs2).
  - One `executor` seat (R12ExecGit2), sent after the orchestrator's route note.
  - Post-integration pair: reviewer and critic.
  - The seat outputs are transcribed in `census/round-12/{planner,connector,scout-surfaces,reviewer-preflight,critic,labrat,scribe,sources-exec2,execgit2,execfs2,postreview}.md`.
- **Provider exhaustion.** All three first-batch executors (R12SourcesExec, R12ExecGit, R12ExecFs) died with `resource_exhausted` ("Reached free model rate limit") before writing anything. Each slice was re-dispatched as a fresh seat. The claims were not shrunk (`LOG.md:453`ff).
- **C1.** The independent scribe mined 52 classes at `dcc8b9e`, with evidence verified by grep (`census/round-12/mistakes.md`). I then wrote:
  - `corpus/QUALITY.md`, which holds Q1–Q15 and cites a lesson for each.
  - `corpus/lessons/round-12.md:43` `## Mistakes`, rows M01–M53 including the new M53 at `:115`.
- **C2.** The work landed in these files:
  - `corpus/SOURCES.md`: 33 rows, `## Paths` at :43, `## Search log` at :49.
  - Five entries in `corpus/knowledge/`: `git-auto-maintenance-prunes-worktrees.md`, `git-grace-periods-and-expire-to.md`, `dupe-finders-detect-then-act.md`, `trash-spec-restorable-quarantine.md`, `quarantine-same-filesystem-rename.md`.
  - The `corpus/README.md` coverage map (:34) and `## Frontier` (:44).
  - The appended `PROVINCE.md:47` Core/Frontier/Adjacent section.
- **C3.** The gate script `tests/fixtures/r12-maintenance-guard.sh` exits 0/1/2, and `--selftest` asserts the pinned ids. Its run is recorded in `tests/results/r12-maintenance-guard.txt`. In `SKILL.md`:
  - a new error pattern (:77);
  - Pre-quarantine checklist rows for the right repo, the guarded commit and pins (:98-100);
  - a gate registry (:102);
  - a sources pointer (:108).
- **Re-derivation.** The pre-landing reviewer reproduced the git prune independently of the fixture author (`census/round-12/reviewer-preflight.md`). After integration, a reviewer and a critic re-derived the Gate. All 10 of their defects were fixed before `d7266c5`; the dispositions table is at `corpus/lessons/round-12.md:121`ff.
- **Incident (M53).** An L2's `cd` failed silently, so a fixture ran in the fleet-root main checkout. It left 4 throwaway commits (c095ea1..b21278d) and about 10 stray files. The full list was reported to the orchestrator, and the lane did not touch the fleet root (`corpus/lessons/round-12.md:29` `## Incident`).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| `corpus/QUALITY.md` (new, Q1–Q15) | LOG.md:453 (round 12) | d7266c5 |
| `corpus/lessons/round-12.md` (Incident, Mistakes M01–M53, Gate with re-derivation table and per-row source grounding) | LOG.md:453 | d7266c5 |
| `corpus/SOURCES.md` (new, 33 rows) | LOG.md:453 | d7266c5 |
| 5 `corpus/knowledge/*.md` entries | LOG.md:453 | d7266c5 |
| `corpus/README.md`, `PROVINCE.md`: appended coverage map, Frontier, corrections, Core/Frontier/Adjacent | LOG.md:453 | d7266c5 |
| `SKILL.md`: error pattern, 3 checklist rows, gate registry, sources pointer (+1,625 B: 6,985 → 8,610) | LOG.md:453 | d7266c5 |
| `tests/fixtures/r12-maintenance-guard.sh` + `tests/results/r12-maintenance-guard.txt` | LOG.md:453 | d7266c5 |
| `SHONEN.md`: 4 boxes `[~]`, each with one evidence line | LOG.md:453 | d7266c5 |
| `SCORECARD.md`: axis rows r12, 2 capability rows, Planned r6–r13, certification correction | LOG.md:453, :493 | d7266c5, de9187e |
| `census/round-12/` evidence, including `baseline.txt` and `after.txt` | LOG.md:453, :493 | d7266c5, de9187e |

## Before → after measurements

- **Before:** `census/round-12/baseline.txt`, measured on dcc8b9e.
- **After:** `census/round-12/after.txt`, measured on d7266c5 with a clean worktree.
- Commands are run from the lane root.

**C1, calibration — a rule-coverage count.** Own-mistake classes whose captured-by cell names an existing rule went from **28/52 to 51/53**. This is rule coverage, not proof of calibration (see Post-review fixes, item 5).
- Command (the BEFORE file is `census/round-12/mistakes.md`; the AFTER file is `corpus/lessons/round-12.md`):
  `sed 's/\\|/%7C/g' <file> | awk -F'|' '/^\| M[0-9]+ \| (defect|process|honest-stop|caught) \|/{n++; if ($6 !~ /^[[:space:]]*none/) c++} END{print c"/"n}'`
- The dangling-criterion check prints nothing.
- This counts *mapped criteria*, not demonstrated catches. M27 and M39 are external, and M43's tool fix is still open.
- Score: 7 → 7 (delta 0). The scores have been legacy-unmapped since r9. The verdict is "improved", pending non-author verification.

**C2, coverage, plus the sources-registry capability.**
- Knowledge entries with all three headers: **0 → 5**, counted by `bash -c 'for f in corpus/knowledge/*.md; do head -3 "$f" | grep -cE "^(source|verified-at|recheck):"; done' | grep -c '^3$'`.
- Frontier rows holding an entry: **0 → 3**, counted by `grep -cE '^\| F[0-9] .*\| frontier, entr' corpus/README.md`.
- SOURCES rows: **absent → 33**. `bash census/round-12/sources-census.sh` printed `33`, `0`, `A=29 B=3 C=1` and `mined=18 queued=13 rejected=2`. The duplicate-id, enum and missing-used-by checks printed nothing.
- Score: 8 → 8 (delta 0). Verdict: improved, pending verification.

**C3, operability, plus the maintenance-guard gate capability.**
- `bash tests/fixtures/r12-maintenance-guard.sh --selftest; echo $?` → 6/6 PASS, `selftest=PASS ids=6/6`, exit **0**. The file did not exist at dcc8b9e.
- Guard rows: `grep -cE 'maintenance\.auto=false|rev-parse --show-toplevel|worktree lock --reason' SKILL.md` → **0 → 3**.
- Score: 8 → 8 (delta 0). Verdict: improved, pending verification.

**Axis harm.**
- **Calibration and coverage:** the post-critic found harm before the commit. Its findings were stale SCORECARD/README state, a C2 dependence on C3, and a broken lock command. All were fixed in d7266c5 (lesson Gate table).
- **Elegance:** the critic found no elegance harm.
- **Operability:** the fixture passed 3 of 3 runs by the critic, 3 of 3 by the labrat, and once more by me.
- Final "no axis harmed" is pending non-author verification.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:28`, `:60`, `:85`; `corpus/SOURCES.md`
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:362` (2026-10-19 operator sweep: 96 pushed-receipt artifacts quarantined, second-checked, removed)
- [~] Instructions executable by an agent without oral context — `SKILL.md:85-108`; `bash tests/fixtures/r12-maintenance-guard.sh --selftest`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:47-69`; `census/round-12/connector.md` §1 (0 sibling claims on F1/F3/F4)

## Sources & frontier

**Rows.** SOURCES rows went from 0 (file absent; `test -e corpus/SOURCES.md` → 1 at dcc8b9e) to 33 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`).
- By tier: A 29, B 3 (S014 community, S017 rmlint Cautions moved down from A, S029 SRE book), C 1 (S030).
- By status: mined 18, queued 13, rejected 2.
- Rejected rows, each with a flip:
  - S030: OneNine `gc --aggressive --prune=now`.
  - S032: git-filter-branch as a cleanup technique.
- Every row was opened on 2026-10-19. The URL, date and quote for each row are in `corpus/lessons/round-12.md:161`ff.
- Rows touched old→new: none, because every row is new.

**Frontier.** Three rows advanced: F1, F3 and F4 went from absent to "frontier, entries held". F2, the size census, was declared but its candidate was deferred.

## Mistakes

- **Classes mined:** 53.
  - By kind: 22 defect, 11 process, 8 honest-stop, 11 caught, plus the r12 M53 defect.
  - At baseline 24 had captured-by `none`; after this round, 2 remain `none` (both external).
- **Criteria added:** 15 in the new `corpus/QUALITY.md`.
  - Q1–Q4 are the seed bar.
  - Q5–Q14 come from the own-mistake classes: blind re-derivation and second seat; certifier evidence integrity; guarded, scoped, right-repo commits; bounded regular-file I/O; shellcheck at `-S warning`; bookkeeping agreement; behavioural checkers and schemas; prune residue; own debris; operator-tooling zone.
  - Q15 is the `/dev/shm` second-device extension. It was written when K5 needed it, and is flagged first for the spot-check.

## Trend verdicts

| trend | verdict | evidence |
|---|---|---|
| **Expansion** | **Moved** (self, pending) | Admitted entries on uncovered ground citing mined rows: 0 → 5, on F1/F3/F4. The connector's sweep found 0 sibling claims on that ground (`census/round-12/connector.md` §1). |
| **Quality** | **Moved** (self, pending) | QUALITY bar created. Every entry clears Q1–Q4, with K5 also needing Q15. A registered gate now has a self-test. The reviewer corrected ART errors (SCHEDULED\|MANUAL; the scope of the fclones group abort). |
| **Discernment** | **Moved** (self, pending) | The admission gate's grounds are below; they await a non-author ≥1-admit / ≥1-reject spot-check. |

Discernment grounds:
- One candidate was rejected (C3 size census), and two SOURCES rows were rejected.
- 10 defects found by the lane's own reviewer and critic were fixed before commit, including the critic's "C2 falsified as declared" finding.
- Three captured-by mappings were downgraded (M10, M23 and M27).

## L0 questions

- `souji | round-12 | Should the fleet-root main checkout be the default cwd for agent shells while `cd` is aliased to a missing function? Lanes cannot fix the harness. A harness-level fix (real cd, or default cwd = the agent's assigned worktree) would close M53's class fleet-wide.`
- `souji | round-12 | F3 and F4 surface three operator decisions: a `duplicate` receipt class, per-item trashinfo-style origin records in quarantine, and `mv --no-copy` / `rm --one-file-system` in souji-quarantine.sh. Approve any for r13+?`

## Integrator notes

- **Fleet root (orchestrator-owned repair).** The fleet root needs repair from souji L2 activity:
  - 4 throwaway commits on master, `c095ea1 551478a 4b2123b b21278d` by `r12 <r12@test>`, all on top of `31baf5c`.
  - The file `f`.
  - Untracked strays: `RelNotes-2.54.0.txt`, `rmlint.1.rst`, `dedupe.rs`, `jdupes-README.md`, `gc-v2.53.0.c`, `gc-v2.54.0.c`.
  - Suggested repair: `git -C /home/vgpnk/Projects/shokunin reset --keep 31baf5c`, then remove those files. The `err.*`, `out.*`, `live_*` and `ind_mode.json` strays at the fleet root are kotoba R46Reviewer-2's (self-reported).
- **Cross-lane.** The cwd hazard reached at least two lanes, souji and kotoba. Git auto-maintenance would prune any expired, unlocked registration on a lane commit. The current fleet exposure is 0 prunable, with gd2d's 3 pins locked (`census/round-12/scout-surfaces.md` §a–b).
- **Contract note.** `SOURCES-CONTRACT-v1` does not say whether `own-work` may be tier A beyond "the lane's own re-runnable gate output". S031 relies on that clause.
- **Open tool gap (lane-owned, Planned r13).** `tools/souji-quarantine.sh` has no per-target timeout (M43, Q8): `grep -c timeout` → 0. Its four tools are not yet in the SKILL gate registry.

## Post-review fixes

The orchestrator's non-author adjudication (reviewer: HOLD; critic: reject as submitted) was handled inside round 12. Fixes are in lane commit **2a363a03d880288fa3df38f411c3b7154fba7def** (lane identity, `-c maintenance.auto=false`, pathspec-limited, credential sweep clean, not pushed). Dispositions are logged in `corpus/lessons/round-12.md` `## Post-review fixes` and `LOG.md` (round 12 post-review entry).

1. **S030 `recheck`** was `—` (census E09). It is now `365d`, changed in place as contract rule 2 allows, and logged old→new in the lesson.
2. **K5 (`quarantine-same-filesystem-rename.md`) moved from admitted to HELD.**
   - Its Gate row claimed a committed fixture, but none exists.
   - Its `/dev/shm` second device relied on Q15.
   - A correction was appended to the entry. S024 and S025 changed from mined to queued, with used-by K5 → `—`, both logged.
3. **Q15 withdrawn.** The superseding row is QUALITY.md Q16: Q15's only lesson pointer was the K5 admission it served, which is circular. Q4 stands unrelaxed.
4. **K2 recheck corrected.** `man` line-wrapping hid the 90-day default. The corrected command, `MANWIDTH=2000 man git-gc | grep -oE '2\.weeks\.ago|3\.months\.ago|defaults to (90|30) days|default is (60|15) days' | sort -u`, finds all 6 defaults; its output is appended to K2.
5. **C1 restated.** 28/52 → 51/53 is a **rule-coverage count**: it counts mistake classes whose captured-by cell names an existing rule. It is not proof of calibration, and it does not show that any rule catches a recurrence. The C1 self-verdict is "rule coverage improved"; whether calibration improved is for the non-author verifier to rule.

Re-measured after the fixes, from the lane root:
- **C2, admitted knowledge entries** (held excluded): **0 → 4**, plus 1 held. Command: `bash -c 'for f in corpus/knowledge/*.md; do grep -q "^## Admission status — HELD" "$f" && continue; head -3 "$f" | grep -cE "^(source|verified-at|recheck):"; done | grep -c "^3$"'`. Frontier rows with an admitted entry: still 3 (F4 via K4).
- **SOURCES census:** `33 / 0 / A=29 B=3 C=1 / mined=16 queued=15 rejected=2`. The last three checks print nothing.
- **Fleet census:** `TZ=UTC bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/souji-shokunin` printed `souji-shokunin	ok	…/corpus/SOURCES.md` with **exit code 0**.
- **C3** is unchanged.

No new claims. The SCORECARD's `## Axes` block carries an appended correction stating the C1 and C2 readings above.
