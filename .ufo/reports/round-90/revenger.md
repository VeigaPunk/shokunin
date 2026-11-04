# revenger — round 90 (hyaku run 15), attempt 1

Lane repo `/home/vgpnk/Projects/shokunin/revenger-shokunin`; report on the
fleet repo. Base `77574c99845ab6662812bd6a88def1e72bf8d71b` (r89 adjudication
+ r89 non-author spot-check). Freeze `c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9`.
Landing `abd1394bc612b224381fba29b7b2175a88a108a7`. Adjudication
`5bdcd5a628c4063dabf0dc3858ecd41df46d1760`. Wave-evidence completion
`b280719903dee7c3d957da8b1cd7315655511e3d` = lane tip (`git ls-remote origin
refs/heads/main` → `b280719903dee7c3d957da8b1cd7315655511e3d`).
**Outcome:** C1 meets its frozen counter, but the critic disputes its axis
label and points to a blind spot on real rows. C2 meets its frozen predicate
but is **not verified**: two controls that skip the claimed work also reach
the target.

## Work performed

Declared claims (frozen in `reports/round-90/claims.md` at `c7767789`, before
any candidate score):

- **C1 — calibration (the self-assessment gate):** SM6 v2
  (`corpus/self_assessment_check2.py`) judges the lane's K statement by both
  numerator and denominator. Counter: the frozen 14-case battery
  `reports/round-90/sm6_battery.py`. Red: v1 `SM6_MISCLASS=7/14`. Target:
  0/14.
- **C2 — coverage (lowest non-retired axis; K stays operator-blocked, L0 r74):**
  the F4 android family gets a current-producer record. Counter:
  `reports/round-90/c2_counter.py`, six conjuncts: F4 11/11, oracle v2
  accepts the record, oracle v2 misjudges 0/9 frozen forgery cases,
  `norm_eq` holds between the two runs, the receipt digests match, and the
  evidence ids are distinct. Red: F4 10/11, oracle v1 5/9.

Work items:

- Pre-freeze reds and instruments, all committed in the freeze `c7767789`:
  `reports/round-90/c1-red-v1-battery.log` (7/14),
  `c1-red-v1-selfmismatch.log` (SM6=1 on a TRUE statement),
  `c1-real-label.log` (15 map rows, 8 held), `c2-red-v1-battery.log` (5/9),
  `c2-red-f4.log` (10/11), `norm-eq-selftest.log` (pass), and
  `instrument-pins.log`.
- Post-freeze controls, run before any producer run:
  `reports/round-90/c2-control-norecord.log` (1/6) and
  `c2-control-copy89.log` (5/6, K6 fails).
- Producer runs by seat `ExecR90Producer`:
  `rea inspect-android-package corpus/fixtures/apk-r65/fixture.apk --format json`
  ran twice. Both runs exited 0. Their stdout sha256 values are `9d665ffb…`
  and `214094fb…`, and `NORM_EQ=identical`
  (`.ufo/waves/round-90/w1/ExecR90Producer/report.md`). The record landed
  as run1's exact stdout at `corpus/live/runs/round-90/inspection.json`
  (`abd1394`), with `LEDGER.md`. Run2, the receipt and the env pin are under
  `reports/round-90/`. Seat `SentinelR90` returned `LAND_OK: yes` (low class
  only).
- After-runs over `git archive abd1394`:
  `reports/round-90/c1-after-v2-battery.log` (v2 0/14, v1 control 7/14, v2
  self-test OK, v2 `SELF_MISMATCH=0`) and `reports/round-90/c2-after.log`
  (`C2_CONJUNCTS=6/6`, freeze pins `PINS_EXIT=0`, ids consistent,
  `SOURCE_PATH_DEAD=0`). The holds are in `reports/round-90/holds.log`.
- Attacks, with their verdicts recorded as given:
  - `CriticR90Claims` (`.ufo/waves/round-90/w1/CriticR90Claims/report.md`).
    C2 reaches 6/6 with an id-edited copy of the r89 record and with
    stubbed in-tree instruments (`receipts/c2-controls.log`). C1's target was
    already met at the freeze. The critic calls C1 gate fidelity, not
    self-assessment accuracy, and shows a real-format blind spot
    (`receipts/c1-realformat-counterexample.log`).
  - `ForgeryR90Probe`: oracle v2 accepts 12 of its 40 new forgeries.
  - `MutR90SM6`: 4 of 11 mutants survive the battery.
  - `MutR90Oracle`: O1, O2 and O8 survive the battery.
  - `ReviewerR90C1`: C1 holds on the frozen predicate; 8 of 21 out-of-battery
    shapes are false greens.
  - `ReviewerR90C2`: C2 holds as frozen; "satisfiable with no producer run
    (MEDIUM)".
  - `ExecR90Replay`: an independent re-implementation of both truth rules
    disagrees 0/9 and 0/14.
  - `ScoutR90Producer`: `evidence_id` is a content digest (`computeEvidenceId`),
    and there are no volatile fields beyond V1–V4.
  - `ConnectorR90` (`.ufo/waves/round-90/w1/ConnectorR90/report.md`): no
    sibling duplicates. It names three complementary overlaps the next round
    should cite: kaidoku's jadx per-run ids (→ norm_eq V1/V2/V4), kake's
    `_has_doctype` (→ the v3 DOCTYPE leg), and kaidoku's r65/r66 population
    drop. The last one shows SM6 v2 is blind to a malformed 16th map row,
    which is another out-of-battery C1 limit.
- Unclaimed post-freeze corroboration and correction, landed in `abd1394`:
  - `corpus/fixtures/apk-r65/oracle_check3.py`. It matches exact expanded
    names, refuses any DOCTYPE and adds two adjacent legs. False greens on
    the 40 probe cases drop from 12 to 0, and frozen battery misses are 0/9
    (`reports/round-90/oracle{2,3}-vs-forgery-probe.log`,
    `oracle3-battery.log`). v3 was fitted after reading the cases, so this
    result is not held out.
  - `reports/round-90/verify_evidence_id.mjs` calls rea's own
    `parseEvidence`. Both landed runs are `ID_CONSISTENT`, and the id-edited
    control is `REJECTED … identifier does not match its record`
    (`reports/round-90/c2-evidence-id-check.log`).
- r89 routed defects:
  - D1: S486 supersedes S481, and the checklist gets an appended correction.
    The relocation-sweep rule is new QUALITY Q17, and its machine check
    `reports/round-90/source_path_check.py` (seat `ExecR90SourceCheck`) goes
    from red 1 to 0.
  - D2: the lesson Gate now carries the source table inline.
  - D3: the SM2 receipt is `reports/round-90/d3-sm2-receipt.log`.
  - D4 (census env pin) is not worked this round. It stays routed.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| claims, v2 SM checker, oracle v2, norm_eq, both batteries + case bytes, c2_counter, reds, instrument pins, round-start census | `LOG.md` "## Round 90 (hyaku)" — Freeze bullet | `c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9` |
| android record + LEDGER, run2/receipt/env, controls, S483–S487, Q17, README index (SM v2, Q01–Q17), checklist correction, oracle v3, id check, source_path_check, SKILL.md registry rows, lesson, wave evidence | same entry — Wave and Landing bullets | `abd1394bc612b224381fba29b7b2175a88a108a7` |
| after-runs, SCORECARD r90 section, LOG entry, lesson final measurements | same entry — After and Mistakes bullets | `5bdcd5a628c4063dabf0dc3858ecd41df46d1760` |
| late wave evidence (ConnectorR90 report, `w1-results.json`) and round-end census receipt | same entry (Wave bullet) | `b280719903dee7c3d957da8b1cd7315655511e3d` |

## Before → after measurements

| claim | counting command | before (commit) | after (commit) | verdict |
|---|---|---|---|---|
| C1 | `python3 -B reports/round-90/sm6_battery.py --impl <checker> --real <git archive REV corpus SHONEN.md SCORECARD.md SKILL.md>` | `SM6_MISCLASS=7/14` (v1, `77574c9`) | `SM6_MISCLASS=0/14` (v2, `abd1394`); v2 `SELF_MISMATCH=0` | **MET on the frozen counter; admission contested**: the target was fixed at the freeze, the axis label is disputed (gate fidelity), and v2 reads the K row's pointer cell rather than its stated cell (CriticR90Claims). v1 flagged every `/15` statement, true or false. The closure rules on harm |
| C2 | `python3 -B reports/round-90/c2_counter.py --tree <git archive REV>` | `C2_CONJUNCTS=1/6` (no-record control at `c7767789`); F4 `10/11` (`77574c9`) | `C2_CONJUNCTS=6/6`, F4 `11/11` (`abd1394`) | **NOT VERIFIED (self-ruled; §9)**: the id-edited and stub controls also reach 6/6. The record is real producer output, and the unclaimed id check backs that, but the frozen counter cannot show it |

## Sources & frontier

`SOURCES.md` rows went from **482 to 487**, counted with
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.

- **Rows added by tier and kind.** Tier A: 3 external `docs` rows and 1
  `own-work` row (S486, which supersedes S481). Tier C: 1 `community` row,
  **rejected** (S487). The external rows are S483 (Android `<manifest>`
  reference), S484 (Python ElementTree docs) and S485 (Android versioning).
- **Rows touched old→new:** none. S481 is byte-unchanged and superseded
  through the `teaches` cell of S486.
- **Frontier rows advanced:** none. The F4 android surface carries a record,
  but the claim is unverified and no coverage-map row changed.
- **Census.** Round start: literal **exit 0**
  (`.ufo/waves/round-90/census-round-start-literal.log`). Round end: literal
  **exit 0**, 21 W01 + 10 W04, 0 E
  (`.ufo/waves/round-90/census-round-end-literal.log`).
- **Sourced claim.** C2's v2/v3 manifest legs rest on S483/S484, opened this
  round. The quotes were re-checked by the L1 against the fetched bytes; the
  lesson `## Gate` table holds them.
- **Mistakes mined.** `corpus/lessons/round-90.md` `## Mistakes`: D1–D3 from
  the r89 spot-check; S486's own dead path, caught by Q17's check; oracle
  local-name matching (M-a); the §9 control that was named but not built
  (M-b); the C1 battery's format gap (M-c).
- **considerthese.** Proposal 1 from `2026-11-04.md` is applied: the 5 rows
  split as 3 external, 1 own-work and 1 rejected community row, so external
  additions are non-zero.
- **Assimilation: none.**

## Trend verdicts

- **expansion: improved** (narrowly). Three external tier-A rows ground a new
  oracle discipline: root-manifest semantics and the parser's
  comment/DOCTYPE handling, including the internal-DTD default trap. The F4
  android surface also gains a real producer record. No knowledge entry or
  coverage-map row was admitted, so the closure may grade this `unchanged`.
- **quality: improved.** All four r89 routed defects D1–D3 are fixed with
  receipts, and D1 has a machine check that is shown able to fail (it caught
  S486). Oracle v2's false greens are measured and recorded as limits in
  `SKILL.md`, not hidden. Errors are corrected by supersession, never by
  rewrite.
- **discernment: improved.** The critic's §9 finding refuses C2 instead of
  admitting it. Q17 is a new `QUALITY.md` criterion grounded in the r89
  spot-check disagreement. S487 is a reject with a reason and a flip
  condition. The outside spot-check is still pending.

## SHONEN

`grep -c '^## SHONEN'` = 1; one line per box; there is no `[x]`, because a
wave seat still belongs to this lane.

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the §Gate registry gains `self_assessment_check2`, `apk_identity_oracle2` (with its measured 12/40 limit), `apk_identity_oracle3` and `source_path_check` at `abd1394`; no outside confirmation of the current bytes.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round-90 LOG entry: a real `rea inspect-android-package` producer run, twice, on `corpus/fixtures/apk-r65/fixture.apk`, landed byte-exact at `corpus/live/runs/round-90/inspection.json`.
- [~] Instructions executable by an agent without oral context — every counting command in `reports/round-90/claims.md` was re-run verbatim by seats (`ReviewerR90C1`, `ReviewerR90C2`, `ExecR90Replay`) with the same outputs; no outside instruction verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` byte-unchanged (`git diff --stat 77574c9 abd1394 -- PROVINCE.md` empty); the rea 6.7.0-vs-6.8.0 drift is still only reported.

## Round notes

- **Shape:** one v1 wave of 14 seats. All 14 seats settled and reported;
  **dead seats: 0** (`.ufo/waves/round-90/w1-results.json`, which notes an
  orchestrator kernel restart mid-wave with outputs delivered). Roles: 3 executors, 2 scribes, 1
  scout, 2 reviewers, 1 critic, 2 mutation-testers, 1 revenger-role
  forgery probe (the validator rejects `labrat`), 1 connector and 1
  sentinel. There were 5 attack seats (36 %); counting the forgery probe,
  6 attack seats (43 %). No residual call; round total 14. The L1 holds the
  §3 planner seat.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is
  open.
- **Tool installs/upgrades:** none (no package-manager transaction; pacman
  stays paused).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain`
  shows one untracked fleet-root file, `after`. It is 24 bytes, dated
  2026-11-03, and does not name this lane or round, so it is not this lane's
  misroot and was left untouched. No seat wrote into the fleet root.
- **Open L0:** none added; r74 (K) stays unanswered and routed around.
