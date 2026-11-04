# mado — round 67 report (hyaku run 15, attempt 1)

Lane: `/home/vgpnk/Projects/shokunin/mado-shokunin` · lane HEAD `92151a50cc79b40700cafab98488012089f67e34`
· report commit: this file · base `0b28ffb4baac9586566d246c3f0986b2bb650a33`
· frozen declaration `061dc329b598b2723a224b6c7b305b436946ec91`
· instrument cutover `5f9ce459803dc17aceb16a6f8507006b85737c35`
· measured content `caf131d6be04dd2ccc742636625c1ce196610522`
· wave/receipt commit `2447048be5467ca0e35928d80aa99c90523a6739`
· record commit `2f052318c75621af16b6cf2af626028671844dc7` · sweep receipt `92151a50cc79b40700cafab98488012089f67e34`
Lane axes: coverage + operability (desktop and compositor craft). No push outside the fleet repo and this lane.

## Work performed

Two declared claims, both frozen before candidate bytes existed, both taking the r66 closure's
planned items (C1 calibration, C2 operability):

1. **C1 calibration — register citation-to-live-object binding.** The returned-host register must
   cite the live receipt inside a table row's receipt cell; the tree-level r66 check accepted an
   unreferenced live object. Measured on a frozen six-case control set: r66 counter 4/6 → r67
   counter 6/6 with the genuine register accepted.
2. **C2 operability — zero-citation and replacement-ref controls.** The standing landing
   instrument must ship tests that kill the zero-citation guard clause (M-Z) and a git-reading
   child's `GIT_NO_REPLACE_OBJECTS` guard (M-R); the pre-r67 tip leaves both untested. Measured:
   candidate harness 2/2 killed, the same harness at the base 0/2.

Work items (one bullet per item; evidence pointer):

- Pre-freeze control baseline built and committed **before** the declaration: the r66 counter on the
  six frozen cases and the pre-r67 instrument inventory + git-layer replacement read. Evidence
  `aa7fe5a1` (`control-baseline-r67.txt`: C1 4/6, C2 0/2, `child_env_read=forged guarded_read=real`).
- Freeze committed alone, before any candidate byte: `.ufo/waves/round-67/claims-declaration-r67.md`
  at `061dc329`; controls unchanged at every later revision (`git diff aa7fe5a1..HEAD -- controls`
  empty; critic chronology check).
- C1 counter `quality/counters/c1-r67-register.py`: git-object reads only, one heading, eight frozen
  groups, row-local receipt resolution, live path required inside a row's receipt cell, exact
  committed live line, 16-case hermetic selftest; control-set scoring with the frozen JSON.
  Evidence `5f9ce459`; measured `caf131d6`.
- C2 harness `quality/counters/c2-r67-landing-controls.py`: extracts the
  standing instrument and children at `--rev`, runs the instrument selftest, deletes exactly one
  occurrence of each frozen literal, runs each mutant, prints mutant digests; 47-case hermetic
  selftest. Evidence `5f9ce459`; measured `caf131d6`.
- Standing instrument `quality/landing-counters.sh`: one new `zero` selftest case (a citecheck marker
  at `citations=0` must be ERROR), 62/62 assertions; marker contract, exit map, `--round` and the
  external-path refusal unchanged (`5f9ce459`).
- Child guards: `quality/counters/c3-r56-used-by.py`, `quality/check-tool-ledger.py` and
  `tools/mado-receipt-citecheck.py` each set `GIT_NO_REPLACE_OBJECTS=1` themselves; the r66 parent
  export did not reach the two children that rebuild their env (`5f9ce459`).
- Knowledge entry `corpus/knowledge/replace-ref-citation-boundaries-r67.md` (blob vs tree/commit
  replacement levels, presence-not-truthiness of the guard, the lane git-reader census, the R
  control's limits), its coverage-map row, source `S436` (git v2.56.0 `git-replace.adoc`, tag-pinned,
  three independent fetches with the same sha256), QUALITY 109, SKILL gate rows, a bold PROVINCE
  refinement paragraph — `caf131d6`.
- Wave: one v1 wave, 13 seats, one batched dispatch through the orchestrator handoff
  (`w1.ready` → `w1-results.json`), settled 13/13. Evidence `.ufo/waves/round-67/w1/`,
  `wave-done-r67.txt` (`seats=13 dispatched=13 settled=13 verdict=OK`).
- m5 auxiliary probe (connector §6): a planted `refs/replace` on `PROVINCE.md` leaves the C1
  verdict unchanged; the counter reads the real object through its own guard (`aux-m5-r67.txt`).
- considerThese 2026-10-28 proposal 2 executed once at the pre-r67 tip:
  `python3 quality/check-session-material.py --repo . --rev 0b28ffb4 --scope all` → exit 1,
  `files=33466 findings=280`, `waived 49 files/47`; the r37/r38 socket tables carry 5 and 715
  process rows (`considerthese-privacy-r67.txt`). Routed to L0 (history/redaction is operator-owned).

## Landed changes

Every change is tied to its `LOG.md` round-67 entry and to the commit that carries it.

| Change | Commit |
|---|---|
| Pre-freeze controls + do-nothing baseline receipt + census start | `aa7fe5a1` |
| Frozen claim declaration (predicates, counters, controls, targets, kill rules) | `061dc329` |
| Wave spec, dispatch payload, registry, ready file | `ac376ef3` |
| `c1-r67-register.py` (with the integration B3 repair), `c2-r67-landing-controls.py`, landing-script `zero` case, three child guards, two ledger rows, baseline-scorer base fix | `5f9ce459` |
| Lesson `corpus/lessons/round-67.md`, knowledge entry, `corpus/README.md` row, `S436`, QUALITY 109, SKILL registry rows, PROVINCE refinement, round-67 citation scope | `caf131d6` |
| Settled wave outputs, measurement receipts, census end, index/anchor receipts, considerThese receipt | `2447048b` |
| SCORECARD round-67 section + capability row, LOG round-67 entry, lesson addendum, source-shape and wave-done receipts, m5 probe | `2f052318` |
| Misroot sweep receipt (fleet root, no lane/round file; unrelated `after` left untouched) | `92151a50` |

The r66 files stay at their historical revisions; the standing script was cut over at its own path
as declared. No compatibility alias was added.

## Before → after measurements

Counting commands are pasteable from the lane root; `REV` is the measured content.

**C1 — calibration.**
`python3 quality/counters/c1-r67-register.py --repo . --rev REV --controls .ufo/waves/round-67/controls/c1-controls.json --scratch-root DIR`
- before (`0b28ffb4`, r66 counter): `correct=4/6`, accepts `unreferenced-live-object` and
  `live-in-state-cell-only` — `control-baseline-r67.txt`.
- after (`caf131d6`): `MADO_R67_REGISTER: register=accept controls=6/6 headings=1 rows=8
  groups=8/8 live-cited=yes verdict=TARGET_MET` rc 0; selftest 16/16
  (`measurement-c1-after.txt`). Bounded score `10 × correct/6`: 6.6667 → 10.0000.

**C2 — operability.**
`python3 quality/counters/c2-r67-landing-controls.py --repo . --rev REV --scratch-root DIR`
- before (`0b28ffb4`): the same harness prints `selftest=0 mz=fail mr=fail killed=0/2
  verdict=TARGET_MISSED` rc 1 — `measurement-baseline-derived.txt`; the pre-freeze inventory shows
  `zero_citation_case=0`, `replace_ref_case=0`, `usedby_guard=0`, `ledger_guard=0`, the used-by-shaped
  child env reading forged bytes.
- after (`caf131d6`): `MADO_R67_LANDING_CONTROLS: selftest=0 mz=pass mr=pass killed=2/2 baseline=0/2
  verdict=TARGET_MET` rc 0; harness selftest 47/47, landing selftest 62/62
  (`measurement-c2-after.txt`). Bounded score `10 × killed/2`: 0.0000 → 10.0000.

Harm watch at `caf131d6`: `MADO_LANDING_COUNTERS: GREEN` with navigation 79/79, used-by
`missing=0` (rows 373), ledger 110/110, all cited paths resolved; gate selftest 460/460; index
79/79 and index-rows 79/0 errors; QUALITY 107 anchor cover 8/8; census exit 0. Receipts:
`landing-counters-r67.txt`, `measurement-selftests-r67.txt`, `index-checks-r67.txt`,
`anchor-cover-r67.txt`, `census-end-r67.txt`.

## Sources & frontier

Registry before → after (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
and the tier histogram in the `CORPUS.md` census block): **372 → 373 rows** at `0b28ffb4` →
`caf131d6`; tiers **A 358 → 359**, B 7, C 7 unchanged; malformed 0 both ends
(`sources-shape-r67.txt`). Census command
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`
exit 0 at round start (`census-start-r67.txt`) and at the final tip (`census-end-r67.txt`; warnings
W04/W01 pre-existing).

Rows added: one — `S436`, tier A, kind docs, git v2.56.0 `Documentation/git-replace.adoc`
(tag-pinned, fetched bytes sha256 `3f61be3f…`, three independent fetches; the tag sentence and the
`GIT_NO_REPLACE_OBJECTS` sentence are quoted in the lesson Gate). Rows touched old→new: **none** —
no existing `status`/`recheck`/`used-by`/`opened` cell changed (the r65 routed defect-1 rule kept).
Frontier rows advanced: one — the lane-tooling ground "what a replacement object does to a git
reader, and which lane instruments must set the guard", landed as
`corpus/knowledge/replace-ref-citation-boundaries-r67.md` with its coverage-map row and `S436`
mined; the entry records the measured two-level rule (a replaced blob leaves `ls-tree` ids intact; a
replaced tree/commit rewrites the listing) rather than the brief's one-level shorthand.
**Assimilation: none** — `shokuknow/merge/mado/` (147 rows, 65 knowledge files) has no fit (0 hits
for replacement refs / lane instruments) and its staged ids S203–S349 collide 94/147 with the lane
registry, so adopting it would need scratch renumbering plus re-grounding and would still be
off-axis (connector screen, `.ufo/waves/round-67/w1/R67ConnSiblings.md` §2).
considerThese: one proposal executed as evidence (2026-10-28 proposal 2, privacy scan), routed to L0;
no proposal absorbed as a claim.

## Trend verdicts

- **expansion: improved (bounded)** — one admitted `corpus/knowledge/` entry on lane-tooling ground
  the coverage map did not hold, its `source:` citing the mined `S436` row and its coverage-map row
  landed in the same commit (`caf131d6`); no desktop surface or PROVINCE frontier move is claimed,
  and the entry's Scope section disclaims desktop/PROVINCE-truth/authenticity claims.
- **quality: improved** — two instruments tightened with owned controls and hermetic selftests
  (4/6→6/6, 0/2→2/2 at a named revision), one new QUALITY criterion (109) grounded in a measured
  failure (parent export never reached env-rebuilding children), and the standing instrument's
  selftest grew 58→62 with the real four-leg landing green at the measured revision; no admitted
  entry was found false or stale and left unmarked.
- **discernment: improved** — the Gate records one admit (`S436`, re-opened by the scout, the
  knowledge scribe and the lesson scribe) and rejects with flip conditions (`core.useReplaceRefs`
  config plane; the "guard proves authenticity / repairs a rewritten repo" over-claim); the round's
  own attack seats disagreed twice on the record and the disagreement became a criterion/fix: the
  r66 routed defect 1 is mined as M67-1 (quote the child literal before freezing), the critic's B3
  regression was repaired at integration with 0 frozen-verdict changes, and B1/B5/B6/B7/B9 are
  disclosed in the lesson. An outside non-author spot-check remains the closure's, not the lane's.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  pointer: `SKILL.md` round-67 registry rows + `corpus/lessons/round-67.md` Gate; historical
  assertion `corpus/knowledge/executor-test-sufficiency.md`; outside-lane independence still not
  established.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: LOG.md round-67
  entry (the two frozen counters run end-to-end at `caf131d6`); no new desktop task this round and
  no outside-lane verification.
- [~] Instructions executable by an agent without oral context — pointer: the seat reports under
  `.ufo/waves/round-67/w1/` executed the frozen declaration from bytes alone; dispatched seats
  remain the authoring lane, not outside clearance.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: PROVINCE.md round-67 refinement
  (bold append after the r65 sentinel; no heading added) and the connector's no-absorb table; no
  fresh outside-lane approval.

## Round shape, seats, L0 and tooling

- Shape: ONE v1 wave (`ufo-wave-policy.json`, band 8–16), **13 seats**, one batched dispatch through
  the orchestrator handoff; no residual call; round total 13. Roles: executor 4, scribe 2, scout 2,
  connector 1, reviewer 2, critic 1, mutation-tester 1 — attack share 4/13 (30.8 %). L1 holds the
  planner seat (validator rejects a planner seat; no planner item was faked). Dead seats: 0;
  seats settled 13/13; `MADO_WAVE_DONE: round=67 waves=1 settled=1 verdict=OK`.
- Re-verified before landing: pre-freeze controls committed before the freeze; `Report:` trailers
  resolved under the lane; no seat wrote the fleet repo, a sibling lane or a mutating git/jj command.
  Misroot sweep at the fleet root found no lane/round file; the unrelated 24-byte `after` and the
  orchestrator-owned `.scratch/*` were left untouched (`misroot-sweep-r67.txt`, `92151a50`).
- Open L0 questions carried (not answered): r57–r60, the standing L2-floor line, the host-recovery
  pacman pause. A new L0 line was filed this round: the tracked r37/r38 socket tables and the
  privacy-gate finding count — a history/redaction decision, not a lane repair.
- Tooling: no install or upgrade; no pacman transaction (host-wide pause respected); no service,
  compositor or socket write. No credential material, session tokens, cookies, `op://` refs or
  screenshots in any artifact.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
