# kama — round 10 report (kaika campaign, 2026-10-19)

Lane commit: **`1e41928`** (`kama-shokunin`, branch `kaika/round`, worktree `.tower/worktrees/kaika/kama-shokunin`, base `35e9175`). Steered round 10 = the 2026-10-18 plan `kama-shokunin/.ufo/round-10/plan.json`, which was never dispatched. Collision check was clean: no `round-10/kama.md` existed at the fleet root or in the ledger worktree, and the lane `LOG.md` had no round-10 entry. Axis authority is `MISSION.md:29` (operability + freshness). This prompt's §1 says "operability + calibration"; the mission file wins, the same G5 conflict recorded at `LOG.md:273-280`.

## Work performed

Declared claims (2):
- **C1 — freshness** (lowest LIVE axis; the plan's declared claim 1). Stale source anchors in existing corpus files are re-anchored by appended, dated corrections. Dated history is not rewritten.
- **C3 — capability acquisition `sources-registry`, per-axis verdict on coverage.** Adds `corpus/SOURCES.md` under contract v1 and admits 3 knowledge entries on uncovered ground.
- Plan claim 2 ("refresh the gate evidence bundle" as operability) is **closed, not claimed**. Re-running unchanged gates re-verifies state; it does not move operability (`corpus/lessons/round-10.md` §Closed plan claim). The critic independently reached the same verdict.

Work items:
- L2 swarm: 12 seats in one batched `task` call — planner, connector, 4 executors, scribe, 2 scouts, reviewer, critic, sentinel. Every prompt led with `/skill:godspeed` plus the verbatim `directive.md` bytes, and no model was passed. The C1 executor stalled when its route ran out of quota (the orchestrator's 22:01 UTC note: `m_swe` "Reached free model rate limit"). I killed it and dispatched a fresh executor (`KamaExecAnchors2`) with the same file set. I also dispatched one follow-up pin scout. Transcripts are under `history://W2RoundKama.*`.
- C1 ledger: `.ufo/round-10/audit/stale-anchors.tsv`, 50 rows (42 active, 8 historical). Each row has a correction appended under `## Corrections — round 10 (2026-10-19)` at the end of its file, across 12 files.
- C3 registry: `corpus/SOURCES.md`, with 30 rows, `## Paths` (4), `## Search log` (3 notes) and `## Leads (unopened)`.
- C3 entries: `corpus/knowledge/runtime-health-surface-matrix.md`, `corpus/knowledge/serving-metrics-crosswalk.md` and `corpus/knowledge/gguf-runtime-compatibility-boundary.md`. Each opens with `source:` (S-rows + URL + §anchor), `verified-at:` and `recheck:`.
- Quality bar: KQ6–KQ10 appended to `corpus/QUALITY.md` §Criteria added — round 10. Each cites its lesson.
- Lesson `corpus/lessons/round-10.md` holds §Mistakes (24 rows), §Gate (URL, access date and ≤25-word quote for all 30 rows), §Admissions, §Rejected, §Corrections, §Closed plan claim, §Contested L1 gate runs and §Review record.
- Index: an appended `corpus/README.md` §Coverage map — round 10 additions (5 rows). `SKILL.md` gains one pointer line only (`SKILL.md:344-345`), with no decision-table bloat.
- `SCORECARD.md`: the capability row (`:126`), the saturation declaration (`:132`), and an appended §Round 10 with per-claim rows and next-round Planned. `LOG.md` §round 10 is appended at the end.
- Re-verification for the record only (contested, see L0): `.ufo/round-10/gates/*.json` (7 files). The 3 registered rows are DEAD connection-refused, `check` exit 2; `consumers` exit 0; fixtures `RESULT pass=24 fail=0`; the unit is not-found; the rows match tracked baseline `20261014T124232Z`.
- Cross-domain evidence (connector, `history://W2RoundKama.KamaConnector`), handed off and not absorbed:
  - **kumitate:** gateway/routing health (SGLang Model Gateway, S024 rejected for kama).
  - **kengaku:** quantization quality and ranking.
  - **kagi:** auth surfaces.
  - 0 sibling `SOURCES.md` rows share kama's URLs.

## Landed changes

All changes are in lane commit `1e41928` and tied to `LOG.md` §"round 10 — sources registry, cross-engine entries, stale anchors":
- `corpus/SOURCES.md` (new) and the 3 new knowledge entries — LOG bullet "C3 capability + coverage".
- 12 corpus files with appended correction blocks, plus the ledger — LOG bullet "C1 freshness".
- `corpus/QUALITY.md` (KQ6–KQ10 appended), `corpus/lessons/round-10.md` (new), `corpus/README.md` (appended coverage block) and `SKILL.md` (pointer) — LOG bullet "C3".
- `SCORECARD.md` (round-10 section, capability row, saturation) — LOG entry header and SCORECARD §Round 10.
- `.ufo/round-10/{audit,gates,fragments}` evidence — LOG bullets "C1" and "Plan claim 2 closed".
- Append-only exceptions, recorded in LOG:
  - `SKILL.md`, `corpus/README.md` and `consumer-registry.md` had no final newline, so each append changes that last line's bytes. The text is identical.
  - Two SCORECARD contract rows were replaced 1:1, with no line shift.

## Before → after measurements

| Claim | Counting command | Before (`35e9175`) | After (`1e41928`) |
|---|---|---|---|
| C1 freshness | ledger loop in `corpus/lessons/round-10.md` §Corrections (prints `rows=` and then the uncorrected count). For the before value, the same loop runs over `git show 35e9175:$f` | rows=50, uncorrected **50** (all 50 `old_pointer`s present on their base lines: 0 MISS) | rows=50, uncorrected **0** |
| C3 capability | contract-v1 census (`SOURCES-CONTRACT-v1.md` §Census, all 7 commands) | `corpus/SOURCES.md` absent | rows 30; malformed 0; tiers A=27 C=3; status mined=17 queued=8 rejected=5; dup ids none; enum/tier-inflation none; missing used-by none |
| C3 coverage | `ls corpus/knowledge/*.md \| wc -l`; `grep -lE '^source: S[0-9]{3}' corpus/knowledge/*.md \| wc -l`; `awk '/^## Coverage map/{f=1;next}/^## /{f=0} f&&/^\| \`/{c++} END{print c}' corpus/README.md` | 9; 0; 19 | 12; 3; 24 |
| no-harm | `md5sum tools/kama-probe.sh`; `bash tools/test-snapshot.sh \| tail -1`; `git diff 35e9175 --stat -- tools registry` | `1f81e859…`; 24/0 | `1f81e859…` (unchanged); `RESULT pass=24 fail=0`; empty diff |

Self-verdicts, pending non-author verification:
- **freshness: improved, 7 → 8.**
- **coverage: improved, 8 → 9**, with the capability row entered.
- operability, depth, calibration (score) and adjacency: unchanged.
- No axis is harmed, as far as the lane can see.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources → `SKILL.md` §Decision table, §Historical error signatures, §Checklist, §Cited sources (`:344` now points to `corpus/SOURCES.md`). Debt: 13 of 14 anchor-bearing SKILL lines are stale per the scout (`history://W2RoundKama.KamaScoutAnchors`).
- [~] At least one end-to-end domain task executed and logged in LOG.md → `LOG.md` §§round 1–3; round 10 is documentation plus corrections, not an endpoint repair.
- [~] Instructions executable by an agent without oral context → `SKILL.md` §Checklist; the C1 counting command is self-contained in `corpus/lessons/round-10.md` §Corrections. Independent execution review is still open.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → each new entry names its kumitate/kengaku boundary (e.g. `corpus/knowledge/runtime-health-surface-matrix.md` §What this does not establish). `PROVINCE.md` is unchanged; its `:11` stale pointer is named as debt.

## Sources & frontier

- SOURCES rows, by the census row count: **0 → 30**.
- Added by tier: A=27 (docs/spec/code/own-work), C=3 (community). Status: mined 17, queued 8, rejected 5 (S024, S026, S027, S028, S030 — each with reason and flip).
- Rows touched old→new: none; every row is new and no in-place status change was made.
- The ART dossier's 20 rows were all re-opened, with these deltas:
  - S017's URL now redirects with a 301 (the row uses the canonical URL).
  - vLLM's and SGLang's GGUF support depends on hardware.
  - S008's source moved from `.md` to `.mdx`.
- All 6 ART leads were opened, becoming S021–S026. One community sweep found 39 results and included 3.
- Revision pins for unversioned docs pages (S006, S007, S009, S010, S018) come from each page's upstream file commit.
- Frontier advanced: the README §Frontier item "Correct still-live source anchors through new cited correction entries" is done for `corpus/` (50 rows). Still frontier: declared-vs-served context size (needs an authorized runtime), the non-author spot-check, and SKILL/PROVINCE/SCORECARD anchors.

## Mistakes

- Mining: 24 rows in `corpus/lessons/round-10.md` §Mistakes, using fleet taxonomy C01–C13 plus the lane's I/M/C/S/P letters.
  - 19 rows were kept from STATE §4, with every pointer re-verified. 1 was dropped because its own evidence contradicts it (#17), and 1 count was corrected (11 → 15).
  - 5 rows are new: rounds 7 and 9 re-dispatching an identical failure, the round-5 unprobed validator, the free-tier/craft round-number collision, and this round's L1 `listeners` slip.
- Unlearned classes with no capturing criterion: 12. Criteria added, each citing the lesson: **KQ6** (docs-scoped engine claims), **KQ7** (stale-anchor ledger with a count that reaches 0, appended at end of file), **KQ8** (UNDECIDABLE plus the blocked command), **KQ9** (full-set, case-canonical reads) and **KQ10** (census scope).
- Carried forward without a criterion: dispatch pre-flight, gate falsifiability, numbering integrity and state derivability. These are process rules, not corpus admission criteria.
- This round's own slips:
  - The L1 ran `kama-probe.sh listeners` outside checklist step 7's scope. Its output was excluded (Mistake 25).
  - The C1 executor read 4 body lines of `~/Projects/ufo-fsd-alpha/config/l1-max-context.yml`. A18 was reduced to `wc -l` and its content-derived wording withdrawn.
  - 18 circular `stale_check`s were caught by the reviewer and rewritten shape-only.
  - A12 was a false positive and was withdrawn.
  - The critic's sweep found one missed anchor, added as A51.

## Trend verdicts

- **Expansion: improved.** 3 admitted `knowledge/` entries cite `mined` S-rows on ground the lane map lacked (`corpus/README.md` §Known gaps: llama.cpp-only evidence, and no metrics or GGUF rows). The critic's caveat stands: health is an extension to cross-engine semantics, not a wholly absent topic.
- **Quality: improved.** 50 stale anchors are now corrected, 0 uncorrected. There is a bar for docs-sourced claims (KQ6), and every row has a revision anchor and a Gate quote.
- **Discernment: unchanged pending outside check.** There are 5 rejected rows with flips, a withdrawn false positive, and dissent recorded in `corpus/lessons/round-10.md` §Review record. No non-author admit/reject spot-check has happened yet.

## L0 questions

- `kama | round-10 | Does the kaika "documentation only — no live-target probing" rule bind the kama L1's own registered-endpoint checklist (loopback GET /v1/models on its 3 registry pins, kama-probe.sh check/consumers, isolated snapshot)? The round-10 plan's declared claim 2 required those runs; the L1 ran them, the round's sentinel and critic hold them prohibited, so S030 is rejected and no claim rests on them. Rule which, so round 11 can either cite or stop running its own gate.`
- `kama | round-10 | Is corpus/SOURCES.md a capability acquisition (the campaign binding §6.4 says so; capability row entered on a clean census) or only a coverage move (the round's critic, citing AXES.md:57-64)?`

## Integrator notes

- **No push.** The standing operator rule "No push" overrides MISSION.md:79's commit-then-push. The lane commit and this report are committed or left for the integrator, never pushed.
- Out-of-scope defects:
  - The round-10 prompt's §1 axes ("operability + calibration") contradict `MISSION.md:29` (operability + freshness), a recurrence of G5.
  - The prompt's `.ufo/round-10/plan.json` reference resolves only in the lane main checkout, not in the worktree.
  - The fleet `MANIFEST.json` still records a max kama round of 4 (STATE G2).
- Harness hazard: `cd` is broken (`__fnmcd`). My first command's `cd` failed silently and ran read-only `ls`/`tail` in the fleet root. No kama writes landed outside the worktree, the ledger report path, and `/dev/shm` scratch. I checked `/home/vgpnk/Projects/shokunin/.ufo/round-10/audit/` (absent) and the fleet-root status for kama-shaped strays (none).
- Provider exhaustion: the executor route was rate-limited mid-round. The C1 seat was re-dispatched fresh, and no claim was shrunk.
- The untracked `kama-shokunin/.ufo/round-10/{plan.json,SEAT-PROTOCOL.md}` in the lane main checkout are left untouched. The plan is now executed by `1e41928` in the worktree, and the integrator decides whether to commit or archive the plan files.
- No mission was open longer than two driver ticks. No watchdog driver was involved: this round was dispatched in-session.

## Post-review fixes

Lane commit **`4066035`** ("round-10: post-review fixes", lane identity, pathspec-limited; parent `1e41928`). Append-only: `git diff --numstat` showed 0 deletions (LOG.md +5, SCORECARD.md +17, corpus/lessons/round-10.md +15, plus one new file). No new claims. Responds to the orchestrator's conditional ADMIT:

- **D-1 (ruling recorded):** the L1's read-only gate runs on the lane's own registered local endpoints are in-province. No claim rests on them. S030 stays `rejected` under append-only, with its flip condition now met. L0 question 1 above is answered by this ruling. Mistake 25 (`listeners` outside checklist step 7's scope) stands. Recorded at `SCORECARD.md` §Erratum — round 10 post-review and `corpus/lessons/round-10.md` §Errata.
- **D-2:** I appended an axes erratum to `SCORECARD.md`. It supersedes the stale top table rows (freshness 6→7, coverage 1→8) with this round's moves: freshness 7 → 8 and coverage 8 → 9. The other four axes are unchanged.
- **D-3:** Mistake 14's `stale_named_lines` count is retired. It measured 15 at `35e9175` and 29 at `1e41928`, because its substring greps also match the correction lines, which quote each old pointer by design. The ledger measurements supersede it, and the "target 15 to 0" fix is withdrawn.
- **C1, corrected measurement:** "uncorrected 0" only means every row has a correction appended. The new `bash .ufo/round-10/audit/validate-new-pointers.sh` validates each new pointer's path and line bounds; host paths get a line count only.
  - Output at `4066035`: `rows=50 resolved=48 terminal=2 unresolved=0`.
  - The two terminal rows are A17 (`none — dead surface`) and A51 (`UNDECIDABLE`). They are corrected but **not re-anchored**.
  - Negative control: a 2-row bad ledger prints `unresolved=2`.
  - Content correspondence is still checked by sampling, not by the script.
- **C3, restated:** I measure coverage on knowledge entries only: 9 → 12 entries, and 0 → 3 with a `source: S###` header. The coverage-map figure of 19 → 24 counted two administrative rows. The per-entry uncovered-ground rationale is in `SCORECARD.md` §Erratum. The health entry extends existing llama.cpp-only ground to cross-engine semantics, while the metrics and GGUF topics were absent.
- **Census:** `TZ=UTC bash …/fleet-census/scripts/sources-census.sh validate <worktree>` printed `kama-shokunin ok …/corpus/SOURCES.md`, exit 0.
