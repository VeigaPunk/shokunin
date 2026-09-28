# kumitate — round 11 of ≤1024 (fleet-2)

**Lane:** kumitate-shokunin · **cwd** `/home/vgpnk/projects/shokunin/kumitate-shokunin`
**Axes:** operability + coverage (orchestration/tooling).
**Round move:** one axis-move, operability. **Score 7 → 8** on the frozen proxy.
**Repo commit:** `23452e7` (`round-11`), pushed to
`github.com/VeigaPunk/kumitate-shokunin`; final lane `HEAD` `59e6c0c` (two
close-evidence commits after it), tree clean,
`git rev-list --count @{u}..HEAD` → 0.

## Axis-move and measurement

Frozen proxy since round 8 (`SCORECARD.md`), formula unchanged; what changed is
that the terms are now **machine-checked**:

| Term | Before (r10 close) | After (r11) | Command |
|---|---|---|---|
| A — runnable artifacts with documented invocation + verdict exit | 3 | **4** | `find . -path ./.git -prune -o -type f \( -name '*.mjs' -o -name '*.js' -o -name '*.sh' -o -name '*.py' \) -print \| wc -l` → 4 (`cite-check`, `surface-probe`, `round-gate`, `proxy-check`) |
| C — `SKILL.md` GFM task items naming a runnable command | 6 | **9** | `grep -c '^\s*- \[' SKILL.md` → 9; all nine *executed*: `node scripts/surface-probe.mjs --checklists` → `CHECKLIST: 9/9 pass`, `VERDICT: PASS`, exit 0 |
| `f_O` ⇒ score | 9/12 ⇒ 7 | **13/16 = 0.8125 ⇒ 8** | `node scripts/proxy-check.mjs` → `PROXY: MATCH (A=4 C=9 operability=8; C1=14/18 C2=39/39 coverage=7; pins=4 match)`, exit 0 |

Round 10 fixed the arithmetic (`A+C ≥ 12` for 8) and offered two honest options.
**Option (a), a scheduled/CI leg, was refused on evidence**: the only schedulers
on this host are `systemd --user` timers owned by other identities
(`systemctl --user list-timers --all` → `ai-usage`, `webzites-probe`,
`charter-scribe`), and the sibling kake lane's recorded position is that a lane
does not toggle host state itself (`.ufo/l0-questions.md`, kake round-12). Option
(b) was taken with the property that makes it more than arithmetics: the same
tool now recomputes every term.

Coverage re-measured as bookkeeping (score stays 7): C2 **36/36 → 39/39** (this
lane's two new notes plus the third-party cold-run artifact the aggregator lane
committed into this repo mid-round), C1 **14/18** unchanged, file-level residue
**140/211 ≈ 0.663** re-measured unchanged.

## What landed

**`scripts/proxy-check.mjs`** — contract `kumitate-proxy-v1`, 1173 L, zero deps,
node ≥20, READ-ONLY, no network, no git, no subprocess on the measurement path,
sha256 `9d35ae74…`. It recomputes `A`, `C`, `C1`, `C1_total`, `C2`, `C2_total`,
both derived scores and four `scripts/*.mjs` sha256 pins from this repo's tree,
then compares them with the `<!-- kumitate-proxy-v1 -->` claim block in
`SCORECARD.md` (`SCORECARD.md:117-140`) and with that file's `## Axes` integers.
9 finding kinds, 10 fail-closed arms, exit 0/1/2/64, `--json`/`--strict`/
`--self`/`--scorecard`, `PROXY_SELFTEST: 55/55 pass` (hermetic, tmp fixtures
only).

Why this is the axis move and not padding: an L2 prior-art survey measured zero
`kumitate-proxy`/`proxy-check` hits fleet-wide and **zero machine-readable claim
blocks in any `.md` of any lane**, so the artifact fills unclaimed scope; and it
answers the aggregator's standing complaint that a lane's score cannot be
re-derived by a non-author — with the block present, any lane can run
`node <kumitate>/scripts/proxy-check.mjs --self <lane repo>`.

**`scripts/round-gate.mjs --tracked`** — the mid-round half of the close-time
tracking clause: enumerate `<reports-dir>/round-*/<lane>.md`, drop the highest
(in-flight) round, require every older report to be tracked in `--main-repo`
(`REPORT_UNTRACKED` per miss), fewer than two filed reports ⇒ fail-closed exit 2
`NO_FILED_REPORTS`, `--tracked --close` ⇒ usage 64 and no audit check runs. Live:
`ROUND_GATE: CLEAN (mode=tracked checked=8 errors=0 warnings=0)` exit 0. The same
file took a **−3 L simplifier pass** (unreachable `UNPUSHED ahead=?(raw=…)` arm,
duplicate missing-`SCORECARD.md` warning) ⇒ 1426 L, `ROUND_GATE_SELFTEST: 57/57
pass`.

Docs: `SKILL.md` (3 checklist items `:525-527`, a `--tracked` paragraph, a
Working-rules bullet `:604-627`), `corpus/knowledge/executable-scorecard.md`
(new), `corpus/knowledge/round-close-gate.md` (`--tracked` section + round-11
verdicts), `corpus/lessons/round-11.md` (new), `corpus/lessons/round-10.md`
(drift marker), `corpus/README.md` (3 rows), `SCORECARD.md` (claim block, axes
rows, 2 move-log rows, 4 limits, S7 row 68 → 69), `LOG.md`.

## Evidence (round close)

```
$ node scripts/proxy-check.mjs
PROXY: MATCH (A=4 C=9 operability=8; C1=14/18 C2=39/39 coverage=7; pins=4 match)   # exit 0
$ node scripts/proxy-check.mjs --selftest
PROXY_SELFTEST: 55/55 pass                    VERDICT: PASS         # exit 0, 2.3 s
$ node scripts/surface-probe.mjs --checklists
CHECKLIST: 9/9 pass                           VERDICT: PASS         # exit 0
$ node scripts/round-gate.mjs --tracked
ROUND_GATE: CLEAN (mode=tracked checked=8 errors=0 warnings=0)        # exit 0
$ node scripts/round-gate.mjs --selftest
ROUND_GATE_SELFTEST: 57/57 pass               VERDICT: PASS         # exit 0
$ node scripts/round-gate.mjs
ROUND_GATE: CLEAN (round=10 lane=kumitate checks=10 errors=0 warnings=0)  # exit 0
$ node scripts/surface-probe.mjs        → SURFACE_PROBE: CLEAN (surfaces=2 checks=12 errors=0 warnings=1)
$ node scripts/cite-check.mjs           → CITE_CHECK: DRIFT (files=41 tokens=2739 errors=14 warnings=72)
$ node scripts/round-gate.mjs --tracked --close            # exit 64
$ node scripts/round-gate.mjs --close
ROUND_GATE: CLEAN (round=11 lane=kumitate checks=13 errors=0 warnings=0)   # exit 0
                                  # close: clean tree, 0 unpushed, report tracked+pushed
$ node scripts/round-gate.mjs --tracked --lane other       # exit 2 NO_FILED_REPORTS
```

Drift arms were re-run on the **final** revision (a `/tmp` copy of the tree, so no
lane file was touched), each exiting as designed: baseline `MATCH` → `A=3`
`PROXY: DRIFT (A_DRIFT …)` exit 1 → `pin.round-gate=000…0`
`PROXY: DRIFT (PIN_DRIFT …)` exit 1 → stanza removed
`PROXY: FAIL-CLOSED (STANZA_MISSING)` exit 2 → `SKILL.md` removed
`PROXY: FAIL-CLOSED (SKILL_MISSING)` exit 2.

Citation gate: `errors=14`, **all** inside third-party aggregator artifacts
(`corpus/lessons/round-6-aggregator-audit.md` 2 × `LINE_OOR`;
`corpus/lessons/round-8-aggregator-box3-coldrun.md` 12, that file being extended
by its owner during the round). Zero lane-local errors — the count moved 7 → 14
inside one round, which is why the durable claim in `SKILL.md` is the lane-local
one.

## Claims falsified inside the round (calibration record)

1. **The registry parser silently mis-counted an escaped-pipe row — found by L1
   falsification, not by the suite.** Flipping the S7 registry row's 4th cell
   `no` → `yes` in a `/tmp` copy produced **no drift at all**: `registryCounts()`
   split rows on raw `|`, so the `\|` escapes inside that row's member column
   shifted every later cell and the "4th cell starts with `yes`" test landed on a
   prose fragment. Every escape-free row was fine, which is why 53 green selftest
   cases and a green live run had missed it. Fixed (`splitRowCells()` honours
   `\|`) with two regression fixtures (a `yes` row with an escape still counts; a
   `no` row does not), suite 53 → 55, artifact and `pin.proxy-check` re-pinned.
   The live term is unchanged by the fix (C1 14/18 under both parses): the defect
   was a latent mis-measurement, not a wrong score — and the round's own tool
   would *not* have caught it, which is exactly why the falsification pass exists.
2. **My first SCORECARD edit carried a wrong residue number.** The draft said
   "142/212 ≈ 0.670"; the documented method re-measures **140/211 ≈ 0.663**
   (unchanged from round 10). Caught by L1 re-measure before publication.
3. **The stale `## Axes` prose survived its own integer.** With the new file on
   disk the tree had A=4 while the row still said A=3; at C=6 the formula still
   yields 7, so no `AXES_DRIFT` fired — the row's *prose* was wrong while its
   *number* was right. Fixed by deriving both at close.
4. **`round-gate --tracked` counts 8, not 9.** The highest round is excluded by
   design and kumitate never filed a round-2 report (`ls .ufo/reports/*/kumitate.md`
   → rounds 1, 3–10).
5. **The S7 registry row was wrong by one member**: `find
   scripts/charter-scribe -type f | wc -l` → 6, not 5 ⇒ S7 is 69 members.
   Corrected with the command; the origin tree is the owner of the growth.
6. **"Uncited" is method-dependent**: the L2 census said 46 of S7 uncited "in any
   form"; strict `.mjs`-basename containment gives **55 of 69**. Both recorded;
   the Planned section quotes the strict method.
7. **An L2 lane wrote a scratch file into this repo.** `audit-env.sh` (the
   sentinel lane's env file) inflated the `A` term; `proxy-check` caught it as
   `A_DRIFT declared=4 computed=5` exit 1 rather than a silent +1, and the file
   was removed before close (`git status` is clean at HEAD). Recorded as both a
   hygiene finding and a term limit (the frozen `find` cannot tell scaffolding
   from an artifact).
8. **A third-party artifact quotes numbers that drift.** The aggregator's box-3
   cold-run file both cites this lane's checklist rows and grows during the
   round; its pins read as stale here and it is not this lane's to rewrite —
   reported, not absorbed (the round-6 precedent, unchanged).
9. **A bare sha of a superseded revision is a finding, not history.** Pinning
   round 10's `round-gate` sha in a corpus doc became `PIN_MISMATCH` the moment
   the file changed, so superseded revisions are now described, not pinned; only
   the current revision's sha appears in a `.md` (historical shas live in
   `LOG.md`).

## L2 concurrency — 14 lanes, one batched dispatch

planner/connector `@m_lunamax` · executor/scribe/scout `@m_flash` ·
critic/reviewer/sentinel/labrat/mutation-tester/simplifier/distiller `@m_zfl`.
Landed: acceptance matrix + re-pin inventory (planner), prior-art verdict "fills a
gap, no duplicate, no lane has a machine-readable claim block" (scout), the
artifact (executor), `--tracked` + suite arms (executor), checklist grammar proof
9/9 + corpus-note draft (scribe), cross-lane gate comparison and a conditional
reuse verdict (connector), a 10-objection design attack (critic), 24-claim
adjudication (reviewer), blast-radius + origin-immutability proof (sentinel),
3× timing/RSS/hermeticity probe (labrat), 12/12 mutation detection (mutation
tester), a keep/drop pass with two applied and one deferred deletion
(simplifier), findings normalization (distiller), and the S7 census for round 12
(coverage scout).

L1 re-measured every claim before it entered a document; five L2 claims were
corrected in that pass (items 1, 3, 4, 5, 6 above). Two L2 verifications were run
against **interim** revisions (the mutation table at the pre-fix build; the
sentinel/reviewer snapshots while the stanza was absent or drifting) and are
recorded as such rather than presented as final-bytes results. Reviewer also
caught a false line citation in a draft (`round-gate` USAGE) that never reached a
document. Sentinel proved the origin tree untouched (HEAD, porcelain, digests and
mtimes identical) and no HOME/`XDG` writes, no tmp fixture leftovers, no
Node-level network tripwire hits; strace was unavailable, so raw network-syscall
absence is recorded as **not fully disproved**.

## Cross-domain (reported, never absorbed)

- **Origin tree** (read-only this round): `crates/ufo-core-runtime/bundled/omp-seat-routing.json`
  is red on the origin's own `sync-ufo-contracts.mjs --check` (ownerLane
  `nc8-runtime`, exit 1); `scripts/charter-scribe/` grew 5 → 6 files (S7 row
  corrected here, owner: origin).
- **Third-party artifacts inside this repo**: `corpus/lessons/round-8-aggregator-box3-coldrun.md`
  (committed by the aggregator lane as `e79fefa`, extended during this round) now
  carries 12 of this repo's 14 citation errors and audits this lane's checklist
  live — owner: aggregator lane. `corpus/lessons/round-6-aggregator-audit.md`
  carries the other two.
- **Fleet/driver**: `scripts/shokunin-watchdog.sh:44` still completes a lane-round
  on file existence alone; the round-10 L0 questions about adopting `round-gate`
  at the driver level remain open.
- **Sibling lane**: kagi's `drift-pins.sh --selftest` now reports 13 cases where
  this lane's old calibration text quoted 11 — corrected here (owner: kagi).
- **Sibling reports**: round-10 `kagi`/`kake`/`kasegi` reports still lack the
  contract `SHONEN` heading (integrator's step-1 call; this lane records only its
  own).

## Residuals / limits (recorded, not hidden)

- `proxy-check` recomputes **claims**: it cannot show that a term measures what
  its name suggests, a prose definition edit that leaves counts unchanged is
  invisible to it (definition changes must be pre-registered), the frozen `C`
  regex admits `- [x]` lines that `--checklists` skips (unused this round:
  `CHECKLIST_SKIPPED: 0`), the frozen `A` cannot distinguish scaffolding from an
  artifact, and the file-level residue diagnostic is not covered. All four are in
  `SCORECARD.md` → Limits and `corpus/knowledge/executable-scorecard.md`.
- `round-gate --tracked` excludes the newest report, so a lane that files once
  and never again keeps a blind spot; it sees only *filed* reports.
- Operability's remaining gap is unchanged and out of this lane's reach: no
  schedule/CI leg it may own. Reaching 9 would need `A+C ≥ 15` — the arithmetic
  is stated in `SCORECARD.md`, and re-chartering the proxy is still rejected.
- Coverage stays bookkeeping (C2 39/39, C1 14/18); the four uncovered/partial
  families (S6, S7, R10, R11) are the only route to C1 > 0.778.

## SHONEN

- [x] SKILL.md contains real decision tables, error patterns, checklists, cited
      sources — decision table `SKILL.md:12`, 16 enforced anti-patterns `:448`,
      executable checklist `:514-527`, `round-gate`/`proxy-check` contract
      bullets `:567-627`.
- [x] At least one end-to-end domain task executed and logged in LOG.md —
      `proxy-check.mjs` designed, implemented, falsified, fixed and verified
      (55/55 hermetic, live MATCH, 5 drift/fail-closed arms) and
      `round-gate --tracked` added with 8 new suite arms; `LOG.md:315-363`.
- [x] Instructions executable by an agent without oral context —
      `node scripts/surface-probe.mjs --checklists` executes all nine items
      (`CHECKLIST: 9/9 pass`, exit 0); every gate's exit map is in the file, not
      in prose.
- [x] No cross-domain bleed (PROVINCE.md still accurate) — origin drift, the
      third-party artifacts' findings and the sibling-lane staleness above are
      reported with owners, never edited in place; `PROVINCE.md` unchanged.

## Next planned move (round 12)

**Coverage**, now the lowest axis (7): one internals-level family note out of the
S7 census, entered through the route-probe cluster the coverage scout ranked
first (`scripts/probe-ufo-route-health.mjs`, 1,364 L, 8 uncited companions,
3,132 L to read) — `14/18 → 15/18 = 0.8333 ⇒ coverage 8` at C2 = 39/39, no proxy
change. S7's census is done (69 members, 55 wholly uncited under the strict
method); `scripts/fake-omp.mjs` is a no-network fixture that could later carry a
hermetic checklist item for that surface, but no operability credit is claimed
for it until the note exists. The deferred `C`-definition hardening is
pre-registered in `SCORECARD.md` → Planned, not slipped in.

## L0 side channel

Appended to `/home/vgpnk/projects/shokunin/.ufo/l0-questions.md`: should the fleet
adopt the `kumitate-proxy-v1` claim block (one HTML comment + four pins in a
lane's `SCORECARD.md`) so the integrator can re-derive every lane's axis score
with `node <kumitate>/scripts/proxy-check.mjs --self <lane repo>` — the
aggregator's round-6 complaint about non-derivable lane scores, answered for one
lane by construction this round. No operator action is needed for this lane's
tools to keep working.

**Report written by:** kumitate L1, round 11. **Cited lane commits:** `23452e7`
(the `round-11` commit) and `59e6c0c` (final `HEAD`) — both ancestors of lane
`HEAD`, which is what `round-gate` re-checks.