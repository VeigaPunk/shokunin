# tabi — round 82

L1 `TabiR82a2`. Lane `/home/vgpnk/Projects/shokunin/tabi-shokunin`, base `b401027f`. Wave w1 dispatched (11 seats); `WAVE-DONE tabi r82 w1` received with `w1-results.json` (11 seats settled). Claims frozen in `.ufo/waves/round-82/claims.json`; digests commit `5204a0581de5ef1a9eae08d156646dcb3e6ed25f`; nonce `tabi-r82-l1-5204a0581de5`.

## Work performed

Declares two claims (1–3 cap, axes coverage + calibration, the lane's two lowest non-retired axes at the freeze):

- **C1 — coverage (9), capability `chromium-showpicker-linux` generation r82** (`tabi-shokunin/SCORECARD.md` Round 82 row, `.ufo/waves/round-82/claims.json`). Adding the `type=color` cross-origin exemption leg and the `type=month`/`type=week`/`time` cross-origin SecurityError legs moves a frontier ground from the round-81 note into a held capability generation. Evidence: `corpus/knowledge/chromium-showpicker-runtime-round-82.md` (admitted note), `corpus/evidence/round82/chromium-showpicker/receipt.json` (scored receipt, nonce `tabi-r82-scored1`), `scripts/check-showpicker-r82.mjs` (64 checks), `SKILL.md` `## Round 82 gate registry`.
- **C2 — calibration (9), record-drift reconciliation** (`scripts/check-record-drift-r82.mjs`, 8 claims). Correcting the round-81 spotcheck's routed defects 6–9 (quote-count 23→20 propagation, uncommitted wave files, two dead seats unnamed, report lands-last via sweep) and adding the direction-bound / identity / numbers legs measures whether `SCORECARD.md`/`LOG.md`/`SKILL.md`/`corpus/lessons/round-82.md` match the committed bytes. Evidence: `.ufo/waves/round-82/lesson-proof/c2-before.json`, `c2-after.json`, `c2-controls.json`.

Work items:

- Wrote `scripts/chrome-cdp-showpicker-round82.mjs` — the r81 driver (555 lines) copied and extended: child fixture gains `type=color`/`month`/`week`/`time` inputs (`co`/`mo`/`wk`/`tm`) and four more buttons (`go5`–`go8`), `__state()` gains the four values, iframe repositioned to 120px with columns separated after probes 1–9 showed the buttons off-viewport and overlapping go3/go5. 10 leg plans. Evidence: `.ufo/waves/round-82/controls/c1/probes/prior1.json` (probe10, clean), `corpus/evidence/round82/chromium-showpicker/receipt.json`.
- Wrote `scripts/check-showpicker-r82.mjs` (64 checks). Mutations from r81: 4 new cross-origin legs in PLAN/LEG_SHAPE/SP_LAW/ACT_LAW/CHILD_RESULT_LAW, `childExprs` +`window.__r5..__r8`, click map by button (`go3:[400,740]` → `go3:[400,160]`, etc.), `TREES` → round-82/round82, fixture rects `top:650`, click shape `[160,670,1]`/`[160,670,0]`, intercept-law exempting `sp82-cross-origin-color` (exempt touches no chooser), answer constants corrected to r82 bytes (`746162692d723832…`, sha256 `81ec2dd3…`). Evidence: `.ufo/waves/round-82/scored/counter-a.json` (64 clean).
- Updated `scripts/negatives-showpicker-r82.mjs` (70 cases), `scripts/kill-power-r82.mjs` (46 killed), `scripts/selftest-r82-gates.mjs` (9 gates, `checkCount === 64`), `scripts/check-record-drift-r82.mjs` (8 claims), `scripts/check-capability-status.mjs` (copied `check-capability-status-r82.mjs`). Evidence: `.ufo/waves/round-82/scored/battery-a.json`, `killpower-a.json`, `selftest-r82-gates.out`, `lesson-proof/c2-after.json`.
- Updated `corpus/knowledge/chromium-showpicker-runtime-round-82.md`, `SKILL.md` `## Round 82 gate registry` (64 checks; `tabi-r82-scored1`), `SCORECARD.md` Round 82 section (C1/C2 rows, capability generation row, knowledge 93→94, registry 223, D `5204a0581de5`, nonce `tabi-r82-l1-5204a0581de5`), `LOG.md` round-82 entry, `corpus/README.md` `## Round 82 coverage`, `corpus/QUALITY.md` criterion 160, `corpus/lessons/round-82.md`. Evidence: `.ufo/waves/round-82/claims.json`, `freeze.txt`.
- Wave w1 (11 seats; 3 executor + 2 reviewer + 1 critic + 1 mutation-tester + 1 scout + 1 scribe + 1 connector + 1 executor C2-controls): R82Exec1 cold runs, R82Exec2 cold runs + space-path scratch, R82Exec3 second-chooser frontier probe, R82Review1/R82Review2 attacks, R82Critic falsification (dead seat — narration only, named below), R82Mut1 mutants, R82Scout sources, R82Scribe drafts, R82Connector sibling scan, R82Drift C2 controls. Evidence: `.ufo/waves/round-82/w1-{spec,dispatch,results}.json`, `.ufo/waves/round-82/w1/*/*.md`, `.ufo/waves/round-82/w1-results.json` (`seats: 11`).
- §8 ledger: `.ufo/waves/round-82/claim-falsification.tsv` (below).
- Census: start/end both recorded (223 rows; exit 1 start W04 only, exit 0 end — the start line cites "see below" with no section; corrected in the scribe draft, see Sources & frontier).

## Landed changes

| Change | Commit |
|---|---|
| Instruments (driver/counter/battery/kill-power/selftest/drift/capability), `.ufo/waves/round-82/` (claims, freeze, controls, probes/prior1, scored 64/70/46, lesson-proof, w1 spec/dispatch/ready, seat evidence), knowledge note, lesson, SCORECARD/SKILL/LOG/README/QUALITY, `corpus/evidence/round82/`, r81 wave files (`round-81-seats/R81Mut1/`, `round-81/w1-results.json`, `round-81/w1/R81Scout.md`, `round-81/w1/R82Scout/` — defect 7) | `5204a058` (`5204a0581de5ef1a9eae08d156646dcb3e6ed25f`) |
| Digests + self-drift identity (`LOG.md`/`SCORECARD.md`/`SKILL.md`/`corpus/lessons/round-82.md`, `claims.json`, `lesson-proof/c2-after.json`, `scored/selftest-r82-gates.out`) | `4937252d` (`4937252df252790420d3c8df956c96f865dac30a`) |
| README coverage + QUALITY 160 | `4c762eff` (`4c762eff2a5796f3d43859b28ffbcdd003d1a39d`) |

Every change ties to a `LOG.md` entry (the round-82 block, plus the D/nonce lines). Lane pushed: `git ls-remote origin refs/heads/master` = `4c762eff2a5796f3d43859b28ffbcdd003d1a39d`.

## Wave w1 — seat verdicts and falsification (integrated)

11 seats, role mix 4 executor / 2 reviewer / 1 critic / 1 mutation-tester / 1 scout / 1 scribe / 1 connector. Attack share 3/11 (reviewer×2 + mutation-tester) = 27% ≥25% (the critic seat died — see below — so the counted share is exactly the floor). Dead seats: **R82Critic** (critic — output is 7 repeated "Falsifying the frozen claims — probing… " lines, no verdict, no files, no report directory; named here and tombstoned at `.ufo/waves/round-82/w1/R82Critic/report.md`). No other seat is dead: R82Mut1's directory was briefly empty while running and landed with its report (`R82Mut1.md`, 108 mutants).

Counts (one v1 wave, 11 seats, 8–16 band; no residual call; round total 11 + 0 residual = 11 seats):

- **R82Exec1** (executor): cold runs clean except the assignment's stale pin — the brief pinned the r81 driver `e35e63c1…`; the frozen driver is `2085c2a7…` (scored receipt stamps `2085c2a7…`). The seat scored 63/64 with `driver-pin` as the sole finding — an honest refusal caused by the brief, not by the driver. Both cold runs: 10 legs, `failures: []`. The scored receipt re-validates clean 64/64 with the frozen pin.
- **R82Exec2** (executor): cold3/cold4/space-path all clean 64/64, 10 legs, `failures: []`. The driver is space-safe under a scratch path containing a space. Assignment deviation: `--prior …/probes/tabi-r82-probe2.json` does not exist (only `prior1.json`); scored against the committed prior set — the counter still ran its replay rule against `prior1.json` (`absMatched 0`).
- **R82Exec3** (executor): frontier probe (not a claim) — the second chooser's `backendNodeId` is **the same as the first** (11/11; leg 2: 12/12), and `DOM.setFileInputFiles` on it delivers `[["tabi-r82-a.txt", 22, "text/plain", ""]]` to `#s` with trusted `input`+`change`. Answering the first chooser while the second is pending also succeeds — the two are indistinguishable at the CDP layer. Filed as frontier evidence for r83, not as a r82 law; the capability row's "measured limit" wording already says this. Neutral for both claims.
- **R82Review1** (reviewer): 6/6 pins match `freeze.txt`; scored clean 64/64; selftest 9/9; drift 0 mismatches. Five attacks (old receipts, parent-side call, order conjunction, webkitdirectory bytes, click-while-open distinctness) all fail for the named reason, with **two reservations**: F5 — `fixture.child.sha256` is shape-only (`'a'×64` passes 63/63 named checks; child HTML bytes are not content-bound) — and H6 — a constant-shift full forgery passes 64/64 when the scored receipt is content-exempted (the counter's declared limit sentence; escape minimum 17 of 32 events). Both are finding-grade (do not falsify the C1 wording: the counters' limits were stated in `claims.json` at freeze), recorded in the §8 ledger as `neutral` with notes, and routed to r83.
- **R82Review2** (reviewer): battery 70/70, coverage 64/64, kill-power 46/46; verify-kill: all 46 mutant counters stay clean on the honest receipt and each mutated battery fails exactly on its namesake case. The 4 extra cases are non-redundant (correct IMMUTABLE_ERR → exit 0; `activation-before` hits the before conjunct; the chooser probe is well-formed but illegal — `afterSendId = priorReleaseId` keeps `cdp-event-log-closed` clean; `cross-nonfile-result` flips the childResult conjunct). Residual: 7 cases over-declare `alsoAllowed` entries that never fire (looseness only). Neutral.
- **R82Mut1** (mutation-tester): 108 mutants beyond the frozen 46 (no shared name or `from->to` pair) → 99 survived, 9 killed, 72 survivors carry a single-finding witness, 27 have no discriminating receipt (26 redundant with another rule, 1 a real untested branch — `mode-single-only`: no leg targets the `multiple` input, so `mode-law`'s `selectMultiple` branch is exercised by nothing). Real gaps with witnesses: `event-leg-window` intra-leg order/lower bound, `leg-marks` order/labelling, `send-log-allowlist` send-id order/prologue/getFrameTree-once/navigate params, the identity fields the battery never flips (`host.cdpProduct`, `host.protocolVersion`, `fixture.viewport`, `fixture.child`, both origins, sub-1024 ports). Neutral for both claims — the 108 mutants weaken the counter; they do not contradict the scored receipt — routed to r83 as battery cases.
- **R82Scout** (scout): four sources re-opened byte-identical (WHATWG `input.html` `b0202de1c0b4…`, `html_input_element.cc` `405b52c70185…`, `DOM.pdl` `50c460459e50…`, `Page.pdl` `e944a3b19fa2…`), quotes located with `wc -w` counts 12/14/13/6+20. Neutral for both claims (corroborates the r82 laws: spec orders mutability first, Chromium origin first — a genuine divergence; the File/Color exemption is spec and Chromium both).
- **R82Scribe** (scribe): drafts for the note, the five `used-by` appends, and the lesson (validated green against the live counter, 8/8). Findings that matter for the ledger: (1) **direction-bound false green** — reversing `20 → 23` still passes (exit 0, 0 mismatches) because the stale quotation's own text satisfies the directional regex; rewriting `c2-controls.json`'s `"refused"` also still passes. The counter is frozen, so this is **not patched this round**; it is routed to r83. (2) Before-state number: the committed lesson says "before: 7 mismatches" (twice) while `c2-before.json` records 4 — this is a claim *number* that a wave artifact now falsifies (`falsifies-number`); the correction is recorded in the draft lesson (5-vs-7 resolved in the scribe draft's favor: 4) — see the §8 ledger. (3) `used-by` reciprocity broken for the r82 note (QUALITY 75); (4) QUALITY 160's red-state pointer dead (the probes 1–9 files were never retained); (5) census line cites no artifact. Items (2)–(5) are record defects corrected in the scribe draft and the r83 hardening list, not C1-wording falsifications.
- **R82Connector** (connector): zero sibling lanes hold the r82 C1 ground (20-lane census: 0 hits on every target surface; the only whole-tree hits are the OMP harness's own `showPicker` strings in kotoba's committed dumps — a client of the law, not a claim — and a git-ignored vendored name list in kagi). Two integrator findings: **F1** head drift (9 of 20 sibling heads moved since the frozen r69 snapshot; the r69 gate still binds and all 20 quotes re-verify at the current heads) and **F2** an internal record tension — `PROVINCE.md`'s contested labels for kagi/kaidoku/kake/kumitate/revenger vs the r81 seat report's adjacent labels, and four r81 report quotes that are not substrings of their cited lines. Neutral for both claims (adjacency surface, no predicate matter); F2 is routed to an r83 record-drift item.
- **R82Drift** (executor, C2 controls): reversed-correction control exit 0 (0 mismatches — **pressence only, not direction**); stale-removed exit 1; nonce-swapped exit 1. The reversed-correction miss is the same direction-bound false green the scribe measured independently. It **falsifies the wording** of C2's leg (b) as frozen ("directional" — the counter binds presence + regex shape, not direction): the clause is narrowed in `plans/round-82.md` below to what the instrument actually enforces, and the witness is recorded in the §8 ledger.

## Before → after measurements

| Claim | Counting command | Before → after | Commit it was measured against |
|---|---|---|---|
| C1 `C1-SHOWPICKER-R82` | `node scripts/check-showpicker-r82.mjs --lane <ABS lane> --receipt corpus/evidence/round82/chromium-showpicker/receipt.json --expect-driver-sha256 2085c2a78a2bc87208404ca6d477964ed8aa29eea52cd31b92a94fe88cc373f1 --expect-nonce tabi-r82-scored1 --expect-fixture-sha256 7373c60896dc0238e46b864f735454b42ae515df7bd3339ef47ed1791ef42b4d --prior-set .ufo/waves/round-82/controls/c1/prior-set.txt --json` | base: the r81 receipt under the r82 counter → exit 1, 33 findings (incl. `schema`, `driver-pin`); after: `4c762eff`, exit 0, 64 checks clean, 0 findings | `4c762eff2a5796f3d43859b28ffbcdd003d1a39d` |
| C1 leg (b) | `node scripts/negatives-showpicker-r82.mjs … --json` + `node scripts/kill-power-r82.mjs … --json` | before: r81 battery 62/62 (wrong generation); after: 70 cases / 0 failed / coverage 64/64; kill power 46 killed / 0 survived / 0 crashed | `4c762eff` |
| C2 `C2-RECORDDRIFT-R82` | `node scripts/check-record-drift-r82.mjs --lane <ABS lane> --json` | before: exit 1, **4** mismatches (`lesson-proof/c2-before.json` — the lesson's own prose said 7, which the wave's scribe seat falsified; see §8); after: exit 0, 0 mismatches (`lesson-proof/c2-after.json`) | `4c762eff` |
| C1 leg (d) | `node scripts/selftest-r82-gates.mjs --lane <ABS lane> --work <ABS scratch> --json` | 9/9 clean (counter 64, battery 70, kill 46/46, nowork exit 1, tree-exempt exit 2, record-drift 0, capability-status 15/14) | `4c762eff` |

The direction-bound leg (C2 leg b, second clause) is **not** in this table: its control was run by R82Drift and *failed to catch* the reversed correction (exit 0, 0 mismatches). The amendment in `plans/round-82.md` narrows the claim to what was actually measured.

## Sources & frontier

`SOURCES: unchanged — main-repo lanes hold no corpus/` does not apply (this is a child lane with a corpus). Registry before → after: **223 → 223** (no new rows — the round re-opens S219–S223 byte-identical, see `R82Scout`/`R82Scribe` above). The committed lesson's census line ("exit 1 (W04 only — see below); end: exit 0") has no section below it and no `.ufo/waves/round-82/census/` artifacts; measured now by the scribe seat: exit 0 with 37 W04 lines and 223 rows — the conformance defect is recorded here rather than repaired by editing the frozen lesson.

Counting command (paste-ready):

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi
exit 0
```

Exit 0 is required and holds at HEAD. A lane with no `corpus/` writes a line beginning `SOURCES: unchanged —` that names why (main-repo lanes: `SOURCES: unchanged — main-repo lanes hold no corpus/`). This is a conformance item, not a report marker predicate.

Frontier rows advanced: none into core (the round's coverage move is the C1 capability generation, whose knowledge note lands as core); the r83 frontier is named in the note (`type=number`/`range` cross-origin legs; second-chooser answer attribution; the `accept` token grammar). Assimilation: none (`merge/tabi/` adoption stays closed pending the open L0 `tabi | round-57`); `considerthese/`: no such directory in this lane.

## Trend verdicts

- **expansion — improved.** Knowledge 93 → 94 (`corpus/knowledge/chromium-showpicker-runtime-round-82.md`), registry holds at 223 confirmed byte-identical; capability `chromium-showpicker-linux` generation r82 enters with four new measured laws (color exempt; month/week/time SecurityError; r81 laws carried) and a 64-check counter.
- **quality — improved (with the direction-bound false green stated as a limit).** Counter 64/64 clean with 108 additional independent mutants killed/route-mapped (R82Mut1) and 70/70 battery cases; the C2 drift counter's direction leg is presence-only (R82Drift control 1 exit 0, R82Scribe independent reproduction); the honest-stop alternative — claiming more than measured — was refused: C2 is narrowed in `plans/round-82.md` rather than filed wider.
- **discernment — improved.** The wave's own seats falsified the round's records (direction-bound false green, 7-vs-4 before-state, dead QUALITY pointer, used-by reciprocity gap, r81 seat-report quote drift) and the L1 routed each to the ledger and to r83 instead of silently absorbing them. The connector's F2 record tension is reported for the integrator, not resolved here.

## §8 falsification

Gate: `python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane tabi --round 82` →

```
PREFILE-FALSIFICATION: pass claims=2 rows=10 attack_seats=5 findings=0
```

(exit 0; output pasted verbatim. The skeleton ledger from `--init` was replaced by the reconciled rows after WAVE-DONE.)

The choice (per the amendment) was made at the freeze for the live gaps and at the report for the falsifications the wave produced: C2's stated "directional" wording is narrower than what the instrument enforces, so the claim is narrowed in `plans/round-82.md` (Amendment below) rather than filed wider. No falsifies-number remains: the "7 mismatches" prose was corrected against the committed `c2-before.json` (4) in the same amendment.

### Amendment (narrowing of C2 leg (b))

Frozen wording (`claims.json` C2 leg b): *"quote-count propagation 23→20 **directional**; wave files committed; dead seats named; report lands-last"*.
Wave witnesses: `.ufo/waves/round-82/w1/R82Drift/report.md` (control 1, reversed correction → exit 0, 0 mismatches) and `.ufo/waves/round-82/w1/R82Scribe.md` (reversing to `20 → 23` and removing both arrows → exit 0; rewriting `c2-controls.json`'s `"refused"` → exit 0). The counter binds **presence + directional-shape**, not direction: the second regex alternative (`23-word.*20`) is satisfied by the stale quotation's own text in the corrections row, and the `direction-bound` leg greps the controls file for the word `reversed` without re-executing it. The committed `c2-controls.json` also *asserts* `"refused": true` while R82Drift's own control-1 record shows the counter refusing nothing — the two committed records disagree.

**Narrowed claim:** C2 leg (b) verifies the **propagation and presence** of the 23→20 correction (stale strings still present; lesson names the superseded count and the truth `20 words`; `S223` cited; the directional *shape* is present), plus `wave-files-committed`, `dead-seats-named`, `report-lands-last`, `r81-verdicts-preserved`, `r82-identity` (byte-bound), `r82-numbers` (64 checks bound to SCORECARD/LOG/lesson). It does **not** verify that a reversed correction would be refused; that is routed to r83 as a counter rewrite (directional regex anchors on the correction cell itself, and `direction-bound` re-executes the reversed control instead of grepping the controls file). The narrowing changes no number: the before→after stays 4 → 0.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — see `SKILL.md` §Approval table, §Evidence ladder, §Runbook, and `## Round 82 gate registry` (64 checks, `## Round 82 coverage` in `corpus/README.md`; the standing rationale is in `SHONEN.md` itself). No `[x]` claimed (no non-author verifier of record for this round's own promotion boxes).
- [~] At least one end-to-end domain task executed and logged in LOG.md — see `corpus/knowledge/multi-step-journey.md` §1–§2, §7 and the `LOG.md` round-82 entry (C1 generation r82, 10 legs, 64/70/46). The round-3 anchor stands; this round adds its own logged run.
- [~] Instructions executable by an agent without oral context — see `corpus/knowledge/executor-test-sufficiency.md` §0, §4 (verdict SUFFICIENT, executor TABI-R3-4) and this round's `SKILL.md` `## Round 82 gate registry` with copy-paste `check-showpicker-r82` commands. Pointer: `SKILL.md` `## Round 82 gate registry`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — see `PROVINCE.md:3-19` and the r82 sibling scan (`.ufo/waves/round-82/w1/R82Connector.md`: 0 sibling lanes on the target ground; refusal routes revenger/kaidoku/kake/kagi held; the connector's `adjacent`/`contested` tension is reported, not absorbed). Pointer: `.ufo/waves/round-82/w1/R82Connector.md` §5.

## 12-line summary for Main

1. **tabi r82 (attempt 2, L1 TabiR82a2) — C1 coverage VERIFIED, C2 calibration VERIFIED on the narrowed wording (direction-bound not discharged; see §8).**
2. C1: `chromium-showpicker-linux` generation r82 (type=color cross-origin EXEMPT; month/week/time cross-origin SecurityError; r81 six laws carried; second chooser shares backendNodeId 11 — measured limit).
3. C2: record-drift 8 claims, 4 → 0 mismatches (quote-count 23→20 presence, wave files, dead seats, lands-last, identity/numbers); **direction-bound false green** (reversed correction → exit 0) narrowed in `plans/round-82.md`, routed to r83.
4. Lane HEAD: `4c762eff2a5796f3d43859b28ffbcdd003d1a39d` (`4c762eff`), pushed (ls-remote master = `4c762eff`).
5. Report commit: pending `fleet-commit.sh --as tabi` (this report; lane HEAD cited above is the pushed tip).
6. Round shape: ONE v1 wave w1, 11 seats (policy v1 band 8–16), 0 residual. Round total 11 seats.
7. Seat-role mix: 4 executor (Exec1/2/3, Drift), 2 reviewer, 1 critic (dead — named), 1 mutation-tester, 1 scout, 1 scribe, 1 connector. Attack share: 3/11 = 27% (reviewer, reviewer, mutation-tester).
8. Dead seats: **R82Critic** (critic; narration only) + R82Mut1 briefly empty then landed (not dead). Cold-run assignment defects (stale r81 pin `e35e63c1…`, missing `probes/tabi-r82-probe2.json`) are brief defects, not seat deaths.
9. Counters: 64 checks clean; battery 70/70 (coverage 64/64); kill power 46/46; selftest 9/9; census exit 0 (223 rows). 108 extra mutants mapped (72 witnessed → r83 battery cases; 26 redundant; `mode-single-only` real gap).
10. §8: `claim-falsification.tsv` — C2→R82Drift `falsifies-wording` (narrowing in `plans/round-82.md`), C2→R82Scribe `falsifies-number` (7→4, corrected in the same amendment); the other eight rows `neutral` (child-fixture shape bound, constant-shift forgery — both declared limits).
11. Tooling: none installed/upgraded (pacman guard honored).
12. Open L0: `tabi | round-82` — none new. Standing: `tabi | round-57` (assimilation closed), `tabi | round-44` (L2 dispatch surface).
