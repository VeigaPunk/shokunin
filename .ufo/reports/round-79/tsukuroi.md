# tsukuroi — round 79

## Work performed

Declared claims: **C1 depth** (lowest non-retired axis, 8), eight pinned
dependency-propagation rows from systemd v262 `man/systemd.unit.xml` with a
byte-bound author review; **C2 operability** (9), zero duplicate current registry
rows and two gate rows with hermetic selftests. C2 verifies; **C1 is a declared
miss** — the reviewer found that the frozen DP6 statement dropped the source's
precondition, and the frozen expected tuple cannot be altered after data. No
ordinal uplift, capability, coverage promotion or outside admission is claimed.
Admission is **not** claimed: C1 is a declared miss, C2 verifies, and the
operator rules on the round.

- C1 opened the owned systemd-unit surface's requirement/ordering keywords
  (`Wants=`, `Requires=`, `Requisite=`, `BindsTo=`, `PartOf=`, `Upholds=`,
  `RequiresMountsFor=`, `After=`) as a finite decision set. The landed entry
  `corpus/knowledge/systemd-dependency-propagation-r79.{md,json}` is byte-bound
  to ReviewDeps' second verdict (`artifact_sha256=1b8f833d…`,
  `companion_sha256=8c6b3809…`, `review_sha256=0c2dd4ad601e179110df546ec4933f2b3e8249e462a548db8263cbf5da1c8168`,
  all eight rows `holds`), verified by the L1 against the landed bytes.
  Receipts: `.ufo/waves/round-79/after/after-C1.txt`,
  `w1/ReviewDeps/{verdict.json,review-first.md,review.md}`.
- The first ReviewDeps pass returned DP6 `partly-holds`: the frozen quote
  stopped at "failed," and the statement omitted the sentence's continuation
  "and no job is queued for them" (`systemd.unit.xml:783–785`). The landed
  statement carries the precondition; the frozen predicate therefore reads
  `finite-content-mismatch`. Evidence: `w1/ReviewDeps/review-first.md`,
  `after/after-C1.txt`.
- C2 marks the four current continuation registry tables `NON-OPERATIVE`,
  gives `check-r71-routed-r72` and `count-md-rows-r72` hermetic selftests
  (8/8 and 23/23, rc 0; TMPDIR refusal rc 2; selftest failure rc 3), replaces
  their two verdict/self-test cells truthfully, and appends the two round-79
  instruments to the operative table. Evidence: `SKILL.md` operative round-71
  table, `w1/ExecInstrument/`, `w1/ExecRegistry/`, `w1/ReviewRegistry/`,
  `after/after-C2.txt`.
- Real read-only host task: `w1/ExecHost/handoff.md`, capture
  2026-11-04T19:08:44Z–19:09:59Z UTC, unprivileged, no unit touched. Directive
  counts over `/etc/systemd` + `/usr/lib/systemd` unit files: After= 279,
  Before= 240, Wants= 75, Requires= 70, PartOf= 24, RequiresMountsFor= 20,
  BindsTo= 20, Upholds= 1 (729 matched lines). Two user-scope transient
  `systemd-run` scopes are failed with `Result=oom-kill`; system scope has zero
  failed units; neither failed scope carries `BindsTo=`/`PartOf=`/`Upholds=`,
  so nothing propagates and nothing restarts them. Bounded-grep limits
  (drop-ins, `/run` units, symlinked `/etc` files, `Requisite=` uncounted) are
  stated in the handoff. No cleanup, restart or package action is authorized.
- One validated v1 wave **w1: 12 seats**, all settled: scout 1 / executors 3 /
  scribes 3 / connector 1 / reviewers 2 / critic 1 / mutation-tester 1; strict
  attack share 4/12; L1 holds the planner seat; residual 0; dead 0. Spec,
  dispatch, ready marker and results: `.ufo/waves/round-79/`. The delivered
  `w1-results.json` carries 12 null outputs with the orchestrator's
  kernel-restart note; the seats' reports are the retained evidence and **no
  output was reconstructed or inferred**. Routing was the live operator table
  (`task.agentModelOverrides`); no model parameter or route override supplied.
- Attacks: CriticFreeze ran 22 counter attacks (13 kills; A3/A7 survive by
  declared design; A13/A14/A15/A17/A18 survive as disclosed instrument gaps).
  MutationCounter killed 8/13 single-clause mutants and left 5 survivors (3
  live-path C2 detector gaps, 2 behind the frozen-equality leg). ReviewRegistry
  independently reproduced `duplicates=0 shape_ok=2/2 met=1` and the before
  `6 / 0-of-2`, confirmed the delivered rows' selftest modes run green, and
  named presence-based F1/F1b counter gaps. Evidence:
  `w1/{CriticFreeze,MutationCounter,ReviewRegistry}/`.
- Cross-domain: ConnectorScope scanned sibling provinces and found no absorbed
  scope; the id-collision guard is reproduced (147 staged ids S200–S346,
  intersection S200–S328) and the package's bare `S329` (a different document)
  is recorded, not renumbered — the package stays unadopted. `PROVINCE.md`,
  `SHONEN.md` and sibling ownership are unchanged.
- Limits: C1's numeric gate is answer-key equality plus digest arithmetic; a
  fabricated review bundle can pass it and the equality leg shadows the
  per-row quote/line clauses. C2's duplicate leg can be weakened by a
  self-declared marker, a new highest heading or duplicated heading text
  (`lines.index`); 36 of 93 operative `gate` rows still declare no selftest.
  Neither instrument is an authenticity or whole-registry conformance proof.
- Tool installs: none. Stale-lane: this is the only tsukuroi mission opened
  here; commits show progress; no successor round was started. The mandatory
  fleet-root sweep `after/fleet-status.txt` shows no round-79 lane artifact
  after the L1's own stray `.ufo/tmp-census-r79.txt` was removed and recorded
  (`corpus/lessons/round-79.md`, R79-FLEET-TMP); `.scratch/`, `.ufo/state/` and
  other lanes' files were untouched. No open L0 question was needed.

## Landed changes

All lane commits by `tsukuroi-shokunin <tsukuroi@shokunin.local>` via
`jj-lane.sh`; each ties to the LOG.md Round-79 entries.

| Commit | Carries | LOG entry |
|---|---|---|
| `afe1f26128bde87484001cd02ebf11fa524c4059` | frozen declaration, expected rows, both counters, pre-data controls, snapshot | LOG `Round 79 (2026-11-04) — dependency-propagation depth and gate-standard registry` |
| `883aae6107cace30795d3163092b08498e8d4b73` | validated w1 spec, dispatch, ready marker, receipt runner | same entry (wave evidence) |
| `c7dcd241cbdebbbfefebb3141aece97eb237ed3c` | knowledge entry + JSON, S329, QUALITY 110, README section, lesson, registry repairs, two tool selftests, wave reports | same entry |
| `36336aac07c25cc9c36343e4a57146035b0592aa` | wave settlement, reviewer-corrected lesson, results; **measured revision** | LOG `Round 79 — integration and measured outcome` |
| `7d5816aa188bc03ef6de630b7d0296495fad2cd0` | revision-bound receipts, SCORECARD measured outcome, structural record | same |
| `3d329c354d9020c0a1ba9d1ef41b50db12ab562a` | end census, fleet sweep, R79-FLEET-TMP correction; **final lane tip** | same |

`git ls-remote origin refs/heads/master` printed
`3d329c354d9020c0a1ba9d1ef41b50db12ab562a refs/heads/master`; `jj-lane.sh
state` reads `local=3d329c35… remote=3d329c35… ahead=0 behind=0` with a clean
tracked/untracked count.

## Before → after measurements

Counting commands, run at the cited revisions; receipts carry revision, tool
path, tool SHA-256, argv, stdout and exit under `.ufo/waves/round-79/after/`.

| Claim | Command | Before (`9086589a82f221d130ed6711fbe70b85f0d07aea`) | After (`36336aac07c25cc9c36343e4a57146035b0592aa`) | Verdict |
|---|---|---|---|---|
| C1 depth | `python3 tools/measure-unit-deps-r79.py --revision <REV>` | `rows=0 met=0 reason=unreadable:FileNotFoundError` rc 1 | `rows=0 met=0 reason=finite-content-mismatch` rc 1 | **not verified** (frozen expected tuple vs reviewer-corrected entry; predicate/counter/expected not altered after data) |
| C2 operability | `python3 tools/check-gate-standard-r79.py --revision <REV>` | `duplicates=6 shape_ok=0/2 met=0` rc 1 | `duplicates=0 shape_ok=2/2 met=1` rc 0 | verified |

Supporting same-run gates at `36336aac`: C1 selftest `32/32`, C2 selftest
`8/8` (both rc 0); `check-registry-coverage` PASS 119/119 rows, 0 findings;
`check-knowledge-refs-r68` 0 dangling; `check-line-endings` PASS;
`check-knowledge-header` keeps its two inherited findings (identical at base).
`after/structural.json`: registry 328 → 329 (A 311 → 312, B 6, C 11; mined
290 → 291, queued 5, rejected 33), knowledge notes 96 → 97, tools 117 → 119,
frozen snapshot/expected byte-identical, only the two routed tools modified and
no tool deleted. The C1 selftest's 32 cases are 32 passed because the expected
file's digest is frozen; per MutationCounter, the data-side equality leg
shadows the per-row quote/line clauses.

## Sources & frontier

Census command, run at round start and round end:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`
→ exit **0** both times (`.ufo/waves/round-79/{before,after}/census.txt`), W04
duplicate-URL warnings only (S329 shares its URL with S304's unit-load scope).

- Rows before → after: **328 → 329** (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`).
- Rows added by tier: **A +1, B +0, C +0**; status mined 290 → 291, queued 5,
  rejected 33.
- Rows touched old→new: **none** — no existing row's `status`, `recheck` or
  `used-by` changed; S329 is new and cites
  `corpus/knowledge/systemd-dependency-propagation-r79.md` and
  `corpus/lessons/round-79.md`.
- Frontier rows advanced: **0**; this deepens existing systemd-unit ground, not
  a coverage-map promotion. `corpus/README.md` carries the Round-79 row and
  says so. `PROVINCE.md` and `SHONEN.md` unchanged.
- Gate records: `corpus/lessons/round-79.md` `## Gate` carries the S329 admit
  (URL, 2026-11-04, located quote at `:659`) and three rejects
  (`After=` pulls in; `Requires=` guarantees active state; `Upholds=` is
  one-time) with located quotes and flip conditions. Non-author spot-check of
  the admits/rejects remains pending.
- Assimilation: none — the operator-held package and promotion stay
  unadopted; the collision guard is reproduced and the package's `S329` is
  recorded as a document-namespace ambiguity, not renumbered.
  `considerthese/2026-10-26.md` adoption: the seat-harm incident log lands as
  QUALITY 110 and the lesson's `## Seat harm` table (two recorded collisions,
  one attributed-by-disclosure set, `/tmp` files left `[unk]`).

## Trend verdicts

| Trend | Verdict | Evidence |
|---|---|---|
| expansion | unchanged | One new row and one new entry, but the entry deepens the already-owned systemd-unit surface; no coverage-map or frontier promotion and no capability row. `corpus/README.md` Round-79 section says so. |
| quality | unchanged | A new sourced entry landed reviewed (all eight holds on the corrected bytes) and two gate interfaces became truthful, but no prior corpus entry was superseded or re-verified, so QUALITY 49's prior-knowledge condition is not met; the entry's admission is not claimed as quality credit. |
| discernment | unchanged | The round's own reviewer caught a real frozen-row defect and the attacks produced a documented survives list, but the author-side catch is not the outside check; the non-author admit/reject spot-check remains pending and is the deciding evidence. |

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — author-side pointer: the operative registry table (119 rows, `check-registry-coverage` PASS) plus the Round-79 decision section; no new non-author verification this round.
- [~] At least one end-to-end domain task executed and logged — `w1/ExecHost/handoff.md` (read-only dependency sweep, 729 matched lines, 2 failed user scopes with `Result=oom-kill`) and LOG Round 79.
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/systemd-dependency-propagation-r79.md` states its source boundary, quote normalization and counter command; the whole-SKILL no-oral-context replay remains unexecuted.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; ConnectorScope's sibling scan (`w1/ConnectorScope/overlap.md`) found no absorbed scope; contested kaidoku/revenger ownership remains unruled.
