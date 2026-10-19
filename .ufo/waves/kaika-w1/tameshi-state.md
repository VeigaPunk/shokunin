# STATE dossier — tameshi-shokunin (verification-fixture craft)

Wave: kaika W1 · Date: 2026-10-19 · Mode: read-only (the only write is this artifact).
All commands run from `/home/vgpnk/Projects/shokunin/tameshi-shokunin` unless noted.
Git state observed once at sweep start; re-verify before acting on any proposal below.
Fleet-root reads: `MANIFEST.json`, `AXES.md`; canonical upstream: `/home/vgpnk/Projects/kimi-shokunin/skills/shokunin/protocol/CORPUS.md`, `templates/mint/PROVINCE.md`.

---

## 1. Identity

- **Domain** — "verification-fixture craft — the reusable method of honest checks: hermetic suites, mutation testing, fail-closed arms, verdict-line discipline" (PROVINCE.md §Domain; ≤25 of its 27 words quoted). Sibling gates stay sibling-owned; read-only probes; out-of-province → report, never absorb (PROVINCE.md §Refuses, §Out of province).
- **Rank** — shonen. Minted 2026-10-14 by operator directive (MINT.md title; LOG.md round-0 entry "minted as shonen (operator directive; see MINT.md)" — `grep -n 'minted as shonen' LOG.md`). Probation rule: ≥3 verified rounds before any roster row (LOG.md round-0); probation completed at round 3 (LOG.md round-3 "probation-completing"; MANIFEST round-3 note "probation-COMPLETE" — `python3` MANIFEST scan below).
- **Git** — branch `master`, in sync with `origin/master`, tree clean:
  - `git status --porcelain=v1 -b` → `## master...origin/master` (zero file lines).
  - `git log -1 --format='%H %ci %s'` → `4eb4cf319c0eddd4ef0c6d1d4d11e51e0d4ee307` · 2026-10-17 00:29:09 −0300 · "tameshi: ignore interactive session logs".
- **Last round: 11** — verified in three places, matching the fleet hint "max recorded round 11":
  - Lane: LOG.md round-11 entry ("round 11 (training r10, the arc's final round)") — `grep -n 'round 11 (training r10' LOG.md`; SCORECARD.md move-log row `| 11 |` and verdict-table row r10 — `grep -n '^| 11 \|^\| r10 |' SCORECARD.md`.
  - Fleet: MANIFEST.json rounds[] — `python3 -c` scan → 294 round entries, 13 mention tameshi, max tameshi round **11**, note "training r10 (lane r11, FINAL)".
- **Next round number** — none in the historical arc: "tameshi round 11 is the tenth *training* round (r10) and the arc has no successor" (plans/round-11.plan.md:14-15). The live open round is **fleet round-1 interactive continuation — BLOCKED at dispatch** (LOG.md 2026-10-15 entries; handoff `.ufo/continuation/fleet-round-1.md` §Unblock before any dispatch). Driver launch counter ≠ completed-round count (LOG.md:428-429 area, "Driver counter 1 is not a completed-round count"). The operator's at-least-100 verified-round target stands (SCORECARD.md blocked-state section).
- **Roster** — **tameshi is absent from the fleet MANIFEST.json roster** (defect D5): `python3` scan → roster ids `['kasegi','kengaku','kake','kumitate','kotoba','kagi','kama','audio','game-dev-2d','game-dev-3d','lore','revenger','kaidoku']`; zero rows mention tameshi. Probation completed 2026-10-14 → the roster row is overdue by the lane's own mint rule.

## 2. Axes

Six-axis vocabulary per fleet AXES.md: depth, coverage, operability, freshness, calibration, adjacency.

Pinned scores (SCORECARD.md "## Current axes — fleet round-1 baseline", measured commit `284ab0f0b8b989ee73d9c00c0c0df0a59757af8d`):

| Axis | Score | Evidence / counting rule | Status at HEAD (4eb4cf3) |
|---|---|---|---|
| depth | 6 | One point per recorded mutation case in the tool's pinned replay ledger, cap 10 (SCORECARD command D) | Re-run at HEAD: `git show "$REV:tools/mutate-and-run.sh" \| python3 …` → `recorded_cases=6 depth_score=6` — holds |
| calibration | 0 | Two points per correctly restrained, durable-evidence-linked `[~]`, cap 8; final 2 require independent promotion review (SCORECARD command C) | Baseline census at 284ab0f: `boxes=4 checked=4 asserted=0` (LOG.md:400-401). At HEAD the four-box rework is in-tree: command C re-run → `boxes=4 checked=0 asserted=3 untouched=1 asserted_mark_upper_bound=6` — but the candidate is **unadmitted** (fleet round-1 admission BLOCKED), so the pinned score stays 0 |
| coverage | — unpinned | Historical move-log rows only (SCORECARD rows 8) | "historical observations, not newly assigned axes" (SCORECARD baseline section) |
| operability | — unpinned | Historical rows 7, 9, 10, 11 | same |
| freshness | — unpinned | No lane row; MANIFEST verdict rows for tameshi rounds 7-10 carry `freshness: improved` — fleet/lane skew (defect D15) | same |
| adjacency | — unpinned | Historical row 6 | same |

- **Lowest non-retired axis: calibration (0)** vs depth 6.
- **Saturation line + stagnation window N: undeclared** — "The lane's saturation line + stagnation window N are to be declared by the lane on its next round per `AXES.md` §The stagnation nudge" (SCORECARD.md §Saturation). AXES.md SCORECARD contract requires the field; still open (defect D11).
- **Capabilities: 0 rows** — the repertoire table holds only the placeholder "— none yet —" (SCORECARD.md §Capabilities), despite 11 rounds of demonstrated runnable capability (`tools/mutate-and-run.sh`, 1,642 L — `wc -l tools/mutate-and-run.sh`; selftest 80/80 rc 0 per LOG round-11 tick receipts). Rows enter only through a round that demonstrates the capability running (AXES.md §Capabilities) — none entered since the table was added (defect D12).
- **Planned** — the actual planned claim lives inline in the baseline section: "replace unsupported completion claims with the canonical four-box checklist and durable, explicitly lane-authored evidence" (SCORECARD.md baseline **Planned:** paragraph), with its falsifier ("any retained `[x]` without independent provenance, any changed box wording, or any unresolved evidence pointer"). The standalone `## Planned` section reads "no entries declared by this rollout" (defect D13).
- **Retired: none** (SCORECARD.md §Retired).

## 3. Corpus

Counts, each with its command (run 2026-10-19):

- **knowledge entries: 19** — `ls corpus/knowledge | wc -l` → 19.
- **lessons: 2** — `ls corpus/lessons | wc -l` → 2. Register numbering follows round id, not chronology: `round-10.md` is the register's first entry (historical round 10, landed during round 11); `round-1.md` is the fleet round-1 lesson. "lessons land one wave late, the sibling lane's round-9 precedent; this is the register's first entry" (corpus/lessons/round-10.md:4-6). Rounds 1-9 have no lesson files (defect D16, by-precedent).
- Both lessons carry `## Gate` — `grep -n '^## Gate' corpus/lessons/*.md` → 2 hits. Contract-conformant.
- **QUALITY.md criteria: 5** — `grep -cE '^[0-9]+\.' corpus/QUALITY.md` → 5 (falsifiable-or-opinion; source anchor; class separation; append-only errata; rejections kept).
- **Coverage map: 9 data rows** — `grep -cE '^\| `+'`'`+`knowledge/' corpus/README.md` → 9 (total `^\| ` rows 12 = 9 coverage + 1 coverage header + 1 lessons-table header + 1 lesson row — `grep -cE '^\| ' corpus/README.md` → 12).
- **Distinct files indexed: 6 of 19** — the 9 rows cover 6 distinct notes (3 rows are same-file round-2 addenda). **13 unindexed**: arm-class-matrix, closeout-r11, fleet-kill-rate-ledger, fleet-suite-census, mutation-case-kagi-checklist, mutation-case-kumitate-claims, mutation-case-mado-verify, mutation-case-tsukuroi-census, operator-runbook, self-hardening-r6, service-limits, service-optin-protocol, service-standing-state — `comm -23 <(ls corpus/knowledge | sort -u) <(grep -oE 'knowledge/[a-z0-9-]+\.md' corpus/README.md | sed 's|knowledge/||' | sort -u)` (defect D3; the round-10 lesson already measured "9 rows covering 6 of 16 knowledge notes" — the gap grew with the corpus).
- **`## Frontier`: absent** — `grep -c 'Frontier' corpus/README.md` → 0. Canonical layout requires "coverage map, known gaps, frontier" (canonical CORPUS.md §Layout) (defect D1).
- **Provenance headers: 0 of 19 entries** open with `source:` / `verified-at:` / `recheck:` — per-file loop `for f in *.md; do … grep -c '^source:' …` → every file `source=0 verified-at=0 recheck=0`; case-insensitive variants also 0 (the only `verified-at:` hits in knowledge/ describe kaidoku's grammar, not tameshi's entries). Canonical rule: "Each `knowledge/` entry opens with `source:`, `verified-at:` and `recheck:`" (canonical CORPUS.md §Layout) (defect D2).
- **Overdue recheck: none computable** — 0 entries carry `recheck:`, so nothing is scheduled and nothing can be overdue; the drift-detection axis (freshness) has no per-entry cadence hook (consequence of D2).
- Entries cite sources inline (sha-pinned anchors, reproduce specs, executed counters) — the *content* is source-cited per QUALITY.md 2; what is missing is the canonical *header form*.

## 4. Mistakes

Mined from LOG.md, SCORECARD.md, both lessons, plans/round-5-record-draft.md, reports/. No `harmed` verdict exists in any landed row (`grep -n 'harmed' LOG.md` → 0 hits) and no honest-stop round: the blocked dispatch is explicitly "one observed blocked attempt, not saturation or a proven three-consecutive-block stop" (LOG.md:524-525).

| # | Class | What happened | Evidence pointer | Captured by an existing rule? |
|---|---|---|---|---|
| M1 | Citation drift (self-caught) | 16 wrong-line citations in the kagi survey, kept as ER-1 with generator analysis (12/16 transcribed from a stripped header view) | LOG.md round-1 entry; gates-survey-kagi.md:508-543 | Yes — QUALITY.md 2 (source anchor); SKILL.md re-resolve-by-number rule |
| M2 | Wrong pre-registered expectation | Round-2 E1: author's D7-survivor expectation wrong (fixtures' modes share floor bits), kept as calibration miss | LOG.md round-2 entry; mutation-case-kimi-census.md errata E1 | Partially — errata practice (QUALITY.md 4) kept it; **no criterion requires a pre-registered prediction to carry its executed outcome** → proposed criterion P1 |
| M3 | Wrong pre-registered expectation (repeat) | Round-3 E1: failing-case counts predicted 6/10, wrong (case 04 is a second green fixture) — "same shape as round-2 E1" (LOG.md round-3) | LOG.md round-3 entry; mutation-case-kagi-census.md E1 | Same as M2 → P1 would have made the repeat a named bar, not a habit |
| M4 | Precision errata from verifier | VER-T1 cross-verify landed 2 precision errata (chmod enumeration :608/:654; JS wording scope) | LOG.md round-4 entry | Yes — errata practice; verifier-catches-author is P3 of verification-patterns-fleet.md |
| M5 | Substrate moved mid-run (incident I1) | Concurrent lane wrote tsukuroi's gate during tameshi's sweep; the plan's "tsukuroi original sha256 unchanged" was unsatisfiable; re-pin `b56c6e57…` | plans/round-5-record-draft.md:108, :249; round-6-record-draft.md:108 | Yes — ledger drift semantics (fleet-kill-rate-ledger.md:293-310); SKILL.md restore discipline; round-10 lesson 3 ("Timestamped readings are the only honest form for moving substrates") |
| M6 | Record defect repaired by scribe | Stray trailing `\|---\|` at SCORECARD EOF (round-1 append) rendered a phantom cell; repaired and noted, not silently dropped (SC-1) | LOG.md:159-162 | Yes — QUALITY.md 4/5 |
| M7 | Stale refs + invalid verdict token | Fleet round-1 ER-I1: stale line references corrected; `unprovable` is not the canonical token — **unprovable-but-better** | corpus/lessons/round-1.md ER-I1 | Yes — canonical LEARNING.md vocabulary; append-only correction |
| M8 | Own scratch-policy miss | First interactive CLI smoke ran under `.ufo/scratch`, violating SKILL.md:25-28's `/tmp` namespace rule; output kept as **nonconforming**, superseded by `cli-smoke-canonical.json` | corpus/lessons/round-1.md ER-I2; .ufo/evidence/fleet-round-1/cli-smoke*.json | Yes — the lesson itself rules "No generic new quality criterion is needed: the existing standing rule already decided this case" |
| M9 | Overreach rejected before landing | Box-3 blanket cold-read claim (historical n=1 JS mutant read as current whole-skill capability) rejected; box 3 stays `[ ]`, candidate calibration 6 not 8 | corpus/lessons/round-1.md §Gate rejected-1 | Yes — QUALITY.md 3 (falsifiable, bounded); PROTOCOL claimed-vs-re-executed rule |
| M10 | Authority rejections (3-in-1) | Promotion by own batch rejected (no independent verifier in batch); no new cross-domain pattern from a single lane (≥2-lane rule); no new QUALITY criterion without a lesson behind it | corpus/lessons/round-1.md §Gate rejected-2..4 | Yes — PROVINCE.md:15-16; LEARNING.md:32 |
| M11 | Rendering staleness recorded, not repaired | AUD-T11 findings F1 (tick-1 cell renders `—` while its receipt carries the reading) + F2 (§2.6 counts restated without an as-of) | reports/r11-aud-t11.md; LOG.md round-11 | Yes — round-10 lesson 2 ("a rendering goes stale by construction; pointers + the anchored-source rule are what make that safe") |
| M12 | Plan-vs-plan disagreement kept | Round-10 plan's "no round 11 is planned by this arc" vs the dispatcher's round-11 dispatch — "the disagreement is recorded here, not smoothed" | plans/round-11.plan.md:19-22 | Yes — record-not-smooth discipline (QUALITY.md 5) |
| M13 | Verifier disagreement kept as finding | Round-4 matrix verification: "matrix disagree-where-it-disagrees is the finding; row E exactly 1 instance in 20" | LOG.md round-4 entry | Yes — verification-patterns-fleet.md P-class (verifier catches author defects) |

**Pattern across M2/M3:** the lane pre-registers claims well but has no standing bar that a *prediction* (as opposed to a claim) must carry its executed outcome in the same entry — both misses were caught and kept only by the author's own errata habit.

Proposed criteria (none exists today):
- **P1** — "A pre-registered prediction carries its executed outcome in the same entry; a miss is an errata row naming the discriminator, never a silent drop." Would convert M2/M3 from habit to bar.
- **P2** — "A knowledge file lands with its coverage-map row in the same round, or the missing row is named as debt in LOG with an owner." Canonical CORPUS.md bars *premature* rows ("An index row is a claim. Write the row when the file exists, not before") but nothing bars *lagging* rows — D3 is the lagging inverse.
- **P3** — "A verifier seat's report lands in-repo in the round it executes; an executed-but-unreported verification is named debt with a landing owner." Round-10 lesson 5 states the principle ("a pass that exists only in scratch cannot be quoted"); D7 shows it is still not enforced.

## 5. Contract defects

Report-paths only; nothing touched. Severity: high = blocks admission/canonical sync; med = durable-record gap; low = housekeeping.

| # | Sev | Defect | Evidence / command |
|---|---|---|---|
| D5 | **high** | **tameshi absent from fleet MANIFEST.json roster** — probation completed 2026-10-14 (round 3), roster row overdue per the lane's own mint rule | `python3` MANIFEST scan → roster ids (13) contain no tameshi; MANIFEST rounds[] carries 10 tameshi train rows + mint row |
| D2 | **high** | 19/19 knowledge entries lack canonical `source:`/`verified-at:`/`recheck:` opening fields | per-file grep loop (§3); canonical CORPUS.md §Layout quote |
| D1 | med | corpus/README.md has no `## Frontier` / known-gaps section (canonical layout: "coverage map, known gaps, frontier") | `grep -c 'Frontier' corpus/README.md` → 0 |
| D3 | med | Coverage map indexes 6 of 19 knowledge files; 13 unindexed | comm pipeline (§3) |
| D4 | med | PROVINCE.md lacks the canonical Core/Frontier/Adjacent shape (uses Domain/Owns/Refuses prose) | canonical templates/mint/PROVINCE.md vs lane PROVINCE.md (1,049 B — `wc -c PROVINCE.md`) |
| D8 | med | Rounds 1-3 + round-11 audit/verifier evidence was retained under `/tmp` only; **the dirs no longer exist** — PROTOCOL.md:340-343 bars tmpfs as evidence | `ls -d /tmp/tameshi-* /tmp/w11-*` → no matches. Mitigations in place: in-note reproduce specs (SKILL.md Appendix A/B), tool `--regression` replays cases at pinned git blobs |
| D6 | med | No fleet-root `.ufo/reports/round-<N>/tameshi.md` for any round; the fleet-round-1 report lives in the lane repo instead | `find /home/vgpnk/Projects/shokunin/.ufo/reports -name 'tameshi.md'` → empty. Round-10 lesson measured the visibility asymmetry: "no fleet document indexes these artifacts" (service-standing-state.md:34-40 area) |
| D7 | med | Verifier reports absent: `reports/r10-ver-t10.md` (VER-T10 executed the cold-read loop, unreported) and `reports/r11-ver-t11.md` (VER-T11 poll lane) — both recorded-as-absent by the lane, never landed | `ls reports/` → 8 files, neither present; LOG.md:382-383, LOG.md round-11 "not landed at this write — the state, not smoothed" |
| D10 | med | fleet-kill-rate-ledger.md: two `stale` successor rows (tsukuroi-census `084951be…`→`bba6cdf6…`; mado-verify `d7edaab4…`→`dc864c6a…`) with no appended re-sweep rows at close; §1 still says "cases 1 and 2 only" vs the six-leg registry | `grep -n 'stale' corpus/knowledge/fleet-kill-rate-ledger.md` → :301-302, :328-329; LOG.md round-11 open items |
| D11 | med | Saturation line + stagnation window N undeclared (AXES.md SCORECARD contract field) | SCORECARD.md §Saturation |
| D9 | low | operator-runbook.md still carries four-leg lines vs the six-leg tool (ER-R3 open; anchored-source rule governs meanwhile) | `grep -n 'four leg\|cases 5/6\|not embedded' corpus/knowledge/operator-runbook.md` → :173, :374-375, :458 |
| D12 | low-med | Capabilities table empty despite demonstrated runnable capability (runner, six-leg regression, cadence tick) | SCORECARD.md §Capabilities; `wc -l tools/mutate-and-run.sh` → 1,642 |
| D13 | low | Standalone `## Planned` section empty; the real planned claim lives inline in the baseline section | SCORECARD.md §Planned vs baseline **Planned:** paragraph |
| D14 | low | SKILL.md bloat risk: 99,223 B / 1,476 L (`wc -c SKILL.md`; `wc -l SKILL.md`) — append-only per-round sections; restructuring would break the lane's own line-cite anchors, so any restructure must re-resolve cites (the ER-1 lesson) | sizes above |
| D15 | low | Fleet/lane ledger skew: MANIFEST has no tameshi round-1 row (train rows start at round 2); MANIFEST rounds 7-10 carry `freshness: improved` verdicts the lane SCORECARD move log does not mirror | MANIFEST scan vs SCORECARD rows 7-10 |
| D16 | low | Lessons register gap: rounds 1-9 have no lesson files (register started at round 10, "one wave late" precedent) | `ls corpus/lessons` → round-1.md, round-10.md |

**Clean checks (no defect):** required files all present (SKILL.md, PROVINCE.md, SCORECARD.md, LOG.md, SHONEN.md, corpus/README.md, corpus/QUALITY.md, corpus/knowledge/, corpus/lessons/); tree clean and in sync; `.ufo/scratch/` empty; SHONEN.md's four evidence links resolve — `grep -n '^#' reports/round-1-calibration.md` shows `## box-1`…`## box-4`; README/lesson pointers (`../reports/round-1-calibration.md`, `../.ufo/evidence/fleet-round-1/`, `../.ufo/continuation/fleet-round-1.md`) all exist; LOG-cited absences (D7) are recorded-as-absent by the lane itself, not silent dead pointers; no credential material observed in the corpus.

## 6. Proposed round

The historical arc is closed; the next round is the **fleet round-1 interactive continuation** (blocked) plus lane-internal claims that do not depend on the dispatch unblock. Three claims, ≥1 on the lowest non-retired axis (calibration 0):

**C1 — calibration (lowest axis; BLOCKED on fleet-level unblock).** Complete the fleet round-1 calibration admission: the four-box SHONEN rework is already in-tree (`[~],[~],[ ],[~]`, four durable links — command C at HEAD: `asserted=3 untouched=1 asserted_mark_upper_bound=6`); what remains is the rubric's reserved authority — a non-author spot-check of ≥1 admit and ≥1 reject from lessons/round-1.md §Gate, and independent promotion review of all four boxes.
- Before → after: calibration 0 (baseline census at 284ab0f: `boxes=4 checked=4 asserted=0`) → admitted score ≤8 with recorded non-author review rows (candidate 6 per the round-1 lesson's own decision).
- Counting commands: SCORECARD command C at HEAD; the acceptance comparison in `.ufo/evidence/fleet-round-1/calibration-acceptance.json` (baseline FAIL vs candidate PASS, exit 0).
- Falsifier (the lane's own): any retained `[x]` without independent provenance, any changed box wording, any unresolved evidence pointer.
- Blocker: requires outside authority — route bindings `@m_composer`/`@m_grok`/`@m_antigravity`+`@m_zfl` and a fresh L1 session (LOG.md 2026-10-15; `.ufo/continuation/fleet-round-1.md` §Unblock). Sequence after the fleet unblock; do not substitute lane-owned checks.

**C2 — coverage (lane-internal; can run now).** Corpus canonical-sync: add the 13 missing coverage-map rows, a `## Frontier`/known-gaps section to corpus/README.md, re-stamp all 19 knowledge entries with `source:`/`verified-at:`/`recheck:` headers (append-style, preserving existing anchors), and reshape PROVINCE.md to Core/Frontier/Adjacent.
- Before → after: 9 rows / 6 of 19 indexed / 0 Frontier / 0 headers → 19 rows / 19 indexed / 1 Frontier / 19 headers.
- Counting commands: `grep -cE '^\| `+'`'`+`knowledge/' corpus/README.md`; `grep -c 'Frontier' corpus/README.md`; the §3 per-file provenance loop.
- Serves **SOURCES.md** directly: the coverage rows' source columns are the seed S-rows (the tool + six surveyed gates are own-work/primary sources); serves new knowledge entries for the 13 unindexed notes. This is wave-2 groundwork per the SOURCES.md contract.

**C3 — freshness (lane-internal; can run now).** Clear the two owed re-sweeps: re-run tsukuroi-census and mado-verify mutation sweeps at their current HEADs, append ledger rows (re-pin, never re-interpret), and land the runbook ER-R3 re-stamp.
- Before → after: pin read 4 current · 2 stale · 0 drift (round-11 tick, five independent firings) → 6 current · 0 stale · 0 drift.
- Counting command: the tool's pin read / `grep -c 'stale' corpus/knowledge/fleet-kill-rate-ledger.md` → 2 → 0 (reading rows).
- Serves a new knowledge entry (re-sweep receipts at live revisions) + an own-work SOURCES.md row for `tools/mutate-and-run.sh`.

**Administrative obligations for the same round** (AXES.md SCORECARD contract): declare the saturation line + stagnation window N (D11); enter the demonstrated capabilities as rows with evidence pointers (D12); populate the standalone `## Planned` (D13). Fleet-level fixes owned by the integrator, not the lane: roster row (D5), fleet-root round reports (D6), MANIFEST round-1 row + freshness-verdict skew (D15).

---

### Sweep provenance

- Reads: lane LOG.md (549 L, full), SCORECARD.md (173 L), PROVINCE.md, SHONEN.md, MINT.md, AGENTS.md, corpus/README.md (raw), corpus/QUALITY.md, corpus/lessons/round-1.md + round-10.md (full), plans/round-11.plan.md:13-25, reports/round-1-calibration.md headings, .ufo/continuation/fleet-round-1.md headings, fleet MANIFEST.json (programmatic scan), fleet AXES.md, canonical CORPUS.md + templates/mint/PROVINCE.md, SKILL.md heading map (1,476 L file, headings only).
- Executed: git status/log; commands C and D at HEAD; all §3 counting commands; the §5 defect greps; the /tmp existence check; the fleet-reports find; the roster scan.
- Not done (out of scope for STATE): web research, SOURCES.md drafting, any re-measurement of landed verdicts (the lane's own rule: "nothing is re-measured and no verdict is re-adjudicated" — SCORECARD.md verdict-table preamble).
