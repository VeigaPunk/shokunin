# souji — round 16 report (attempt 1)

Lane HEAD (pushed, `git -C souji-shokunin rev-list --count @{u}..HEAD` → 0): `c46eabf80f4c5b34a6774cd8725a0787306ba754`. Baseline `58ace9f` (r15 closure on top of `b410186`). Round lesson: `souji-shokunin/corpus/lessons/round-16.md`.

## Work performed

Declared claims (repair-first round; r14 and r15 were rejected-harmed):
1. **C1 operability** — restore a parsing `tools/souji-census.sh` (r15's `b410186` did not parse) and replace r14's value-blind config refusals with value/effect-aware handling, keeping r14's namespace refusals. Author verdict: **improved, not no-harm** (outside admission pending).
2. **C2 calibration** (lowest non-retired axis, 7) — `tools/souji-landing-gate.py`, a landing-claim gate for the three r15 closure-found defect classes. Author verdict: **improved, scoped** (red on its training instance; parse/pin classes only on r13/r14; not robust to hostile content).

Work items (routed R1–R7 from `corpus/lessons/round-15-verifier-spotcheck.md`):
- R1 parse restore + correction sweep — `cbf688a`, `0a70bef`; corrections in `LOG.md` (r16 correction entry), `SKILL.md`, `SCORECARD.md` operability row, `corpus/README.md:191-203`; lesson `## Corrections (R1 sweep)`.
- R2 r14 harm repair — census value/effect-aware (`0a70bef`): only a config-named protected reach keeps whole-run exit 2 for config; unevaluable config → per-repo `error` row; bound filter → `status-unverifiable`; `GIT_CONFIG_COUNT` neutralizes hooks/fsmonitor, `GIT_NO_LAZY_FETCH` on every git call. Residual contractions vs pre-harm listed in lesson `## Residuals (open)` and the L0 question.
- R3 seat failures carried verbatim — lesson `## Seat-reported failures`: 12 wave-1, 29 wave-2, 4 round-15 lines, each `open` or `resolved@<hex>`; gate at `6ff91f5` → 0 uncarried (`census/round-16/gate-landing.json`). Non-vocabulary wave-1 defect lines (9, per `CriticHonestyAudit.md`) are not exhaustively carried — open.
- R4 r15 checker executed for the first time and repaired (`c6207bd`); frozen record regenerated from real runs (`regenerate.py`), measured at `c6207bd`, landed `7a79dc2`. Class tables are observed-baseline pins; 4 r15 predictions falsified (R16-M4).
- R5 seat probe rule audited from transcripts — `tools/souji-seat-audit.py` (`7a79dc2`, `a6ec781`); `census/round-16/seat-audit-w1.json`, `seat-audit-w2.json`. Neither complete nor precise (Q26).
- R6 cross-domain line — below.
- R7 git-status(1) rejected row — S044 `rejected`, teaches cell corrected after reopen (`4f9a4e8`).
- Wave-2 integration (`fb23b12`, `4f9a4e8`, `6ff91f5`): gate-fixture vacuity case fixed (passed on exit code alone); 9 overclaims corrected (pre-harm classification, "19 recursive", "held-out", "integrated 65 reviews", R5 "enforced", SCORECARD:46 "refuse only", carry scope, Residuals omissions, dead-seat authorship); S045 teaches narrowed; three knowledge entries verified on Git 2.55.0 marked for recheck (host now 2.56.0); QUALITY Q25/Q26 restated.
- Planner mapping: L1 holds the canonical planner seat; the bounded planning data-walk rode wave-1 item `PlanWalk` (revenger) (`.ufo/waves/round-16/w1/PlanWalk.md`).

## Landed changes

All pushed; LOG binding: `LOG.md` "round 16" entry (line 836) and the appended "round 16 wave-2 corrections" entry (line 886).

| commit | change | LOG binding |
|---|---|---|
| `cbf688a` | C1 census restored on the `cc21683` base, value/effect-aware; r15 config fixture first run + oracle fixes | LOG:836 C1 paragraph |
| `0a70bef` | wave-1 review fixes (soft degrade, GIT_CONFIG_COUNT, lazy fetch, info-file/filter guards, include bases); matrix runner; `c1-matrix.json`, `live-fleet.json` | LOG:836 C1 |
| `c6207bd` | R4 checker repair (CASE regex, token ids, r16 class tables), external fixture literals, `regenerate.py` | LOG:836 R4 |
| `7a79dc2` | landing gate, r16 gate fixture, seat audit, regenerated frozen record, `c1-matrix-final.json`, `live-fleet-final.json`, `seat-audit-w1.json`, wave-1 reports | LOG:836 C2/R4/R5 |
| `a6ec781` | gate STATUS-only channel; audit honors ALLOWED-EXEC | LOG:836 C2 |
| `163158a` | lesson, SOURCES S043–S050, Q25/Q26, LOG, SCORECARD, SKILL, README, wave-2 spec/dispatch, `c1-matrix-landing.json` | LOG:836 |
| `fb23b12` | wave-2 reports; gate-fixture vacuity fix; knowledge freshness notes | LOG:886 |
| `4f9a4e8` | honesty corrections (lesson, SCORECARD, QUALITY, SOURCES S044/S045, README, SKILL); `seat-audit-w2.json` | LOG:886 |
| `79bbe7a` | final wave-2 seat reports | LOG:886 |
| `6ff91f5` | wave-2 STATUS lines carried; dead-seat authorship; wave-2 audit in Process | LOG:886 |
| `c46eabf` | `census/round-16/gate-landing.json` (gate at `6ff91f5`) | LOG:886 |

Inherited state: no `lane-dead-no-report souji round=16` line in `.ufo/watchdog.log` (count 0); no inherited lane-authored leftovers. Untracked `census/operator-sweep-20261019/` is operator-owned, never opened, staged or deleted.

## Before → after measurements

- **C1** — `python3 census/round-16/run-matrix.py --changed <rev> --output <new.json>` (same fixtures every arm). At `0a70bef` (census sha256 `64a60fd0…`, unchanged to HEAD; `census/round-16/c1-matrix-final.json`): before — r15 baseline `b410186` `bash -n` rc 2 at line 1368, every case fails; r14-harm `cc21683` fails 16/20 r15-config cases (15 HARM_CASES + 19); pre-harm `a31642d` fails 02, 03, 08, 11, 14, 17, 18, 19. After — changed arm r15-config 20/20, r14 namespace 12/12, `--selftest` 38/38, `bash -n` rc 0, `shellcheck -S warning` 0 findings. Landing rerun with HEAD fixture bytes `27474396…` identical (`c1-matrix-landing.json`). Live fleet paired runs, 21 repos, rows identical r14-harm vs changed (`live-fleet-final.json`; preservation only — no live repo used an r14-refused key).
- **C2** — `python3 tools/souji-landing-gate.py --root souji-shokunin --rev <rev> --round <N>`. Before: no lane mechanism detected the three classes (r15 closure found them by hand). After: `--rev b410186 --round 15` → exit 1, 5 findings (LG-PARSE-REG census, LG-FROZEN-PIN, 2× LG-FROZEN-MEASURED, LG-SEAT-UNCARRIED `ConfigRepair.md` line 7); `a31642d`/13 and `cc21683`/14 → 0 (parse and pin classes only). `--selftest` 18/18; `python3 tests/fixtures/r16-landing-gate.py` 15/15 (re-run at `fb23b12` after the vacuity fix). Round-end binding: `--rev 6ff91f5 --round 16` → findings=0, checked_reg=21, checked_pins=16, checked_markers=30, checked_reports=141 (`census/round-16/gate-landing.json`); before carry, `79bbe7a` → 29 LG-SEAT-UNCARRIED.
- **R4** — `python3 tools/souji-preservation-evidence.py --selftest`: 24/47 (r15 landing bytes) → 47/47; external fixture 8/8; `--frozen` clean (measured `c6207bd`).
- **R5** — `python3 tools/souji-seat-audit.py --spec … --transcripts … --lane …`: wave 1 65 seats, 3173 calls, 1 major (failed edit), 18 V-RECURSIVE + 1 V-WRITE-UNKNOWN; wave 2 79 seats, 4348 calls, 3 major V-WRITE-SCOPE (all failed edit calls, no bytes written), 42 V-RECURSIVE (unconfirmed). `--selftest` 20/20.

## Sources & frontier

- Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`. Start (SOURCES sha256 `5185720f…`): exit 0, W04 S035/S036/S038, `souji ok`. End (at `c46eabf`, SOURCES sha256 `b0683473…`): exit 0, W04 S035/S036/S038/S049, `souji ok`.
- Rows 42 → 50 (row-regex count over `corpus/SOURCES.md`); tiers A/B/C 38/3/1 → 46/3/1. Added (all tier A): mined S043 (bash `-n`), S045 (gitattributes), S046 (git-check-attr), S047 (gitignore), S049 (git GIT_NO_LAZY_FETCH), S050 (Python compile()); rejected S044 (git-status, on-release), S048 (ShellCheck SC1046, 365d).
- Touched old → new: S042 used-by `round-15.md` → `round-15.md, round-16.md`; S044 teaches widened / S045 teaches narrowed after wave-2 reopens (`4f9a4e8`).
- Frontier rows advanced: none. Admitted knowledge stays 5, K5 HELD, certification OFF.

## Trend verdicts

- **expansion: unprovable-but-better** — two new runnable capabilities (landing gate, seat transcript audit; `SCORECARD.md` Capabilities) and six mined source rows, but no knowledge entry or frontier row advanced and both tools carry open wave-2 defects (mutation survivors, hostile-input gaps).
- **quality: improved** — the r15 non-parsing census and the unattested frozen pin are repaired with measured runs (C1 matrix; `--frozen` clean); three knowledge entries verified on Git 2.55.0 now carry a freshness note instead of staying silently stale; S044/S045 cells corrected against their pages.
- **discernment: improved** — every r15 closure disagreement/routed defect became a fix or criterion (R16-M1..M6, Q25, Q26); wave-2 falsification found 9 overclaims in the committed wording, which were corrected and carried with dispositions rather than defended. No non-author record of this round exists yet; the closure decides admission.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` registry rows 152-154, "Repeatable fleet census" bullet; QUALITY Q25/Q26; S043–S050.
- [~] At least one end-to-end domain task executed and logged in LOG.md — live fleet paired census (`census/round-16/live-fleet-final.json`, LOG:836).
- [~] Instructions executable by an agent without oral context — `SKILL.md` registry entry commands + self-tests; `corpus/lessons/round-16.md` Gate commands.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md unchanged; gate checks only souji's own pins (R6 line).

## Extras

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Cross-domain evidence line (R6):** frozen-pin and round-landing validation are split-owned — pin classification and its refusals are tameshi's, the fleet `round-gate` is kumitate's lane-scoped instrument, and `souji-landing-gate.py` checks only souji's own pins and claims neither mutation-leg status nor fleet conformance — evidence `tameshi-shokunin/PROVINCE.md:49-57` (tameshi HEAD `017a2b0` at wave-2 read), `souji-shokunin/.ufo/waves/round-16/w1/SiblingOverlap.md:39`, re-checked `.ufo/waves/round-16/w2/ConnSiblingOverlap2.md` (holds F5/F7; sibling-internal leg-count inconsistency F1 is tameshi's).
- **Seat-reported failures (R3):** verbatim in `corpus/lessons/round-16.md` `## Seat-reported failures` (45 lines with dispositions); open items routed to r17 in `## Residuals (open)`.
- **Tool installs:** none. L1 ran no install; no bash call in the 144 exported seat transcripts (`/var/tmp/souji-r16/transcripts/w1`, `w2`) matches `pacman -S`, `uv tool install`, `npm -g`, `cargo install` or `pip install` (matches occur only in the dispatched context text). pacman paused host-wide.
- **Waves:** wave 1 = 65 seats (scout 17, reviewer 14, connector 9, critic 6, scribe 6, revenger 5, executor 3, sentinel 2, mutation-tester 2, simplifier 1); dead: SentinelStoreAccess (provider policy refusal), PreservationRepin (m_swe rate limit), LandingGate (m_swe rate limit after producing the gate file). Wave 2 = 79 seats (reviewer 28, scout 20, connector 8, critic 7, scribe 6, mutation-tester 4, revenger 3, sentinel 2, simplifier 1), dispatched on the 4th try after 3 refusals "Background job limit reached (100)"; dead: SentinelCensusFinal (provider policy refusal). Round total 144 seats. Wave 2 had no executor seats (falsify wave of reviews/reruns), below the suggested executor share — disclosed.
- **Open L0 questions:** `souji | round-16 | Operator scope call on the census contractions…` (appended to `.ufo/l0-questions.md`): accept or narrow the whole-run metadata/`info/attributes` refusals, ignored global/system config, bound-filter skip, `~user`/`%(prefix)` degrade, `--ignore-submodules=all`.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` → `M .ufo/watchdog.log`, `?? .ufo/state/*.report-baseline` (driver files), `?? scripts/hyaku/jj-lane*.sh.new` (orchestrator) — none written by souji seats; nothing moved. Fleet `.ufo/waves/round-16/` is tracked protocol-shokunin content (commit `7c5b34f`), not ours; the one relative-path seat write attempt (ConnReadmeIndex) failed and wrote nothing.
