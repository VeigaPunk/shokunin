# kotoba — round 59 report (hyaku phase 4, attempt 1)

L1 `KotobaR59`. Base `a975cbbf`. Lane tip `0de5aba507784c478dc81f62df7c28d1ac07c559` (pushed: `jj-lane.sh state` shows local = remote, ahead 0). Dispatched 08:56Z. Closed 10:12Z.

## Work performed

There was one declared claim. **C1 is a depth claim (lowest owned axis, 9): hook files by client.** It is sourced, and it is the learning claim. `SKILL.md` gained a new section, § Hook files by client. For each client, the table says which file holds hook configuration, which event names the client's own pages print, and where to send a check that must run at an event instead of writing it into a prompt.

- **Plan.** The draft `a3e70a30` fixed the row rule and the target formula T_F = F_max − 2, T_G = G_max − 1, with targets `TBD`. The freeze `4b2125c9` came after the Q45 census (`.ufo/waves/round-59/w0/Census*.md`, 7 scouts). Six of 7 clients were eligible and all six tokens were absent from the base, so F_max = 6 and G_max = 6, which gives T_F = 4 and T_G = 5. The counter is `verifiers/check_hook_files.py`, sha256 `f695d59e…`, built by `ExecC1Counter`. The addendum `67b68e0f` named the limit of the Events check before any control scored.
- **Pre-data controls.** Commit `283124cd`, `.ufo/waves/round-59/controls/SUMMARY.md`. There were 8 controls: do-nothing, junk, all-false, no-reader, fabricated snapshot, fabricated events, off-topic and label-shortcut. All exited 1 and none met the predicate. The fabricated worlds pass the offline snapshot line, so the live conjunct is the measure.
- **Content.** Commit `c63ccc68`. It adds:
  - the SKILL section (`SKILL.md:121-133`);
  - the knowledge entry `corpus/knowledge/hook-files-round59.md`;
  - sources S096–S101, each with a committed snapshot (`.ufo/waves/round-59/snapshots/`) whose sha256 equals its SOURCES row;
  - S102, the routed R4 correction row;
  - the lesson `corpus/lessons/round-59.md`;
  - Q49–Q51 in `corpus/QUALITY.md`;
  - three index rows in `corpus/README.md`;
  - the PROVINCE.md Core bullet;
  - a verbatim move of the 28-line § Sources block into `corpus/knowledge/anatomy-and-compression.md` (block sha256 `9d74c44e…` on both sides).
- **Round-58 routed defects:**
  - R1: the misrooted `ReviewBudgetMove.md` was copied byte-exact into the lane with a provenance note (`a3e70a30`). The output directory is pinned in `.ufo/waves/round-59/bounds.md`. The misroot sweep was run after the last seat settled (`misroot-sweep.txt`).
  - R2: receipts committed at `ed44e0c4` and at `a975cbbf` (`receipts/`).
  - R3: the counter now reads the Events field cell, checks a committed snapshot, and fetches with curl and a browser user agent. `ScoutLiveDrift` found that code.claude.com returns 403 to Python urllib, so a urllib fetch would have failed S096.
  - R4: correction row S102; S089 left byte-identical.
  - R5: budget lines name the base value.
  - R6: carried.
- **Falsify corrections.** Commit `a5e55b3c`, listed in the lesson § Falsify corrections:
  - Codex trust wording;
  - Cursor `sessionStart` on self-hosted workers;
  - VS Code scoped to the Copilot harness;
  - opencode events labelled as the V2 plugin API;
  - the intro narrowed to command hooks;
  - the three hook scopes kept apart;
  - the shaping notes corrected (M85);
  - the M81 sandbox hash taken out of a `commit` + backtick span, because `verify_corpus_integrity.py` read it as a lane commit and raised `commit_unresolvable` from 1 to 2.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `a3e70a30` | plan draft, R1 copy and provenance, bounds, census start | § Round 59 bullets 1, 4 |
| `4b2125c9` | freeze: census, targets, counter, registry row, W0 reports, R2 receipts | bullet 1 |
| `67b68e0f` | freeze addendum (Events limit) | bullet 1 |
| `283124cd` | control receipts | bullet 2 |
| `c63ccc68` | C1 content, R3–R5, Q49–Q51, index rows, budget move, build reports | bullets 3–5 |
| `d64d945b` | C1 measure receipt | bullet 3 |
| `3f15f844` | LOG entry and SCORECARD depth row | entry |
| `a5e55b3c` | falsify corrections, 40 falsify reports, tip receipts, misroot sweep | falsify bullet |
| `0de5aba5` | close: SCORECARD completion and next round, census end, re-measure | falsify bullet |

## Before → after measurements

- **C1.** Command: `python3 -B verifiers/check_hook_files.py --rev <rev> --fetch`. Predicate: *exit 0 iff F ≥ 4 and G ≥ 5*.
  - Before, at `a975cbbf`: `0 of 0 … new ground 0`, exit 1 (`controls/CtlDoNothing.md`).
  - After, at `c63ccc68`: `hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6`, exit 0 (`.ufo/waves/round-59/C1-measure.txt`). `RerunC1Counter` reproduced this independently.
  - A later measurement at `a5e55b3c`, after the corrections, gives the same result (`C1-remeasure-tip.txt`).
  - The counter sha is unchanged since the freeze (`ReviewChronologyData`).
- **No harm.**
  - All 33 gate self-tests exit 0, the same exit column as the base (`receipts/noharm-base-selftests.txt` vs `noharm-tip-selftests.txt`).
  - Checklist: 11/11.
  - SKILL.md: 596 lines at base `a975cbbf` → 587 at the tip (budget 600).
  - Corpus integrity: 5 DRIFT at base → 4 at the tip. All four are present at base; the one removed is `unindexed`.
  - Gate registry: 32/32 → 33/33.
  - Prior SKILL tables and the round 52–58 entries are byte-identical (`NoHarmPriorClaims`).

## Sources & frontier

`SOURCES.md` rows: 94 → 101. Counting command: `grep -cE '^\| S[0-9]{3} \|' corpus/SOURCES.md`.

- **Rows added (all tier A, mined):** S096–S101, the hook pages of six clients, plus S102, the S089 anchor-correction row.
- **Rows touched:** none in place. S089 is unchanged.
- **Census:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` exits 0 at round start and at round end. Both runs show `kotoba ok` with the same 8 W04 warnings, all on rows ≤ S086 (`census-start.txt`, `census-end.txt`).
- **Frontier advanced:** "Hook files by client" moved into PROVINCE Core, and the frontier note was added to `corpus/README.md`.
- **Mined mistake:** M84. The L1 swapped the census seat's VS Code token without having a seat re-score it. M85 is a further mistake: shaping notes overclaimed for the third time.
- **Sourced claim:** C1 rests on S096–S101.

## Trend verdicts

- **expansion: improved.** There is one new indexed entry and a new SKILL section. 7 new rows were added. Six tokens had 0 hits in the base tree (`ScoutHeldGround`, `ScoutHeldGroundTip`).
- **quality: improved.**
  - Round-58 R1–R5 landed.
  - The counter now reads the field cell and a committed snapshot.
  - All re-opened rows were byte-identical to their snapshots.
  - Seven `Cells*` semantic seats ruled every Events span a real event.
  - The falsify corrections landed.
  - Known limits are disclosed: Action cells and Events semantics are invisible to the counter (`MutC1Content`), and 13 self-test mutants survive but do not change the measurement (`MutC1Survivors`).
- **discernment: improved.**
  - Pre-data controls tested every shortcut class before any data.
  - The census came before the targets.
  - The falsify wave caught M85 and a corpus-integrity regression, and both were fixed before the report.
  - Rejections recorded in the Gate include the opencode plugin token, the VS Code example file, the Cursor `.md` URL and the sentinel's suggested token.

## Gate

There were real rejects:

- `SentinelContexts` and `SentinelFalsifyContext` recommended leading the VS Code row with `.github/hooks/audit.json`. I rejected this: the page names `.github/hooks/*.json` (`hooks.md:59`) as the location, and the E5 premise behind the census seat's rejection does not hold, because Copilot CLI leads with its own path (`CriticCensus`, `CriticCopilotE5`: HOLDS).
- The in-place S089 anchor edit was rejected because the SOURCES contract does not allow it.

Disputed axis: `CriticAxisFit` and `CriticAxisDepth` rule the claim MIXED, arguing that frontier → core reads as coverage under §9, while the routing detail is depth. The claim stays as declared (depth, frozen before data). The closure rules on it.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists and cited sources. Evidence: § Hook files by client, with S096–S101 re-opened byte-identical by falsify seats.
- [~] At least one end-to-end domain task is executed and logged in LOG.md. Evidence: `SHONEN.md:4` (unchanged).
- [~] Instructions are executable by an agent without oral context. Evidence: `SHONEN.md:6` (unchanged).
- [~] No cross-domain bleed; PROVINCE.md is still accurate. Evidence: `w0/ConnSiblingHooks.md` (FITS) and the scope boundary in the entry.

## Round shape and seats

The round used pre-freeze W0 (an ordinary `task` call, 10 seats), pre-data controls (an ordinary `task` call, 8 seats), and two v1 waves validated by the wave validator: build (33 seats) and falsify (40 seats). **Round total: 91 seats.**

- W0: 7 scouts, 2 executors, 1 connector.
- Controls: 4 executors, 4 mutation-testers.
- Build: 13 scribes, 6 scouts, 4 critics, 4 reviewers, 3 executors, 1 mutation-tester, 1 connector, 1 sentinel.
- Falsify: 19 reviewers, 12 critics, 3 mutation-testers, 2 executors, 2 scouts, 1 connector, 1 sentinel.

The L1 held the planner seat. No seat died, none was cancelled, and none was resent.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Tool installs: none. L0 questions: none new; `kotoba | round-55 |` is still open. Fleet-root file left in place for the operator: `.ufo/waves/round-58/falsify/ReviewBudgetMove.md` (a copy is in the lane).
