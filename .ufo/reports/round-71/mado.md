# mado round 71 — report (hyaku run 15)

Lane: mado (desktop & compositor craft), lane counter 71, attempt 2 (attempt 1 died at launch
2026-11-04T00:06 -03 with zero lane progress and no report; nothing of its making was reused).
Lane base `c354f4d410b829d985b31560af9202d98655dad0` (the round-70 closure tip `e2bf3fc7` plus
the routed round-70 leftovers); lane tip at report time
`82927056e21b2e7b9ab2c7570e783c0bb851e132`, pushed (see Landed changes).

## Work performed

Claims (2, distinct axes, causally separable, frozen at
`4a91c644289437b588881a7254481157decfa450` before any candidate data; declaration
`.ufo/waves/round-71/claims-declaration-r71.md`):

- **C1 — calibration.** The landing control harness's M-Z kill credit follows the child's own
  parsed failed-assertion summary whatever the child's exit status
  (`mz_killed = summary_shows_failure(out)`; the round-70 `mz_rc != 0` conjunct is dropped),
  proven with four real `bash` children whose exit status disagrees with their own summary.
  Bounded score `10 × correct / 4` on the frozen four-scenario set. Do-nothing control: the
  held round-70 harness scores `base_correct=3/4`, missing `liar-success` and only it
  (`control-baseline-c1-r71.txt`).
- **C2 — operability.** The guard census's carrier rule counts four more Python shapes — the
  `dict(**module_mapping)` call splat, the splat through a one-hop alias, a key store through
  a one-hop alias of the handed mapping, and an attribute store bridged by one object-alias
  edge — each under the held dominance test, with the round-70 seventeen-case set carried
  forward byte-identically and two new negatives frozen. Bounded discrimination score
  `10 × controls / 23` on the frozen 23-case set. Do-nothing control: the held round-70
  classifier scores `19/23`, missing exactly the four carriers
  (`control-baseline-c2-r71.txt`).

Work items (each with evidence):

- Inherited round-70 seat-report leftovers committed under this round's entry (r70 spot-check
  routed defect 1; mined as M71-1) — commit `c354f4d4`.
- Freeze: declaration + both do-nothing control receipts + frozen control set + prototype
  scripts + fetch receipts — commit `4a91c644`. Duplicate-source check run at freeze time per
  M70-3: both planned rows cite already-held URLs, so the round appends superseding rows
  (CORPUS rule 2), never second rows for held bytes.
- Instruments: `quality/counters/c1-r71-landing-controls.py` (selftest 70/70),
  `quality/counters/c1-r71-real-children.py` (27/27), `quality/counters/c2-r71-shapes.py`
  (61/61) — commit `8e78a4ee`.
- Both frozen counting commands run verbatim at the instrument commit, rc 0 both — receipt
  `.ufo/waves/round-71/measurement-r71.txt` § C1/§ C2 — commit `e137b5a4` (with the wave spec,
  dispatch payload and validator stderr).
- Wave: ONE v1 wave of 13 seats (executor 3, scribe 3, scout 2, reviewer 2, critic 1,
  mutation-tester 1, connector 1; attack share 4/13 = 30.8% ≥ 25%; 1 connector ≤ 2) validated
  under `scripts/hyaku/ufo-wave-policy.json` (band 8–16) and dispatched through the inline
  spawn handoff (`w1.ready` → `w1.ready.dispatched`); the orchestrator reported WAVE-DONE with
  all 13 seats settled `status: ok`, zero dead seats, and results at
  `.ufo/waves/round-71/w1-results.json`. **Evidence gap (disclosed, not papered over):** 11 of
  the 13 seats returned empty final outputs and wrote no seat files; only the two reviewer
  seats delivered (`w1/R71RevC1.md`, `w1/R71RevC2.md`). Their reviews are the round's
  independent attack evidence — C1 verdict "predicate sound as bounded" with six disclosure
  findings; C2 verdict "UNSOUND as bounded" with two real dominance bypasses. No counter binds
  seat votes, so no frozen result depends on the missing seats (mined as M71-4; QUALITY 115
  registered).
- **C2 dominance repair** (review F1 HIGH: splat-alias rebind before the splat; F2 MEDIUM:
  object-alias edge bound after the call): repaired against the frozen sentence at
  `3868bc65`, red-before/green-after in `.ufo/waves/round-71/c2-dominance-repair-r71.txt`
  (the pre-fix blob at `8e78a4ee` credits both bypass fixtures; the repaired counter refuses
  both), both repro sources pinned as counter regressions (selftest 63/63), the frozen 23
  scoring identically before and after, and the per-file production census unchanged
  (20 / 13 / 13 / 0).
- Landing content: two knowledge entries, SOURCES rows S442/S443, README index + frontier
  bullet, lesson `corpus/lessons/round-71.md` (M71-1..M71-4, Gate, wave findings), QUALITY
  criteria 114–115, PROVINCE round-71 refinement, tool-ledger 119 → 122 rows, receipts dir —
  commit `443cbd50`; the five held rows' used-by reverse links (logged old→new in the lesson)
  — commit `9b2f1bce`; final harm-watch battery and census-after receipt — commit `f9230c46`;
  wave evidence — commit `82927056`.
- Standing-instrument repair (r70 spot-check routed defect 2; mined as M71-2): red-before
  receipt `.ufo/waves/round-71/m71-2-red-before-r71.txt` (`--round 70` default → rc 2,
  `citecheck path missing`); repaired by committing the round's receipts at
  `.ufo/waves/round-71/receipts/` so the `--round 71` default resolves committed bytes; the
  landing-time default-path run ends `MADO_LANDING_COUNTERS: GREEN` at the tip
  (`harm-watch-r71.txt`). Routed defect 3 (r69 deliverable-citation reds) stays
  observed-not-repaired: it belongs to a round-69 correction entry.
- Harm watch: gate `MADO_SELFTEST: 460/460` (unchanged); the frozen round-70 counters stay
  TARGET_MET at the tip (`cases=3 correct=3 base_correct=1`; `controls=17/17
  base_controls=13/17` — the r70 harness/classifier files byte-identical); axis table
  `checked=3 mismatched=0`; navigation 85/85; ledger 122/122 TARGET_MET; used-by
  `missing=0 TARGET_MET`; landing GREEN on the repaired default path —
  `.ufo/waves/round-71/harm-watch-r71.txt`. No config tree, compositor, service or sibling
  repo was written; no pacman transaction; no tool installed or upgraded (nothing needed
  beyond the committed instruments).

## Landed changes

Every change below is tied to the round-71 LOG entry (`LOG.md` § Round 71) and its commit;
the table enumerates all 8 content commits after the base (`git rev-list --count
c354f4d4..82927056` → 8, per QUALITY 112(b)):

| commit | what |
|---|---|
| `4a91c644` | claims declaration, control set (sha-pinned), both pre-freeze do-nothing control receipts, proto scripts, fetch receipts |
| `8e78a4ee` | the three scored instruments (harness, C1 counter, C2 counter) |
| `e137b5a4` | wave spec, dispatch payload, validator stderr, first measurement receipt |
| `3868bc65` | C2 dominance repair (review F1/F2), red-before/green-after receipt, two new counter regressions, docstring updates |
| `443cbd50` | knowledge entries ×2, SOURCES +2 rows (S442/S443), README index 83→85 + frontier bullet, round-71 lesson, QUALITY 114–115, PROVINCE refinement, tool-ledger +3 rows, receipts dir, LOG entry, SCORECARD round-71 section |
| `9b2f1bce` | five used-by reverse links for held rows cited by the new entries (old→new logged in the lesson) |
| `f9230c46` | final harm-watch battery receipt and census-after receipt |
| `82927056` | w1 wave evidence (results, ready markers, registry, the two delivered seat reports) |

## Before → after measurements

| Claim | Counting command | Before → after | Measured commit |
|---|---|---|---|
| C1 (calibration) | `python3 -I quality/counters/c1-r71-real-children.py --repo . --rev REV --base-rev c354f4d410b829d985b31560af9202d98655dad0 --scratch-root <scratch>` | held r70 harness on the four frozen real-child scenarios: `base_correct=3/4` (7.5000), missing `liar-success` only; instrument absent (0.0000) → `cases=4 correct=4 base_correct=3 verdict=TARGET_MET` rc 0; bounded 7.5000/absent → 10.0000 | first measured `8e78a4ee`; re-run at `3868bc65`, `9b2f1bce` — identical counts |
| C2 (operability) | `python3 -I quality/counters/c2-r71-shapes.py --repo . --rev REV --base-rev c354f4d410b829d985b31560af9202d98655dad0 --controls .ufo/waves/round-71/controls/c2-controls-r71.json --scratch-root <scratch>` | held r70 classifier on the frozen 23-case set: `19/23` (8.2609) → `population=20 readers=13 guarded=13 unguarded=0 controls=23/23 base_controls=19/23 verdict=TARGET_MET` rc 0; bounded 8.2609 → 10.0000 | first measured `8e78a4ee` (pre-repair); re-run at `3868bc65`, `9b2f1bce` — identical counts after the repair |

## Sources & frontier

- Census before (round start): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
  validate --root /home/vgpnk/Projects/shokunin mado` → exit 0, final line `mado ok …`
  (38 warnings, all pre-existing W04/W01 duplicate-url and tier-C families); rows 378.
- Census after (round end, receipt `.ufo/waves/round-71/receipts/census-after-r71.txt`): exit
  0, `mado ok …` (39 warnings: the 38 pre-existing plus one new W04 for the superseding
  same-URL rows — the sanctioned CORPUS rule 2 mechanism); rows **380** (378 → 380).
- Rows added by tier: A/docs/mined ×2 — **S442** (supersedes S108 for the `subprocess.run`
  capture_output scope; quote A `:53`, quote B `:54-55`) and **S443** (supersedes S439 for the
  § Calls `**` scope; 25-word quote `:1415-1417`), each fetched three times this round,
  byte-identical to the held pins (fetch receipts committed under
  `.ufo/waves/round-71/fetch/`). Rows touched old→new: five `used-by` appends (S108, S435,
  S438, S439, S441), each logged in the lesson; no `status` or `recheck` cell changed. One
  reject recorded in the Gate: `stdtypes.rst` (mapping-method behaviour, not call semantics).
- Frontier row advanced: the round-71 bullet at the head of `corpus/README.md` § Frontier
  (kill credit past the exit status + the four carrier shapes, with the still-open items).
- Mistakes mined: M71-1 (inherited uncommitted round-70 seat reports → QUALITY 114), M71-2
  (standing default-path wart → repaired, receipts committed), M71-3 (the C2 widening's two
  dominance bypasses → repaired red-to-green, pinned as regressions), M71-4 (the wave's 11
  empty-output seats → disclosed; QUALITY 115).
- Assimilation: none this round — no `merge/mado/` theme taken. `considerthese/2026-10-28.md`
  proposal 4 (a live-tool table) remains named-not-adopted (it governs live-state instruments
  on a probed host; this round probes no host).

## Trend verdicts

- **expansion: improved** — two admitted knowledge entries on the lane-tooling ground's new
  edge classes, each `source:` citing a `mined` row opened this round (S442, S443), plus the
  capability row entering the SCORECARD capabilities table in the same round (the
  exit-status-disagreement real-children battery + the shape-extended carrier census).
  Evidence: `corpus/knowledge/kill-credit-exit-disagreement-r71.md`,
  `corpus/knowledge/guard-carrier-shapes-r71.md`, SCORECARD § Round 71.
- **quality: improved** — both re-measured discriminations are repairs of disclosed limits
  (the r70 review's declared-limit disclosures and the round-70 planned intent), each with a
  pre-freeze red do-nothing control, and the wave's own falsification of the first widening
  was repaired red-to-green inside the round with the frozen set unchanged. Remaining limits
  are explicitly disclosed and pinned in selftests rather than claimed away.
- **discernment: improved** — the round's delivered outside-lane-style attack (the C2
  reviewer seat, a role the operator routes off the authoring model) falsified the first
  widening, and the repair stayed inside the frozen sentence with receipts; the C1 reviewer
  independently re-ran the counting command, the fixture modes as real bash children, the
  base leg and the doctrine counterexamples, and its soundness verdict rests on reproduced
  evidence. The outside non-author closure's spot-check (admit/reject sample) remains the
  integrator's duty and is not pre-claimed here; the evidence gap of the 11 silent seats is
  reported as a gap, not filled with assumed work.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: SKILL.md decision tables and the gate registry; the round's two entries carry cited, located sources (S442/S443 with line-pinned quotes); asserted by the lane (`[~]`, no non-author promotion verdict claimed).
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: LOG round-3 entry (the historical end-to-end pass); this round's domain work is the lane-tooling record plane (the lane's live desktop plane has been absent/probed-absent since r57 and its own records govern); asserted by the lane.
- [~] Instructions executable by an agent without oral context — evidence: the frozen counting commands were re-run verbatim end-to-end this round by the C2 reviewer seat and by the L1 (`w1/R71RevC2.md` reproduced receipts; `harm-watch-r71.txt`), with no oral context beyond the committed declaration; asserted by the lane.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: PROVINCE round-71 refinement appended; no compositor/config surface touched (all instruments are lane records); the reviewer's C1 stale-lane fixture probes touched only scratch; asserted by the lane.

## Stale-lane, L0, tooling, misc

- Stale-lane: none — this lane's mission is the only open mado mission (respawn-per-round
  driver; the round-71 attempt-1 L1 died at launch with zero lane progress and no report; the
  watchdog relaunched this attempt 2 the same minute).
- Open L0 questions (r57–r60 host/absence records, the L2 floor, the host-recovery pacman
  pause, the r37/r38 session-material history question) stay operator-owned; none was answered
  this round and none blocks it.
- Tooling: no tool installed or upgraded this round; pacman untouched per the host pause.
- Fleet-root misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`, no
  pathspec): no mado round-71 misroot found. An unattributed 24-byte stub named `after`
  ("== SCORECARD diff base-") sits at the fleet root; it does not name this lane or round and
  was left for its author. `.scratch/` changes are orchestrator-owned run state, never a
  misroot.
- Wave-evidence note: the w1 registry records 13 spawn members; per-seat agent ids in the
  results file are null (the orchestrator's capture shape), and the two delivered seat reports
  cite their own verified instrument digests — the round's verification rests on those
  reports plus the L1's re-runs, not on the empty seats.
