# kumitate — round 78 (hyaku run-15; attempt 1)

Lane: `/home/vgpnk/Projects/shokunin/kumitate-shokunin` (axes: **operability + coverage** —
orchestration and tooling). Base `0b4df07b6f7478e7db6afb6852c418e096663c3c`; scaffolding
`ad2630d0566a561ee078f47fade5644a22c10621`; final lane tip `94ab406521369a11621103b1b22e6fe95bbeeab9` (pushed; `ls-remote` equal).
Host: Linux 7.2.11-arch1-1 x86_64, node v24.21.0. **Stale-lane:** none — the hyaku driver is
respawn-per-round; no other mission of this lane is open. Tools installed: none.

## Work performed

The round declared **two claims**: **C1** `coverage:kimi-layer` — the K plane's score becomes a
derivation of the census decision (findings included) instead of a private duplicate table; **C2**
`operability` — capability acquisition **`omp-shape-compare`**, a count-only, non-scoring
live-vs-receipt drift diagnostic. ONE v1 wave of 14 seats + the L1 planner seat; every claim was
frozen with controls before data (`plan.md`, `## Amendment 1`–`4`).

- **C1 mechanism landed.** `scripts/kimi-census.mjs` exports `decide(root)` (members, findings,
  identities, byBasename, rows, counts); `scripts/proxy-check.mjs` imports it, deletes
  `K_MEMBER_RULES` (5 occurrences → 0), adds the `K_findings` stanza term and derives
  `coverage_kimi = floor(10 × C1k/C1k_total × (K_members − K_findings)/K_members)`. Evidence:
  `scripts/proxy-check.mjs:325` (import), `scripts/proxy-check.mjs:949-950` (terms),
  `SCORECARD.md` stanza (`K_findings=0`), `close/c1-probe.txt`
  (`C78_C1: HELD held=12/12`), `close/proxy-json.txt`.
- **C1 harm found and reported, not smoothed.** The frozen formula *replaces* the
  `K_sections/K_members` factor. With one member-naming heading de-named, the base tree's score
  moves 10 → 9 while the patched tree stays 10 (only `K_SECTIONS_DRIFT` fires). Receipt:
  `close/harm-counterexample.txt` (both trees, both commands, verbatim outputs), first raised by
  the critic seat (`build/K78CriticClaims/section-loss-witness.json`, `amended-plan-observed.md`).
  **C1 is reported `held-but-harmed` and not admitted**; the L0 ruling is open (accept the
  redefinition, pre-register the composite in r79 with a discriminating arm, or revert the
  formula).
- **C2 mechanism landed.** `scripts/omp-census.mjs --compare FILE [--root DIR]` prints
  `OMP_SHAPE_COMPARE: IN_SYNC|DRIFT entries=<live> receipt=<n> added=<a> removed=<r> changed=<c>
  first=<name>` (first on DRIFT only); exit 0/1/2 (`SHAPE_INVALID`, `SHAPE_NOT_FOUND`,
  `ROOT_NOT_A_DIR`); count-only, shape-only, non-scoring, exclusive with `--snapshot`/`--shape`.
  Evidence: `close/c2-probe.txt` (`C78_C2: HELD held=11/11`), `close/c2-non-scoring.txt`,
  `close/omp-census-selftest.txt` (79 cases), `close/mutants-c2.txt`
  (`MUTANTS78_C2: ALL-KILLED killed=10/10`).
- **Frozen counters and controls before data** (`ad2630d0`): `probe/probe78-c1.mjs` (12 arms),
  `probe/probe78-c2.mjs` (11 arms), `probe/kimi-fixture.json`; base-tree controls 4/12 and 2/11,
  constant-printer controls 5/12 and 5/11 (`controls/*.txt`, each naming `probe-sha256=`).
- **Counter amendments, all before any claim verdict** (`plan.md`): A1 the axes arm read `f.term`
  instead of the canonical `f.key` (`aa00be37…` → `5e9d9d4f…`); A2 the claim commands made explicit
  with `--lane` (the probes' three-`..` `DEFAULT_LANE` routed to r79, probe bytes untouched
  post-C2-data); A3 `first=` is DRIFT-only; A4 the A2 wording narrowed and arm 7's import gap
  disclosed (covered by SKILL checklist item 38).
- **r77 closure routed defects D1–D6 repaired** (status-neutral, not claims): `corpus/lessons/round-77.md`
  `## Erratum` (counter row 856 → 857; quote word counts 21 → 20 and 24 → 25; loader-exit
  annotation; the r76 why-not pointer); corrected r77 base-control receipts on the final counter
  bytes (`probe-sha256=d48390c3…`) at `.ufo/waves/round-77/close/r78-*`; the wave-floor definition
  stated against the template (round 78 meets it with 3 executors); evidence files at
  `build/K78ExecRepair77/`.
- **Seventh spotcheck recurrence repaired** in the scaffolding commit:
  `spotcheck-adopt --adopt corpus/lessons/round-77-verifier-spotcheck.md` → `wrote=both`;
  `README_MAP: CLEAN files=187 rows=187 covered=187`, `SPOTCHECK_MAP: CLEAN spotchecks=44
  uncovered=0` (`open/gates-open.txt`).
- **Mistake mined** (`corpus/lessons/round-78.md` `## Mistakes`): the C1 counter's scorecard-copy
  helper wrote two fixture files into the lane root because the destination was a relative path;
  captured by the §3 misroot sweep (`git status --porcelain`) before the scaffolding commit; fix =
  an explicit absolute destination under `--work`, re-run clean.

- **Wave and settlement.** ONE v1 wave, 14 seats spawned 03:39 and settled (all 14 seats returned output;
  0 dead): reviewer ×2 (`@m_zfl` route), critic, mutation-tester ×2, sentinel, connector, executors 3,
  scribes 2, scouts 2; planner = the L1. `w1-results.json` is committed. The C1 mutant seat's runner
  refused after plan A1 on the superseded counter digest — an honest refusal, not a survivor; the L1
  re-pinned the digest and fixed its copy filter (the frozen counter's `A` term counts every runnable
  file, so excluding `.ufo/waves` broke the baseline), then re-ran it: 8/8 killed. The sentinel seat's
  three findings are routed, not repaired: S1 (low) an unescaped newline in a root member name can inject
  a second line into `OMP_SHAPE_COMPARE` (`first=` must escape control characters); S2 (low) the exported
  `decide(root)` omits the owner-check default (the CLI and proxy pass the uid; the API trap is real);
  B1 (informational) an explicitly named receipt symlink is followed (inherited behaviour, not a root
  escape; the probe opens no member content — marker-free, 0 member-content opens in every trace).
  Round 79 carries all three with the pre-registered candidates.

## Landed changes

All lane changes are in one work commit and tie to the `LOG.md` round-78 entry:

| commit | content | LOG |
|---|---|---|
| `ad2630d0` | frozen plan, counters, fixture, open receipts, controls; r77 spotcheck adopted; stanza re-measured | scaffolding |
| `1c06b670` | the round's work: `scripts/kimi-census.mjs`, `scripts/proxy-check.mjs`, `scripts/omp-census.mjs`, `SCORECARD.md`, `SKILL.md`, `corpus/knowledge/shape-receipt-live-drift.md`, `corpus/knowledge/kimi-plane-single-derivation.md`, `corpus/README.md`, `corpus/lessons/round-78.md`, `corpus/lessons/round-77.md` (erratum), `corpus/SOURCES.md` (S228), `.ufo/pins/*`, `.ufo/waves/round-78/**`, `.ufo/waves/round-77/close/r78-*`, `LOG.md` | round 78 |
| `2ffcb26a`, `94ab4065` | settlement artifacts: `w1-results.json`, the late seat reports, the sentinel's security evidence, and the M2 re-measure (A 866 → 868) | round 78 |
| (this filing) | this report on the fleet repo, committed through `fleet-commit.sh --as kumitate` | round 78 |

## Before → after measurements

Each claim's counter is frozen in `plan.md` and re-runnable verbatim.

- **C1** — `node .ufo/waves/round-78/probe/probe78-c1.mjs --set c1 --lane .`
  before (base tree `git archive 0b4df07b`): `C78_C1: HELD held=4/12` exit 1
  (`controls/c1-base.txt`); after (M = `94ab406521369a11621103b1b22e6fe95bbeeab9`): `C78_C1: HELD held=12/12` exit 0
  (`close/c1-probe.txt`). Constant-printer control 5/12 (`controls/c1-stub.txt`). Key terms:
  `K_MEMBER_RULES` 5 → 0; clean fixture `K_findings=0 coverage_kimi=10`; a `0400`-floor loss
  `1 → 9`; stray `1 → 9`; missing `54/1 → 9`. **Verdict: predicate held; axis harmed** (see
  `close/harm-counterexample.txt`) — not admitted.
- **C2** — `node .ufo/waves/round-78/probe/probe78-c2.mjs --set c2 --lane .`
  before (base tree): `C78_C2: HELD held=2/11` exit 1 (`controls/c2-base.txt`); after (M):
  `C78_C2: HELD held=11/11` exit 0 (`close/c2-probe.txt`). Constant-printer control 5/11
  (`controls/c2-stub.txt`). **Verdict: improved** (capability row entered).
- **Mutation batteries** — C1: `MUTANTS78_C1: ALL-KILLED killed=8/8` (`close/mutants-c1.txt`);
  C2: `MUTANTS78_C2: ALL-KILLED killed=10/10` (`close/mutants-c2.txt`).
- **Selftests** — proxy 156/156 (`close/proxy-selftest.txt`), kimi-census 56/56
  (`close/census-selftest.txt`), omp-census 79 cases (`close/omp-census-selftest.txt`).
- **Gates at close** — `PROXY: MATCH --strict` (`close/proxy-check.txt`), A 859 → 868, C 37 → 39,
  C2/C2_total 187 → 189, `README_MAP: CLEAN files=189 rows=189 covered=189`, `SPOTCHECK_MAP: CLEAN
  spotchecks=44 uncovered=0`, checklists 39/39, `SOURCE_CAPTURE: CLEAN captures=59`,
  `SOURCES_CHECK: CLEAN rows=167`, `KIMI_CENSUS: CLEAN (members=55 …)`,
  `OMP_CENSUS: CLEAN (source=snapshot entries=64 findings=0 bound=35/35)`.

## Sources & frontier

- **`SOURCES.md` rows 166 → 167** (tier A 142 → 143), count command:
  `node scripts/sources-check.mjs` → `SOURCE_CAPTURE: CLEAN captures=59 exemptions=108`;
  `sources-census.sh validate --root … kumitate` → exit 0 (start and end, six carried W04).
- **Added:** S228 (Terraform CLI `plan`, `#detailed-exitcode`; tier A, kind `docs`; capture
  `.ufo/waves/round-78/build/K78ScoutOpen/terraform-plan.html`, 276352 bytes, sha256 `a501ef22…`;
  quote 19 words, located at `-detailed-exitcode`). **Rows touched:** S228 new → `mined`; S227 and
  S226 re-opened with no change.
- **Frontier advanced:** `knowledge/shape-receipt-live-drift.md` (capture-time proof vs
  present-tense drift; the exit-code contract; the non-scoring boundary) and
  `knowledge/kimi-plane-single-derivation.md` (the census-owned K derivation and its limit).
- **Assimilation: none.** `merge/kumitate/` re-opened read-only and refused again as a bulk append
  (155 rows / 161 lines / 70 entries; CORPUS.md rule 4); flip: a dedicated assimilation round.
- **Adjacency (connector seat):** `build/K78ConnectSiblings/` — no sibling lane owns this round's
  exact ground; `chousa`'s anchor-boundary rule is the nearest generic practice (cited, not
  absorbed). `PROVINCE.md` byte-unchanged.

## Trend verdicts

- **expansion — improved.** One admitted sourced entry and one derivation note on ground the lane
  did not hold; SOURCES 166 → 167 (tier A 142 → 143); README map 187 → 189 with no uncovered file.
- **quality — improved.** The K plane's evidence chain is single-sourced (import, not duplicate
  table), the OMP receipt gained a live-vs-receipt reading, and both new mechanisms carry selftests
  (79 cases) and killed mutant batteries; the r77 closure's six defects are repaired and the 7th
  spotcheck recurrence is closed.
- **discernment — improved.** The round's own attack seats changed its outcome: the critic's
  section-loss counterexample turned C1 from an "improved" claim into `held-but-harmed`, and the
  freeze review found two counter defects before any verdict (A1, A2). Neither was smoothed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the
  round adds one gate-row clause and two executable items (39/39 pass, `close/checklists.txt`);
  non-author verification of the wording is not on record this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the K derivation and the
  OMP comparison ran end-to-end on this host; `LOG.md` round-78 entry cites both.
- [~] Instructions executable by an agent without oral context — the plan + counters + controls
  reproduce the round's measurements from committed bytes (`plan.md` A2 commands).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` byte-unchanged; the
  connector's sibling scan adds no absorbed material.
