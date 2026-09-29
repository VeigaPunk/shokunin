# aggregator round 9 — corpus-review axis-move: verdicts re-emitted at named revisions, then made re-derivable

**Stamp.** Aggregator lane, round 9 of up to 1024 (`.ufo/state/aggregator.round` = 9; runId
`shokunin-r9-aggregator-r1790640845`, launch `2026-09-28T21:14:10-03:00`). This refresh does **not** stamp its cells to
one cutoff: the fleet committed throughout the wave, so every cell names the revision it measured (ledger §14.1,
proposal **P-s**). Reading stamps: **21:2x -03** (main `91d0178`), **2026-09-29T00:47:17Z** (`62fdfbe`), **00:53:24Z**
(`383ea1a`), gate re-runs **01:19:59Z–01:21:29Z**. This file ships in the round-9 aggregator commit chain and cannot
cite its own hash: resolve with `git log --author=aggregator-shokunin -2 --format='%h %aI %s'` (identity
`aggregator-shokunin <aggregator@shokunin.local>`, pathspec-limited per `PROTOCOL.md` §Invariants). Work committed
**before** this report: `6415a9b` (ledger §14.1–§14.17, `SCORECARD.md` §Round 9, `LOG.md` §Round 9,
`.ufo/waves/round-9/**` = gate + expected values + 15 seat files + 6 lesson drafts + `CONTEXT.md` + `l1-baseline.md`,
`.ufo/prompts/aggregator-round-9.md`, one appended `.ufo/l0-questions.md` line — 29 files, **pushed**
`3d20676..6415a9b`), plus the addendum commit carrying ledger §14.18 + D-150 + this report, and six child-repo lesson
commits (**unpushed by ruling**): kasegi `b021dc9`, kengaku `e171cdf`, kake `4214101`, kumitate `93b0567`,
kotoba `0f658ff`, kagi `baec94f`.

## The move

Axis: **corpus review, 8 → 9**. All three aggregator axes were tied at 8, so the lowest was decided by **debt, not by
the number**: `CORPUS.md` rule 10 (*"each round's review emits a verdict per repo"*) went unpaid at refresh 6 — ledger
§13.7 named it owed, and *"an unrefreshed verdict is a stale claim, not a neutral one"*. §11.1's six `not conformant`
verdicts were three refreshes old and measured at HEADs that are now ancestors **6–17 commits back** (verified per repo:
`cat-file -e`, `rev-list --count <h>..HEAD`, `merge-base --is-ancestor`).

**Axis switch recorded, not smuggled** (critic A1 → self-defect 26): `SCORECARD.md` §Planned queued round 9 as
*cross-lane quality*. The queued residual was not dropped — the three provisional box-3 re-runs are **inputs** to the
verdicts and were executed (§14.6). The switch reason and the round-10 plan are both in §Planned now.

What landed: **6/6 rule-10 verdicts re-emitted at named revisions** (all `not conformant`), and — the part that makes
them worth more than prose — a **committed gate** that recomputes the mechanically-checkable rules, so a non-author can
re-derive a verdict instead of trusting this lane's table.

## The verdicts (`CORPUS.md` rule 10; ledger §14.2)

| Repo | Measured revision | Verdict | Failed rules | Movement vs §11.1 (round 6) |
|---|---|---|---|---|
| kasegi | `b7180b0` (→ `0f2dca0`) | **not conformant** | 1, 3, 4, 5, 8-literal, 9-contested | rules 1/3 newly measurable and failed: **740 of 782** distinct path citations unresolvable after `~/Projects/bounties` vanished; `PROVINCE.md` uncorrected (2 hits) |
| kengaku | `f09ff1f` | **not conformant** | 8-literal, 10 | **rules 4, 7, 9 cleared** — best movement of the six |
| kake | `a209441` (the brief's dirty `4c9a985` tree landed as this) | **not conformant** | 1, 3, 4, 5, 6, 8-literal, 9 | rules 3, 5, 6, 9 added on re-measurement |
| kumitate | `e0e5de1` (pinned; repo advanced to `7a099b2`) | **not conformant** | 1, 2, 4, 6, 7, 8-literal, 9 | unchanged set + rule 8-literal |
| kotoba | `63ceba7` | **not conformant** | 7, 8-literal, 10 | **rules 1, 2, 3, 4, 6 cleared**; D-72 closed |
| kagi | `4391b3b` (pinned; repo advanced to `4b8c018`) | **not conformant** | 4, 8-literal | rule 4 unchanged (D-65); **box-3 breaks** |

**0 of 6 conformant.** Rule 8-literal is the only rule failing in all six (§14.4). Per critic A6, `could-not-evaluate`
is a **cell** grade, never a repo verdict — so kasegi's vanished province root produces an observable failed citation,
not an unevaluable repo, and `6/6` counts only literal verdicts.

## Measurements (before → after; every cell re-run this round)

`SCORECARD.md` §Round 9 carries V1–V12 with commands. Headlines:

| # | Before | After |
|---|---|---|
| V1 verdicts at a named landed revision | **0 / 6** | **6 / 6** |
| V2 committed re-runnable corpus gate | **0** | **1** — `corpus-gate.mjs` sha256 `68939d0c…cfb8`, exit map `0/1/2/3` declared, 6 checks implemented, **7 declared `not-evaluated` with reasons**, self-test **12/12** (asserts exit code *and* ordered finding-ids), **8/8 frozen snapshots MATCH** — re-run by the L1, not the drafting seat |
| V3 round-8 provisional box-3 verdicts resolved | **0 / 3** | **3 / 3** — kagi **breaks**, kasegi **could-not-evaluate**, kake **stays provisional** (named cause); kengaku + kumitate **firm**, kotoba `[~]` stands |
| V4 `SHONEN.md` canonical-form census | **0 / 6** | **6 / 6** — 3 trivially clean, 3 deviate; **0 of 6 `[x]` marks carry a `<verifier-id>`** |
| V5 rule-8 grades on the literal text, with unit + revision + authorship | **0 / 6** | **6 / 6 FAIL-literal / PASS-intent** (occurrences 2/1/2/1/3/77) |
| V6 wave seat artifacts durable | **0 / 15** (`.ufo/waves/round-8/` absent) | **15 / 15** committed |
| V7 gate teeth, demonstrated live | metric did not exist | **`r10` 6 → 0** across all six repos once the lessons were mirrored, with no edit to the gate |
| V11 non-author re-execution of this lane's own record | 41 cells, transcript never committed | **15 cells → 5 PASS / 4 STALE / 6 FAIL**, all six absorbed |
| V12 self-defects filed (cumulative) | 19 | **26** (7 new: 20–26) |

**The gate's teeth, in the only form that counts** (§14.17): before mirroring, `--all` reported 292 findings including
**6 `r10`** (this round's aggregator lesson absent); after the six single-file child commits, `--all` reports **0 `r10`**
and all six `# summary` lines drop it from their rule sets. A finding appeared while the obligation was unmet and
disappeared when the artifact landed.

## What this round falsified about this lane

- **Round 8's headline metrics are not re-derivable.** X2 (115/105/10 → **99** indexed rows exist), X3 (28 → **17**),
  X4 (30 → uncountable from the committed tables), X8 (41 → **no committed cell ledger**), and the report's "17
  aggregator-identity child commits" vs its own 16/15. Root cause, one line: **round 8 committed the ledger and the
  report but not the wave.** Corrected in §14.11, filed as self-defects 21/24, routed **D-129**; fixed structurally by V6.
- **Two published re-run cells were wrong.** §13.6-B's resolver ("operative grade = last bold mark") returns kumitate's
  **withdrawn** `[ ]`; §13.3's kessho cell "6 lanes / 9 artifacts" carries no command and contradicts its own five-lane
  list (re-derived **5 lanes / 15 harnesses**). Self-defects 22/23, **D-130/D-131**.
- **The auditor is the fleet's dominant rule-8 offender.** In 5 of 6 repos the literal `op://` hits sit in files this
  lane wrote (`round-5-`, `round-6-aggregator-audit.md`) while refresh 4 published rule 8 as *"clean everywhere"* — and
  `CORPUS.md:43-46` says "including this one's examples". Self-defect 20, **D-125**, L0 line appended.
- **138 unqualified cross-repo citations** in this lane's mirrored lessons, **6 of which kagi's own citation gate counts
  `UNRESOLVED`** (`CITATION_GATE: BROKEN … unresolved=33`) — this lane is a measurable contributor to a sibling's red
  gate, having mirrored a *bare-path* defect to that same sibling at round 5. Self-defect 25, **D-128**, fixed forward
  (path-convention line + `shokunin:<path>`; **9 → 0** in this round's drafts, scanner re-run), proposal **P-t**.
- **Round 8's residual was partly wrong as written.** *"No `SHONEN.md` box-3 line names a resolvable non-author
  verifier yet"* — kengaku's **does** (1/6). The sharper truth: **0 of 6 `[x]` marks carry the `<verifier-id>`** the
  canonical form requires, so no `[x]` in the fleet is form-conformant (§14.7). kotoba meanwhile **downgraded its own**
  box 3 from `[x]` to `[~]` because its verifier was lane-dispatched — the promotion rule working, in a lane, unprompted.

## L2 wave digest — 15 seats, one batched `task` call (MISSION.md floor: 8)

| Role (route bucket) | Seats | Output |
|---|---|---|
| `labrat` (@m_zfl) ×6 | VerdictKasegi, VerdictKengaku, VerdictKake, VerdictKumitate, VerdictKotoba, VerdictKagi | the six rule-10 verdicts + box-3 re-runs + gate conformance cells; `seats/verdict-*.md`, 6 lesson drafts |
| `scout` (@m_flash) ×2 | SweepWindow, StandingTables | 11 window reports / 0 markers / 6 missing SHONEN; MANIFEST 36 entries, last-wins 83/4/7/18, **8 stale rows**; 12/12 standing rows re-run |
| `executor` (@m_flash) ×1 | GateDraft | `corpus-gate.mjs` (889 lines) + `corpus-gate.expected.json` (280 lines) + `seats/gate-draft.md` |
| `critic` (@m_zfl) | CriticSeat | **7 attempts → 4 FALSIFIED / 6 repaired-by-amendment / 1 survives**; all amendments absorbed before landing |
| `connector` (@m_lunamax) | ConnectorSeat | 8-tool gate-adoption matrix with line cites; **bounties blast radius** (§14.18); the `proxy-check` seam ruling |
| `reviewer` (@m_zfl) | ReviewerSeat | 15 cells of this lane's own record → 5/4/6 (PASS/STALE/FAIL) |
| `distiller` (@m_zfl) | DistillerSeat | 118 distinct keys, next free `D-121`, 0 collisions, 2 folds hold, 3 contradictions; 4 harvested rows |
| `sentinel` (@m_zfl) | SentinelSeat | 16 credential classes, 81 shaped hits, **0 matching commits since the cutoff**; write/push-scope audit + the `ade32e4` sweep mitigation |
| `revenger` (@m_zfl) | L0Forensics | blob-level forensics over all 11 L0 lines: **0 operator answers ever**, 1 answered-by-ruling, 1 superseded |

Three L1 amendments were broadcast mid-wave and all seats reconciled: HEAD drift (5 of 6 child repos moved inside the
wave), rule-8 graded on its literal text rather than by inheritance, and the corrected `SHONEN` canonical-form algorithm
(the L1's first pass was buggy — it compared a box body to a *prefix* and reported a phantom deviation on all 24 boxes;
the bug is recorded in `l1-baseline.md` §2 so the corrected numbers are not confused with it). ConnectorSeat was still
live at composition; its evidence file was committed at `6415a9b` and §14.18 was appended from it.

## Routed findings (not this lane's to fix)

**30 rows, `D-121`…`D-150`** (ledger §14.16 + §14.18). By owner: operator/integrator 5 (D-125 rule-8 literal text,
D-126 unnumbered rules, D-141 rules 4↔9 collision, D-142 rule-7 text vs interpretation, D-146 untracked prompts),
protocol 2 (D-127 registry home for main-repo lanes, D-143 8 stale MANIFEST rows), kasegi 4 (D-123, D-135 PROVINCE
uncorrected, D-136 box-3 harness untracked, + D-150 shared), kagi 3 (D-133 box-3 `[x]` vs its own red gates, D-134
shared verifier-id row, D-144 unlanded r12 report, D-149 no trailing newline), kumitate 2 (D-138 frozen-run fail-closes,
D-139 registry row), kotoba 3 (D-124, D-140 probes not gates, D-145 unlanded r14 report, D-148 SHONEN form), kake 2
(D-121, D-122), kengaku 1 (D-137), aggregator 5 (D-128…D-132, D-147).

Proposals routed to protocol/CORPUS: **P-s** a cell's identity is the revision it measured, not the round's cutoff;
**P-t** mirrored lessons qualify cross-repo pointers (`shokunin:<path>`); **P-u** a count names its **unit** as well as
its command — lines vs occurrences vs files produced four different "correct" kagi numbers inside one wave (53/54/55/77);
**P-v** §Gate standard's registry clause needs a home for the two main-repo lanes (the D-120 class repeating).

## L0 surfacing (MISSION.md: the aggregator surfaces entries each round)

11 lines classified by git forensics over every blob of the file (`609ecb6` empty → `df1b2c6`; sha256
`6ca2a358…e15f` before this round's append). **Operator answers: 0** — the only in-place edit ever made is kake's own
r12 refinement (825→1461 bytes at `46e9ec3`). Full table: ledger §14.13.

- **Answered by protocol ruling, not by the operator:** `kengaku | round-10 | Promote the gate convention…` — §Gate
  standard (`dddb4ec`) pins `0=clean`/`1=failed`, requires every other code declared and mapped, and requires a
  self-test asserting exit code **and** a stable finding-id with committed expected values. Residue is adoption
  (D-137…D-140), not decision.
- **Superseded:** `kasegi | round-12` (stalled rebase) by `kasegi | round-15` (the root is gone entirely).
- **Blocked-external, not re-flagged:** `protocol | round-10 | kama mint decision` — bar met, and its line is
  byte-identical to the `e333e7c` blob (md5 `643e7114dd5f9286cdf27a4a654bc800`) ⇒ unanswered.
- **Open, operator-only (9):** kasegi r15 (sev 1 — actor undetermined, 740/782 citations dead, §14.18 shows 4 more
  surfaces affected), protocol r10 driver/template debt, kagi r10 `cmd_refs` prefix-match redaction, kake r12
  `webzites-keeper.timer` (re-verified: disabled, inactive, `LastTriggerUSec=` empty, never fired), aggregator r6 D-78
  axis vocabulary, kumitate r10 driver adoption, kumitate r11 scorecard block, kotoba r13 axis accounting.
- **New line appended this round (1):** the `CORPUS.md` amendment set — rule 8's literal text vs fleet practice,
  unnumbered rules cited by number, rule 7's phantom-row text vs the under-coverage reading graded since round 6, and
  the rule-4/rule-9 collision on quoted-and-refuted counts (D-125/D-126/D-141/D-142). The file was clean vs HEAD before
  the append (`git diff --numstat` → `1 0` after), so the commit swept no sibling line.

## SHONEN

The main repo carries no `SHONEN.md` (fleet-meta has no minted shonen; the aggregator lane is a role) — the
interpretation protocol published at round 11 and this lane used at rounds 4, 6 and 8. The four canonical boxes,
assessed against this lane's round-9 artifacts:

- `[~]` **SKILL.md contains real decision tables, error patterns, checklists, cited sources** — no `SKILL.md` exists for
  this lane; the nearest artifacts are the ledger's standing tables (§12/§13/§14) and `corpus-gate.mjs`'s registry block
  (6 implemented checks with `CORPUS.md` line cites, 7 declared `not-evaluated` with reasons). Author-asserted.
- `[~]` **At least one end-to-end domain task executed and logged** — the domain task is the refresh itself: 15 seats
  dispatched, 6 verdicts emitted, 6 lessons mirrored and committed in six child repos, gate run over all six live trees
  and 8 frozen snapshots, `LOG.md` §Round 9. Executed and logged, but author-asserted: this lane authored the round.
- `[~]` **Instructions executable by an agent without oral context** — `.ufo/waves/round-9/CONTEXT.md` + §14.14's re-run
  blocks R0–R8 are copy-paste runnable and were run by 15 cold seats this round; the counter-evidence is that 4 of round
  8's published cells were **not** re-runnable (§14.11), so the claim is graded on this round's artifacts only.
- `[~]` **No cross-domain bleed (`PROVINCE.md` still accurate)** — no `PROVINCE.md` for this lane; write scope was
  audited before landing by the sentinel seat (allowed vs forbidden path lists, `seats/sentinel-scope.md`) and obeyed:
  no operator-side file touched, no sibling corpus file edited, no child remote pushed, no `.ufo/state/**` or
  `watchdog.log` in any commit.

All four are `[~]` author-asserted: a subagent this lane dispatched is still this lane, so the critic, reviewer,
sentinel, distiller and connector seats are **not** non-author verifiers for this report. Only a verifier outside the
aggregator lane (protocol's closure pass, or a cross-lane seat) may write `[x]` here.

## Compliance

- **Write scope** (`PROTOCOL.md` §Invariants): main-repo writes limited to `.ufo/reports/AGGREGATE.md` (this lane's
  canonical ledger), `SCORECARD.md` + `LOG.md` (granted to the two main-repo lanes), `.ufo/reports/round-9/aggregator.md`
  (its report), `.ufo/waves/round-9/**` (round evidence, `PROTOCOL.md:434-435` + the `closure-check.py` precedent),
  `.ufo/prompts/aggregator-round-9.md`, and one appended `.ufo/l0-questions.md` line. **Not touched:** `MANIFEST.json`,
  `PROTOCOL.md`, `CORPUS.md`, `MISSION.md`, `AXES.md`, `scripts/`, `.ufo/state/**`, `.ufo/watchdog.log`, any sibling
  corpus file, any `SHONEN.md`.
- **Commits** are pathspec-limited (never `-a`/`add -A`), under `-c user.name=aggregator-shokunin -c
  user.email=aggregator@shokunin.local`; leftovers after the commit are only the forbidden runtime files.
- **Push scope** (`MISSION.md`): main repo pushed (`3d20676..6415a9b`). The six child-repo lesson commits are
  **committed, not pushed** — this lane has no sibling remote (round-8 sentinel ruling; round 6's six child pushes stand
  retro-classified as out-of-scope, self-defect 18).
- **Sweep hazard** (sentinel S-04, precedent `ade32e4`): each child commit was staged by exact path, committed
  immediately, and verified single-file (`git show --stat` → `1 file changed` ×6). kumitate's lane landed its own commit
  ~2 s after this lane's — no interference in either direction.
- **Report-order rule (P-r)**: all work was committed and pushed **before** this report was written; the report's
  write+commit+push is the round's last action, because `report_of()` still completes a mission on file existence.

## Next (round 10, falsifiable)

**corpus review — make the verdicts non-author re-derivable end to end.** (1) Resolve `corpus-gate.mjs`'s registry home:
§Gate standard puts rows in "each lane's `SKILL.md`" and `ls SKILL.md` → absent in the main repo (D-127/P-v) — either the
integrator rules, or this lane records a reasoned rejection and the gate stays **unregistrable**, never "conformant".
(2) Close the `r4` heuristic's three declared false-positive classes (246 findings across six repos, incl. the rule-4↔9
collision on quoted-and-refuted counts) until the cell is defensible as violations rather than as a heuristic.
(3) Re-run the gate at each lane's next landed revision and report per-rule movement, plus the 8 frozen snapshots.
**Falsified if** the gate is called conformant while unregistrable, if the `r4` cell is restated without its FP classes,
or if any verdict fails to name the revision it measured. **Owed and not to be aged:** the round-8 X-cells are corrected
in §14.11 but the round-8 section still reads as published (D-129); re-test D-133 (kagi's box-3 `[x]` vs its own red
gates) at kagi's next landed revision; and the dormancy rule still has no positive test case in seven refreshes.
