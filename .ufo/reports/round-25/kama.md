# kama — round 25 report (attempt 2)

Lane: kama (local model serving and endpoint health). Round 25, attempt 2,
dispatched 2026-10-22T09:19:50Z (session note: 09:19:49Z). Attempt 1 was
stood down by the orchestrator for capacity, not for a fault; no attempt-1
identity was resumed. Lane tip at report time: a46a61815f79c558992e3fdea5e01b738442d6a8
(pushed; `jj-lane.sh state`: local = remote, ahead 0, behind 0, tracked 0,
untracked 0).

## Work performed

Declared claims (`.ufo/waves/round-25/preregistration.json`, amendments 1-4,
errata `errata-attempt-2.json` and `errata-attempt-2-falsify.json`):

- **C1 — declared calibration (repair-first; axis fit not established).**
  Registered isolation mutant anchors, target `stale 0`. Repairs the M-series
  part of the round-24 spot-check's routed defect 2.
- **C2 — coverage, learning claim on frontier K05 (declared versus served
  context capacity), with a capability.** Target `registered 14 observed 14
  bound True`. Sourced on S106-S113, opened this round.

Work items:

- Re-verified inherited state: efe58e96 (preregistration, amendment 1,
  pilot, census before exit 0 with 105 rows); C1 before `registered 27 stale
  2 ['M11-listing-surrogates', 'M17-ref-shadow']`. The attempt-1 build wave
  (34 seats, cancelled) is committed as a record only, not claim evidence
  (5388b7cf, `build/ATTEMPT-1-DISPOSITION.md`, corrected by both errata files).
- C1 repair (1fc41e34): `tests/report-audit/isolation-mutants.py` M11
  re-anchored, M17 kept on its round-23 line, new id M33 for the second call
  site. Full run at 1fc41e34 (`.ufo/waves/round-25/final/c1/c1-tip-mutants.json`):
  exit 0, pristine passed, 28 mutants, 26 killed, survivors M17 and M20;
  replicated by seat ExecC1TipReplicate. M17 survives because round-24
  commit 92063cf moved the reachable path to `bare_objects()`; grid row F13
  now kills M33 (RevengerM17Sites causal run on ed1cc3a). Docstring and
  SKILL registry row say so.
- C2 tool and receipt: `tools/kama-context-capacity.py` (5ea4fc44, request
  timing and teardown gate at 46fb04bd); counter tightened by amendments 3
  (c808ba07) and 4 (46fb04bd) after two attack seats found false counts;
  final receipt re-run after amendment 4 (5c95c8f1), 70 raw files with sha256.
- Knowledge: `corpus/knowledge/context-capacity.md` (new entry on K05
  ground): KV pool versus per-slot ceiling; fit raising a zero split context
  (X1: pool 8192, 2048 per slot; X3 fit off: 2048, 512; K7 exception); both
  concurrent requests failing with HTTP 500 on a shared 2048 pool (L1) while
  L2 (split 8192) and L3 (sequential) pass; identical endpoint values for
  pools 2048 and 8192 (K1, X2). Falsify-wave supporting cells (unregistered):
  shared 8192 pool passes, shared 2048/3072 fail and 4096 passes, boundary
  at n_predict 25 pass / 26 fail. SKILL.md round-25 decision rows; KQ36;
  lesson `corpus/lessons/round-25.md`; SCORECARD and LOG entries.
- Routed repairs: PM08 wording in SKILL.md (manual, review-only, unexecuted,
  uncredited); registry count 27 → 28; `SKILL.md:188-191` premise; round-24
  locator erratum (lesson §Routed defects item 3). H2 (Git >=2.45) left
  operator-owned.
- Planner seat: held by the L1 author; the planning walks were the attempt-1
  pilot and an L1 verbosity walk (amendment 2 honesty note 3). No planner
  seat in any wave.

Round shape: default two v1 waves. Wave 1 build: 40 seats (scribe 14,
executor 7, critic 5, scout 5, mutation-tester 3, revenger 2, reviewer 2,
connector 1, sentinel 1; attack roles 10 of 40), all 40 returned, 0 dead.
Wave 2 falsify: 37 seats (reviewer 22, critic 5, executor 4,
mutation-tester 3, sentinel 1, scout 1, connector 1; attack roles 30 of 37);
at report time 19 had returned and 18 were still running, 0 dead. Round
total 77 seats. Seat gate: granted for both waves (`wave-slot.sh`, cap 85);
wave-1 reservation released after all 40 returned; the wave-2 reservation is
still held because 18 seats had not returned. No task call was refused.
Every task carried the validator's taskCall plus the task tool's required
`solutionSpace` field (`dispatched-payload.json`).

## Landed changes

Lane commits of round 25 (all through `jj-lane.sh`, pushed):

| commit | what | LOG |
|---|---|---|
| efe58e96e6cfbef88a0fba9d64505e18b7ad7356 | attempt 1: preregistration, amendment 1, pilot, census before | LOG §Round 25 |
| 5388b7cf1d5bad9c228da6f95c40f323414be2f1 | amendment 2, strict counter, attempt-1 build record | LOG §Round 25 |
| 1fc41e346853afd98cbd7010af5db4e54dc877f7 | C1 re-anchor, M33 | LOG §Round 25 C1 bullet |
| 5ea4fc44e1d0b5236e14e8b4881f446626a56682 | C2 tool and first receipt | LOG §Round 25 C2 bullet |
| c808ba07f09c4be55413d3d6516c542ab69b64f8 | amendment 3 | LOG §Round 25 C2 bullet |
| 46fb04bd54978a2a3c47b3da098a2526804014e0 | amendment 4, request timing | LOG §Round 25 C2 bullet |
| 5c95c8f111a981e316cd4933e38fc363e51f8604 | final receipt | LOG §Round 25 C2 bullet |
| fa3b62ae6475d111eb466d79af616aeebb08bbb9 | entry, S106-S113, SKILL rows, KQ36, lesson, SCORECARD, LOG, C1 evidence | LOG §Round 25 |
| 46be41cf674301953837c8863cd2026e8a21fcb0 | report draft, falsify spec | LOG §Round 25 |
| c0a9b029c0355fedb6880541d95982849026f626 | falsify corrections: entry scope, SKILL rows, C1 axis-fit correction | LOG §Round 25 |
| a46a61815f79c558992e3fdea5e01b738442d6a8 | falsify errata, entry and lesson fixes, falsify advice so far | LOG §Round 25 |

## Before → after measurements

- **C1:** `python3 -c "…"` (preregistration.json C1.command; enumerates the
  whole MUTANTS list): `registered 27 stale 2 ['M11-listing-surrogates',
  'M17-ref-shadow']` at efe58e96 → `registered 28 stale 0 []` at 1fc41e34 and
  at a46a6181 (exit 0). Re-run by falsify seat RerunC1Count: matches.
- **C2:** `python3 .ufo/waves/round-25/count-c2.py` (amendment-4 bytes): no
  receipt at efe58e96 (counter added at 5388b7cf exits 2, no count) →
  `registered 14 observed 14 bound True missing []` on the receipt at
  5c95c8f1, re-run at a46a6181 (exit 0).

## Sources & frontier

- Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`.
  Start: exit 0, 105 rows. End (10:17Z): exit 0, `kama ok`, W04 warnings only.
- Rows 105 → 113; added by tier: A +8 (S106-S113), B 0, C 0; mined 86 → 94,
  queued 8, rejected 11.
- Touched: S060 used-by gains `corpus/knowledge/context-capacity.md`
  (logged old → new in the lesson Gate).
- Frontier advanced: K05 on the lane fixture only (`corpus/README.md`
  §Frontier advanced — round 25). Consumers, large models, other builds and
  engines stay open.
- Mined mistakes: six rows in the lesson §Mistakes, including the stale
  registered instrument (captured-by none; KQ36, shown able to fail: stale 2
  at efe58e96, stale 0 at 1fc41e34) and the axis misfile.

## Trend verdicts

- **expansion: improved** — one entry on uncovered K05 ground with observed
  cells, one capability shown running (`tools/kama-context-capacity.py`,
  receipt 5c95c8f1). Falsify critic CriticLearningBarFinal: clears the
  learning bar as knowledge on uncovered ground, not through supersession.
- **quality: unchanged** — routed wording and count corrections
  landed and KQ36 added, but chronology defects recurred inside the round
  (two false `written_utc` stamps, an amendment after its receipt, a commit
  that captured a running seat; all disclosed in the errata files) and
  wording corrections from the falsify wave were still arriving at report
  time, some not applied (§Open items). The gains and the in-round defects
  do not net to a provable improvement; the closure decides.
- **discernment: unchanged** — attack findings were turned into stricter
  counters and scoped claims, but the round declared C1 on an axis it does
  not fit; C1 earns no calibration credit.

Claim verdicts (author): C1 measured value verified, axis fit to
calibration not established (falsify critics CriticC1Calibration and
CriticC1AxisFit: drift, which AXES files under freshness), so this round
does not show the lowest-axis obligation (calibration 7; no stagnation
waiver). C2 verified as measured (`registered 14 observed 14 bound True`).

## Open items at report time

- 18 falsify seats had not returned (including RerunC1FullMutants,
  ReplicateReceipt, ReviewerEntryClaims, ReviewerCapacityTool, the S106,
  S107, S112, S113 re-opens, RerunCensus, ReviewerReportDraft). Their advice
  lands under `.ufo/waves/round-25/a2-falsify/advice/` but is not integrated.
- ReopenS109 (returned after the last lane commit): the entry's "2 × 1025
  cells overflow the 2048 pool" should read "each slot held 1024 decoded
  tokens, filling the pool; the logged 1025 counts the unplaced next token";
  the SKILL row should cite the observed L1 row, not S109, for HTTP 500; S109
  teaches omits the unified-cache precondition of the idle-slot purge (a
  `supersedes S109` row is the correction route). Not applied.
- ReopenS106 and ReopenS113 (returned after the last lane commit): the S106
  teaches cell is wrong in places (fit measures before it resolves a zero
  context, fit.cpp 264 and 276; reduction needs the memory deficit at 384
  as well as 393-394; `-c 0` is raised too, only its reduction is
  disabled; a direct-floor path at 414 and 441-444 is omitted). S113 says
  "per layer" where only layers allocating their own K/V count. Under the
  SOURCES contract both need appended `supersedes` rows; not applied this
  round. The entry's observed values are not contradicted.
- SentinelCapacityTool: five tool-safety risks remain open (listener
  ownership after reads, cleanup on all exits, stop after a failed
  teardown, scratch containment, caller-selected executable). The committed
  receipt shows every port closed; hardening is not claimed.
- Fleet-root strays not written by kama (`write`, a `.pyc`, intent-to-add
  entries; ScoutMisroot) were left untouched. No kama seat file remains at
  the fleet root.
- L0: "kama | round-24 | R23-H2 … Git >=2.45" stays open, routed around. The
  round-16 fixture scope is still pending L0 ratification.

## SHONEN

- [~] SKILL.md contains real decision tables… → `SKILL.md` §Round-25 decision rows; no non-author verifier named.
- [~] At least one end-to-end domain task executed and logged → `.ufo/waves/round-25/final/context-capacity-receipt.json`, LOG §Round 25.
- [~] Instructions executable by an agent without oral context → `SCORECARD.md` §Round 25 capability row command.
- [~] No cross-domain bleed → `corpus/knowledge/context-capacity.md` §Related lane evidence (kengaku cited, not absorbed).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none by the author; no seat reported an install or upgrade.
No llama-server was left running (`pgrep` empty at 10:17Z).
