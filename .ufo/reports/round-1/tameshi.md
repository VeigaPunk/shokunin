# tameshi — fleet round 1 (kaika continuation, steered round 1)

Lane commits (worktree `.tower/worktrees/kaika/tameshi-shokunin`, branch `kaika/round`, base `4eb4cf3`, identity `tameshi-shokunin <tameshi@shokunin.local>`):
**`c7986cdf051cbe9d047f02f76f2e1da0b36a84e3`** (round content) and **`121696bf92db813f75f792be8590cf2c2c98edb1`** (same-round phase-2 corrections; measured HEAD).
This closes the open fleet round 1. The blocked 2026-10-15 attempt (`cd31c6b`) declared a calibration claim. That claim is judged here once: the inherited `0 → 6` is not landed a second time.
Collision check: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-1/tameshi.md` was absent, and lane `LOG.md` had not closed round 1. Both were checked at round start.

**No push.** The standing operator rule "No push" overrides MISSION.md:79 (commit then push), under the kaika binding §6.6. Both lane commits are local. This report is uncommitted; the integrator commits it.

## Work performed

Declared claims: **K1 — calibration** (the lowest non-retired axis; this is the open round's declared claim, completed) and **K2 — capability `sources-registry`**. A third claim, **K3 — coverage**, was declared and then withdrawn before landing (see the reject list).

- Re-read MISSION.md, AXES.md, PROTOCOL.md (headings and evidence standard :338-343), PROTOCOL-APPENDIX.md, CORPUS.md, LEARNING.md :20-50, the STATE/ART dossiers, the frozen SOURCES contract v1, and the fleet critic.
- Took the baselines before dispatch:
  - command C @ `284ab0f`: `checked=4 asserted=0` → bound 0.
  - command C @ `4eb4cf3`: `asserted=3 untouched=1` → bound 6.
  - command D: `recorded_cases=6`.
  - `corpus/SOURCES.md` was absent.
- **L2 swarm: one batched `task` call of 10 seats.** Roles: Planner (planner), Overlap (connector), ColdRead, ScoreSemantics and WitnessKill (3 executors), Sources (scribe), LeadScout (scout), CapabilityLab (labrat), Reviewer (reviewer), Critic (critic).
  - Every fresh prompt began with `/skill:godspeed` plus the verbatim `directive.md` bytes.
  - Writing seats had disjoint file sets. No seat committed.
  - Two earlier attempts were refused with `Background job limit reached (100)`. The same batch was retried unchanged.
- **Provider exhaustion (named):** ColdRead-3, ScoreSemantics-3 and WitnessKill-3 died with `resource_exhausted` ("Reached free model rate limit").
  - They were re-dispatched fresh, and the dead seats' scratch directories were declared off-limits.
  - ScoreSemantics-4 and WitnessKill-4 ran in one batched call on the reassigned executor route.
  - ColdRead-4 on that route failed at capacity (`turn_rate_limit_exceeded`). The cold-read then ran as ColdReadLab-2 on the `labrat` role route.
  - An interim labrat spawn was cancelled to follow the orchestrator's same-role note. When the executor route failed again, the cold-read went back to labrat.
  - Evidence: lesson ER-K4 (`corpus/lessons/round-1.md:398+`).
- **K1 cold-read:** run from the page alone, with no access to the corpus or LOG.
  - Result: `COLDREAD: SUFFICIENT (appendixA=8/10 recorded=8/10 appendixB=8/10 recorded=8/10 blocking-gaps=0 wrong-expectations=0 survivors-probed=4/4)`.
  - Evidence: `reports/round-1-kaika-coldread.md` and `.ufo/evidence/kaika-round-1/coldread/` (results.tsv and per-defect logs). Reviewer spot-checked D5, B4 and the D2/B2/B5 probes.
  - It ran against blob `4eb4cf3:SKILL.md`, sha256 `33e3009c…0f81`, which this round did not change.
- **K1 mistakes mined:** `corpus/lessons/round-1.md:266` `## Mistakes` lists MK-1…MK-11.
  - Five classes were unlearned. They became `corpus/QUALITY.md:10` criteria 6–10, each citing its MK row.
- **K1 box 4 correction:** the Reviewer found box 4's "PROVINCE.md still accurate" overreached, because the Owns list omitted the tsukuroi and mado gates. Fixed by appending `PROVINCE.md:22` Core / Frontier / Adjacent.
- **K2:** `corpus/SOURCES.md` now holds 44 rows.
  - 37 external sources were re-opened this round, each with a fetch sha256 in `.ufo/evidence/kaika-round-1/sources-opened.tsv`. 7 own/gate rows are anchored as path @ commit.
  - It also carries `## Paths`, `## Search log` (2 sweeps plus the W1 restatement) and `## Leads`.
  - Spot-check: the S002 hash re-fetched identical (`404575e9…`). The Critic re-opened S001 and S003; anchors and quotes match.
- **K2 demonstration — mining into admitted entries:**
  - `corpus/knowledge/mutation-score-semantics.md` (F1) mines S001, S002, S004, S005 and S006. Six cases were recomputed; t = 0, so the Stryker score equals tameshi's rate on every recorded case. NoCoverage is kept as U. The "timeout counts as a kill" rule is rejected and kept.
  - `corpus/knowledge/witness-scoped-kill-verdict.md` (F2) mines S006. It declares witnesses for js-kimi-census: **8 killed-on-witness / 0 accidental / 2 survived**, which equals the recorded 8/10. The declaration sha `32241b02…` was recorded at 22:05:45Z, before the 22:07:13Z sweep. Contamination is disclosed (erratum E1).
- **Capability demo (labrat), evidence in `.ufo/evidence/kaika-round-1/capability-demo/`:**
  - H1 CONFIRMED: `MUTATE_SELFTEST: 80/80 pass` exit 0, and `REGRESSION: PASS (cases=6 passed=6 …)` exit 0.
  - H2 CONFIRMED: one control per sweep (F3 evidence).
  - H3 CONFIRMED: the selftest output is identical under `env -i LANG=C TZ=UTC`.
- **Phase-2 review/critique**, re-run on `c7986cd`:
  - All counts re-ran identical. No knowledge was changed or deleted. Edits were append-only apart from SHONEN lines 9-12 and the capabilities placeholder.
  - Defects were found and fixed in `121696b` (ER-K5…ER-K8; see Mistakes).

## Landed changes

| Change | Commit | LOG.md entry |
|---|---|---|
| SHONEN box 3 `[ ]`→`[~]` (wording unchanged; evidence line scope-bounded), box 4 evidence line | `c7986cd`, narrowed in `121696b` | `LOG.md:551`, `:614` |
| `reports/round-1-kaika-coldread.md` + `.ufo/evidence/kaika-round-1/coldread/` | `c7986cd` | `LOG.md:551` |
| lesson `## Mistakes`, `## Gate — kaika continuation`, errata ER-K1…K4 | `c7986cd` | `LOG.md:551` |
| `QUALITY.md` criteria 6–10 | `c7986cd` | `LOG.md:551` |
| `corpus/SOURCES.md` (44 rows) + `sources-opened.tsv` + census v1 script/output | `c7986cd` | `LOG.md:551` |
| `knowledge/mutation-score-semantics.md`, `knowledge/witness-scoped-kill-verdict.md` + evidence dirs | `c7986cd` | `LOG.md:551` |
| `corpus/README.md` coverage addendum (15 rows), `## Sources`, `## Frontier` F1–F10, `## Known gaps`; `PROVINCE.md` Core/Frontier/Adjacent | `c7986cd` | `LOG.md:551` |
| `SCORECARD.md` claims section, 3 capability rows, saturation line 8/10 + window N=2, round-2 Planned | `c7986cd` | `LOG.md:551` |
| Gate addendum (quotes for S031–S037), ER-K5…K8, census v2 (`sources-census-v2.sh`, mutation-tested), SCORECARD phase-2 paragraph, witness erratum E1, README gap | `121696b` | `LOG.md:614` |

Untouched on purpose: `SKILL.md`, which keeps the cold-read bound to its bytes; `tools/`; all 19 pre-round knowledge files; sibling repos, which were only read and materialized into `/tmp`.

## Before → after measurements

| Claim | Counting command | Before | After (measured on `121696b`) |
|---|---|---|---|
| K1 calibration | command C (`SCORECARD.md` `## Current axes`): `git show "$REV:SHONEN.md" \| python3 -c '…'` | `284ab0f`: `boxes=4 checked=4 asserted=0 untouched=0 asserted_mark_upper_bound=0` (pinned 0); `4eb4cf3`: `asserted=3 untouched=1 …=6` (inherited, unadmitted) | `boxes=4 checked=0 asserted=4 untouched=0 asserted_mark_upper_bound=8`. Candidate 8 (lane cap). Pinned score stays 0 until non-author review. The final 2 points need independent promotion review. |
| K1 (discernment support) | `git show $REV:corpus/QUALITY.md \| grep -cE '^[0-9]+\.'` | 5 | 10 (criteria 6–10 each cite an MK row) |
| K2 sources-registry | `bash .ufo/evidence/kaika-round-1/sources-census-v2.sh` | no `corpus/SOURCES.md`; ART §1.2 sweep `https?://` → 0 lines | exit 0; rows 44; malformed 0; A=37 B=5 C=2; mined=12 queued=29 rejected=3; no dups, no enum/tier-inflation hits, no missing used-by; H4 id-or-path 0 violations; strict id-cite 25 (informational, own/gate rows); `SOURCES_CENSUS: CLEAN (contract v1 + H4 id-or-path)` |
| Guardrail (depth) | command D | `recorded_cases=6 depth_score=6` | `recorded_cases=6 depth_score=6` (unchanged) |

Expansion support:
- Unindexed notes: 13 → 0, using `for f in corpus/knowledge/*.md; do b=${f##*/}; grep -qF "knowledge/$b" corpus/README.md || echo "$b"; done | wc -l`.
- Source-headed entries: 0/19 → 2/21, using the per-file `head -5 | grep -c '^source:'` loop.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. This is a lane assertion. Phase-1 Reviewer verdict: SUPPORTED (`reports/round-1-calibration.md#box-1`).
- [~] At least one end-to-end domain task executed and logged in LOG.md. This is a lane assertion. Reviewer verdict: SUPPORTED (`reports/round-1-calibration.md#box-2`). The cold-read sweeps are a further current execution.
- [~] Instructions executable by an agent without oral context. This is a lane assertion, bounded to the Appendix A + B sweep recipe (`reports/round-1-kaika-coldread.md`; SHONEN.md:10).
  - Not exercised: the audit recipe, the fail-closed taxonomy, and the service, cadence and runbook sections.
  - The Critic rates it a scope-incomplete candidate.
- [~] No cross-domain bleed (PROVINCE.md still accurate). This is a lane assertion. The PROVINCE overreach was corrected by an append (`PROVINCE.md:22`; `reports/round-1-calibration.md#box-4`).

No `[x]`: non-author verification is the orchestrator's job.

## Sources & frontier

- **SOURCES rows: 0 → 44**, counted with `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
  - External: A 30 (5 mined, 25 queued); B 5 (4 queued, 1 rejected: S030); C 2 (rejected: S029, S046).
  - Own/gate: A 7 (all mined).
  - S038–S039 are unused (ER-K8).
- **Rows touched old→new (contract rule 2):** S005 `queued`→`mined`; S006 used-by gained `mutation-score-semantics.md`. Both changed before the commit and are logged in the lesson Gate.
- **Frontier:** F1–F10 are declared in `corpus/README.md:68`, from 0 rows before.
  - Advanced to held: F1 (score semantics) and F2 (witness-scoped kills).
  - Readings for the next move: F3 (one control per sweep, H2) and F5 (selftest env-invariant, H3).
- **Leads:** 6 promoted to rows S040–S046. Zeller & Hildebrandt TSE 2002 stays a lead (author PDFs returned HTTP 000; ResearchGate returned 403).
- **Connector:** 0 of the 30 ART URLs are rowed by any sibling registry (chousa, game-dev-2d and kotoba were scanned). Its "second lane for witness contracts" (kotoba `verifiers/fault_injection_corpus.sh`) is reported here as a lead and not claimed: generality needs two lanes' evidence (PROVINCE.md:15-16).

## Mistakes

- **Mined from the lane's history** (`corpus/lessons/round-1.md:266`): 11 classes, MK-1…MK-11.
  - Unlearned before this round: MK-2/3 (a wrong pre-registered prediction, repeated), MK-4 (lagging index), MK-5 (verification run but no report landed), MK-6 (evidence only in `/tmp`, later lost), MK-7 (entries without a provenance header).
  - These became QUALITY criteria 6–10.
- **This round's own mistakes**, caught by the lane's Reviewer and Critic seats and kept as errata ER-K1…ER-K8:
  - The K2 census was first called clean while its H4 block printed 25 lines, and the own/gate rows lacked Gate quotes. Fixed with census v2 plus a Gate addendum.
  - The box-3 line was broader than the run. It was narrowed.
  - `SKILL.md:14-15`/`:133-135` are now stale against the cold-read. They are marked, not edited.
  - The witness "pre-registration" heading overstated blindness. Erratum E1.
  - The MK-6 evidence command was wrong as first written. Fixed before commit.
  - Gate reject-4 was not reconciled with the new criteria. ER-K1.
- **Credential sweep:** it hit on `coldread/SKILL.snapshot.md` — a copy of SKILL.md text that describes `op://`-style paths (descriptive text, not credential material). The copy was replaced by a sha pointer, and the final sweep printed nothing.

## Trend verdicts

All are self-verdicts pending the orchestrator's non-author verification.

- **expansion: improved.** Two entries were admitted on frontier ground (F1, F2) that the coverage map did not hold. Each cites `mined` rows and has its own coverage-map row (`corpus/README.md:60-61`). Neither failed its bar on phase-2 review.
- **quality: improved.** 13 → 0 unindexed notes. The box-4 PROVINCE overreach was corrected. Stale SKILL status sentences are marked rather than left silent (ER-K5). No admitted entry failed its re-check.
- **discernment: pending.** No self-verdict is given. The non-author spot-check of ≥1 admit and ≥1 reject is owed by the orchestrator.
  - Suggested sample: admit `witness-scoped-kill-verdict.md`; reject K3 or S046.
  - The lesson Gate (`corpus/lessons/round-1.md:302`) holds the full admit/reject list with reasons.

## L0 questions

- `tameshi | round-1 | The 19 pre-round knowledge entries lack source:/verified-at:/recheck: headers (CORPUS.md §Layout). Prepending would shift every path:line cite into them, which harms depth and calibration evidence. Rule: (a) a sidecar provenance table, (b) a citation-remap migration round, or (c) grandfather them with the header bar applying only to new entries (the current state)?`
- `tameshi | round-1 | Box 3 "Instructions executable by an agent without oral context": does a cold-read of the SKILL's two declared "reproduce from this page alone" appendices suffice for [~], or must the audit recipe, fail-closed taxonomy and service sections also be exercised? (The Critic says scope-incomplete.)`

## Integrator notes

- **Tameshi is missing from the MANIFEST roster.** Probation completed at round 3 (2026-10-14). The roster row is the operator's to write (STATE D5).
- **Worktree artifact:** `SKILL.md:1469` `../PROTOCOL.md` resolves from the main checkout only, not from a `.tower` worktree (ER-K2).
- **Sibling incident:** the cold-read observed kumitate's `scripts/kimi-census.mjs` worktree edited mid-sweep (22:06:51Z). The pinned blob `175de6ba` still reads `83016d45…`, so the measured table binds to the pin. This is not tameshi's to act on.
- **Fleet-root strays** (RelNotes, dedupe.rs, err.*.txt …) were present during this round. Tameshi wrote none of them. Every tameshi command used the bash `cwd` parameter or absolute paths.
- **H4 strict id-cite:** pre-registry own/gate rows cite their sources by path. The fleet census could adopt v2's id-or-path rule for own-work/code rows.
- **Merge:** the integrator merges `kaika/round` @ `121696b` into tameshi `master`. The lane's main checkout was not touched.

## Post-review fixes

Lane commit **`01b358c30ba484e766c281823c5b0f89ecff0840`** (`round-1: post-review fixes`, identity `tameshi-shokunin`, pathspec-limited, 5 files, 91 insertions / 0 deletions — append-only). This follows the orchestrator's adjudication: reviewer admitted with conditions; critic admitted K2 and rejected K1 as measured.

- **K1 re-pinned without the box-3 increment.** Calibration is pinned at **6**: boxes 1, 2 and 4 are restrained `[~]`, at 2 points each. This is measured on `121696b`/`01b358c`. Command C still prints `asserted_mark_upper_bound=8`; that is the mark census only.
  - Box 3 stays `[~]` with its scope note, and scores 0.
  - The verified calibration work is the QUALITY criteria (5 → 10) and the box-4 overreach fix. See `SCORECARD.md` §Post-review corrections and lesson §Non-author adjudication.
- **F1 and F2 relabelled `held` → `partly held`** (`corpus/README.md` §Frontier — status correction):
  - F1: report interop was not validated.
  - F2: only one JS leg was measured, and its witness declaration was partly contaminated.
- **SCORECARD corrections:** the K1 and K2 measured-commit cells now read `121696bf92db813f75f792be8590cf2c2c98edb1`. The K2 counting command now points to census v2 (`sources-census-v2.sh`, exit 0, `SOURCES_CENSUS: CLEAN`), not v1.
- **S038–S039 reservation:** recorded in `corpus/SOURCES.md` §Id allocation as allocated, never written, and retired. They are not reused or renumbered. The next id is S047.
- **No SOURCES row cell changed,** so the lesson owes no old→new entries.
- **Fleet census:** `TZ=UTC bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate <worktree>` printed `tameshi-shokunin	ok …/corpus/SOURCES.md` and exited **0**.
- **Credential sweep** on the staged diff printed nothing.
- **Corrected trend verdicts:**
  - expansion: improved.
  - **quality: unchanged.** This supersedes "improved" in §Trend verdicts above.
  - discernment: per the orchestrator's adjudication. The non-author spot-check disagreed with the lane's Gate admit of the box-3 move. That disagreement is recorded in the lesson, and it is taught by ER-K7: a mark's evidence must cover the mark's whole wording, or the mark does not score.
- **Calibration self-verdict, corrected:** improved, 0 → 6 pinned. All other axes are unchanged. No new claims.
