# souji — round 17 report (hyaku phase 2, attempt 1)

Lane repo `souji-shokunin`, branch `master`. Base `5fa6017` (round-16 closure). Lane tip at report time: `2cfc6c0b2388367a5ab99d532bc02a2ebddb5984` (`jj-lane.sh state`: ahead=0 behind=0). Every hash below is a `landed <hash>` line from `scripts/hyaku/jj-lane.sh`.

## Work performed

Declared claims:
- **C1 operability**: closure D1 and D2 in `tools/souji-census.sh`.
- **C2 calibration**: the lowest non-retired axis (7). Seat-audit precision plus reproducible evidence (D4).
- **C3 coverage**: jj-colocated repositories become a governed edge class. This answers the routed jj-migration evidence in JjAuditSouji and JjTrialSouji.

Work items:
- **C1, D1.** Every dirty-count `git status` now passes `--untracked-files=normal`. A repo-local, included or `config.worktree` `status.showUntrackedFiles` can no longer produce a false clean. Evidence: `tools/souji-census.sh` count_dirty; fixture cases R17-01..06.
- **C1, D2.** A hardlinked or non-regular `info/attributes` (repo gitdir, common dir or admin dir) now produces a per-repo `error` row with stderr `git-metadata-unsupported`. There is no early return, and every other metadata guard keeps whole-run exit 2.
  - When a repo also carries a config soft finding, both diagnostics print (L1 fix to `emit_soft_diag`).
  - Wave-2 fixes: `LC_ALL=C stat`, `regular empty file` is accepted, and dot-named admin dirs are guarded.
  - Evidence: fixture R17-07..29; `census/round-17/c1-matrix-4f48343.json`.
- **C2.** Changes to `tools/souji-seat-audit.py`:
  - exact-prefix paths (`removeprefix`, S061);
  - `V-WRITE-RELATIVE`: relative targets resolve at the fleet root, so the suffix match is gone;
  - status-aware `V-WRITE-UNPARSED`;
  - every `[path#TAG]` header is audited;
  - normpath and seat-scoped scratch;
  - `V-PROBE`;
  - the selftest is severity-exact (66 cases).
- **C2 evidence.** The r16 transcripts are committed at `census/round-16/transcripts` (144 files, `MANIFEST.sha256`, checker `census/round-17/transcript-manifest.py`). The replay record binds the auditor, specs, manifest, tool sha and Python version (`census/round-17/seat-audit-replay.py`). Records: `census/round-17/seat-audit-r16-replay-{base5fa6017,4f48343}.json`.
- **C3 receipt tools.** In `souji-verify.sh`, `souji-vault-verify.sh` and `souji-quarantine.sh`, the live roots site uses `for-each-ref --exclude='refs/jj/'`, so `refs/stash` and other refs stay roots.
  - `jj_keep_novel` (identical body sha `7fc7cc63…` in all three tools): a keep-only commit refuses only when it brings novel leaf-blob content at the target. It is SIGPIPE-safe and fails closed.
  - Dead shadowed sites are untouched (quarantine `try_pushed` is byte-identical to 5fa6017).
  - For jj repos, quarantine prints the helper runbook naming both paths.
  - Fixture: `tests/fixtures/r17-jj-receipts.sh` (git-emulated J1–J8 and J10–J12; real-jj J9).
- **C3 docs and knowledge.**
  - `corpus/knowledge/jj-colocation-receipts.md` is grounded on jj source at the host's tag v0.45.1 (S054) and on S051–S063.
  - SKILL.md: the git-add recipe is replaced by a three-way commit rule (souji lane: helper; jj repo: owning helper naming both paths, then a post-check; plain repo: guarded git). It gains jj error-pattern bullets and 6 new and 4 updated registry rows.
  - PROVINCE.md gains a work-surface bullet and a boundary section. `corpus/README.md` gains an F1-jj row.
- **Phantom-deletion hazard.** At round start `jj status` showed `D` for the two tracked `p6repo` files.
  - The empty stub `tests/vault/vadv54-run/p/p6repo/.git` was moved, not deleted (same inode 30073199, empty), to `souji-shokunin/.ufo/quarantine/round-17/tests/vault/vadv54-run/p/p6repo/dot-git-empty-stub`. That is lane-local and uncommitted, because git cannot track an empty dir. Receipt: `stat` = `directory|1|0|30073199`.
  - The harness now creates the stub only during case P6.
  - A helper call naming both files re-tracked them; `@` no longer lists them. Evidence: lesson R17-M3.
- **Routed fixes.**
  - D3: two append-only LOG corrections (28→29; pre-harm also fails 03/18).
  - D5 and D7: lesson Corrections.
  - D6: gate selftest 18→33 with exact id sets and exit-2 totality. Replays are committed (`census/round-17/gate-replays.py`, `gate-replays-expected.json`, `gate-replays-4f48343.json`). `regenerate.py` now computes the verdict, and the r15 frozen record was regenerated at `4f48343` (`--frozen` rc 0).
  - Mined mistakes R17-M1..M6 and new criteria QUALITY Q27/Q28.
- **Swarm.**
  - Planner seat: held by L1 (the validator rejects `planner`); planning data-walks rode connector items.
  - Wave 1: 78 seats (23 scout, 13 executor, 13 reviewer, 8 connector, 7 scribe, 5 critic, 4 revenger, 3 sentinel, 2 simplifier), 0 dead.
  - Wave 2: 71 seats (38 reviewer, 16 scout, 5 critic, 4 mutation-tester, 3 scribe, 2 sentinel, 2 connector, 1 executor). The first dispatch was refused by the job cap (100); the second try spawned.
  - Dead seats: **28** (27 reviewer, 1 connector), all on m_zfl 429 "Rate limit reached (type=1302)" with the retry budget exhausted. They were not respawned. L1 ran their executable checks (Process section of the lesson).
  - Round total: 149 seats.
  - Wave-2 findings went back to five idle wave-1 executors as fixes, landed in `4f48343`.
- **Misroot sweep.** `git -C <fleet> status --porcelain` shows only `.ufo/state/*.report-baseline` driver files, none written by souji seats. No misroots; nothing was moved.
- **Inherited state.** The operator-owned untracked `census/operator-sweep-20261019/` was never opened. Its metadata fingerprint `f6a84466…` (155 entries) is unchanged. `round-16-verifier-spotcheck.md` is not edited. Every D1–D7 item is turned into a fix or criterion (see above and the lesson).

## Landed changes

| commit (landed) | content | LOG |
|---|---|---|
| `ddb73474433977ff54b015ac3e77669ff2537353` | C1/C2/C3 code, fixtures, evidence runners, r16 transcript bundle, gate D6, vadv54 harness, regenerate.py | LOG round-17 entry |
| `d7e648d5a1931e6dbacfd5be0587547afee15de3` | r15 frozen record regenerated at ddb7347 | same |
| `4f4834390ad4845b76804e94cc04d8f867ef9b54` | wave-2 fixes (census empty/locale/dot-admin + both diagnostics; jj_keep_novel leaf-blob/SIGPIPE/fail-closed; gate totality and mutant killers; seat-audit survivors; fixtures R17-27..29, J10..J12); `c1-matrix.json` (ddb7347 run) | same |
| `95519a70bac653badf71c646128c6ed6d76d119f` | wave specs, dispatch records, registries and 122 seat reports; landed-rev evidence (matrix, gate replays, jj fixture both arms, live fleet, seat-audit replays); frozen record regenerated at 4f48343 | same |
| `d98065ded46b27cb8f135255dfda72b1936e0743` | lesson `round-17.md`, knowledge entry, SOURCES S051–S063, QUALITY Q27/Q28, SKILL/PROVINCE/README, SCORECARD, LOG (D3 corrections and round entry) | LOG D3 entries and round-17 entry |
| `2cfc6c0b2388367a5ab99d532bc02a2ebddb5984` | `census/round-17/gate-landing.json`: gate at `d98065d`, findings 0 | same |
| fleet `23efcab` | `.ufo/l0-questions.md`: two souji round-17 lines | — |

## Before → after measurements

- **C1 (operability)**
  - Command: `python3 census/round-17/run-matrix.py --changed <rev> --output <f>`, measured at `4f48343`. Record: `census/round-17/c1-matrix-4f48343.json`; `invalid_suites` empty; reproduced with 0 diffs by seat RerunMatrixLanded at ddb7347.
  - Results by arm:

    | arm | rev | hygiene (failed/29) | r15-config | namespace | selftest |
    |---|---|---|---|---|---|
    | r16 (before) | `5fa6017` | 14 (13 repair cases + R17-29) | 0 | 0 | 38/0 |
    | changed (after) | `4f48343` | 0 | 0 | 0 | 49/0 |
    | pre-harm | `a31642d` | 21 | 8 | 10 | — |
    | r14-harm | `cc21683` | 14 | 16 | 0 | — |

  - `bash -n` and shellcheck are clean on every arm.
  - Live fleet pair (`census/round-17/live-fleet.json`): 22 rows identical excluding mtime, rc 0.
- **C2 (calibration)**
  - Command: `python3 census/round-17/seat-audit-replay.py --lane <lane> --transcripts census/round-16/transcripts --specs .ufo/waves/round-16/w1-spec.json:.ufo/waves/round-16/w2-spec.json --auditor <A> --output <f>`, measured at `4f48343`. The auditor was taken at `5fa6017` for the "before" record.
  - Majors w1: 1 → 1 (SrcGitNoLazyFetch:144, a true violation, kept).
  - Majors w2: 3 → 1. ConnReadmeIndex:180 is now `V-WRITE-RELATIVE`, a true fleet-root attempt; the two RerunGateReplayR14 rows are now `V-WRITE-UNPARSED` minors.
  - Minors w1: 19 → 24. Minors w2: 42 → 48. The rise comes from new classes.
  - `--selftest`: 20 severity-blind → 66/66 severity-exact.
  - Held-out table: 5fa6017 scores 30/48, ddb7347 scores 48/48 (`w2/HeldOutBaseAuditor.md`).
  - Precision on fresh transcripts is unmeasured.
- **C3 (coverage)**
  - Command: `bash tests/fixtures/r17-jj-receipts.sh --tool-dir <tools> [--baseline-dir <base>]`. Before (5fa6017 tools): 33 cases, 13 FAIL, 2 SKIP. After (`4f48343`): 35/0/0, with J6 plain-repo byte identity. Records: `census/round-17/jj-receipts-{base5fa6017,4f48343}.txt`.
  - Selftests at `4f48343`: verify 40→49, vault 51→57, quarantine 91→101 (0 failed).
  - Command: `python3 census/round-14/count-claims.py <rev>`, measured at `5fa6017` → `d98065d`. admitted_knowledge 5→6 (author inventory; the closure decides), held 1, source_rows 50→63.

## Sources & frontier

- **SOURCES rows.** 50 → 63, counted with `python3 census/round-14/count-claims.py <rev>` at `5fa6017` → `d98065d`.
  - Added: 13, all tier A: S051–S063. Of these, 12 are docs and 1 is code (S054, jj source at tag v0.45.1).
  - Status: all 13 are mined. Totals go from mined 31 / queued 15 / rejected 4 to mined 44 / queued 15 / rejected 4.
  - Existing rows touched: none.
  - Every new row was opened by a wave-1 seat and re-opened by a wave-2 seat (`ReopenS051`–`S063`). ConnLessonGateSection confirmed all 13 quotes verbatim.
- **Census at round start:** exit 0. W04 for S035, S036, S038 and S049; `souji ok`.
- **Census at round end:** exit 0. W04 for S035, S036, S038, S049, S057, S058, S059 and S063 (declared shared-URL scopes); `souji ok`.
- **Mined mistakes.** R17-M1..M6 are in `corpus/lessons/round-17.md` `## Mistakes`.
- **Sourced claims.**
  - C1 rests on S057, S058, S059 and S062.
  - C2 rests on S061.
  - C3 rests on S051, S054, S056 and S060.
- **Frontier.** F1-jj, the bounded receipt-root rule, is marked Core as a candidate (`corpus/README.md`, `PROVINCE.md`). F1 as a whole stays frontier: keep-ref lifetime is unmeasured.

## Trend verdicts

- **expansion: improved** (author). One knowledge entry is added and grounded (S051–S056, S060, S063). The PROVINCE surface and README row for jj-colocated repos are new ground. Three capabilities run with committed evidence: census hygiene, jj-aware receipts, reproducible seat audit. Admission is pending the closure.
- **quality: improved** (author). Two r16 overstatements are corrected append-only (D3). The r16 seat-audit disposition is corrected (R17-M1). The census regression found by wave 2 was fixed before final landing (R17-M5). The r16 replay verdicts are committed runs, not prose (D6). No admitted entry failed a re-check.
- **discernment: improved** (author). Every closure D-item became a fix or criterion: Q27 cites R17-M1, Q28 cites R17-M3. The wave-1 critics changed two claims before landing, rejecting unfiltered keep-glob refusal and heads/tags/remotes-only roots. Wave 2 found the census regression and it was fixed. The non-author closure decides admission.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists and cited sources. Evidence: SKILL.md jj error patterns and the three-way commit rule (`d98065d`); `corpus/SOURCES.md` S051–S063.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: round-17 LOG entry; the stub move with its inode receipt and the re-tracking of the phantom-deleted files.
- [~] Instructions executable by an agent without oral context. Evidence: registry rows for r17-census-hygiene, r17-jj-receipts, r17-gate-replays and r17-transcript-manifest in SKILL.md.
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: PROVINCE boundary section ("souji's tools never invoke `jj`; commits stay helper-owned").

## Extras

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Cross-domain line:** these jj hazards belong to the fleet helper `scripts/hyaku/jj-lane.sh` (orchestrator-owned) and are reported, not changed:
  - its phantom-deletion refusal runs after `jj commit`, which leaves keep-held commits;
  - nothing in the helper runs `jj util gc`.

  The evidence is `.ufo/waves/round-17/w1/ConnSiblingJj.md`, `CriticC3Coverage.md` §3.4, and lesson R17-M3. Souji owns only receipt semantics and lane hygiene.
- **jj routed items:**
  - Phantom-deletion hazard: fixed (stub moved, harness scoped, files re-tracked).
  - `--branches --not --remotes` and `--not --all` blind spots: fixed in the live receipt sites. The dead `--not --all` sites are shadowed and not executed.
  - Quarantine `git mv` and `git rm --cached` vs the helper: documented in the SKILL rule and the quarantine runbook output. Action mode is unchanged for plain repos.
  - SKILL `git add` recipe: replaced.
  - Census `unpushed` column: left branch-based and disclosed.
- **Open L0 questions:**
  - `souji | round-16` (scope of residual contractions), still open;
  - `souji | round-17` jj keep-ref gc policy (new);
  - `souji | round-17` operator-sweep disposition (new).
- **Tool installs:** none by L1. Seats reported none.
- **Driver:** `watchdog.log` launch line 493 shows no `lane-dead-no-report souji round=17`, so this is attempt 1 with nothing inherited. The session was interrupted once by an Anthropic 429 and resumed under the same identity.
