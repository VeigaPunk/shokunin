# kumitate — round 10 of ≤1024 (fleet-2)

**Lane:** kumitate-shokunin · **cwd** `/home/vgpnk/projects/shokunin/kumitate-shokunin`
**Axes:** operability + coverage (orchestration/tooling).
**Round move:** one axis-move, operability. **Score 6 → 7** on the frozen proxy.
**Repo commit:** `c91fe96` (`round-10`), pushed to
`github.com/VeigaPunk/kumitate-shokunin` (`d65aa24..c91fe96`), tree clean,
`git rev-list --count @{u}..HEAD` → 0.

## Axis-move and measurement

Frozen proxy since round 8 (`SCORECARD.md`), unchanged this round:
`f_O = (A + C) / (A + C + 3)`, score `= floor(10 × f_O)`.

| Term | Before (r9 close) | After (r10) | Command |
|---|---|---|---|
| A — runnable artifacts with documented invocation + verdict exit | 2 | **3** | `find . -path ./.git -prune -o -type f \( -name '*.mjs' -o -name '*.js' -o -name '*.sh' -o -name '*.py' \) -print \| wc -l` → 3 (`cite-check.mjs`, `surface-probe.mjs`, `round-gate.mjs`) |
| C — `SKILL.md` GFM task items naming a runnable command | 4 | **6** | `grep -c '^\s*- \[' SKILL.md` → 6 |
| `f_O` ⇒ score | 6/9 ⇒ 6 | **9/12 = 0.75 ⇒ 7** | `floor(10 × f_O)`; all 6 items *executed*: `node scripts/surface-probe.mjs --checklists` → `CHECKLIST: 6/6 pass`, `VERDICT: PASS`, exit 0 |

Round 9's plan named the choice and the honest consequence: option (a), a third
live surface in `surface-probe.mjs`, "raises no proxy term" and saturates
operability at 6; option (b), widening the checklist to the fleet-round gates a
lane actually runs, moves `f_O`. (b) was taken. The proxy was **not**
re-chartered, and the arithmetic for 8 is recorded in `SCORECARD.md`:
`(A+C)/(A+C+3) ≥ 0.8` needs `A+C ≥ 12` — six more real executed items or a
scheduled leg, not a redefinition.

Coverage re-measured as bookkeeping (score stays 7): C2 README rows/files
**34/34 → 36/36** (rows for `knowledge/round-close-gate.md`,
`lessons/round-10.md`), C1 **14/18** unchanged, file-level residue **140/211 ≈
0.664** unchanged (the new note cites fleet artifacts — `PROTOCOL.md`,
`MISSION.md`, `watchdog.sh` — not origin sources).

## What landed

`scripts/round-gate.mjs` — contract `kumitate-round-gate-v1`, 1226 L, zero deps,
node ≥20, executable, sha256 `2c6c580b…`. The fleet round-close contract, which
existed only as prose in the dispatcher prompt and as
`report_of() { [ -f … ]; }` in `scripts/shokunin-watchdog.sh:44`, is now a
runnable, exit-mapped, self-tested gate over *this lane's own* artifacts:

- **audit mode** (default; latest closed round, or `--round N`): report present /
  ≥1024 B / ≥2 `#` headings / names its round / carries a `SHONEN` heading;
  cited commit tokens resolve (lane → `--main-repo` → `--origin`) and are
  ancestors of lane `HEAD`; a `SCORECARD.md` row for `N`; a `LOG.md` round
  entry; a `round-<N>` commit marker. 11 kinds (9 error, 2 warning).
- **`--close`**: adds the close-only trio — clean tree, nothing unpushed, report
  tracked *and* pushed in `--main-repo` (`REPORT_UNTRACKED` true-positive below).
- 5 fail-closed arms (exit 2), usage exit 64, `--json` (`kumitate-round-gate-v1`),
  `--strict` warning promotion, 49-case hermetic suite.

Docs: `SKILL.md` (2 checklist items, a `ROUND_GATE: DRIFT` paragraph, a
Working-rules bullet), `corpus/knowledge/round-close-gate.md` (new, 16 invariant
rows each cited to the main repo), `corpus/lessons/round-10.md` (new),
`corpus/README.md` (2 rows), `SCORECARD.md`, `LOG.md` — each change tied to the
`round-10` LOG entry.

The two citation checks are not invented thresholds: they mechanize a **written
integrator step**. `PROTOCOL.md:264-265` — "verifies each cited child-repo commit
exists *and is an ancestor of the lane repo's `HEAD`*" — and
`PROTOCOL.md:118-120` "a report naming a hash the repo does not contain fails
verification". The gate is the lane-local pre-check so a report is
integrator-ready before it is filed; the fleet-level call stays the integrator's
(`PROTOCOL.md:263-267`), which is also why a missing `SHONEN` heading is
warning-class here.

## Evidence (round close)

```
$ node scripts/round-gate.mjs --selftest
ROUND_GATE_SELFTEST: 49/49 pass          VERDICT: PASS          exit 0, 3.1 s
$ node scripts/round-gate.mjs
ROUND_GATE  warning  REPORT_SHONEN_MISSING  no ^#{1,6} SHONEN heading in …round-9/kumitate.md
ROUND_GATE: CLEAN (round=9 lane=kumitate checks=10 errors=0 warnings=1)   exit 0
$ node scripts/round-gate.mjs --round 42
ROUND_GATE  error  REPORT_MISSING / SCORECARD_ROW_MISSING / LOG_ENTRY_MISSING / COMMIT_MISSING
ROUND_GATE: DRIFT (round=42 lane=kumitate checks=5 errors=4 warnings=1)   exit 1
$ node scripts/round-gate.mjs --reports-dir /nonexistent   # exit 2 REPORTS_DIR_MISSING
$ cd /tmp && node <repo>/scripts/round-gate.mjs --repo /tmp # exit 2 NOT_A_GIT_WORKTREE
$ node scripts/round-gate.mjs --bogus                       # exit 64
$ node scripts/surface-probe.mjs --checklists
CHECKLIST: 6/6 pass                      VERDICT: PASS          exit 0
$ node scripts/surface-probe.mjs
SURFACE_PROBE: CLEAN (surfaces=2 checks=12 errors=0 warnings=1)      exit 0
$ node scripts/cite-check.mjs
CITE_CHECK: DRIFT (files=38 tokens=2472 errors=2 warnings=52)        exit 1
```

Both citation kinds were falsified **live**, not only in fixtures — a doctored
report copy: `COMMIT_CITED_UNRESOLVED  cited=5 unresolved=1 [deadbeef0]`; and
round-9's report with `--repo` a throwaway clone checked out at `efe19da`:
`COMMIT_CITED_NOT_ANCESTOR  cited=4 notAncestor=3 [d65aa24 31f09cd 0ac2272]`.

Citation-gate delta, measured in place (`files=36 tokens=2324 errors=2
warnings=52` → `files=38 tokens=2472 errors=2 warnings=52`); both errors remain
the aggregator-owned `LINE_OOR` rows in `corpus/lessons/round-6-aggregator-audit.md`.

**Defect found by the new gate, repaired this round:** `.ufo/reports/round-9/
kumitate.md` was never tracked in the main repo (`git ls-files --error-unmatch`
→ exit 1) — `REPORT_UNTRACKED` fired on our own round-9 report. It is committed
together with this report.

## Claims falsified inside the round (calibration record)

1. **`SCORECARD_PLAN_MISSING` false-positived on a correct tree.** The frozen
   check required `## Planned` to name `round <N+1>`; once round 11's plan
   replaced round 10's, auditing round 9 warned — a finding the lane could not
   fix by any correct action. Found by L1 re-running the gate *after*
   integration. Fix: the body must name any `round M` with `M > N`
   (`scripts/round-gate.mjs:366-372`), one new selftest arm (48 → 49 cases), the
   old negative arm's fixture changed to a past round, and every pinned fact
   (sha, line count, case count) re-pinned in the note, lesson, README,
   `SCORECARD.md` and `LOG.md`.
2. **"Never reads the origin tree"** — my own frozen spec, falsified by the
   cited-hash check: this lane's real reports cite origin-only shas
   (`.ufo/reports/round-9/kumitate.md` cites `ee907f1cf`), so the rule would
   have raised a false `COMMIT_CITED_UNRESOLVED`. Repair: lazy `--origin`
   (default `$UFO_SRC`), consulted only for tokens unresolved in lane and main.
3. **The audit duplicates protocol-lane authority** (critic O1) — partly
   falsified: it is the lane-local pre-check of the integrator's own step, and
   the `SHONEN` check is warning-class. The critic's *disagreeing-labels* point
   is kept as a documented split verdict: `.ufo/reports/round-7/kumitate.md` is
   122 B — protocol grades `ok` with a minimum-content defect
   (`PROTOCOL.md:210-213`), this gate raises `REPORT_THIN` + `REPORT_HEADINGS`.
4. **"Watchdog line 44 is blank"** (executor deviation note) — false; line 44 is
   `report_of() { [ -f "$SK/.ufo/reports/round-$2/$1.md" ]; }`. The claim never
   reached a document.
5. **A citation baseline measured outside the fleet is invalid.** `cite-check`
   in a `/tmp` clone at `d65aa24` reported `errors=13`; in place, `errors=2`.
   Cause: fleet-rung refs (`PROTOCOL.md`, `MISSION.md`, `AXES.md`, …) cannot
   resolve without the fleet parent. Valid method: move the new file aside and
   re-run in place.
6. **`SCORECARD.md` move-log rows exist only for rounds 8–9** (reviewer C2), so
   `SCORECARD_ROW_MISSING` for rounds 1–7 is a true finding, not a false
   positive — and the default audit is unaffected because it pins the latest
   closed round.

## L2 concurrency — 13 lanes, one batched dispatch

planner/connector `@m_lunamax` · executor/scribe/scout `@m_flash` ·
critic/reviewer/sentinel/labrat/mutation-tester/simplifier/distiller `@m_zfl`.
Landed: round-contract census (planner), prior-art verdict "fills a GAP, no
duplicate" (scout), the gate implementation (executor), the corpus note draft
(executor), the SKILL block with a grammar+pass proof (scribe), sibling-overlap
synthesis (connector), design attack R1–R7 (critic), 10-claim adjudication
(reviewer), blast-radius audit + origin-tree immutability proof (sentinel),
environment probes (labrat), mutation survivors (mutation-tester), YAGNI pass
(simplifier), findings normalization (distiller). L1 re-measured every claim
before it entered a document — items 1, 4 and 5 above are L2 claims caught or
repaired this way, and the critic's O1/O2/O3/O4/O6 repairs were forwarded to the
implementer mid-flight rather than discovered afterwards.

## Cross-domain (reported, never absorbed)

- **Origin tree** `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha` (read-only
  this round; sentinel proved no write: HEAD `ee907f1cf`, porcelain unchanged,
  all tracked-modified files mtime 2026-09-27): its
  `crates/ufo-core-runtime/bundled/omp-seat-routing.json` is red on the origin's
  own `sync-ufo-contracts.mjs --check` (ownerLane `nc8-runtime`, exit 1).
- **Main-repo protocol/driver surface** — not this lane's to edit:
  `scripts/shokunin-watchdog.sh:44` completion is existence-only, so a 0-byte
  file closes a lane-round; `kasegi-round-10.md` still quotes the pre-`c8f9f57`
  route map (`m_composer`/`m_antigravity`) that `PROTOCOL.md:266-269` requires to
  match the current `MISSION.md` bucket; no aggregator round-10 prompt exists.
- **Sibling reports missing the contract-required `SHONEN` heading** (measured
  in round-10 reports: `kagi`, `kake`, `kasegi`; present in `kotoba`,
  `protocol`) — the integrator's step-1 call; this lane records only its own.
- The main repo's unpushed-commit count is time-varying and not
  lane-attributable (`PROTOCOL.md:128-137`: 46 of 60 reports were swept into
  three commits by other identities) — why `--close` is a close-time act.

## Residuals / limits (recorded, not hidden)

- **Audit mode cannot see a round that filed no report** — it pins the latest
  *existing* report; `--round N` is the explicit path. The default is a
  regression tripwire, not a monitor.
- The 1024-byte and 2-heading thresholds are **this lane's** bar, not fleet law
  (planner census found no normative clause); only the citation checks and the
  `SHONEN` heading trace to written protocol. Warnings never gate without
  `--strict`.
- YAGNI residue, measured and deliberately not applied: `citations.
  mainProbeable`/`originProbeable` (4 L, writes with no internal readers — they
  are JSON output surface, kept as diagnostics), one unreachable `UNPUSHED
  ahead=?(raw=)` arm (2 L), one duplicate missing-SCORECARD path (1 L) — ~11 L
  total. Applying them re-pins the artifact, its docs and every recorded sha for
  no observable behaviour change; recorded for round 11 instead.
- `--close` cannot be green mid-round by construction, which is exactly why the
  close-only checks are documented and demonstrated but are **not** checklist
  items.

## SHONEN

- [x] SKILL.md contains real decision tables, error patterns, checklists, cited
      sources — decision table `SKILL.md:12`, 16 enforced anti-patterns
      `:448`, executable checklist `:514-540`, `round-gate` contract bullet
      `:564-581`.
- [x] At least one end-to-end domain task executed and logged in LOG.md —
      `round-gate.mjs` designed, implemented, fixed, verified (49/49 hermetic,
      live CLEAN/DRIFT/fail-closed arms) and logged: `LOG.md:263-314`.
- [x] Instructions executable by an agent without oral context —
      `node scripts/surface-probe.mjs --checklists` executes all six items
      (`CHECKLIST: 6/6 pass`, exit 0); the four gates' exit maps are in the
      files, not in prose.
- [x] No cross-domain bleed (PROVINCE.md still accurate) — the origin-drift,
      watchdog and sibling-report findings above are reported with owners, never
      edited in place; `PROVINCE.md` unchanged.

## Next planned move (round 11)

Operability 7 is still lowest and the axis's named gap is unchanged: the gates
run on demand, nothing schedules them. Round 11 either lands a real
scheduled/CI leg (preferred if a non-lane scheduler exists) or adds three more
genuinely executed checklist items — not a proxy re-charter, and the arithmetic
(`A+C ≥ 12`) is stated in `SCORECARD.md`. Coverage stays bookkeeping until a
family note lands for S6/S7/R10/R11 (S7, 68 members, is the largest).

## L0 side channel

No blocking question. Appended to `/home/vgpnk/projects/shokunin/.ufo/l0-questions.md`:
whether the fleet should adopt `round-gate.mjs` at the driver level (the
protocol lane has already asked the operator about the existence-only
`report_of()`); the lane-local tool needs no operator action to keep working.

**Report written by:** kumitate L1, round 10. **Cited lane commit:** `c91fe96`
(ancestor of lane `HEAD`).