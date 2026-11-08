# tameshi round 98 — measurement-derived control codes (C1) and guard refusal receipts (C2)

Lane: `tameshi-shokunin` (verification-fixture craft). Round 98, attempt 1.
Lane base at round start: `034240a591575167f0747ad7372a1f4b9cd33a58`.
Instruments commits: `6b1428c8` (v1 audit, repaired driver, battery, registry audit) and
`d32043ec` (battery exit-code repair; wave specs). Freeze: `764aca97`. Records revision R:
`3b7ae1272d161aa0297e1d04b2b7ec5b40112912` (the commit that carries the amended plan/claims, the
repaired instruments, the wave reports and the record prose). Landing: `fa2d2169`; lesson wave
section: `647408f0`; falsification ledger: `4b8f4ed1`. **Lane tip at filing: `28e7bda908bcef05261961f744dfe11edbf099a9`**
(`git -C tameshi-shokunin ls-remote origin refs/heads/master` prints it; `jj-lane.sh state` →
`branch=master local=28e7bda9 remote=28e7bda9 ahead=0 behind=0`; worktree clean).

## Work performed

Declared claims (two, distinct axes; frozen in `plans/round-98.plan.md` and
`.ufo/waves/round-98/claims.json`, amended A1-A10 with wave artifacts before the records run):

- **C1 — calibration (the lane's lowest non-retired axis, pinned 8):** every recorded code in a
  control driver is measurement-derived, checked by a committed static audit over committed driver
  bytes; the diagnosed round-97 literal-coded state (`c2-nowork-absent`) is repaired and its
  battery prints 18/18.
- **C2 — operability:** all six `GUARD_SETUP` refusal classes of the frozen round-97
  `guard-inertia.py` are exercised end to end through its public CLI from committed bytes, with a
  positive run, per-class lines and a red arm that must miss.

Work items (each with its evidence pointer):

- **C1 instrument.** `tools/control-assertion-audit.py` (records bytes sha256 `82c2e54b…`): reads
  a driver blob at `--rev` through `git cat-file` and classifies every bare-name `add(...)` site's
  recorded-code expression as measured / literal / unresolved, following a name through the
  call's scope chain to every assignment before the call. Selftest `18/18`
  (`pre-freeze/c1-audit-selftest.out` at the freeze; `records/c1-audit-selftest.out` at R). The
  round-97 driver prints `CONTROL_ASSERT sites=15 measured=14 literal=1 unmeasured=1` exit 1, line
  156 named (`records/c1-audit-r97-driver.out`); the repaired driver prints `sites=15
  measured=15 literal=0 unmeasured=0` exit 0 (`records/c1-audit-controls98.out`). The wave forced
  the repair (A5): v1 read source order over the whole module and missed branch order, function
  scope, shadowed `add`, attribute reassignment and augmented assignment — seven fixtures in
  `w1/R98R1.md`, the nested-scope constant in `w1/R98C1-c1-kill-a-shadow.txt`. The stub-runner
  spelling and the `want=code` tautology stay declared limits (A2, A6).
- **C1 repair.** `.ufo/evidence/round-98/controls98.py` (sha256 `f1c1db0e…`): `c2-nowork-absent`
  grades the measured `git grep` rc (1 at base `07e50d6d`) instead of the literal 0. Its full run
  prints `CONTROLS98 states=18 matched=18 mismatched=0` exit 0 (`records/controls98-run.out`);
  the only round-97→round-98 receipt change is `c2-nowork-absent` outer `rc=0`→`rc=1`
  (`w1/R98E3-receipts/R98E3-freeze-identity.txt`; 17 receipts byte-identical, all 18 re-derived by
  the seat). The same driver at base `034240a5` prints `matched=16 mismatched=2` by design
  (`pre-freeze/controls98-at-round-base.out`), the disclosed limit (A1).
- **C2 instrument.** `.ufo/evidence/round-98/refusals/guard-refusals.py` (records bytes sha256
  `de94cbcc…`): six manifest fixtures, one per class, run through the frozen tool's public CLI
  with the tool read as a blob at R and pinned to the frozen digest `634997d0…`; the positive runs
  the committed manifest and prints its ten `GUARD_ROW` lines. Positive: six `GUARD_REFUSAL
  <class> rc=2 token=ok` lines, `GUARD_REFUSAL_POSITIVE rows=10 rc=0`, `GUARD_REFUSALS classes=6
  refused=6 wrong=0 positive=ok`, exit 0 (`records/c2-refusals-positive.out`). Red:
  `GUARD_REFUSALS_RED state-unbuildable observed=missed rc=0` and `classes=6 refused=5 wrong=1
  positive=ok red=state-unbuildable`, exit 1 (`records/c2-refusals-red.out`). Selftest 9/9. The
  wave forced the pin and transcript repairs (A7-A9): `w1/R98R2.md` F1-F3, `w1/R98SN1.md` F1 and
  `w1/R98E2.md` F1-F3 showed a caller-supplied tool pin, no per-class line and an
  indistinguishable red summary in v1.
- **Routed defect D-1.** The round-97 in-place `anchor` edits on S159/S006 are logged old→new in
  the lesson (remedy B) and the class is measured by `tools/registry-cell-immutability.py`
  (sha256 `30f0543a…`): red pair `0b19af5f..29734beb` → `REGISTRY_CELL S006:anchor changed`,
  `REGISTRY_CELL S159:anchor changed`, `changed=2`, exit 1
  (`pre-freeze/registry-red-r96-r97.out`); green pair `29734beb..R` → `changed=0 removed=0
  added=0`, exit 0 (`records/registry-green-r97-records.out`); selftest 10/10. (The registry
  re-check seat R98E4 settled without a report; the L1 ran both pairs itself.)
- **D-3.** The three stale pre-A15 fragments are marked superseded by appended notes with both
  digests (`.ufo/evidence/round-97/pre-freeze/NOTE-superseded-r98.txt`,
  `.ufo/waves/round-97/w1/NOTE-superseded-r98.txt`); no original byte rewritten.
- **D-4.** `committed-battery binder`, `guard-inertia matrix`, `control-assertion audit`,
  `guard refusal battery` and `registry cell audit` entered the SCORECARD `## Capabilities` table;
  the table's stale "none enter" sentence is corrected append-only.
- **D-5.** The round-97 report's S159/S006 erratum and the `CONTROLS97` summary restatement are in
  `corpus/lessons/round-98.md` §Errata and
  `.ufo/evidence/round-97/pre-freeze/CONTROLS97-summary.txt`.
- **D-6.** Closed by C2: the two code-only classes (`state-unbuildable`,
  `limit-mechanism-missing`) now have committed receipts through the frozen tool's public CLI.
- **D-7.** Stale-lane line below.
- **Frontier.** S012 re-opened live (snapshot sha256 `fb6f384d…`, renderer line 112, 16-word
  quote) and cited by `corpus/knowledge/control-assertion-anchoring.md`; S009 re-opened on a
  declared-UA fetch (HTTP 200, 42254 B, sha256 `be3f85db…`, abstract at renderer line 413, 14
  words), row kept `queued` (no admitted entry cites it); the default-UA 403 challenge is M5.
  Census exit 0 before and after (183 rows); QUALITY 177; README round-98 row; mistakes M1-M7 in
  `corpus/lessons/round-98.md`.
- **Wave.** One v1 wave `w1`, 13 seats (executor 4, scribe 1, scout 1, reviewer 2, critic 1,
  mutation-tester 1, sentinel 1, connector 1, revenger 1; attack 6/13 = 46% by the §6 named set —
  reviewer×2, critic, mutation-tester, sentinel, revenger). Twelve seats filed a report in
  `.ufo/waves/round-98/w1/`; **executor R98E4 is a dead seat** — its `w1-results.json` output is a
  truncated first line ("I'll start by reading my spec and the frozen claims.") with no report and
  no receipts. The L1 holds the canonical planner seat (the validator rejects `planner`); the
  bounded planning data-walk rode the critic/revenger items. Round total: 13 seats, one v1 wave,
  no residual call. Seat verdicts: R98E1 reproduced C1's numbers/exits/blob arms; R98E2 reproduced
  C2 and hand-drove both formerly code-only classes; R98E3 re-derived all 18 control receipts;
  R98R1 falsified five C1 classification mechanisms (A5); R98R2 falsified C2's pin/red/transcript
  sentences (A4/A7/A8/A10); R98C1 found the nested-scope constant (A5) and the `want=code`
  tautology (A6); R98M1 ran a 20-mutant matrix over both instruments (`MUTANTS audit=7/10 battery=7/10`;
  with the repaired instruments the same runs give `audit=6/10 battery=5/10`, the three extra
  survivors a8/b8/b11 killed only by a supplementary arm); R98SN1 held environment/path confinement and found the unpinned
  battery mode (A7); R98CN1 found no duplicate implementation; R98L1 mapped the recorder-shape
  boundary; R98S1 drafted the record fragments; R98SC1 re-opened both sources and the UA matrix.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| v1 instruments: audit, repaired driver, battery, registry audit | Round 98 C1/C2 | `6b1428c8` |
| battery exit-code repair + wave specs | Round 98 | `d32043ec` |
| freeze: plan, claims, 12 pre-freeze control runs, S012/S009 snapshots | Round 98 | `764aca97` |
| wave w1 spec + validator dispatch (13 seats) | Round 98 wave line | `cdaecece` |
| records: repaired audit (v3) and battery (v2), wave reports, lesson, QUALITY/README/SOURCES, before-token controls | Round 98 | `3b7ae127` (R) |
| records receipts at R, SCORECARD §Round 98, `records-rev.txt`, falsification ledger, census after | Round 98 | `fa2d2169` |
| lesson Wave section | Round 98 | `647408f0` |
| falsification ledger paths under `w1/` (prefile gate pass) | Round 98 | `4b8f4ed1` |
| SCORECARD wave text (R98M1 mutant tallies as reported) | Round 98 | `28e7bda9` |

## Before → after measurements

Each line is printed by a committed command at the revision named; both counters are re-derived
by this round's wave seats and the closure can re-run them.

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 | at base `034240a5` no `CONTROL_ASSERT` line exists (`git grep` empty, rc 1; `pre-freeze/c1-before-token.out`); the round-97 `c2-nowork-absent` is `add("c2-nowork-absent", 0, …)` and its receipt carries outer `rc=0` while the wrapped grep returns 1 (spot-check D-2; `.ufo/evidence/round-97/pre-freeze/c2-nowork-absent.out`) | `CONTROL_ASSERT sites=15 measured=15 literal=0 unmeasured=0` exit 0; round-97 driver `sites=15 measured=14 literal=1 unmeasured=1` exit 1; `CONTROL_ASSERT_SELFTEST: 18/18 pass`; `CONTROLS98 states=18 matched=18 mismatched=0` exit 0 | `python3 -I tools/control-assertion-audit.py --repo . --rev R --driver .ufo/evidence/round-98/controls98.py`; `--driver .ufo/evidence/round-97/controls97.py`; `--selftest` | `3b7ae127` |
| C2 | at base no `GUARD_REFUSALS` line and neither `GUARD_SETUP state-unbuildable` nor `GUARD_SETUP limit-mechanism-missing` in any committed receipt (`git grep` rc 1 each; `pre-freeze/c2-before-*.out`); spot-check D-6: four classes receipted, two code-only | six `GUARD_REFUSAL <class> rc=2 token=ok` lines + `GUARD_REFUSAL_POSITIVE rows=10 rc=0` + `GUARD_REFUSALS classes=6 refused=6 wrong=0 positive=ok` exit 0; red `GUARD_REFUSALS_RED state-unbuildable observed=missed rc=0` + `classes=6 refused=5 wrong=1 positive=ok red=state-unbuildable` exit 1; selftest 9/9 | `python3 -I .ufo/evidence/round-98/refusals/guard-refusals.py --lane . --rev R --tool .ufo/evidence/round-97/c2/guard-inertia.py --tool-sha 634997d0… --work <empty dir>`; `--red state-unbuildable`; `--selftest` | `3b7ae127` |

## Sources & frontier

`SOURCES:` rows before → after: **183 → 183** (A 165 · B 14 · C 4; mined 149 · queued 23 ·
rejected 11), counting command
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`
→ exit 0 both runs (`.ufo/waves/round-98/census-before.txt`, `census-after.txt`). Rows added by
tier: **none**. Rows touched old → new: S012 `used-by`
`corpus/knowledge/oracle-anchored-survivors.md` → `… , corpus/knowledge/control-assertion-anchoring.md`
(`status` `mined`, `recheck` `90d` unchanged); the two round-97 `anchor` edits are logged old→new
in the lesson and not re-edited. Frontier rows advanced: **none** (F1 and F2 partly held; F3-F11
as before); the new entry is calibration ground with a re-opened source, not a coverage-map
ground. S012 was re-opened this round (fetch 2026-11-08, HTTP 200, 42588 B, sha256 `fb6f384d…`,
renderer line 112, 16 words; the live snapshot is byte-identical to the freeze snapshot). S009 was
re-opened with a declared UA (HTTP 200, 42254 B, sha256 `be3f85db…`, abstract at renderer line
413, 14 words) after the default-UA fetch returned the 403 challenge (5517 B, sha256
`d04c1de8…`); the row stays `queued`, no admitted entry cites it, and its opening `teaches` clause
("identical compiled output …") is not in this abstract — a correction would be a superseding row,
not this round's append. Assimilation: none (no `merge/tameshi/` package was adopted);
`considerthese/2026-11-08.md` idea 1 (frozen-tally reconciler) is not mined — every tally landed
here is bound to a receipt path (the manual form), and idea 3 is exercised only by the sentinel's
probes.

## Trend verdicts

- **expansion: unchanged** — no new knowledge ground on previously uncovered frontier; SOURCES
  183 → 183; the new entry re-grounds calibration ground with S012.
- **quality: improved** — QUALITY 177 appended with an able-to-fail receipt; two new instruments
  replace a spot-checked defect class with mechanical checks, and D-1's registry class gains a
  checker (red 2 / green 0); the wave's instrument repairs (A5-A9) turned five C1 mechanisms and
  four C2 sentences into enforced refusals.
- **discernment: improved** — the round's own wave falsified C1's classification clause through
  five mechanisms (R98R1, R98C1) and C2's pin/red/transcript sentences (R98R2, R98SN1, R98E2);
  every finding is an amendment A5-A10 with its artifact, the prefile ledger records 19 rows over
  all seven attack seats, and mistakes M5-M7 were mined from the round's own first conclusions.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  [lane assertion, no independent promotion verifier](reports/round-1-calibration.md#box-1)
- [~] At least one end-to-end domain task executed and logged in LOG.md
  [lane assertion, no independent promotion verifier](reports/round-1-calibration.md#box-2)
- [~] Instructions executable by an agent without oral context
  [lane assertion, input-keyed monitor only; no independent promotion verifier](.ufo/evidence/round-21/coldread/ledger.json)
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  [lane assertion, no independent promotion verifier](reports/round-1-calibration.md#box-4)

## Stale-lane

This is the lane's only open mission (respawn-per-round driver). Launch
`2026-11-08T12:28:49-03:00` → lane tip `2026-11-08T13:41:20-03:00` = **1 h 12 m 31 s**; **9 lane
commits** landed after the launch (`git log --oneline 034240a5..28e7bda9 | wc -l` → 9), so the
round is `progressing`, not silent. The wave sat at the dispatcher's `host-defer` gate from 12:50
to 13:12 (~22 min) because 128 leaked `while True: pass` burners held load1 ~160 against
`LOAD_MAX` 144; the orchestrator reaped them (message at 13:12) and the wave spawned at
13:12:28 (`inline-dispatcher.log`).

## Tool installs

None this round (pacman paused and unused; no `uv`/`npx` install was needed).

## Prefile falsification

`PREFILE-FALSIFICATION: pass claims=2 rows=19 attack_seats=7 findings=0`, exit 0
