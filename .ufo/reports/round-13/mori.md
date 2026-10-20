# mori — round 13 (attempt 1), 2026-10-20

Lane repository: `/home/vgpnk/Projects/shokunin/mori-shokunin`. Unprefixed repository paths below refer to that lane; `evidence/…` abbreviates its `.ufo/waves/round-13/evidence/…`. This report is the fleet-repository artifact.

## Work performed

Exactly two declared, causally separable claims:

1. **C1 — coverage / capability acquisition:** independently scoped, boot-anchored, MESSAGE-free journal record counters. Explicit scoped surfaces **0 → 2**; independent live source-counter comparison **12/12**. Sources S013/S014/S015/S035/S036. Evidence: lane `SCORECARD.md` round-13 section; `.ufo/waves/round-13/evidence/live-measurement.json`.
2. **C2 — operability:** repair long-history exact-author loss (audit F01) and final-verdict acceptance (F02). Named demonstrated defects **2 → 0**; honest oracle remains **28/28**; BANANA **28/28 accepted → 0/28 rejected**. Evidence: `corpus/knowledge/verdict-contract-r13.md`; frozen-before and accepted-after receipts below.

Both owned axes entered at 6, satisfying the lowest-owned-axis duty. The old planned freshness re-pin is not claimed. The plan's “five kernel records” was explicitly corrected: those prior-boot `--grep` samples match MESSAGE internally and cannot satisfy structured-count criterion Q15. C1 advances only FR1's notice/result plane; kernel victim-token attribution and fleet correlation remain frontier.

- Replaced journal text classifiers with six field-matched classes in separate `journal.user` / `journal.system` rows; validated current boot, per-query timeout, stderr-aware unavailable states, client-supplied-field labels, and `oomd_activity=unmeasured`. Preserved the supported user SIGKILL warning through structured process-result metadata; arbitrary unreported signal paths are explicitly unmeasured. `tools/mori-census.sh::probe_journal`, commit `18d7d55`.
- Repaired F01 using captured history and whole-line author membership; cleared inherited repository overrides in grading and disabled fsmonitor for its file scan. `tools/mori-census.sh::grade_lane`, `18d7d55`.
- Repaired F02 across all normal, shape-invariance and read-only cases: terminal, unique, complete roll; CLEAN/0/zero-drift and DRIFT/1/positive-drift agreement. `tools/mori-silence-cases.sh::verdict_grade`, `18d7d55`.
- Landed the reproducible fixture/wrapper harness, pinned original scripts, source openings, lessons, Q26–Q28 and append-only corrections distinguishing MESSAGE matching from MESSAGE-free output. `corpus/lessons/round-13.md`; `corpus/knowledge/*-r13.md`; `.ufo/waves/round-13/frozen/inputs.json`.
- Preserved two red integration runs. The new harness initially misparsed `severity=... obs=...`; fixing that exposed a zero-arm expectation mistakenly reused for the user-positive fixture. These were harness defects, not production regressions; corrected in `80bd58a` and `c13df48`. Raw failures remain in `evidence/regressions-after/` and `regressions-after-final/`.
- Ran one validated **32-seat wave**, then L1 integration verification after implementation deliveries. Registry and unchanged dispatch payload: lane `.ufo/waves/round-13/{spec.json,dispatch.json,build/swarm-registry.json}`. Role mix: 8 executor, 8 scout, 4 connector, 5 reviewer, 3 critic, 2 scribe, 1 sentinel, 1 revenger. L1 held the canonical planner seat; PlanningWalk scout performed its bounded data-walk. No model parameter or routing mutation.

## Landed changes

**Pushed lane HEAD: `2e576474707c4936ecd9d9baca64e2f1085aded2`.** Lane work was committed and pushed before this report was written; the post-push lane status was clean after removing L1's generated Python cache.

All changes belong to `LOG.md`'s **Round 13 — structured journal scopes and verdict-contract repair** entry and its appended measured corrections:

| Commit | Landed work | LOG linkage |
|---|---|---|
| `18d7d55` | census/oracle repairs, harness, wave/frozen evidence, source/quality/frontier integration | round-13 declared claims and integration-review decisions |
| `80bd58a` | producer-schema parser correction, pure schema test and first red evidence | “L1 integrated check at 18d7d55” |
| `c13df48` | exact nonzero-fixture FINDING expectations; second red evidence | “The corrected parser exposed one further harness-only expectation defect” |
| `2e57647` | accepted measurements, live/security/tamper evidence, final scorecard/capabilities, source census and lesson closure | “Final accepted measurement at c13df48” and following paragraphs |

No inherited dirty lane work existed at entry. Non-author `round-12-verifier-spotcheck.md` and historical lessons were not rewritten. SHONEN's transient indentation mistake was caught and restored to its entering canonical bytes; no box was checked.

## Before → after measurements

Commands below run from `/home/vgpnk/Projects/shokunin/mori-shokunin`. Production measurements bind to **`c13df48`**, census SHA-256 `39abda0a67028575d888d9157b8548dec0b4944c3d8c165691e88ab657fc3985`, oracle SHA-256 `34cd5770889ec6e7521b477aa9976cece7a64e07b83774c12ce2aea73161abfa`. Frozen target inputs come from entering commit `6531ac6`; their digests are checked before execution. The before harness revision is `80bd58a`; all harness corrections are disclosed above.

### C1 — coverage: improved, 6 → 7

```sh
jq '[.result.baseline.stdout,.result.delivered.stdout] | map(split("\n") | map(select(startswith("SURFACE journal."))) | length)' .ufo/waves/round-13/evidence/live-measurement.json
# [0, 2] ; exit 0
```

The live artifact contains the exact executable Python reproducer, source-query argv, full frozen/delivered censuses and bracketing counters: **12/12** class/scope cells matched. All cells were zero in current boot `430d3038185949e682cf5fc475d1b3d0`; this is not an observed new kill, an active/healthy oomd claim, or proof of complete journal access. Five C1 behavioral checks separately verify system positives 2/1/3/3, user zeros, user-only positives 3/0/1/1, canary exclusion, and scoped-row/CLEAN behavior.

The local score rubric retains entering 6 and adds one point only with two delivered scoped surfaces, all five C1 checks and 12/12 live parity. `SCORECARD.md` records the rubric, command and revision. FR1 attribution/correlation is deliberately not claimed.

### C2 — operability: improved, 6 → 7

```sh
jq -s '[.[] | [.claims[] | select(.id == "R13_F01_EXACT_AUTHOR_LONG_HISTORY" or .id == "R13_F02_REJECT_BANANA") | select(.status == "expected-defect" or .status == "fail")] | length]' .ufo/waves/round-13/evidence/regressions-before-final/evidence.json .ufo/waves/round-13/evidence/regressions-accepted/evidence.json
# [2, 0] ; exit 0
```

Behavioral counting commands actually run:

```sh
python3 tools/mori-round13-regressions.py --baseline --jobs 1 --output .ufo/waves/round-13/evidence/regressions-before-final
# 19 assertions: baseline-control=1 baseline-ok=4 baseline-rejected=3 expected-defect=11; exit 0
python3 tools/mori-round13-regressions.py --mutation both --jobs 1 --output .ufo/waves/round-13/evidence/regressions-accepted
# 19 passing contract checks + 2 mutation-red witnesses; exit 0
```

The harness calls assertion ids “claims”; these are **not** extra round claims. F01 subject-first history changed row-C → row-A, while the 12,000-sibling control stayed row-C. Reverting only grade_lane reproduced the old 12,001-record wrong grade. Honest oracle stayed 28/28. BANANA, missing, duplicate, trailer and verdict-first proxies each scored 0/28 after repair; selective tally/rc proxies correctly retained their unaffected 7 or 21 cases, but never a green suite. Reverting only verdict validation restored BANANA 28/28. Arbitrary finding-total corruption and aggregate/registry-count vacuity remain open portions of audit D02, not claimed fixed.

The score adds one point to entering 6 only when both named defects disappear, honest/control cases hold and both exact-locus negative witnesses reproduce the old failure.

### Exercised guards, costs and axis verdicts

- `bash -n` on census and oracle: exit 0. Census `--selftest`: **91/91**, exit 0 at `18d7d55` (same production SHA); the seat's predicted 87 was wrong and remains labeled a prediction. Harness `--selftest`: **24/24**, exit 0. Evidence: `evidence/{syntax-census,syntax-oracle,census-selftest,regression-selftest-final}.json`.
- Synthetic 440,000-byte stderr and malformed JSON: expected unavailable classes, no hang or fake-payload output; fixture pin also contains no canary. Copied frozen-input tamper: exit 2, `snapshot_tampered`. Exact stub/generator/hash and observations: `evidence/security-probes.json`, `security-fixture-pin.txt`, `snapshot-tamper-witness/evidence.json`.
- One interleaved full-census pair: **3.025310 s old / 2.960516 s new**; not a distribution or speedup claim. Honest fixture oracle: **1.881 s / 3.132 s**. Twelve journal producers each have a local 2-second bound plus 1-second kill grace; this is not a whole-census bound and no budget was retuned.
- Live roll: `DRIFT (findings=20 drift=12 unavailable=1 surfaces=8)`, versus old `19/12/1/7`; tmux unavailable is not unhealthy. R10 drift compare still exits 1. Its 42 tokens are classified as intentional journal schema, carried r12 roster schema, or explicitly inferred live-state families; no regression-free proof or re-pin is claimed (`evidence/drift-retained-baseline.json`, `drift-classification.json`).

| Axis | Verdict | Score / evidence |
|---|---|---|
| coverage | improved | 6 → 7; C1 |
| operability | improved | 6 → 7; C2 |
| depth | unchanged | 5 held; no independent claim |
| freshness | unchanged | 5 held; old red baseline retained |
| calibration | unchanged | 5 held; honors round-12 outside correction |
| adjacency | unchanged | 6 held; no sibling ownership or actuation absorbed |

No harmed axis was identified by the exercised checks; costs, retired unreliable text semantics and remaining blind paths are disclosed rather than equated with universal no-regression proof. Independent non-author admission/closure is still required.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin mori`; before and after exit 0. Retained complete outputs: lane `.ufo/waves/round-13/sources-before.json` and `sources-after.json`.

| Metric | Before | After |
|---|---:|---:|
| Rows | 34 | 36 |
| Tier A / B / C | 31 / 2 / 1 | 33 / 2 / 1 |
| Mined / queued / rejected | 12 / 21 / 1 | 15 / 20 / 1 |

Required validation command, both times:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori
```

Before output, exit **0**:
```text
mori	ok	/home/vgpnk/Projects/shokunin/mori-shokunin/corpus/SOURCES.md
```
After output, exit **0**:
```text
mori	W04	S035 duplicate url raw.githubusercontent.com/systemd/systemd/cf8ebfc6159cf0b3b99aa9a0164ccb07c4c9c5af/catalog/systemd.catalog.in across scopes
mori	ok	/home/vgpnk/Projects/shokunin/mori-shokunin/corpus/SOURCES.md
```

W04 is informational, not an enum/shape failure: immutable S013's old scope was not rewritten when newly opened process-result scope S035 was added. Added **2 tier-A code rows**, S035 catalog process-exit/unit-result scope and S036 primary emitter; no B/C rows added. Existing changes: S013/S014/S015 used-by gain the new journal note; S031 queued → mined and `—` → the verdict note; no recheck changes. Full old→new values, access dates and located ≤25-word quotes are in `corpus/lessons/round-13.md` Gate.

FR1's structured system-journal notice/result plane advances; kernel victim-token attribution, signal sender/cause and fleet correlation remain frontier. Kernel `--grep` samples are explicitly marked historical text selection in appended corrections, not silently retained as a structured capability. FR11 cursor rotation/vacuum remains unknown. Mistakes M1–M8 include F01/F02, prior outside-score/seed corrections, the inherited roster-override residual and this round's two harness errors.

## Trend verdicts

- **expansion: improved** — demonstrated dual-scope journal capability and the FR1 notice/result-plane coverage entry; `SCORECARD.md` round-13 capabilities, source-linked `structured-journal-scopes-r13.md`, live 12/12 receipt.
- **quality: improved** — F01/F02 repairs verify; weaker text selection is superseded by structured records, and historical MESSAGE-matching overclaims are marked with append-only errata. Negative and red harness evidence is preserved, not prettified.
- **discernment: improved** — the prior named non-author W3ReviewMori correction is converted into lesson-backed Q28 and a failing indented-seed witness. This is learning from the prior outside review, **not** calling this wave's own seats independent. Round-13 admit/reject spot-check remains pending.

## SHONEN

The file remains four unchecked boxes, canonical bytes verified by the harness. These are author assertions only; no promotion or non-author `[x]` is claimed.

- [~] Decision tables, error patterns, checklists and cited sources — `SKILL.md`; `corpus/SOURCES.md`; `structured-journal-scopes-r13.md`.
- [~] End-to-end domain task executed/logged — `LOG.md` round 13 C1 live domain task; `evidence/live-measurement.json`.
- [~] Instructions executable without oral context — `tools/mori-round13-regressions.py`, its 19 passing checks and retained reproducer/argv; residuals explicitly named in the knowledge notes.
- [~] No cross-domain bleed — `PROVINCE.md` Core/Frontier/Adjacent; detection/report only. Tsukuroi retains OS diagnosis, kumitate orchestration/collection, operator host actuation. No sibling files or domain source trees were changed.

Stale-lane: respawn-per-round assignment; this mori round progressed through lane-authored commits, and no other mori round mission is open in this assignment. This is not a fleet-wide liveness verdict. No daemon restart, steer, dispatch-policy change or remediation occurred.

Open L0 questions added: **none**. Remaining limits are recorded, not blocked on an answer: client-set IDs, duplicate records, fail-closed array values, silent partial-store access, kernel-token attribution, unvalidated roster overrides and oracle tally/aggregate weaknesses.

Tool install: **core/man-pages 6.19-1**, official `sudo pacman -S --needed --noconfirm man-pages` channel, installed by PipeSource to inspect authoritative local pipe(7). No other installs/updates reported. Temporary fixture trees and the L1-generated Python cache were removed; no uncommitted lane work remained before report creation.
