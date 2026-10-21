# kumitate — round-35 report (hyaku block 35–44, attempt 1, 2026-10-20)

Lane `/home/vgpnk/Projects/shokunin/kumitate-shokunin`, branch `master`, base `1770305fae20826b39905a8251ddeca6b4957ac4`.
Landed lane commit: `4c9e40759d0946d8abac07d87ea0b6363fa8dbc3` (author `kumitate-shokunin <kumitate@shokunin.local>`,
helper line `landed 4c9e40759d0946d8abac07d87ea0b6363fa8dbc3`, remote verified). Upstream source pinned through a private
read-only clone at `31c465f15669f744848bd9f5d56191c5085670f7` (base `964f443e` in the same clone); the operator's
`~/Projects/ufo-fsd-alpha` was never checked out, reset or edited.

## Work performed

Declared claims (3; frozen before implementation; causally separable — seat ReviewSeparability rebuilt one tree per claim):

1. **C1 — operability (lowest live axis, 8): distinct S/R member derivation** in `scripts/proxy-check.mjs` (pre-registered since round 17).
2. **C2 — coverage:script-layer 9 → 10 at the pinned origin `31c465f1`**: S8 re-census after the upstream advance (members 91 → 88).
3. **C3 — coverage:kimi-layer: pre-registered K1 registry change 3 → 4**, root `~/.kimi-code/mcp.json` as a shape-only member.

Work items:

- Fresh baseline before any edit, at the pin: `.ufo/waves/round-35/baseline/` (proxy DRIFT S 86/88, claims 6 errors, census DRIFT UNLISTED mcp.json, checklist 9/13). Frozen populations: `.ufo/waves/round-35/frozen/` (55 modified, 2 added, 5 deleted S members).
- C1: `layerTerms()` counts distinct in-family `section.file` identities per layer; 5 new hermetic cases (S and R duplicate/drop, distinct control, cross-row, heading alias); `pin.proxy-check` re-pinned. Evidence: `SCORECARD.md` `## Move log` round-35 row; `.ufo/waves/round-35/final/mutation.txt`.
- C2: `corpus/knowledge/remaining-scripts-census.md` — 2 new member sections (`omp-route-grammar.mjs`, `ufo-swarm-registry.mjs`), 5 departed members kept as history bullets, 36 changed sections re-anchored at the pin (56 fidelity seats + seats ExecS8Fidelity/ExecS8Fix), registry cell S8 63 → 60 (a measurement: seat ReviewS8Membership).
- C3: `scripts/kimi-census.mjs` K1 member `mcp.json` (secret leaf, 0400 floor, never read), FROZEN K1 4, selftest 45 → 48; `scripts/proxy-check.mjs` K rule + 30-member fixture; `corpus/knowledge/kimi-mcp-plane.md` round-35 section (S005, S022).
- Riders: R11 `round.rs` dead anchor re-anchored (`corpus/knowledge/runtime-remainder-census.md`); README rows for the round-34 verifier note and the round-35 lesson (C2 77/78 → 79/79); round-32 Move-log row + LOG bullet (`round-gate --round 32` DRIFT → CLEAN); Q11 retro-admission entry for `16a5441` (`LOG.md` end); Q15 in `corpus/QUALITY.md`; fidelity notices at the top of the 11 S1–S7 notes (624 non-ok anchors counted, not fixed).
- Frontier: `corpus/SOURCES.md` 20 → 28 rows; lesson `corpus/lessons/round-35.md` (`## Mistakes` 8 rows, `## Gate`, `## Falsify wave`).
- Planner seat: held by the L1 (frozen topology); the bounded planning data-walk rode seat ScoutPlannerWalk (scout).

## Landed changes

All in `4c9e40759d0946d8abac07d87ea0b6363fa8dbc3`, logged in `LOG.md` round 35 (bullet `- 2026-10-20 — round 35`, plus the falsify-wave paragraph and the Q11 entry that follow it):

| Change | Files | LOG pointer |
|---|---|---|
| C1 distinct derivation + 5 cases + pin | `scripts/proxy-check.mjs`, `SCORECARD.md` | round-35 entry, Claim 1 + falsify paragraph |
| C2 S8 re-census + re-anchoring + registry cell | `corpus/knowledge/remaining-scripts-census.md`, `SCORECARD.md` | Claim 2 + falsify paragraph |
| C3 K1 member + census/proxy rules + note | `scripts/kimi-census.mjs`, `scripts/proxy-check.mjs`, `SCORECARD.md`, `corpus/knowledge/kimi-mcp-plane.md` | Claim 3 |
| Riders, frontier, lesson, notices, docs | `LOG.md`, `SKILL.md`, `corpus/{QUALITY,README,SOURCES}.md`, `corpus/lessons/round-35.md`, 13 knowledge notes | Riders + falsify paragraph |
| Wave evidence (specs, dispatch, registries, 170 seat reports, patches, final gate outputs) | `.ufo/waves/round-35/` | round-35 entry |

## Before → after measurements

All "after" values on `4c9e407…` with `--src` = the clone pinned at `31c465f1` (`.ufo/waves/round-35/final/*.txt`).

- **C1 (operability; integer 8 held, `f_O` 20/23 unchanged).** `bash .ufo/waves/round-35/mutate-distinct.sh.txt --self <tree> --src <pin>`: master `MUTATION_KILLS 0/2` (S 86→86, R 83→83) → `MUTATION_KILLS 2/2` (S 88→87, R 83→82). `node scripts/proxy-check.mjs --selftest`: 104/104 → `PROXY_SELFTEST: 109/109 pass`; the row-scoped and heading-keyed mutants left alive by the falsify mutation seat now fail at 107/109 each.
- **C2 (coverage:script-layer).** `node scripts/proxy-check.mjs --src <pin>`: before `PROXY: DRIFT (… S_MEMBERS_DRIFT … declared=91 computed=88 …; S_SECTIONS_DRIFT … computed=86 …; COVERAGE_SCRIPT_DRIFT … computed=9 …)` ⇒ live 86/88 = **9**; after `PROXY: MATCH (A=7 C=13 operability=8; C1=19/19 C2=79/79 coverage=10; S=88/88 coverage:script-layer=10; R=83/92 coverage:runtime-layer=9; K=51/51 coverage:kimi-layer=10; pins=6 match)` ⇒ **10**. `node scripts/claims-check.mjs --src <pin>`: 6 errors → `CLAIMS: MATCH (rows=19 yes=19 notes=27 sections=175 adv=6)`; `--row S8` sections=60, errors 0. S8 note: dead own-file anchors 36 → 0, fidelity-sweep regressions 41 → 0, per-file cite-check errors 91 (master clone) → 30.
- **C3 (coverage:kimi-layer; integer 10 held).** `node scripts/kimi-census.mjs`: `KIMI_CENSUS: DRIFT (UNLISTED mcp.json)` exit 1 → `KIMI_CENSUS: CLEAN (members=51 checked=51 chain=7 info=4)` exit 0; proxy K 50/50 → 51/51; census selftest 45 → 48/48; `strace -f -e trace=open,openat,openat2 node scripts/kimi-census.mjs 2>&1 | grep -c 'mcp[.]json'` → 0 (2 stat-family calls).
- **Round records / no-harm.** Checklist (`UFO_SRC=<pin> node scripts/surface-probe.mjs --checklists`) 9/13 → 12/13 (item 620 red: upstream `VERB_UNDECLARED surface` + lane probe digest order, round 36). `round-gate --round 32` DRIFT (2 errors) → CLEAN; `--round 34` CLEAN. All 7 hermetic suites PASS (cite 62, surface 42, round-gate 60, proxy 109, kimi 48, sources 46, claims 39). Per-file cite-check vs a master clone with the same src: no edited file rose. `git log --format='%ae' -1 master` → `kumitate@shokunin.local`.

## Sources & frontier

- Rows: `grep -cE '^\| S[0-9]{3} \|' corpus/SOURCES.md` 20 → 28; census `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate` → `ok` exit 0 at start and at end; `node scripts/sources-check.mjs` → `SOURCES_CHECK: CLEAN (rows=28 tiers=A:27,B:1,C:0 status=queued:14,mined:12,rejected:2 …)`.
- Added by tier: A 8 (own-work 1, docs 6, spec 1). Mined 3 (S021 → S8 note, C2; S022 → kimi-mcp-plane, C3; S023 → lesson, C1); queued 5 (S024–S028).
- Rows touched old→new: S005 used-by + `corpus/lessons/round-35.md`. Pre-landing amendments to this round's own rows from the falsify re-opens (S021 count, S022 Last-Modified, S024 teaches scope, S025 canonical URL, S026/S028 revision anchors). S020 flip re-checked, still unmet.
- Frontier advanced: five queued leads opened (OMP MCP config, Anthropic agent vocabulary, MCP Tasks extension, git 2.55 worktree note, LangGraph durability modes); two follow-on leads added.
- Sourced claims: C1 rests on S023, C2 on S021, C3 on S022 (+ S005), each cited by its used-by path.

## Trend verdicts

- **expansion: unchanged.** No new admitted knowledge entry on uncovered ground (CriticTrends); the two new S8 sections restore coverage of a family that moved, and 5 of 8 new rows are queued.
- **quality: improved.** Stale entries re-verified at the pin and fixed (S8 note 36 dead anchors → 0; one materially false section, `fleet-ledger-rotate.test.mjs`, rewritten; R11 dead anchor fixed); the S1–S7 debt that remains is now marked in situ (11 notices), not left unmarked. Reviewer RerunClaims: no new advisory; master's 6 errors gone.
- **discernment: unchanged.** No non-author spot-check exists for this round yet (the closure session is pending); Q15 is grounded in a mined mistake; S020's flip was refused on evidence. Lane-dispatched critics are still the lane (LEARNING.md).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `## Verifiable checklist` (12/13 pass, `.ufo/waves/round-35/final/checklists.txt`), `corpus/SOURCES.md` 28 rows.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round 35: upstream advance detected → pinned clone → re-census → gates MATCH.
- [~] Instructions executable by an agent without oral context — `corpus/QUALITY.md` Q15 + `## How to apply`; checklist-source pinning pre-registered for round 36.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — upstream defects and sibling overlaps below are routed, not absorbed.

## Mistakes (frontier step 3)

8 classes in `corpus/lessons/round-35.md` `## Mistakes`: pre-registered baseline on a moving tree (fix Q15); checklist pass count contradicted by the gate; checklist verdict follows the moving checkout (round 36); wave scratch `.mjs` entered the A walk (A_DRIFT 7→8; evidence now `.txt`); out-of-lane note landed without a map row; seat writes outside scope (one report misrooted to the fleet `.ufo/waves/round-35/build/`, moved byte-exact into the lane, `cmp` OK, fleet copy deleted; one seat's stray edit restored from `master`); executor patch delivered unrun and dead on arrival (fixed by the L1); anchors wrong at their own stated revision.

## Swarm and seats

- Wave 1 (build): one validated `task` call, **95** seats — scout 41, reviewer 33, scribe 9, executor 5, critic 3, connector 2, revenger 1, sentinel 1. Spec/dispatch/registry: `.ufo/waves/round-35/build-spec.json`, `build-dispatch.json`, `build/swarm-registry.json`.
- Wave 2 (falsify): one validated `task` call, **75** seats (75 distinct attack items) — reviewer 33, scout 33, critic 4, mutation-tester 4, sentinel 1. Verdicts 48 holds / 26 partial / 1 refuted (SCORECARD round-32 baseline + K1 "kind file" wording, both corrected); no claim refuted.
- Ordinary writer tasks: 2 executors (ExecS8Fidelity, ExecS8Fix), private clones. Round total **172** seats. Dead seats: **0**. The host `task` tool requires `solutionSpace`; it was added per role to the validator's `{name, agent, task}` entries, nothing else changed. Answering models were not recorded per seat; no claim depends on them.
- Tool installs/updates: none (L1 and every seat reported none).

## Routed, not absorbed

- Upstream (operator): `scripts/ufo-sighting-lib/surface.mjs` manifest omits the `surface` verb that `scripts/ufo-sighting.mjs:4484` dispatches (`VERB_UNDECLARED`, since `72ab84a`); the dispatcher's status verb creates `<src>/.ufo` and fails on a read-only tree; stale "importSiblingModule"/"three pre hooks" comments.
- Cross-lane (seat ConnectorSiblingOverlap): game-dev-3d `reports/round-101/probes/kimi-surfaces.md:190-201` reproduces `~/.kimi-code/mcp.json` content, which kumitate treats as shape-only — security owners (kagi/kasegi) should look; tabi and kumitate both claim `plugins/managed/kimi-webbridge`; kaidoku and kumitate pin different `config.toml` lines.
- Host fact: `~/.kimi-code/mcp.json` is mode 0644; the census floor is owner-read only, so it passes.
- r34 spot-check (`corpus/lessons/round-34-verifier-spotcheck.md`): agree/agree, no disagreement to turn into a criterion; its missing README row is fixed this round; its glued-token adjudication text is integrator-owned and was not edited.

## Inherited state and boundaries

- Inherited: none (no `lane-dead-no-report kumitate round=35` attempt; lane clean at `1770305`). Integrator-authored `corpus/lessons/round-34-verifier-spotcheck.md` read, not edited.
- Fleet paths written: this report; one misroot deletion (above). No MANIFEST, fleet scripts/templates/state, sibling, `~/.kimi-code`, `~/.omp` or routing writes. `.ufo/state/*.report-baseline` files are watchdog state, not touched.
- L0 questions: none appended.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
