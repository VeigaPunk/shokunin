# tameshi round 43 report

L1 tameshi, hyaku run 6, attempt 1 (2026-10-25). Lane HEAD at report time: `718a1e987febd32eb78ebc65adfe939f23b3de63` (the deciding measurements were taken at `3c4003f6e97e5c787e7538b2eb35d62f49783aaf`; the freeze of record is `6b83a11c61f0fad1074ec1f2a4c38a2fd7034685`; amendment chain A1–A14, all pre-deciding).

## Work performed

Claims (three, each falsifiable; contract `.ufo/evidence/round-43/contract.json` frozen before any seat and before the deciding run; amendments A1–A14 recorded there and in the lesson, all `when` before the first deciding run):

- **C1 (depth):** the two survivors of the round-42 mutant set (round-42 closure, `rejected-honest-stop`: C2 4/6) are resolved under the **pre-declared K/D/E/U rule** — `outflag_no_parse_args_check` killed by a reachable-code fixture `F11_outflag_namespace` (a `SimpleNamespace` whose attribute equals an argparse output-flag dest; the tool's documented rule says only a `parse_args` namespace counts); `method_fold_several_returns` named `dead_code_only` because it differs from the tool only on a fixture whose discriminating construct (a second top-level `return`) is unreachable. Mutant declaration unchanged and byte-pinned.
- **C2 (calibration, lowest non-retired axis at 6):** record agreement across seven classes — m6 m7 m8 m10 m11 carried from round 42; **m12** (the newest SCORECARD block carries the field `**Planned (round N+1):**`; the round-42 block had none) and **m13** (the newest standing sources-registry command is census-valid and load-bearing on an indented mirror) are new.
- **C3 (operability, capability acquisition):** `tools/staged-id-guard.py` answers the round-42 post-append hazard before any append: census-valid 0–3-space collision extraction, document-keyed dedupe, refusal of its own naive arithmetic map (its targets are still staged ids), refusal of maps that move a held document off its registry id or decide an undocumented row, and admission of a by-document map whose fresh targets are at or above the safe floor.

Frontier step (§2b) rode inside the round: sources opened (S159 Wikipedia; S089 Stryker re-opened), census before→after, a mined mistake per row, and a sourced claim (C1 rests on S089/S159/S155/S158). Assimilation: **none** (the package's staged ids were examined read-only for the collision hazard; no adoption).

Round shape: **default — two v1 waves** (policy v1, band 32–64). Wave 1 (build + first falsifiers): **34 seats** — 9 reviewer, 6 scout, 5 critic, 4 mutation-tester, 4 executor, 3 scribe, 1 connector, 1 sentinel, 1 revenger; 34 completed, 0 dead. Wave 2 (falsify, 34 fresh attack seats): 12 reviewer, 5 critic, 5 mutation-tester, 4 executor, 3 scout, 2 sentinel, 1 simplifier, 1 revenger, 1 scribe attack items only; 34 completed, 0 dead. Round total **68 seats**, ≤128, no residual call. The canonical §3 planner seat is held by the L1 (the validator rejects `planner` as a swarm role — recorded in the previous rounds; not bypassed). Both waves dispatched as exactly one `task` call carrying the validator's `taskCall` unchanged (`.ufo/waves/round-43/{spec,dispatch}-w{1,2}.json`).

Key work items and evidence: counters and receipts under `.ufo/evidence/round-43/{contract.json,before,control,prerun,after,census-sources,sources}/`; source snapshots (Wikipedia/stryker/pit) with `sha256.txt`; wave-1/2 seat reports under `.ufo/waves/round-43/w{1,2}/` (68 reports, all committed).

## Landed changes (all via the lane helper, all pushed; lanes landed: `697d2f1` freeze, `f0f2636` A1, `17f6ef0` A2/A3, `5cd2154` A4/A5, `114ffacd` A6/A7, `53cb32b` A8, `273c047` A9, `3aee2c0` A10, `c5335c70` records + wave-1 evidence, `b510ad1` A11 + quote/drift corrections, `bb36f80` A12, `f551ca69` A13, `6b83a11` A14, `3c4003f6` records corrections + wave-2 evidence, `718a1e98` deciding receipts)

- Freeze chain A1–A14: contract + three counters + guard tool, each step pre-deciding; the claiming bytes at `3c4003f6` equal the pins (self_pin=1 in every deciding run).
- C1 counter: K/D/E/U oracle with a **reachability gate** (a kill requires at least one failing fixture with no unreachable statement), per-fixture kill binding (`kill_binding`), pinned mutant declaration (`mutants_sha_ok`), differential probe over fixtures **and live sites**, and `--probe-mutant` that reports the gated class.
- C2 counter: seven classes with the value-id masks (staged:/next-unused/safe-floor), field form for `planned`, backticked command cell for m13, per-claim supersede re-assertion for m10, object-level m11, brace expansion and directory resolution for m8.
- C3 tool `tools/staged-id-guard.py`: 0–3-space extraction, `held` dedupe, naive-map cascade refusal, safe floor (no whole-set exemption), held-moved/undocumented/malformed refusals, digest emission, 24-case selftest.
- Knowledge: `corpus/knowledge/r43-survivor-resolution-rule.md` (new; S089 re-opened, S159 new, S155/S158 held; `verified-at`/`recheck` fields per criterion 10).
- Registry: one row added **S159** (Wikipedia, Mutation testing), 113 → 114 rows; used-by cells extended for S089/S155/S158; census exit 0 start and end (`.ufo/evidence/round-43/census-sources/{start,after}.stdout`).
- QUALITY criteria 83 (a survivor is classified, never relabelled) and 84 (a self-assessment count uses the pattern its registry accepts) + falsifier-correction errata.
- Lesson `corpus/lessons/round-43.md`: Gate (admit/re-open/deferral with located quotes, collision check, census, used-by log), Mistakes (twelve rows incl. duplicate-document append and digest-assertion), C1/C2/C3 instrument limits, Holds, considerthese correction.
- SCORECARD round-43 block with claim table, capability row, after-subsection; LOG round-43 section; README coverage row.

## Before → after measurements

### C1 — depth (counting command: `python3 .ufo/evidence/round-43/mutants/measure.py --lane LANE --rev REV --freeze FREEZE`)

- Before: round-42 counter at base `487b8f0` → `mutants_declared=6 mutants_killed=4`, survivors `outflag_no_parse_args_check` + `method_fold_several_returns` named, exit 1 (`.ufo/evidence/round-43/before/c1-round42-at-base.stdout`). Probes of both survivors against the round-42 ten-fixture battery: `probe_outcome=survived` (`control/c1-probe-survivors.stdout`). Do-nothing control (round-42 battery): `10/10 mutants_killed=4 C1_R43_CONTROL_PASS=false` (`control/c1-round42-battery-A10.stdout`).
- After (measurement revision `3c4003f6`): `mutants_killed=5 dead_code_only=1 equivalent=0 unresolved=0 kill_binding=1 dead_code_arg_ok=1 mutants_sha_ok=1 C1_R43_PASS=true`, exit 0 (`.ufo/evidence/round-43/after/c1-at-3c4003f6.stdout`). **Verdict: improved.** Wave-2 MutC1GateRemoved proved the reachability gate is load-bearing (removing it → `mutants_killed=6 dead_code_only=0`, PASS=false).

### C2 — calibration (counting command: `python3 .ufo/evidence/round-43/calibration/measure.py --lane LANE --rev REV --freeze FREEZE`)

- Before (base): `m12=1 m13=1 total=2 C2_R43_PASS=false`, exit 1 (`.ufo/evidence/round-43/before/c2-at-base-A10.stdout`; the final counter's base run also reports the block-round binding, total=3). Do-nothing control: the round-42 counter prints no m12/m13/classes fields (`control/c2-round42-counter.stdout`).
- After (measurement revision `3c4003f6`): `m6=0 m7=0 m8=0 m10=0 m11=0 m12=0 m13=0 total=0 records=4 sources_rows=114 C2_R43_PASS=true`, exit 0 (`.ufo/evidence/round-43/after/c2-at-3c4003f6.stdout`). **Verdict: improved.** Wave-2 mutation-testers confirmed the two new classes distinguish their shapes (m12 fires on prose, clean on the field; m13 fires on a column-zero command with prose `0,3`).

### C3 — operability (counting command: `python3 .ufo/evidence/round-43/guard/measure.py --lane LANE --rev REV --freeze FREEZE`)

- Before (base): `tool_absent=1 C3_R43_PASS=false`, exit 1 (`.ufo/evidence/round-43/before/c3-at-base.stdout`). Control: a constant-empty stand-in disagrees with the counter's own extraction → `C3_R43_CONTROL_PASS=false` (`control/c3-constant-empty-A10.stdout`).
- After (measurement revision `3c4003f6`): `selftest_cases=24 failed=0 staged_rows=103 live_collisions=7 live_collisions_agree=1 live_held=3 live_held_agree=1 live_unmapped=0 live_verdict=refused naive_map_refused=1 safe_map_admitted=1 map_dedupe_live=1 held_refused=1 naive_agree=1 substitute=0 C3_R43_PASS=true`, exit 0 (`.ufo/evidence/round-43/after/c3-at-3c4003f6.stdout`). **Verdict: improved (capability).** The live package collision set (S153–S159) contains three held documents (S153→S105, S154→S106, S159→S155); the naive map lands on staged ids (cascade) and is refused; the by-document map is admitted.

No axis harmed: depth 9 → 9 (command D), calibration 6 → 6 (round-21 coldread monitor), re-run at base and freeze by wave-1 ExecCommandD with byte-identical tool/`SHONEN.md`/monitor (`.ufo/waves/round-43/w1/ExecCommandD.md`). No SHONEN box moved.

## Sources & frontier

- Rows before → after: **113 → 114** (`grep -cE '^ {0,3}\| S[0-9]{3} \|' corpus/SOURCES.md` → 114). Added: S159 (Wikipedia, Mutation testing; tier A docs, mined, opened 2026-10-25, recheck 180d, snapshot 170793 B sha256 `6e4a06c0` revid 1373580212, two byte-identical fetches). Re-opened: S089 (Stryker equivalent-mutants; the bytes drifted from the 2026-10-22 anchor while every quoted sentence survives at the same offset, `last-modified` 2026-10-24). Rows touched old→new: S089, S155, S158 `used-by` cells gain `corpus/knowledge/r43-survivor-resolution-rule.md` (logged in the lesson). The Stryker document was **not** appended as a new row — the census W04 warning caught that S089 already holds that URL, the dedupe rule applied to the lane's own append.
- Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi` exit 0 at round start (113 rows; `start.stdout`) and exit 0 at round end (114 rows; `after.stdout`), identical 9 × W04 + 1 × W01 warning set, zero E codes.
- Frontier: C1 moves F1's survivor side (what an un-killed mutant is *called*, with the rule and the two fixtures); F9 is not touched (no LLM generated or classified a mutant). README coverage row added for `r43-survivor-resolution-rule.md`.
- Assimilation: **none** — the CR's staged ids were examined read-only by the guard; `Assimilation: none` line above. Quarantine slice re-derived read-only (17 data rows: 14 payload-absent, 3 could-not-be-fetched; same set as round 40/41). considerthese: proposal 5 of 2026-10-22 (survivor reclassification tracker) mined, not implemented; the paragraph corrected per wave-2 RevConsider.

## Trend verdicts

- **expansion: improved** — one admitted entry on ground the lane did not hold (the equivalence-problem separation and the K/D/E/U taxonomy on the survivor side), on two source rows (S089 re-opened, S159 new); the entry carries `verified-at`/`recheck` after the wave-2 criterion-10 finding. The capability row (staged-id guard) is a new repertoire entry.
- **quality: improved** — the two routed survivors are resolved with the rule and the fixtures; QUALITY criteria 83/84 added with falsifiers that fail (gate removal and mirror counts); the append-only repair held; the claim and its counter were attacked by 68 seats and 14 amendments before the deciding run, each ending in a disclosure or a repair.
- **discernment: improved** — the outside spot-check chain continues (round-43-verifier-spotcheck.md is written by the closure); the lens records the instrument limits the waves found, including the fixture-granular reachability gate, the presence/pattern nature of m12/m13, the per-claim supersede rule, and the guard's fragment-form document join; none was used to reach the verdicts.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — no standing command (considerthese table, round-42 lesson); `[~]` At least one end-to-end domain task executed and logged in LOG.md — round-43 LOG section lands this round; `[~]` Instructions executable by an agent without oral context — coldread monitor `python3 .ufo/evidence/round-21/coldread/measure.py --rev REV` exits 0 at base and freeze, selftest 12/12; `[~]` No cross-domain bleed (PROVINCE.md still accurate) — no tool reads PROVINCE.md; the guard's province scope (lane-local, census authority) is stated per wave-2 RevGuardScope. No box changed; all remain `[~]` lane-asserted.

Stale-lane: no other mission of this lane is open (respawn-per-round driver).

Misroot sweep (before report): `git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all` — the untracked set is driver/foreign (`.omp/mcp.json`, `.scratch/goal-20261025-hyaku-12h.md`, `.ufo/state/*` baselines, tabi r24 and kotoba r69 wave files); no tameshi round-43 seat misroot (wave-1/2 ScoutMisroot both report the same set with the two foreign files already filed by revenger r69).

Tool installs: none (curl/git/python3 pre-existing; pacman guard respected — no transactions; no `uv`/`npx`/binary installs recorded by any seat).

Open L0 questions: none new.
