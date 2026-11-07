# mado — round 93 report (hyaku run 15, attempt 1)

L1 `MadoR93`. Lane `mado-shokunin`, branch `master`, base `4c6f723f3dca3a26f9d14475d695fe797e2e972c` (round-92 closure
tip), final lane hash **`28a97421a73d3205851634b0821c8f60ebc414df`** (`git ls-remote origin refs/heads/master` prints it).
No earlier attempt of round 93 (`.ufo/watchdog.log` has only `launch mado round=93 … attempt=1`); nothing inherited; the
lane tree was clean at start.

## Work performed

Declared claims (`mado-shokunin/.ufo/waves/round-93/claims-declaration-r93.md`, frozen at `65dac61b`):
**C1 — coverage (edge class):** `tools/mado-portals.py` reads xdg-desktop-portal 1.22.1's `portals.conf`/`.portal` bytes
as GLib 2.90.1 GKeyFile does — invalid UTF-8 checked per value read, raw name bytes, VT not whitespace, NUL as a C-string
end (round-92 spot-check routed defect 2). **C2 — operability:** `quality/check-selftest-strength.py`, a gate that prints
WEAK when a passing selftest assertion of the seat-report gate is weakened (routed defect 3). Sourced claim: C1 (S511–S514
opened this round).

- Protocol load and inputs: round-92 non-author spot-check (three routed defects), `considerthese/2026-11-06.md`
  (proposals 4 and 1), the round-92 lesson and R92MExecD1; GLib 2.90.1 `gstrfuncs.c`, `gstrfuncs.h`, `gkeyfile.c` and
  xdg-desktop-portal 1.22.1 `xdp-portal-config.c` fetched twice each by the L1 (`receipts/sources-open-r93.txt`).
- Wave w1 (13 seats) built and attacked: 71 byte cases and a bytes-writing oracle (R93MExecCasesC1), the C1 counter
  (R93MExecCounterC1), 74 C1 mutants (R93MMutC1), 53 review fixtures incl. the NUL class the round-92 port missed
  (R93MReviewC1 F1/F2), the gate and a 20-kill set (R93MExecGateC2), a C2 counter (R93MExecCounterC2), 19 gate mutants and
  six escapes (R93MMutC2), the C2 review (20/23 coverage, rc-blind counter; R93MReviewC2), the critic's forgeries and
  class-rule finding (R93MCritic), sources (R93MScoutSources: `portal-impl.c` 404 at the tag), overlap/assimilation/
  cross-domain sweep (R93MConnector), the entry draft (R93MScribeEntry), host replay (R93MExecHost).
- L1 integration before the freeze (all in `corpus/lessons/round-93.md` "Wave findings routed"): NUL C-string view and
  continuation-byte skip patched into the candidate (`build/mado-portals.c1.py`, sha256 `e46a861e…c021`); 366-case frozen
  set (`controls/merge-c1-cases-r93.py`); MB11 frozen after two distinguishing cases; exact-set kills (32) and a check-count
  pin in the gate; the C2 counter rewritten (verdict and exit code, 23 neutralisations, 16 weakenings, 6 neutral edits,
  14-probe setup panel, early-stop mutant probing); both counters pinned to the frozen candidates.
- Pre-freeze controls executed and committed in the freeze: C1 candidate DRAFT_TARGET_MET; base tool 318/366 and byte
  subset 32/80; label-table forgery 366/366 frozen but `fresh_bytes=50/60` (MISSED)
  (`receipts/c1-controls-prefreeze-r93.txt`); C2 DRAFT_TARGET_MET with do-nothing 0/39, always-OK 0/39, always-WEAK failing
  (i), sha-diff failing the neutrals 0/6 (`receipts/c2-controls-prefreeze-r93.txt`).
- Freeze `65dac61b0a3097d5f4f6f8ccf7444ea60ab27a77`; C1 `0a85e687048ae24f77f043b268794e408d0cc306`; C2
  `4fd3b292eb6a96c5c6e471728dbab9ff2a15b99a`; records `28a97421a73d3205851634b0821c8f60ebc414df` (gated by
  `quality/check-seat-reports.py --worktree --round 93` → 13/13 present and `check-receipt-presence.py` → 21/21 cited
  receipts present, `receipts/records-gate-r93.txt`).
- **Cross-domain evidence** encountered: GLib internals (gkeyfile.c, gstrfuncs.c/.h — GNOME/GLib domain), Python's
  `surrogateescape` handler (Python runtime), test-mutation methodology (kotoba runs `selftest-kills.py` for its own
  verifiers: `kotoba-shokunin/verifiers/fixtures/round-100/selftest-kills.py`, cited as method, not absorbed). No sibling
  lane owns any of them: R93MConnector §4 swept every sibling `PROVINCE.md` for `glib|surrogateescape|mutation-of-test|
  selftest-strength|meta-test` → `none` ×20; souji (`origin-record-format-gvfs-r40.md`) and tsukuroi (journal records of
  xdg-desktop-portal) mention the surfaces without owning them.

(Receipt paths are under `mado-shokunin/.ufo/waves/round-93/`.)

## Landed changes

| Commit | What | LOG.md |
|---|---|---|
| `65dac61b0a3097d5f4f6f8ccf7444ea60ab27a77` | freeze: declaration, frozen cases/mutants/panel/gate mutants, both counters, candidates, forgery, pre-freeze controls, assimilation check, w1 evidence and results | LOG round 93 "Landed" |
| `0a85e687048ae24f77f043b268794e408d0cc306` | C1: `tools/mado-portals.py` (= frozen candidate), `corpus/knowledge/portal-keyfile-bytes-r93.md`, S511–S514, PROVINCE/SKILL/ledger/index rows | LOG round 93 "Landed" |
| `4fd3b292eb6a96c5c6e471728dbab9ff2a15b99a` | C2: `quality/check-selftest-strength.py`, `quality/selftest-kills/check-seat-reports.json`, SKILL/ledger/PROVINCE rows | LOG round 93 "Landed" |
| `28a97421a73d3205851634b0821c8f60ebc414df` | records: lesson (M93-1…M93-6, Gate), QUALITY 155–158, SCORECARD round 93 + capability row, LOG entry, S511–S514 used-by, measurements, separability, harm watch, census end, records gates | LOG round 93 entry itself |

## Before → after measurements

- **C1 (coverage, edge class)** — `python3 -I quality/counters/c1-r93-portal-bytes.py --repo . --rev
  0a85e687048ae24f77f043b268794e408d0cc306 --base-rev 4c6f723f3dca3a26f9d14475d695fe797e2e972c --cases
  .ufo/waves/round-93/controls/portal-cases-r93.json --expect-cases-sha256 351072d1… --mutants
  .ufo/waves/round-93/controls/portal-mutants-r93-frozen.json --expect-mutants-sha256 7e45edc9… --oracle
  .ufo/waves/round-93/controls/portal-oracle-r93.py --expect-oracle-sha256 d50d88bf… --fuzz-bytes-gen
  .ufo/waves/round-93/controls/fuzz-bytes-r93.py --expect-fuzz-bytes-sha256 94fdfe8f… --expect-oracle-binary-sha256
  e1429fbe… --expect-tool-sha256 e46a861e… --fresh 120 --fresh-bytes 60 --scratch-root DIR` (full digests in the
  declaration and SCORECARD). Measured at `0a85e687`: byte-subset cases (invalid UTF-8/raw names, VT, NUL) answered as the
  installed xdg-desktop-portal does: base **32/80 → 80/80**; `TARGET_MET tool_pin=ok cases=366 correct=366 answered=366/366
  fresh=120/120 fresh_bytes=60/60 mutants=75 killed=75 crashed_not_killed=0`, controls do-nothing 35, r12 74, host-table 10,
  base 318 — `receipts/c1-measured-r93.txt`, rc 0. Separability: C1 at the C2 revision `TARGET_MET` (`receipts/c1-at-c2-r93.txt`).
- **C2 (operability)** — `python3 -I quality/counters/c2-r93-selftest-strength.py --repo . --rev
  4fd3b292eb6a96c5c6e471728dbab9ff2a15b99a --panel .ufo/waves/round-93/controls/selftest-panel-r93.json
  --expect-panel-sha256 a6d2cbe2… --mutants .ufo/waves/round-93/controls/selftest-gate-mutants-r93-frozen.json
  --expect-mutants-sha256 be676929… --expect-r92-counter-sha256 0aa4d1f1… --expect-gate-sha256 2d6f1219…
  --expect-kills-sha256 00befb3e… --workers 16 --scratch-root DIR`. Measured at `4fd3b292`: single-check neutralisations of
  the seat-report gate's selftest flagged by a lane instrument **0/23 → 23/23**; `TARGET_MET frozen_pin=ok positive=OK:0
  hand_flagged=16/16 neutral_ok=6/6 mutants=22 killed=22 crashed_not_killed=0 do_nothing_flagged=0/39 always_ok_flagged=0/39
  always_weak_positive=WEAK:1 shadiff_neutral_ok=0/6 gate_selftest=ok` — `receipts/c2-measured-r93.txt`, rc 0.
  Separability: C2 counter at `0a85e687` `SETUP_ERROR … gate/kill-set/tool absent`, rc 2 (`receipts/c2-at-c1-r93.txt`).
- Harm watch at `4fd3b292` (`receipts/harm-final-r93.txt`): gate selftest 460/460, `--no-live` CLEAN 29, index 114/114,
  ledger 179/179, portals 28/28, mime 17/17, xdgmime 12/12, mako 62/62 (the first mako line was a harness defect — missing
  scratch dir, rc 2 = setup error — corrected append-only in the receipt), seat-reports 23/23, receipt-presence 6/6,
  selftest-strength 11/11 and `OK kills=32 held=32`, round-90 C2 83/83 28/28, round-92 C2 45/45 with its round-91 leg; the
  round-90 C1 counter stops `SETUP_ERROR mutant M03 find occurs 0 times` on the ported tool, as the declaration states
  (its anchors are removed by the port; its receipt stays pinned at `7bec2399`; QUALITY 155). No axis harmed.

## Sources & frontier

- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`:
  start `mado ok` rc 0 (`receipts/census-start-r93.txt`); end `mado ok` rc 0, W04 55 → 56 (S514 shares S502's URL under a
  different scope), W01 1 (S277, as before) (`receipts/census-end-r93.txt`). Rows by `grep -cE '^ {0,3}\| S[0-9]{3,} '
  corpus/SOURCES.md`: 445 → 449.
- Rows added by tier: A 4 — S511 GLib 2.90.1 `gstrfuncs.c` (ASCII table), S512 `gstrfuncs.h` (`g_ascii_isspace`), S513
  xdg-desktop-portal 1.22.1 `xdp-portal-config.c` (key-read scope), S514 GLib 2.90.1 `gkeyfile.c` (byte-class scope); each
  fetched twice by the L1 with sha256 and a ≤25-word located quote in the lesson `## Gate`; R93MScoutSources reproduced
  every digest independently.
- Rows touched old→new: S511–S514 used-by `corpus/knowledge/portal-keyfile-bytes-r93.md` (C1) → `+corpus/lessons/round-93.md`
  (records). Logged in the lesson.
- Frontier: the byte edge of the portal plane moves to core (`corpus/README.md` round-93 frontier line; index 113 → 114);
  runtime and other GKeyFile consumers stay frontier.
- Mistakes mined: M93-1 (candidate moved under a running mutant sweep; fix shown able to fail — `tool_pin=FAIL` for base and
  forgery; QUALITY 155), M93-2 (unique-killer brief left 3/23 checks unguarded; fix shown able to fail 20/23 → 23/23; QUALITY
  156), M93-3 (rc-blind counter; G19 killed only by `WEAK:1->WEAK:0`), M93-4 (round-92 report lacked the cross-domain item;
  `grep -c '^- \*\*Cross-domain evidence'` → 0 on round 92, 1 here; QUALITY 157), M93-5 (stale source path sent to a seat;
  QUALITY 158, not mechanical), M93-6 (counter byte subset not the declared one; fixed before the freeze).
- Gate decisions: 1 admit (knowledge entry), 6 reject (draft VT sentence, a `portal-impl.c` row, freezing X19/MB06, the
  20-kill unique set, the fresh-seeded C2 clause, assimilation) — one table in the lesson.
- Assimilation: none — no staged GKeyFile/portal-config entry in `merge/mado/` (R93MConnector §2); collision check committed
  at `.ufo/waves/round-93/assimilation/` (`reg-ids` 449, `staged-ids` 147, `collisions` 94); nothing appended.
- considerthese: `considerthese/2026-11-06.md` proposal 4 (operator-config gap) mined into C1 (entry §7, lesson
  `## Considerthese`); proposal 1 (survivor ledger) closed: the round-87 mako survivors were killed in round 88
  (`.ufo/waves/round-88/receipts/c1-measured-A-r88.txt` 194–201).

## Trend verdicts

- **expansion — improved:** a new edge class of an operator-config surface (the bytes of a hand-edited
  `portals.conf`/`.portal`) moves into core with an admitted entry (index 113 → 114) and four tier-A rows; one capability
  row (selftest-strength gate). The byte subset goes from 32/80 to 80/80 against the installed binary.
- **quality — improved:** C1 366/366 with 75/75 mutants, two fresh legs (the byte leg is the one a label-table forgery fails,
  50/60), a tool pin; C2 23/23 neutralisations, 16/16 weakenings, 6/6 neutral edits, 22/22 gate mutants and four failing
  controls; the round-90 tool's byte divergences (round-91 M91-1, round-92 R92MExecD1) are closed; harm watch green with the
  round-90 C1 counter's declared setup error.
- **discernment — improved:** six reject decisions with evidence; three pre-freeze findings that would have been false
  greens or false misses (rc-blind counter, byte-subset class rule, unpinned tool) became predicate clauses before any
  measurement; the draft's over-strong VT sentence was corrected before landing. Non-author closure spot-check pending.

## Round shape and extras

- Shape: ONE v1 wave `w1` of 13 seats (scout 1, scribe 1, executor 5, connector 1, reviewer 2, critic 1, mutation-tester 2;
  attack 5/13 = 38 %), validated under `ufo-wave-policy.json` and spawned via the inline handoff (`w1.ready`, l1
  `MadoR93`); WAVE-DONE received; no residual call. Round total 13; dead seats 0; `w1-results.json` retains every seat's
  output. Planner seat held by the L1. Routing per the live `task.agentModelOverrides` (no model passed).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `.scratch/` (orchestrator-owned) and
  `trail-ids.txt` (predates this round; not this lane's) — none misrooted by round-93 seats.
- Scratch: `$HYAKU_SCRATCH/mado-r93` removed after landing; every seat reported its own scratch deleted.
- Routed to round 94: QUALITY 158 has no instrument (dispatch URLs unchecked); the selftest-strength gate is wired only for
  `quality/check-seat-reports.py` (other lane gates' selftests unguarded); trailing TAB/FF in a value and VT before a comment
  have no frozen case; the round-90 C1 receipt can no longer be replayed on the current tool (by design).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (pacman paused; nothing needed). L0 questions: none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — registry rows `mado-r93-portal-bytes`, `mado-selftest-strength`, `mado-r93-selftest-strength` added and the `mado-portals` row updated to 28 checks and S511–S514 (`mado-shokunin/SKILL.md`, rows after `mado-xdgmime`); no non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — xdg-desktop-portal's backend choice on 366 byte-level config fixtures and 180 fresh ones, all agreeing with the installed binary (`receipts/c1-measured-r93.txt`, LOG.md round 93); lane-authored.
- [~] Instructions executable by an agent without oral context — registry rows carry argv and verdict maps; the declaration holds the frozen argv both measurements reproduce; outside-lane test not run.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — round-93 refinements (C1 read-only byte rules, C2 scratch-only gate) and the cross-domain item above (GLib, Python runtime, test-mutation method — cited, not absorbed); no outside-lane approval.
