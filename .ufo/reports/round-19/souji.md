# souji — round 19 (hyaku phase 2)

Lane: `/home/vgpnk/Projects/shokunin/souji-shokunin`. Baseline `3ab2c81479f5004c8bc91946eea482caec45408f`
(round-18 closure tip). Lane tip at this report: `25bf2d50beef4e6c0c9801122affdf7e867d0412`
(pushed; `jj-lane.sh state` local=remote, ahead=0). Axes: calibration 7 (lowest non-retired), operability 8, coverage 8.

## Work performed

Declared claims (pre-registered in `.ufo/waves/round-19/preregistration.txt`):

- **C1 calibration** — the landing gate's carry check and the seat auditor's contract shapes tell
  the truth: wrapped STATUS paragraphs are matched as paragraphs (an unmarked cut at a source
  physical-line end is `LG-SEAT-UNCARRIED`; an ellipsis exactly there carries; a complete
  paragraph carries; a wrapped lesson bullet is joined), strict branch gated at `--round >= 18`;
  the auditor allows exactly the sibling artifacts the wave contract authorizes and majors a
  signal-shaped call.
- **C2 operability** — the r13/r14 evidence runners and both `count-claims` consumers stamp only
  a durable 40-hex revision (reachable from `refs/heads|refs/tags|refs/remotes`, never `refs/jj`)
  whose tracked measured bytes equal the working tree; refusal exits 2 and writes no record.
- **C3 coverage** — F5 process residue gains its first admitted `corpus/knowledge/` entry, sourced
  from man7 pages opened this round, with its SKILL rule and README row; list-only, no reap
  authority.

Work items (evidence pointer each):

- C1 gate rule and cases: `tools/souji-landing-gate.py` (`WRAP_STRICT_FROM_ROUND`,
  `_continues_paragraph`, `status_paragraph`, `carry_entries`, `carries`), four selftest cases;
  `census/round-19/c1-carry.txt`.
- C1 external gate: `tests/fixtures/r19-carry-wrap.py` (4 cases, base arm discriminates 2);
  `census/round-19/carry-invariants.txt` (400 seeded paragraphs, 1,404 cuts, 0 violations).
- C1 history: five pinned replays unchanged (`census/round-19/gate-replays-r19.json`); strict
  receipt over the r18 lesson at `3ab2c81` (`census/round-19/gate-r18-strict-fleet.json`).
- C1 auditor: `tools/souji-seat-audit.py` (`DELIVERY_SUFFIXES`, `V-SIGNAL`); selftest 66→73;
  `tests/fixtures/r19-seat-audit-shapes.py`; r18 transcript re-audit
  (`census/round-19/seat-audit-r18-recheck-w1.json`, `...-w2.json`).
- C2 helper and wiring: `tools/souji-rev-pin.py`; `census/round-13/{run-verification,count-claims}.py`;
  `census/round-14/{run-verification,run-targeted,count-claims,cache-demonstration}.py`;
  `tests/fixtures/r19-rev-pin.py`; `census/round-19/c2-smoke.txt`.
- C3 entry and ground: `corpus/knowledge/process-residue-observations.md`; SKILL rule;
  `corpus/README.md` F5 Core row; `corpus/QUALITY.md` Q36–Q38; `corpus/SOURCES.md` S079–S085;
  `census/round-19/counts-start.json`, `counts-end.json`.
- D2: `census/round-19/verify-agreement-pin.py` and `census/round-19/proc-agreement-pinned.json`.
- D5: `(pid, starttime)` recheck in the r15/r17 `kill_session`; fixtures 20/0 and 29/0.
- D3: old 33 baseline stays labeled static; 61/0 is receipt-backed. D1: gate receipt
  `census/round-19/gate-at-commitB.json` binding `63bb8878bace9f814c1d94a8c7932b37da1259c8`.
- D4 folded into C1: `V-SIGNAL` surfaces the three real signal calls in the r18 w1 transcripts
  that the old auditor could not see (R18-M6 class).
- Pre-submit rehearsal in a private sandbox found the r15 preservation pin break caused by D5 and
  the three dangling lesson citations; both fixed before landing (R19-M6 records a tracked-pyc
  cleanup mistake and its byte-exact restoration).

## Landed changes

| commit | contents | LOG entry |
|---|---|---|
| `005f3d376e5b421c57c4405be37fb10e7ab49381` | C1/C2/C3 code, fixtures, docs, sources, evidence, wave specs | `LOG.md` round-19 entry |
| `63bb8878bace9f814c1d94a8c7932b37da1259c8` | r15 preservation pins regenerated from real runs at `005f3d3`; end counts; commit-A pin receipt | same entry + regenerated `record.json` |
| `4ecb0dfdffa930864946705f3a9bcde74cd2f395` | gate receipt binding `63bb887` | same entry |
| `1db7108dfa305c53916522193e014e9ae8400d16` | measured SCORECARD rows/capabilities/planned, 18-command acceptance record, gate replays, wave hold disclosed | appended acceptance entry |
| `25bf2d50beef4e6c0c9801122affdf7e867d0412` | acceptance driver summary-parse fix (record tails unchanged) | appended correction |

## Before → after measurements

| claim | counting command | before | after | measured commit |
|---|---|---|---|---|
| C1 carry | `python3 tests/fixtures/r19-carry-wrap.py` | base gate: unmarked cut exit 0, wrapped bullet `LG-SEAT-UNCARRIED` (2 discriminations) | 4/0 cases; `SUMMARY total=4 failed=0 base_discriminating=2` | `005f3d3` |
| C1 gate selftest | `python3 tools/souji-landing-gate.py --selftest` | 61/0 | 65/0 | `005f3d3` |
| C1 invariant probe | `python3 census/round-19/probe-carry-invariants.py` | n/a (new) | 0 violations over 400 paragraphs / 562 boundary / 842 mid-line cuts | `005f3d3` |
| C1 audit | `python3 tools/souji-seat-audit.py --selftest` | 66/0 | 73/0 | `005f3d3` |
| C1 re-audit | `python3 tools/souji-seat-audit.py --spec .ufo/waves/round-18/w1-spec.json --transcripts census/round-18/transcripts/w1 …` | w1 139 major / w2 92 | w1 134 (8 delivery false rows removed, 3 real signals added) / w2 92 | `005f3d3` |
| C2 helper | `python3 tools/souji-rev-pin.py --selftest` | none (new) | 11/0 | `005f3d3` |
| C2 fixture | `python3 tests/fixtures/r19-rev-pin.py` | pre-fix stub accepts all 6 refusal cases | 13/0, 6 base discriminators, 0 leftovers | `005f3d3` |
| C2 real refusal | `python3 census/round-13/run-verification.py --round 19` on the dirty lane | would stamp `HEAD` over uncommitted bytes | exit 2, no output file | working tree at `005f3d3` |
| C3 knowledge | `python3 census/round-13/count-claims.py <rev>` | admitted 6, sources 78 | admitted 7, sources 85 (mined 59→66) | `3ab2c81` → `005f3d3` |
| C3 census | `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` | exit 0, sha `74c5e01e…` | exit 0, sha `24a411da…` | base bytes / `005f3d3` |
| D2 | `python3 census/round-19/verify-agreement-pin.py --check …` | no digest binding | exit 0 with tool/counter/agreement digests | `005f3d3` |
| D5 | `tests/fixtures/r15-census-config.py --tool tools/souji-census.sh`; `r17-census-hygiene.py --census tools/souji-census.sh` | n/a | 20/0 and 29/0 | `005f3d3` |

## Sources & frontier

SOURCES rows 78 → 85 (`bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`,
start exit 0 over the base corpus bytes, end exit 0; 14 W04 shared-URL warnings, no errors). Rows
added by tier: A +7 (S079–S085: git-rev-parse, git-for-each-ref, git-diff, proc_pid_cwd, proc_pid_fd,
proc_pid_wchan, proc_pid_status), B 0, C 0; mined 59 → 66, queued 15, rejected 4, malformed 0.
Rows touched old→new: none of S001–S078 changed; S075/S076 re-opened and rechecked, status and
cells unchanged. Frontier rows advanced: F5 moved from frontier to Core for the *observation*
surface (entry + SKILL rule + README row); F1–F4 unchanged. The r15 frozen preservation record was
regenerated from real runs at `005f3d3` (pre-harm 8/20 fail, baseline 16/20, changed 0/20,
namespace 0/12, verdict clean) because D5 changed a pinned fixture byte; that is a deliberate
re-pin, not a weakened expectation.

## Trend verdicts

- **expansion: improved.** F5 gains its first admitted knowledge entry (6→7 admitted), seven new
  mined source rows, and three demonstrated capabilities (paragraph-aware carry, durable revision
  binding, auditor delivery/signal classes). No knowledge entry was added on F1–F4.
- **quality: improved.** The carry gate now detects what it silently passed (7 historical wrapped
  quotes are named, not rewritten); the auditor no longer majors authorized delivery; D2 and D5
  close two routed defects; D1 and D3 have their owed receipts/labels. The r15 preservation record
  was regenerated from real runs, not hand-edited.
- **discernment: improved, with a disclosure.** The lane's own counter caught the r18 "admitted
  five" prose defect (R19-M1); the pre-submit sandbox rehearsal caught the pin break and three
  dangling citations before landing; the re-audit keeps every real violation major. The external
  non-author spot-check remains the admission authority.

## SHONEN

- [~] SKILL.md decision tables, error patterns, checklists with cited sources — `SKILL.md`
  r19 error patterns + `corpus/QUALITY.md` Q36–Q38; non-author check pending.
- [~] At least one end-to-end domain task executed and logged — gate/fixture/runner work measured in
  `census/round-19/`; non-author verification pending.
- [~] Instructions executable by an agent without oral context — fixtures self-invoking, SELFTEST
  modes; pending outside review.
- [~] No cross-domain bleed; PROVINCE still accurate — F5 stays list-only, reap to the operator;
  pending outside review.

## Stale-lane

Respawn-per-round driver (hyaku inline). No other souji mission is open; this report closes the
round-19 mission for the lane. The mission started at the watchdog line
`2026-10-21T00:38:34-03:00 launch souji round=19 pgid=2971251 driver=hyaku-inline attempt=1`;
progressing (commits authored by the lane since launch).

## Wave and dispatch

**Wave 1 (build): NOT DISPATCHED.** The 90-seat spec was generated and validated under policy v2
(band 64–100): `counts {"spawn": 90, "resume": 0, "total": 90}`, `maxLanes 100`, registry
`.ufo/waves/round-19/w1/swarm-registry.json`; the dispatch payload was rendered (task context
4,872 B + 90 tasks; role mix 31 scout, 12 reviewer, 11 executor, 9 scribe, 8 connector, 6 critic,
4 revenger, 4 mutation-tester, 3 simplifier, 2 sentinel). Dispatch was held under the
orchestrator's explicit capacity gate ("hold only task dispatch until parent confirms capacity");
no confirmation arrived before the run budget stop. **No seat was spawned; no wave report, transcript
or dead-seat record exists.** The 65-seat wave-2 falsification spec is prepared
(`.ufo/waves/round-19/w2-spec.json`) and was not dispatched.

Consequence, stated plainly: the round's L2 floor (§3: at least 8 L2 subagents in one batched
swarm) and the §6 wave requirement (64–100) are **UNMET**. Seat count this round: 0; dead seats:
none (none spawned). The three claims are author-measured only; the outside closure should not
treat this round as satisfying the wave contract. The implementation, fixtures and the 18-command
acceptance record are real, committed and independently re-runnable, so the work is not lost — but
admission of the wave obligation is not claimed.

## Tool installs

None by L1 or seats (gitleaks, jq, node and the fixture toolchain were already present). No
pacman transaction was run.

## Erratum — waves (appended after the filed bytes; the filed text above is unchanged)

Filed after the orchestrator reopened capacity and directed the wave to run.

- **Wave 1 packing.** The validated 90-seat build spec was re-packed to **68 seats** under the
  process-wide 100-job cap; the 22 dropped items are named in
  `.ufo/waves/round-19/w1b-spec.json` as unexecuted with reason "packing under the 100-job cap".
  The retained seats are read-only falsifiers of the landed work (no executor patch builders).
- **Dispatch.** A first attempt with the 68-seat payload returned 68/68 runtime refusals
  ("Background job limit reached (100)"); **no seat started**. The identical payload was retried
  after 180 s and **spawned 68** (`SoujiR19.*-2`), under slot `souji r19-w1b` granted at
  `live=129 pending=0 cap=200`.
- **State at filing.** Completed: 3 (`SimplCarryRule`, `SimplRevPin`, `SimplAuditShapes`);
  still running: 65; dead/unstarted from the spawning call: 0. Their reports land under
  `.ufo/waves/round-19/w1/`.
- **Verified findings.** The three completed seats independently re-ran the integrated artifacts:
  carry fixture 4/4 with the base arm discriminating and the invariant probe 0 violations;
  rev-pin helper/fixture API minimal and correctly wired across five call sites; auditor delivery
  and `V-SIGNAL` minimal with `r19-seat-audit-shapes.py` 5/0 and base discriminating. No code
  correction was required. One contract defect was disclosed: `MutRevPin` refused to run a fixture
  that creates a synthetic git repo because the wave contract's blanket "no git or jj mutations
  anywhere" conflicts with it; the seat refused rather than fabricate. Lesson **R19-M7** records
  the wording fix for wave 2; the fixture itself is unchanged (L1 ran it: 13/0).
- **Wave 2.** NOT RUN: 65 wave-1 seats were still running at the run budget stop, so dispatching
  the prepared 65-seat falsification spec (`.ufo/waves/round-19/w2-spec.json`) would have exceeded
  the process job cap. Round seats spawned: **68**; completed at filing: 3; running: 65.
- **Corrections landed.** Lane commits `90dd68ce33053d8b210a88f90362011dc9047281`
  (wave-1b spec, 68-member registry, first report, R19-M7) and
  `4f0d500339aa4b5103ecb4fb4d921c43e2adbb84` (completed seat reports). **Final landed lane hash:
  `4f0d500339aa4b5103ecb4fb4d921c43e2adbb84`.** No code changed after the 18/18 acceptance record
  at `63bb887`; that record remains the code measurement.
- **Slot.** `souji r19-w1b` released at filing; the running seats remain counted by the gate's
  live measure.

## Erratum 2 — additional wave-1b finding (appended after Erratum 1)

- `CriticD5` completed after Erratum 1. It judges the D5 `(pid, starttime)` recheck an
  admissible **bounded** improvement, not a PID-recycle proof, and records the residual
  check-to-signal window plus an **unguarded `killpg(session, SIGKILL)`** call in the fixture
  cleanup. No code change was made at the budget stop; this is an open operability residual for
  r20, alongside the already-disclosed D5 TOCTOU. Report committed in lane commit `7d199d2b2446cac1a0c6d08c53e1e950e99bec35`.
- Lane tip after this erratum: `7d199d2b2446cac1a0c6d08c53e1e950e99bec35`. The other wave-1b
  seats' reports continue to land under `.ufo/waves/round-19/w1/` and remain uncommitted at filing.
