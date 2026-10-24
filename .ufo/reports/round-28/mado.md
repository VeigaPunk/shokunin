# mado round 28 — rotating held-out mutation gate; nine-defect record audit (attempt 1 after stale-claim reset)

Lane: mado-shokunin. The watchdog logged `lane-dead-no-report mado round=28` ×7; the attempt counter was
reset and this attempt (2026-10-24) inherited the committed work of the 2026-10-23 attempt (OOM-killed
mid-work after landing integration at `317ff19`) and finished the round. Rulebook: frozen
`.ufo/waves/round-28/registration.md` (b84348d; counters hardened 123d8cd; pre-data controls K1*/K2
committed). Lane tip at report time: `3565f13786ca563f29021db733c2d436d70c77cd` (pushed, ahead=0;
C1/C2 measured at `77cdda869ec616cb38cda494d992e57153a4a602`, the content tip this attempt landed before
writing the records; a LOG seat-count correction followed at `9ea706c3`'s child).

## Work performed

Declared claims (frozen registration, distinct axes): **C1 operability** (sourced: S183) — six-leg
composite PRED-C1-r28 closing the round-27 gate blind spots and rotating the held-out set; **C2
calibration** — the round-27 closure's nine routed record defects repaired. Lowest active scored axis was
calibration (7.4286 lesson-citation rubric vs coverage/operability at their finite 10.0000 ceilings —
CritCalibration w1 §1 selection audit).

- Re-verified every inherited committed artifact before reuse: registration, both frozen counters
  (c1 sha256 `dcca084f…`, c2 `c0415c9a…`), K1/K2 controls, H2 set + seal, q36 fixtures, suites, wave
  specs/registries (git log `b84348d…9ea706c3`; per-leg re-runs below).
- Restored the round-26/27 oracle byte-identically with the committed recipe
  `.ufo/waves/round-26/harness/build-tinywl.sh`: rebuilt tinywl sha256 `227a74af…` and
  libwlroots `1f3d7036…`, both exactly matching the pins in `.ufo/waves/round-27/harness/oracle.py`
  (no package installs; meson 1.12.1, ninja 1.13.2, gcc 16.2.1 already present; parent dir
  `/fast/scratch/hyaku/mado-r26` had to be re-created — the recipe assumed it).
- Measured C2 at the tip: 9/9 conditions PASS, `PRED-C2-r28 verdict=TARGET_MET` exit 0
  (`.ufo/waves/round-28/evidence/c2-after-77cdda86.txt`); before-state control `controls/K2DoNothing.txt`
  (1/9, TARGET_MISSED).
- Measured C1 per-leg at the tip (`.ufo/waves/round-28/evidence/c1-after-77cdda86.txt`): h2-rotate,
  refpub-kills, q36-witness, q37-open-ended PASS; h1-rotation and boolword-v5 FAIL inside the composite for
  two evidenced causes (below); composite prints `PRED-C1-r28 verdict=TARGET_MISSED` exit 1 — verbatim in
  the receipt.
- Authored and sealed the missing public reference set `c1/refpub/` (12 mutants, 4 per public subject, +
  6 benign rows) from the three committed public subject files only; frozen counter scored it 12/12,
  `h_min_per_subject=4` (first draft iterated: comment-only benign rows AST-invalid; `ref-chk-no-anchor`
  survived — both caught by the counter, replaced; lesson M28-3).
- Regenerated the q36 witness receipts (`quality/q36-successor-receipts.txt`, Q36WITNESS rows=4 failed=0)
  — the file is rewritten by the runner on each verification run.
- Appended SCORECARD round-28 results, LOG round-28 entry, lesson M28-1/M28-2/M28-3 + completion addendum,
  QUALITY criteria 38–40; re-ran the fleet-root misroot sweep (0 mado-owned files).
- Recorded wave accounting from the committed specs/registries (below).

## Landed changes

All commits via `scripts/hyaku/jj-lane.sh` (each prints `landed <hash>`):

- Inherited chain (2026-10-23 attempt): `b84348d` registration + both counters · `56ef773` report-blob pins ·
  `5198cc8` freeze + w1 spec (39 seats) · `123d8cd` counter hardening · `4f61006` controls + census-start ·
  `317ff19` suite blind-spot probes, H2 + seal, count-v5, q36 runner/receipts, check-population open-ended
  checker, D1–D9 record repairs, wave evidence. (LOG round-28 entry names each.)
- This attempt: `77cdda86` — refpub set + seal + regenerated q36 receipts ("round-28: public reference
  mutant set …"); `9ea706c3` — SCORECARD/LOG/lesson/QUALITY/evidence records; `3565f13` — LOG seat-count
  correction (88 no-report seats, not 72).
- Fleet repo: L0 questions `e2ce057fae3d1cf2e5197ac78e1c15368bad437d`; this report (below).

## Before → after measurements

- **C2 calibration**: `python3 -I .ufo/waves/round-28/c2/count.py REV` — before: 1/9 conditions,
  `verdict=TARGET_MISSED` exit 1 (committed control `controls/K2DoNothing.txt` at the registration commit);
  after at `77cdda86`: `CHECK D1..D9 PASS`, `verdict=TARGET_MET` exit 0
  (`.ufo/waves/round-28/evidence/c2-after-77cdda86.txt`). Honest framing per CritCalibration §3: eight
  unresolved conditions repaired in a frozen nine-condition audit; D9 passed pre-round (`dac4aef`) and is
  retained, not counted as an r28 gain. The lesson-citation rubric is not re-scored by this claim. Residual:
  the spotcheck routed ten record defects; the frozen population measures nine — the omitted §6.6
  docstring-citation overclaim is real, unclaimed, carried to r29 intent (RevengerNineDefects.md).
- **C1 operability** (sourced S183): `python3 -I .ufo/waves/round-28/c1/count.py REV` — before: all six
  legs FAIL at `123d8cd` (`.ufo/waves/round-28/evidence/c1-before.txt`); after at `77cdda86` (verbatim
  vector in `evidence/c1-after-77cdda86.txt`):
  - `h2-rotate` PASS — frozen round-27 counter on the rotated sealed H2: `TARGET_MET`.
  - `refpub-kills` PASS — new public reference set: `h_killed=12/12 h_valid=12 h_min_per_subject=4`.
  - `q36-witness` PASS — `rc=0 names=True` (both committed survivors named in the receipts).
  - `q37-open-ended` PASS — `rc=0`, frozen round-26 artifact sha `803e0096…` unchanged.
  - `h1-rotation` FAIL live (`rc=2 no-tally`): `/fast/scratch/hyaku/mado-r27/heldout` (H1, the
    registration-declared ephemeral input) was cleaned before closure. After-state verified by the
    committed w2 receipt `.ufo/waves/round-28/w2/reports/ReviewerSuiteMonotone.md`: new suite
    `h_killed=18/18 verdict=TARGET_MET`, green 17/17, w 15/15, exactly the three `held-c1v2` survivors flip
    to KILLED, monotone and behavioural.
  - `boolword-v5` FAIL inside the composite only: the frozen guard (`count.py:100`) pins count-v4.py at
    `3d7d301f…` while committed bytes are `635ae788…` — verified never-matching at freeze `5198cc8` and r27
    tip `20022a65`. The leg's frozen commands pass standalone at `77cdda86`: `count-v5.py 77cdda86
    --seed 28c1a8c0ffee0001` → `cases_pass=41/41 boolword_pass=2/2 verdict=TARGET_MET` exit 0; with
    `--tool-file c1/ref-mutants/exactbool-tool.py` → `boolword_pass=0/2 verdict=TARGET_MISSED` exit 1.
    HOST_SAFETY coredumps 1338→1338 on both runs.
  - Composite at `77cdda86` prints `PRED-C1-r28 verdict=TARGET_MISSED` exit 1 — reported verbatim. No
    leg rule was changed after data; both blockers are declared/evidenced boundaries (one declared in the
    registration, one a frozen-counter defect, lesson M28-1/M28-2, L0 questions open).

## Sources & frontier

Census (spec command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin mado`): start exit 0, 182 rows (`.ufo/waves/round-28/evidence/census-start.txt`);
end exit 0, 183 rows (`.ufo/waves/round-28/evidence/census-end.txt`; FLEET tier.A=176, B=1, C=6;
mined=164, queued=10, rejected=9; seven W04 duplicate-url warnings unchanged from round start).
Rows added: 1 — S183 (tier A, mined, opened 2026-10-23) by `corpus/knowledge/mutation-testing-r28.md`;
gate quote (≤25 words) in `corpus/lessons/round-28.md ## Gate`; search-log paragraph appended to
SOURCES.md. Rows touched old→new: none (append-only round). Frontier rows advanced: none. Sourced claim:
C1's method-and-limits note rests on S183 opened this round.

## Trend verdicts

- expansion — **improved**: new admitted surface on uncovered ground — the first public reference mutant
  set scored by the frozen counter (12/12) plus the restored oracle enabling the v5 successor measurement;
  evidence: `c1/refpub/` + seal at `77cdda86`, v5 receipts, capability row "rotating held-out mutation gate"
  (SCORECARD).
- quality — **improved**: the offline gates now close the three round-27 survivor classes (18/18 committed
  receipt) and the population checker reads open-ended targets (q37 PASS, frozen artifact untouched); the
  lane's records were repaired against an outside-enumerated defect list (9/9); evidence:
  `ReviewerSuiteMonotone.md`, `c2-after-77cdda86.txt`.
- discernment — **improved**: the round mined its own stale-premise and vacuous-check defects (M28-1 guard
  pin never matched; M28-2 ephemeral input lost pre-closure after a critic named the risk), turned them
  into QUALITY criteria 38–40, and published the composite's TARGET_MISSED verbatim instead of
  prettifying it; evidence: lesson `round-28.md`, QUALITY.md, `c1-after-77cdda86.txt`.

## SHONEN

- [~] SKILL.md decision tables/cited sources — gate registry rows current through r28 (D1 repair,
  `SKILL.md` rows 633–635); outside-lane verifier independence still not established (inherited note).
- [~] End-to-end domain task logged — C1's legs re-run the offline gates end-to-end; the boolword oracle
  was restored byte-identically and run (41/41); no new live-desktop task this round.
- [~] Executable instructions — wave prompts carried full contracts; 105 seats executed; the frozen
  registration + counters re-ran without oral context (receipts above).
- [~] No cross-domain bleed — PROVINCE untouched; harm watch: `git diff --stat 317ff19..77cdda86` touches
  only refpub + q36 receipts; census W04 unchanged; Hyprland coredumps 1338→1338.

Stale-lane: respawn-per-round driver; no other mission open. Tool installs: none (oracle rebuilt with the
already-installed meson 1.12.1/ninja/gcc; pacman paused throughout; nothing installed or upgraded).
L0: two questions committed (`e2ce057`) — scratch-input preservation policy; frozen composite guard-pin
ruling.

Round shape: this round is one steered lane round on a seat without a dispatch tool — the 2026-10-23
attempt ran the waves in-session; this completing attempt prepared no new waves and itemizes the surviving
wave evidence: w1 build 39 seats (one batched dispatch, policy v1; role mix executor 4, mutation-tester 4,
scribe 8, scout 14, critic 3, reviewer 3, connector 1, sentinel 1, revenger 1; 6 reports landed);
w1b attack 32 seats (registry committed; 0 reports — see dead seats); w2 falsify 34 seats (one batched
task call per `w2-run.json`, spawn=34 resume=0; role mix executor 5, mutation-tester 4, scribe 5, critic 6,
reviewer 4, scout 6, sentinel 1, revenger 1, connector 1, simplifier 1; 11 reports landed); round total
105 seats (≤128). §3 L2 floor met inside w1. Residual checks: none needed beyond the w2 falsify wave.
Planner seat: the L1 (validator rejects planner as a swarm role); the bounded planning data-walk rode w1
scouts/critics per the orchestrator ruling — no planner bypass. Dead seats: the 2026-10-23 attempt died
mid-work (7 watchdog deaths); w1 33 seats, w1b 32, w2 23 returned no in-tree reports — all named in the
three committed swarm registries; w2's ExecCountV5 and ExecRefPub were mid-work when the attempt died,
which is why refpub was authored and the v5 receipt captured by this attempt. Seat routing: operator route
table (`task.agentModelOverrides`); no claim depends on a seat's answering model; no provider backoff
observed this attempt. Misroot sweep at write time: `git -C <fleet> status --porcelain` — no mado round-28
file at the fleet root (foreign untracked files of other lanes left untouched; `.ufo/state` and
`watchdog.log` never touched).
