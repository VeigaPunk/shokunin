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

## Erratum 3 — additional wave-1b mutation result (appended after Erratum 2)

- `MutCarryEllipsis` completed: mutant M1 (accept any prefix without the ellipsis check) is
  **KILLED** by the unchanged carry fixture — pristine PASS/exit 0, M1 FAIL/exit 1, restored
  PASS/exit 0; the restored rule's sha256 matches pristine exactly
  (`342085992da876a75418ca00471d4e70d0c13adc14a3ac475f5280a42c973674`). This confirms the
  ellipsis guard is load-bearing for C1. Report committed in lane commit
  `93e51f58a5d2346e96bfa7d965670a38aed0c272`; no code change.
- Final lane tip at this erratum: `93e51f58a5d2346e96bfa7d965670a38aed0c272`. Remaining
  wave-1b seats' reports, if still landing, remain uncommitted and unadjudicated.

## Erratum 4 — source-quote correction from wave 1b (appended after Erratum 3)

- `ScribeSources` re-opened S082–S085 (and S075/S076) on the live man7 pages: every quote is
  verbatim; three **Gate word counts were wrong** (S082 13 not 15, S083 13 not 17, S085 18 not
  23; all ≤25) and three `teaches` cells overreached the page text. Corrections: a lesson
  correction section appended; **S086–S088** supersede only the S083/S084/S085 teaches cells; no
  other SOURCES cell changed. S079–S081 were outside that seat's item and are not re-verified by
  it (open second-source check).
- Lane commit `4be24d515fa09166dd47942eb4f3ed6774deeb84`; final lane tip at this erratum
  `4be24d515fa09166dd47942eb4f3ed6774deeb84`. No code changed after the 18/18 acceptance
  at `63bb887`. Remaining wave-1b reports, if still landing, remain uncommitted/unadjudicated.

## Erratum 5 — wave-1b corrections and residuals (appended after Erratum 4)

- `ScribeProcSkillRow` verified the integrated r19 text and found: (a) the C3 preregistered
  counting command `grep -c 'status: admitted'` is **defective** (matches nothing; returns 0
  before and after) — corrected by appending to `preregistration.txt` that the measured command
  is `count-claims.py` (6→7); (b) the F5 entry's "reads only" list omits `/proc/uptime`,
  `boot_id` and the `/proc` listing — an append-only correction now names the full set;
  (c) the SKILL rule and README F5 row are **close but incomplete** versus the seat's verbatim
  draft (exact command, list/nominate/reap vocabulary, zero-signal route, fixture command,
  cross-link), and the Frontier bullet cites an L0 line no lane file locates. Those two text
  improvements are **open for r20**, not applied at this budget stop; no behavior changes.
- `MutRevPin` could not produce killed/survived verdicts: the fixture creates a synthetic git
  repo, and the wave contract's blanket "no git or jj mutations" stopped all five attempts before
  `git init`. Both mutants were restored byte-for-byte; **no killed claim is made**. This is the
  same contract-wording defect as R19-M7; it remains the reason wave 2 must allow private
  `/var/tmp` sandboxes.
- Lane commit `d707fc982cc4754fb73ab366238ae0266dca691a`; **final lane tip at this
  erratum: `d707fc982cc4754fb73ab366238ae0266dca691a`.** No code changed after the 18/18
  acceptance at `63bb887`; later seat reports, if still landing, remain uncommitted.

## Erratum 6 — further wave-1b falsification results (appended after Erratum 5)

- `MutCarryJoin`: mutant M2 (bypass `carry_entries`) is **KILLED** by TC4 — pristine 10/0,
  M2 9/1, restored 10/0; all five pinned carry verdicts and a strict round-18 control stayed
  unchanged. Confirms the lesson-bullet join is load-bearing.
- `ConnCarryParsers`: no second production STATUS-carry parser exists in tools/ or tests/; the
  auditor and harnesses parse different formats. No blind spot found.
- `CriticRevPin`: **open C2 gap** — `census/round-14/run-targeted.py` is not in the r14
  `MEASURED_PATHS` list, so that wrapper's own bytes can be dirty when it stamps its revision
  (false provenance). Not fixed at this budget stop: a one-line fix without a re-run of the
  fixture and acceptance would be an unverified change. Recorded for r20.
- `ScribeProcEntry`: its 8-item revision proposal is recorded, but **L1 disputes item 3** —
  `proc_pid_status(5)` does document the state-letter list in its State field paragraph, so
  S085/S088 stand; the remaining items (source line missing the fixture, verified-at, redaction
  scope, argv/fd defaults, silent omission, identity detail, recheck header) are **open revisions**
  and were not applied unverified at the stop.
- Lane commit `8acf281ab0e8ce360a7c315081c911992b6e8e4d`; **final lane tip at this
  erratum: `8acf281ab0e8ce360a7c315081c911992b6e8e4d`.** No code changed after the 18/18
  acceptance at `63bb887`; further seat reports remain uncommitted.

## Erratum 7 — auditor-fixture coverage gap fixed (appended after Erratum 6)

- `MutAuditPatchPath`: two requested mutants **survived the r19 fixture** — accepting any
  absolute target ending `.patch` (the negative tools case tested only `x.py`) and dropping
  `os.kill` from the signal tokens (the signal case tested shell `kill` only). A supplemental
  exact-class witness killed both, so the mutations were effective and the **fixture** lacked the
  cases. Fixed in lane commit `019aefa27c1c5a85e851376345dca6be2f33cfcf` by adding
  `patch-in-tools` (`tools/x.patch` must stay `V-WRITE-SCOPE`) and `signal-os-kill`
  (`python3 -c 'os.kill(...)'` must be `V-SIGNAL`); the fixture now runs 7 cases, 0 failed.
- `ScoutProcCounter` independently confirms the D2 digests: counter at `2d4c7f8`
  `a26530199434ecddf4b36d2513730765bb0ae7487fa3c007f9c04d33244ebb3b`, tool
  `37c3316a1fd8cdda18cbefdc7692d3d3f388e5783e8fe19085f5d932a8ceba64`; the r18 agreement
  records indeed carry no counter digest, which is why `proc-agreement-pinned.json` exists.
- Lane tip at this erratum: `019aefa27c1c5a85e851376345dca6be2f33cfcf`. No other code
  changed after the 18/18 acceptance at `63bb887`; the acceptance record does not cover this
  fixture-coverage edit, which is verified by the fixture's own 7/0 run.

## Erratum 8 — PROVINCE F5 contradiction corrected (appended after Erratum 7)

- Two independent wave-1b seats (`CriticProcEntry`, `ConnSiblingOverlap`) found the same
  internal contradiction: `PROVINCE.md` still said F5 had no knowledge entry while the r19
  SKILL/README identify one. Corrected by appending a **Round 19 boundary refinement**: the F5
  observation surface (own-uid cwd/argv/fd listing) is Core with its entry and SKILL rule; the
  earlier frontier sentence is superseded for that surface only; reaping still requires operator
  approval, fresh identity verification and LOG receipts; other uids/liveness stay mori's.
  Lane commit `3a25875cee6053ec7f76ed278986d6367bf7bff7`.
- `RevCarryHistory`: the evidence points to the r16 gate's first-physical-line rule (inference,
  no explicit L1 intent found) for five incomplete cuts; two other excerpts stop at complete
  clause boundaries. No retro-correction — the disclosure stands.
- `ConnSiblingOverlap`: no sibling charter claims wrap-aware STATUS parsing or souji's
  list-only residue surface; five siblings have analogous lane-scoped revision/landing rules
  that souji must not absorb.
- **Final lane tip at this erratum: `3a25875cee6053ec7f76ed278986d6367bf7bff7`.** No
  production code changed after the 18/18 acceptance at `63bb887`.

## Erratum 9 — Q36 lesson anchor corrected (appended after Erratum 8)

- `ScoutQualityMap` found that Q36's lesson cell cited a nonexistent "round-16.md D5"; the
  truncation finding is **round-17.md:72 (D5)**. Corrected in lane commit
  `c6703daef7dfa7de2f1a5a72e86f40de3717049b`; no other criterion text changed.
- `ScoutAuditModel` confirms the two base shapes (patch delivery, slot-suffixed clone) both major
  at base and proposes granting the seat's explicitly slot-qualified scratch root in addition to
  the exact patch file. **Not applied**: it would need a fresh r18 re-audit and acceptance run,
  and the clone-path majors are already disclosed as a residual.
- **Final lane tip at this erratum: `c6703daef7dfa7de2f1a5a72e86f40de3717049b`.** No
  production code changed after the 18/18 acceptance at `63bb887`.

## Erratum 10 — late adjacency/source findings (appended after Erratum 9)

- `ConnProcAdjacency` flags two wording tensions in the F5 entry: it assigns **all other-uid
  residue to mori** (broader than mori's stated health surface), and it says souji never reads
  secret content while the census reads `argv` **before** redacting credential-shaped values.
  A proposed adjacency sentence covers mori/tsukuroi/kagi. Not applied: it belongs to the open
  entry revision, and the read-then-redact order is a real disclosure the entry must state.
- `ScoutSourceSearch`: `pidfd_send_signal(2)` is a candidate for PID-reuse context but does not
  prove the no-signal claim; `proc_pid_stat(5)` field 22 duplicates S075. No row added at the
  budget stop; the proposed row joins the open source list.
- Lane tip unchanged at **`c6703daef7dfa7de2f1a5a72e86f40de3717049b`**. No code or corpus change
  in this erratum; late wave reports remain uncommitted under `.ufo/waves/round-19/w1/`.

## Erratum 11 — C2 abbreviation contraction and a seat read deviation (appended after Erratum 10)

- `ScoutCountClaims` found that the lane's logged r13 commands use **abbreviated** hashes (e.g.
  `31984f4`), while the C2 resolver accepts only full 40-hex ids; those historical commands now
  refuse. The claim was worded for 40-hex replay commands, so it is not false, but the contraction
  is real and is disclosed here. Open for r20: either widen the helper to a unique hex prefix
  (still refusing symrefs) or re-record the affected commands with full hashes. r14's committed
  command records already use full ids; default `HEAD` refusal is expected and documented.
- The same seat disclosed a contract deviation: an initial broad grep over the lane root included
  `census/operator-sweep-20261019/` (read-only; no write). Per Q26 the affected evidence is not
  relied on: the abbreviation finding is independently verifiable from `LOG.md` itself.
- `RevCarryVacuity` confirms the minimal non-vacuity guard is the complete source-line boundary and
  that wrapped lesson entries still need joining; no change required.
- Lane tip unchanged at **`c6703daef7dfa7de2f1a5a72e86f40de3717049b`**. Late reports remain
  uncommitted under `.ufo/waves/round-19/w1/`.

## Erratum 12 — final wave-1b disclosures (appended after Erratum 11)

- `ConnToolsPatterns` reports **partial** status and discloses a second Q26 deviation: a `census/`
  root listing displayed child names/metadata of `census/operator-sweep-20261019/`; it did not read
  or search files there and made no change. No evidence in this report rests on that listing. It
  also maps duplicated r13/r14 worktree-pin and counter adapters (candidates for a shared
  entrypoint, not applied) and flags the helper's `git diff --quiet` tree check as a read-only risk
  to verify. The diff docs state `--quiet` disables external diff helpers; the helper already
  neutralizes hooks/fsmonitor/maintenance, and it runs only in the lane repo. Recorded, not changed.
- `ScoutWriteScope` confirms 68 distinct report paths, no same-file executor collisions among the
  planned targets, and flags the D1 receipt filename (now fixed as
  `census/round-19/gate-at-commitB.json`) and the C2/C3 shared counter dependency (both use
  `count-claims.py`; C3's count is independent of the C2 resolver for the base/end measurements).
- Lane tip unchanged at **`c6703daef7dfa7de2f1a5a72e86f40de3717049b`**. This is the final erratum
  filed by this run; late wave reports remain uncommitted and unadjudicated under
  `.ufo/waves/round-19/w1/`.

## Erratum 13 — S079 count corrected; final late-report routing (appended after Erratum 12)

- `RevSourcesQuotes`: **S079's quote is 18 words, not 20** — corrected by an appended lesson
  correction; S079–S081 teaches cells mix documentation with implementation statements and need
  narrowing rows (S089+) before the next admission. Quotes are verbatim; no row rewritten.
  Lane commit `51aa813077fa8f5e414dd5d30b2e7291188ce427`.
- `RevAuditOrigin`: patch delivery/clone workflows postdate the auditor's r16 creation and r17
  calibration; r18 declared them, and the derived scratch rule misclassified some W2/variant
  paths. Recommendation (exact per-item patch and scratch permissions) matches Q38; the
  slot-qualified scratch grant remains open.
- `ConnClaimSeparability`: C1/C2 have independent measurements; C3's count shares the C2 helper
  and the aggregate acceptance runner is the shared surface — noted, no change.
- **Final lane tip at this erratum: `51aa813077fa8f5e414dd5d30b2e7291188ce427`.** No code
  changed after the 18/18 acceptance at `63bb887`; remaining reports stay uncommitted.

## Erratum 14 — Q38 protected-path wording corrected (appended after Erratum 13)

- `RevAuditShapes` raised a high finding: the auditor's allow-list can clear a protected-path
  write through an exact absolute `OWN ONLY` grant (that is the executor contract, and wave 1b
  grants none), through unvalidated spec `name`/`reportDir` (the wave parser validates the name
  grammar and a relative reportDir; the auditor itself does not), and through pre-existing symlink
  aliases (the check is lexical). The published Q38 sentence "any `tools/` … stays major" was too
  absolute; it now names the `OWN ONLY` exception, the lexical/symlink limit, and the parser's
  validation role (lane commit `2efadf6f55a6b2371475d9a64b85ee4b21a5a621`). A defensive
  spec-symlink check remains open for r20; no production code changed.
- `RevD5` confirms the bounded `(session,starttime)` recheck and that the later `killpg` is not
  covered by the per-PID check; `RevCarryHistory` and `ScoutS038` confirm the recorded carry
  attribution and the S038 anchor drift (S089/S090 proposals open).
- **Final lane tip at this erratum: `2efadf6f55a6b2371475d9a64b85ee4b21a5a621`.** Remaining
  wave reports stay uncommitted; no round 20.

## Erratum 15 — final falsifier confirmations (appended after Erratum 14)

- `ReviewerCarryFixture` notes the fixture's vacuity guard would pass if only TC4 discriminated,
  and that the summary counters are not asserted. The committed run shows **both** TC1 and TC4
  base mismatches (`base_discriminating=2`), so the present evidence is intact; a strict
  two-case guard and counter assertions are open fixture-strength items for r20.
- `RevCarryRule` restates the known conflict: the `--round >= 18` branch preserves the pinned r16
  replay while leaving its seven unmarked cuts unreported. Already disclosed; no change.
- `ScoutD1Receipt` confirms no committed r18 receipt binds `8be6523`; the r18 gate claim remains
  scoped to `74f9adb`, and r19's receipt binds `63bb887`. The `8be6523` result stays unavailable,
  not claimed.
- **Final lane tip at this erratum: `2efadf6f55a6b2371475d9a64b85ee4b21a5a621`.** Remaining wave
  reports stay uncommitted; no round 20.

## Erratum 16 — two code fixes from the last falsifiers (appended after Erratum 15)

- `RevRevPin`/`CriticRoundAdmission` found that r14's `resolve_revision()` printed to
  `sys.stderr` without importing `sys`, so a refusal raised `NameError` instead of exiting 2.
  Fixed (`import sys`); exercised in place: the refusal path now prints and exits 2.
- The auditor's signal token set missed `os.killpg`/`killpg`; added. Auditor selftest 73/0 and
  a direct in-memory probe on `python3 -c 'os.killpg(...)'` now fires `V-SIGNAL`.
- Still open: r13/r14 `MEASURED_PATHS` omit `run-targeted.py` and the helper itself (provenance
  completeness; not falsified by the current fixture, recorded for r20).
- Lane commit `bbeb73bd4dad181b9b293b242dbf5749acbe3568`. These change code **after** the
  18/18 acceptance at `63bb887`; they are verified by the probes and selftest above, not by a
  full acceptance re-run. **Final lane tip at this erratum: `bbeb73bd4dad181b9b293b242dbf5749acbe3568`.**

## Erratum 17 — final acceptance at the fixed tip (appended after Erratum 16)

- Acceptance re-run at `bbeb73bd4dad181b9b293b242dbf5749acbe3568`: the first attempt failed only
  because `gate-replays` refused to overwrite the `63bb887` record (`exit 2`, not a product
  failure). The driver now writes a revision-scoped replay record; the repeat run is **18/18 all
  matched** (`census/round-19/final-verification-bbeb73b-fixed.json`); the failed record is
  retained as `final-verification-bbeb73b.json`.
- `RevProcEntry` finds the entry needs pinned code evidence for the procfs read-set/no-environ
  claims (Q2) and cites S083–S085, now superseded by S086–S088 — an open entry revision, not
  applied. `ScoutAuditSignal` maps the r18 signal shapes and V-SIGNAL false-positive risks
  (`kill -0` probes, quoted search patterns) for the r20 token refinement.
- Lane commit `649eba34cd02d03aa9b0dc1b92abd5149e131d41`; **final lane tip at this
  erratum: `649eba34cd02d03aa9b0dc1b92abd5149e131d41`**.

## Erratum 18 — r17 cleanup decode guard restored (appended after Erratum 17)

- `ScoutKillSession` found a regression in the integrated r17 `process_identity`: the original
  cleanup caught `ValueError` per entry, but the new helper caught only `OSError`, so a
  `UnicodeDecodeError` on a malformed `/proc/<pid>/stat` would have crashed cleanup. Fixed with
  `except (OSError, UnicodeDecodeError)`; r17 fixture rerun **29/0**.
- `ScoutRevSites` adds two measured-path gaps to the recorded open list: r14 full verification
  runs `tests/fixtures/r14-cache-frozen` without it in the path set, and r14 targeted does not
  tree-check its own script. Not fixed (path-set completeness needs a fresh acceptance).
- Lane commit `bf104970048e51939de1a45efc4ef5f068fb46cc`; **final lane tip at this
  erratum: `bf104970048e51939de1a45efc4ef5f068fb46cc`**. No further changes.

## Erratum 19 — evidence packet records added (appended after Erratum 18)

- `ConnEvidenceLayout` identified missing r18-style packet records. Added: `census/round-19/source-census.json`
  (start over base bytes: 78 rows, sha `74c5e01e…`, exit 0; current end: `88` rows, sha
  `436b015c79386b0931641ffe01f4af4c416163e33f8ceed4fd1061a5da72ecff`, exit 0, 17 W04 warnings) and `census/round-19/dead-seats.json` (68 spawned after the
  first-attempt 68/68 refusal, 0 dead, 22 packing-unexecuted named, last live snapshot 9 running).
  Not produced: a 68-seat transcript export and an r18-style census matrix — the former would need
  a per-seat transcript pull after the budget stop, the latter is an r18 artifact not run this
  round. Both are disclosed rather than simulated.
- Lane commit `49b64584e48aee7c21757a19601bfa4524c05b13`; **final lane tip at this erratum:
  `49b64584e48aee7c21757a19601bfa4524c05b13`**.

## Erratum 20 — all late wave-1b evidence committed (appended after Erratum 19)

- Committed the complete `.ufo/waves/round-19/` set (late seat reports, w1/w1b/w2 specs,
  dispatch registry, preregistration) after a gitleaks secret-shape scan (dir scan, redacted,
  exit 0, no leaks) and a >1MiB check (none). Lane commit `e6df080a60cae997bfcd387738a87aa449c85484`.
- These reports are **committed but unadjudicated**: their findings are already routed in
  errata 1–19 (fixes landed where bounded, the rest open for r20). No production change, no new
  claim, no filed-text rewrite, no round 20.
- **Final lane tip: `e6df080a60cae997bfcd387738a87aa449c85484`.** Lane dirt after this
  commit: only the inherited, untouched `census/operator-sweep-20261019/`.
