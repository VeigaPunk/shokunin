# kaika W3 — non-author review: kengaku round 24

Reviewer: W3ReviewKengaku (orchestrator-dispatched). Not on the round-24 dispatch roster: `grep -rn W3ReviewKengaku .ufo/prompts/` in the fleet-ledger worktree → no match.
Subject: lane `kaika/round` head `06872d4`; round commits `94da19e` (round work) and `06872d4` (after-receipt). Base `99cf615ca`. Report: `fleet-ledger/.ufo/reports/round-24/kengaku.md` (cites `94da19e`/`06872d4`).

Incidents (disclosed): (a) an early `curl -o S0xx.html` ran with cwd = fleet root (`cd` did not take effect); 11 untracked files written at 19:28, deleted by me; `git -C /home/vgpnk/Projects/shokunin status --short` empty afterwards. (b) `/tmp/kaika-verify/kengaku` vanished once mid-review (cause unknown); recreated, and every number below was re-run after recreation on fresh `git archive` copies.

## Recommendation

**RETURN — do not admit round 24 as landed.** Provenance, append-only, credential sweep, and the counts all reproduce. Blocking: F1 (fleet validator exits 1, check 4). Required before admission: F1–F5. C2 should not be admitted as a calibration axis-move (see §3).

## 1. Provenance — PASS

`git -C <lane> log --format='%h %an <%ae> | %cn <%ce> | %s' 99cf615ca..06872d4db` → 2 commits, `94da19e` and `06872d4`, both author and committer `kengaku-shokunin <kengaku@shokunin.local>`.

## 2. Append-only — PASS (0 deletions in append-only paths)

- `git -C <lane> diff -U0 99cf615ca 06872d4db -- LOG.md corpus/lessons corpus/QUALITY.md corpus/SOURCES.md | grep -cE '^-[^-]'` → `0`.
- `git -C <lane> diff --diff-filter=D --name-only 99cf615ca 06872d4db` → empty (no file deleted, incl. `corpus/knowledge`).
- Only non-additive change in the range: `SCORECARD.md` placeholder row `-| — none yet — | | | |` (one line). SCORECARD is not in the append-only list; benign.
- `corpus/SOURCES.md` is new this round; no in-place edits to prior rows exist to audit.

## 3. Claims — per-claim verdicts (commands and outputs)

Counts were re-run with the lane's `plans/round24_census.sh` (sha of the file in the after tree) on fresh archives of `99cf615ca` (base; v2 script copied in) and `06872d4db` (after). Output matches the committed receipts `corpus/evidence/round24-census/base-99cf615.txt` and `after.txt` line-for-line (receipt header differs only in `HEAD`).

| key | report before→after | re-run base | re-run after | verdict |
|---|---|---|---|---|
| C1.expansion_entries_on_mined_rows | 0→5 | 0 | 5 | verified |
| C1.full_triad_knowledge | 0→5 | 0 | 5 | verified |
| C1.knowledge_unindexed | 3→0 | 3 | 0 | verified |
| C1.lessons_unindexed_excl_round24 | 5→0 | 5 | 0 | verified |
| C1.root_logs_indexed | 0/28→28/28 | 0/28 | 28/28 | verified |
| C1.plans_indexed | 0/8→10/10 | 0/8 | 10/10 | verified |
| C1.dead_index_rows / dead_plans_rows | 0/0→0/0 | 0 / 0 | 0 / 0 | verified |
| C1.coverage_map_rows | 11→16 | 11 | 16 | verified |
| C1.frontier_rows | 0→5 | 0 | 5 | verified |
| C1.province_map_sections | 0→4 | 0 | 4 | verified |
| C1.sources_rows | absent→25 | absent | 25 | verified |
| C1.knowledge_files | 27→32 | 27 | 32 | verified |
| C1 contract census (SOURCES-CONTRACT-v1 l.66–80, my `contract-census.sh` on `06872d4` archive) | malformed 0; A=24 C=1; mined=18 queued=5 rejected=2; dup/enum/mined-path empty | — | rows 25, malformed 0, tiers A=24 C=1, statuses mined=18 queued=5 rejected=2, all three checks empty | verified |
| C2.lesson_mistake_rows | absent→20 | absent | 20 | verified |
| C2.closure_criteria_citing_round24 | absent→10 | absent | 10 | verified |
| C2.round23_sections (LOG SCORECARD) | 0 0→1 1 | 0 0 | 1 1 | verified |
| C2.round23_not_admitted_with_fail_quote | 0→1 | 0 | 1 | verified |
| C2.saturation_declared | 0→1 | 0 | 1 | verified |
| C2.capability_rows | 0→3 | 0 | 3 | verified (see F8) |
| C2.scorecard_state_defects_open | 6/6→0/6 | 6/6 | 0/6 | verified as a presence check only (see F9) |

Claim verdicts:
- **C1 coverage (7→7, held by cap) + capability `sources-registry`.** Counts: verified. Capability: **not-verified as landed** — the pre-registered condition is "every contract census command runs clean" (claims Amendment 7), and the contract commands do; but the fleet validator required by this review (check 4) exits 1 (F1). Verified once F1 is fixed. Coverage held at 7: agree (cap).
- **C2 calibration (8→8, held).** Counts: verified. Axis-move: **not-verified**. The lane's own report and critic record C2 as bookkeeping; the score is held; the state census is presence-based. Recommend the operator rule C2 as counts-without-axis-move, not as a calibration admission.
- No exploratory claim is declared.

## 4. SOURCES

- Check 4 (must exit 0): `bash …/fleet-census/scripts/sources-census.sh validate <lane>` → **exit 1**. Output: `25 E08` and `21 E09`; no E01–E07, E10, E11, W-codes.
  - E09 (real, registry-cell defect): recheck cell `2027-01-17 (90d)` on S001–S004, S007–S013, S015–S022 (19 rows); `each round` on S024, S025. Contract `SOURCES-CONTRACT-v1.md:38–39`: recheck is "ISO date or cadence (`90d`, `180d`, `on-release`)". Rule 2 allows recheck changes in place, logged old→new in the round lesson.
  - E08 (tool false positive, see F13): with `TZ=UTC` the 25 E08 disappear; the 21 E09 remain (exit still 1).
- Re-opened rows (≥3 required; I re-opened 20 web rows; table below). For each: `sha256sum` of a fresh fetch vs the `gate.md` receipt, and grep/reader for the quote.

| row | tier / scope | sha vs receipt | quote check |
|---|---|---|---|
| S001 | A paper | match | abstract: "no detection method is consistently reliable across contamination tiers, model-access settings, and training stages" — present |
| S002 | A paper | match | abstract: "even a brief Group Relative Policy Optimization (GRPO) training can markedly conceal contamination signals" — present; Fig. 2 caption: "simply after 156 steps" — present |
| S003 | A (rejected) | match | §Limitations: "the current DCR framework is not yet adaptable to generative tasks such as machine translation and summarization" — present |
| S004 | A paper | match | abstract "contamination-resistant, i.e., unlearnable, but support inference" — present |
| S005 | A docs (self-report) | **mismatch** (dynamic page; 0568df0b vs 8bd40cbc) | reader text: "at least 59.4% of the audited problems have flawed test cases…" — present |
| S006 | A docs (self-report) | **mismatch** (e3052697 vs fba4c005; raw HTML lacks text) | reader text: "we retract our earlier recommendation to adopt SWE-Bench Pro" — present |
| S007 | A paper | match | "Hiding test data does not appear to prevent saturation once benchmarks are widely adopted" §4.1 — present; "Of the 60 benchmarks analyzed, 29 exhibit high or very high saturation" §4.1 — present |
| S008 | A paper | match | abstract "we provide eight key recommendations" — present |
| S009 | A paper | match | "rubric order bias, score ID bias, and reference answer score bias" — present; "~45–48%" — see F3 |
| S010 | A paper | match | reader text §1: "rubric ordering alone flips the top-1 candidate on 15% to 41% of prompts" — present; abstract "some judges favor the first option, while others favor the last" — present |
| S011 | A proceedings | match | abstract "remains unbiased under distribution shift between the test and calibration datasets" — present |
| S012 | A canonical | match | §3.3 "we found all of them exhibit strong position bias" — present; "cannot pass the more advanced 'repetitive list' attack" — present in §3.3 (not Abstract; F2b) |
| S013 | A paper | match | abstract "the time humans typically take to complete tasks that AI models can complete with 50% success rate" — present |
| S014 | A dataset | match | header "This page is no longer actively updated." — present; FAQ "a measure of the difficulty of a task, rather than the time an AI spends" — present; "Measurements above 16 hrs are unreliable" — present |
| S015 | A paper | match | §4.2 "we therefore recommend using the paired version of the standard error estimate wherever practicable" — present |
| S016 | A paper | match | abstract "not all models give deterministic answers, even when setting temperature to zero with a fixed random seed" — present |
| S017 | A proceedings | match | abstract "accounting for both of them is necessary to avoid substantially underestimating the overall variability" — present |
| S018 | A paper | match | §1 "is a statistical claim about the gap, not the gap itself" — present; §6.4 "14 subject categories as natural clusters" — present |
| S019 | A paper | match | §3.2 / App. B "ad-hoc without-replacement variants can fail to yield valid coverage" — present |
| S023 | C (rejected) | **mismatch** (bf62b2cd vs ee510e84; dynamic page) | reader text: "We use code that models haven't been trained on." — present |
| S024 | A own-work | local | `git show 99cf615ca:grader.py` → sha `90c87c88…ae941f` (= receipt); line 2 and line 5664 (`def main(argv=None):`) match the row |
| S025 | A own-work | local | `git show 99cf615ca:corpus/evidence/attrib-r23-stream.log` → sha `afaae9dd…` (= receipt); line 239 matches the quote exactly |

Hash matches: 17 of 20 web rows reproduce `gate.md` exactly; the 3 mismatches are dynamic OpenAI/Scale pages (F10).

- **Rejected row S023** — the teaches cell (`corpus/SOURCES.md:45`) and the search-log entry (`:62`) say the lab audit "contradicts" the contamination-resistance claim. The cited S006 measures task validity (broken tasks) and says nothing about training exposure. See F4.

## 5. Discernment spot-check (`LEARNING.md`)

| sample | gate decision | what I checked | non-author verdict | reason |
|---|---|---|---|---|
| `corpus/knowledge/llm-judge-calibration.md` | admit | triad (l.1–3); tiers S009–S012 all A; S010 §1 and S011 abstract quotes verbatim; S012 canonical labelled; "What this does not establish" present; "Rejected" present | **agree (admit)** | Admission holds. Two location slips (F2b) and one unreproduced figure (F3) must be fixed; they do not reverse the admit. |
| S003 (DCR factor) | reject | Limitations quote verbatim (§Sx1); "excluding frontier-scale systems" and 72B limit present; flip condition concrete | **agree (reject)** | The rejection is grounded in the paper's own limitations. |
| S023 (Scale SWE-Bench Pro blog) | reject | tier C / vendor blog: verdict to keep it out of evidence holds; **stated reason does not**: S006 is about broken tasks, not training exposure | **disagree (reason)** | Keep the rejection, correct the reason via a new row (F4). Per LEARNING, convert this into a grounded QUALITY criterion (e.g. a rejection must cite a source that addresses the claim's scope). |

## 6. Per-axis verdicts (recommended; lane values from the report)

| axis | lane | recommended | basis |
|---|---|---|---|
| novelty | 7→7 unchanged | unchanged — agree | no probe ran this round (SCORECARD round 24) |
| calibration | 8→8 held | held — agree | C2 is bookkeeping, not an axis-move (§3) |
| depth | 9→9 held | held — agree | +2 SKILL.md lines (a pointer), no new decision rule |
| coverage | 7→7 held by cap | held — agree | counts moved and reproduce; cap stands per lane's PROVINCE §Historical (I did not independently re-test route-telemetry absence) |
| operability | 8→8 held | held — agree | `grader.py` on `06872d4` archive → `CHECKS n=733 mismatches=0 errata_pinned=1`, `VERDICT: PASS`; `freeze-check` → `block_sha=1b2d6a01bfa431ec … -> OK` |
| freshness | 8→8 held | held — agree | 17/20 web hashes reproduce; PROVINCE core `test -e` paths resolve (grader.py, plans/attrib_probe.py, frozen tables, QUALITY.md, SOURCES.md, round evidence dirs) |
| adjacency | 8→8 held | held — agree | report-outs named; not independently verified |

## 7. Trend verdicts (LEARNING.md vocabulary)

- **Expansion: improved.** `C1.expansion_entries_on_mined_rows` 0→5 (§3); knowledge files 27→32. The five topics were absent from the base coverage map (`git show 99cf615ca:corpus/README.md` coverage map has no contamination, judge-calibration, saturation, or paired-statistics row; time-horizon extends the existing planning-horizon row, which the entry says). Coverage rows 11→16 (`corpus/README.md:208–212`).
- **Quality: unchanged (pending F2–F3).** No admitted entry is false on my re-check; 17 of 20 re-fetched sources match their receipts; quotes are present. But four location slips and one unreproduced figure sit in admitted entries and are unmarked. The LEARNING "improved" trigger needs them corrected.
- **Discernment: unchanged (becomes harmed if F4 is not learned).** One admit agreed, S003 reject agreed, S023 reject disagreed on reason. LEARNING: a disagreement must become a lesson with a grounded QUALITY criterion; none exists yet.

## 8. Report (check 8)

Sections present, in §4 order: Work performed; Landed changes; Before → after measurements; SHONEN; then Sources & frontier, Mistakes, Trend verdicts, L0 questions, Integrator notes (plus Verdicts and Adjacency). Cites `94da19e`/`06872d4`. No `[x]` boxes (SHONEN all `[~]`). Overstatement: §Verdicts/Trend line "No admitted entry fails its re-check (7 agree, 1 location disagree, fixed)" — my re-check finds more location errors and one unreproduced figure (F2–F3). Pointer drift: report line 43 cites `SCORECARD.md:569` (the round-23 header, correct); lesson `round-24.md` M14 and the round-23 disposition cite `SCORECARD.md:567` (blank line; F6).

## 9. Defects by severity

**High (blocks admission)**
- **F1 — registry fails fleet validator.** `sources-census.sh validate` → exit 1 (21 E09). Fix: change the 21 recheck cells to a valid form (`90d`, `180d`, `on-release`, or ISO date) in place; log old→new in `corpus/lessons/round-24.md` `## Gate` (contract rule 2).

**Medium**
- **F2 — quote-location errors in admitted entries (Q3).**
  - (a) `corpus/knowledge/contamination-detection-and-transparency.md` "RL post-training hides contamination": "Table 2 shows reference-free AUROCs falling to near 50% after 156 GRPO steps" — that statement is the S002 Figure 2 caption (§3.1, `S3.F2`), not Table 2. Fix to "Figure 2".
  - (b) `corpus/knowledge/llm-judge-calibration.md` "canonical study set": attributes "cannot pass the more advanced 'repetitive list' attack" to "Abstract" — it is S012 §3.3. Fix location.
  - (c) same contamination entry, "CoT contamination…": "S002, §4: 'almost all the detection approaches consistently perform near random guess…'" — the sentence is S002 §1 (Introduction, Stage II paragraph). Fix location.
  - (d) `corpus/knowledge/agent-time-horizon-and-task-validity.md`: the S005 "at least 59.4%…" quote is listed under "Too narrow and too wide tests"; it is from the intro's numbered list. Fix location.
- **F3 — unreproduced figure.** `llm-judge-calibration.md`: "§4.2 Table 3 shows flip rates up to ~45–48% under the Ref-5 perturbation." In S009 HTML the Ref-5 values in the first numeric column are 35.40–45.54 (`grep` hits at lines 698–902); "48" appears only in an unlabelled 4th column. Restate with the exact cell and column header, or narrow to "up to ~45.5%".
- **F4 — rejected-row reason is a non-sequitur (Q8).** `corpus/SOURCES.md:45` (S023 teaches) and `:62` (search log): "contradicts"/"contradicted by" the OpenAI S006 audit. S006 reports task validity (~30% broken tasks), not training-data exposure, so it does not contradict S023's contamination-resistance claim. Verdict (tier C, vendor) stands; the reason must change. The teaches cell is committed, so correct it with a new row whose teaches opens `supersedes S023 —` (contract rule 2).
- **F5 — overstated self-verdict.** Report "no admitted entry fails its re-check" and the Gate's "Q1–Q8 pass" should name F2–F3 as open or fixed.

**Low**
- **F6 — stale pointer.** `corpus/lessons/round-24.md` M14 and "Round 23 disposition" cite `SCORECARD.md:567`; the round-23 header is at `SCORECARD.md:569`.
- **F7 — tier A for S025.** `corpus/SOURCES.md:47` gives tier A as "the lane's own re-runnable gate output"; S025 is a recorded live-run log (needs an endpoint to re-run). No admitted entry cites it (used-by `—`), so no admitted claim is affected. Downgrade to B or justify.
- **F8 — capability rows.** `SCORECARD.md:556` records `frozen-table-pin-check` via `freeze-check`; Amendment 7 (`plans/round-24-claims.md:131–134`) pre-registered `block-sha`. Both rows are re-demonstrations (first-working rounds 10 and 21), not acquisitions this round; `C2.capability_rows 0→3` measures table filling.
- **F9 — presence-based state census.** `plans/round24_census.sh:65–73` checks that headings or strings exist (e.g. `grep -qE '^- \*\*D14 errata'`); `0/6` does not show SCORECARD matches repo state. The report already concedes this.
- **F10 — receipts not byte-reproducible for dynamic pages.** S005 `0568df0b…` ≠ `8bd40cbc…`; S006 `e3052697…` ≠ `fba4c054…`; S023 `bf62b2cd…` ≠ `ee510e84…`. Add an access-time capture caveat to `corpus/evidence/round24-sources/gate.md`.
- **F11 — missing qualifier.** `llm-judge-calibration.md`: "S010: extremes n=2 and n=9 carry the highest Cramér's V." S010 says this holds on 5 of 6 judges; GPT-OSS-20B peaks at n=5 (Table 4: 0.080). Add the qualifier.
- **F12 — extends target is new.** `paired-eval-uncertainty-reporting.md` "Extends the README 'Statistical reporting' coverage row": that row is created this round (`corpus/README.md:212`); it was not on the base coverage map.
- **F13 — tool defect (outside lane), filed to `xd://report_issue`.** `sources-census.sh validate` flags `opened == today` as E08 when the local TZ is not UTC: default (−03) → 25 E08; `TZ=UTC` → 0; `--today 2026-10-20` → 0. Root cause in `epoch()` (tool lines 328–333, 380–381) not isolated.
- **F14 — benign.** SCORECARD placeholder row removed (see §2).

## 10. L0 / Integrator notes

- Operator ruling needed: is C2 (counts, score held 8→8, presence-based census) admissible as an axis-move? Recommend no.
- Operator ruling needed: C1's `sources-registry` capability: must the fleet validator exit 0 (my check 4 says yes) or only the contract census commands (lane's reading)?
- Integrator: fleet validator E08 false positive (F13) should be fixed before the next round's registry validation.

## 11. Verification gaps (not verified)

- L2 prompts (the `/skill:godspeed` + directive-bytes requirement) are not in the repo; not checked.
- `PROTOCOL.md` / `PROTOCOL-APPENDIX.md` not reviewed beyond the rules cited above.
- S020–S022 (queued leads, not used) not re-opened.
- S006/S023 quotes checked via reader text only (raw re-fetch differs).
- `grader.py` exit code not captured separately (the verdict line `PASS` was captured through a pipe).
- Route-telemetry absence and the other PROVINCE §Historical rows not independently re-tested.
