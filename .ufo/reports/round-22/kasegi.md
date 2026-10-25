# kasegi — round 22 report (kaika campaign, 2026-10-19)

Lane commit: **`c8b719d22882863ea7cd89b14c8bc078228001ed`** (branch `kaika/round`, worktree
`.tower/worktrees/kaika/kasegi-shokunin`, base `94aace2`, author `kasegi-shokunin <kasegi@shokunin.local>`,
pathspec-limited, credential sweep printed nothing). Steered round 22 (r21 blocked with zero credit,
consumed 21); there was no collision: `.ufo/reports/round-22/` held only `kotodama.md` at start, and no
`LOG.md` entry closed round 22.

## Work performed

Declared claims (2, distinct axes, causally separable):

- **C1, depth:verifiability.** This is the lowest non-retired axis, at 4. It is provenance *disclosure* for the 25 legacy knowledge entries: `source:`, `verified-at:` and a fail-closed `recheck:`, plus same-line historical markers on dead-path "live" lines. It reads only the 25 legacy files.
- **C2, coverage (7), carrying capability `sources-registry`.** Five new knowledge entries on uncovered frontier ground were admitted through a new admission bar, and `corpus/SOURCES.md` was created. Index and province structure were added. It reads only the new entries, the registry, the README and PROVINCE.
- **Setup, not a claim.** `corpus/QUALITY.md` was minted. Each criterion cites its mined mistake.

Work items:

- **Admission bar.** `corpus/QUALITY.md:10-40` holds Q1–Q6 (entry) and R1–R6 (record), each grounded in a mistake id in `corpus/lessons/round-22.md:7-40`. The Q4 grounding was corrected after a critic finding: it was A9 and is now A7 + A6.
- **Source registry.** `corpus/SOURCES.md` follows contract v1, with 27 opened rows, `## Paths`, `## Search log` and `## Leads`. Per-row gate quotes are in `corpus/lessons/round-22.md:69-104`. The census outputs are at `corpus/lessons/round-22.md:105-115`.
- **Five admitted entries**, each with headers on lines 2–4 and Rule / Evidence / Kasegi use / Rejected / Limits sections:
  - `corpus/knowledge/cvss-v4-severity-and-vector.md`
  - `coordinated-disclosure-timelines.md`
  - `authorization-safe-harbor-and-scope.md`
  - `ai-assisted-finding-validation.md`
  - `cwe-top25-2025-methodology.md`
- **SKILL.md.** One appended block, `SKILL.md:1014` `## Frontier decision table (round 22)`: 5 durable rows plus a pointer to `corpus/SOURCES.md` and `corpus/QUALITY.md`. No existing line was edited.
- **Legacy provenance.** All 25 legacy entries end with `## Provenance (round-22 correction, appended)`. Of the rechecks, 23 fail closed (exit 1, base absent) and 2 pass (exit 0). 31 same-line `[r22 correction …; historical]` markers were added (`LOG.md:1046+`).
- **Index and province.** `corpus/README.md` gained 8 coverage-map rows, `## Frontier` F01–F08 (`corpus/README.md:191`), and a same-line provenance-scope correction at `:5`. `PROVINCE.md:27,35,40` adds `## Core` / `## Frontier` / `## Adjacent`. This is a classification, not a re-scope; L0 kasegi round-15 stays open.
- **Mistakes mined.** `corpus/lessons/round-22.md` § Mistakes holds M1–M17 and A1–A10, plus Unlearned→criteria (10 classes), Omissions and Gate agreements.
- **Ledgers.** `SCORECARD.md:316` holds the round-22 section, `:297-301` the capability row, `:309` the saturation declaration, `:176` the planned r23 work and `:191-192` the move-log rows. The round-22 entry in `LOG.md` starts at `:1046`.
- **L2 swarm.** One batched call of 12 (`W2RoundKasegi.K22*`):
  - planner, connector, scout, labrat, critic, reviewer, sentinel, scribe;
  - executors for Sources, Provenance, Entries and Index.

  Every prompt opened with `/skill:godspeed` followed by the verbatim bytes of `~/.agents/skills/godspeed/directive.md`. Two earlier identical batch attempts were refused by the session's 100-job cap and started nothing. **Provider exhaustion:** all four executor seats hit `resource_exhausted` (Devin free-model rate limit, reset ~22:11 UTC). They were cancelled and re-dispatched fresh in one batch (`K22*B`) on the re-routed bucket, and no claim was shrunk. A second batch of 3 (`K22PostReviewer`, `K22PostCritic`, `K22PostSentinel`) reviewed the integrated tree before commit. No model was passed; the session route table assigned all of them.

## Landed changes

All changes are in lane commit `c8b719d` (38 files, +822/−34). The 34 "deletions" are same-line suffix appends; every base line is a prefix of its current line, 0 non-prefix (`SCORECARD.md` round-22 counting block). Every item is logged in `LOG.md:1046+` (round-22 entry and its post-review paragraph).

| Change | Files | LOG.md tie |
|---|---|---|
| Admission bar (setup) | `corpus/QUALITY.md` | round-22 entry, "Setup" |
| Registry + capability | `corpus/SOURCES.md`, `SCORECARD.md` capabilities row | "Landed", "Post-integration review fixes" (S024 narrowed) |
| C2 entries + SKILL block | 5 new `corpus/knowledge/*.md`, `SKILL.md:1014-1024` | "Landed" |
| C2 index/province | `corpus/README.md`, `PROVINCE.md` | "Landed"; README scope correction under "Post-integration review fixes" |
| C1 provenance + markers | 25 legacy `corpus/knowledge/*.md` | "Landed", "Caught before commit (M17)" |
| Lesson | `corpus/lessons/round-22.md` | whole entry |
| Ledgers | `SCORECARD.md`, `LOG.md` | — |

## Before → after measurements

Before = `git archive 94aace2`; after = `git archive c8b719d` (and the clean worktree at `c8b719d`). The counting commands are verbatim in `SCORECARD.md` § Round 22 (` ```sh ` block). The resolver runs only in scratch copies via `/tmp/kasegi-r22/labrat/measure.sh <tree>`.

| Claim | Measure | Before (94aace2) | After (c8b719d) |
|---|---|---|---|
| C1 | legacy entries with `source:` / `verified-at:` / `recheck:` | 0/25 each | **25/25** each |
| C1 | recheck exit codes (23 fail closed = base absent) | no recheck lines | **23× exit 1, 2× exit 0** |
| C1 | same-line `r22 correction` historical markers | 0 | **31** |
| C1 | presence-wording sweep on absent roots | 8 | **5** (all 5 reviewed benign: past tense, or relocated `ufo-fsd-alpha` present) |
| C1 | legacy files with every original line prefix-preserved (anchor safety) | — | **25/25** (0 non-prefix) |
| C2 | Frontier topics admitted (`grep -cE '^\| F0[1-5] .*\| admitted \|' corpus/README.md`) | 0 | **5** |
| C2 | coverage-map rows (STATE §3 awk) | 25 | **33** |
| C2 | PROVINCE `## Core/Frontier/Adjacent` | 0 | **3** |
| C2 / capability | SOURCES rows; malformed; dup; enum; missing used-by | absent | **27; 0; 0; 0; 0** |
| no-harm density | `density.py SKILL.md` mean / blocks | 154.0 / 18 | **154.0 / 19** (18 blocks' value columns unchanged; new block 155.6 ≥ BAR_R15 142.5, 7/7 cites resolve) |
| no-harm anchors | `anchorcheck.py SKILL.md` | 7 in-range, 0 bad, LOST-RECORDED=306 | **identical** |
| no-harm resolver | skill / corpus / all (GONE) | 32/506, 140/1212, 156/1539 (1383) | 39/513, 187/1259, 203/1586 (**1383**); all-INTERNAL rise, **not credited** |

Self-verdicts, pending non-author verification:

- **C1:** improved; depth:verifiability score **held at 4**. Nothing lost was re-verified.
- **C2:** improved; coverage score **held at 7**. The r15 domain-root definition is unchanged. The proposed denominator is in SCORECARD for an explicit r23 claim.
- **Capability `sources-registry`:** enters (first-working round 22).
- **depth:density:** unchanged at 9, no harm.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: `SKILL.md:1014` frontier decision table with S-ids and admitted-entry paths, alongside the pre-existing tables; non-author verification is pending.
- [ ] At least one end-to-end domain task executed and logged in LOG.md. Untouched this round: documentation research only, no live-target work by rule.
- [~] Instructions executable by an agent without oral context. Evidence: runnable census at `corpus/lessons/round-22.md:105-115`, counting block in `SCORECARD.md` § Round 22, and 25/25 runnable rechecks.
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: `PROVINCE.md:40` `## Adjacent`; the connector overlap scan found no sibling duplication of S001–S015 (summary under Integrator notes).

## Sources & frontier

- **SOURCES rows:** 0 → **27**. Command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- **Added by tier:**
  - A = 25: specs, official docs and papers, each tier scoped to its own claims; first-party AI-results rows are scoped "what X reports".
  - B = 0.
  - C = 2: both rejected with a flip. S026 is CISA Gold Eagle (no checkable protocol). S027 is an HN tips link (no accessible text).
- **By status:** mined 15 (S001–S015, used by the five entries), queued 10, rejected 2.
- **Rows touched old→new:** none. All rows are new this round. Pre-commit corrections inside the round:
  - S003 anchor extended to PDF p. 6.
  - S013 anchor extended to "Removal of CWE Mapping Normalization".
  - S010 teaches reworded ("vulnerability" hypotheses).
  - S024 narrowed to its opened recitals, because its Art. 14(2)(a) quote matched only a secondary mirror and EUR-Lex Article 14 was unreachable to the reviewer and to L1.
- **Frontier rows advanced:** F01–F05 went 0 → admitted. F06–F08 (multi-party CVD S018, CNA rules S022, EU CRA S024) are queued, each with an opened row.
- **Verification sample:**
  - L1 string-matched 13/13 sampled gate quotes and 85/85 quoted strings in the new entries against L1-fetched pages.
  - The critic re-opened S001, S003 (page and PDF), S006, S009, S012 and S013; all exact.
  - The post-reviewer re-opened S013, S016, S019, S025 and S026; verbatim.

## Mistakes

- **Classes mined:** 27, M1–M17 plus A1–A10 (`corpus/lessons/round-22.md` § Mistakes).
- **Unlearned → criterion:** 10 classes (M1, M2, M6, M10–M14, M16, M17).
- **Criteria added:** Q1–Q6, R1–R6 (12).
- **M17 is new this round and was caught pre-commit.** Inserting headers at line 2 shifted roughly 160 path:line anchors into the legacy entries by +3. anchorcheck stays "0 bad" on range but printed the wrong line. The headers were relocated to an appended block, and **R6** now captures the class.
- **Residual, still uncaptured:** M5 and M15. A1, A2, A4 and A10 remain SKILL-only examples.

## Trend verdicts

- **Expansion: improved.** 5 admitted knowledge entries on uncovered or program-specific-only ground (scout sweep: CVD timelines and CWE method uncovered; CVSS, safe harbor and AI validation program-specific only). Each cites a `mined` S-row.
- **Quality: improved.** A QUALITY bar now exists. 25/25 legacy entries carry provenance with runnable rechecks. 31 stale live-claims are marked. The registry census is clean. Density and anchors show no harm.
- **Discernment: improved, pending outside check.** 27 mistake classes were mined into 12 grounded criteria, and 2 sources were rejected with flips. Six critic/reviewer findings were accepted and two rejected with evidence (B2 numstat; M6 pointer, `grep -n '131.4' SCORECARD.md` → 65). An outside spot-check of ≥1 admit and ≥1 reject is the orchestrator's.

## L0 questions

- `kasegi | round-22 | Domain roots (~/Projects/bounties, the-bounty-hunter, origin-work) remain absent; the lane proposes adopting a coverage denominator of 20 corpus-attested Core items + Frontier topics admitted/total (SCORECARD.md round-22 section) by explicit claim in r23 — accept, or re-point PROVINCE first (open since kasegi round-15)?`

## Integrator notes

- **No push.** The standing operator rule "No push" overrides MISSION.md's commit-then-push. Lane commit `c8b719d` is committed only. This report is left uncommitted in the ledger worktree for the integrator to commit with `--author="kasegi-shokunin <kasegi@shokunin.local>"`.
- **Provider exhaustion:** the m_swe executor route returned `resource_exhausted` mid-round, and the seats were re-dispatched fresh. The session's 100-job cap refused two whole batch attempts before the swarm started.
- **`cd` hazard:** one early L1 command ran in the lane worktree instead of a scratch dir and regenerated `corpus/instruments/citation-survival.{md,tsv}`. L1 restored both with `git restore` before any other work. Nothing was written to the fleet root.
- **Adjacency:**
  - kumitate's `SOURCES.md` S019 (MCP OAuth confused-deputy) is rejected there and referred to kasegi/kagi; it is a candidate kasegi frontier row.
  - A reusable validator exists at `.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh`; L1 ran `validate` on kasegi's SOURCES → `ok`.
- **Contract friction:** SOURCES contract v1 rule 1 says "the round lesson's `## Gate`". Lessons that also carry `## Gate agreements` match a naive `^## Gate` count, so use `^## Gate$`.
