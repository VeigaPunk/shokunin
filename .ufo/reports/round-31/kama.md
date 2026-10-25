# kama — round 31 report (attempt 3 of the steered round; attempts 1-2 died without a report)

Lane tip at report time: `c16fe3e5a1577c075668004d4b737a6b15061210` (jj-lane `landed` line, remote
verified, ahead=0). The watchdog logged six `lane-dead-no-report kama round=31` lines across
2026-10-23; this attempt inherits attempts 1-2's committed work, re-executes every frozen counter
at write time, runs the frontier step, prepares the round-32 wave, and lands the report attempts
1-2 never filed.

## Work performed

Declared claims (all frozen by attempts 1-2 of this round; no predicate amended this attempt):

1. **C1 — depth**: the `/v1/chat/completions` parameter layer on pinned llama-server b11755;
   frozen counter `.ufo/waves/round-31/count-c1.py` (sha256 `d86c4a94…9216`, frozen `0e6f8ed6`),
   predicate "Claim met iff counted >= 12."
2. **C2 — calibration**: revision-keyed evidence on every SCORECARD claim row; frozen counter
   `.ufo/waves/round-31/count-c2.py` (sha256 `2d06f38d…c6fe`, frozen `0e6f8ed6`), predicate
   "Claim met iff rows >= 28 and unresolved == 0 and false_corrections == 0 and append_only is
   True and every non-exempt claim row is either RESOLVED or has exactly one VALID correction row."
3. **C3 — operability** (frozen attempt 2): instrument-registry coverage via
   `tools/gate-registry-check.py`; predicate "registered 9, unregistered 0, exit 0."

Work items this attempt, each with an evidence pointer:

- Re-executed C1 at the tip on a fresh scratch clone: `/usr/bin/python3
  .ufo/waves/round-31/count-c1.py --lane . --repo /tmp/kama-r31-clone --tip
  f129e27b3b57a8fed7a34a8e6fe96d481e6c959d --out .ufo/waves/round-31/res/out/KamaR31a3.ResReRunC1/c1-tip.json`
  → `registered 18 counted 17 target 12 met True not-counted ['K31-10']`, exit 0; all 18 per-row
  live observations byte-identical to attempt 2's inherited receipt (same `diff` empty,
  `res/out/KamaR31a1b.ResReRunC1/c1-tip.json`). The counter starts its own pinned server
  (binary/impl/model sha256 checked).
- Re-executed C2 at the tip: `/usr/bin/python3 .ufo/waves/round-31/count-c2.py --repo
  /tmp/kama-r31-clone --tip f129e27b… --out .ufo/waves/round-31/res/out/KamaR31a3.ResReRunC2/c2-tip.json`
  → `rows 30 base_mismatched 13 exempt 1 valid_corrections 10 false_corrections 0 unresolved 3
  append_only True met False`, exit 0 — identical to the inherited `res/out/ResReRunC2/c2-tip.json`.
- Re-executed C3: `python3 tools/gate-registry-check.py --rev
  f129e27b3b57a8fed7a34a8e6fe96d481e6c959d` → `registered 9 unregistered 0`, exit 0.
- Committed the inherited-untracked re-run receipts (`res/`, left `??` by attempt 2's dying
  session) under this round's entry; lesson `corpus/lessons/round-31.md` §Attempt 3 mines the
  recurrence as mistake 9. The report-time untracked gate
  `test "$(git status --porcelain .ufo/waves/round-31 | grep -c '^??')" -eq 0` fails (exit 1) on
  the inherited tree and passes (exit 0) after the lane commit — shown live this attempt.
- Opened source **S192** (OpenAI Chat Completions API reference, `response_format`) and appended
  its registry row; census before 191 → after 192 rows, validate exit 0 both ends
  (`census-end-attempt3.out`). The row grounds the round-32 frontier item
  (`response_format`/`json_schema` → grammar transform).
- Prepared wave-3 (round-32 repair candidates): 32-seat spec validated under policy v1
  (`ufo-swarm-wave.mjs plan --emit-tasks` exit 0), written to `.ufo/waves/round-31/w3/spec.json`
  + `plan.json` + `taskCall.json`. **Not dispatched** — accepted host mapping: this L1 seat has no
  swarm-dispatch tool; the orchestrator dispatches prepared waves between rounds. Itemized as
  prepared-but-undispatched in this report per the host surface note.
- Misroot sweep at the fleet root: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows
  only driver runtime (`.ufo/state/*`, `.ufo/watchdog.log`) and other lanes'/operator files; no
  kama round-31 seat artifact misrooted — nothing to relocate.

## Landed changes

All in lane repo, committed and pushed via `scripts/hyaku/jj-lane.sh` — `landed
c16fe3e5a1577c075668004d4b737a6b15061210`:

- `SCORECARD.md` — §Round 31 attempt 3 (re-executed measurements, unchanged verdicts, frontier
  record, prepared wave) — LOG.md §Round 31 attempt 3 entry.
- `LOG.md` — §Round 31 attempt 3 (re-execution, receipts, S192, wave-3 prepared).
- `corpus/SOURCES.md` — S192 row added inside `## Registry` (191 → 192 rows).
- `corpus/lessons/round-31.md` — §Attempt 3: Gate (S192 URL, access date 2026-10-24, 22-word
  located quote) + Mistakes row 9.
- `.ufo/waves/round-31/res/` — attempt 2's inherited receipts + this attempt's re-run receipts.
- `.ufo/waves/round-31/census-end-attempt3.out` — end-of-round census receipt.
- `.ufo/waves/round-31/w3/` — prepared wave-3 spec/plan/taskCall.

Inherited, reused after re-verification: all of attempts 1-2's committed work (claims, counters,
receipts, wave-1/wave-2 evidence, corrections) — re-measured byte-stable above. Inherited,
discarded: none (the untracked `res/` receipts were committed, not discarded).

## Before → after measurements

- **C1** (depth, 7 → 7): command `/usr/bin/python3 .ufo/waves/round-31/count-c1.py --lane . --repo
  /tmp/kama-r31-clone --tip <commit> --out <receipt>`; base `07794a4d` exits 2 (no table) → this
  attempt's re-run at `f129e27b` (measured commit for the round's landed data) and the landed tip
  `c16fe3e5` both read `registered 18 counted 17 target 12 met True not-counted ['K31-10']`.
  Verdict: **met on the frozen counter; NOT admitted** — a twelve-duplicate-row no-op registry also
  meets it (`w2/out/CriticNoop/c1-noop.json` counts 12/12), so the counter cannot separate depth
  from a no-op; three pin mutants also survive (`w2/out/MutC1Pin/`).
- **C2** (calibration, 7 → 7): command `/usr/bin/python3 .ufo/waves/round-31/count-c2.py --repo
  /tmp/kama-r31-clone --tip <commit> --out <receipt>`; base `rows 28 … unresolved 13 met False` →
  re-run `rows 30 base_mismatched 13 exempt 1 valid_corrections 10 false_corrections 0 unresolved
  3 append_only True met False`. Verdict: **not met — counter defect**; rounds 11-13 share the
  Claim cell `C1`, the `(row, class)` key is non-injective, and the reference repair arm also fails
  (`w2/out/RefRepair/`, `w2/out/MutC2Key/`).
- **C3** (operability, 8 → 8): command `python3 tools/gate-registry-check.py --rev f129e27b…` →
  `registered 9 unregistered 0`, exit 0. Verdict: **met on the frozen predicate; NOT admitted** —
  the gate is an occurrence check; a row with an empty exit map and even a nonexistent metadata
  path also reads `registered 9 unregistered 0` (`w2/out/ExecC3Control/`, `w2/out/CriticC3Control/`).

No axis score moved; no capability row entered. All three claims report honest non-admission with
the counter defects routed to round 32 (repair candidates prepared as wave-3).

## Sources & frontier

Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kama` (run at the fleet root).
Before: exit 0, 191 rows (this attempt's round start). After: exit 0, 192 rows
(`.ufo/waves/round-31/census-end-attempt3.out`). Rows added by tier: A=+1 (S192, docs, OpenAI chat
`response_format` reference; scoped tier A — official docs authoritative for the OpenAI-side
declared semantics). Rows touched old→new: none (S180-S191 unchanged; zero status/recheck/used-by
changes). Frontier rows advanced: S192 opens the round-32 grammar-transform frontier; the six
round-30/31 rows S178/S179/S180-S191 remain mined. One sourced claim: C1's eighteen registry rows
rest on S180-S191 opened this round; the lesson Gate records S192's URL, access date and located
quote. Rejections this attempt: none.

## Trend verdicts

- **expansion — improved**: one new sourced registry row on uncovered frontier ground (S192) and
  the chat-adapter surface (18 measured rows, C1) committed this round; wave-3's two scout items
  extend the frontier map (`ScoutGrammarTransform`, `ScoutCompletionsSurface`). Evidence:
  `corpus/SOURCES.md` S192; `registry/chat-param-outcomes-r31.json`; `.ufo/waves/round-31/w3/spec.json`.
- **quality — improved**: six probe-falsified `meaning` cells corrected by appended SKILL block
  (attempt 2, KQ42 now in `corpus/QUALITY.md:309`); committed 404 snapshot body and duplicate
  snapshot files removed (`a9181096`); README/PROVINCE count drift corrected; this attempt's
  re-execution shows the round's measurements byte-stable across three sessions. No admitted entry
  failed re-check. Evidence: `corpus/lessons/round-31.md` §Mistakes 6-7; `SCORECARD.md` §Round 31
  attempt 2 corrections; `res/out/KamaR31a3.*` receipts.
- **discernment — improved**: all three shortcut controls were found by the waves before any
  admission (no-op registry 12/12; non-injective key; occurrence-only gate), and all three claims
  are reported not-admitted with the defects routed rather than prettified; mistake 9 records the
  second recurrence of uncommitted-receipt loss and its enforced fix. The round-30 verifier
  spot-check (`07794a4d`, non-author) admitted round 30; this round awaits its own outside
  closure. Evidence: `w2/out/CriticNoop`, `w2/out/MutC2Key`, `w2/out/ExecC3Control`;
  `corpus/lessons/round-31.md` §Attempt 3.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources →
  `SKILL.md` §§Decision table, Error signatures, Checklist + §Round-31 chat-completions parameter
  outcomes (18 rows, probe-corrected); author assertion, no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md → `LOG.md` §§round 16-18
  live lane-owned receipts (`.ufo/waves/round-16/live/receipt.json`, round-17 graded v2 receipts)
  plus this round's live pinned-server measurement of all 18 chat-adapter rows
  (`res/out/KamaR31a3.ResReRunC1/c1-tip.json`); author assertion.
- [~] Instructions executable by an agent without oral context → `SKILL.md` §Checklist and
  `corpus/knowledge/snapshot-history.md` §Run it; independent execution review remains open.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → `PROVINCE.md` §Write boundary and
  `corpus/knowledge/cross-lane-scope.md`; service repair, routing and credentials remain
  operator/sibling-owned; the wave-3 connector item re-scans sibling overlap.

## Round shape and seats

Two v1 waves inherited (attempts 1-2) + one prepared wave this attempt; together ≤128 seats.

- Wave 1 (attempt 1, build): 44 seats — data/executor 24, scribe 4, reviewer 3, scout 2, critic 2,
  connector 1, mutation-tester 1, sentinel 1 (+ control call, 12 arms, committed `3b1e84f8`).
  Dead seats: none recorded in `w1/out`.
- Wave 2 (attempt 2, falsify): 44 seats — reviewer 13, critic 10, mutation-tester 5, executor 5,
  scribe 4, connector 2, scout 2, sentinel 2, simplifier 1; attack roles 28/44 = 64%. Dead seats:
  none recorded; all 44 returned reports (`w2/out/`).
- Wave 3 (this attempt, prepared-but-undispatched per host mapping): 32 seats — mutation-tester 8,
  reviewer 8, critic 4, executor 3, scout 3, scribe 2, connector 1, sentinel 1, revenger 1,
  simplifier 1; attack roles 20/32 = 62.5%. Validator: `ufo-swarm-wave.mjs plan --emit-tasks`
  under `ufo-wave-policy.json`, exit 0. Planner seat: held by the L1 per orchestrator ruling
  2026-10-19 (the validator rejects `planner`; the bounded planning data-walk rode scout items).
- Residual calls: none. Round total: 88 seats dispatched-and-landed across attempts 1-2 + 32
  prepared this attempt; 0 dead seats observed across the round.

## Stale-lane, tooling, L0

- Stale-lane: respawn-per-round driver; no other mission of this lane is open. This mission
  progressed throughout (commits `f129e27b`, `c16fe3e5` within the round).
- Tool installs this attempt: none (no pacman, no new tools; the pinned fixture
  `~/.local/opt/llama-b11755` and `~/.cache/kama-shokunin/models/stories260K.gguf` were verified
  by sha256, not installed).
- Open L0 questions: none new this attempt. Routed defects (the two frozen-counter defects, the
  C3 occurrence check, KQ42 probe gating, pin verification) are lane-owned round-32 work, not
  operator questions.

## Honesty notes

- C1/C2/C3 verify on their frozen counters where applicable but are **not admitted**; the round's
  landed value is the falsification record, the byte-stable measurements, the frontier row, and
  the prepared repair wave — not claim admission.
- The inherited `res/` receipts are committed as attempt-2 artifacts (`KamaR31a1b`, `ResReRunC2`)
  and re-executed by this attempt's own runs (`KamaR31a3`); nothing in this report rests on an
  unrun check.
