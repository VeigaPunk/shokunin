# mado — round 78 report (hyaku run 15, attempt 1)

Lane: mado-shokunin · round 78 · base `f597eccbffefd5fd6bbb01f3511c88bbeaed493c` · landing tip
`a6ed9867afc83ab0a66372c8df6c4fea484147f0` · measured `35cfa614e2ad5c8398721724e60ee4c9aae4e1eb`
· report filed after WAVE-DONE (`w1-results.json`, 13/13 seats settled).

## Work performed

**Declared claims (2, frozen before data; `.ufo/waves/round-78/claims-declaration-r78.md`):**

1. **C1 — coverage.** The margined auto exclusive-zone composition becomes a modelled join:
   `tools/mado-barfoot.py` derives `expected = extent + margins[opposite edge]` from
   gtk-layer-shell's client auto zone (allocation plus the unanchored edge's margin,
   `layer-surface.c:264-288`) plus Hyprland's anchored-edge margin (`Renderer.cpp:2575-2583`);
   eighteen frozen cases, seven named mutants, the held round-77 model as the do-nothing control.
2. **C2 — operability.** The read-only `SKILL.md` runbook binds twelve of its seventeen rows by
   shape (regex, integer range, JSON field schema, sorted-unique list) with committed churn and
   negative fixtures, validates the two bar captures as dump rows, and is bound to each row's
   command cell; the held fixed-value rule is the control.

- **C1 instrument and evidence.** `tools/mado-barfoot.py` `r78-v2` (sha256 `1bceb514…`) composes the
  margined band, refuses a negative margin, and — after the wave — follows waybar's two `output`
  branches, `std::stoi` margin parsing, Hyprland's single rounding of the centred box and the empty
  reserved area of an overflowing bar. `quality/counters/c1-r78-margins.py` scores the eighteen
  cases, kills seven single-anchor mutants and scores the base tool:
  `receipts/measurement-final-r78.txt`, `receipts/control-baseline-c1-r78-frozen.txt`,
  `receipts/repair-r78-tool.txt` (six red-before/green-after fixtures from the scout).
- **C2 instrument and evidence.** `quality/counters/c2-r78-runbook.py` runs seventeen frozen read
  verbs, binds each to a `SKILL.md` table row's command cell, and scores live output plus committed
  churn and negative samples; `receipts/measurement-final-r78.txt`,
  `receipts/control-baseline-c2-r78.txt`.
- **Knowledge and frontier.** `corpus/knowledge/bar-footprint-margins-r78.md` (merged from the
  scribe's draft plus the live join), the index row and frontier bullet in `corpus/README.md`, the
  r77 entry's appended erratum, and the eight `used-by` cells that cite the new entry.
- **Host ground (read-only).** The declared zero-margin bar joins CLEAN (DP-1, level 2, box
  0,0,3440,26, `reserved [0,26,0,0]`); a margin-4 fixture declaration predicts `box=4,4,3432,26`
  and band 34 against the live 26 and reports DIFFER where the r77 tool returned UNMODELLED
  (`receipts/live-join-r78.txt`; both captures reduced to the fields the join reads).
- **Wave.** One v1 wave, 13 seats (scout 1, connector 1, executor 4, scribe 2, reviewer 2, critic
  1, mutation-tester 1, sentinel 1; attack share 5/13), validated by `ufo-swarm-wave.mjs plan`
  (`spawn=13`, band 8-16) and dispatched through the inline handoff (`w1.ready` →
  `w1-dispatch.json`). Outcomes in **Wave disclosures**; evidence under `.ufo/waves/round-78/w1/`.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: tool, two counters, frozen case sets and generators, declaration, control baselines, SKILL probe rows, ledger rows | round-78 | `b8508bd9` |
| pre-wave amendment: three fixture boxes and one churn sample corrected | round-78 | `44a36b64` |
| wave w1 spec, validated dispatch (13 seats), ready handoff | round-78 | `00ed4ac0` |
| ledger row single line; round fetch receipts (seven sources) | round-78 | `fa6f3fda` |
| C1 knowledge entry, index row, frontier bullet; used-by for eight rows | round-78 | `93a10a13` |
| privacy: JSON probes never quote a dump; reduced monitor capture; live join | round-78 | `90fc8d84` |
| C2 receipt at `90fc8d84` | round-78 | `e117a113` |
| connector findings: registry row, index row, r77 erratum, row-bound anchor check, declaration provenance | round-78 | `d27c5ff4` |
| SCORECARD block, LOG entry, lesson, registry counts | round-78 | `0bba350f` |
| measurement receipts at `d27c5ff4` | round-78 | `3eb518a5` |
| C2 matcher hardening from the wave attack | round-78 | `aea5409e` |
| wave dispositions: declaration limits, lesson findings, registry counts | round-78 | `f7c9bf9b` |
| generator docstring; base control on the frozen set (8/18) | round-78 | `307c125a` |
| serial redaction and harm-watch receipt | round-78 | `edb4159b` |
| tool `r78-v2` repairs (output/margin/centring/overflow) and receipt; entry and registry | round-78 | `b774f920` |
| scorecard/declaration repair notes; measurement at `b774f920` | round-78 | `9d6cdb15` |
| privacy pass: reduced layers capture, redacted seat copies, child `TMPDIR`; critic dispositions | round-78 | `88486da1` |
| lesson wave findings; C1 receipt | round-78 | `e3744771` |
| final measurement and harm watch | round-78 | `fb63bee1` |
| wave evidence: eleven seat reports, receipts and the relocated scout fetches | round-78 | `a5b13b4b` |
| r77 routed defects D1-D13 dispositioned; r77 selftests at the tip; r77 scratch removed | round-78 | `969fa30e` |
| wave results (13 seats settled) | round-78 | `35cfa614` |
| final measurement at `35cfa614`; scorecard measured revision | round-78 | `a6ed9867` |

Every row above is recorded in `LOG.md` under `## Round 78` (the freeze/amendment/wave commits are
named there by subject and date as they landed; the LOG entry covers the round's changes as one
entry, per the append-only format).

## Before → after measurements

**C1 — coverage.** Counting command:

```sh
python3 -I quality/counters/c1-r78-margins.py --repo . --rev REV \
  --base-rev f597eccbffefd5fd6bbb01f3511c88bbeaed493c \
  --controls .ufo/waves/round-78/controls/c1-cases-r78.json --scratch-root DIR
```

- before (base `f597eccb`, held r77 model): `cases=18 correct=8 mutants=0 killed=0 base_correct=8/18
  tool_selftest=18/18 verdict=TARGET_MISSED` rc 1
  (`receipts/control-baseline-c1-r78-frozen.txt`).
- after (measured `35cfa614`, tool sha `1bceb514…`):
  `MADO_R78_BARFOOT: cases=18 correct=18 mutants=7 killed=7 base_correct=8/18 tool_selftest=28/28
  verdict=TARGET_MET` rc 0 (`receipts/measurement-final-r78.txt`).

**C2 — operability.** Counting command:

```sh
python3 -I quality/counters/c2-r78-runbook.py --repo . --rev REV \
  --controls .ufo/waves/round-78/controls/c2-runbook-cases-r78.json --scratch-root DIR
```

- before (base `f597eccb`): rc 2, `anchor 'hyprctl activeworkspace' … not in SKILL.md`
  (`receipts/control-baseline-c2-r78.txt`).
- after (measured `35cfa614`): `MADO_R78_RUNBOOK: cases=17 executed=17 matched=17 shapes=12/12
  anchors=17/17 control=5/17 mutants=5 killed=5 verdict=TARGET_MET` rc 0
  (`receipts/measurement-final-r78.txt`).

**Harm watch at the measured tip.** gate `MADO_SELFTEST: 460/460`; index 97/97; instrument ledger
142/142; axis table `checked=3 mismatched=0` (navigation 97/97, calibration resolved-active 86/86,
operability selftest 12/12, ledger 142/142); used-by green (401 rows, 97 entries, 0 missing/extra/
stale); session material 291 findings at both base and tip with none on a round-78 path; census
exit 0 (`mado ok …/corpus/SOURCES.md`, with the standing W04 duplicate-URL warnings and one
`W01 S277 tierC mined`).

## Sources & frontier

- **Rows before → after:** 401 → 401 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  corpus/SOURCES.md`); no row added, no id reused; census exit 0 at both ends
  (`receipts/census-{start,end}-r78.txt`).
- **Rows touched old → new:** eight `used-by` cells gain
  `corpus/knowledge/bar-footprint-margins-r78.md` (S457, S458, S459, S460, S461, S462, S463, S464);
  each old→new pair is in `corpus/lessons/round-78.md` (Gate section). No status or recheck change.
- **Rows added by tier:** none (A 386 / B 7 / C 8 unchanged).
- **Frontier rows advanced:** the seven rows the claims rest on were re-opened this round with
  fresh pinned fetches (`.ufo/waves/round-78/fetch/`, `sha256-r78.txt`; the six code files are
  byte-identical to the r77 copies), S463 re-confirmed rejected, and the margined band moved from
  the frontier into `corpus/knowledge/`.
- `SOURCES: 401 → 401 rows; 8 rows touched (used-by only); 0 added; census exit 0 (W04 duplicate-URL
  warnings plus one W01 S277 tierC mined).`

## Trend verdicts

- **expansion — improved.** One new admitted knowledge entry on ground the coverage map did not
  hold (the margined band composition), citing re-opened `mined` rows S457/S462/S464 and indexed
  (index 96/96 → 97/97); the r77 entry is superseded on its margin limit by an appended erratum and
  a stronger entry.
- **quality — improved.** The tool's output/margin/centring/overflow models were repaired against
  the sources with a red-before/green-after receipt (six fixtures); the stale registry row, the
  contradicting index row and the r77 entry's present-tense claims about a superseded instrument
  were corrected (append-only where the record is history); no entry was left false or stale.
- **discernment — improved.** The round's gate decisions carry an admit/reject sample (admit
  S457/S464, reject S463); the wave's connector, critic, mutation-tester and sentinel broke the
  anchor leg, the freeze pin, the control pointer and the privacy surface, and every disagreement
  became a repaired instrument, a named limit, or a committed red/green receipt. The outside
  non-author closure remains the judgement; nothing here self-promotes.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the probe
  table executes as 17 rows (12 shape-bound) and the gate registry carries the two r78 instruments
  reading the current tool (28/28); historical assertion corpus/knowledge/executor-test-sufficiency.md.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the live join over reduced
  host captures and the seventeen-probe runbook are this round's end-to-end executions; no
  outside-lane verification.
- [~] Instructions executable by an agent without oral context — the declaration, registry rows and
  lesson name every command and path; an outside-lane verifier is still missing.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round touches only the lane's own
  instrument and record; PROVINCE.md unchanged.

## Wave disclosures

One v1 wave (`w1`), 13 seats, validated (`spawn=13`, band 8-16) and dispatched through the inline
handoff; `w1-results.json` records all 13 settlements. Reports are committed under `w1/`.

| seat | role | outcome |
|---|---|---|
| R78ScoutMargins | scout | reported; anchor table for every reachable declaration and six discriminating defects (F1-F4 repaired in `r78-v2`, F5-F7 named limits) |
| R78ConnSiblings | connector | reported; no sibling lane claims the plane; found the stale registry/index/entry claims, the ledger-red freeze, the time-bound r77 citation and the anchor hole |
| R78ExecC1Tool | executor | settled mid-work, no report; its partial output in `w1-results.json` (harness bug fixing) is kept, never backfilled |
| R78ExecC1Cases | executor | reported; 18/18 independent re-derivation, held r77 tool 8/18 |
| R78ExecC2Shapes | executor | reported; six accepted negatives plus the PATH-shim limit; two matcher repairs landed |
| R78ExecC2Cases | executor | reported; 17/17 live re-derivation; shared-anchor and silent-environment flags |
| R78ScribeEntry | scribe | reported; the C1 entry draft the landed entry is based on |
| R78ScribeSources | scribe | reported; registry delta (401→401, eight used-by cells), census and quote/locator checks |
| R78RevC1 | reviewer | reported; all counts reproduced, no crash kills, model read line-by-line, two provenance notes (both dispositioned) |
| R78RevC2 | reviewer | settled mid-work, no report; its partial output noticed the mid-wave counter change and is kept in `w1-results.json` |
| R78CritClaims | critic | reported; claim classification, control attacks, the freeze-event ruling, four next-freeze upgrades |
| R78MutC1 | mutation-tester | reported; 27 mutants, 16 killed, 11 survivors classified, the centring model gap (repaired) |
| R78Sentinel | sentinel | reported; the serial in fourteen pushed revisions, the `/tmp` write (fixed), env pass-through (named), pids in a capture (reduced) |

No seat was replaced and no seat output was backfilled; the two partial seats stay partial in the
evidence.

## Routed defects (round-77 spot-check D1-D13)

Dispositioned append-only in `corpus/lessons/round-77.md` (`## Corrections (round 78, append-only)`):
D1/D2 (the filed r77 report's registry arithmetic: 401 rows, six touched rows, twelve used-by pairs),
D3 (the r77 SCORECARD's final revisions: `9197405c` / `e54787b7…`), D4 (six mistakes, not five),
D6/D7 (the two scratch-only red halves are restated **not durable**; this round commits every red
run under the wave dir), D8 (S460's quote is at `set_margin :193-200`, line 196), D11 (seven mined
rows), D12 (W04 and W01 classes), D13 (r77 counters' selftests 15/15 and 9/9 at the tip). D5 (the
missing `R77RevClaims` row) and D10 (the r77 report rewrite) are named here; this report is filed
once. D9: `/fast/scratch/hyaku/mado-r77` was removed at 06:51.

## Stale-lane

Mission open since 06:08 (`2026-11-04T06:08:41-03:00 launch mado round=78`), inside the two-tick
window; activity is observable (23 lane commits and the wave's seat writes under
`.ufo/waves/round-78/`), so the mission is **progressing**, not silent.

## Tool installs

None. No tool was installed or upgraded and `pacman` was not run; the probes used the host's
existing `hyprctl`, `jq`, `pgrep`, `makoctl`, `omarchy` and `python3`.

## L0

One question appended: `mado | round-78 |` the host monitor serial that reached fourteen pushed
revisions (operator-owned history decision; the working tree, the tip and every seat copy are
redacted). Routed around; not blocking.
