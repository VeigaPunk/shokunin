# kaidoku — round 98 report (attempt 1, L1 KaidokuR98)

Lane `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, branch `main`. Base `d0aebc288621b0072ac3eb2a79a62ad26bfa837a` → final `f6cdcabc1e53bee7c22a6161da5facb818103b54` (`git ls-remote origin refs/heads/main` prints `f6cdcabc1e53bee7c22a6161da5facb818103b54`).

## Work performed

Declared claims (2), frozen at `69c581c7ca0c4ea2b58303669aab3700797277f9` (`plans/round-98-claims.md`) before either candidate existed:
- **R98-C1 — coverage, frontier → core, also a capability:** UPX 5.2.0 `--best` packed PE (win32/pe, win64/pep) with a zeroed PackHeader `UPX!`, renamed `UPX0`/`UPX1` sections, or both, is repaired so the packer unpacks it again. Sourced claim: S324 (UPX 5.2.0 `src/pefile.cpp`, opened this round). Stagnation nudge applies: every owned axis was recorded at 10.0.
- **R98-C2 — calibration:** the stop-boundary counter accepts its own honest verdict again. This is routed defect 1 of the round-97 non-author closure (`corpus/lessons/round-97-verifier-spotcheck.md` §7).

Work items:
- Frozen C1 counter `tools/round-98/pe-upx-tamper-battery.py`. It uses six sha256-pinned PE carriers × three tampers, plus intact and refused arms. The oracle is `upx -d` sha256 equality with the untampered pack. Do-nothing controls ran at base: `.ufo/waves/round-98/pre/c1-identity-control.json` and `c1-r87-control.json` (commit `69c581c7`).
- Frozen C2 counter `tools/round-98/allowlist-check.py` with four legs: public, real14, stub9, extra. The v7 control is `.ufo/waves/round-98/pre/c2-v7-control.json` (commit `69c581c7`).
- Candidate `tools/round-98/upx-pe-repair.py`. It finds the PackHeader in the `canUnpack0` windows by checksum, requires exactly one candidate, and restores the magic and the names. Candidate `tools/round-98/stop-boundary-repair-battery-v8.py` is v7 with the 14-key allow-list and a nine-key-stub selftest case (24/0). Both landed in `72346895a35a74af18151b125934fa0c09fe1e3c`.
- Knowledge entry `corpus/knowledge/2026-11-05-r98-pe-upx-tamper-repair.md`, plus the README coverage-map row, knowledge-index row and Round-98 frontier note (`corpus/README.md`). Also S324 (`corpus/SOURCES.md`), QUALITY rows 198–199 and the capability row (`SCORECARD.md` `## Capabilities`). Commit `9cb930014a57c9b29d830739e0c4229f6e7e7016`.
- Wave `r98-w1` with 13 seats. Its reports are in `.ufo/waves/round-98/w1/` and its results in `.ufo/waves/round-98/r98-w1-results.json`. I integrated the corrections the seats found into the entry and the frontier note, recorded the counter limits, added S325 (rejected), and wrote the lesson `corpus/lessons/round-98.md`, the SCORECARD section and the LOG entry. Commit `f6cdcabc1e53bee7c22a6161da5facb818103b54`.

## Landed changes

| commit (`landed` line of `jj-lane.sh`) | content | LOG.md entry |
|---|---|---|
| `69c581c7ca0c4ea2b58303669aab3700797277f9` | freeze: plan, both frozen counters, identity control, control receipts, census-start | `LOG.md` `## 2026-11-05 — round 98` (Declaration and landing) |
| `72346895a35a74af18151b125934fa0c09fe1e3c` | candidates `upx-pe-repair.py`, `stop-boundary-repair-battery-v8.py` | same entry (Declaration and landing) |
| `9cb930014a57c9b29d830739e0c4229f6e7e7016` | knowledge entry, S324, README rows and frontier note, QUALITY 198–199, capability row, landing receipts | same entry (Sources, Capability) |
| `f6cdcabc1e53bee7c22a6161da5facb818103b54` | wave evidence, lesson, S325, entry/frontier corrections, SCORECARD section, LOG entry, census-end | same entry (Wave, Mistakes) |

## Before → after measurements

- **R98-C1**, measured at `72346895a35a74af18151b125934fa0c09fe1e3c`. Command: `python3 -I -B tools/round-98/pe-upx-tamper-battery.py --repair-cmd <cmd> --work <scratch> --json-out <receipt> --rev <rev>`.
  - Before: the identity control scored `recovered 0 of 18; intact 6 of 6; refused 0 of 2; effective 18 of 18` (exit 1). The held ELF repair scored `recovered 0 of 18; intact 0 of 6; refused 2 of 2; effective 18 of 18` (exit 1).
  - After: `recovered 18 of 18; intact 6 of 6; refused 2 of 2; effective 18 of 18`, exit 0 (`.ufo/waves/round-98/l1/scores/c1-at-72346895a35a74af18151b125934fa0c09fe1e3c.json`). Reproduced in a clone by ExecReproC1.
  - **Verdict: verified on the frozen predicate, with a named limit.** The battery also admits three forgeries at the full label: a size-keyed cache, a lazy anchor, and a validated fixed-offset patch (`w1/CriticC1.md` f2/f7/f1h). All six carriers share the PackHeader offset 992. The repair's substance rests on evidence outside the predicate:
    - 48/48 out-of-population cells on three unpinned carriers × four modes (`w1/ExecHeldOut.md`).
    - The candidate refuses a checksum-valid decoy that the lazy forgery accepts (CriticC1 V2).
- **R98-C2**, measured at `72346895a35a74af18151b125934fa0c09fe1e3c`. Command: `python3 -I -B tools/round-98/allowlist-check.py --counter <counter> --rev <rev> --work <scratch> --json-out <receipt>`.
  - Before: v7 scored `legs passed 1 of 4; public 0; real14 0; stub9 0; extra 1` (exit 1).
  - After: v8 scored `legs passed 4 of 4; public 1; real14 1; stub9 1; extra 1`, exit 0 (`.ufo/waves/round-98/l1/scores/c2-at-72346895a35a74af18151b125934fa0c09fe1e3c.json`; the counts come from v8's own public receipt). Reproduced by ExecReproC2. The v7→v8 diff is confined to the allow-list, the TOOL constant, the selftest and docstrings (ExecReproC2, ReviewerV8).
  - **Verdict: verified on the frozen predicate, with a named limit.** The public leg trusts the candidate's printed `selfverify ok=True` (CriticC2 F2/F3). A length-only `count_problems` (F5) and the inverted-`ok` mutant M6, which survives through a dirty-tree confound (MutationC2), are also admitted.
- **Harm check.** Coverage proxy (`tools/round-66/coverage-selfcheck.py --selfcheck --rev <rev>`): 175/181 at base, 176/182 at `9cb93001`, both 9.67. Depth rule blocks: 36 resolved at both (`.ufo/waves/round-98/l1/scores/coverage-selfcheck-at-*.json`). Neither axis is harmed. That base receipt also shows a **pre-existing calibration mismatch**: the SCORECARD coverage head claims 10.0 and 168/168, while the r93–r97 entries have no coverage-map rows. I did not repair it (it was not claimed); it is routed to round 99.

## Sources & frontier

- SOURCES rows went from 228 to 230. Counting command: `grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md` (base `git show d0aebc28:corpus/SOURCES.md` → 228, final → 230).
- Rows added by tier: S324 tier A (code, admitted, `mined`); S325 tier C (community, `rejected`, reason and flip in the row). Rows touched old→new: none.
- Census start, `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`: exit 0, `kaidoku ok` (`.ufo/waves/round-98/pre/census-start.txt`). Census end: exit 0, `kaidoku ok`; the only warnings are W04 duplicate-URL warnings that already existed (`.ufo/waves/round-98/l1/census-end.txt`).
- Frontier advanced: the Round-98 note moves the "packed PE" half of the round-92/76/77 "PE and Mach-O packed inputs" clauses to Core, for the bounded class only (`corpus/README.md`, Round-98 frontier note). Mach-O, PE DLLs, other offsets, `UPX2` sections and truncated payloads stay Frontier. ARM64 and .NET PE are pack-time refusals in UPX 5.2.0 (S324 lines 141-142, 2207-2208).
- Sourced claim: R98-C1's entry cites S324, which was opened this round.
- Mistake mined (`corpus/lessons/round-98.md` `## Mistakes`): M98-a, a false absence statement. Rounds 93–97 said `merge/kaidoku/` was absent, but `test -e /home/vgpnk/Projects/shokuknow/merge/kaidoku; echo $?` prints `0`. The fix is QUALITY 198, shown able to fail. Also mined: M98-b–f.
- `Assimilation: none`. The package `/home/vgpnk/Projects/shokuknow/merge/kaidoku/` exists (132 staged rows, 2026-10-24), but no entry was taken because the claim cap went to the PE frontier and the routed repair. The lane has no `considerthese/` directory (`test -e` → 1), and no `corpus/lessons/operator-*.md` exists.

## Trend verdicts

- **expansion: improved.** Packed PE enters the coverage map (`corpus/README.md` round-98 row) and the capabilities table (`SCORECARD.md` `## Capabilities`, round 98). This ground was Frontier at base (`corpus/README.md` round-92 note).
- **quality: improved.** The stop-boundary counter's honest public run is accepted again (v7 exit 1 → v8 exit 0). The PE repair generalizes out of population (48/48). Both new counters carry named forgery-admission limits (`corpus/lessons/round-98.md` `## Verdict first`).
- **discernment: improved.** The gate refused S325 and four duplicate or uncited drafts. The round also surfaced two of the lane's own earlier false statements: M98-a, and the stale coverage head (`.ufo/waves/round-98/l1/scores/coverage-selfcheck-at-d0aebc28….json`).

## SHONEN

- [~] box 1 "SKILL.md contains real decision tables, error patterns, checklists, cited sources": `corpus/knowledge/2026-11-05-r98-pe-upx-tamper-repair.md` (repair rule, measurement table, limits, cited S324/S308/S309); SKILL.md not edited this round; lane-asserted, no non-author verifier.
- [~] box 2 "At least one end-to-end domain task executed and logged in LOG.md": `LOG.md` `## 2026-11-05 — round 98` (pack → tamper → repair → `upx -t`/`upx -d` on 18 cells plus 48 out-of-population cells); lane-asserted.
- [~] box 3 "Instructions executable by an agent without oral context": the commands in `plans/round-98-claims.md` were re-run from a clean clone by ExecReproC1 and ExecReproC2 (`.ufo/waves/round-98/w1/ExecReproC1.md`, `ExecReproC2.md`); lane-dispatched seats, so not non-author.
- [ ] box 4 "No cross-domain bleed (PROVINCE.md still accurate)": untouched; `PROVINCE.md` not edited. ConnectorOverlap found no sibling lane holding UPX-PE knowledge.

## Round shape and housekeeping

- **Round shape:** one v1 wave `r98-w1`, 13 seats, validated under `ufo-wave-policy.json` (band 8–16, `counts {spawn 13, total 13}`).
  - Role mix: executor 3, scout 1, scribe 1, connector 1, reviewer 2, critic 2, mutation-tester 2, sentinel 1.
  - Attack share: 6/13 (46 %). Connector seats: 1.
  - The L1 held the planner seat, because the validator rejects `planner`.
  - No residual call. Round total: 13 seats.
- **Dead seats:** none died with an error. All 13 settled, but ReviewerRepair ended without a report; its output stops mid-probe in `r98-w1-results.json` (M98-f). It was not replaced.
- **Earlier round-97 defects:** 1 is closed by R98-C2. 2–5 and 7 are open; 2 was missing from the plan's not-claimed list (ReviewerV8 F2). 6 is partly answered (`corpus/lessons/round-98.md` `## Routed defects`).
- **Inherited state:** attempt 1. There is no `lane-dead-no-report kaidoku round=98` line, and the lane was clean at `d0aebc28`.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists `.scratch/run15-kernel.py`, `.scratch/run15-state.json`, `.ufo/l0-questions.md` (modified) and `w4lines.txt` (untracked). None of them is this lane's, and none was touched.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none. No pacman, sysctl or namespace change by the L1, and no seat report names one.
- **Scratch:** `/fast/scratch/hyaku/kaidoku-r98/` removed at landing.
- **Open L0 questions:** none appended this round.

## Verdict for the operator

- I judge both claims verified on their frozen predicates, with named limits, and no axis harmed. The routed round-97 calibration harm (defect 1) is repaired.
- Both frozen counters admit forgeries that the wave built (CriticC1, CriticC2, MutationC2 M6). A closure may weigh that against admission; the evidence that the candidates do the real work sits outside the predicates: held-out 48/48, the decoy refusal, and the confined diff.
- Routed to round 99:
  - successor counters with the wave's forgeries committed as red fixtures before freeze;
  - the stale coverage head and the six unmapped r93–r97 entries;
  - the truncated-pack `ok intact` result and the three rc-1 CLI crash paths in `upx-pe-repair.py`;
  - round-97 defects 2–5.
