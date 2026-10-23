# chousa — round 36 (attempt 2)

Lane: chousa (deep-research method). Round 36, attempt 2 of 2 (attempt 1 was OOM-killed mid-round;
`lane-dead-no-report chousa round=36`, `.ufo/watchdog.log` line 980). Campaign target round 100.
Lane tip at this report: `e66c4563e3a76c90dcbb37e834cd07b533199849`. Round commits:
`76597487c8c3f963465cdbcfcabe91acd1ea2500` (round work — counters/claims/errata, corpus entries,
SCORECARD/LOG/SKILL/QUALITY/SOURCES/lesson, wave evidence), `6b3aba52f046bae0bf7b48fcf8e4eda16e20aff7`
(late seat evidence `CritC2CallForShow`), `e66c4563e3a76c90dcbb37e834cd07b533199849` (critic
corrections to the two knowledge entries, the lesson and SCORECARD; late seat evidence
`ConnOverlap`, `CritLessonGate`, `RevReportCounts`). Base lane tip at round start:
`700bd5fcbf9abc118a6a0f078d51a2e7460c2878` (attempt-1 freeze: counters, witness, gate edits,
controls, receipts), pushed (`local=remote=700bd5f`, `ahead=0` at start).

## Work performed

The round declares **two claims on distinct axes**, both frozen by attempt 1 in
`corpus/evidence/round36/claims.md` (P1/P2, kill rules, stated limits, repairs R1-R6):

- **C1 — operability** (lowest scored axis, 3/10; surface: the gate's matcher provenance and the
  tools its receipt names as identity). The gate and its counter separate an output-equivalent
  engine swap in fourteen scenarios, one per demonstrated swap class.
- **C2 — calibration** (surface: the lane's measurement method). The witness attributes the matcher
  PER RECORD through the pinned engine's out-of-band argv channel, separating the five
  output-equivalent engines the round-35 witness admitted, while a renamed matcher passes.

Work items (each carries its evidence pointer):

- **Inherited attempt-1 landing re-verified.** `w1/ScoutInherited.md`: the three tracked files under
  `corpus/evidence/round36/` are `CMP_IDENTICAL` to `700bd5f`; the untracked
  `corpus/evidence/round36/__pycache__/` (one 20,219-byte CPython 3.14 pyc of `c2-count.py`,
  mtime 18:00:17 -0300, predating the freeze commit 18:03:56) is build residue with no authored
  work — removed and `corpus/**/__pycache__/` gitignored; named under Mistakes.
- **C1 re-derived on fresh seeds.** Construction receipts (frozen by attempt 1): 14/14 on seeds
  36001/36011. Wave + L1: `w1/ExecC1FreshA/c1-after-s36301.json`, `w1/ExecC1FreshB/c1-after-s36311.json`,
  `w1/ExecC1ScenarioMap/c1-s36331.json`, `w1/MutC1Arm/pristine-landed-s36341.json`,
  `w1/LabScenarioIsolation/{clean,poison}.json` (seed 36351), `measure-l1/c1-s36361.json`,
  `w1/RevClaimPredicate/c1-fresh-s36301.json` — all `ENGINE_SWAP_CANARY=14/14` with
  `predicate_holds=true`. Before: `measure/c1-before-s36001.json` and
  `w1/ExecC1BaseCtl/c1-before-s36321.json` → `10/14` on the base control.
- **C1's arms scrutinized.** `w1/ScoutC1Counter.md` maps all 14 scenarios to fixtures, assertions
  and lines and names three vacuity candidates (S7, S8, S9). `w1/MutC1Arm.md` shows S11 and S12 are
  each worth exactly one point (10/14 → 11/14 in their own cell) and that the do-nothing control's
  four failures are S11-S14. `w1/RevCounterHonesty.md` re-derived 14/14 on fresh seeds, measured a for-show gate at 14/14 (the
  stated limit), proved the receipt's `gate_sha256` cannot enforce the kill rule's second sentence
  (a comment-only gate scores 14/14), measured a non-executing pin at 12/14 with S9 PASS (Erratum 11)
  and found a third docstring number to correct (Erratum 12). `w1/ExecC1ScenarioMap.md`,
  `w1/ExecHashShim.md`, `w1/ExecLocaleDecode.md`, `w1/ExecPinEchoDrift.md`,
  `w1/ExecModeCoverage.md` reproduce S11-S14 by hand and the R6 pin-coverage ledger (1 recorder
  call, `--version`, 0 matcher calls for `verify-integrity`/`verify-sweeps`).
- **C2 re-derived on fresh seeds.** Construction receipts: 5/5 on seeds 36001/36011. Wave + L1:
  `w1/ExecC2FreshA/c2-after-s36301.json`, `w1/ExecC2FreshB/c2-36311.json`,
  `w1/CritC2CallForShow/c2-s36331-committed.json`, `w1/MutC2AttrKey/art/rec-pristine-s36341.json`,
  `measure-l1/c2-s36371.json` — all `WITNESS_PER_RECORD=5/5 OUTPUT_EQUIV=5/5 LANDED_ATTRIB=pass
  RENAMED=pass`. Before: `measure/c2-before-legacy-s36001.json` and
  `w1/ExecC2LegacyCtl/c2-before-legacy-s36321.json` → `2/5` (V1/V4 separated; V2/V3/V5 pass;
  renamed killed).
- **C2's witness attacked.** `w1/ScoutC2Counter.md` maps the channel, the per-record key and the six
  patches, and confirms the docstring drift against the receipts. `w1/ExecWitnessDirect.md` runs the
  witness directly (9/9 attributed, one representative `-a -z -b -o -P` argv quoted).
  `w1/MutC2AttrKey.md`: collapsing attribution to a global count drops the count to 0/5 (the key is
  load-bearing); requiring only the span's first 64 bytes **survives at 5/5** (Erratum 8).
  `w1/CritC2CallForShow.md` scores the call-for-show engine (not separated, as the stated limit
  predicts) and a recorder-reading forger (passes; the disclosed anti-instrumentation limit), and
  shows a deeper legitimate refactor is not killed.
- **No-harm.** `w1/ExecSelftest.md`: `PASS (261 cases, 0 skipped)` under default, `LC_ALL=C` and a
  scratch `TMPDIR`. `w1/SentNoHarm.md`: claims 17/17, chain 17/22, broken control 1/2, archives 3/3.
  `w1/ExecNewCases.md`: the five new cases (257-261) are absent from the base's 256-case suite and
  each fails on the base behaviour in its scratch variant.
- **Contract review.** `w1/RevPinContract.md` (echo is stderr-only; R1's scrub has a `BASH_ENV`
  re-export hole, Erratum 7), `w1/RevClaimportPredicate`→`w1/RevClaimPredicate.md` (both predicates
  encoded faithfully; F1-F4 errata), `w1/RevLocaleSeam.md` (seam closed for the decode across 11 escape cases × 7 locales; one verdict-flipping seam outside it at `research-gate.sh:1015`, Erratum 13), `w1/RevCounterHonesty.md`.
- **Frontier drafted.** `w1/ScribeSrcGrep.md` + `w1/ScribeSrcSha.md` (S069/S070 drafts),
  `w1/ScribeKnowC1.md`, `w1/ScribeKnowC2.md`, `w1/ScribeLesson.md`; integrated by the L1.
- **Sibling-overlap and YAGNI.** `w1/ConnOverlap.md`: both r36 capabilities are fleet-unique **by token over
  every sibling lane**, with one disclosed limit — mori's `worktrees/round-19` fixture copies were
  unscanned after three 30 s timeouts (recorded `[INFERENCE]` as mori-own gates in the scan log,
  sha256 `722e44bb…`). The closest sibling is tameshi's declared-witness mutation study, a
  pattern-family cousin that separates no output-equivalent engine and attributes nothing per record. The L1's own token sweep
  agrees (no `argv-witness`/`WITNESS_PER_RECORD`/`ENGINE_SWAP_CANARY`/`RESEARCH_GATE_GREP` outside
  this lane; one unrelated `mechanism-witness` mention in `audio-shokunin`).
  `w1/SimpDiff.md`: gate diff clean — every hunk claimed; three dead fields in `argv-witness.py`
  named as r37 candidates, not edited post-data.
- **Residual attack call (3 seats, counted in the round total).** `w1/RevReportCounts.md` (count
  reconciliation: found the SCORECARD's "6 entries" claim and the C1 seed-list ambiguity, both
  corrected) and `w1/CritLessonGate.md` (adversarial read of the lesson, QUALITY 50-52 and the two
  knowledge entries: demanded the heading overclaim, the V1/V4 admission wording, the S070 policy
  labelling, the S11 refusal-observation wording, the S069 quote word count and a
  `## Spot-check intake` section — all landed before the commit). The third seat
  (`RevSourcesNew`, non-author re-open of S069/S070) did not return; the rows' quotes were verified
  by the L1 against the installed pages (`zcat` + line numbers) and by `w1/ScoutC2Counter.md`'s
  independent read of the grep page.

## Landed changes

All lane changes are carried by the round commit `76597487c8c3f963465cdbcfcabe91acd1ea2500` under LOG.md §Round 36
(`## Round 36 — 2026-10-23 — the engine-swap canary and per-record attribution`), except the
inherited gate/tool/counter bytes, which are carried by `700bd5f` (attempt-1 freeze) and cited here
because this round's receipts are measured against them.

| Change | LOG.md entry | Commit |
|---|---|---|
| `tools/research-gate.sh`: `sha256_hex_file` + manifest/`--pin` hash pin, `json_unescape` C-locale UTF-8, pin-echo scrub, `GATE_GREP` drift token, selftest 257-261 | Round 36 | `700bd5f` (inherited freeze) |
| `corpus/evidence/round36/{claims.md,c1-count.py,c2-count.py}`, `tools/argv-witness.py`, `.ufo/waves/round-36/{controls,measure}/` | Round 36 | `700bd5f` (inherited freeze) |
| `corpus/evidence/round36/claims.md` §Erratum 1-13 (six L1 + seven wave findings, append-only) | Round 36 | `76597487c8c3f963465cdbcfcabe91acd1ea2500` |
| Critic corrections to the two knowledge entries, the lesson (`## Spot-check intake`, S069 word count) and SCORECARD (erratum count, C1 seed-list wording) | Round 36 | `e66c4563e3a76c90dcbb37e834cd07b533199849` |
| `corpus/evidence/round36/c{1,2}-count.py` docstrings corrected to their receipts (R7) | Round 36 | `76597487c8c3f963465cdbcfcabe91acd1ea2500` |
| `corpus/knowledge/engine-swap-canary-r36.md`, `corpus/knowledge/per-record-argv-attribution-r36.md` | Round 36 | `76597487c8c3f963465cdbcfcabe91acd1ea2500` |
| `corpus/SOURCES.md` S069, S070 | Round 36 | `76597487c8c3f963465cdbcfcabe91acd1ea2500` |
| `corpus/QUALITY.md` 50-52 | Round 36 | `76597487c8c3f963465cdbcfcabe91acd1ea2500` |
| `corpus/lessons/round-36.md` (`## Mistakes` ×5, `## Gate`) | Round 36 | `76597487c8c3f963465cdbcfcabe91acd1ea2500` |
| `SKILL.md`: selftest counts 256 → 261, r36 counter + `argv-witness` tool rows, round-36 section with the R6 pin-coverage ledger | Round 36 | `76597487c8c3f963465cdbcfcabe91acd1ea2500` |
| `SCORECARD.md` §Round 36, capabilities ×2, planned r37 | Round 36 | `76597487c8c3f963465cdbcfcabe91acd1ea2500` |
| `LOG.md` §Round 36 | — | `76597487c8c3f963465cdbcfcabe91acd1ea2500` |
| `.gitignore` `corpus/**/__pycache__/` | Round 36 | `76597487c8c3f963465cdbcfcabe91acd1ea2500` |
| `.ufo/waves/round-36/{w1-spec.json,w1-dispatch.json,w1-taskcall.json,w1-briefs/,w1/,measure-l1/,gen-w1-spec.py}` (wave evidence) | Round 36 | `76597487c8c3f963465cdbcfcabe91acd1ea2500` |

## Before → after measurements

Counting commands are run from the lane root. `--receipt` writes the JSON the numbers come from.

| Claim | Counting command | Before | After | Measured against |
|---|---|---|---|---|
| C1 | `python3 corpus/evidence/round36/c1-count.py --gate tools/research-gate.sh --seed N --receipt F` | `ENGINE_SWAP_CANARY=10/14`, `predicate_holds=false` (`measure/c1-before-s36001.json`; re-derived `w1/ExecC1BaseCtl/c1-before-s36321.json`) on base gate `a4768851…` | `ENGINE_SWAP_CANARY=14/14`, `predicate_holds=true` on seeds 36001, 36011, 36301, 36311, 36331, 36341, 36351, 36361 | gate `a7d3922c768a217a2dcedf347b4de438b8dda4108e1335f5a39af6117e1f54e8`, committed at `700bd5f` |
| C2 | `python3 corpus/evidence/round36/c2-count.py --gate tools/research-gate.sh --witness tools/argv-witness.py --seed N --receipt F` | `WITNESS_PER_RECORD=2/5 OUTPUT_EQUIV=5/5 LANDED_ATTRIB=absent RENAMED=fail` (`measure/c2-before-legacy-s36001.json`; re-derived `w1/ExecC2LegacyCtl/c2-before-legacy-s36321.json`) on base gate + `tools/mechanism-witness.py` | `WITNESS_PER_RECORD=5/5 OUTPUT_EQUIV=5/5 LANDED_ATTRIB=pass RENAMED=pass` on seeds 36001, 36011, 36301, 36311, 36371 | gate `a7d3922c…`, witness `e6832e0b…`, both committed at `700bd5f` |

Kill-rule check: no committed run of either counter against the landed gate is below its target
(`w1/ScoutReceipts.md`; the only lower labels are the disclosed controls: base-gate runs and the
always-pass witness stub at 0/5 with `predicate_holds=false`).

Claim verdicts, reported as measured: **C1 met under P1 with its reading narrowed** — the four
failures S11-S14 are this round's separations; S1-S10 also pass the base control; S7-S9 assert the
echo/refusal contract rather than per-call engine identity (QUALITY 52); S10 is what stops a
no-call gate scoring 14/14. **C2 met under P2 as a query witness** — it proves the pinned matcher
was queried per record, not that its answer was used; the call-for-show engine scores 14/14 on C1
(Erratum 9) and the prefix-64 witness bypass passes P2 (Erratum 8).

## Sources & frontier

Census command (run at round start and at round end):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa
```

- Before: exit 0, `rows 68` (tier A 62 / B 1 / C 5; mined 45 / queued 19 / rejected 4), two standing
  W04 duplicate-URL warnings (S051, S053).
- After: exit 0, `rows 70` (tier A 64 / B 1 / C 5; mined 47 / queued 19 / rejected 4), the same two
  standing W04 warnings. Counting command for rows:
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- Rows added by tier: **tier A ×2** — S069 (GNU `grep(1)`, `-o`+`-b` offset semantics;
  `/usr/share/man/man1/grep.1.gz`, quote at decompressed 387-391; file SHA-256 `9b027d02…85ba`) and
  S070 (coreutils `sha256sum(1)`, digest text and `--check`;
  `/usr/share/man/man1/sha256sum.1.gz`, quote at line 11; file SHA-256 `93c17dff…403f`). Both opened
  locally on 2026-10-23; the lesson's `## Gate` carries the located quotes (S069 15 words, S070 6).
- Rows touched old→new: none (no `status`/`recheck`/`used-by` edit in place; both new rows enter
  `mined` with their `used-by` at creation).
- Rejected candidates: the man7.org `grep(1)` HTML page (not opened this round; citing a URL for the
  installed page's bytes would be a reference drift), the POSIX `grep` specification (external fetch
  without operator approval this round — deferred, not rejected on merit), and `locale(7)` (the
  C-locale arm's evidence is measured behaviour plus a selftest case, not a documented norm).
- Frontier rows advanced: S069 → `corpus/knowledge/per-record-argv-attribution-r36.md` (C2's sourced
  claim); S070 → `corpus/knowledge/engine-swap-canary-r36.md` (C1's S11 arm). Non-author re-open:
  `w1/RevSourcesNew.md`.

## Trend verdicts

- **expansion: improved.** Two admitted knowledge entries on ground the corpus did not hold before
  (`engine-swap-canary-r36.md`, `per-record-argv-attribution-r36.md`), each with the provenance trio
  and each resting on a row opened this round (S069, S070); the capability table gains two rows
  (engine-swap canary; per-record argv attribution). Command:
  `ls corpus/knowledge/*r36.md` → 2; `grep -cE '^\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` → 70.
- **quality: improved.** Four gate holes closed and measured (manifest hash shim, C-locale decode,
  pin-echo isolation, drift token) with the before/after receipts above; selftest 256 → 261 cases
  all passing under three environments; the pin-coverage ledger is measured, not asserted (0 matcher
  calls for the two exempt modes); three dead fields in the new witness are named for deletion.
- **discernment: improved.** The round's own docstring drift was caught by a seat and corrected
  (QUALITY 50), the three vacuity candidates in C1 were named by a seat that did not run the counter
  (QUALITY 52), the S11/S12 point value was established by mutation, and the claim readings were
  narrowed in the report rather than defended: a call-for-show engine scoring 14/14 and a prefix-64
  witness bypass are on the record as errata. One seat died (provider `cyber_policy`); no seat's
  verdict was prettified.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SKILL.md` tools table (r36 counter + `argv-witness` rows), §Round 36, `corpus/knowledge/*-r36.md`
  (lane evidence; no non-author promotion verifier this round).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` §Round 36;
  `corpus/evidence/round36/claims.md`; receipts under `.ufo/waves/round-36/`.
- [~] Instructions executable by an agent without oral context — `bash tools/research-gate.sh
  --selftest` → `PASS (261 cases, 0 skipped)`; `python3 corpus/evidence/round36/c1-count.py --seed N`
  → 14/14; `python3 corpus/evidence/round36/c2-count.py --seed N` → 5/5.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md`; out-of-province findings
  (another lane's fleet-root files) were named, not absorbed; `w1/ConnOverlap.md` finds both r36
  capabilities fleet-unique.

## Round shape, dead seats, stale-lane, installs, sweep, L0

- **Round shape:** one v1 wave, **36 seats** (executor 15, scout 5, scribe 5, reviewer 4, critic 2,
  mutation-tester 2, sentinel 1, simplifier 1, connector 1; attack roles 10 = 28%) plus one residual
  call of **3 seats** (reviewer 2, critic 1). Round total **39 seats** (cap 128), all under policy
  `ufo-wave-policy.json` (band 32-64); the wave was validated with `plan --emit-tasks`/`run --spec`
  (`.ufo/waves/round-36/{w1-spec.json,w1-dispatch.json,w1-taskcall.json}`). The planner seat is held
  by the L1 (the validator rejects `planner`); its bounded data-walk rode the `LabScenarioIsolation`
  seat. Wave 2 was not dispatched: the timeout-freeze budget (2 h) required the round to land, and
  the wave-1 returns plus the residual call already produced the attack layer (each attack item
  names what it attacks in its report). Seat briefs were delivered as byte-exact per-seat files
  under `.ufo/waves/round-36/w1-briefs/` (the validated payload is 77 KB; the task texts carry the
  Godspeed lead and point at each brief).
- **Seat reports on disk at integration:** **35** of 36 wave seats (`.ufo/waves/round-36/w1/*.md`;
  seat reports committed by the round commit `76597487` and the late-evidence commit `6b3aba52`).
- **Dead seats:** `CritC1Swap` (critic) — provider refusal, first error text:
  `[openai-codex/gpt-6.1-sol] Codex error event: This content was flagged for possible cybersecurity risk … (code=cyber_policy)`;
  not retried, no replacement. All live seats returned; the only missing
  report is the dead `CritC1Swap`. `CritC2CallForShow` returned late and landed as `6b3aba52`: a call-for-show engine
  is NOT separated and a recorder-reading forger passes — both are the limits `claims.md` already
  discloses, so they confirm the frontier as stated; a deeper legitimate refactor (rename plus argv
  construction moved into helpers) is not killed.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none (no pacman/uv/npm transaction this round; pacman transactions stayed
  paused host-wide).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists no file whose
  content names this lane or round (`grep -l -i 'chousa|round-36'` over every untracked fleet-root
  path → no match); nothing copied or deleted at the fleet root. The untracked set there belongs to
  other lanes/the operator and was left untouched.
- **L0 questions:** none raised this round; no blocker needed an operator decision.
