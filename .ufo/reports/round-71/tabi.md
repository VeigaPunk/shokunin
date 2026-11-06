# tabi — round 71 report (attempt 1)

Lane HEAD (pushed): `47ffeac32b7ba47a9de945c37e4d0f47ba93d36f` (`git ls-remote origin refs/heads/master` prints it). Base `11b00f644f5af1a4f7827da6956732e0b91023a5`. Round 70 was admitted (MANIFEST `rounds[1439]`), so there was no fresh-start obligation. No earlier attempt of r71 exists, so nothing was inherited.

## Work performed

Two claims were declared and frozen at `04f4330f` (`.ufo/waves/round-71/claims.json`). The pre-freeze instruments and executed controls landed first at `711a38c2`, and the digests at `749a1ab5` (`.ufo/waves/round-71/freeze.txt`). All six axes started at 9, so both claims work a lowest axis.

- **C1 — coverage, capability acquisition `chromium-synth-pinch-gesture-linux`.** Sourced on S176–S178, all opened this round. Predicate `C1-SYNTHPINCH` (a)–(d). **Honest stop: leg (b) is red.**
- **C2 — operability.** `scripts/verify-live-r71.mjs` is an execution-bound generation of the live verifier for the r69 and r70 capabilities. It is measured by a frozen attack harness and evaluator. Predicate `C2-EXEC-BOUND` (a)–(d). **Verified on the frozen predicate.**

Work items:

- **Inputs read before declaring.** The r70 spot-check (`corpus/lessons/round-70-verifier-spotcheck.md`). Routed defects R1–R6 are handled one by one in `corpus/lessons/round-71.md` § Round-70 routed defects. R2 is closed by a named correction entry in SCORECARD `## Round 71`.
- **Sources.** S176–S178 were fetched from Chromium 155.0.8059.84 `content/common/input/` (`.ufo/waves/round-71/sources/`). `input_handler.cc` and `Input.pdl` were re-opened, and their digests are unchanged.
- **New instruments** (`711a38c2`):
  - driver `scripts/chrome-cdp-synthpinch-round71.mjs`: 11 legs, a child-exit listener, and a socket-path guard. This closes r70 R4 for the new driver.
  - counter `scripts/check-synthpinch-r71.mjs`: 87 checks.
  - battery `scripts/negatives-synthpinch-r71.mjs`: 107 cases with an isolation rule, which addresses r70 R3.
  - kill-power control `controls/c1/kill-power.mjs`.
  - verifier `scripts/verify-live-r71.mjs`: refuses injected environments and execArgv, gives every child an allow-listed environment, runs from a private snapshot that it re-hashes, enforces a 6 s wall floor, and binds the driver's stdout to its receipt.
  - attack harness `controls/c2/attack-harness.mjs` and evaluator `controls/c2/evaluate-c2.mjs`.
- **Pre-freeze executed controls** (`711a38c2`):
  - C1: do-nothing exits 2 (`receipt-unreadable`). Degenerate drivers `dispatch-wheel`, `set-scale` and `skip-touch` hold 4/4 under `evaluate-c1-controls.mjs`. Battery 107/107 and kill power 87/87 on the smoke receipt.
  - C2: verify-live-r70 has **falsePass 4** (`controls/c2/pre-r70/summary.json`).
  - The r70 bytes installed under the r71 name score falsePass 4, and the evaluator exits 1 (`donothing-r70-bytes.eval.json`).
  - The blanket-refuse and blanket-accept verifiers both evaluate false.
  - verify-live-r71 before the freeze: the evaluator holds.
- **Scored runs, after the freeze** (`244505a0`):
  - C1 receipt `corpus/evidence/round71/chromium-synth-pinch-gesture/receipt.json` (sha256 `19e3c5b6…1ab6`): counter clean on 87 checks; battery 107/107 with 98 isolated cases; kill power 87/87.
  - C2 L1 harness: falsePass 0, notLanded 0, and the evaluator exits 0 (`scored/c2-eval-L1.json`). `verify-live-r71` exits 0 on both profiles.
- **Knowledge note** `corpus/knowledge/chromium-synth-pinch-gesture-runtime-round-71.md` (cites S176, S177, S178, S174, S173). Committed at `64e389f2`, extended at `a6626204`.
  - Mouse and default-source pinches arrive at the page as trusted ctrl+wheel events.
  - The duration law `(s−1)·200/speed` holds exactly.
  - The clamp leg's deltas sum to 100·ln 2.
  - `scaleFactor:1` is a no-op.
  - `scaleFactor:0` never finishes and wedges the gesture queue.
  - The touch geometry is two pointers on one line, and touch pinches do not zoom.
  - The note also takes in R71Exec3's probe measurements: scale range 1..4, a negative scale produces one NaN-delta wheel, the per-event delta law, and anchor bounds that scale with zoom.
- **Gate registry.** SKILL.md `## Round 71 gate registry` and `scripts/selftest-r71-gates.mjs` (8/8, exit 0, `scored/selftest-r71-gates.out`). `check-gate-registry --rev 64e389f2` reports only the 5 pre-existing missing rows (R6).
- **QUALITY 133–134**, each backed by a Mistakes row.
- **Wave w1:** 12 seats, all settled. Evidence is in `.ufo/waves/round-71/w1/` (`47ffeac3`).

## Landed changes

| Commit | Content | LOG.md entry |
|---|---|---|
| `711a38c24d9220fa93599b72d901bc1846a3087a` | pre-freeze instruments, executed controls, staged sources, census start, lesson proof | `## Round 71` bullets 1–2, 4 |
| `04f4330f5047ce75df70007f7a6b210950ee8cde` | freeze `claims.json` | bullet 1 |
| `749a1ab58d791a112ad7462dcea2a0bed7d6454e` | `freeze.txt` | bullet 1 |
| `244505a0b4dfe0f32db3349cdd173caa60a0e97b` | C1 scored receipt, counter, battery and kill power; C2 scored harness, evaluator and live runs; wave spec and dispatch | bullets 2, 4 |
| `64e389f21f57f9ca3b96d97978f9b6a6f01dc356` | knowledge note, S176–S178 rows, S173/S174 used-by, lesson draft, QUALITY 133–134, SKILL registry, self-test | bullets 3, 6 |
| `a662620415f20205e199aeefca9c08d5b3341eea` | SCORECARD r71 block with both corrections, LOG, note with R71Exec3 measurements, lesson attack findings, census end | bullets 2–7 |
| `47ffeac32b7ba47a9de945c37e4d0f47ba93d36f` | wave w1 evidence (12 seats), `w1-results.json`, ready markers, Scout finding | bullet 2 |

## Before → after measurements

| Claim | Counting command | Measured against | Before → after |
|---|---|---|---|
| C1 coverage capability | `node scripts/check-synthpinch-r71.mjs --receipt corpus/evidence/round71/chromium-synth-pinch-gesture/receipt.json --expect-driver-sha256 5318780cc13664f36a41d33024a500b5a5b2a8a3737d39489990fd98084922af --json` | before `11b00f64`; after `244505a0` (instruments unchanged to `47ffeac3`) | counter exit 2 (no receipt) → (a) exit 0, 87 checks clean; **(b) R71Exec1's cold run is refused, exit 1 `event-leg-domain`** (`w1/R71Exec1/counter.json`); (c) 107/107 and 87/87; (d) note committed, capability row withheld. **Not verified — honest stop.** |
| C2 operability | `node .ufo/waves/round-71/controls/c2/attack-harness.mjs --lane <ABS> --verifier verify-live-r71.mjs --work <ABS> --out <ABS>; node .ufo/waves/round-71/controls/c2/evaluate-c2.mjs --summary <out>/summary.json --json` | before `11b00f64` (verify-live-r70); after `244505a0` (verifier bytes `61f43596…f333` unchanged to `47ffeac3`) | falsePass **4 → 0**, positives 2/2 exit 0, evaluator exit 1 → 0. Independently reproduced by R71Exec2. Both live profiles exit 0 for the L1 and for R71Exec2. **Verified.** |

**C1 kill, frozen and not amended.**
- The runaway `scaleFactor:0` gesture delivered one wheel after the driver relabelled the page `end`. Two of three live runs were clean; R71Exec1's was not.
- R71Critic agrees: C1 is FALSIFIED on leg (b).
- R71Critic also found that a three-field rebrand of the scored receipt passes the counter, battery and kill power. This is within the declared limit "not an execution oracle". Leg (b) was the only execution evidence.

**C2 attack record.**
- R71Critic: HOLDS-WITH-LIMIT. Two vectors the frozen limit sentence did not name:
  - receipt hand-off between the load and the counter spawn;
  - a node interpreter that the same user can write.
  Both are now named by the correction entry in SCORECARD `## Round 71`.
- R71Review2: SOUND, with two findings: `NODE_COMPILE_CACHE` is not on the refused-environment list, and the harness summary is not bound to the verifier's digest.
- R71Mut2: 2 of 11 hardening mutants were killed, with 0 false passes. The four attacks prove the layers in combination, not each layer alone.

**Author's verdicts (closure pending):** C1 not verified (honest stop); C2 verified. Under §2 admission rules, this round cannot be admitted, because not every claim verifies. All verdicts are reported for the operator to rule.

## Sources & frontier

- **Census command:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`.
  - Start: exit 0, 175 rows (`.ufo/waves/round-71/census/start.txt`).
  - End: exit 0, 178 rows (`.ufo/waves/round-71/census/end.txt`; W04 cross-scope warnings only).
  - `grep -c '^| S[0-9]' corpus/SOURCES.md`: 175 → 178.
- **Rows added:** 3, all tier A `code`, status `mined`:
  - **S176** `synthetic_pinch_gesture.cc` (`4f7fd101…`)
  - **S177** `synthetic_touchpad_pinch_gesture.cc` (`67ab6a4b…`)
  - **S178** `synthetic_touchscreen_pinch_gesture.cc` (`3b5253ce…`)
  R71Scout re-fetched all three independently and got byte-identical results, both decoded and as base64 transport.
- **Rows touched (old → new):** S173 and S174 used-by now include the r71 note. The change is logged in the lesson `## Gate`. R71Scout notes that both rows are scoped to scroll and are now cited for pinch lines; this scope gap is routed to r72.
- **Frontier advanced:**
  - Runtime delivery of `Input.synthesizePinchGesture` is measured and written up as knowledge. The capability row stays withheld.
  - Gesture-queue wedging by a zero-scale pinch is new frontier.
- **Sourced claim:** C1 rests on S176–S178, opened 2026-11-06.
- **Mistakes mined** (`corpus/lessons/round-71.md` `## Mistakes`):
  1. A control labelled degenerate actually ran the honest producer. Became QUALITY 133. Shown able to fail: `lesson-proof/mislabeled-summary.json`.
  2. A swap attack that never landed almost read as a defence. Became QUALITY 134. Shown able to fail: `blanket-accept.eval.json`. The deleted first red run is recorded honestly.
  3. A counter assumed every event ends inside its leg, for a gesture that never ends. Routed to r72.
- **Assimilation:** none. `merge/tabi/` adoption stays closed (L0 `tabi | round-57`). `considerthese/`: this lane has no such directory.

## Trend verdicts

- **expansion: improved.**
  - Knowledge 83 → 84, on ground the lane did not hold (pinch delivery, the zero-scale queue wedge, scale bounds).
  - Registry 175 → 178.
  - The C2 attack harness is a new runnable instrument.
  - No capability row was added (C1 withheld).
- **quality: improved.**
  - The r69 and r70 capabilities were re-derived live today through a verifier that four named attacks no longer green (L1 and R71Exec2, 4/4 snapshot reads equal to the pins).
  - The r70 C1 limit sentence got its owed correction (r70 R2).
  - QUALITY 133–134 were added.
- **discernment: improved.**
  - The gate rejects three claims against source and runtime:
    - omitted source → touch, for pinch;
    - `scaleFactor` 0 is usable;
    - touch pinch zooms (R71Exec3 confirmed this reject under emulation too).
  - The round reports its own leg-(b) failure as an honest stop instead of narrowing the predicate.
  - Outside agreement is still owed.

## Round shape and seats

- **Shape:** ONE v1 wave `w1` (policy band 8–16): 12 seats.
- **Roles:** scout 1, connector 1, executor 4, scribe 1, reviewer 2, critic 1, mutation-tester 2. Attack seats: 5/12 (42 %).
- **Planner:** the L1 holds the planner seat, because the validator refuses `planner`.
- **Dispatch:** inline spawn handoff (`w1.ready` → `w1.ready.dispatched`); WAVE-DONE received.
- **Seats:** 12 settled, 0 dead (`w1-results.json`; rows carry no `status` field, R6).
- No residual call. **Round total 12.**

## Other

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only orchestrator `.scratch/` entries. No tabi seat misroots.
- **Scratch:** `/fast/scratch/hyaku/tabi-r71` removed.
- **Tool installs:** none.
- **L0:** no new questions. Earlier tabi L0s (r57, r69, r70) remain open and are routed around.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `## Round 71 gate registry`; knowledge note items 1–9 tied to S176–S178/S174/S173 lines. Lane-authored, not verified by a non-author.
- [~] At least one end-to-end domain task executed and logged in LOG.md — an eleven-leg live `Input.synthesizePinchGesture` journey on Chromium 155 (`corpus/evidence/round71/chromium-synth-pinch-gesture/receipt.json`; independent run `.ufo/waves/round-71/w1/R71Exec1/receipt.json`); `LOG.md` `## Round 71`.
- [~] Instructions executable by an agent without oral context — R71Exec1 and R71Exec2 ran the note's `recheck:` command and the C2 harness cold. These are lane-dispatched seats, not non-authors.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — R71Connector found no sibling holding the pinch surface; kama's adjacency ground is reported, not absorbed. `PROVINCE.md` is unchanged.
