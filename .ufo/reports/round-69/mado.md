# mado — round 69 report

Lane `mado-shokunin`, round 69, hyaku run 15, attempt 1. In-session L1 `MadoR69`.
Base `04093b83f73a841117d3b31dbb2a6063f4f2a454`; freeze `789a87f1a667b43dd759222a2f048bf8f75b43ce`;
measured content `759c9d7b0d81ed0d6457b0b83e5f7e05b46abe3d`; final re-measurement at the records tip
`139f4801bf729e27c6f5599c37a7c84b30a18758`; lane tip `9d91f7f6f5c603bdc19cf455ce6f413c5990d744`
(`git ls-remote origin refs/heads/master` printed that hash).

## Work performed

Round 69 declares **two claims**, each on a distinct axis, each with a finite frozen denominator
and a committed do-nothing control that misses the target:

- **C1 — calibration:** the hardened control harness kills *paired* (decision + oracle) forgeries.
- **C2 — operability:** the guard census requires the guard key in key position **and** requires
  the guarded environment to reach a `git` launch (dominance), not merely to occur in the file.

Work items (evidence pointer after each):

- Load order and prior state: read the round contract, MISSION/AXES, the lane SKILL/PROVINCE/
  SCORECARD/corpus frontier and the r68 lesson + verifier spot-check before declaring
  (`corpus/lessons/round-68-verifier-spotcheck.md`, `corpus/lessons/round-68.md`). The lane was
  clean at the base (`tracked=0 untracked=0`, `ahead=0`), so nothing was inherited.
- Froze both claims, the eleven-case control set, the three recipe texts and both do-nothing
  baselines before any candidate data — `789a87f1`
  (`.ufo/waves/round-69/claims-declaration-r69.md`,
  `controls/c2-controls-r69.json` sha256 `975ca3ba…f90b9`, `control-baseline-r69.txt`, `proto/`).
- Built and landed the two counters and the harness successor — `5fc29ae7`
  (`quality/counters/c1-r69-landing-controls.py`, `c1-r69-paired-recipes.py`,
  `c2-r69-guard-dominance.py`); first measurement and harm watch — `6a5cefd2`.
- Dispatched **one v1 wave of 12 seats** (spec `98bff016`, validated dispatch
  `.ufo/waves/round-69/w1-dispatch.json` `spawn=12`; seats and results under
  `.ufo/waves/round-69/w1/`, settlement `w1-results.json`).
- Closed the C2 reviewer's six bounded defects against the frozen sentence — `6d21f535`
  (receipt `c2-classifier-repair-r69.txt`: pre-fix 7 violations → post-fix 8/8 cases; frozen
  controls and the 20/13/13 population unchanged; selftest 40/40 with the cases pinned).
- Closed the C1 reviewer's S1–S5 — `296ed0d7` (base harness required and its absence a setup
  error; `py_compile` gate before any kill; `OSError`/`SubprocessError` → rc 2 with a reason;
  the seat's harness draft `9461a059…` adopted, `r69-c1` scratch dirs, round-69 limits paragraph;
  selftest 27/27).
- Landed the sourced knowledge entry, registry row S438, the lesson, QUALITY 111, the index row
  and Frontier bullet, PROVINCE and SKILL gate rows, the tool-ledger rows, the SCORECARD section
  and the LOG entry — `5864b00d`; criterion-107 single-line locator pins — `3cd68aa3`; registry
  `used-by` cells for S436/S437 and the lesson's old→new log — `fc0387b9`.
- Closed the mutation battery's only survivor (base-rev-ignoring mutant) by separating the
  scripted revisions — `e0e1831a`; pinned the population regex in the C2 selftest — `932bc932`;
  named the out-of-population guard sites with cites — `bba64c3a`.
- Closed the critic's B2 (base-leg applicability now enforced) and B3 (two dominance regression
  cases in the counter's own selftest; the dominance mutant now dies 39/41), applied the
  B8/B9/B11 corrections append-only, disclosed B1/B4/B5/B6/B7/B10 — `759c9d7b`, receipt
  `critic-closures-r69.txt`, dispositions in `SCORECARD.md` § Closure corrections.
- Harm watch and gates at the tip — `4a9482bb`, `1f26080d`, `landing-final-r69.txt`: landing
  counters GREEN (`nav=0 usedby=0 ledger=0 citecheck=0`); index 81/81; ledger 116/116; used-by
  `missing=0`; criterion 107 `rows=8 covered=8 miss=0`; gate `MADO_SELFTEST: 460/460`; axis table
  3/3 MATCH; census exit 0 at 375 rows; cross-set check that the r69 rule scores 11/11 on the
  round-68 control set too (`cross-set-r69.txt`).
- Wave evidence committed — `3b2756e4` (12 seat reports, `w1-results.json`, dispatch markers);
  superseded draft removed — `9d91f7f6`.
- Frontier step: census exit 0 at start (374 rows) and end (375 rows); one new `A/docs/mined`
  row S438; one mistake mined with class/evidence/captured-by/fix; C2's claim rests on S438.
- Curation: `considerthese/2026-10-28.md` proposal 4 (a live-tool table) was read and is **not**
  adopted this round; **Assimilation: none** (no `merge/mado/` theme was taken).
- Tooling: nothing installed or upgraded; no pacman transaction (host pause respected).

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Frozen claims, control set, recipes, do-nothing baselines | round-69 bullets 1–2 | `789a87f1a667b43dd759222a2f048bf8f75b43ce` |
| Wave spec and validated dispatch (12 seats) | bullet 3 | `98bff016d0ef151aceedf03d75239b81c9f6eeed` |
| `c1-r69-landing-controls.py`, `c1-r69-paired-recipes.py`, `c2-r69-guard-dominance.py` | bullet 4 | `5fc29ae72e66b9347d576c796ee656aea2fdd04c` |
| Claim measurements, harm watch, census start, ready file | bullets 4–5 | `6a5cefd252c41c7ff71217da65126fc831f8bc34` |
| C2 classifier repair (six review findings) + receipt | bullet 5 | `6d21f535492f74dfef538eecb303486a1588c1be` |
| C1 instrument repairs (S1–S5) | bullet 5 | `296ed0d75e361387908cf2dd418d3677f49f94c8` |
| Entry, S438, lesson, QUALITY 111, index/frontier, PROVINCE, SKILL, ledger, SCORECARD, LOG, measurement | bullets 6–7 | `5864b00da73631cad2b9f719c4ea9c9a8eaca509` |
| Criterion-107 locator cells to single line pins | bullet 7 | `3cd68aa33fa9986a02614922370b714413d0dcdc` |
| Registry `used-by` for S436/S437 + lesson old→new log | bullet 7 | `fc0387b970e602e4588bbf07f95675f88678094b` |
| Scripted revisions separated (mutation survivor closed) | bullet 8 | `e0e1831aed0b5b983957d2eb1aae4e0f1ebcd630` |
| C2 selftest pins the population regex | bullet 8 | `932bc932c577942fcd908c2dde4e1c6716ba3a7e` |
| Entry limits name the out-of-population sites with cites | bullet 8 | `bba64c3aa5cb78d4b9becf6bd73d75dca5e8c4b2` |
| Critic closures B2/B3 + dispositions, corrections, final content | bullet 9 | `759c9d7b0d81ed0d6457b0b83e5f7e05b46abe3d` |
| Records finalized at the measured content | bullet 9 | `139f4801bf729e27c6f5599c37a7c84b30a18758` |
| Final measurement receipt | bullet 9 | `4a9482bbc390ba7ad4d1fa5fd77ba3622120dd36` |
| Landing + gate receipt | bullet 9 | `1f26080d055539c192390bfd8bc17686f71c2d2b` |
| Wave w1 seat reports, results, dispatch evidence | bullet 10 | `3b2756e44515a020eec716845d0c1ec3fabeba3e` |
| Superseded report draft removed | bullet 10 | `9d91f7f6f5c603bdc19cf455ce6f413c5990d744` |

## Before → after measurements

**C1 — calibration.** Counting command (frozen at the declaration):

```sh
python3 quality/counters/c1-r69-paired-recipes.py --repo . --rev <rev> \
  --base-rev 04093b83f73a841117d3b31dbb2a6063f4f2a454 --scratch-root <scratch>
```

- **Before**, at the base revision (`04093b83`): `selftest=absent killed=0/3 applied=0/3 base=0/3
  verdict=TARGET_MISSED` rc 1 — the harness does not exist there, and the do-nothing control (the
  r68 harness under the same three recipes) survives all three (`killed=0/3 applied=3/3`, green
  52/52). Bounded `10 × killed / 3` = 0.0000.
- **After**, at the measured content `759c9d7b` and again at the records tip `139f4801`:
  `selftest=0 killed=3/3 applied=3/3 base=0/3 verdict=TARGET_MET` rc 0; bounded 10.0000.
  Receipt `.ufo/waves/round-69/measurement-final-r69.txt`.

**C2 — operability.** Counting command (frozen at the declaration):

```sh
python3 quality/counters/c2-r69-guard-dominance.py --repo . --rev <rev> \
  --base-rev 04093b83f73a841117d3b31dbb2a6063f4f2a454 \
  --controls .ufo/waves/round-69/controls/c2-controls-r69.json --scratch-root <scratch>
```

- **Before:** the counter does not exist at the base revision, and the *held rule* — the round-68
  classifier on the same frozen eleven cases — scores `controls=7/11` (it accepts
  `value-position-only`, `dead-branch-only`, `uncalled-helper`, `overwritten-env`). Receipt
  `.ufo/waves/round-69/control-baseline-r69.txt`. Bounded discrimination `10 × controls / 11` =
  7.0000.
- **After**, at `759c9d7b` and `139f4801`: `population=20 readers=13 guarded=13 unguarded=0
  controls=11/11 base_controls=7/11 verdict=TARGET_MET` rc 0; bounded 10.0000. The population
  fraction `10 × guarded / readers` is 10.0000 at both ends and is harm-watch only, not the move
  (critic B11): the round moves *discrimination*, and the counter prints the held rule's 7/11 in
  the same line. Receipt `.ufo/waves/round-69/measurement-final-r69.txt`.

No claim was narrowed after data, and no frozen predicate was changed. Instrument defects found by
the attack seats were repaired *before* landing with red-before receipts: C2 six bounded
violations (`c2-classifier-repair-r69.txt`), C1 S1–S5 (`w1/R69RevC1.md`), and critic B2/B3
(`critic-closures-r69.txt`).

## Sources & frontier

- Counting command, run at both ends:
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`
  — start: `mado ok`, exit 0, **374** data rows (`census-start-r69.txt`); end: `mado ok`, exit 0,
  **375** data rows (same command at the final tip).
- Rows added: **1** — **S438**, tier `A`, kind `docs`, status `mined` (git v2.56.0
  `Documentation/git.adoc`; three fetches byte-identical, sha256 `050c5330…f79`, 47005 B;
  anchors `git.adoc:14,178-182,927-929`). Rows added by tier: A +1, B +0, C +0.
- Rows touched old→new (logged in `corpus/lessons/round-69.md` § Gate, append-only):
  S436 `used-by` and S437 `used-by` each gain `corpus/knowledge/gate-guard-dominance-r69.md`;
  no `status` and no `recheck` cell changed.
- Frontier rows advanced: one `corpus/README.md` Frontier bullet and one index row for
  `corpus/knowledge/gate-guard-dominance-r69.md`; navigation 80/80 → 81/81 (published in
  `SCORECARD.md`, gate 3/3 MATCH).
- Sourced claim: **C2** rests on S438 (its entry cites it with locators; criterion 107
  `rows=8 covered=8 miss=0 verdict=OK`). The lesson `## Gate` carries one admit (S438, URL, access
  date, a ≤25-word located quote) and one reject (`git-replace.adoc` as a new row — duplicate
  scope with held S436; flip condition recorded).
- Assimilation: **none** this round (no `merge/mado/` theme taken; `considerthese/2026-10-28.md`
  proposal 4 read and not adopted).

## Trend verdicts

| Trend | Verdict | Evidence |
|---|---|---|
| expansion | unchanged | No new province ground: the round is instrument craft over the lane's own gates. One technical source opened (S438) and one lane-tooling entry added; the desktop/compositor axis gains no surface this round. |
| quality | improved | Two new measured instruments with frozen do-nothing controls (0/3 and 7/11); eleven instrument defects caught by the attack seats and repaired before landing with red-before receipts; QUALITY 111 added; the r69 rule scores 11/11 on the round-68 control set too (`cross-set-r69.txt`). |
| discernment | improved | The round mines its predecessor's equivalent-mutant misclassification (M69-1) and the round-68 classifier's value-position over-inclusion (M69-2), excludes the equivalent recipe from the frozen denominator with a probe, and records eleven critic blockers with dispositions instead of smoothing them (three corrections, six disclosures, one limit). |

## Lane state

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open, and this report
  closes round 69 only.
- **Round shape:** one v1 wave, 12 seats validated under `scripts/hyaku/ufo-wave-policy.json`
  (band 8–16), dispatched as one `task` call by the orchestrator from
  `.ufo/waves/round-69/w1.ready`; residual call: none; round total: 12.
- **Seats:** executor 4, scribe 2, scout 1, connector 1, reviewer 2, critic 1, mutation-tester 1;
  attack seats 4/12 = 33 % (reviewer ×2, critic, mutation-tester); connector seats 1 (≤2).
  The L1 holds the planner seat (the validator rejects a planner role).
- **Settlement:** `w1-results.json` — 12 dispatched, 12 settled, **no dead seats**.
- **Chronology:** freeze commit 22:42:47-03:00 < ready file 22:44:47 < dispatch marker 22:47:43.
  `check-freeze-order.py` reads `reason=no_freeze` for both r68 and r69 because its FREEZE set
  expects `claims-frozen.md`/`registration.md`; the lane has used `claims-declaration-rN.md` since
  the r56 era. Disclosed, pre-existing.
- **Gates at the tip** (`landing-final-r69.txt`): landing GREEN, index 81/81, ledger 116/116,
  used-by `missing=0`, criterion 107 OK, gate 460/460, axis 3/3 MATCH, census exit 0.
  Pre-existing red, reported not smoothed: `check-deliverables.py` on the round-68 seat reports
  (`reports=6 declared=4 exists=1 absent=3 undeclared=5`), reproduced at the base by the cadence
  seat on the full twelve.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` (no pathspec) shows
  `.ufo/reports/round-69/mado.md` (this report), orchestrator-owned `.scratch/*`, and one 24-byte
  fleet-root file `after` dated 20:05-03:00 (before this round's launch, no mado/round-69 content);
  no file written by this round's seats is at the fleet root, so nothing was copied or deleted.
- **Tool installs:** none this round (no `uv`, `npm`, `cargo`, binary or pacman transaction); the
  host pacman pause was respected.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — historical assertion `corpus/knowledge/executor-test-sufficiency.md`; round 69 adds two pinned gate rows, but no outside-lane promotion authority is claimed.
- [~] At least one end-to-end domain task executed and logged in LOG.md — historical assertion round 3; round 69's end-to-end task is the two frozen counting commands run green at `759c9d7b`/`139f4801` and the landing battery at `4a9482bb`.
- [~] Instructions executable by an agent without oral context — the two new gate rows carry entry command, verdict map, selftest spelling and pinned path; the declaration, lesson and receipts are self-contained; dispatched subagents still do not satisfy the outside-lane rule.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md carries the round-69 paragraph and names the instruments as lane record tools; no outside-lane adjudication in this round.
