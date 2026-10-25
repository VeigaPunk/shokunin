# Souji — round 18

## Work performed

Declared claims: **C1 operability** — bound the routed FIFO/special-reader stalls in repository-content reads and clean up fixture-owned in-session children; **C2 calibration** (lowest axis, 7) — detect authority-file evidence pointers absent at the measured revision; **C3 coverage / capability acquisition** — observe own-uid process residue, list-only. Author verdicts: **improved within the measured boundaries** for all three; outside admission remains the non-author closure's decision. Scores stay coverage 8 / calibration 7 / operability 8 (numeric delta 0, legacy-unmapped).

- Census preflight and measurement now have process-group watchdogs, interruption-safe cleanup, timeout/error rows for gitfile candidates, raw-control-character input refusal, system-attributes suppression and adaptive success polling. A blocked repository no longer loses the healthy neighbours' measurements. Evidence: lane `4800fd79488e5f2c11a18117958f104171d85dc8`; `census/round-18/c1-matrix-4800fd7.json`; lesson R18-M4/M8.
- FIFO census fixtures use session-wide cleanup rather than killing only their leader's group. Activated different-PGID/same-SID mutants distinguish the implementations: mutant residue 2 vs original/restored 0 in both r15 and r17 helpers. The r14 harness-only change was **reverted** because its unchanged-control digest is pinned; its landed original fixture still passes 12/12. Evidence: `w2/MutFixtureSessionKill.md`, `w2/RevR14Revert.md`, final matrix.
- Landing gate gained scoped `LG-DANGLING-PTR`, exact synthetic measured-commit exemptions, stale-exemption checks, lane/fleet collision controls, quarantine-pointer coverage, all-same-round LOG scanning and CLI early-error totality. Seven real bad-name citations were re-pointed, not deleted; four deliberate/synthetic exceptions are committed with reasons. Evidence: `tools/souji-landing-gate.py`; `corpus/pointer-exemptions.tsv`; before/after JSON records below.
- Added read-only `tools/souji-proc-census.sh`, independent `census/round-18/leak-count.py` and a 19-case external fixture. Literal live names ending in ` (deleted)`, missing credential-shaped redactions, PID identity and an ancestor-exclusion mismatch were found and repaired. No inherited process was reaped. Evidence: `proc-agreement-final.json` (failed observation retained), `proc-agreement-counterfix.json` (two 66=66 pid-identical pairs), lesson R18-M9/M10.
- Closed routed **R1–R4**: recipe owner from repository-local `lane.id` (basename/unknown fallbacks); committed r17 record names fixed in SKILL/README/knowledge with append-only LOG corrections; 21 repositories, not 22; Q29 **supersedes** Q7 for colocated commits without rewriting the old criterion. Evidence: quarantine 108/0, jj fixture 37/0/0, `LOG.md:953–963`, QUALITY Q29.
- Curated S064–S071 and then append-only corrections S072–S078 when source reopens caught over-attribution. No new knowledge entry is claimed; F5 remains frontier. Evidence: SOURCES, lesson Gate, `source-counts.json`, `source-census-final.json`.
- Retained complete wave evidence, 170 digest-checked rendered transcripts, raw nonzero audits and per-call adjudications. L1 reran installed acceptance independently of seat votes. Evidence: `census/round-18/transcripts/MANIFEST.sha256`, `seat-audit-adjudication.json`, `final-verification-4800fd7.json`.

**Boundary honesty.** The initial shorthand “no single repository can hang the fleet census, and no lane fixture leaves a blocked process behind” was overbroad. The measured repair bounds repository-content operations **after enumeration**, for descendants remaining in the assigned group. Unresponsive filesystem/NSS operations during discovery, escaping descendants and unkillable D-state processes are not contained; survivors are reported where observable. Guard and measurement have separate deadlines, not a fleet-wide budget. These limits and the frozen r14 runner are explicit in Q34 and the lesson. No no-harm claim against pre-harm `a31642d` is made; inherited contractions remain open. Deletion certification stays OFF; K5 HELD.

## Landed changes

All lane hashes below came from the helper's successful `landed <hash>` output and were pushed. Lane final tip: **`8be65236a4b61fffe9c0d05d30043650848c0a60`**; helper state reports local=remote, ahead=0, behind=0. The only untracked lane path is the inherited, operator-owned `census/operator-sweep-20261019/`, left unopened and unchanged by this work.

| Landed commit | Change | LOG / lesson tie |
|---|---|---|
| `3f822e85c6a5f866c4003be0ad039d5583d14364` | Initial C1/C2/C3 build, R1 and citation repairs, wave-1 evidence | LOG:951; lesson initial measurements |
| `42d9ff3930933cada8ba7e028d97b69a6889fc15` | Initial lesson, scorecard, Q29–Q32, sources and domain docs | LOG:951 |
| `2fc5f33d0b000c0e10450a5139137bf4300fe54b` | r14 fixture restored to pinned control bytes; gate/carry repairs | LOG:955; lesson r14-revert disclosure |
| `5efb519f00075d958c3d1109ef6fcb24c487eb87` | First real frozen-record regeneration | LOG:955; historical preservation measurements |
| `4800fd79488e5f2c11a18117958f104171d85dc8` | Falsification-driven code/fixture fixes | LOG:961; R18-M8/M9; final acceptance batch |
| `2d4c7f84b969ee0485d657b86f7860af01bbf3cf` | Final matrix/frozen records, transcripts/audits, counter ancestor-exclusion repair | LOG:961–963; R18-M10 |
| `74f9adb489fcf1393bbd479425acf5545ded9908` | Scoped final claims, source corrections, Q33–Q35, complete dispositions | LOG:961–963; lesson Gate / Process |
| `8be65236a4b61fffe9c0d05d30043650848c0a60` | Committed zero-finding authority-tree receipt and final census/misroot receipts | LOG:961–963; final Gate paragraph |

L0 questions landed separately in fleet **`52b38630d3f86add311b184bef692b59758b6e77`**. This report lands last through the fleet helper.

## Before → after measurements

All paths in this section are relative to `souji-shokunin/` unless stated otherwise. Commands require a **new** output path; producers refuse overwrites.

### C1 — operability: improved, bounded

```sh
python3 census/round-18/run-matrix.py --changed 4800fd79488e5f2c11a18117958f104171d85dc8 --output <new.json>
```

Measured record: `census/round-18/c1-matrix-4800fd7.json`, runner exit 0, `invalid_suites=[]`.

| Suite | b576341 baseline | Final 4800fd7 |
|---|---:|---:|
| r18 bounded | 12 cases, **9 failed** | 12 cases, **0 failed** |
| r17 hygiene | 29/0 failed | 29/0 failed |
| r15 config | 20/0 failed | 20/0 failed |
| r14 namespace, pinned original fixture | 12/0 failed | 12/0 failed |
| census selftest | 49/0 failed | 69/0 failed |
| bash syntax / ShellCheck warning level | exit 0 / 0 | exit 0 / 0 |

Baseline failures are B1–B4, B8–B12; B5–B7 are preserved controls. Final B10 exercises parent TERM/KILL cleanup, B11 raw-newline refusal, B12 gitfile-preflight timeout rows. Every final matrix suite records **0 new residue processes**; inherited prefix matches are separated from new `(pid,starttime)` observations.

The matrix also retains pre-harm/r14-harm arms: r18-bounded failures 10/9, respectively; their old config/namespace contractions remain visible. The final r14 oracle digest is the original pinned `e6a984b1…14b2`, unlike the disclosed temporary dirty-fixture run in the initial working-tree record.

Live observations are not frozen-workload benchmarks: pair 1 matches excluding mtime on **21 repositories**; pair 2 has mado dirty 10→13 during concurrent writes (`live-fleet-pairs/`). Watchdog overhead remains measurable: the initial 200-repo median was 42.264 s vs 22.464 s baseline; adaptive polling reduced the final single-sample 200-repo run to 30.188 s (`w2/ProbeScale.md`, `w1/CensusWatchdogFix.md`). No performance-equivalence claim is made.

### C2 — calibration: improved within the declared grammar

```sh
python3 tools/souji-landing-gate.py --root <lane> --rev b576341 --round 18 --fleet-root /home/vgpnk/Projects/shokunin --json <new-before.json>
python3 tools/souji-landing-gate.py --root <lane> --rev 74f9adb489fcf1393bbd479425acf5545ded9908 --base b576341 --round 18 --fleet-root /home/vgpnk/Projects/shokunin --json <new-after.json>
```

- Before: **11 findings**, 320 pointer tokens, 3 fleet classifications, 0 exemptions. Exit **2**, because b576341 has no round-18 wave reports; independent pointer findings are still retained. Record: `gate-pointers-before-finalgrammar-b576341.json`.
- After: **0 findings**, exit **0**, registry scripts 33, changed scripts 13, pins 13, measured checks 3, failure markers 10, reports 175. Record: `gate-pointers-after-final.json` (resolved revision 74f9adb).
- Rechecked at the final pushed tip `8be6523` with the same `--base/--round/--fleet-root`: **exit 0**, identical summary counts.
- The delta is **7 real citation repairs plus 4 exact reasoned exceptions**, not 11 fabricated calibration errors. Old-grammar 10→0 is retained as historical evidence.
- Selftest **33→61**, pointer fixture **11/0**, r16 fixture **15/0**, five historical replay exit/finding-multiset matches. Exact runs: `final-verification-4800fd7.json`, `gate-replays-final-4800fd7.json`. Replay JSON byte identity is not claimed.

### C3 — coverage/capability: improved, list-only frontier

```sh
bash tests/fixtures/r18-proc-census.sh --tool tools/souji-proc-census.sh
bash tools/souji-proc-census.sh
python3 census/round-18/leak-count.py
```

Before b576341 had no proc-census tool and no process-residue surface. After: **3 observed classes**, fixture **19/0** at 4800fd7, plus expanded selftests. The header-only-stub check is a vacuity control, **not** a replay of the nonexistent baseline tool.

Final counter fix is at `2d4c7f8`. Two consecutive observations are **66=66**, with equal PID sets and no stable differences (`proc-agreement-counterfix.json`); the independent counter selftest passed 66→67 with exactly its seeded process added (`counter-exclusion-repair.json`). The failed stable-PID-1659 observation is preserved in `proc-agreement-final.json`. Live counts change with process churn; an earlier dated 65=65 snapshot is not a constant-count guarantee.

### Other exercised checks

`final-verification-4800fd7.json` contains the commands, stdout/stderr, exits, durations and digests for every final check: proc selftest, proc fixture 19/0, quarantine selftest **108/0**, jj receipt fixture **37/0/0** with `--baseline-dir` (both identity controls exercised), preservation selftest **47/47**, external fixture **8/8**, real frozen regeneration at 4800fd7 and frozen checker **clean**, plus warning-level ShellCheck exit 0. For the jj red arm, export the three baseline tools from b576341 into an isolated directory before passing `--tool-dir`; J13 fails there (committed `jj-receipts-r18-baseb576341.txt`).

## Sources & frontier

Required census command, start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji
```

| Observation | Output / exit |
|---|---|
| Start | `souji ok`, 8 W04 shared-URL/different-scope warnings, exit 0; SOURCES SHA `25c91f68…` |
| End | `souji ok`, 14 W04 warnings, exit 0; SHA `74c5e01e…`; complete output in `source-census-final.json` |

Registry census: rows **63→78**; A **59→74**, B **3→3**, C **1→1**; mined **44→59**, queued **15→15**, rejected **4→4**; malformed **0→0**. `source-counts.json` preserves these counts. Re-derive by splitting `| S### |` rows into the 11 contract cells (tier column 4, status column 8), using `git show b576341:corpus/SOURCES.md` for before and current SOURCES for after.

- New rows S064–S071: absent→opened/mined, 2026-10-20, `on-release`, used-by round-18 lesson.
- Corrections S072–S078: absent→opened/mined; `teaches` starts `supersedes S0NN —`. Original immutable rows are preserved, not silently fixed.
- Existing `status/recheck/used-by` changes: **none**. S038 was reopened; its mutable installed-info anchor drift remains disclosed and routed.
- Each new row's URL, access date and ≤25-word located quote is in the lesson Gate. All initial quotes were independently reopened by wave 2; seven overbroad teaches extrapolations were narrowed through new correction rows.
- F5 was entered as **observed/frontier**, not Core. No new `knowledge/` entry or permission to reap processes is claimed. No F1–F4 frontier closure is claimed.

## Trend verdicts

- **expansion: improved as a capability/frontier move** — three demonstrated capabilities enter SCORECARD and F5 is newly observed. **No knowledge-entry count growth** is claimed; the outside closure decides capability admission.
- **quality: improved** — committed evidence pointers in the existing jj knowledge entry re-verify, the missing-name/summary drift is corrected, real frozen evidence is regenerated, and source over-attribution is visibly superseded. The rejected universal liveness wording and runtime/sandbox limits remain explicit.
- **discernment: improved, author-side evidence; independent confirmation pending** — r17 closure disagreements R1–R4 became lesson-backed Q29–Q31; wave-2 disagreements led to Q33–Q35, stronger negative controls and retained failed observations. These lane-dispatched seats are **not** the required outside judge. The later non-author closure must sample an admit and a reject.

## SHONEN

No `[x]` promotion claim is made; no round-18 non-author verifier exists yet.

- [~] Real decision tables, error patterns, checklists, sources — SKILL sections and SOURCES; unchanged checklist evidence pointer, extended this round.
- [~] End-to-end domain task executed/logged — LOG:362 operator sweep; r18 bounded census measurements and final acceptance records add evidence.
- [~] Executable without oral context — named Gate-registry commands and fixtures; limits and prerequisites disclosed.
- [~] No cross-domain bleed — PROVINCE F5/Adjacency; liveness routes to mori, host repair to tsukuroi, credential-shaped content to kagi; listing is not reap authority.

### Swarm, deviations and operator handoff

- **Wave 1: 91** (27 scout, 15 executor, 15 reviewer, 10 scribe, 8 connector, 8 critic, 4 revenger, 2 sentinel, 2 simplifier). Four complete job-cap refusals, fifth dispatch succeeded at 16:53:50. **Wave 2: 79** (34 reviewer, 24 scout, 6 critic, 4 mutation-tester, 3 connector, 2 sentinel, 2 scribe, 2 revenger, 2 simplifier), first dispatch succeeded at 18:17:16. **170 distinct seats**; L1 holds the frozen planner seat. No nested delegation appears in exported transcripts. Same-identity follow-ups are not new seats.
- Initial wave deaths: **0 + 0**. One source-correction follow-up failed: `ScribeRowsGit-5`, `[anthropic/claude-haiku-5-5] 429 rate_limit_error`, retry-after **8,152,000 ms**. Never replaced; L1 reopened and corrected the sources. Registry/spec/dispatch/refusal evidence and `dead-seats.json` are committed.
- Mutation evidence is honest: watchdog 2 killed/4 survived; pointer gate 4 killed/2 survived; proc 3 killed/2 survived/precedence inconclusive on the first landing. Discriminator cases were added for the concrete gaps; unactivated/environ-prohibited probes are not counted killed. Session-kill mutants were later activated and killed in both helpers.
- Transcript audit is **not clean**: 170/170 manifest verified; gitleaks exit 0/no leaks (~1.80 MB); raw w1/w2 majors **139/92**. Per-call adjudication retains 196 false positives, 26 contract deviations and 9 forbidden driver-state reads. MatrixR18 also disclosed SIGKILL of four unowned prefix-matched processes; the old measurements are void. L1 reran all installed acceptances, used no forbidden-read content, and used a status-only misroot sweep. Evidence: `seat-audit-adjudication.json`, lesson Process. Truncated rendered arguments mean this is not proof of absence.
- Final fleet misroot sweep found no souji seat file misplaced at the fleet root. Driver state files and another lane's report were untouched. No operator sweep contents were opened; only the inherited path remains untracked.
- **Open L0:** inherited r16 contraction scope; r17 jj keep-ref retention and operator-sweep disposition; new r18 approval to reap 58 inherited souji fixture orphans and permission/procedure to re-derive the r14 namespace-control pin. New questions are fleet `52b3863`, lines 70–71. Route around them: no inherited process reaped, no gc, r14 control restored, certification OFF.
- **Stale-lane:** respawn-per-round driver; this is souji round 18 only, no other souji mission is open. Round 19 is planned in SCORECARD, not started.
- **Tool installs/updates: none.** Existing tools were used; all pacman transactions remained paused.
