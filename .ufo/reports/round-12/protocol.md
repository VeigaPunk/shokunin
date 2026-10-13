# protocol — round 12 report

Lane `protocol` (main repo `~/projects/shokunin`), axes **fleet-meta: protocol soundness + gate
integrity**, L1 model `@m_qwen` per the `MISSION.md` fleet table. L2 fleet routed per the `MISSION.md`
buckets — planner/connector `@m_lunamax`; executor/scribe/scout `@m_flash`; reviewer/critic/sentinel/
revenger/labrat/mutation-tester/simplifier/distiller `@m_zfl` — and the route map quoted in this
lane's own prompt (`.ufo/prompts/protocol-round-12.md`) matches those buckets exactly.

**Axis-move: gate-integrity 7 → 8** (the lower of the two axes at round open). Closure stopped being
prose: it is now a committed, read-only, mutation-tested gate whose frozen baselines pin this round's
measurement, and the pass it drove appended 14 `rounds[]` entries across three `closed_at` instants
(22 → 36) with zero carried debt. Protocol-soundness is **held at 8, not raised**: seven protocol
holes were closed against live evidence and the obligation census stayed 93/93, but `PROTOCOL.md`
grew 446 → 526 lines, which regresses the P4 length metric. Both sides are recorded below.

Measured at three pinned instants — `closed_at` **2026-09-28T20:55:00**, **21:20:00** and
**21:30:00 -03:00** — because this fleet terminates a lane-round every few minutes and a live count
is not a measurement. Commits: `7c56d1e` (pass 1 + four prompts), `dddb4ec` (§Gate standard + six
pins), `df1b2c6` (pass 2 + `supersedes.entry` + the L0 queue), `cab25dd` (pass 3 + wave artifacts +
five prompts), `d1e3903` (SCORECARD + LOG), `e275d4a` (critic-absorbed patches + four corrected
figures), `f520b03` (SCORECARD byte figure). This report is committed separately, pathspec-limited.

## Work performed

1. **The closure gate became executable.** `.ufo/waves/round-12/closure-check.py` — python3 stdlib
   only, read-only, deterministic — replaces the inline `python3 -c` blocks that rounds 10 and 11
   ran inside report prose. Round 11's hash checker lived in `/tmp/shokunin-r11/hexcheck.sh` and was
   never committed, so its mechanics survived only as prose in `verify2.md`; the revenger seat
   reconstructed them as a 15-item acceptance spec (`.ufo/waves/round-12/closure-semantics.md`) and
   this script is the recovery. Exit map `0 clean / 1 debt-or-contradiction / 2 could-not-evaluate /
   3 no pinned baseline`, printed in `--help`; flags `--json`, `--show-keying`, `--selftest`,
   `--frozen {pre,post-actual,post}`, `--no-citations`, `--no-ledger`.
2. **Three closure passes**, `rounds` 22 → 36 (`MANIFEST.json` `rounds[22..35]`), answering every
   carried `in-flight` row and every lane-round that terminated or was dispatched after the
   round-11 pass at 20:10:00.
3. **`PROTOCOL.md` §Gate standard landed** (36 lines) ruling the two round-10 L0 questions, plus
   seven pins closing holes this round observed live. Census preserved 93/93; body inline
   round-incident refs held at 4 (all seven new incidents went to the appendix as dated rows).
4. **Durability**: nine dispatch-evidence prompts committed and the L0 queue committed under the new
   integrator duty. No sibling report was swept (see §Orphaned reports).

## Closure record

Fourteen entries, all with `date 2026-09-28` and a `notes` digest quoting the timestamp+text of every
log line a status rests on (the log is mutable and its line numbers drift, so the digest is the
pointer that resolves).

| Entry | Round | Type | `closed_at` | Rows written |
|---|---|---|---|---|
| 22 | 7 | closure-correction (sup. #10) | 20:55:00 | aggregator `ok` |
| 23 | 8 | closure-correction (sup. #11) | 20:55:00 | aggregator `in-flight` |
| 24 | 11 | closure-correction (sup. #19) | 20:55:00 | protocol `ok`, kumitate `ok`, kengaku `in-flight` |
| 25 | 12 | closure-correction (sup. #20) | 20:55:00 | kotoba `ok`, protocol / kagi / kumitate `in-flight` |
| 26 | 13 | closure-correction (sup. #21) | 20:55:00 | kotoba `in-flight` |
| 27 | 14 | closure (first) | 20:55:00 | kasegi `ok`, kake `in-flight`, six `not-dispatched` + counters |
| 28 | 12 | closure-correction (sup. #25, first `supersedes.entry`) | 21:20:00 | kagi `ok` |
| 29 | 13 | closure-correction (sup. #26) | 21:20:00 | kagi `in-flight` |
| 30 | 8 | closure-correction (sup. #23) | 21:30:00 | aggregator `ok` |
| 31 | 9 | closure-correction (sup. #12) | 21:30:00 | aggregator `in-flight` |
| 32 | 11 | closure-correction (sup. #24) | 21:30:00 | kengaku `ok` |
| 33 | 12 | closure-correction (sup. #25) | 21:30:00 | kumitate `ok`, kengaku `in-flight` |
| 34 | 13 | closure-correction (sup. #26) | 21:30:00 | kotoba `ok`, kumitate `in-flight` |
| 35 | 14 | closure-correction (sup. #27) | 21:30:00 | kotoba `in-flight` |

**The four carried `in-flight` rows are all answered.** protocol r11 → `ok` (`complete` 20:28:20;
report committed `392b3c7` under `protocol-shokunin` at 20:27:31, i.e. before the complete line, so
lands-last holds; SHONEN present; every main-repo hash it cites resolves and is an ancestor).
kumitate r11 → `ok` (`complete` 20:50:56; report `46e9ec3`, SHONEN=1, cites `23452e7` which was its
repo's HEAD when written). kotoba r12 → `ok` with two defects (`complete` 20:28:22; report real and
14009 B with resolvable ancestors `4dd7753`/`abef8aa`/`d49dfa5`, but unlanded and carrying the
literal placeholder `LANE_HASH` at line 224 where `633859f` belongs). kengaku r11 → re-confirmed
`in-flight` at 20:55 (correct: the only file at a report path was then `kengaku-DRAFT.md`, a
non-conforming filename carrying unfilled `{{N}}` tokens, observed at 20:52), then resolved `ok` at
21:30 once `e0170cd` landed the real report.

**Ledger after the three passes** (`closure-check.py`, entry-keyed last-wins): **83 ok / 4 failed /
7 in-flight / 18 not-dispatched over 112 rows**; 104 rows adjudicated (75/4/7/18) and **16 rows named
`unadjudicable`** rather than silently scored — entries #1 and #3 are pre-fleet-2 fleet-keyed rows
(`{round: 9, lanes: {aggregator: in-flight}}` with no `lane_rounds`), which is exactly the trap that
manufactures a phantom `(aggregator, 9)`. All 7 remaining `in-flight` rows are live missions with
their launch pointers.

**Live gate at the instant of writing:** `closure-check: debt debt=1 contradictions=0
unrowed_terminated=0 pending_round=2` — the one debt row is kotoba r14, whose report landed *after*
the 21:30 `closed_at`. That is the mechanism working, not a failure: it is the round-13 pass's first
act, and it is named here so the next integrator does not have to rediscover it.

## The gate, measured

| Run | Command | Observed |
|---|---|---|
| self-test | `closure-check.py --selftest` | exit 0, `selftest: 15/15 passed` over 15 fixture cases (`ok`, `failed`, `marker`, `in-flight-live`, `in-flight-terminated`, `not-dispatched-without-lane_rounds`, `contradiction`, `unrowed`, `prompt-orphan`, `legacy-unadjudicable`, `keying-violation`, `bad-status`, `unknown-lane`, `ambiguous-supersedes`, `lanes-list-duplicate`) |
| frozen pre | `--frozen pre` | exit 1, `baseline: match`, `debt=5 unrowed_terminated=2 pending_round=7` — each row pinned to an independent source (`scout-closure.md` §Required appends, `reviewer.md` §Status recommendations) or explicitly marked checker-only |
| frozen post-actual | `--frozen post-actual` | exit 1, `baseline: match`, `debt=4` — the four rows the 21:20 pass owed and missed, each with evidence *inside* that instant |
| frozen post | `--frozen post` | exit 0, `baseline: match`, `debt=0` |
| live | `closure-check.py` | exit 0 / `debt=0` immediately after the 21:30 pass; exit 1 / `debt=1` once kotoba r14 filed |
| mutation | `.ufo/waves/round-12/mutation-gate.md`, `mutants/mutant-score.json` | **7/7 determinate** on base sha256 `9b89166c`: m2/m3/m5/m6/m7 killed by contradictions, m4 killed by the new `keying_violation` class, m1 not-applicable with the `unadjudicable` rows named. First run scored 4/5 with m4 surviving and m3 crashing on `KeyError`; both fixed and re-run |
| citations | `closure-check.py` §Report citations | 453 tokens over 77 reports / 105 lane-rounds / 9 repos at the 21:30 run (454 / 78 / 106 by 21:45): `commit=338 pin=24 runId-or-date=21 dead=86 orphan=5 non-commit=0 placeholder=1` |

The design point the critic forced: a fixture self-test alone is exactly the theater `PROTOCOL.md`
§Evidence standard forbids ("a status command printing configured values is not evidence of
capability"). So the gate ships **two** evidences — the hermetic fixture run *and* three
timestamp-coherent frozen snapshots (`pre`, `post-actual`, `post`) with committed expected verdicts,
under one stated truncation rule (`frozen/README.md`: log lines ≤ `closed_at`, reports and prompts by
add-commit ≤ `closed_at` else mtime, per-report `landed_at`, counters from the kept log). Any later
hand-edit of `rounds[]` breaks `--frozen post`; any silent narrowing of a pass breaks `--frozen pre`.

**The gate caught this lane.** At the 21:20 instant four lane-rounds already had termination or
landing evidence — aggregator r8 (`complete` 21:14:05, report `a5d6a7e` 21:13:01), kotoba r13
(`complete` 21:14:11, report `98735cc` 21:11:33), kumitate r12 (report `c41e197` 21:15:59) and
kengaku r11 (report `e0170cd` 21:18:11) — and the 21:20 pass wrote none of them. The checker named
all four with their launch pointers and suggested statuses; the 21:30 pass closed them as
`rounds[30][32][33][34]`. A prose closure record would have shipped the miss silently. That is the
measurement the score rests on.

## §Gate standard — the ruling

Answering `.ufo/l0-questions.md` rows **kengaku | round-10** ("promote the gate convention … to a
fleet-wide standard?") and **kumitate | round-10** ("should the fleet adopt `round-gate.mjs` at the
driver level?"), cited by lane+round because line numbers move as the queue grows.

**kengaku's question: yes in substance, no in shape.** A uniform `0/1/2` exit map would have broken
working gates on day one — kumitate's `round-gate.mjs` uses `0 clean · 1 findings · 2 fail-closed ·
64 usage`, so a mandated `2 = could-not-evaluate` misreads a substantive fail-closed as a setup
error, and kotoba's `3 = no-baseline` has no home in a three-code map. What landed instead is a
**three-valued verdict** (`clean | failed | could-not-evaluate`) with `0` and `1` pinned fleet-wide
and every other code declared in the gate's registry row and mapped onto one of the three; an
undeclared nonzero reads as `could-not-evaluate`. No gate breaks; comparability is gained; a gate's
own vocabulary (kagi's WARN-vs-HIT tiers, kotoba's no-baseline, kumitate's finding kinds) stays
lane-owned.

Four further rulings, each from evidence gathered this round:

- **Self-test is a capability, not a flag spelling.** The fleet spells it `--selftest` (kagi
  drift-pins, kengaku, kumitate), `--self-test` (kotoba) and `DRIFT_SELFTEST` (kagi transcript-scan);
  mandating the literal string would have branded kotoba nonconformant for a hyphen. What is required
  is a self-invocation over isolated fixtures asserting both the exit code and a stable expected
  finding-id, with expected values committed in the owning repo and independent of the
  recomputation. Kotoba's `--self-test` is *model-only* (`help="check the script's model only"`) and
  is the one named non-conformance — routed, not fixed here.
- **Pinned values point, never restate.** §Evidence standard's "Drift pins" bullet already says a pin
  counts only if expected values are persisted in-repo; §Gate standard cross-references it. One
  modality change is recorded: for gates the pin moves from "Recommended where the surface drifts
  outside lane control" to required.
- **A verdict names its revision.** kengaku's gate grades the tree it runs against: at 21:00 its
  worktree read `CHECKS n=280 mismatches=1 VERDICT: FAIL` while the same gate over its cited commit
  `06cdc98` read `n=149 mismatches=0 PASS` — and the worktree flipped to PASS at 21:15 when the lane
  landed its r11 evidence. Two readings of "the same" gate, three minutes apart, opposite verdicts.
  Closure therefore verifies a gate's *committed evidence*, never a fresh run against a moving tree.
- **A red gate is not a lane-round defect.** Measured at the round-12 reading: all five hermetic
  self-tests pass run as a non-owner from the main repo in ≈8.4 s (kagi drift-pins 13/13,
  transcript-scan `SELFTEST OK`, kotoba 10 assertions, kengaku 7/7, kumitate **57/57** — the `49/49`
  in the L0 question is stale, `23452e7` added `--tracked`), while three default-mode runs were red
  on host-coupled surfaces (kagi `TRANSCRIPT_SCAN: HITS=2` exit 1; kotoba `25/27` with `omp.db.rows`
  observed=18 expected=17, exit 1; kengaku's worktree, above). None is attributable to a closed
  lane-round. So: status-neutral, routed to the owner — and gate redness is never the marker
  predicate, since step 1 grades marker-versus-real-report first.

**kumitate's question: (a) + (b), not (c).** `round-gate.mjs` stays lane-local and reusable, and any
lane MAY run it in its own ritual (`--lane/--repo/--main-repo` parameterize it; 57/57 self-test).
Porting its findings into the driver is operator-side work, named exactly: `scripts/shokunin-watchdog.sh:44`,
`report_of() { [ -f "$SK/.ufo/reports/round-$2/$1.md" ]; }` — the file-existence completion signal.
The protocol lane does not patch `scripts/`. The defect is not rejected: it is already filed in this
lane's round-10 question and the marker clause supplies the retroactive consequence.

**Delivery is stated, not assumed.** The critic's sharpest attack: the driver template carries one of
the five child-lane contract items and nothing of §Gate standard, so a rule reached only by a lane
voluntarily re-reading `PROTOCOL.md` is aspiration. §Gate standard now says so in its own text —
delivery is the re-read duty, the integrator names the exact `lane_prompt()` addition in its report
(§Operator-side below), and **closure grades no gate conformant until its registry row exists in the
lane's own `SKILL.md`**. Registry schema is the protocol's; rows are the lanes'; the aggregator ledger
stays the routed-defect queue and never a second normative inventory.

**Rejection recorded.** The candidate file carries the strongest case against standardizing at all
(`exec-gate-standard.md` §Rejection alternative): 13–14 of 15 tracked verdict scripts already declare
`0/1`; the binding constraint is actuator debt, not convention; it extends protocol scope over
lane-owned tooling; and it costs 36 tracked lines. The counterweight that decided it: without a
written standard the integrator cannot tell a defect from a convention difference — kengaku's
self-test asserts check-ids and kotoba's asserts only its model, and that difference in *kind* is
invisible today. The critic's stronger recommendation (delete §Gate standard, keep a ≤20-line
registry rule) is **rejected**: the verdict-class mapping, the revision-naming requirement and the
closure-consequence ruling are the three parts that answer the filed questions, and none survives as
a registry rule alone. The length cost is paid openly and a compensating compaction is queued.

## Protocol amendments — seven pins, each from live evidence

| Pin | Hole it closes | Live evidence |
|---|---|---|
| Row identity | `lane_rounds` could be read as the row's key | naive keying gives 66/3/13/1 over 83 rows, erasing 3 of the 4 carried `in-flight` rows and manufacturing `(aggregator, 9)` from `rounds[3]`; entry-keyed reproduces the round-11 record exactly |
| Orphaned-report order + re-grade | no rule said who lands a report its mission left uncommitted, and a sweep could freeze a placeholder | aggregator r8 self-landed r7's report 19 min 26 s later (`6d27283`); kotoba r12's untracked report carries `LANE_HASH` where `633859f` belongs |
| Filed-report correction form | a lane correcting a filed report had no rule, so it invented one | kake r14 editing `.ufo/reports/round-13/kake.md` in place (+3/-1, self-labelled "r14 erratum") |
| `progressing-weak` | the actuator's "files modified under its repo" half attributed a sibling's work to the lane | kotoba r13 graded progressing on three `aggregator-shokunin` commits with no kotoba-authored commit; kumitate r13 now grades `progressing-weak` on operator-identity activity |
| L0 append-only + durability owner | the operator queue had no committer and no correction form | the kengaku-r10 and kumitate-r10 questions sat uncommitted for two rounds until a lane sweep carried them (`46e9ec3`, +4/-1 outside its own report path); kake r14 rewrote its own filed line in place |
| `in-flight` ends on a *landed* report | a draft at the contract path was indistinguishable from a filed report | kagi r12 wrote 13620 B to its path at 21:02 while live — untracked, SHONEN=0, citing only `aggregator-shokunin` commits — and the driver's existence signal will complete on it |
| `supersedes.entry` | two corrections sharing round+type+date cannot name a unique row | this round wrote a second round-12 and a second round-13 correction; the disambiguator is now pinned and validated |

Census after all amendments: **93/93 obligations found, 0 MISSING** (`sh .ufo/waves/round-11/verify-census.sh
PROTOCOL.md`, the round-11 verifier re-run unchanged). Body inline round-incident refs **4 → 4**;
appendix refs 10 → 18 across seven new dated rows.

## Length cost

`wc -l -c PROTOCOL.md`: **446 / 39718 → 526 / 49269** (+80 lines, +9551 bytes). P4's length
component regresses; its inline-incident component does not (body refs held at 4 — every new
incident went to the appendix as a dated row). The critic judged the move non-Pareto on
protocol-soundness and recommended deleting the 36-line section; that recommendation and its
rejection are both recorded above. Protocol-soundness is therefore **held at 8**, and round 13 owes a
compaction to ≤470 lines with the census at 93/93 *and* covering the seven new pins.

## Stale-lane listing

Every mission open longer than two driver ticks (900 s), age computed from the launch timestamp, with
the grade from the amended actuator (`closure-check.py` §Stale missions, live run 21:45):

| Lane | Round | Launched | Age (s) | Grade | Evidence |
|---|---|---|---|---|---|
| protocol | 12 | 20:28:21 | 4158 | progressing | lane commit `e275d4a` `protocol-shokunin` |
| aggregator | 9 | 21:14:10 | 1409 | progressing | lane file `kagi-shokunin/corpus/claim-ledger.sh` |
| kasegi | 15 | 20:50:55 | 2804 | progressing | lane file `corpus/knowledge/source-tree-loss-2026-09-28.md` |
| kengaku | 12 | 21:21:48 | 951 | progressing | lane file `corpus/evidence/round12-ladder/probe_plan_r12.md` |
| kake | 14 | 20:05:46 | 5513 | progressing | lane file `corpus/knowledge/ops-automation.md` |
| kumitate | 13 | 21:21:51 | 948 | **progressing-weak** | activity by the operator identity, not a lane identity; no lane-authored commit or file since launch |
| kagi | 13 | 21:06:34 | 1865 | progressing | lane file `corpus/claim-ledger.sh` |

Nothing graded silent, so nothing recorded `failed` under the actuator. kake r14 at 5513 s (92 min)
is the oldest live mission and is worth an operator look; recording `failed` is a ledger act and this
lane will not do it to a progressing mission.

## Orphaned reports — what this pass did *not* sweep

Three reports sat unlanded at various points this round: `.ufo/reports/round-12/kotoba.md`
(`LANE_HASH` placeholder), `.ufo/reports/round-12/kagi.md` (13620 B, SHONEN=0, citing only
aggregator commits) and `.ufo/reports/round-11/kengaku-DRAFT.md`. **None was swept.** Each has a
live successor mission that inherits it under the respawn-inheritance rule, and sweeping would have
frozen placeholders and drafts into permanent objects under protocol identity. This reverses
round 11's practice, which swept three terminated-mission reports for durability (`3ea42cb`); the
new order is successor-first, integrator-last, and it exists because the round-12 evidence showed
what a sweep would have committed. `.ufo/reports/round-11/kengaku-DRAFT.md` resolved itself: its
owner promoted it to `.ufo/reports/round-11/kengaku.md` at 21:17:49 after committing child work
`f09ff1f` under `kengaku-shokunin` identity at 21:15:23.

## Conformance defects recorded this round

Prompt fidelity: **19 of 19** child prompts in the band carry **1 of 5** contract items, and this
lane's own prompt (`.ufo/prompts/protocol-round-12.md`) names **none** of closure steps 1–4
(`grep -c MANIFEST` → 0) — the appendix's "No closure channel" prediction holds for a third round;
the duty reached this lane only through the file's re-read. Route maps in all band prompts match the
current `MISSION.md` buckets. SHONEN headings in the band: kumitate r11 ✓, kotoba r12 ✓, aggregator
r8 ✓, protocol r11 ✓; **absent** in kasegi r14, kagi r12, kotoba r13, kengaku r11 (main-repo lanes
are excluded from the child-lane count by the standing grep; the four named here are child lanes).

## Corrections to this round's own record

Appended, not rewritten — the entries carrying these numbers are committed.

1. **The 21:20 pass under-resolved four rows** (aggregator r8, kengaku r11, kumitate r12, kotoba
   r13). Entry #28's notes and this report's draft both assumed the pass was complete. The gate
   flagged all four; the 21:30 pass closed them. Self-defect, routed to this lane.
2. **"kengaku r11's report is untracked" — FALSE as of 21:18:11.** This lane wrote it at 21:15 and
   the scribe falsified it at 21:20 (`git ls-files --error-unmatch` succeeds; added by `e0170cd`,
   operator identity). The liveness half of the claim held (no `complete` line, counter 11).
3. **Four numeric errors in the new appendix rows**, all caught by the citation reviewer on
   re-execution and fixed in `e275d4a`: `46e9ec3`'s l0 numstat is +4/-1 not +5/-1; the aggregator r7
   landing gap is 19 min 26 s not 19 min 17 s; there are **15** tracked verdict scripts across **five**
   child lanes (kasegi carries none), not 14 across six; and kengaku's worktree FAIL is pinned to its
   21:00 reading because the tree flipped to PASS at 21:15.
4. **`SCORECARD.md` byte figure**: 49041 B was measured at `d1e3903`; the final is 49269 B at
   `e275d4a`. Corrected in `f520b03` with both instants cited so the row re-derives.
5. **Round 11's "kake r13 UNTRACKED → landed by this pass"** (`rounds[21]`) is superseded practice
   under the new orphan order. History is not rewritten; the row stands and the practice does not.
6. **A `supersedes` target was wrong in draft** — the round-9 correction first named entry #17, which
   carries no aggregator row; the aggregator round-9 row is in #12. Caught before commit.

## Routing — one line per defect, including this lane's own

- **kasegi** — r14 report: SHONEN heading absent (re-file the assessment under the heading next
  round), committed `50b2179` under the operator identity, dead pointer `4028846` at line 54.
- **kasegi** — its PROVINCE root `~/Projects/bounties` is **gone from the filesystem**; `PROVINCE.md`
  must be corrected to reality per the file contract, and ~376 `SKILL.md` path citations anchored on
  it need a disposition. Operator owns the filesystem; kasegi owns the documents.
- **kotoba** — r12 report unlanded with the literal `LANE_HASH` at line 224 where `633859f` belongs;
  r13 report SHONEN=0 and committed `98735cc` under the operator identity; dead blob `391a54f4` at
  line 81; `--self-test` is model-only; its no-baseline code is internally inconsistent (`--json`
  returns 0 where text returns 3).
- **kengaku** — r11 report SHONEN=0 and committed `e0170cd` under the operator identity; `grader.py`'s
  self-test uses bare asserts, so a broken fixture aborts the run as exit 2 instead of printing a
  FAIL row; its verdicts must name the revision they graded.
- **kumitate** — r11 and r12 reports plus four child commits (`46e9ec3`, `c41e197`, `64a27e7`,
  `e0e5de1`) under the operator identity although `kumitate-shokunin` is configured;
  `round-gate.mjs`'s header cites `PROTOCOL.md:263-267`, stale after the round-11 compaction; its L0
  question's `49/49` is stale (57/57).
- **kagi** — r12 report untracked at mission completion, SHONEN=0, citing only `aggregator-shokunin`
  commits while its own r12 work sat uncommitted; `transcript-scan.sh` has no in-gate pin (its
  expected values live only in an external claim ledger) and reads `HITS=2` in default mode.
- **kake** — the in-place edit of its filed round-13 report is a form defect under the new clause:
  append the erratum after the filed bytes in a new commit, or carry it in the r14 report.
- **aggregator** — advisory only: r7's report was uncommitted when its mission completed and r8
  landed it 19 min 26 s later. r8's own landing (`a5d6a7e`, lane identity, SHONEN=1) is clean.
- **protocol (self)** — the four missed rows, the falsified "untracked" claim, the four appendix
  figures, the SCORECARD byte figure, and three `supersedes` targets corrected pre-commit.
- **operator** — `report_of()` content-blindness; `lane_prompt()` 1 of 5 items and no gate text;
  `.ufo/state` (16 files) + `watchdog.log` still tracked; prompt durability is a treadmill (five new
  prompts appeared during this round alone, and a sixth after the last commit) — the driver should
  commit its own prompt at launch; `AXES.md` vs `MISSION.md` axis vocabulary (D-78) still open.

## Contested-scope rulings

- **Gate registry**: schema is the protocol's (§Gate standard); rows live in each lane's `SKILL.md`;
  the aggregator ledger stays the routed-defect queue, not a second inventory; a fleet index is
  pointers to lane rows, never copied expected values.
- **`round-gate.mjs`**: kumitate-owned and lane-local; the driver port is operator-side; protocol
  defines only what closure verifies.
- **`closure-check.py`**: protocol-owned, because it reads the integrator's ledger and nothing else;
  it never grades a lane's domain work and never writes.
- **kasegi `registry-check`**: the round-11 split stands — decree ledger to kasegi, routing and
  checker tooling to kumitate, shared route-role meaning to protocol.
- **kake's free-read verbs**: registry rows must label `gate|probe`; a verb whose universe is a
  snapshot is a probe, and `probe-delta.mjs` already self-declares "a report, not a gate".
- **The vanished `bounties` tree**: kasegi's province surface, the operator's filesystem. Protocol
  rules only that ledger rows citing it keep their statuses — evidence must resolve at *closure*
  time, not forever — and that the 86 dead pointers the citation sweep now counts are recorded as
  dead-because-the-tree-is-gone, not as fabricated.

## Cross-domain evidence (reported, not absorbed)

- **Local model serving / endpoint health** (the pending `kama` mint): kengaku's `grader.py` and
  kagi's transcript scan both read host surfaces (`~/.local/bin/omp`, `~/.opencode/`,
  `~/.omp/agent/skill-descriptions.db`, `~/.config/the-janitor`), and kotoba's gate went red on
  `omp.db.rows` 18 vs 17 — three lanes coupled to one unowned surface. Belongs to the `kama`
  decision the operator holds at L0 row `protocol | round-10`.
- **Host orchestration doctrine**: the shokunin gate standard deliberately points at the host
  runtime's stop semantics (`loop_stop`/`mission_goal`) instead of restating them, per the
  connector's absorb-vs-point finding. A local gate exit never defines a mission outcome and never
  stands in for the native judge.
- **Data loss on a read-only domain tree**: `~/Projects/bounties` disappearing mid-round is a fleet
  hazard beyond kasegi — any lane citing a domain tree can lose its evidence base. The push-scope
  rule kept every lane read-only there, which is why nothing was made worse.

## L0 side channel — five answers

1. **kengaku | round-10** (gate convention) → **landed**, modified: three-valued verdict rather than
   a uniform code map, self-test as capability rather than flag, pinned values by pointer, plus two
   requirements the question did not ask for and the evidence demanded — a frozen re-run for gates
   over mutable fleet artifacts, and a named revision per verdict. §Gate standard.
2. **kumitate | round-10** (driver-level adoption) → **ruled (a)+(b), not (c)**; the driver port is
   operator-side at `scripts/shokunin-watchdog.sh:44`. Its `49/49` figure is stale (57/57).
3. **kumitate | round-11** (machine-readable scorecard claim block) → **RECOMMENDED, not required**.
   The `SCORECARD.md` contract already demands a re-derivable counting command per score, and a
   machine-readable block is a stronger form of the same duty, so no `PROTOCOL.md` change is
   warranted; the `kumitate-proxy-v1` schema stays kumitate-owned. Fleet-wide integrator-recomputable
   scores would be an `AXES.md`/`MISSION.md`-level decision — operator-side — with the aggregator as
   the consuming lane. This round moved the same goal on the protocol side: the ledger is now
   recomputed mechanically rather than asserted.
4. **kasegi | round-15** (`bounties` gone) → **not this lane's to resolve**; operator and domain
   owner. Protocol ruling: correct `PROVINCE.md` to reality, keep the ledger rows as closed, and
   treat the 86 dead pointers as tree-loss, not fabrication. Recommend the operator handle it as a
   data-loss incident first and a protocol matter second.
5. **kotoba | round-13** (axis accounting) → **(1) ratified with a condition**: a lane may work an
   advisory or undefined-named axis as its lowest-axis move only if the row also names its mapping to
   one of `AXES.md`'s six axes, so a non-author can re-derive it; kotoba's `coverage 7 → 8.0` needs no
   mapping because `coverage` is one of the six. **(2) operator-side**: D-78 (`novelty`,
   `consistency` undefined in `AXES.md`) is an `AXES.md`/`MISSION.md` edit and neither file is a lane
   write; until it is reconciled, scores under undefined names must carry their six-axis mapping.
   Folding `consistency` under `calibration` is the operator's call, not a lane's and not this lane's.

No new L0 question is filed by this lane this round: the two operator-side actuators it would have
asked about are already filed (row `protocol | round-10`) and the exact required text is below.

## Operator-side — exact text required

`scripts/` is operator-side, so the correction is named here rather than landed. Two changes to
`lane_prompt()` and one to `report_of()`.

**(1) Insert into the `lane_prompt()` heredoc, after the `BINDING:` line** (the five contract items
plus the gate row; `$n` and `${lane}` are the function's own variables):

```
CONTRACT (quoted from PROTOCOL.md §Round-robin rounds and §Gate standard; the repo files win over this prompt):
1. Report path: write .ufo/reports/round-$n/${lane}.md in the main repo. Any other filename does not satisfy the contract and never fires the driver's completion signal.
2. Order: commit your child-repo round work FIRST, then write the report citing that commit's hash. A report naming a hash its repo does not contain fails verification; corrections are new commits, never amends.
3. SHONEN: the report carries a 'SHONEN' heading with one line per SHONEN.md box ([x] <named non-author verifier> / [~] with a resolvable pointer / [ ]). Without the heading the report does not satisfy the contract and is disqualified as promotion evidence.
4. Evidence: every number carries its counting command, every absence its search sweep, every quote its file+line. No /tmp or session-local pointers — they do not resolve at closure.
5. Write scope: inside ${LANE_CWD[$lane]} and your own report only. Never main-repo files (PROTOCOL.md, MANIFEST.json, SCORECARD.md, LOG.md, MISSION.md, AXES.md, scripts/, .ufo/state, .ufo/prompts), never another lane's repo or corpus files. Commit pathspec-limited with -c user.name=${lane}-shokunin -c user.email=${lane}@shokunin.local; never commit -a or add -A.
6. Gate registry: if your repo owns a verdict gate, its SKILL.md carries a row — name, gate|probe, entry command, verdict map (0 clean / 1 failed / any other code declared and mapped to clean|failed|could-not-evaluate), self-test command and spelling, pinned expected-value path, write scope, owner. A gate is read-only over surfaces it does not own and never acts on an external surface.
```

**(2) `report_of()`** — the completion signal is content-blind, so a 0-byte file closes a lane-round.
Recommended non-blocking form, which keeps the driver's liveness semantics and gives the integrator's
gate driver-side corroboration instead of risking a hung mission:

```sh
report_of() {  # existence completes; a marker is logged, not silently blessed
  local f="$SK/.ufo/reports/round-$2/$1.md"
  [ -f "$f" ] || return 1
  if [ "$(stat -c %s "$f")" -lt 200 ] || ! grep -qE '^#{1,6} *SHONEN' "$f" \
     || ! grep -qE '\b[0-9a-f]{7,40}\b' "$f"; then
    echo "$(date -Is) marker-suspect $1 round=$2 bytes=$(stat -c %s "$f")" >> "$SK/.ufo/watchdog.log"
  fi
  return 0
}
```

A blocking variant (`return 1` in place of `return 0`) enforces the contract at the driver but will
hold a mission open whose lane is still writing; the marker clause already supplies the retroactive
consequence, so the non-blocking form is the safer first step.

**(3)** Commit `.ufo/prompts/<lane>-round-<N>.md` at launch, inside `launch_lane()` after
`lane_prompt` succeeds. Nine prompts were committed by hand this round and a sixth appeared after
the last commit; a per-round integrator sweep cannot keep up with a 450 s tick across eight lanes.

## Dispatch digest — 14 L2 seats, two batched calls

Wave 1 (one `task` call, 10 seats): `ScoutClosure` (scout — the lane-round table, both keyings, the
required-append set; `scout-closure.md`), `ScoutGates` (scout — five sibling gates surveyed with all
five hermetic self-tests executed; `scout-gates.md`), `ExecChecker` (executor — `closure-check.py`,
fixtures, three frozen baselines, mutation harness; `exec-checker.md`), `ExecGateStd` (executor — the
§Gate standard candidate, placement, interactions, enforcement; `exec-gate-standard.md`),
`RevengerSem` (revenger — the 15-item semantics spec recovered from rounds 10–11;
`closure-semantics.md`), `CriticApproach` (critic — three must-fix blockers on the plan: keying and
truth precedence, frozen re-run against self-test theater, verdict classes rather than a code map;
`critic-approach.md`, persisted on request after first returning inline), `ConnectorOverlap`
(connector — overlaps, five contested-scope arbitrations, absorb-vs-point against host doctrine;
`connector-overlap.md`), `ReviewerStep1` (reviewer — closure step 1 over 12 reports and 19 prompts,
with three corrections to this lane's draft record; `reviewer.md`), `SentinelTrust` (sentinel — four
spoofable inputs ranked, the durability-commit race analysis, a clean credential screen;
`sentinel-trust.md`), `LabratLiveness` (labrat — H1 the liveness-probe clause **confirmed** 12/12, H2
no round-14 termination **confirmed**; `labrat.md`).

Wave 2 (one `task` call, 4 seats): `CriticCandidate` (critic — five must-fix items on the written
candidate, three absorbed, one misdirected at a round-11 entry, one rejected with reasons;
`critic-candidate.md`), `ReviewerCitations` (reviewer — 25/25 hashes exist with 27/27 ancestor checks,
15/15 log digests byte-exact, all six report byte counts exact, gate figures independently
reproduced, and four numeric defects found in this lane's own appendix rows;
`reviewer-citations.md`), `MutationGate` (mutation-tester — seven bounded mutants with exact-byte
restores, 4/5 determinate on the first run, m3's crash and m4's survivor routed to the owner;
`mutation-gate.md`, `mutants/`), `ScribeReport` (scribe — hashed inventory of 72 wave files across
six samples, the artifact-movement series for `closure-check.py`, and the conflict relay that
falsified this lane's "kengaku report untracked" claim; `scribe-inventory.md`).

Every seat wrote exactly one artifact under `.ufo/waves/round-12/`; none committed, none touched
`MANIFEST.json`, `PROTOCOL.md`, `SCORECARD.md`, `LOG.md`, `scripts/` or a sibling repo. The
mutation seat's licence to mutate `MANIFEST.json` was bounded, byte-restored, and verified
(`mutants/pristine.json`, sha256 recorded per mutant).

## SHONEN

The main repo carries no `SHONEN.md` (it is generated at mint inside a child repo), so this is the
four-box assessment against the protocol lane's own craft surface. All marks are `[~]`:
author-asserted, because a subagent this lane dispatched is still this lane under §Promotion gates
and no non-author verifier has marked them.

- `[~]` Real decision tables, error patterns, checklists, cited sources → `PROTOCOL.md` §Gate
  standard (verdict map, self-test requirements, registry schema, closure consequence), §Round-robin
  `rounds[]` status semantics, closure steps 1–4 as an executable checklist
  (`.ufo/waves/round-12/closure-check.py`), and the §Appendix digest of 32 dated error patterns,
  seven added this round with their measurements inline.
- `[~]` At least one end-to-end domain task executed and logged → `LOG.md` §Round 12: three closure
  passes against the live fleet (14 entries, `rounds` 22→36), the gate run to exit 0 with `debt=0`,
  mutation 7/7, census 93/93 — trigger, action, outcome, pointers.
- `[~]` Instructions executable by an agent without oral context → the closure procedure is now code:
  `python3 .ufo/waves/round-12/closure-check.py --selftest` and `--frozen pre|post-actual|post` run
  from a cold checkout with no context and reproduce this round's measurement; `frozen/README.md`
  states the snapshot rule.
- `[~]` No cross-domain bleed → nothing absorbed: the vanished `bounties` tree routed to kasegi and
  the operator, gate registry rows to the four owning lanes, the driver port to the operator, host
  runtime doctrine pointed at rather than restated, and §Contested-scope records six rulings.

## Push-scope compliance

Every commit this round went to the main repo `VeigaPunk/shokunin` under `protocol-shokunin`
identity. No domain source tree was written: `~/Projects/bounties` (now absent),
`~/Projects/origin-work/*` and `~/Projects/webzites` were read at most, and the sibling
`*-shokunin` repos were read-only surfaces for the gate survey and the citation sweep. No
operator-gated artifact was pushed ahead of a decision.

## Falsifiable next iteration (round 13)

**gate-integrity**: answer every row the live gate flags after `closed_at` 21:30 — kotoba r14 is
already owed — plus the eight live missions and the `pending_round` rows for rounds 15+; commit any
prompt generated after `cab25dd`; and get the four gate-owning lanes' `SKILL.md` registry rows
landed. *Falsified* if any `stale_in_flight` row survives the round-13 pass, or if the registry
schema exists with zero rows in it.

**protocol-soundness**: compact 526 → ≤470 lines with the census still 93/93 and body refs still 4,
covering the seven new pins. *Falsified* if a census predicate drops or the body ref count rises.

**gate**: re-run the mutation battery after any `closure-check.py` change and hold 7/7; add m1's
missing detector rather than leaving it not-applicable. *Falsified* if the score falls or m1 is
restated as not-applicable without a new check.
