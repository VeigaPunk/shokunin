# tsukuroi — round 35 report (attempt 1, 2026-10-23)

Lane tip `c535371b4570a869bdadcf46c4d85187e96d4900` (branch `master`, pushed; `jj-lane.sh state`: ahead 0, behind 0). Claim base `b40c01df38eb26f74c095c471efc6d1649b00fd4`. Admission is for the non-author closure; the author verdicts below are C1 **not verified** (honest stop under its declared kill rule) and C2 exploratory, awaiting the named non-author reviewer.

## Work performed

Declared claims (`SCORECARD.md` "Round 35 — declaration, pre-freeze candidate", `6b4561e4`; redesign section, `7186722b`):
- **C1 (coverage, ordinal 9 → 9):** the census gains a pacnew/pacsave drift arm (one verdict-neutral `DRIFT pacnew-plane` line pairing the readable `/etc` sweep with `pacman.log` and reporting unreadable directories; surface `PROVINCE.md:21`). A different surface and counter shape from the rejected rounds 33-34 (fixture oracle and battery, not a tracer).
- **C2 (depth, exploratory, ordinal 8 → 8; lowest axis):** `corpus/knowledge/pacman-backup-files-r35.md`, how pacman 7.1 itself creates and logs `.pacnew`/`.pacsave`. Sourced claim: S191-S196, opened this round.

Work items:
- Repair first (round-34 spot-check §5): 22 leftovers landed as non-evidence records with a time table (`.ufo/waves/round-34/w2/UNINTEGRATED-AT-FILING.md`, `6b4561e4`); corrections for items 3-6 appended to `SCORECARD.md` and `corpus/lessons/round-34.md` (`7186722b`; verified by W2RevCorrections, no factual defect); item 2 receipted: VERSION 6 reads r33claim 8/15 and regression 22/33 on byte-identical tools (`.ufo/waves/round-35/w1/ExecV6Calibration/`); item 8 correction block appended to `coredump-count-unit-r34.md` and its recheck executed on systemd 262 (W2RevC2Remnants, W2ExecC2Remnants). **Still owed:** item 1 (untraced view; ExecProbeV7 cancelled with no output), the VERSION 6 normalisation fix, and item 9's five live-tool ambient copies (ExecAmbientA/B cancelled with no patch); RevHistoricalProbes found the six historical probes' copies are deliberate, pinned inputs (leave as evidence).
- C1 counter VERSION 1 (`tools/score-pacnew-arm-r35.py`, `6b4561e4`) was met pre-freeze by K08FixtureKeyed (24/24, role encoded in name length) and K15FieldMutants' unpaired-regex mutant (24/24); retired unchanged. VERSION 2 (`tools/score-pacnew-arm-r35b.py`, `7186722b`, sha256 `7517af92…`) adds namespace and live views, base parity and a 17-arm should-fail battery (QUALITY 73/82) and a kill rule fixed before it was scored. Wave 2 met it too: W2TreeKeyed (24/24, forced-FIFO signature plus constants), W2LogKeyed (24/24, first-warning gate), and W2LiveOracle's two live-view-gated cached arms (24/24 each); W2NsDetect reached the declared namespace limit. Evidence `.ufo/waves/round-35/w2/`.
- C1 change landed unverified: `tools/tsukuroi-census.sh` `probe_pacnew_arm`, seam `TSUKUROI_ETC_DIR`, four selftest cases (`e2f97e6e`); selftest 105/105 (`.ufo/waves/round-35/l1/r35-st-after2.txt`).
- C2 note integrated from ScribeC2Draft with W2QuoteHash/W2QuoteRemove/W2QuotePacdiff (every quote re-opened, none fabricated), W2CritC2Depth and W2RevC2Quality corrections (`95684c65`, recheck fixed `199beb97`).
- Freshness repair: `pacnew-plane.md` R35-FRESHNESS block (11 unreadable, pacman-contrib installed, `find` exit 1), from ExecHostPacnew and W2RevHostCapture (`95684c65`).
- Gates: four reds this round caused at `95684c65` were repaired at `199beb97` (lesson "Gates at the outcome commit").

## Landed changes

| Commit | Change | LOG entry |
|---|---|---|
| `6b4561e4` | pre-freeze declaration, counter VERSION 1, census start, round-34 leftovers as records | "Round 35 — declaration, pre-freeze candidate" |
| `7186722b` | VERSION 1 retired; VERSION 2 candidate counter; wave-1 evidence; round-34 corrections | "VERSION 1 met by a pre-freeze control" |
| `e2f97e6e` | C1 change: census drift arm, selftest cases; `SKILL.md` round35 registry and DRIFT reading rule | "C1 kill rule fired before the freeze" |
| `95684c65` | measured outcome, C2 note, S191-S197, pacnew-plane freshness, coredump remnants, lesson, axes table | "measured outcome, C2 note, sources" |
| `199beb97` | gate repairs (registry kinds, note recheck without pacman, IN-109 line, round-35 capabilities table) | "gate repairs after the outcome commit" |
| `6f92080d` | late wave-2 evidence, gates at `199beb97`, census end | "late wave-2 evidence" |
| `c535371b` | erratum: five LOG heading times were later than their commits | "erratum: LOG heading times" |

## Before → after measurements

- **C1:** `python3 tools/run-receipt.py --revision <REV> --tool-revision 7186722b -- tools/score-pacnew-arm-r35b.py --lane '{lane}' --revision '{rev}'` (battery mode). Before at `7186722b`: `candidate_matches` 0/24, `control_matches` 24, `should_fail_accepted` 0/17, exit 1 (`.ufo/waves/round-35/w2/W2BeforeBattery/before-battery-7186722b.jsonl`). After at `e2f97e6e`: 24/24, control 24, accepted 0/17, `harness_errors` [], exit 0 (`.ufo/waves/round-35/after/c1-after-battery-e2f97e6e.jsonl`). **Not verified:** four skip-work controls met VERSION 2 before the change existed (above). No freeze, no VERSION 3.
- **C2:** exploratory, no counter. Before: no entry read pacman's code for these branches (sweep in the note's Prior state). After: the note at `199beb97`.
- No-harm: census selftest 101 → 105 cases, all pass; base parity held in 20/20 after stub views; only `tools/tsukuroi-census.sh` changed among tools (`git diff --stat 7186722b e2f97e6e -- tools/`). Gates at `199beb97` (`.ufo/waves/round-35/after/gates-199beb97/`): self-assessment, registry-coverage, knowledge-header, recheck-commands, adjacency-anchors, report-red-causes exit 0; pause-gate exit 1 with the same P3 as base.

## Sources & frontier

`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`: start exit 0 (`.ufo/waves/round-35/l1/census-start.txt`), end exit 0, last line `tsukuroi ok …` (`census-end.txt`). Rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`) 190 → 197. Added by tier: A 7 (S191-S196 mined; S197 pacman master `add.c` **rejected**: not the installed version, flip on a later installed commit). Rows touched old → new: none. Re-opened unchanged: S010, S011 (W2CritGate: S011's "list all" is not authority for a complete log enumeration). Frontier rows advanced: none (`PROVINCE.md` Frontier unchanged). Mined mistakes: `corpus/lessons/round-35.md` `## Mistakes` (R35-V1-ROLE-LENGTH, R35-V1-QUALITY-73-82, R35-V2-FORCED-SHAPE-CONSTANTS, R34-MUTBINGITALIAS-HOLD, R35-SCORE-ONCE) plus R35-GATES-AFTER-OUTCOME and R35-LOG-TIME-ESTIMATES.

## Gate

Real reject: S197 (pacman `add.c` on master, sha256 `c63fb24d…`), rejected because it is not the installed 7.1.0.r9.g54d9411 source (lesson `## Gate`).

## Trend verdicts

- **expansion: `unchanged`.** The drift arm covers an already-owned surface and its claim is not verified; C2 is deeper ground, not new ground.
- **quality: `improved`.** Prior entries superseded or re-verified: `pacnew-plane.md`'s 12-unreadable and "pacdiff not installed" readings re-measured and superseded (R35-FRESHNESS); the NoUpgrade-as-pin grouping (`SKILL.md:397-399`, `update-safety-note.md:420-424`, `update-safety-v2.md`) superseded as a classification by a sourced note; the coredump note's three remnants corrected and its recheck executed.
- **discernment: `unchanged`.** For: the control waves caught both counter versions before data and the kill rule was applied against the author's claim. Against: VERSION 1 ignored the lane's own QUALITY 73/82, VERSION 2's fixed-count forced shapes were a label, the round's own gates were run only after the outcome commit, and the round-34 timestamp defect recurred.

## SHONEN

- [~] SKILL.md tables, patterns, sources: round35 registry and the `DRIFT pacnew-plane` reading rule (`SKILL.md`, `e2f97e6e`/`199beb97`).
- [~] End-to-end task: unchanged (`corpus/knowledge/host-health-report-r3.md`).
- [~] No-oral-context instructions: unchanged.
- [~] No cross-domain bleed: ConnSiblings and W2ConnAfter found no crossing (`.ufo/waves/round-35/w1/ConnSiblings.md`, `w2/W2ConnAfter.md`); not acknowledged by a sibling.

## Round shape, seats and holds

Shape: default two v1 waves (policy `ufo-wave-policy.json`), no residual call. Planner seat: held by the L1 (no planning data-walk seat). Wave 1 `tsukuroi-r35-w1`, 37 seats (14 mutation-tester, 9 executor, 7 scribe, 3 reviewer, 2 critic, 1 scout, 1 connector), dispatched 11:06:54Z. Wave 2 `tsukuroi-r35-w2`, 32 seats (12 mutation-tester, 9 reviewer, 4 executor, 4 critic, 1 connector, 1 sentinel, 1 scribe), dispatched 11:42Z. Round total 69. Hold: K09HarnessSnoop, "This content was flagged for possible cybersecurity risk … (code=cyber_policy)", not retried. Cancelled at settle deadlines: w1 at 11:49Z — K14PositiveArm, ExecSelftestBaselines, ExecProbeV7, ExecV6Calibration (its receipts had landed), ExecAmbientA, ExecAmbientB; w2 at 12:25Z — W2NsViewProbe (records only). Dead seats: none. Inherited state: no `lane-dead-no-report tsukuroi round=35` line; the only inherited files were the 22 round-34 leftovers (landed as records). Not committed (over 1 MiB): `.ufo/waves/round-35/w1/ScribeC2Draft/pacman-54d9411.tar.gz`, sha256 `830ab30f…c9a5a`. Misroot sweep: no fleet-root file names this lane; an unattributed file `0` (12:09Z, a table-cell check output) is left untouched ([unk]). Deviations recorded: ExecHostPacnew used `sudo -n find` outside the read-only allow-list (W2RevHostCapture); the L1 used `sed -i` once on `corpus/SOURCES.md` used-by cells before commit.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Tool installs: none. Open L0 questions: none.
