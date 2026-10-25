# kotoba — round 51 report

Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, base `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`,
pushed lane head `588f5824c01068381f58c67b97fe288ab57bd9c6` (jj-lane.sh `landed`). Attempt 1. Plan
`plans/round-51.md`. This header is frozen; any later lane head goes in an appended addendum.

## Work performed

Declared claims (2): **C1 freshness** (lowest non-retired axis under the all-axes reading, 8.0, tied with
adjacency; adjacency was claimed in rounds 49 and 50) — run against the installed omp 18.12.6,
`python3 -B verifiers/verify_surfaces.py --json` passes 5 of 7 → 7 of 7 checks (the two omp checks 0 of 2 → 2
of 2). **C2 depth** (owned axis, lowest owned at 9; the learning claim and the sourced claim) — `SKILL.md`
§ Anti-patterns names, for 7 pinned clients, a reviewed lever other than description wording that removes
one named skill from the candidates, each backed by a quote in a new knowledge entry and a `mined` SOURCES
row: `check_overlap_levers.py` 0 of 7 → 7 of 7. Both statements were re-sized by the build critics before
landing (`plans/round-51.md` § Re-sizing). **C2 is not verified as declared:** see the measurements below.

- C1: callee allowlist `+Kl|Ho|bq`; the rebound group identifier `S$` resolves from the call's own module
  scope (an in-module ambiguity or a parameter shadow stays `<unresolved-var:NAME>`); new fixture
  `verifiers/fixtures/surfaces/strings-omp-18.12.6.txt`; `--json` prints the binaries it read; pins re-pinned
  (`verifiers/baseline.json` `measured_against` only). Commits `e0320302`, `533ff208`, `c363de7d`; seats
  `.ufo/waves/round-51/build/SurfacesRepin.md`, `PinsRepin.md`, `OmpCalleeCensus.md`, `CriticC1Sizing.md`.
- C2: entry `corpus/knowledge/skill-overlap-levers-round51.md` (supersedes round-50 finding 4), the table in
  `SKILL.md` § Anti-patterns, rows S030 and S031, used-by on S021, S022, S024, S025, S029; counter
  `verifiers/check_overlap_levers.py` (self-test 51, floored). Commits `7c81a787`, `34cfffbb`, `c363de7d`;
  seats `build/Src*.md`, `LeverGuard.md`, `CriticC2Sizing.md`, `CriticLearning.md`.
- Routed round-50 defects D1–D7, each fixed or explained in `corpus/lessons/round-51.md` § Routed defects and
  § Falsify-wave corrections: D1 `DescDraft.md` committed byte-exact (`e6219026`, sha256 `0181a459…`) and the
  seat accounting corrected in LOG.md and the lesson; D2 bounded in `SKILL.md:135-141` and the SCORECARD
  operability qualifier; D3 swept (`SKILL.md`, `corpus/README.md:72`, round-50 entry note, census S026 note);
  D4 erratum and row S030; D5 kama quote and kengaku correction (`PROVINCE.md`, census entry); D6 precedence
  rule marked provisional, not extended and not relied on; D7 carried with reasons.
- Frontier step: census before and after (below); rows S030–S031 opened this round; mistakes M33, M34, M35
  mined with criteria Q27 and Q28 (`corpus/QUALITY.md`); C2 rests on S030 and S031.
- Calibration: falsify seat `CriticCalibrationRows.md` counted 5 mismatches of 23 current-state statements in
  SCORECARD/SHONEN at `59903b26`; four answered by an appended SCORECARD calibration note, one (SHONEN box 1's
  "38" Sources entries; 39 by the round-46 method) reported, SHONEN unchanged.
- Corpus baseline re-record (`59903b26`): tracked 69 → 72, report_total 44 → 46, after indexing the
  closure-written `corpus/lessons/round-50-verifier-spotcheck.md` (`ReviewBaselineRerecord.md`: honest, add-only).

## Landed changes

| commit | what | LOG.md entry |
|---|---|---|
| `7c81a787` | plan with re-sized claims; C2 counter (self-test 22) | Round 51 landing |
| `e0320302` | C1: omp 18.12.6 re-derivation, fixture, re-pin, floors | Round 51 landing |
| `34cfffbb` | C2 content: entry, `SKILL.md` table, S030–S031, used-by; D2–D6; Q27; lesson | Round 51 landing |
| `e6219026` | D1: round-50 `DescDraft.md` byte-exact | Round 51 landing |
| `59903b26` | corpus baseline re-record | Round 51 landing |
| `533ff208` | frontier and Core rows, SCORECARD rows, calibration note, scope-proxy docstring | Round 51 landing |
| `c363de7d` | falsify corrections: C2 table and entry, hardened counter (51), C1 parameter-shadow fix (119), M35/Q28, LOG | Round 51 landing pin and falsify wave |
| `588f5824` | wave evidence: specs, dispatch payloads, gate grants, registries, 67 seat reports | Round 51 landing pin and falsify wave |

All eight landed through `scripts/hyaku/jj-lane.sh commit` as `kotoba-shokunin <kotoba@shokunin.local>`;
`jj-lane.sh state` → `local=remote=588f5824… ahead=0 behind=0 tracked=0 untracked=0`.

## Before → after measurements

- **C1** — `python3 -B verifiers/verify_surfaces.py --json` (no override flags), installed omp 18.12.6 sha256
  `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`: `{'exit_code': 1, 'fail': 2, 'pass': 5}` at
  `43ca0bfb` (14:09Z) → `pass 7, fail 0, exit_code 0` at `e0320302` and at `588f5824` (15:30Z). Companion
  `python3 -B verifiers/check_substrate_pins.py`: `DRIFT 2/3`, exit 1 → `OK 3/3 pins hold`, exit 0. Shown able
  to fail: base red on the same binary; the 18.12.6 fixture fails with the round-50 allowlist (self-test arm);
  disabling the module-scope rule gives pass 5 (`ReplayC1Counter.md`). Falsify replay: `ReplayC1Counter.md`,
  `CriticC1Landed.md`, `NoHarmGates.md` (HOLDS-BOUNDED). Bounds: the gate reads `strings`, not omp's runtime
  (`ScoutOmpRuntime.md`); 25 of 33 omp loader rows are substring probes; the source-path comment is a scope
  proxy; three fixture lines are unlabelled non-dump bytes (`FixtureFaithful.md`, carried).
- **C2** — `python3 -B verifiers/check_overlap_levers.py --rev <rev>`:
  - declared counter (the script committed with the plan, `7c81a787`): `0 of 7`, exit 1 at `43ca0bfb` → **4 of
    7**, exit 1 on the landed content at `34cfffbb` and **4 of 7** on the final content (`--root` on the lane at
    `588f5824`; Copilot SDK and Gemini CLI fail on the effect value `removed in a scope`, opencode on a quote
    with inner double quotes). **Not verified as declared.** The L1 added three terms to the counter's reviewed
    list in `34cfffbb`, after the plan commit, and the plan said "no target value moved" (`ReviewCommitOrder.md`;
    lesson M35; criterion Q28 reads the verdict on the declared counter).
  - falsify-hardened counter at `588f5824` (self-test 51, floored at 51; per-lever labels pinned; Gate read from
    `### Admitted`; page-pinned rows; two of the three added terms removed again): `0 of 7`, exit 1 at
    `43ca0bfb` → `7 of 7`, exit 0; `--fetch` `quotes found on live pages 7 of 7`, exit 0 at 2026-10-22T15:33:31Z.
    Reported beside the declared count, not in its place.
- **No harm** — `NoHarmGates.md` at `59903b26`: all 11 base-green gates green; surfaces and pins red → green;
  corpus integrity 4 DRIFT → 1 (`report_dead 2`, closure-owned round-48 spot-check); `verify_harness_claims.py`
  21/28 and `fault_injection_corpus.sh` red at both ends, unchanged. Re-run by the L1 at `c363de7d`:
  `verify_skill_checklist.py --json` 11 of 11, exit 0; `check_assertion_floors.py` 12 PASS, exit 0;
  `verify_corpus_integrity.py` 8 of 9; census guard 20 of 20 and 9 of 9.

## Sources & frontier

- Census (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`): round start 14:08:58Z
  exit 0 (W04 S018, S019, S021; `kotoba ok`); round end 15:33:31Z exit 0, the same three W04 and `kotoba ok`.
- Rows 29 → 31 (`grep -c '^| S0' corpus/SOURCES.md`). Added by tier: A 2 (S030 GitHub Copilot SDK skills page;
  S031 GitHub Copilot CLI command reference), both `docs`, `mined`, opened 2026-10-22. Touched old → new
  (used-by only, contract rule 2): S021, S022, S024, S025, S029 gain `corpus/knowledge/skill-overlap-levers-round51.md`.
  Search log: one round-51 note. Gate record with URLs, access times and quotes: `corpus/lessons/round-51.md` § Gate.
- Frontier rows advanced: Sibling arbitration (overlap levers by client moved to Core, `PROVINCE.md` § Core and
  § Frontier); Loader-rule freshness (omp 18.12.6 re-derived and re-pinned; still not held: the callee allowlist,
  six renames since round 18, `OmpRenameHistory.md`).
- Carried: S024 and S031 `teaches` cells narrower or wider than their pages (superseding rows next round).

## Trend verdicts

- **expansion: improved.** One new admitted entry (37 → 38 knowledge files) on uncovered ground: four of seven
  counted levers are new to the corpus (`CriticLearningLanded.md`); two new tier-A rows.
- **quality: improved.** omp 18.12.6 freshness debt (open since round 48) closed: surfaces 5 → 7 of 7, pins 3/3;
  five rows re-opened byte-identical; falsify findings landed as corrections; the new rule's false-green path was
  fixed before the report.
- **discernment: unchanged.** Three mistakes mined with two new criteria, but the round repeated a sizing error
  of its own (M35: the C2 reviewed list widened after the plan) and the falsify wave, not the L1, caught it;
  several Gate reasons were wrong (`ReviewLessonGate.md`).

## SHONEN

- [~] SKILL.md decision tables, error patterns, checklists, cited sources — new § Anti-patterns "Overlap levers
  by client" table citing `corpus/knowledge/skill-overlap-levers-round51.md`; `verify_skill_checklist.py --json`
  11 of 11, exit 0 at `c363de7d`.
- [~] End-to-end domain task executed and logged — LOG.md § Round 51 landing (surfaces gate and lever counter
  run at base and head).
- [~] Instructions executable without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md` (no
  fresh non-author cold run this round).
- [~] No cross-domain bleed — `PROVINCE.md` § Adjacent unchanged in classification; D5 corrections and the D6
  provisional note; `SiblingOverlapScan.md` found no sibling owning the overlap-lever ground.

## Round shape and seats

- Shape: default two v1 waves, each validated under `scripts/hyaku/ufo-wave-policy.json` and sent as one `task`
  call carrying the validator's `taskCall`, with one `solutionSpace` string added per task and nothing else
  changed (payloads `.ufo/waves/round-51/*-taskcall-sent.json`). Seat gate: build granted 14:18:45Z (33 seats),
  falsify granted 15:14:05Z (34 seats); both released after every seat returned. The L1 held the planner seat.
- Wave 1 build: **33 seats** — scribe 14, scout 6, executor 4, critic 4, reviewer 3, connector 1, mutation-tester 1.
  33 returned, 0 dead. Follow-ups went to the same identities (`LeverGuard` ×2, `SurfacesRepin` ×2); no new seats.
- Wave 2 falsify: **34 seats** — reviewer 25, critic 6, mutation-tester 2, scout 1. `MutSurfacesHead` and
  `MutLeverGuard` first ended on "[inception/mercury-3] 429 Rate limit reached: input token limit exceeded";
  each identity was resumed once and completed. 34 returned; no seat stayed dead.
- **Round total 67 seats**, no residual call. Attack roles 8 + 33 = 41 of 67 (61%).
- Seats addressed Main twice (`SrcOpencode`); the falsify context named `agent://KotobaR51` as the only target.

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs/updates: none by the L1 or any seat that reported.
- L0: no new line. Open: kotoba round-50 line 105 (precedence rule; this round neither extends nor relies on
  it); round-49 lines 100–101.
- Leftover and misroot sweep after the last seat write (Q27): newest wave file 15:29:25Z; sweep 15:33:54Z;
  `git --no-optional-locks -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked file and
  no kotoba or round-51 path except the driver's own `.ufo/state/kotoba.report-baseline` (untouched); lane
  `git status --porcelain` empty. No misroot this round.
- Carried to round 52: callee-name-independent omp rule; S024/S031 superseding rows; fixture labels; D2 F1–F5
  and the substring advertisement test; D7 items; R1, R5.
- Driver completion is not admission; the non-author closure judges both claims.
