# tabi — round 29 report (hyaku run 8, attempt 1, fresh-start round)

Lane repo `/home/vgpnk/Projects/shokunin/tabi-shokunin`, branch `master`. Baseline
`856fa9e1202179f5cfbd28c1f0efdd4eb1f426bb` → final lane hash **`f36caf6a12faa14e33ff27efabe09f7d6c1324df`**
(`git ls-remote origin refs/heads/master` → `f36caf6a12faa14e33ff27efabe09f7d6c1324df`). L1: TabiR29.

## Work performed

Declared claims (frozen before data in `97be89bc66139eb45526a04af59a35dccc006eb9`, `.ufo/waves/round-29/claims.json`):

- **C1 — operability** (lowest-axis tie at 8): repair the `scripts/check-s106-evidence.mjs` self-test (round-28 routed defects 1–2).
- **C2 — calibration**: self-assessment-vs-observed mismatches 6 → 0 under a counter whose supersession citation must name the stale line's own document (round-28 routed defect 3).
- **C3 — freshness** (lowest-axis tie at 8; the round's sourced claim): re-open the 23 on-release registry rows pinned to Chromium tag 154.0.8037.97 at the new Stable tag 156.0.8078.47 (trigger: new row S108).

Fresh-start preparation: read the r26/r27/r28 closures (`MANIFEST.json` tabi rounds 26–28) and `corpus/lessons/round-2{6,7,8}-verifier-spotcheck.md`. Each claim got a do-nothing control and a junk control. All of them were scored before any claim data, and none reaches its target (`.ufo/waves/round-29/baseline/`, provenance `baseline/README-receipts.md`).

- C2 counter frozen with doc-bound `citesLine` and two cross-document red cases. Before the fix: `SELFASSESSMENT_SELFTEST verdict=failed cases=22 passed=20` (`baseline/c2-red-before-selftest.txt`). After: clean 22/22 (`baseline/c2-after-fix-selftest.txt`). Cross-document junk control: the old counter reports 0 mismatches, the frozen counter 6 (`baseline/c2-control-crossdoc-*.json`). Landed in `97be89bc`.
- C3 counter `scripts/check-release-pins.mjs` written by the L1 before freezing; self-test `cases=20 passed=20` (`baseline/c3-selftest-frozen.txt`). Baseline reading: population 23, unresolved 23, exit 1 (`baseline/c3-before.json`). Landed in `97be89bc`.
- C1 controls:
  - Baseline self-test exits 1 on `ReferenceError existsSync`, with no tally (`baseline/s106-selftest.txt`).
  - Case-deletion junk control: clean 5/5, so it misses the target (`baseline/c1-control-case-deletion.txt`).
  - Import-only control: 5/7 failed (`w1/MutC1Baseline.md` §2).
- C3 data:
  - 23 wave-1 seats (`PinS033`…`PinS106`) fetched each cited file at both tags: 46 distinct files.
  - Integrated as `corpus/evidence/round-29/release-pins/{receipt.json,bytes/}` with rows S108–S115 in `corpus/SOURCES.md:122-129` (`190052c9`).
  - 16 rows hold; 7 drifted (S042, S071, S078, S080, S081, S096, S100) and are superseded by S109–S115.
- C3 refetch: 23 wave-2 seats (`Refetch<id>`) each re-fetched their row at both tags and wrote an independent re-fetch record. All 23 agree with the receipt (S094 after the documented 404-nonce normalisation). Committed at `corpus/evidence/round-29/release-pins/refetch/` (`9cc92b08`).
- Knowledge: new entry `corpus/knowledge/chromium-156-release-pin-recheck.md`. Appended round-29 recheck notes in the 7 entries that cite a drifted row, plus an S045 semantic note: its lines hold but the test contract changed (`32008a45`). Wave-2 errata appended (`9cc92b08`, `ab080992`).
- C1 repair: written by wave-1 seat ExecC1Repair (import, `fieldValue` assertion, mismatch case commits its receipt) and integrated with the L1's re-run mutation receipt `corpus/evidence/round-29/s106-selftest/mutation.txt` (`59e8167a`).
- C2 corrections: append-only `SCORECARD.md:1458-1466` (each line cites the stale line in its own document) and the `LOG.md` round-29 paragraph "Correction (supersedes LOG.md:221)" (`59e8167a`, `35045d7d`).
- Gate registry rows: `SKILL.md:2532-2545` round-29 section. `check-gate-registry` nonconformant goes 2 → 0 (`measure/gate-registry-rev.txt`).
- Lesson `corpus/lessons/round-29.md` (Gate, Mistakes M1–M5) and `corpus/QUALITY.md` criteria 71–73, each citing that lesson (`e1e3a15f`).
- Round-28 routed defects:
  1. s106 self-test controls: fixed (C1).
  2. Post-edit evidence: `.ufo/waves/round-29/measure/` with SKILL tallies taken from observed runs.
  3. Cross-document citation: fixed (C2).
  4. Wave accounting: `.ufo/waves/round-29/r28-wave-accounting.md`.
  5. Byte-exact census: captures committed by redirect, criterion 72.
- Planner seat: held by the L1 (the validator rejects `planner`). The bounded planning data-walk rode the connector and scout items (`w1/ConnSeparability.md`, `w1/ScoutUsedBy.md`).

### Round shape

- Two v1 waves, both validated under `scripts/hyaku/ufo-wave-policy.json` (exit 0) and dispatched through the inline handoff (`w1.ready`, `w2.ready`).
- **W1 (build + first falsifiers): 44 seats** — 26 executor, 6 critic, 3 reviewer, 3 mutation-tester, 3 connector, 2 scout, 1 scribe. m_flash roles 33/44 = 75 %; attack roles 12/44 = 27 %. 44 results, 44 reports.
- **W2 (falsify): 39 seats** — 25 critic, 5 executor, 3 reviewer, 3 mutation-tester, 2 connector, 1 scout. m_flash 30/39 = 77 %; attack 31/39 = 79 %. 39 results, 39 reports. Every W2 item names what it attacks.
- **Round total: 83 seats; 0 dead; no residual call.** Results: `.ufo/waves/round-29/w1-results.json` and `w2-results.json`.
- Seats that left scratch on disk (their own defect; removed by the L1): ExecC2DryRun, ExecRerunC2, ExecRerunC3, MutC2Corrections, RefetchS077, RevC3Code, RevSources, ScoutGateRegistry.

### What the attack waves found, and what was done

- **C3 counter weaknesses (critical, not fixable this round — the counter is frozen).**
  - Re-fetch records derived from the receipt reach unresolved=0 with no network fetch (`w1/CritC3Gaming.md` S1/S14).
  - Filing a subset of a row's cited spans hides drift (`w1/CritSemanticDrift.md` §1).
  - Single-number range tokens bind to tag digits.
  - The population is a count, not an id set.
  - `w1/MutC3.md`: 10 surviving mutants. `w2/MutC3Receipt.md`: one surviving mutant (an omitted file).
  - The predicate sentence claims more than the code enforces (`w2/CritPredicateIdentity.md`).

  Response: no counter change after data. On the round's own data, wave 2 checked the stronger sentence directly:
  - Every row re-fetched at both tags by a seat other than its wave-1 fetcher, with filing completeness checked against each anchor. 44 of 46 files are byte-identical; the S094 404 bodies match after normalisation (`w2/RevKnowledge.md` method §3, `w2/Refetch*.md`).
  - Reversing any one claim leaves the other two claims' counts byte-identical (`w2/ConnSeparabilityW2.md`).

  Recorded as lesson M4 and QUALITY 73; counter v2 is planned for next round.
- **S094 404 bodies carry a per-request nonce** (`w1/CritSemanticDrift.md` §4). Normalised in the committed body. The receipt fields `normalization` and `raw_new_sha256` disclose it (lesson M5).
- **S045 holds, but its meaning changed at 156** (events now dispatch on `document.modelContext`). Marked in the citing entry.
- **Accuracy defects in the recheck notes** (`w2/RevKnowledge.md` F2–F6, `w2/RevSources.md`): wrong line pointer, wrong struct name, guard range 201-209 / 9 lines. Corrected by appended errata. The registry cells S110, S114 and S115 keep their wording defects, which are recorded in the lesson.
- **C2 before-value provenance** (`w1/CritProcedure.md` F1): 6 with the frozen counter run outside a clean baseline clone; 5 in-tree at 97be89b (SCORECARD.md:1439 is could-not-evaluate there). Both readings are > 0, so the target is unaffected (`baseline/README-receipts.md`).
- **s106 self-test coverage gaps**: sha-drop and anchor-uniqueness mutants survive (`w1/MutC1Baseline.md`, `w1/CritC1Vacuity.md`). Routed to next round.

## Landed changes

| Commit | LOG.md entry | Change |
|---|---|---|
| `97be89bc66139eb45526a04af59a35dccc006eb9` | `LOG.md:1989-2024` (round 29, ledger at `:2015`) | claims freeze, C2 frozen counter, C3 counter, baseline + control receipts |
| `190052c923c6968a3d4a292eb1330938a7cb10b4` | same | C3 receipt + bytes, S108–S115, summary knowledge entry, 7 recheck notes |
| `59e8167aa5a4399e4115e7253fa0bab5e8dd773d` | same | C1 repair + mutation receipt, C2 SCORECARD corrections, SKILL gate rows |
| `35045d7d9f6cf0bbdc4c734881ab77b48deedb81` | same | LOG round-29 entry + LOG.md:221 correction |
| `32008a453737a27f69e9ab401d0b9775d2a944f7` | same | S094 nonce normalisation, S045 note, receipt provenance |
| `e1e3a15f2db10c135739e0ee7e81ce63a02facf6` | same | wave-1 evidence, lesson round-29, QUALITY 71–73, README frontier |
| `9cc92b0880a104551a32369f8f59bf4af9d0959e` | same | 23 wave-2 refetch records, knowledge errata |
| `ab080992491fd2d8b9b6768cd522cf8d89e23ed6` | same | wave-2 evidence, SCORECARD round-29 disposition |
| `dcfb7a3c2f5556a820ca48b5d06e4bd37a3e9e6d` | same | final measurements at ab080992 |
| `2cb31aa60521cd0a67b10e96e9f48121a0e2b722` | same (the ledger itself) | LOG commit ledger |
| `f36caf6a12faa14e33ff27efabe09f7d6c1324df` | same | C2/C3 re-measured at the ledger tip |

Each line above is the helper's `landed <hash>` output. All landings went through `scripts/hyaku/jj-lane.sh commit … --as tabi`. The lane is clean: `jj-lane.sh state` → `ahead=0 behind=0 tracked=0 untracked=0`.

## Before → after measurements

All after-measurements ran in a clean `git clone --shared` checkout (porcelain 0). Raw outputs are under `.ufo/waves/round-29/measure/`.

| Claim | Counting command | Before (rev 856fa9e) | After | Measured at |
|---|---|---|---|---|
| C1 operability | `node scripts/check-s106-evidence.mjs --selftest; echo exit=$?` | exit=1, `ReferenceError: existsSync is not defined`, no tally | `S106_SELFTEST verdict=clean cases=7 passed=7`, exit=0. Both revision case ids present. Mutant without the revision comparison: `measured-revision-bytes-mismatch … FAIL`, `verdict=failed cases=7 passed=6`. `--rev … --json` gives `"valid": true` | `ab080992491fd2d8b9b6768cd522cf8d89e23ed6` (`measure/c1-*`) |
| C2 calibration | `node scripts/check-selfassessment.mjs --rev <REV> --json` (frozen sha256 `728128008e2242b635bda30a28313de20b06d381d7855f11f18fa5043ba560c4`) | `mismatches=6` (`baseline/c2-before-frozen-counter-cleanbase.json.txt`) | `mismatches=0`, `counted=[]` | `ab080992…` and `2cb31aa60521cd0a67b10e96e9f48121a0e2b722` (`measure/c2-*`) |
| C3 freshness | `node scripts/check-release-pins.mjs --rev <REV> --stable 156.0.8078.47 --json` (sha256 `567637200b05eaf6c4ca750294b6ddc30ce64417c336fe135ab625f8c6fc3770`) | `population=23 resolved=0 unresolved=23`, exit 1 (`baseline/c3-before.json`) | `population=23 resolved=23 unresolved=0 holds=16 drifted=7`, exit 0 | `ab080992…` and `2cb31aa6…` (`measure/c3-*`) |

Lane-side verdicts:

- C1: **met**.
- C2: **met**.
- C3: **met on the frozen counter, with disclosed counter weaknesses.** The independent re-fetch evidence for the actual data is in `w2/Refetch*.md`.

Non-author admission is the closure's call. Score deltas recorded in `SCORECARD.md:1468-1501`: operability 8→8, calibration 9→9, freshness 8→9. There is no exploratory claim.

## Sources & frontier

Census command (the CORPUS.md manual census reads the same registry):

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi
```

- **Before** (`.ufo/waves/round-29/baseline/census-start.txt`, sha256 `603360be…e750`): 16 `W04` duplicate-URL warnings, S058 … S100.
  Final lines: `tabi	ok	/home/vgpnk/Projects/shokunin/tabi-shokunin/corpus/SOURCES.md` and `exit=0`.
- **After** (`.ufo/waves/round-29/measure/census-end.txt`, sha256 `9dbb9173…6cead`): the same 16 W04 lines plus two more.
  The two additions: `tabi	W04	S114 duplicate url chromium.googlesource.com/chromium/src/+/refs/tags/156.0.8078.47/third_party/blink/renderer/core/html/forms/html_form_element.cc?format=TEXT across scopes` and the same line for `S115`.
  Final lines: `tabi	ok	…/corpus/SOURCES.md` and `exit=0`.
- Byte-exact captures are the committed files themselves (criterion 72). Note: `baseline/census-start.txt` reproduces only at the 856fa9e tree.

Registry totals:

- **Rows**: 107 → 115. Command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` at `856fa9e` and `ab080992`.
- **Tier**: A=92 B=6 C=9 → A=100 B=6 C=9. Added this round: 8 rows, all tier A — S108 (dataset; Chromium Dash Stable feed) and S109–S115 (code; 156-tag supersessions).
- **Status**: mined=79 queued=19 rejected=9 → mined=87 queued=19 rejected=9.
- **Rows touched old→new**: none. No `status`, `recheck` or `used-by` cell of an existing row changed.
- **Re-opened at both tags**: S033 S034 S041 S042 S045 S062 S064 S071 S074 S077 S078 S079 S080 S081 S093 S094 S096 S097 S098 S099 S100 S105 S106.
  Every new row carries a URL, access date and a ≤25-word located quote in `corpus/lessons/round-29.md` §Gate.

Frontier:

- Advanced: "On-release source freshness (Chromium tag pins)" is held at 156.0.8078.47.
- Opened: "Runtime behaviour on a 156 build" (`corpus/README.md:619-630`).

Frontier step:

- Sourced claim: C3 rests on S108, opened this round.
- Mistakes mined: M1–M5 in `corpus/lessons/round-29.md`. M1, M2 and M4 had no criterion that would have caught them; they now become QUALITY 71–73, and M3 reinforces existing criteria 65/70.
- Assimilation: **none**. No `merge/tabi/` adoption this round; the round-27 L0 question on S114/S140 stays open and was routed around. Lane rows S114/S115 are unrelated to the package ids.
- considerthese/: the directory is absent in the tabi lane.

## Trend verdicts

- **expansion: improved.** One admitted knowledge entry (`corpus/knowledge/chromium-156-release-pin-recheck.md`) on ground the coverage map did not hold: the Chromium 156 source state, including the new post-fill detached-document failure arm. It cites mined rows S108–S115, and the coverage map gains a new row (`corpus/README.md:619-630`).
- **quality: improved.** 23 stale-due rows were re-verified at the new release. The 7 entries citing a drifted row, and the S045 contract change, are marked with appended notes. Wave-2 accuracy defects were corrected by errata. Re-fetch reproduced 44/46 files byte-identically, and the 2 S094 404 bodies match after nonce normalisation. No admitted entry fails its re-check unmarked.
- **discernment: improved.** The round-28 outside spot-check's routed disagreements became lessons M1–M3 with grounded QUALITY criteria 71/72. This round's own counter over-reach (M4) became criterion 73. The outside spot-check of this round's admits/rejects is owed to the closure.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:697`, `:1598-1617`; round-29 gate rows `SKILL.md:2532-2545`; no non-author verifier named.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `corpus/knowledge/multi-step-journey.md` §1–§2, §7 (LOG round-3 entry); this round, a source-level end-to-end recheck is logged at `LOG.md:1989-2024`.
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/executor-test-sufficiency.md` §0, §4. This round 23 lane-dispatched seats executed the per-row recheck procedure from the item text alone (`w1/Pin*.md`), but they are not non-author.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:3-19`. The wave-1 adjacency scan `w1/ConnSiblings.md` absorbed nothing.

## Extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (L1 and every seat report checked; e.g. `w2/RefetchS078.md` "No tools installed or updated"). pacman untouched.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows untracked `baseline-plain.txt` (kasegi capture-binding output), `.ufo/waves/round-34/` (another lane) and `.ufo/state/*`. None was written by a tabi seat, so there are no misroots and nothing was moved.
- Scratch: `/fast/scratch/hyaku/tabi-r29` removed by the L1 (1.6 GB, including the 8 seat dirs named above). The uncommitted duplicate wave-1 fetch bytes under `w1/pins/*/bytes` were deleted; they are identical to the committed evidence bytes.
- Earlier attempts: none (`.ufo/watchdog.log` has no `lane-dead-no-report tabi round=29`).
- L0 questions: none new. The open question `tabi | round-27` (S114/S140 quarantine vs. frozen claim) is unchanged and was routed around.
