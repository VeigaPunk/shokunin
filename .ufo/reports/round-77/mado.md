# mado — round 77 (hyaku run 15, attempt 1)

## Work performed

Declared claims (frozen in `.ufo/waves/round-77/claims-declaration-r77.md` before the wave; base
`aeeef067bd63672dfc681d6dacc3797f53ffd1f9`):

- **C1 — coverage:** the bar-footprint chain becomes a measured join. `tools/mado-barfoot.py`
  derives the declared waybar box (position, layer, height, width, margin, exclusive) and joins
  it to the live layer entry in `hyprctl layers -j` and the monitor's `reserved` band in
  `hyprctl monitors -j`; a frozen fifteen-case set scores the join and kills five named mutations.
- **C2 — operability:** the SKILL.md read-only probe table executes end-to-end. Twelve frozen
  cases, each bound to its committed table row, run all twelve probes and compare the stated
  outcome; the read-the-table control is reported separately and cannot claim an execution.

Work items, each with its evidence pointer:

- **C1 join built, frozen and measured.** `tools/mado-barfoot.py` (`VERSION r77-v1`, sha256
  `61f34022…`), `quality/counters/c1-r77-barfoot.py`, frozen set
  `controls/c1-cases-r77.json` (15 cases, sha256 `7d6e2b1a…`, generator `controls/make-cases-r77.py`);
  freeze `e4717a1c`, v2 `a83e9bee`; measurement `receipts/measurement-final-r77.txt`.
- **The host join measured read-only.** DP-1 3440x1440@99.997, waybar at level 2, box
  0,0,3440,26, reserved `[0,26,0,0]`, usable area y=26..1440; captures
  `fetch/live-layers-r77.json` (sha256 `46eb2481…`) and `fetch/live-monitors-r77.json`
  (`e732af34…`), live run in `receipts/pre-wave-evidence-r77.txt`.
- **Seven sources opened, one rejected.** SOURCES 393 → 401 rows: S457–S462 and S464 mined,
  S463 rejected with its flip condition; census exit 0 with the documented W04 duplicate-URL
  warnings (`corpus/SOURCES.md`; fetch receipts `fetch/S457.bin`–`S464.bin`,
  `fetch/sha256-r77.txt`).
- **Knowledge entry and index.** `corpus/knowledge/bar-footprint-r77.md` (`verified-at:
  2026-11-04`), index row in `corpus/README.md`, Frontier bullet at `corpus/README.md`.
- **C2 runbook frozen and executed.** `quality/counters/c2-r77-runbook.py`, control set
  `controls/c2-runbook-cases-r77.json` (12 cases, sha256 `597b2302…`); the twelve probes run and
  match in `receipts/measurement-final-r77.txt`.
- **Wave-found hardening (coverage).** The scout's F1/F2: a monitor's pixel size was read as the
  logical box, and the dynamic cross-size branch guessed a size the bar never declares. Both are
  now refused (`UNMODELLED`, exit 3); red/green in `receipts/repair-r77-tool-refusals.txt`
  (rc 1 before, rc 3 after for both fixtures).
- **Wave-found hardening (operability).** The runbook counter inherited the caller's environment;
  a non-session runner lacks `HYPRLAND_INSTANCE_SIGNATURE` and `OMARCHY_PATH`, so every
  `hyprctl`/`omarchy` probe failed. It now discovers the instance from
  `$XDG_RUNTIME_DIR/hypr/*/.socket.sock` and `OMARCHY_PATH` from the `omarchy` binary's own
  location, adding them only when absent; red/green in `receipts/repair-r77-c2-env.txt`.
- **Cited-revision probe (D2 fix).** `quality/check-cited-revisions.py` reads a row, resolves the
  instrument's last-change commit and reports green/red; a row with no claim is an error, never
  green. Red on `5dade9b3`, green on `3588a527` (row fixtures under
  `fixtures/cited-r76-{red,green}-row.txt`; `receipts/cited-revision-check-r77.txt`; selftest
  6/6). Registered as a probe (`SKILL.md`, `quality/tool-ledger.md`).
- **Records.** `corpus/lessons/round-77.md` (six mined mistakes M77-1…M77-6, Gate with one admit
  class and one reject, wave findings), `SCORECARD.md` round-77 block (two claim rows, two
  capability rows, planned r78), `LOG.md` round-77 entry, `SKILL.md` canonical gate registry
  (four rows), `quality/tool-ledger.md` 136 → 140 rows, `PROVINCE.md` round-77 refinement,
  `corpus/QUALITY.md` 132–134.
- **Routed defects from round 76.** D1 provenance trios appended to the two r76 entries; D2 the
  SCORECARD C2 revision correction plus the new probe; D3 the declaration errata and the r76
  counter's docstring text (numeric example, limits paragraph and the superseded mutant list),
  each with a parity run; D4 the mistake count from the lesson rows plus the LOG correction;
  D5 this report's Stale-lane line; D6 the three r76 handoff files committed with the freeze;
  D7/D8 the pointer corrections in the r76 lesson. Evidence: `receipts/parity-r76-docstring.txt`,
  `receipts/cited-revision-check-r77.txt`, the r76 lesson `## Corrections (round 77)`,
  `SCORECARD.md` r76 `### Corrections (round 77)`.
- **Wave.** One v1 wave, 12 seats (4 executors, 2 scribes, 1 scout, 1 connector, 1 reviewer,
  1 critic, 1 mutation-tester, 1 revenger; attack share 4/12). Seat outcomes below.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Freeze: tool, both counters, both frozen case sets, declaration, live captures; r76 handoff retention (D6) | round-77 bullet 1 | `e4717a1c` |
| Freeze v2: C1 counter resolves `--repo` before the scratch-cwd git call | round-77 bullet 1 | `a83e9bee` |
| Pre-wave control baseline and freeze-rev measurement | round-77 bullet 1 | `94b5afb1` |
| w1 spec, validator plan, dispatch payload | round-77 wave bullet | `8b7ef027` |
| Entry, index, frontier, SOURCES rows, lesson, SCORECARD, LOG, gate registry, ledger, PROVINCE; r76 D1–D4/D7–D8 corrections | round-77 bullets 2–5 | `3e35d0a9` |
| Ledger pointers and the r77 axis-table re-derivation | round-77 bullet 5 | `6923899` |
| Wave-found hardening (scale/transform and dynamic cross-size refusals) and entry limit corrections | round-77 bullet 6 | `0fa69f41` |
| Cited-revision probe first cut (pair list) and registrations | round-77 bullet 6 | `c083db4f` |
| Probe rewritten to read the r76 row itself; superseded pair fixtures dropped | round-77 bullet 6 | `cb8d559d` |
| QUALITY 132–134, scout/connector wave findings, r76 count correction in LOG | round-77 mistakes/registry bullets | `adf8875b` |
| C2 counter session-env discovery with the red/green receipt and M77-6 | round-77 bullet 6 | `4a17b31f` |
| D3 mutant-list text in the r76 counter docstring with a parity run | round-77 bullet 5 | `8722d564` |
| Critic dispositions: C2 limits erratum, oracle-based `reserved-wrong-edge` mutant with a red/green | round-77 bullet 6 | `de627316` |
| Revenger fixes: mode-preset refusal (red/green), gate-row exit map, anchor attribution, literal quotes | round-77 bullet 6 | `bbca7469` |
| Literal single-line quote fragments in SOURCES/lesson and the tool contract's anchor attribution | round-77 bullet 6 | `2df46e29` |
| S464 (gtk-layer-shell auto zone) grounds the `NOT_MODELLED` claim; manual-line precision | round-77 bullet 5 | `e177c79b` |
| Revenger residuals: S464 bytes+manifest, seven-source wording, ranges, scorecard revision correction | round-77 bullet 5 | `53b4fadf` |
| Minor residuals: background-layer refusal, margin wording, S463 rationale note, C2 written-form transforms | round-77 bullet 6 | `9197405c` |
| Used-by back-references repaired in place (7 rows, 12 pairs) and logged; landing counters GREEN | round-77 registry bullet | `a0a8b2a0` |
| Mutant finding: C2 matcher requires exit 0 (red/green), QUALITY 135, three frozen-set gaps named | round-77 bullet 6 | `bce906f3` |
| Measurement and harm-watch receipts at the repaired tip | round-77 bullet 5 | `ee62bd7f` |
| Wave evidence (nine reports, three partial seats, `w1-results.json`) and the reviewer dispositions | round-77 wave bullet | `d362908b` |
| Final measurement, harm watch, landing-green receipt; lane tip pushed | round-77 bullet 5 | `d71b93fb` |

Lane tip at filing: `d71b93fbadde05319f1645842d24b6e21b354a62` (`git ls-remote origin
refs/heads/master` prints the same hash; `jj-lane.sh state` reports `ahead=0 behind=0`). The twenty-five lane
commits between `aeeef067` and this tip are all ancestors of it.

## Before → after measurements

- **C1.** `python3 -I quality/counters/c1-r77-barfoot.py --repo . --rev REV --controls
  .ufo/waves/round-77/controls/c1-cases-r77.json --scratch-root DIR` — at base `aeeef067` the
  join does not exist (0 layer-plane rows; the live-echo control scores `8/15`); at the final measured tip `d362908b` (C1 counter's last change `de627316`, tool `9197405c`): `cases=15 correct=15 mutants=5
  killed=5 base_correct=8/15 tool_selftest=18/18 verdict=TARGET_MET` rc 0
  (`tool_sha256=e54787b7…`). Bounded `10 × 15/15` → 10.0000 on this finite set.
- **C2.** `python3 -I quality/counters/c2-r77-runbook.py --repo . --rev REV --controls
  .ufo/waves/round-77/controls/c2-runbook-cases-r77.json` — at base the table is a dated record
  (the read-the-table control reports `executed=0`); at its instrument's last change `bce906f3` and at the final measured tip `d362908b`: `cases=12 executed=12 matched=12 unexecuted=0 anchors=12/12
  verdict=TARGET_MET` rc 0, run from a non-session shell. Bounded `10 × 12/12` → 10.0000.
- Counts re-measured at the landing tip: gate `MADO_SELFTEST: 460/460`; index 96/96; ledger
  140/140 (`uncovered=0 bad_pointer=0`); axis `checked=3 mismatched=0`; census exit 0; cited probe
  green on the corrected r76 row.

## Sources & frontier

`SOURCES.md` 393 → 400 rows. Census command:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`
— before: exit 0 (W04 duplicate-URL warnings only); after: exit 0 (the same class, S458 sharing
the HyprCtl.cpp URL with earlier rows). Rows added by tier: seven tier-A mined (S457 Hyprland
`Renderer.cpp`, S458 `HyprCtl.cpp`, S459 `ReservedArea.cpp`, S460 the layer-shell XML — all at
`efb5099`; S461 the installed `waybar(5)` 0.15.0; S462 Waybar 0.15.0 `bar.cpp`; S464
gtk-layer-shell v0.10.1 `layer-surface.c`), one tier-C rejected (S463 wayland.app, no revision
pin; flip recorded). Rows touched old→new: none (no
status, recheck or used-by edit to an existing row). Frontier rows advanced: the layer plane and
the reserved-band join move from point-sample mentions to a measured surface
(`corpus/knowledge/bar-footprint-r77.md`, index 95 → 96), and the read-only probe table moves
from a dated record to an executed checklist. **Assimilation: none** — the connector's scan finds
`considerthese/2026-10-28.md` proposal 4 (the live-tool table) still unimplemented and justified
as round-78 work; absorbing it now would change `quality/` bytes and the ledger grammar after
the freeze.

## Trend verdicts

- **expansion: improved** — one new entry on ground the coverage map did not hold (the layer
  plane plus the reserved band; index 95 → 96), six mined source rows, and a new measured
  surface. Qualification: one host, one bar; no rendered-output claim.
- **quality: improved** — both claims meet their frozen targets at their instruments' last
  changes (15/15 with 5/5 mutants; 12/12 executed and matched), the base controls miss (8/15 and
  `executed=0`), the gate stays 460/460 at unchanged bytes, and QUALITY 132–134 land from the
  round's mistakes and the wave scout's findings. The wave's two hardening repairs (refusals;
  session-env discovery) each carry a red/green receipt.
- **discernment: improved** — the wave's scout found two real model gaps and both are now
  refused; the connector counted the stale-revision class at nine instances in ten rounds and the
  round lands the first in-class check with a red/green pair on the r76 row itself; six mined
  mistakes each carry a red/green or a re-derivation. Qualification: the standing-gate wiring and
  proposal 4 are deferred, and the closure must judge whether the red/green pair is enough.
- **Wave qualification.** The wave's reviewer and mutation tester found the C2 matcher's rc-blindness
  (repaired with a red/green and QUALITY 135), the constructed-mutant comma (repaired to an
  oracle-based kill), and three frozen-set coverage gaps (right edge, bottom-declared level lookup,
  exclusion-only output) that are named and carried to round 78 rather than re-cut post-score; the
  critic's two predicate/disclosure findings are dispositioned by declaration errata; the revenger's
  nine byte/claim findings are repaired with receipts. The reviewer also names the post-freeze repair
  drift explicitly (the declaration now says a reader must pin a revision), and three seats settled
  mid-work with partial evidence (disclosed above, never backfilled).
- **axes:** coverage (C1) and operability (C2) improved; calibration unchanged (axis table
  re-derived 3/3); freshness unchanged (the host register was not re-derived this round);
  adjacency unchanged (no sibling surface written; the connector confirms no collision). No axis
  harmed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the canonical gate registry gains four r77 rows and the read-only probe table now has an executable form; `SKILL.md` gate registry, `quality/counters/c2-r77-runbook.py`; no outside-lane promotion evidence this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the read-only probe table ran end-to-end (12/12) and the bar-footprint join ran on live captures (box MATCH, reserved EQ); `LOG.md` round-77 entry, `receipts/measurement-final-r77.txt`; the closure is not an outside-lane verifier for promotion.
- [~] Instructions executable by an agent without oral context — the frozen case sets, both counters and their selftests are in-repo (`--selftest` 15/15 and 9/9); dispatched seats do not count as outside-lane promotion evidence.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the `PROVINCE.md` round-77 refinement names the instrument surfaces and no new write surface; the connector's 20-repo scan found no sibling claim (0 `hyprctl layers` hits); outside-lane approval still absent.

## Wave disclosures (per seat)

All twelve seats were spawned in one v1 wave at `2026-11-04T05:00:30-03:00`; every seat below
settled through the dispatcher's handoff. A seat whose output is empty or partial is an evidence
gap, never backfilled (QUALITY 115).

| Seat | Role | What it returned and what was done |
|---|---|---|
| `R77ScoutSources` | scout | Anchor table for every modelled branch (levels, arrange anchors/margins, `applyExclusive`, reserved composition, reply fields, waybar margin precedence/anchors/exclusive) with the gaps the declaration missed: F1 pixel-size vs logical box, F2 the unreachable auto branch, F3 `mode` presets, F4 centring rounding, F5 static `addreserved`, I2 the opposite-edge margin. F1/F2 fixed as refusals (red/green `receipts/repair-r77-tool-refusals.txt`); the rest named in the entry. |
| `R77ConnSiblings` | connector | 20-repo scan: no sibling claims the layer plane (0 `hyprctl layers` hits); the stale-revision class measured at nine instances in rounds 68–77; `considerthese/2026-10-28.md` proposal 4 (live-tool table) still unimplemented and deferred to round 78 with reasons. |
| `R77ExecRepairs` | executor | D1/D2/D3/D4 repair pack, the landed-state verification, and the cited-revision probe (red on the r76 row, green on the corrected row); its D3 finding (the superseded mutant list) landed as a text-only fix with a parity run. |
| `R77Critic` | critic | Falsified the design: C1 is a coverage move (no `barfoot`/`footprint` at base), best alternative control 8/15, constants ≤5/15, C1/C2 separable. Findings F1 (C2 predicate overclaim → declaration erratum), F2 (`reserved-wrong-edge` replacement was a tuple crash → fixed to a valid dict, `correct=10/15` oracle kill), F3 (source provenance uncommitted at scan → landed), W1/W2 watch notes. |
| `R77RevBytes` | revenger | Byte audit: seven fetches and the live join re-derive byte-identically. Found and had fixed: the gate row's `NOT_MODELLED` exit map, the docstring's false "refused" for `mode` (now refused), the entry's anchor-attribution error, the S463 quote (not literal) and the S461 rendered quote; a second round caught S464's uncommitted bytes/manifest, the seven-source wording, range drift and the stale SCORECARD revision. All fixed with receipts. |
| `R77ScribeEntryC1` | scribe | Drafted the C1 entry and audited the committed one: flagged the `gls:` citation outside the registry (fixed by opening S464), the manual's line pins (corrected), and confirmed every measured number. |
| `R77ScribeSources` | scribe | Independent re-fetch and quote/anchor verification of all seven rows, both counters re-run at the freeze and the hardened tip, the census re-run: all agree; its stale-SCORECARD-pointer finding is the same class the cited-revision probe now checks. |
| `R77Mutant` | mutation-tester | Thirteen own mutants (ten killed, one proven equivalent) and three named frozen-set gaps (right edge, bottom-declared level lookup, exclusion-only output) carried to round 78; its C2 attack found the matcher's rc-blindness, repaired with the `rc == 0` guard and QUALITY 135. |

| `R77ExecTool` | executor | **Dead seat (honest record).** Settled mid-work with an empty write directory and no report
(`outlen=94`: "Now building the patched copy…"); its scratch was removed. No output is claimed from it; the
tool review it was chartered for was covered by `R77RevClaims`, `R77Mutant`, `R77RevBytes` and the L1's own repairs. |
| `R77ExecCases` | executor | **Partial seat.** Settled mid-work after writing six candidate case triples
(`outlen=154`: "Now writing the six case triples…"); no report. The triples are kept as wave evidence and were not
run into the frozen set; the mutation tester's three named gaps carry the same ground. |
| `R77ExecLive` | executor | **Partial seat.** Settled mid-work after the t0 capture (`outlen=729`), which shows the
committed tool CLEAN on t0 and selftest 18/18; no t1 pair and no report. Its t0 evidence is kept, never backfilled;
the L1's committed live run and `R77RevBytes`' re-derivation carry the live claim. |

Wave summary: 12 seats spawned and settled (dispatcher `w1-results.json`, `quality/check-wave-done.py --round 77`
→ `settled=1 verdict=OK`); 9 report-bearing seats, 3 partial/dead seats named above; attack seats 4/12 (reviewer,
critic, mutation-tester, revenger). No seat was replaced.


## Stale-lane

Respawn-per-round driver; this lane has no other mission open. Mission launched 2026-11-04
04:47:56 and the report is filed at 05:5x after the freeze, twenty-five lane commits (`git rev-list --count aeeef067..d71b93fb` = 25), the measurement
and harm receipts, the landing-green run and the settled wave (WAVE-DONE at 05:50) — visible
activity throughout, grading **progressing**. No other mission of this lane is open.

## Routed-defect dispositions (round-76 spot-check)

D1 → append-only provenance trio in both r76 entries (`3e35d0a9`). D2 → SCORECARD correction
(`3e35d0a9`) plus the executable cited-revision probe (`cb8d559d`, red/green). D3 → declaration
errata (`3e35d0a9`) and the counter's docstring example, limits line and mutant list
(`3e35d0a9`, `8722d564`), each with a parity run. D4 → the lesson correction and the LOG
correction (`3e35d0a9`, `adf8875b`). D5 → this section's Stale-lane line. D6 → the three r76
handoff files committed at `e4717a1c`. D7/D8 → the r76 lesson correction block naming the
superseding locations and their commands (`3e35d0a9`).

## Tool installs

None: no pacman transaction, no `uv`/`npx`/binary install. The two pinned source trees were
cloned read-only under `/fast/scratch/hyaku/mado-r77/l1-src/` for source ground and were removed
with the lane's scratch after landing.
