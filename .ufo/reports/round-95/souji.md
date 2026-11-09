# souji — round 95 report (L1 SoujiR95, attempt 1)

Lane `souji-shokunin`, branch `master`. Base `93c3ef13a9eb9678483518562f3692124db714c2` (r94 closed admitted). Final
lane hash `71a1ae0951c605e4d539cd25db3a5aad150c003e` (pushed; see Extras, pre-report gate). Date 2026-11-09.

## Work performed

Declared claims (2): **C1 — calibration 7** (the lane's lowest owned non-retired axis): crash-channel fixtures the
survivor search scores other than errored, 5 → 0. **C2 — operability 8**: forgery-probe arms whose exit code matches
its meaning, 12 → 16 of 16. C1 is the round's sourced claim (S360-S364, opened 2026-11-09).

- Claim choice, A0 (L1 planner seat): r94 spot-check §5 item 1 → C1, item 3 → C2; items 2, 4, 5 carried
  (`souji-shokunin/plans/round-95.md` A0.0). MANIFEST: souji r90-r94 admitted, no pause.
- P1 instruments `d79bc3fe`: r95 search with a five-channel sentinel (`sys.unraisablehook`, `threading.excepthook`,
  `os._exit`, a `sys.monitoring` RAISE leg for SystemExit, signal leg in the rule) and a per-channel CHECK precondition
  (`census/round-95/c1-survivor-search.py`), ten targets, r94-rule control wrapper, C1 forgery runner; r95 probe with
  decode/create/write/timeout/internal-error refusals (`census/round-95/c2-forgery-probe.py`), sixteen-arm counter,
  C2 forgery runner; five source captures (`census/round-95/srcs/`), rows S360-S364, knowledge entry
  `corpus/knowledge/crash-channels-beyond-excepthook.md`.
- P2 controls `48c5efe9` (before F): C1 do-nothing `errored=2 killed=5 survived=3`
  (`census/round-95/controls/c1-control-r94-rule.txt`), FA/FB/FC refused 3/3 (`controls/c1-forgery-controls.txt`);
  C2 do-nothing `ARMS-SUMMARY arms=16 conform=12` EXIT 1 (`controls/c2-control-r94-probe.txt`), GA/GB/GC refused 3/3
  (`controls/c2-forgery-controls.txt`); pre-freeze trial runs disclosed (`controls/prefreeze-feasibility-note.txt`).
- F `59fd7be0`: `census/round-95/preregistration.txt` alone.
- A `dd520684`: after receipts on committed bytes — C1 `errored=7 killed=2 survived=1` with the full check line,
  EXIT 0 (`census/round-95/records/c1-after.txt`); C2 `conform=16`, EXIT 0 (`records/c2-after.txt`).
- Wave w1, 13 seats, all settled (`.ufo/waves/round-95/w1-results.json`); WAVE-DONE received. Every number
  re-derived by non-author seats (R95ExecC1, R95ExecC2, R95Critic, R95Sentinel, R95Scribe).
- Amendments A1-A7 (`plans/round-95.md`): the wave falsified five wording points, each narrowed before filing — A1
  SystemExit-leg false positives (R95Labrat; re-measured `census/round-95/records/declared-shapes.txt`
  `SHAPES-SUMMARY shapes=12 mismatched=6`), A2 no unraisablehook at finalization after a SystemExit exit, A3
  `os._exit(0)` → 70 and a crash path that hangs with the stderr lock held (R95Sentinel F1), A5 S13 does not isolate
  the /tmp guard (R95MutC2 PM9), A6 an escaping grandchild hangs the probe past `--timeout` (R95ReviewerC2); A4 scope
  limit; A7 this round's S360/S361 cells corrected. The counted quantities and predicates stand.
- Integration `dc947be6`: amendments, row corrections, knowledge-entry wave corrections, lesson
  `corpus/lessons/round-95.md`, QUALITY Q172, SCORECARD r95 rows + capabilities + `### Planned (r96)`, LOG, census after.
- Wave evidence `71a1ae09`: spec builder, spec, dispatch, results, claims.json, 13 seat reports + receipts,
  `claim-falsification.tsv`, `prefile-gate.txt`.

## Landed changes

| commit | what | LOG.md entry |
|---|---|---|
| `d79bc3fe1a9aa5aaf0104b90c38cc3c8c5850dd7` | P1 instruments, captures, S360-S364, knowledge entry | `## Round 95 (2026-11-09)` |
| `48c5efe9c8b50f56fa7da01fa75298855ef47d84` | P2 controls, receipt runner, census before, feasibility note | same |
| `59fd7be028a7eab071ff8109ad7a1eb10b5f493c` | F preregistration | same |
| `dd5206842fcead3b1e7301d3dbaaec42b625dd54` | A after receipts | same |
| `dc947be605888c068ee31cb04c507f5ae9e70396` | integration (plan A0-A7, rows, entry, lesson, Q172, SCORECARD, LOG) | same |
| `71a1ae0951c605e4d539cd25db3a5aad150c003e` | wave evidence + ledger + prefile gate | same |

## Before → after measurements

- **C1** (calibration 7), measured against `dd5206842fcead3b1e7301d3dbaaec42b625dd54`. Counting command:
  `python3 -B census/round-95/c1-survivor-search.py --counter census/round-87/c1-pointer-counter.py --harness
  census/round-93/c1-false-row-harness.py --population census/round-93/c1-false-rows.tsv --lane . --fleet-root
  /home/vgpnk/Projects/shokunin --work <empty> --jobs 5 --ids census/round-95/c1-targets.json` (before: the same with
  `census/round-95/c1-control-r94-rule.py`). Mis-scored crash-channel fixtures =
  `grep -cE '^SEARCH h-(sysexit|atexit|thread|osexit|sigkill) ' FILE` − `grep -cE '^SEARCH
  h-(sysexit|atexit|thread|osexit|sigkill) .*killed=errored' FILE`: before **5** (control: `errored=2 killed=5
  survived=3`), after **0** (`errored=7 killed=2 survived=1`, check line `excepthook=70 sysexit=70 atexit=70 thread=70
  osexit=70 declared=1 argparse=2`); five r94 targets unchanged.
- **C2** (operability 8), measured against `dd5206842fcead3b1e7301d3dbaaec42b625dd54`. Counting command:
  `python3 -B census/round-95/c2-setup-arms.py --probe census/round-95/c2-forgery-probe.py --fixture-pass
  tests/fixtures/r93-k4-flagfail.py --fixture-fail tests/fixtures/r92-k4-flagfail.py --tool
  tools/souji-record-agreement.py --before census/round-92/controls/c2-before-tool.py --work <empty>` (before: `--probe
  census/round-94/c2-forgery-probe.py`): before **12/16** (S9-S11 exit 1, S12 hung), after **16/16**.

## Sources & frontier

- Rows before → after: 281 → 286, counted by `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
  Added by tier: A ×5 (S360 `sys.monitoring` RAISE, S361 `threading.excepthook`, S362 `os._exit`, S363 subprocess
  returncode, S364 atexit), all `mined`, `used-by` `corpus/knowledge/crash-channels-beyond-excepthook.md`. Rows
  touched old→new: none of the pre-existing rows (`git diff --numstat 93c3ef13 -- corpus/SOURCES.md` → `5 0`);
  S360's scope cell and S361's locator/grounds cells (added this round) were corrected after the wave (A7).
- Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`
  → round start `souji ok` EXIT 0 (`census/round-95/records/sources-census-before.txt`); round end `souji ok` EXIT 0
  (`census/round-95/records/sources-census-after.txt`); W04 duplicate-URL warnings only.
- Live re-open (non-author): R95ScoutSources and R95Scribe fetched S360-S364 live — byte-identical sha256, quotes and
  occurrence counts re-derived. Reject sample: Python `faulthandler` docs (no exit-status statement, SIGKILL absent;
  flip stated); PEP 669, PEP 578, `sys.audit` rejected alongside.
- Frontier advanced: crash channels beyond the excepthook (SystemExit provenance, unraisable, thread, `os._exit`,
  signal) — ground the lane did not hold. Mistakes mined: M1-M4 (`corpus/lessons/round-95.md` `## Mistakes`); M1 is
  the r94 M3 class recurring and its fix (Q172) is shown able to fail by `records/declared-shapes.txt` (mismatched=6).
- Assimilation: none (no `merge/souji/` theme taken). considerthese: the lane has no `considerthese/` dir.

## Trend verdicts

- **expansion: improved.** Five admitted tier-A rows (live-verified by two non-author seats) and a knowledge entry on
  ground the lane did not hold; two capability rows backed by re-measured commands (SCORECARD `### Round 95
  capability rows`).
- **quality: improved.** Two instruments whose verdicts or exit codes misreported are fixed and re-measured by
  non-author seats on committed bytes (C1 5 → 0 mis-scored; C2 12 → 16); the full-population census shows no verdict
  change on the 263 generated ids (R95ExecCensus).
- **discernment: improved.** The lane recorded five falsified wording points as narrowings (A1-A3, A5, A6) instead of
  defending them, corrected its own new rows (A7), re-measured the labrat's finding on exact bytes, and mined the
  recurrence of last round's mistake into a criterion with a failing test (Q172).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `corpus/SOURCES.md`
  S360-S364; `corpus/QUALITY.md` Q172; `corpus/lessons/round-95.md` Gate.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md `## Round 95 (2026-11-09)`
  (controls and after receipts on committed bytes: `census/round-95/controls/`, `census/round-95/records/`).
- [~] Instructions executable by an agent without oral context — `census/round-95/preregistration.txt` commands
  reproduced by non-author seats (`.ufo/waves/round-95/w1/R95ExecC1.md`, `R95ExecC2.md`, `R95Critic.md`,
  `R95Sentinel.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `.ufo/waves/round-95/w1/R95Connector.md` §1: no sibling
  owns the surface; no credentials, history or sibling lane touched.

## Extras

- **Round shape:** one v1 wave (`w1`, policy `ufo-wave-policy.json`, `w1-dispatch.json` validated `spawn 13`), 13
  seats: 3 executor, 3 reviewer (R95Labrat ran the prereg's labrat task as a reviewer — the validator refuses
  `labrat`; plans A0.2), critic, 2 mutation-tester, sentinel, connector (1), scout, scribe; planner held by the L1
  (validator-frozen); the planning data-walk rode R95Connector. Residual call: none. Round total 13. Dead seats: none
  (13/13 settled with a report). Ready file `l1` `SoujiR95`; WAVE-DONE received.
- **Attack share:** 6/13 = 46 % (reviewer ×3, critic, mutation-tester ×2).
- **Pre-file falsification ledger:** `.ufo/waves/round-95/claim-falsification.tsv` (27 rows; 14 `falsifies-wording`,
  each pointing at `plans/round-95.md`). `python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py
  --lane souji --round 95` → `PREFILE-FALSIFICATION: pass claims=2 rows=27 attack_seats=8 findings=0`, EXIT 0 (receipt `.ufo/waves/round-95/prefile-gate.txt`).
- **Pre-report gate:** `git -C souji-shokunin ls-remote origin refs/heads/master` → `71a1ae0951c605e4d539cd25db3a5aad150c003e	refs/heads/master`.
- **Inherited state:** none (attempt 1; lane clean at base, no `lane-dead-no-report souji round=95` line). Not
  authored by this lane and not edited: `corpus/lessons/round-94-verifier-spotcheck.md`, `.ufo/state/*`.
- **r94 spot-check routed defects:** item 1 answered by C1 (and item 2's signal half), item 3 by C2 (write failure,
  TOCTOU, randomized arm names carried); items 2 (harness-side crash target), 4 and 5 (seat temp under the round
  scratch root — written into the wave context; no seat wrote under /var/tmp) carried to `### Planned (r96)`.
- **Misroot sweep:** fleet-root `git status --porcelain` shows no souji r95 file; only orchestrator `.scratch/`
  entries, never touched. No `/tmp/souji-r95*` left.
- **Pre-freeze disclosure:** both after arms were trial-run before F (`controls/prefreeze-feasibility-note.txt`).
- **Stale-lane:** respawn-per-round driver, round 95 of the hyaku campaign; no other mission of this lane is open.
- **Tool installs:** none (no pacman, uv, npx or binary fetch; no sysctl or sudo).
- **L0 questions:** none opened this round.
