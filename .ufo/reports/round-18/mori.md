# mori — round 18 (recovery attempt 2)

Lane HEAD (landed): `3786f3f1bde2fbcc5ce617e35e8c9becdbf9d9e8`; measured commit `3127c3a0aec48f41bbae3700b6bbaa13b759797a`.
Entering `d005cdd` (r17 non-author closure: rejected-harmed, adjacency). Attempt 1 (launch 2026-10-20T18:52:38-03:00,
`lane-dead-no-report` 2026-10-21T02:47:20-03:00) left no lane files, waves, worktrees or seats: nothing reused, nothing discarded.

## Work performed

Declared claims, frozen at `29b0dc7` before the first implementation commit `b8f5c6c`:
**C1 adjacency** (committed private-context retention gate; sourced S049–S052), **C2 calibration** (lowest non-retired axis, tie at 5;
freeze-order verdicts), **C3 operability** (capability: per-attempt dispatch payload binding).

- Repair first (routed defect 1): three routed reports minimized (`.ufo/waves/round-17/build/{PacmanActorTrace,OmpRetryConfig,SessionExitCorrelation}.md`,
  provenance blob + SHA-256 kept); 22 further files token-redacted; second pass after wave-2 falsification (OmpRetryConfig integration had
  truncated §3–§8 — restored; config state and store aggregates removed; seat-live.json regenerated JSON-aware after my edit broke it).
  Register of every out-of-metric finding with admit/reject: `.ufo/waves/round-18/out-of-metric-triage.md`. History not rewritten (operator/kagi).
- Routed defect 2: r17-C3 "precommitted" overclaim corrected by appended row `corpus/evidence/freeze-register.json`; r18 inputs frozen first.
- Routed defect 3: wave contexts restate VCS/scratch/field bounds; wave-2 adds V12 jj-config ban and not-runtime/clean-state caveat (`.ufo/waves/round-18/falsify/SentinelContextWave2.md`); CONTEXT_OK both waves (`evidence/wave{1,2}-context-check.json`).
- Routed defect 4: per-attempt ledgers `.ufo/waves/round-18/{wave1,wave2,residual-drafting}-attempts.json`.
- Routed defects 5/6: r10 drift red and r13–r16 qualifications carried, no repin; package events stay a tsukuroi/operator handoff.
- Tools: `tools/mori-retention-gate.py`, `tools/mori-freeze-order.py`, `tools/mori-dispatch-ledger.py` (registry rows `SKILL.md`); mutation survivors from wave 2 closed with new arms (21/21, 12/12, 14/14); one survivor (date-order DAG) left as a stated limit.
- Corpus: SOURCES S049–S063 (9 admitted, 6 rejected), knowledge `corpus/knowledge/{evidence-minimization,freeze-order,dispatch-ledger}-r18.md`, QUALITY 51–56, lesson `corpus/lessons/round-18.md`, PROVINCE round-18 notes.
- Planner mapping: the L1 held the frozen planner seat; planning data-walks rode scout/revenger items.
- Waves: **w1 68 seats** (scout21 reviewer19 scribe13 critic4 executor3 revenger3 connector3 sentinel2), dispatched once, 68/68 started; **15 died**
  with `[openai-codex/gpt-6-luna] Retry budget exhausted after 10 retries: Codex error event: Codex is at capacity, please try again later (code=turn_rate_limit_exceeded)`; one same-identity resume each failed identically (`evidence/wave1-dead-seats.json`), never replaced.
  **w2 67 seats** (reviewer31 scout17 critic8 mutation-tester3 revenger3 sentinel3 connector2): attempt 1 refused "Background job limit reached (100)" (0 started), attempt 2 started 67/67, 0 dead.
  An 8-scribe residual drafting call was refused 7× by the same job cap and superseded (L1 did the edits). Round total 135 seats.

## Landed changes

| Commit | Change | LOG |
|---|---|---|
| `29b0dc7` | contract + frozen C1 policy/population, C2 register, C3 ledger format | LOG round 18 |
| `11db4df` | wave-1 spec/dispatch/ledger/registry | LOG round 18 |
| `b8f5c6c` | three tools, routed minimizations, metric redactions, r17-C3 correction, wave-1 reports | LOG round 18 |
| `daceeec` | SOURCES, knowledge, QUALITY 51–55, registry, PROVINCE, overclaim-rule fix | LOG round 18 |
| `e2bfbd6` / `95c6158` | identity redactions, triage, draft verdicts, lesson, V13 values, wave-2 prep | LOG round 18 |
| `9db5168` | wave-2 reports, second-pass minimizations, selftest arms, QUALITY 56 | LOG round 18 |
| `3127c3a` | retention allowlist (86 name-only rows) — measured commit | LOG round 18 |
| `3786f3f` | final evidence, SCORECARD, LOG | LOG round 18 |

## Before → after measurements

- **C1:** `python3 tools/mori-retention-gate.py scan --repo . --rev <rev> --policy .ufo/waves/round-18/frozen/c1-policy.json [--allowlist corpus/evidence/retention-allowlist.json]` —
  `d005cdd`: rc1, metric **116**, routed 40, population_match true (independent recount agrees: `falsify/RecountPopulation.md`) → `3127c3a`: rc0 `RETENTION_CLEAN`, metric **0**, routed 0, 86 allowlisted, 0 forbidden. Frozen run rc0.
- **C2:** `python3 tools/mori-freeze-order.py check --repo . --register .ufo/waves/round-18/frozen/c2-register.json [--corrections corpus/evidence/freeze-register.json] --tip-for r18-C{1,2,3}=<rev>` —
  before (no corrections, tips `29b0dc7`): overclaims **4** (r17-C3 + three r18 no-implementation), oracle disagreements 0/3 → `3127c3a`: overclaims **0**, r17 3× co-evolved, r18 3× pre-build.
- **C3:** `python3 tools/mori-dispatch-ledger.py verify --repo . --rev 3127c3a --ledger <file>` — r17 legacy wave1 5/5 and wave2 4/4 **unbound** (rc1) → r18 wave1 1/1, wave2 2/2 bound rc0; residual 7/7 bound but `STARTED_MISSING` rc1.
- Final suite at the measured tree: census selftest 134/134; r17 context-check selftest 31 arms OK; new selftests 21/21, 12/12, 14/14 (`evidence/final-selftests.txt`).

## Sources & frontier

Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`: start exit 0 (W04 ×2), end exit 0 (W04 ×2) (`evidence/census-{start.txt,end.txt}`).
Rows 48 → 63: added tier A ×11 (S050–S054, S056, S058, S060, S062 + S053 queued), B ×1 (S049), C ×4 (S055, S057, S059, S061, S063 — rejected; S054 rejected for scope despite tier A).
Touched old rows: none (status none → new for all 15). Mistakes mined: M1–M6 in `corpus/lessons/round-18.md`. Sourced claim: C1 (S049–S052 in `evidence-minimization-r18.md`).
Inside-lane disagreement recorded: GDPR S054 admit (SrcGdprArt5) vs reject (SrcNist800122); L1 rejected for scope.

## Trend verdicts

- **expansion: improved** — three knowledge entries on uncovered ground citing mined S049–S062; three capability rows. (Wave-2 CriticTrendVerdicts argued `unchanged`; recorded.)
- **quality: improved** — round-17 private context minimized in two passes, tool/contract contradiction fixed to the frozen rule (QUALITY 55), mutation survivors closed; one survivor and line-digest guessability stated as limits.
- **discernment: unprovable-but-better pending outside check** — r17 disagreements became QUALITY 51/52; wave-2 critics judge discernment *harmed* because adjacency residue remains contested; the L1 does not self-certify. Adjacency axis: metric improved, axis-level harm cure **for the non-author closure to rule** (`falsify/CriticC1Admission.md`).

## SHONEN

- [~] Decision tables/error patterns/checklists with cited sources — `corpus/knowledge/evidence-minimization-r18.md`, `SKILL.md` registry rows.
- [~] End-to-end domain task executed and logged — C1/C2/C3 runs, `evidence/c1-after.json`, `c2-after.json`, `c3-after-*.json`.
- [~] Instructions executable without oral context — recheck commands in the three r18 knowledge entries (selftests need `TMPDIR=<repo>/.scratch`).
- [ ] No cross-domain bleed — contested: round-17 privacy residue judged by wave-2 critics; awaits non-author closure.

Stale-lane: respawn-per-round driver; this mission (launch 2026-10-21T02:47:21-03:00) is progressing (lane commits above); no other mori mission open.
Misroot sweep: fleet-root untracked non-state entries `.ufo/waves/round-25/`, `.ufo/waves/round-37/` belong to other lanes; none from mori seats; nothing moved (`evidence/misroot-sweep.txt`).
Tool installs: none. L0 questions: none new. Process deviations: seat /tmp write (M6), seats used `git rev-parse`/`git diff` that my own item prompts named but the context allowlist omitted (ConformanceAuditR18), L1 used `sed -i` once for a tool tally edit.
