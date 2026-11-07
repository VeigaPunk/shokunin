# tsukuroi — round 90 report

L1: TsukuroiR90 (attempt 1; `.ufo/watchdog.log` `2026-11-06T23:21:22-03:00 launch tsukuroi round=90 … attempt=1`, no
earlier attempt, no inherited round-90 files). Lane `master` tip: `b1ef413d88a8fd13f3df9dda6b2e257d4a299318`;
`git ls-remote origin refs/heads/master` prints this hash. Pre-round tip `c0f91856a5cc4816ae5d075022f16dc6aef0593c`.

## Work performed

Declared claims, frozen at `6511437e7d86d3f1e7e39a45df91ade1d8293612` before the candidate gate was committed or
scored (`SCORECARD.md` "Round 90 — declaration"):

- **C1 (measured; surface: consequence modelling of the `limine-pins` gate; operability 9; sourced S364 opened this
  round, S350-S353/S361/S362 re-opened from the v12.9.4 tag clone).** `tools/check-limine-pins.py` follows the
  Limine v12.9.4 pin rule set R1-R7, R9-R10 and contract R8 of the r90 battery docstring: 73/73 families `met` in
  each of three runs, canonical lane and clean `git clone --shared`. New rules: R4 invalid resource name →
  `LP-BAD-RESOURCE`; R9 missing image of an efi chainload entry → `panic`; R10 `on_panic` menu/halt/halt-if-tpm
  with `--tpm-present`.
- **C2 (exploratory; depth 8, the lowest-tied axis; sourced S365-S373 opened this round).** Entry
  `corpus/knowledge/limine-tpm-volume-r90.md` (+ `.json`), rows TV1-TV9: what Limine's `tpm_present()` asks, how
  this host answers `--tpm-present`, and how `guid()`/`uuid()`/`fslabel()`/`boot(N)` find a volume and which name
  this host's ESP. Verdict only from a non-author `unprovable-but-better` judgment (the hyaku closure).

Work items:

- **Inputs.** r89 closure (MANIFEST index 1471, `rejected-honest-stop`, second in a row) and
  `corpus/lessons/round-89-verifier-spotcheck.md` §5; disposition table `corpus/lessons/round-90.md` "Inputs read".
  Routed 4 (R89-R5) is C1's surface; routed 2 repaired in the battery (N24-N27); routed 1/3 not this round's
  instrument (R90-R4).
- **Freeze `6511437e`.** Battery `tools/limine-pin-battery-r90.py` sha256 `8f0daee8…fb303e5` (73 families),
  `before/controls/` (make-controls.py, run-controls.sh, candidate-draft.py disclosed, 29 gates + INDEX.tsv),
  `before/src/` (6 v12.9.4 files, `cmp-pins.txt`), `before/host/receipt.txt`, `before/new-ground-sweep.txt`,
  census start receipt (rc 0), S364, declaration with the QUALITY 125 clause map.
- **Controls** (3 runs each; canonical at `6511437e`, clone layout at `cd165cf2`; `before/controls/summary-*.txt`):
  K1 landed gate 0/0/0 (canonical) and 1/0/0 (clone) of 73; K2 adapter 51/50/51 and 51/51/50; N01-N27 each killed
  by its named family in all three runs in both layouts (N26 by crash rows only).
- **Candidate `ce89df93`.** Gate r90 (selftest 25/25), registry row `limine-pin-battery-r90`, correction R90-REG-1.
- **C1 measured `ce89df93`** (`58723499` carries receipts): 73/73 ×3 clone and canonical
  (`.ufo/waves/round-90/after/measured/`), battery `--selftest --reference` 18/18; live read-only run
  (`after/live-receipt.txt`, `/boot` digest list identical before/after): lines 30/38 `LP-MISMATCH` `prompt`,
  `on_panic menu`.
- **C1 fidelity defect (honest stop).** Wave seat ReviewSource F1, re-read by the L1 at `config.c` raw 642-650:
  Limine reads `hash_mismatch_panic` and `measured_boot` only from the global section unless line 1 is an entry;
  r90 R10 and r87's R6 say "whole file", and families MEASURED-IN-ENTRY and PANIC-AFTER-PIN certify Limine-false
  answers (probe `after/visibility-probe.txt`). C1 filed target met, NOT VERIFIED as declared (QUALITY 106).
- **C2 landing** (`b380483e`, `9b4d9cda`, `b1ef413d`): TV1-TV9, S365-S373, pinned `after/src-c2/` (Limine, systemd
  v262.1, TCG spec PDF), host receipt `after/host-c2-receipt.txt`; TV2/TV4/TV9 strengthened on ScoutTPM, TV5/TV8
  corrected on ScoutVolume, drift limits on ScoutDrift — each after the L1 re-opened the source.
- **Quality.** LP5 erratum in `limine-pin-plane-r87.md` with carrier sweep `after/erratum-sweep.txt`; QUALITY 130
  (`--runs 0` vacuous verdict) and 131 (visibility read at the caller's buffer); lesson M1-M2, routed R90-R1..R5.
- **Wave w1** (13 seats, 0 dead): see "Round shape" below and the lesson's "Wave w1" section.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain`: untracked `trail-ids.txt` (pre-r89,
  not this round's, r89 report) and `.scratch/run15-wrapup/…` (orchestrator-owned); nothing moved.

## Landed changes

| Commit | What | LOG.md |
|---|---|---|
| `6511437e7d86d3f1e7e39a45df91ade1d8293612` | freeze: battery r90, 29 controls ×3 canonical, pinned sources, host receipt, S364, declaration | Round 90 entry "Freeze" |
| `cd165cf29071cc1f61ae3a5194b65d25f298894e` | clone-layout control receipts | "Freeze" |
| `ce89df93e5f576c5c236d4547299e9ea954e8853` | candidate gate r90, registry row, R90-REG-1 | "Candidate" |
| `587234994bbea98559daa5f92b01e7fe6f01a492` | C1 receipts, live receipt | "C1 measured" |
| `b380483e2a1d8edc97556fdd021794f619b6e1a6` | C2 entry TV1-TV8, S365-S371, LP5 erratum, sweep, visibility probe, QUALITY 130-131, lesson | "Landing" |
| `9b4d9cda5018bab51860129656155bf96c27bedd` | TV9, S372 (TCG spec), SCORECARD outcome, LOG, README frontier | "Landing" |
| `b1ef413d88a8fd13f3df9dda6b2e257d4a299318` | integration after WAVE-DONE: TV5/TV8 corrections, S373, drift limits, R90-R5, wave evidence, census end | "Wave w1", "Landing" |

## Before → after measurements

- **C1** — counting command `python3 tools/limine-pin-battery-r90.py --gate tools/check-limine-pins.py --runs 3`,
  measured at `ce89df93` (bytes unchanged to `b1ef413d`: `git diff ce89df93 b1ef413d -- tools/` empty). Before
  (do-nothing K1, landed r87 gate): 0/73, 0/73, 0/73 canonical; K2 adapter 51/50/51. After: 73/73, 73/73, 73/73
  `met` rc 0, clone and canonical. Verdict: target met; NOT VERIFIED as declared (R10/R6 visibility sub-clause
  contradicts `config.c` 642-650; 20 of the 21 mapped r90 clauses confirmed).
- **C2** — exploratory, no counting command. Prior state `before/new-ground-sweep.txt` (`git grep -n -i -e
  tpm_present -e volume_get_by -e TCG2 -e binary_bios_measurements c0f91856 -- corpus/knowledge`: r89 Limits lines
  only) → entry with TV1-TV9 at `b1ef413d`. Verdict pending the non-author closure.

## Sources & frontier

`SOURCES.md` rows 363 → 373 (`grep -c '^| S[0-9]' corpus/SOURCES.md` at `c0f91856` and `b1ef413d`). Census:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi` →
start rc 0 (`before/census-start.txt`), end rc 0 (`after/census-end.txt`), 52 W04 pre-existing duplicate-URL warnings
both ends, no E code. Rows added by tier: A 10 (S364-S370, S373 code; S372 spec; S371 own-work). Rows touched
old→new: S366 anchor `575, 597-598, 1035-1047, 1050-1061` → adds `488-497` (disk GUID) and "slot + 1"; S371 digest
`273c55ff…` → `09ca1d6a…` (has-tpm2 lines appended). No status change. Frontier advanced: r89 "Held-out clauses"
(except containment, empty label) and "UF1 … efi `LP-MISSING` as `panic`" answered; new frontier R90-R1..R5
(`corpus/README.md` "Round 90"). Sourced claims: C1 rests on S364 (opened this round); C2 on S365-S373.
Mined mistake: M1 `R89-EMPTY-RUNS-MET` (fix shown able to fail: r89 `--runs 0` rc 0 vs r90 rc 2); M2
`R90-VISIBILITY-WHOLE-FILE` (red shown; fix routed). Gate: admits S364-S373, rejects `hdd(1:1)`, `+TPM2` and
unopened scout rows (lesson `## Gate`). Assimilation: none (no `merge/tsukuroi/` theme). considerthese: none fits —
all five proposals of `considerthese/2026-10-26.md` already adopted (QUALITY 103, 108, 110, 112, 115).

## Trend verdicts

- **expansion — unprovable-but-better (claimed; the closure rules).** New ground TV1-TV9 (TPM presence and volume
  lookup, sweep 0 → 2 files), 10 new tier-A rows, host answer for the gate's new flag; exploratory, no counter.
- **quality — improved.** QUALITY 130/131 with receipts; LP5 erratum with a carrier map; four r89 routed-2 clauses
  given controls (N24-N26 certified; N27 found wrong and routed); scout rows corrected before admission; lints
  143/143, 106/106, 0 dangling.
- **discernment — improved.** The wave falsified a rule the lane had carried since r87; the L1 re-read the bytes,
  built a probe that can fail, filed C1 as NOT VERIFIED rather than reading 73/73 as proof, and rejected two
  plausible but unsupported proposals (`hdd(1:1)`, `+TPM2`).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence `SKILL.md`
  registry row `limine-pin-battery-r90` and `R90-REG-1` (this round); non-author verification still owed.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: live read-only gate run
  `.ufo/waves/round-90/after/live-receipt.txt`, LOG.md "Round 90".
- [~] Instructions executable by an agent without oral context — evidence: entry `limine-tpm-volume-r90.md`
  "Operator actions" (exact read-only commands); no no-oral-context retest this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: ConnectorOverlap scan
  `.ufo/waves/round-90/w1/ConnectorOverlap.md` (20 siblings, no conflict); PROVINCE.md unchanged.

## Round shape

One v1 wave of 13 seats (policy `scripts/hyaku/ufo-wave-policy.json`, validator rc 0): executor 2, mutation-tester 2,
critic 2, reviewer 2, scout 3, connector 1, scribe 1; attack share 6/13 (46 %). 0 dead seats; no residual call; round
total 13. Planner seat held by the L1. Dispatched via `w1.ready` (taken 2026-11-06T23:50:50), WAVE-DONE received
before this report.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Tool installs: none (L1 and every seat
report none). Open L0 questions: none new; `tsukuroi | round-86 | HOST INCIDENT` stays open (live pins 30/38 still
`LP-MISMATCH`, `prompt`).
