# mado — round 45 report (hyaku run 9, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/mado-shokunin`, branch `master`, final lane hash **`4d22eeb66c2835af8aaa3fac6ad838fa616aa663`** (`git ls-remote origin refs/heads/master` prints it). Base `0c89478af821a6424c9ac922eafe02e39630cf4f`. Round shape: **one v1 wave run** — `w1` 41 seats (build + first falsifiers; executor 13, scribe 7, critic 6, reviewer 4, scout 3, connector 3, mutation-tester 2, sentinel 1, simplifier 1, revenger 1; m_flash roles 29/41, attack roles 12/41); dead seats **0** (41 reports in `.ufo/waves/round-45/w1/`; `w1-results.json` records 41 settled with outputs not retained after an orchestrator kernel restart). The planned falsification wave `w2` was **not run**: the run's request budget ended the round after integration. **Round total 41 seats — below the 64-seat floor of the run-9 directive; a conformance defect, reported as such.** No residual call. The L1 (`MadoR45`) held the planner seat.

## Work performed

Declared claims (`.ufo/waves/round-45/registration.md`, freeze `22a8dedd02f507689c567777e0f20b5e645c8ce0`; both re-registered before any data in `registration-v2.md`, freeze `7c0b00350d70f6e5d3b0259a132d25ee030d525e`):
- **C1 — operability (capability acquisition): `tools/mado-monitors.py`**, the read-only join of `monitor =` rules with `hyprctl monitors all -j`, judged by `PRED-C1-r45-v2`.
- **C2 — coverage (sourced): `corpus/knowledge/hyprland-monitor-rule-r45.md`**, the monitor-rule chain at Hyprland 0.56.2 (U5 runtime state agreement), judged by `PRED-C2-r45-v2`.

Lowest-axis rule: every published axis tied at its maximum at base (`receipts/axis-base.txt`, `checked=3 mismatched=0`). Paths below are under `mado-shokunin/.ufo/waves/round-45/`.

- Pins fetched and opened 2026-10-26: nine at v1, five more at v2 (`fetch/`, `receipts/fetch-sha256.txt`).
- v1 freeze with controls (`receipts/ctl-c1.txt` 0 of 16 met; `receipts/ctl-c2.txt` P admitted, 9 rejected).
- w1 broke both v1 predicates before data: 11 cheats + 5 do-nothing controls met C1 (`w1/CritC1Cheat.md`, `w1/ExecDoNothingC1.md`); 9 forgeries met C2 (`w1/CritC2Forgery.md`); six contract errors against Hyprland (`w1/CritToolSemantics.md`, `w1/ExecParseOracle.md`, `w1/RevTool.md`, `w1/CritEntryContent.md`); one critic finding refuted (float32 integrality; Vector2D is double, `w1/ExecScaleOracle.md` 0 divergences in 445,875 cases).
- v2 freeze: C1 adds 32 fixtures (81), three runs per fixture (seed 45 / environment B / nonce), bubblewrap isolation, 150 nonce-generated cases judged by the pinned v2 reference; C2 adds T1-T5, 5 pins, 7 surfaces. Controls: `receipts/ctl-c1-v2.txt` `CTL_C1v2 VERDICT: PASS (controls scoring TARGET_MET: 0 of 45; reference met: 1)`; `receipts/ctl-c2-v2.txt` `CTL_C2v2 VERDICT: PASS (wrong=0 of 15; positive admitted=1)`.
- Independent rebuilds met C1 v1 from the contract text (`w1/ExecIndepA.md`, `w1/ExecIndepB.md`); separability shown both ways (`w1/ConnCrossClaim.md`).
- Round-44 closure D1: both live-title dumps projected (`.ufo/waves/round-43/...`, from `w1/ExecProjectTitles`); considerthese `2026-10-26.md` proposal 1 → `quality/check-session-material.py` + QUALITY 85.

## Landed changes

| Commit | Change | LOG.md Round 45 bullet |
|---|---|---|
| `22a8dedd02f507689c567777e0f20b5e645c8ce0` | v1 freeze: registration, counters, reference, draft, controls, pins, before receipts | 2 |
| `ebdba13f7cb16d454763003d424398eec3bb2788` | w1 spec/dispatch (41 seats), C2 v1 controls receipt | 3 |
| `7c0b00350d70f6e5d3b0259a132d25ee030d525e` | v2 freeze before data + w1 evidence (41 reports; seat files carrying the host monitor serial redacted, lesson M45-2) | 4 |
| `ee6659b90f7bf69aa03283dba804dd90081b7ff5` | **data**: tool, entry, rows S302-S315, lesson, README row + Frontier, SKILL/PROVINCE rows, QUALITY 85-86, privacy gate, D1 projections, live receipt, census after | 5 |
| `ac3f9dee1af417652fcd3705a729e1dcd93fcf20` | SCORECARD/LOG Round 45, after-data receipts | 5 |
| `4d22eeb66c2835af8aaa3fac6ad838fa616aa663` | v2 control receipts, tip axis receipt | 4 |

Inherited state: none (tree clean at start). Left untracked: `w1/MutC1Counter/results.json` (4 MB, skipped by the helper's size rule; its `summary.txt`/`matrix.md` are committed).

## Before → after measurements

- **C1** — `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/counters/c1-r45-monitors-v2.py --repo . --rev <rev> --work <scratch>`: base `0c89478` `fixtures=0/81 generated=0/150 selftest=fail readonly=fail tool=absent verdict=TARGET_MISSED`, exit 1 (`receipts/c1-v2-before-base.txt`) → data `ee6659b` `fixtures=81/81 generated=150/150 selftest=ok readonly=ok tool=present verdict=TARGET_MET`, exit 0 (`receipts/c1-after-data.txt`). Self-verdict **TARGET_MET**.
- **C2** — `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/counters/c2-r45-monitor-entry-v2.py --repo . --rev <rev>`: base `admitted=0/1 verdict=TARGET_MISSED`, exit 1 (`receipts/c2-v2-before-base.txt`) → data `ee6659b` `admitted=1/1 verdict=TARGET_MET`, exit 0 (`receipts/c2-after-data.txt`). Self-verdict **TARGET_MET**.
- Harm watch: `python3 -I quality/check-axis-scores.py --rev ac3f9de… --repo .` → `MADO_AXIS: checked=3 mismatched=0` (navigation 62/62, calibration 73/73, operability 12/12; `receipts/axis-tip.txt`); the data commit reads STALE until publication (`receipts/axis-data.txt`, the declared two-phase window). Base gate baseline `w1/ExecHarmBase.md`. No falsification wave re-ran these after data (w2 not run).

## Sources & frontier

Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`: round start (`receipts/census-before.txt`) W04 ×7 + W01 S277, `mado ok`, exit 0 → round end (`receipts/census-after.txt`) the same plus W04 S303 and S307 (held URLs under a new scope), `mado ok`, exit 0.

- Rows 238 → **252** (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Added by tier: **A ×14** — S302-S315 (13 code, 1 docs), all `mined`, opened 2026-10-26; Gate lines in `corpus/lessons/round-45.md` `## Gate`.
- Rows touched old→new: none.
- Frontier advanced: `corpus/README.md` Frontier "Round 45 moves U5's runtime state agreement for the monitor rule"; knowledge entries 61 → 62.
- Sourced claim: C2 rests on S302-S315, opened this round.
- **Assimilation: none** (`w1/ExecIdGuard.md`: no `merge/mado/` theme on the monitor plane; nothing appended).
- Mistakes mined: M45-1..6 (`corpus/lessons/round-45.md` `## Mistakes`); QUALITY 85-86.
- considerthese: `considerthese/2026-10-26.md` proposal 1 → QUALITY 85 + `quality/check-session-material.py` (shown able to fail: base 50 findings incl. both D1 files, projected tree 48).

## Trend verdicts

- **expansion: improved** — one capability (monitor rule versus running output join, SCORECARD Round 45 capabilities) and one entry on ground absent at base (claim grep exit 1, `receipts/c2-ground-base.txt`), rows 238 → 252.
- **quality: unprovable-but-better** — both instruments were re-registered before data after w1 broke them, the contract was corrected on six Hyprland forms, D1 fixed; but no post-data falsification wave ran, so no outside re-check of the landed bytes exists yet.
- **discernment: improved (self-assessed, pending the non-author closure)** — three w1 refusals recorded with flips (S158/S162 reuse, wiki at main, the float32 finding), the lane's own v1 predicates withdrawn on evidence; the round-size shortfall and the 49 synthetic gate findings (`receipts/session-material-data.txt`) are reported, not hidden.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — new section "Monitor rule versus running output (round 45)" (`SKILL.md` tail, commit `ee6659b`); no non-author verifier.
- [~] At least one end-to-end domain task executed and logged — live read-only host run of the landed tool `.ufo/waves/round-45/receipts/live-monitors-host-r45.txt` (DP-1 AGREE, `verdict=OK`, exit 0); LOG.md Round 45; no non-author verifier.
- [~] Instructions executable by an agent without oral context — two seats rebuilt passing tools from the contract text (`w1/ExecIndepA.md`, `w1/ExecIndepB.md`); dispatched seats are not outside-lane verifiers.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE round-45 refinement; `w1/ScoutSiblings.md`: 0 sibling lanes on the monitor plane; no non-author verifier.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none (python3, git, curl, g++ and bwrap already present).

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed no files written by this round's seats in the fleet root.

Open L0 questions: none filed. Note for the operator: the host monitor serial is in held `corpus/knowledge/hyprctl-verification-layer.md:153` since round 2 (lesson M45-2); removing it from history is the operator's decision.
