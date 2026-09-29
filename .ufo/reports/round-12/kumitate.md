# kumitate — round 12 of ≤1024 (fleet-2)

**Lane:** kumitate-shokunin · **cwd** `/home/vgpnk/projects/shokunin/kumitate-shokunin`
**Axes:** operability + coverage (orchestration/tooling).
**Round move:** one axis-move, **coverage**. **Score 7 → 8** on the frozen proxy.
**Repo commit:** `64a27e7` (`round-12`), pushed to
`github.com/VeigaPunk/kumitate-shokunin`; final lane `HEAD` `e0e5de1` (one
close-evidence commit after it), tree clean,
`git rev-list --count @{u}..HEAD` → 0.

## Axis-move and measurement

Frozen proxy, formula unchanged since round 8 (`SCORECARD.md` → `### coverage`).
What changed this round is the *stated* standard behind C1: a family counts only
when a note names **every** member at internals level (line anchor or named
symbol describing that member's own behavior; usage lists, `Sources:` footers,
`README.md` map/hole rows and `SKILL.md` do not count).

| Term | Before (r11 close) | After (r12) | Command |
|---|---|---|---|
| C1 | 14/18 (S6 `partial`, R10 `no`) | **16/18** (S6 5/5, R10 2/2) | `node scripts/proxy-check.mjs` → `C1=14/18` → `C1=16/18` |
| C2 | 39/39 | **43/43** (3 knowledge notes + `lessons/round-12.md`) | `grep -c '^\| `\(knowledge\|lessons\)/' corpus/README.md` → 43; `find corpus/knowledge corpus/lessons -name '*.md' \| wc -l` → 43 |
| coverage ⇒ score | `floor(10 × 0.778 × 1.0)` = 7 | `floor(10 × 0.888 × 1.0)` = **8** | `node scripts/proxy-check.mjs` → `PROXY: MATCH (A=4 C=9 operability=8; C1=16/18 C2=43/43 coverage=8; pins=4 match)`, exit 0 |

A and C are untouched (`find … \| wc -l` → 4; `grep -c '^\s*- \[' SKILL.md` → 9),
so operability stays 8. File-level residue (diagnostic, not scored) rose
**140 → 150 of 211** with the three new notes.

## Deviation from the pre-registered round-12 plan (recorded, not smoothed)

Round 11's `## Planned` said: "one internals-level family note out of the S7
census, landed from the route-probe cluster" (`14/18 → 15/18 ⇒ 8 at C2 38/38`).
That route was **not taken as written**, on evidence measured this round:

1. The registry's own standard already denied S6 at `2 of 5 named` (40%). A
   9-of-69 cluster note (13%) flipping S7 while S6 sat denied would invert the
   standard — so S7 keeps `no` and the cluster note lands as **C2-only residue
   progress**.
2. The forecast's arithmetic was stale twice: round 11 had already closed at
   C2 39/39 (not 38/38), and **15/18 and 16/18 both score 8** — the next
   threshold is **17/18 ⇒ 9** (verified: C1 17 with the `## Axes` row left at 8
   produces `PROXY: DRIFT (AXES_DRIFT term=coverage declared=8 computed=9)`,
   exit 1).

So the round completed the two *fully enumerable* families (S6 5 members, R10 2
members) and left S7 to a pre-registered partition decision in round 13.

## What landed

- **`corpus/knowledge/ops-watchers.md`** (S6, 5 of 5 members): `ufo-l0-watch.mjs`
  (1679 L) tick geometry + 14-row hole ladder + seal lifecycle + whip ladder;
  `ufo-stale-watchdog.mjs` (1010 L) `POLL_MS`/`STALE_MS`, the nudge → `remove` +
  `fleet-dispatcher repend` ladder, the single-writer rule, `isSafeRunId`
  prototype-key hygiene; `ufo-l0-monitor.mjs` (1638 L) the
  `--rebind --repair --repend --settle` family with its mutate/refuse table, the
  sanctioned second queue write path, settle-receipt binding; `the-tick-ping.mjs`
  (831 L) completion wakeup, interval/deadline bounds, 11 exit codes;
  `ufo-ground-handler.mjs` (859 L) the four-op unix socket, all 7
  `PATH_PING_ERROR_CODES`, the 1 s `FRESHNESS_CLOCK_SKEW_MS` bound, and the one
  model-touch path. Each member has its own `## ` section and a member probe.
- **`corpus/knowledge/gate-verdict.md`** (R10, 2 of 2): `gate.rs` type surface
  with anchors, the `verdict` priority ladder, the five refusal literals with
  their `echo_bounded` binds, `validate_vector`'s empty-declaration delegation
  and per-entry-before-omitted precedence (`jw-34-malformed-precedence`), the
  512-char echo ceiling, 11 consumer sites, and a `gate_tests.rs` census
  (19 `#[test]`, literal-needle style, 0 unix arms, six named gaps).
- **`corpus/knowledge/route-probe-cluster.md`** (S7 residue, 9 of 69 members):
  probe internals, outcome/refusal vocabulary, exit map, the redaction table +
  emit gate, token-plan catalog/subprocess wiring, bounds, downstream consumers,
  and an explicit `## Scope — this note does NOT cover S7`.
- `corpus/lessons/round-12.md`; 4 `corpus/README.md` rows (39 → 43) plus
  re-measured gap prose; `SCORECARD.md` registry cells (S6/R10 → `yes`), claim
  block (C1 14 → 16, C2 39 → 43), `## Axes` row 7 → 8, 2 move-log rows, the
  stated family standard, 3 new limits, the round-13 plan; 2 `SKILL.md` fixes.

## Evidence (round close, lane `HEAD` `64a27e7`)

```
$ node scripts/proxy-check.mjs
PROXY: MATCH (A=4 C=9 operability=8; C1=16/18 C2=43/43 coverage=8; pins=4 match)   # exit 0
$ node scripts/proxy-check.mjs --selftest
PROXY_SELFTEST: 55/55 pass   (10 fail-closed arms observed)   VERDICT: PASS        # exit 0
$ node scripts/surface-probe.mjs --checklists
CHECKLIST_SKIPPED: 0
CHECKLIST: 9/9 pass                            VERDICT: PASS                      # exit 0
$ node scripts/round-gate.mjs
ROUND_GATE: CLEAN (round=11 lane=kumitate checks=10 errors=0 warnings=0)           # exit 0
$ node scripts/cite-check.mjs
CITE_CHECK: DRIFT (files=45 tokens=3769 errors=14 warnings=75)                     # exit 1
$ grep -c '^\s*- \[' SKILL.md            → 9      (unchanged; A = 4 unchanged)
```

Member probes (printed inside each note with their output):

```
ops-watchers.md   ufo-stale-watchdog heading=1 cites=37 names=2
                  ufo-l0-monitor     heading=1 cites=55 names=3
                  ufo-l0-watch       heading=1 cites=35 names=4
                  the-tick-ping      heading=1 cites=41 names=2
                  ufo-ground-handler heading=1 cites=58 names=4
gate-verdict.md   gate.rs            heading=1 cites=92 names=4
                  gate_tests.rs      heading=1 cites=21 names=5
```

Citation gate: `errors=14`, **all** inside the third-party aggregator artifacts
(`corpus/lessons/round-6-aggregator-audit.md` 2 × `LINE_OOR`;
`corpus/lessons/round-8-aggregator-box3-coldrun.md` 12). **Zero lane-local
errors** — four introduced by this round's own notes were found by the gate and
fixed before landing (two runtime-artifact names without an owning path token,
two `package.json:NN` tokens that suffix-resolved to `substrates/cursor/package.json`).
`cite-check --symbols` reports no symbol finding in the three new notes (one
`SYMBOL_OFF_LINE` in `gate-verdict.md` was fixed by citing `validate_score_vector`'s
definition at `native_scores.rs:334`).

Mutation pass (on a `/tmp` copy; the real tree untouched): 7/7 arms fire — a
dishonest registry `yes` flip → `C1_DRIFT` + `AXES_DRIFT`, axes integer →
`AXES_DRIFT`, stanza C2 → `C2_DRIFT`, `- [ ]` line → `C_DRIFT`, stray script →
`A_DRIFT` + `PIN_UNPINNED`, stanza deleted → `FAIL-CLOSED` exit 2; baseline
`MATCH` re-proved after each restore.

## Claims falsified inside the round (calibration record)

1. **S6's attribution was wrong, not just its count.** Line-by-line
   adjudication: `ufo-l0-watch.mjs` ✓ (`sighting-wall.md:142`),
   `ufo-l0-monitor.mjs` ✓ (`round-6.md:25-27` with `:226-232` anchors),
   `ufo-stale-watchdog.mjs` ✗ (usage list at `singleton-and-queue-ownership.md:6`
   + `Sources:` footer at `:33-34`), `the-tick-ping.mjs`/`ufo-ground-handler.mjs` ✗
   (`README.md:71-72` hole sentence). Number 2 survived; members changed. A
   scout's looser "3 of 5" reading was rejected in favour of the stated standard
   — both readings are recorded in `SCORECARD.md` → Limits.
2. **Round 11's `## Planned` forecast was stale:** C2 was already 39/39, and one
   note was already enough for 8.
3. **`## Axes` "four uncovered/partial families (S6, S7, R10, R11)"** was stale
   on arrival; the set is now two (S7, R11).
4. **`SKILL.md:388` carried a wrong constant** — ">5 s future-skew refused". The
   origin constant is `FRESHNESS_CLOCK_SKEW_MS = 1_000`
   (`ufo-ground-handler.mjs:38`, compared `:319`), and `docs/THE-TICK.md:89`
   says "the 1,000 ms clock-skew allowance". Found by an executor, verified by
   L1, corrected in `SKILL.md` (a freshness fix landed inside a coverage round,
   reported as such).
5. **The route-probe cluster's size was a membership-boundary artifact**, not a
   phantom: 9 files / 3,132 L (`probe-*.mjs` ×7 + `atomic-write.mjs` +
   `fake-omp.mjs`) vs 7 / 2,651 L under the `probe-*` glob; round 11's "8 uncited
   companions / 3,132 L" matches the 9-member reading (8 = members − hub).
6. **`corpus/README.md`'s script-layer gap was stale**: 48 → 39 of 72 top-level
   `.mjs` uncited (re-measured with the per-basename shell loop stated in the
   file), and the "no dedicated note" line for `the-tick-ping.mjs` /
   `ufo-ground-handler.mjs` was corrected.

## Cross-domain (reported, never absorbed)

- **Origin tree** (read-only this round): HEAD moved `ee907f1cf` → `daa371583`,
  with 37 dirty paths at the round's start and 39 by the sentinel's T1 check —
  the origin's own lane is actively writing; **none** of this round's target
  files were among them (verified by L1 before the round, re-checked by the
  sentinel after). The origin's own
  `conformance/vectors/native/judge-wave.json:1368` still describes
  `validate_vector`'s undeclared-before-omitted order as "the reverse" of the
  reordered code (`23e476e21`, 2026-09-24) — its `expect` block is correct; the
  description text is stale. Owner: origin runtime lane.
- **Sibling lanes**: the connector found **zero** exact-name hits for this
  round's 9 surfaces across kasegi/kake/kagi/kengaku/kotoba `corpus/**` +
  `SKILL.md`, and no sibling uses family-member enumeration — kasegi's
  class-granularity proxy is a different measure, so the coverage convention
  stays lane-local. Adjacent scope to not absorb: kake's site-probe history,
  kagi's Janitor config/credentials, kengaku's model identity/capability
  interpretation, kotoba's prompt craft.
- **Substrate**: one `@m_flash` lane (`ExecGateNote`) died mid-round on a
  provider quota error ("weekly usage quota has been exhausted") **after**
  writing its artifact; the draft was recovered from scratch and adjudicated like
  any other — recorded so a substrate failure is not mistaken for work that never
  happened.

## L2 concurrency — 16 lanes, one batched dispatch

planner/connector `@m_lunamax` · executor/scribe/scout `@m_flash` ·
critic/reviewer/sentinel/labrat/mutation-tester `@m_zfl`. Landed: acceptance
matrix with exact before/after edit strings (planner), three source censuses —
S6 (5 files, 137 ledger rows), R10 (444 lines, 86 rows + 9 missing fact-classes),
S7 (measured member set) — five note drafts, the README/lesson/`SKILL` drafts
(scribe), a cross-lane overlap verdict (connector), a 5-objection attack with
commands (critic), 398-row citation adjudication, 1.01% non-OK (reviewer),
blast-radius proof (sentinel), `node --check` 11/11 + help-only probes + two
empirical claim cross-checks (labrat), and 7/7 proxy mutations
(mutation-tester). L1 re-measured every claim before it entered a document — six
corrections above — and landed every edit.

Critic's strongest objection (recorded, not hidden): `proxy-check.mjs` cannot see
a note, so the cheapest fake (flip two cells + update the stanza and the axes
integer) passes all arithmetic checks. The round's answer is the **per-note
member probe** (one `## ` heading per member plus line-anchored citations inside
that member's own section, printed with its output in each note) — a check a
non-author can re-run, not a gate. Turning it into a gate is deliberately *not*
slipped into this round; it is named as a future operability move.

## Residuals / limits (recorded, not hidden)

- `proxy-check` recomputes claims, not justification: the semantic gap above,
  the invisible-to-the-tool definition edit (definition changes must be
  pre-registered), the frozen `C` regex admitting `- [x]` lines that
  `--checklists` skips (unused: `CHECKLIST_SKIPPED: 0`), and `A` counting files
  rather than provenance — all in `SCORECARD.md` → Limits.
- **S7 (69 members, 9 named) and R11 (42 runtime `.rs` + 5 CLI `.rs`, 0 named)
  remain uncovered.** A partition into `S7a`/`S7b` is a *registry* change
  (C1_total 18 → 19) and is pre-registered for round 13, not slipped in.
- The 15:18 ⇒ 9 threshold arithmetic is stated in `SCORECARD.md` → Planned:
  reaching 9 needs 17 of 18 covered or a stated partition.
- Operability's gap is unchanged and out of this lane's reach (no CI/schedule leg
  it may own; the host's schedulers belong to other identities) — round 11's
  finding, still true.

## SHONEN

- [x] SKILL.md contains real decision tables, error patterns, checklists, cited
      sources — decision table `SKILL.md:12`, 16 enforced anti-patterns `:448`,
      executable checklist `:514-537`, the watcher paragraph + three round-12
      pointer bullets `:375-404`, `round-gate`/`proxy-check` contract bullets
      `:567-627`.
- [x] At least one end-to-end domain task executed and logged in LOG.md — three
      internals-level family notes built from source censuses, cross-verified by
      a reviewer (398 rows) and an empirical labrat pass, landed with their own
      member probes; `LOG.md:367-441`.
- [x] Instructions executable by an agent without oral context —
      `node scripts/surface-probe.mjs --checklists` executes all nine items
      (`CHECKLIST: 9/9 pass`, exit 0); each new note carries the command that
      reproduces its member-completeness claim.
- [x] No cross-domain bleed (PROVINCE.md still accurate) — origin drift, the
      stale vector description and the sibling-lane boundary are reported with
      owners, never edited in place; `PROVINCE.md` unchanged.

## Next planned move (round 13)

**Coverage, 8: pre-register the S7 partition, then work it.** Either partition S7
into `S7a` (route-probe cluster + shared helpers) / `S7b` (60-member remainder) —
C1 17/19 = 0.894 ⇒ still 8, gain is an honest boundary plus a smaller remainder —
or name the remainder at census level (the round-11 census is done: 69 = 59 + 6 +
4). R11 is the other candidate. Both need the partition/definition stated in the
round that measures it. The `C`-regex hardening and the `--claims` gate remain
pre-registered, not slipped in.

## L0 side channel

No new operator decision is required for this lane; round-10's question (adopt
`round-gate.mjs` at the driver level) and round-11's (adopt the
`kumitate-proxy-v1` claim block fleet-wide) remain open in
`/home/vgpnk/projects/shokunin/.ufo/l0-questions.md` and are not re-filed.

**Report written by:** kumitate L1, round 12. **Cited lane commits:** `64a27e7`
(the `round-12` commit) and `e0e5de1` (close evidence) — both ancestors of lane
`HEAD`, which is what `round-gate` re-checks.