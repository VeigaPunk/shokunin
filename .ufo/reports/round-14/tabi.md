# tabi — round 14 (hyaku, attempt 1)

## Work performed

Declared claims: **C1 operability** — newly verified non-shell SCORECARD counting paths0→2, preserving legitimate historical tree-path/content counts; **C2 calibration** — digest-bound qualified historical metadata correction0→1, without new browser execution. Operability8 is a lowest non-retired tie. Neither claim is exploratory; every ordinal scalar delta is0. The prior planned coverage item is explicitly carried forward, not claimed completed: the independent round13 cleanup/counting defects motivated this round instead.

**Pushed lane HEAD:** `5c7710d7393112f2163dd7efcaa38fccf534dfc2`. Baseline: `bebe2efc4565bb068efd905e9ef78011bb6b4efd`. The lane push succeeded and `git status --short` was empty before this report was created.

- Replaced both gates' authored-shell count execution with closed, quote-aware parsing and argv-based Git reads. Historical forms are `git ls-tree … | grep BRE [| grep BRE] | wc -l` and the fixture's `git grep -h … REV -- PATH | wc -l`; they are not all blob counts. BRE dot semantics/no-match0 remain; unsupported commands and missing revisions fail closed. Exact code/control bindings: `tabi-shokunin/corpus/evidence/round-14/gates.json`; code commits `ed69b15` and `f942c62`.
- Exercised real supported, refusal/no-marker and same-command old/new controls. ROUND selftest32 fixtures+alias; USER29 fixtures+alias, six committed-row count controls and a count-witness differential all passed. Pinned old gates accept/produce the isolated marker; repaired gates reject `score_mismatch` without it. Historical-policy witnesses remain separate and passed. Full command outputs: `tabi-shokunin/corpus/evidence/round-14/executions/roundSelfTest.json`, `userSelfTest.json`, `roundHistoryWitness.json`, `userHistoryWitness.json`.
- Preserved the production boundary: final committed-input ROUND clean10 exit0; USER remains exit1 `round_count`, “Found 6 user rounds, expected 10”. USER stops before its counting step; its parser evidence is the controls, not a production-green claim. Final input revision `20b72b9bdad30578ad1ef438527642c46dc79c68`; `tabi-shokunin/corpus/evidence/round-14/final-production.json`.
- Added a failure-capable historical ARIA metadata checker, persisted fixture expectations and qualified sidecar. Complete worker/source identities support corrected listeningAfter=false; observed Node26.12.0 is distinct from descriptive24.21.0 and minimumMajor20. The sidecar states browserExecuted=false/exactMatch=false. Original producer/note/receipt/pin remain unchanged. Evidence: `tabi-shokunin/corpus/evidence/round-14/aria-metadata/verification.json`, `corrected.json`; checker repair `e570380`.
- Retained actual failures: initial metadata checker wrongly required nonexistent cleanup.workers and read the wrong derived Node property; its two failures were repaired without changing expected truths. Initial C2 counting then failed on positional selftest tokens and named-finding formatting; only that consumer was corrected. Evidence: `tabi-shokunin/corpus/evidence/round-14/executions/metadata*.json`, `measure-c2-initial.json`; repairs `e570380` and `0c5567e`.
- Learned the previous non-author findings into QUALITY18/19 and the new lesson. A proposed producer edit/note append was withdrawn before commit because it would break round13's source/note digest checks; the corrected semantics instead live in new evidence/SKILL/lesson. All six routed items have dispositions, including explicit retained debt. Evidence: `tabi-shokunin/corpus/lessons/round-14.md`, `SKILL.md:1717-1762`, `corpus/QUALITY.md:54-64`, `LOG.md:700-826`.
- Dispatched one validated, unchanged32-seat taskCall; L1 held the canonical planner seat and PlanningDataWalk supplied bounded reconnaissance. Roles: executor4/scout7/connector4/reviewer7/critic4/sentinel2/revenger2/scribe2. Session role overrides chose models; no model parameter or routing changes. Absolute seat paths and lane-relative Report trailers were bound in context. Evidence: `tabi-shokunin/.ufo/waves/round-14/w1/{spec,dispatch,swarm-registry}.json` and32 seat reports.

Stale-lane: respawn-per-round mission; this is the only tabi mission, no other mission of this lane is open. Initial lane worktree was clean; no inherited lane-authored leftovers were reused/discarded. The existing non-author round13 verifier lesson was read-only. Only this lane and this fleet report were written; no sibling gate was executed.

Cross-domain boundary: this is maintenance of tabi's own browser evidence and legacy lane gates, not generic security/testing ownership. Publishing remains kake-owned, credentials kagi-owned, forensics revenger/kaidoku-owned. Current frozen step1/step4 closure-checker certification remains protocol/operator debt; this author report does not supply it. Git configuration/PATH/environment/hooks/replace-ref/alias trust, r07 survivor replay, user-record freezing, IPv6 origin classification and the unpinned external validator remain uncredited. Deliberate legacy-witness arms still execute pinned old gates in isolated scratch; the claim is not “the entire lane never uses shell”.

## Landed changes

Every row is tied to the round14 LOG entry (`tabi-shokunin/LOG.md:700-826`). All commits below are ancestors of pushed HEAD; no history was amended.

| Commit | Landed work / LOG linkage |
|---|---|
| `ed69b15` | Both non-shell historical counters, initial revision probe and motivating LOG declaration |
| `f942c62` | Metadata checker, digest-bound corrected sidecar and persisted fixture expectations |
| `6be0990` | First actual execution receipts: counter passes, original metadata failures; gates.json and LOG |
| `e570380` | Targeted real-schema/Node-property repair and diagnostic LOG explanation |
| `4a300f6` | Single first-add round14 lesson; sourced registry/docs/QUALITY; complete validated swarm and corrected metadata receipts |
| `4844f6c` | Preserved failed C2 counting observation and LOG routing |
| `0c5567e` | Consumer parses actual key/value output and unambiguous structured findings; own report/LOG |
| `20b72b9` | SCORECARD per-axis verdicts, final measurements, unchanged scalars and LOG |
| `5c7710d7393112f2163dd7efcaa38fccf534dfc2` | Final committed-input production/census receipts and LOG; pushed before report |

The frozen round14 lesson was committed once. Later measurement/production records were added only to LOG/SCORECARD/evidence, preserving USER's future-lesson immutability policy. Historical inputs/baselines/census were not moved. USER explicitly archives known intermediate ROUND digests while requiring the exact current cutover at HEAD; no blanket checker exemption was added.

## Before → after measurements

Actual command/stdout/stderr/exits, code revision and counter identity are retained in `tabi-shokunin/corpus/evidence/round-14/measurements.json`. The final counter is committed at `0c5567e8a2b57fc64d5526f830941e2304cd2c35`; its C1 logic is unchanged from the earlier passing C1 measurement. Counts are bounded artifacts/policies, not expertise percentages.

| Claim | Counting command | Before | After | Self-verdict |
|---|---|---|---|---|
| C1 operability | `node .ufo/waves/round-14/measure.mjs REV --claim C1` from lane root | baseline `bebe2efc4565bb068efd905e9ef78011bb6b4efd`:0, exit0 | evidence `6be099015ca347eab36c62f30551eab919c2ce5c`:2, exit0; both committed code digests/real controls verified | improved; operability8→8 |
| C2 calibration | `node .ufo/waves/round-14/measure.mjs REV --claim C2` from lane root | same baseline:0, exit0 | `0c5567e8a2b57fc64d5526f830941e2304cd2c35`:1, exit0; original_pinned1, lesson_admitted1, browser_executed0 | improved; calibration9→9 |

C1/C2 --claim modes read disjoint evidence. C2's initial counting failure did not suppress C1=2. C1 counts verified counter cutovers, not two newly clean full production gates. C2 counts one corrected original receipt/pin pair, not a browser run or a correction of every failed/intermediate receipt.

Checker demonstration at `e570380d77180ab394256dd6187cac0c5eaf62ec`:

- `node scripts/check-aria-metadata.mjs --self-test`: exit0,16 cases.
- `--witness`: exit0, same checker red→clean, original_unchanged=true.
- `--check corpus/evidence/round-13/aria/receipt.json`: exit1, only `R14-ARIA-CLEANUP-LISTENING-AFTER-01`.
- `--check corpus/evidence/round-14/aria-metadata/corrected.json`: exit0,27 findings/zero failures, accepted=true.
- Actual `--derive RECEIPT PIN --out corrected.json`: exit0, wrote=false/identical=true; no original overwrite.

The registered current gate entry names the corrected sidecar; no-argument/raw checking deliberately retains the original contradiction as red. No browser was launched this round. Source selftest26/live29 and freshness --worktree34/34 were exercised clean. The main sweep ran after seat handoff; only failed/repaired targets were rerun, plus production/census against newly committed lesson/SCORECARD inputs. One critic ran bounded read-only historical counting probes mid-flight despite skip-check instructions; no seat executed the actual gate/selftest/browser suite. Tools installed/updated this round: **none**.

## Sources & frontier

`corpus/SOURCES.md` rows28→29; tiers A22→23/B4→4/C2→2; statuses mined23→24/queued3→3/rejected2→2. Added by tier A1/B0/C0: **S029**, own-work scoped to exact historical worker cleanup/Node fields. Source path opened2026-10-20: `corpus/evidence/round-13/aria/receipt.json` at `837b33a3988ebeea7f6b4ef5c04698da88909a73`; located quote at cleanup.server.perWorker[0].listeningAfter: `"listeningAfter": false`. Its date, quote and all transitions are recorded in the round14 lesson Gate. C2 cites this mined row.

No pre-existing row cells change. S029 status nonexistent→mined; recheck nonexistent→on-change→365d (unsupported cadence caught before commit); used-by nonexistent→lesson, briefly lesson+old runtime note, then back to lesson-only to preserve the old note's digest. No new knowledge note/capability or source-row-driven expansion is claimed. Preamble “all rows opened round1” is explicitly qualified to original S001–S028.

Existing sources reopened: [S023 Locators](https://playwright.dev/docs/locators) §Locate by role, “role locators do not replace accessibility audits and conformance tests”; [S024 Snapshot testing](https://playwright.dev/docs/aria-snapshots) §Aria snapshots, “A template is a constraint, not necessarily a complete serialization of the accessibility tree.” These preserve scope, not new runtime support. Bounded reopening identified5/screened5/included3/excluded2; pin/producer were supporting inputs, excluded as separate rows. Exact enumeration/counting command: `tabi-shokunin/corpus/evidence/round-14/source-reopening-count.json`.

Revision histogram/count command:

```sh
node .ufo/waves/round-14/measure.mjs REV --histogram
```

Baseline `bebe2ef` and after `4a300f676e4f9731402d85f409895fb1123aee4a` both exit0. Knowledge notes/map stay32/32, missing[]. Exact full output is in measurements.json.

Required census command at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi
```

Start output, exit0 (`tabi-shokunin/.ufo/waves/round-14/before.json`):

```text
tabi	ok	/home/vgpnk/Projects/shokunin/tabi-shokunin/corpus/SOURCES.md
```

End output, exit0 on committed input `20b72b9` (`tabi-shokunin/corpus/evidence/round-14/final-production.json`; earlier end receipt also retained):

```text
tabi	ok	/home/vgpnk/Projects/shokunin/tabi-shokunin/corpus/SOURCES.md
```

Frontier rows advanced: none. Extension↔daemon handshake, native WebMCP, real-site rate/rights, real-site journeys and WebMCP mining remain open. Accessible selectors remain narrowly runtime-held by the round13 fixture; this correction does not renew its execution date. The lesson mines the prior outside aggregate/version/count-authority mistakes into QUALITY18/19 with actual red controls and retained failed executions.

Open L0: existing tabi round5 external-action approval and round1 namespace/dispatch wording questions remain open and untouched. No new question. The later campaign ruling places planner with L1; it does not silently answer the older namespace question.

## Trend verdicts

| Trend | Self-verdict | Evidence / boundary |
|---|---|---|
| expansion | unchanged |32/32 notes/map; no new domain ground, knowledge entry, runtime experiment or capability; S029 is curation, not expansion |
| quality | improved | Held metadata gets a checked digest-bound qualification; runnable counters reject executable authored grammar; actual failures retained and repaired without changing true expectations; historical source/note pins preserved |
| discernment | improved | Prior non-author routed defects become grounded QUALITY18/19 and failure-capable controls; all six routed items dispositioned in lesson. Current-round external admit/reject agreement remains pending; no author-side seat is called non-author |

All-axis verdicts: depth unchanged8→8; coverage unchanged9→9; operability improved8→8; freshness unchanged8→8; calibration improved9→9; adjacency unchanged8→8. No owned axis harm is claimed. This is the author's measured case for admission, **not independent closure/admission**. No scalar, promotion or SHONEN certification is inferred. Saturation8/window3 retained; round14 is position1 since the round13 capability, not a restart.

## SHONEN

- [~] Real decision tables, error patterns, checklists and cited sources: `tabi-shokunin/SKILL.md` Runbook/Evidence ladder and round14 metadata table/registry; `corpus/QUALITY.md:54-64`. Author assertion only; no named non-author certification.
- [~] End-to-end domain task executed/logged: historical real browser experiment `tabi-shokunin/corpus/evidence/round-13/aria-execution-pass.json`, `aria/receipt.json`, LOG round13; round14 qualifies metadata, does not reexecute it.
- [~] Instructions executable without oral context: `tabi-shokunin/corpus/knowledge/executor-test-sufficiency.md`, SKILL runbook and committed round14 CLI/control receipts. Prior executor was lane-dispatched; no new independent cold-execution certification.
- [~] No cross-domain bleed: unchanged `tabi-shokunin/PROVINCE.md:3-19`, explicit boundaries above, own-lane code/evidence only. Non-author promotion review remains external; no `[x]` or rank change.
