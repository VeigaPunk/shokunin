# revenger — round 89 (hyaku), attempt 1 — honest stop

Lane repo `/home/vgpnk/Projects/shokunin/revenger-shokunin`; report on the
fleet repo. Base `2b017fa3c616a84b7b491e3312029fa8a8c076e6` (r88 adjudication
+ r88 non-author spot-check + the operator-authored
`considerthese/2026-11-04.md` reflection). Freeze
`c84339c051443e13f6a546cf186cc8965649a932`. Landing
`6ce41aabc3216b9d07981ea573cce70dbee93b76`. Adjudication
`bd575ca1166df8d8554eaa769ad4164c6b998675`; correction
`5f7ecce6a712f114e8ae020b26ef8712a87297f4`, then the wave-evidence completion
`b90bf377a2e510b091f2842409d3c7ecf047a4fd` (lane tip; `ls-remote` =
`b90bf37…`). **Neither claim is admitted**: C1 missed its frozen target, C2
was killed by its own kill rules. The round reports that as the outcome and
lands the work that survives its own attacks.

## Work performed

Declared claims (frozen in `reports/round-89/claims.md` at `c84339c`, before
any after-run):

- **C1 — freshness:** the 18-row host-readiness census is re-derived against
  the live host; target `CENSUS_STALE_UNFLAGGED=0`.
- **C2 — coverage (the lowest reachable criterion; K stays operator-blocked by
  the unanswered r74 L0):** an android-family record moves F4 10/11 → 11/11
  together with an identity oracle at `ORACLE OK (19/19)`.

- **C1 measured and missed.** `corpus/census_reprobe.py` (frozen, sha256
  `c3127ffc…648b`) re-derives each row from the live host. Base red
  `reports/round-89/census-red.log`: 10 findings over 10 rows, exit 1. After
  the append-only correction `reports/round-89/c1-after.log`: **2 findings
  (K04 only), exit 1**. Zero is unreachable: `K04` scores one string for two
  probes whose live states are opposite (ghidra present, ida absent), and each
  presence rule requires its own literal and forbids the other's
  (`ReviewerR89C1` D1, `CriticR89Claims` §C1). Measured floor 1 (one half in
  prose), truthful-literal 2. The cheapest cheat to 0 — `ghidra`/`ida` stubs
  on `PATH` — is measured by the critic and blocked by no frozen rule.
- **C1's own instrument was attacked and shown weaker than its docstring.**
  `ReviewerR89C1` D2: a census that asserts the *opposite* of every live fact,
  phrased with negation (`not present`, `imports? no`), prints byte-identical
  output to the honest correction. D3: rows are keyed by id across both files,
  so a corrected row in the wrong file masks the stale one. D4: the same tree
  scores 2 / 8 / 10 across shells (PATH/HOME-relative; `rea` is a per-session
  fnm shim). D7: `--selftest` has no leg on the forbidden-opposite branch and
  never calls `main`. `MutR89Census` adds four surviving one-limb mutants.
- **C2 measured, then killed.** With the producer record inside the counted
  surface the frozen counters read `F4_COVERAGE=11/11` and
  `ORACLE OK (19/19)`. Kill (a) fails: a hand-written minimal record and a
  `<manifest package="com.attacker.fabricated" …><!-- versionCode="1" -->`
  record both pass 19/19 and move F4 (`ReviewerR89C2`, `CriticR89Claims`
  §C2). Kill (c) fails: two independent producer runs differ at byte 20
  (`evidence_id`, a per-run `rea-android-XXXXXX` path, JVM map order,
  `load_duration_ms`). `MutR89Oracle` shows four of five oracle legs are
  load-bearing for one-field tampers but none binds the record to a producer
  run.
- **The rejected record is preserved, not counted.** Relocated
  byte-identically (`cmp` 3/3) to `reports/round-89/rejected-android-record/`,
  outside the `corpus/live/runs/**` surface `f_probe4.py` scans; F4 re-measured
  at **10/11** (`reports/round-89/c2-after.log`).
- **A false `holds` in this round's own new table was caught after landing.**
  `ScribeR89Rows` (stood down before the landing) ran its detector afterwards
  and found F02 `holds` against a recorded 37/170 while live is 42/207, and F05
  `holds` against a recorded pin 6.4.0 while live is 6.7.0 — exactly the class
  the round is about, in the round's own bytes. Both verdicts are corrected in
  `5f7ecce`; the frozen gate is token-neutral to the fix (still 2 findings).
  Its two K06 hits are the detector's own prose-cell limitation and are not
  applied.
- **The correction that does stand.** Both census files gain an append-only
  `## Re-verification 2026-11-04` table: eight stale rows now state live values
  (`rea` 6.7.0 on PATH, ghidra present at `/usr/bin/ghidra`, pwntools imports,
  seven reference names, `HOST-CONTRACT.md`, `rea-agents@6.7.0`, node/npm
  versions); `K04` keeps the truthful split. The earlier tables stay
  byte-identical.
- **Registration with limits.** `SKILL.md` §Gate registry gains
  `census_reprobe` (registered as an *experimental probe-as-gate*, five
  measured blind spots named) and `apk_identity_oracle` (probe: no self-test),
  plus error pattern **M43** (a marker count is not a re-verification).
  `corpus/README.md` index gains `audit_source_quotes.py` and
  `census_reprobe.py`; `self_assessment_check.py` SM2 drops 1 → 0 (SM6 still
  hardcodes a `/14` denominator against the 15-row map — routed).
- **Wave.** 12 seats in one v1 wave (band 8–16): 3 scribe, 2 executor, 1 scout,
  2 reviewer, 1 critic, 2 mutation-tester, 1 connector, 1 sentinel — 5 attack
  seats (42 %). The canonical planner seat is held by the L1 (the validator
  rejects `planner`). Two seats (`ScribeR89Rows`, `ScribeR89Registry`) stalled
  after prototyping and were stood down; the L1 executed both items and
  retained their wave dirs. One seat, `ScoutR89Host`, produced no report and
  no wave directory: it was still `running` at its last observed state ("final
  verification pass") when this report was filed, so its item is reported as
  **no output** — a stalled seat, not a dead-with-error seat (no error text was
  observed). 11 of 12 seats produced evidence. `WAVE-DONE` never arrived for
  this wave; the evidence below is enumerated from `.ufo/waves/round-89/`
  (spec, dispatch, registry, 11 seat reports).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| `corpus/census_reprobe.py` + `corpus/fixtures/apk-r65/oracle_check.py` + the frozen claims/reds/controls/instrument pins + round-start census receipts | LOG r89 bullet 1–2 | `c84339c` (freeze) |
| census re-verification tables (both files), rejected android record + ledger/receipt, SOURCES S480–S482, `corpus/lessons/round-89.md`, `reports/round-89/{carry-in,environment,c1-after,c2-after,holds}`, SKILL registry rows + M43, README index, wave evidence | LOG r89 bullets 2–5 | `6ce41aa` (landing) |
| rejected record relocated out of the counted surface; lesson final measurements; SCORECARD round-89 section; LOG round entry; holds re-measured | LOG r89 bullet 6 | `bd575ca` (adjudication) |
| two false `holds` verdicts (F02, F05) corrected to `STALE -> 42 / 207` and `STALE -> 6.7.0` after a post-landing detector found them; detector limitation recorded; mistake mined | LOG r89 bullet 6 (correction) | `5f7ecce` (correction) |

No `corpus/QUALITY.md`, `PROVINCE.md`, `corpus/knowledge` entry beyond the two
census files, or `corpus/live/runs` record from an earlier round was edited
(`git diff --stat 2b017fa3..bd575ca -- PROVINCE.md corpus/QUALITY.md` empty).

## Before → after measurements

Environment for every number: `reports/round-89/environment.log` (HOME
`/home/vgpnk`, fnm-multishell PATH; `rea`/`node`/`npm` resolve through the
per-session shim, so no count is quoted without it).

| claim | counting command | before | after | target | verdict |
|---|---|---|---|---|---|
| C1 freshness | `PYTHONUTF8=1 python3 -B corpus/census_reprobe.py --root TREE` | 10 findings / 10 rows, exit 1 (`census-red.log`, base `2b017fa3`) | 2 findings / 1 row, exit 1 (`c1-after.log`, tip `5f7ecce`) | 0 | **MISS** |
| C2 coverage | `python3 -B reports/round-81/f_probe4.py corpus` + `oracle_check.py truth.json <record>` | 10/11 (9.09) (`f4-red.log`, base) | 10/11 (9.09) landed; 11/11 + 19/19 only while the rejected record was counted (`c2-after.log`) | 11/11 + 19/19 with kill rules holding | **KILLED** |
| separability | C1-only tree / C2-only tree | — | F4 stays 10/11 / census stays 10 (`CriticR89Claims.md`) | isolated | PASS |
| no-work control | untouched base | 10, F4 10/11 | — | cannot reach either target | PASS |

## Sources & frontier

`SOURCES.md` rows **479 → 482** — counting command
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
Rows added: **3, all tier A, all `own-work`** (S480 the C1 red receipt, S481
the C2 producer receipt, S482 the oracle green receipt), appended inside the
Registry directly after S479 with 11 cells each and no `|` in any cell. Rows
touched old→new: **none** (append-only; no status/recheck/used-by edit was
needed). Frontier rows advanced: **none** — no knowledge entry was admitted
and no coverage-map row changed (C1/C2 are quality/coverage attempts, both
unadmitted). Census: round start sanctioned **exit 0** and literal **exit 0**
(this Linux host; the r74–r88 literal exit-2 lineage was the Windows layout),
round end both forms **exit 0, zero E**
(`.ufo/waves/round-89/census-round-end-{sanctioned,literal}.log`).
Mistake mined: `corpus/lessons/round-89.md` `## Mistakes` (six rows: oracle
expected-value source confusion, listing case-fold defect, self-contradicting
clean fixture, row-wide multi-tool state conflation, the helper-bypass, and the
false `holds` in the round's own new table).
Latest `considerthese/2026-11-04.md` mined: proposal 1 (report new rows split
by kind/tier and flag a zero-external window) is applied in this section —
3 rows, 3 own-work, 0 external, disclosed. **Assimilation: none** (no
`shokuknow` package adopted; nothing written outside this lane).

## Trend verdicts

- **expansion: unchanged.** No `knowledge/` entry admitted and no
  coverage-map row changed; the three new source rows are own-work evidence
  for this round's receipts, not new ground.
- **quality: improved** on the census surface, and the round says so while
  admitting its claim missed: ten stale rows were found and eight corrected
  with dated live values, append-only, with the `K04` residual disclosed;
  the android record was preserved with its rejection framing rather than
  deleted (`corpus/knowledge/*.md`, `reports/round-89/rejected-android-record/`).
- **discernment: improved.** Three false greens were found and receipted by
  the wave rather than by the author — a negated census passing identically
  (`ReviewerR89C1` D2), a fabricated and an XML-comment record passing both C2
  counters (`ReviewerR89C2`, `CriticR89Claims`), and the census's own
  environment dependence (D4) — and they are recorded as `SKILL.md` limits and
  M43. No `QUALITY.md` criterion was added (the round pre-declared that file
  unchanged); the Q17 proposal is routed to r90. Outside spot-check pending.

## SHONEN

`grep -c '^## SHONEN'` = 1; one line per box, no `[x]` (a wave seat is still
this lane).

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — §1–§4 and §6 stand; this round adds M43 and two registry rows at `6ce41aa`/`bd575ca`; no outside confirmation of the current bytes.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round-89 LOG entry: census re-probe over the real host and a real `rea inspect-android-package` run on `corpus/fixtures/apk-r65/fixture.apk` (record preserved, rejected).
- [~] Instructions executable by an agent without oral context — `SKILL.md` §6.1–§6.5 commands ran verbatim this round (gate, census, oracle); no independent outside instruction verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` byte-unchanged; the `rea` 6.7.0-vs-6.8.0 and Windows-ghidra-path drift inside it is reported here, not absorbed; ADJ-06 unchanged.

## Round notes

- **Shape:** one v1 wave, 12 seats, 5 attack seats (42 %), 1 connector; no
  residual call; round total 12. One stalled seat (`ScoutR89Host`, no output),
  two stood-down seats whose items the L1 executed, nine seats reporting. Two seats stalled and their items were
  executed by the L1 (their reports are retained; no seat wrote outside its
  declared files).
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is
  open.
- **Tool installs/upgrades:** none this round (no package-manager transaction;
  `pacman` stays paused per the addendum guard).
- **Procedural defect (disclosed, mined):** one direct `jj new` moved an empty
  working copy onto the branch tip after `jj-lane.sh` refused a non-tip base
  (a bot commit had advanced `main` past the working-copy parent). Every
  commit and push still went through the helpers; the deviation is recorded in
  `reports/round-89/carry-in.md` and `corpus/lessons/round-89.md` `## Mistakes`.
- **Open L0:** none added; the r74 K L0 stays unanswered and routed around.

## Erratum (appended after filing; supersedes one sentence above, names it)

The sentence **"One seat, `ScoutR89Host`, produced no report and no wave
directory: it was still `running` at its last observed state … so its item is
reported as **no output** — a stalled seat, not a dead-with-error seat (no error
text was observed). 11 of 12 seats produced evidence."** is superseded: the
seat landed its report after this report was filed, at
`.ufo/waves/round-89/w1/ScoutR89Host.md` (+ receipts dir), committed in the lane
at `7f840eb6fac82e974ab5cda28858fb35177233d9` (lane tip; `ls-remote` =
`7f840eb…`). **12 of 12 seats produced evidence; no seat died and none stalled
without output.** The seat's independent probe table corroborates the red
(rea 6.7.0 on PATH, ghidra present, ida absent, pwntools imports, seven
reference names, two top-level `*.md` entries, SKILL.md 42/207, skill pin
`rea-agents@6.7.0`) and adds one fact this report did not state: `npm view
rea-agents version` returns `6.8.0` (registry latest), which is the publisher's
version and not the skill's pin — the census row's probe is the pin, so F05's
`STALE -> 6.7.0` verdict stands. No claim verdict changes: C1 is still a MISS
at 2 findings and C2 is still killed.

## Erratum 2 (appended after filing; supersedes one sentence above, names it)

The sentence **"Kill (a) fails: a hand-written minimal record and a
`<manifest package="com.attacker.fabricated" …><!-- versionCode="1" -->`
record both pass 19/19 and move F4"** is superseded by `ReviewerR89C2`'s
measured precision (receipts under `.ufo/waves/round-89/w1/ReviewerR89C2/receipts/`;
lane erratum at `e0fbf2ea88ce8855f29259fa33265379b712e13b`, lane tip;
`ls-remote` = `e0fbf2e…`). A *minimal* 3-key record (`evidence_id`,
`operation`, `normalized_result: {}`) moves F4 to 11/11 but the oracle
**rejects it at 6/19**. What passes `ORACLE OK (19/19)` **and** moves F4 is
(i) a hand-written record that is fully accurate against the fixture — which
falsifies only the "cannot be a fabrication" limb, at the Q09
non-provenance boundary — and (ii) a real producer record whose
`manifest.text` is contradicted by `package="com.attacker.fabricated"` with
the expected fragments hidden in an XML comment. A third variant
(co-editing `truth.json` `axml_declared` together with the record) passes
19/19 but is a sourcing demonstration, not a fixed-truth falsifier. Kill (a)
therefore rests on (i) and (ii). No verdict changes: C2 is still **KILLED**,
on kill (a) as restated and on kill (c) (two producer runs differ at byte 20).
