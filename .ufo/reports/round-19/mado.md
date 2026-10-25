# mado — round 19 (hyaku phase 2, attempt 1)

Lane `mado-shokunin`, branch `master`. Baseline `9c54c56a6a7528675027b7f628f97a1b8d1b8e8d` →
lane tip **`b435568540f9a28f4f7bb902af8dbe6a5b084dfe`** (landed and pushed by `scripts/hyaku/jj-lane.sh`; `state …
local=remote=b435568… ahead=0 behind=0`). The lane VCS is jj-colocated, and every lane commit
went through the helper. Tools final at `7b4839d31d60af5bac40e3e74aec70e928601dfc` (gate F9 containment landed
after wave 2); later commits change prose, receipts and seat reports only.

## Work performed

Declared claims (pre-registered at `17661e0`, `SCORECARD.md` "Round 19 — declared claims"):
**C1 calibration** (literal lesson-citation fraction), **C2 freshness** (new bounded
sub-axis: walker version-pin currency over the 13 owned files that said `2.17.0`; the
lowest scored axis at 2/13, and the round's **sourced** claim, on S096), and **C3
operability** (new bounded sub-axis: tripwire recall on the 6 frozen real-incident lines).
No exploratory claim. Both sub-axis rubrics were declared before measurement.

- **Outside spot-check R18-V1..V4, how each was handled.**
  - R18-V1 (S094 anchors per-fetch HTML digests) → lesson M1, QUALITY 27, checker
    `.ufo/waves/round-19/anchor-durability.py` (red `9c54c56` `FLAGGED S084 S094` exit 1 →
    green `flagged=0`, `evidence/final/anchor-durability-{red,green}.txt`). S097 supersedes
    S094 (tag commit `8fcc9d60…`, git tree ids `3fc08f95…`/`ff02c341…`, raw `dbdd13a6…`);
    S094 `mined → rejected`.
  - R18-V4 (S084 docs.rs `latest`) → M2, QUALITY 27 UNPINNED_ALIAS arm; S098 = xdg 3.0.0
    crate whose sha256 `2fb43323…` equals walker v2.17.2 `Cargo.lock:2708`; S084 rejected.
  - R18-V3 (stale walker pins in sibling notes) → M3, QUALITY 28, checker
    `supersede-sweep.py` (red `stale=11` → green `stale=0`), and C2 (13 files pointered).
  - R18-V2 (criterion 26's red-before headerless) → M4, recorded as an application of
    criterion 24, not a new criterion (outside critic CriticC1: a 29 would restate 24);
    header-bound re-cut `evidence/gate-swap-receipt.txt` (383 passed / 6 failed).
  - '14/31' note: the round-18 report counted failures; the old tool passes 17/31
    (RevSpotcheckRouting: lesson-only, no further action).
- **Carried items.** Frozen F1 (blank-line pin → `frozen_error`) and F2 (`link/.` →
  `snapshot_tampered`) closed (suite `r19-frozen-f1f2` 13/13). `measure-mutants.py`: no
  default lane write, and `--workdir` no longer deletes a caller-named directory. jj F6:
  the gate reads the branch tip only when `$tree/.jj` exists and `HEAD^{tree}` equals the
  tip's tree (OM11/OM16/OM17); F9: `[ -e "$tree/.git" ]` then `rev-parse --git-dir`
(OM12, OM18 — w2 ReviewJjFinal caught the walk-up to `~/.git`); F16 narrowed by
  `landed-check.sh` (a probe, not a gate row); F17 stays operator-owned — colocation is
  structural while `HYAKU_VCS=jj` (w1 JjIncidentScan).
- **C2.** Gate `live.walker.version` pin 2.17.0 → 2.17.2 with the PASS narrowed to
  "installed version matches pin; claims measured on 2.17.0 stay dated"; nine notes,
  SKILL.md and README gained dated pointers; S096 = host walker bytes (sha256
  `25240650…`, one `2.17.2` literal at offset 856,302, none `2.17.0`). Wave 2 found two
  pointers calling S096 "reserved" and several "not re-measured" overstatements; all
  corrected (lesson M10).
- **C3.** Six patches composed by one integration seat into `tools/mado-tripwire.py`
  (BashCVar, HelperFn, Installers → class `tool_install`, VcsClass → class `vcs_write`,
  frozen F1, F2); 247/247 suite cases over 11 suites; round-19 frozen baseline re-pinned.
- **PROVINCE.** One path-root line for `~/.config/omarchy/**` (IN: theme state and
  `current/` links; OUT: hooks, branding, extensions, themed templates, secrets → kagi);
  no sibling owns any IN item (w1 ConnProvinceRoster, w2 AtkProvinceLine).
- **Planner seat:** L1 held the canonical planner seat (the validator rejects `planner`);
  planning data-walks rode scouts/reviewers (RevSpotcheckRouting, FrontierRows).
- **Frontier step (mistakes).** Lesson rows M1–M14, plus wave-2 corrections; this round's
  own: M5 (pre-registration receipts named a commit without their producer), M6 (bot-
  challenge pages with the operator's IPv6 nearly committed), M7 (overfit recall counter),
  M10–M14.

## Landed changes

LOG entry `## 2026-10-20 — round 19: durable anchors and supersession sweep, walker pin
currency, tripwire recall`.

| commit | content |
|---|---|
| `17661e0f` | pre-registration, counters `fresh-pins.py`/`tw-recall.py`, before receipts |
| `df84807d` | wave-1 integration: gate walker re-pin + F6/F9 (443/443), S096–S098, S084/S094 rejected, walker pointers, SKILL erratum, PROVINCE line, round-19 checkers, w1 reports |
| `01b80946` | tripwire merge (247/247), round-19 frozen re-pin, QUALITY 27–28 + R18-V2 note, lesson, SKILL registry, gate-swap + recut receipts |
| `61eaa071` | wave-2 integration: gate F5–F9 + F6 tree check + OM1 guard (452/452), note corrections, ledger, QUALITY limits, lesson M10–M14, SCORECARD/LOG, tool-safety fixes, fetch RETENTION, w2 reports |
| `6963d34b` | final header-bound receipts at `61eaa07` |
| `0fa41252` | receipt claims 16/16, SCORECARD final state + round-20 plan |
| `c7693eb2` | post-wave seat tripwire scan receipt, lesson M12 correction |
| `7b4839d3` | gate F9 containment (`[ -e .git ]`, OM18; 460/460), delta-carry note corrections, late w2 reports |
| `d642ce52` | final receipts + harm watch re-cut at `7b4839d` |
| `daf6543e` | receipt claims 17/17, SCORECARD final-state correction |
| `b4355685` | last w2 report (ReviewLessonRows) and its lesson corrections |

Inherited state: no `lane-dead-no-report mado round=19` line; attempt 1; the worktree was
clean at start. Nothing inherited.

## Before → after measurements

| Claim | Counting command | Before (`9c54c56`) | After (`7b4839d`) | Receipt |
|---|---|---|---|---|
| C1 calibration | `python3 .ufo/waves/round-17/measure.py REV` (`c1`; instrument `de4c422b…`) | 18/26 = 6.9231 | 20/28 = 7.1429 | `evidence/measure-before.json.txt`, `evidence/final/measure-after.txt` |
| C2 freshness | `python3 -I .ufo/waves/round-19/fresh-pins.py REV` | 2/13 = 1.5385 | 13/13 = 10.0000 | `evidence/fresh-pins-before-recut.txt`, `evidence/final/fresh-pins-after.txt` |
| C3 operability | `python3 -I .ufo/waves/round-19/tw-recall.py REV` | 3/6 = 5.0000 (tool `c1ae45a7…`) | 6/6 = 10.0000 (tool `367be947…`) | `evidence/tw-recall-before-recut.txt`, `evidence/final/tw-recall-after.txt` |

All receipts bind producer and commit: `python3 -I .ufo/waves/round-18/receipt-check.py
.ufo/waves/round-19/receipt-claims.json` → `EXPECT_SUMMARY: 17/17` (final receipts at
`7b4839d`, committed `d642ce5`).

Verdicts (author, bounded):
- **C1: improved, pre-registered target ≥21/29 missed** (decision recorded; criterion
  28's walker entry is the C2 file set, so its green is not independent of C2).
- **C2: improved as counted; read as "13/13 pointed, 5/13 name S096 on the crediting
  line, 0 walker facts re-measured on 2.17.2"**. The 2/13 baseline credited two round-18
  lines; substantively 0/13 before.
- **C3: improved on the six lines the drafts were written for; 5/6 without the HelperFn
  rule-B lead.** Guards: the three new findings are `package_query/pacman:-Q`, the class
  the round-18 notes name; 0 findings on the 20 control lines; whole-corpus base-vs-merged
  diff lost 0 findings (w1 TwMerge-2, w2 RerunPrecision: 4,728 stable transcripts, 13
  added rows outside the new classes, all judged true). Open: rule B fires on 12/12
  synthetic data-only shapes and does not mark leads; `vcs_write` reports 74 `jj … --help`
  and 4 `git --dry-run` rows; eval-surface VCS writes unseen (lesson M14).

Harm watch at `7b4839d` (`evidence/final/harm/`): `HARM_WATCH: PASS`, 22 runs — gate
selftest 389 → 460/460 (the ten old OM10 assertions were replaced by OM10A/B, no other
assertion lost; w2 CriticAdmission label diff at 443), regression PASS (`PIN_MADO`
`367ff5ec…`), classifier 52/52, 11/11 tripwire suites (round-17 hardening reads 32/33
under the pre-round tool after one reasoned case edit), rubric V 6/6, U 7/7, navigation
34/34, census exit 0. No owned axis harmed by lane action.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin mado`. Start: exit 0, 95 rows, W04 S030/S042/S045
  (`evidence/census-before.txt`). End: exit 0, 98 rows, W04 S030/S042/S045/S097 (S097
  shares S094's raw URL; S094 is rejected) — re-run by w2 RerunCensusNav.
- Rows 95 → 98; added by tier: A +3 (S096 host walker bytes, S097 omarchy theme payload,
  S098 xdg crate). Tiers A 88 → 91, B 1, C 6; mined 80 → 81, queued 8, rejected 7 → 9.
- Rows touched old→new: S084 status mined → rejected, used-by
  `corpus/knowledge/walker-route-r18.md` → `—`; S094 status mined → rejected, used-by
  `corpus/knowledge/theme-route-r18.md` → `—`; S096 used-by widened to eight paths (lesson
  `round-19.md` § Gate). All three new rows re-opened by non-author seats (w2 ReopenS096,
  ReopenS097, ReopenS098, AtkLessonGate) — agree, with two quote-position corrections.
- Frontier advanced: README `## Frontier` — "host binaries stay `[UNK]`" narrowed to
  walker's binary bytes (S096); new `## Paths` entry "Walker version provenance";
  Search-log note. Still open: running process, rendered UI, elephant/uwsm/hyprland moves.
- Sourced claim: C2 rests on S096, opened this round.

## Trend verdicts

- **expansion: unchanged.** No new knowledge entry on uncovered ground; three new rows
  harden existing routes (rubric V 6/6 held).
- **quality: improved.** Anchors made reproducible (S097/S098), thirteen stale files
  dated and pointered, gate jj/worktree false readings closed (F6 incl. the tree check,
  F9), four tool-safety defects fixed, tripwire recall 3/6 → 6/6 with precision guards;
  wave 2 found and the round corrected 10+ overstatements in its own new text.
- **discernment: improved.** Two lesson-cited criteria with real reds at `9c54c56`; the
  round declined a duplicate criterion and reported the missed target; outside critics'
  narrowings (C2 sourcing, C3 overfit, R10 attribution) are recorded rather than argued.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` registry rows `mado-anchor-durability` … `mado-fresh-pins`; round-19 errata (author assertion).
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG round-19 entry; walker version re-anchor end to end (host bytes → pointers → gate pin), not outside-verified.
- [~] Instructions executable by an agent without oral context — `evidence/final/*.txt` commands re-run by 67 wave-2 seats from the committed text (lane-dispatched, so author-side).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` round-19 line; w1 ConnProvinceRoster and w2 AtkProvinceLine: no contested scope.

## Waves, seats, installs, L0

| wave | seats | role mix | dead (no report) |
|---|---|---|---|
| w1 (build) | 86 | reviewer 18, executor 15, scribe 15, scout 14, connector 8, critic 5, revenger 4, mutation-tester 3, simplifier 2, sentinel 2 | 25, all m_zfl (`429 Rate limit reached`, zai glm-5.3-flash): ConnCarriedLedger, ConnFrontierPlan, ConnJjAuditsFleet, ConnRegistryTools, ConnSiblingAnchors, ConnSiblingSupersede, RevDraftBashCVar, RevDraftHelperFn, RevF1F2Repro, RevFreshPinsCounter, RevGateWalkerRow, RevJjDisposition, RevNavigationU, RevPipeRcTip, RevPreReg19, RevQualityOverlap, RevR18Mining, RevReceiptChecker, RevSkillHeadGuidance, RevSourcesContract, RevTwRecallPrecision, RevengeFrozenValidation, RevengeS094Anchor, RevengeWalkerPinHistory, SimplifyTripwireTip |
| integration | 1 | executor (TwMerge-2, ordinary `task`; first attempt refused by the 100-job cap, retried) | 0 |
| w2 (falsify) | 67 | scout 22, executor 20, reviewer 10, critic 5, mutation-tester 4, sentinel 3, scribe 3 | 0 (all 67 reported; m_zfl reviewers slow, 30–60 min) |

Round total 154 seats (≤200). Routing by role (orchestrator note mid-round: scout/labrat
→ m_flash); no `model` parameter passed. Misroot sweep: seat QualityDraft wrote two files
at the fleet root `.ufo/waves/round-19/`; copied byte-exact into the lane (`cmp` equal) and
the fleet copies deleted (lesson M8); final fleet sweep clean.

Installs: none by L1. Seat AdvInstallers ran pip 26.2.1 ephemerally via `uv run
--no-project --with pip` (uv cache only) to check pip's grammar. Host-pause breach: seat
SentinelGatePath ran the real `/usr/bin/hyprctl probe` once (rc 0, `unknown request`),
self-reported (lesson M12); the post-wave tripwire scan did not see it (script-run form).
No pacman transaction or package query by any mado seat (w2 AtkInstallsRecord).

Stale-lane: respawn-per-round driver; launch `2026-10-20T13:54:23-03:00 launch mado
round=19`; this mission is progressing (lane commits above); no other mission of this lane
is open.

Open L0 questions: none new. R15-V1 stays operator-owned.
