# mado — round 92 report (hyaku run 15, attempt 1)

L1 `MadoR92`. Lane `mado-shokunin`, branch `master`, base `d992ef7494b054591ee9104df1da49264678df5d` (round-91 closure
tip), final lane hash **`fbcc2672b7068b3f536a849b0ec5b72da56bf7fd`** (`git ls-remote origin refs/heads/master` prints it).
No earlier attempt of round 92 (`.ufo/watchdog.log` has no `lane-dead-no-report mado round=92`); nothing inherited.

## Work performed

Declared claims (`mado-shokunin/.ufo/waves/round-92/claims-declaration-r92.md`, frozen at `6a0134ac`):
**C1 — coverage (capability acquisition):** what `xdg-open` launches on Hyprland — a read-only replay of xdg-utils 1.2.1
`xdg-mime query default TYPE` (the resolver `xdg-open` uses on a desktop xdg-utils does not recognise), a new caller
plane (considerthese 2026-11-06 proposal 4). **C2 — operability:** `quality/check-seat-reports.py` closes the round-91
residual defects F1–F5 (round-91 spot-check routed defect 2). Sourced claim: C1 (S508–S510 opened this round).

- Protocol load and inputs: round-91 non-author spot-check (three routed defects), `considerthese/2026-11-06.md`, the
  round-91 lesson and R91MResidC2; xdg-utils v1.2.1 sources fetched and diffed against the installed script by the L1
  (`receipts/sources-open-r92.txt`: three raw files + tag archive, eight modelled functions byte-identical); gnu.org
  unreachable (curl rc 28 twice), so the installed bash(1)/grep(1) manuals of the same releases were opened instead.
- Candidates and instruments drafted before the wave: `build/mado-xdgmime.c1.py`, `build/check-seat-reports.c2.py`,
  xdg-mime oracle (`controls/xdgmime-oracle-r92.py`, `env -i`, `query default` only), L1 case generator (124 cases), fuzz
  generator, both counters, L1 mutants, C2 battery.
- Wave w1 (13 seats) attacked and extended them; findings changed the candidate (RFC 6838 type scope, glob escapes and
  reversed ranges, gawk escapes, `--selftest`, directory/gitlink dispatches refused), the counters (C1 bytes clause
  against a shipped interpreter, C2 sandbox and fresh leg, round-91 leg read from `<rev>` and pinned) and the sets — all
  before the freeze (`corpus/lessons/round-92.md` "Wave findings routed").
- Pre-freeze controls executed and committed in the freeze (`receipts/c1-controls-prefreeze-r92.txt`,
  `receipts/c2-controls-prefreeze-r92.txt`): label-table forgery 268/270 frozen but fresh 58/120 (MISSED); shell-out
  forgery 101/270 = do-nothing (sandbox hides xdg-mime and every host shell); bundled-interpreter forgery 270/270 and
  fresh 120/120 but `bytes_clause=FAIL:size_1659133_>_65536` (MISSED); C2 base 19/45, always-OK 7/45, always-refuse 15/45.
- Freeze `6a0134acb08b26b1cd3c6f0a4b8c63495ca89e3e`: declaration with verbatim predicates, pins and argv; 270 cases, 81
  mutants; 45-fixture battery, 37 mutants; counters; all w1 evidence then present.
- C1 `243326cb884b04bf91c36e6c7565b6f079a8fb7f`: `tools/mado-xdgmime.py` (= frozen candidate, sha256 `4e7fff9e…fd88`),
  knowledge entry `corpus/knowledge/xdg-mime-default-resolution-r92.md`, S508–S510, append-only correction §15 of the
  round-91 entry, PROVINCE round-92 refinement, SKILL/ledger/index rows, host replay `receipts/host-run-r92.txt`.
- C2 `297e25153ceb3a4e119eed5b377d7547828d01b6`: `quality/check-seat-reports.py` (= frozen candidate, sha256
  `176fc066…663a`), SKILL/ledger/PROVINCE rows.
- Records `c7627393dc17dc99908c987c74dac18e96a8c8a8` and `fbcc2672b7068b3f536a849b0ec5b72da56bf7fd`: lesson
  `corpus/lessons/round-92.md` (M92-1…M92-5, Gate), QUALITY 153–154, SCORECARD round 92 + capability row, LOG entry,
  round-90 entry correction §12 (routed defect 1), S-row used-by updates, measurement/harm/census receipts, w1 results
  and reports; gated by `check-receipt-presence.py --worktree` (`receipts/records-gate-r92.txt`, OK 19/19) and the new
  gate on round 92 itself (`receipts/c2-gate-round92-r92.txt`, 13/13 present).

(Receipt paths are under `mado-shokunin/.ufo/waves/round-92/`.)

## Landed changes

| Commit | What | LOG.md |
|---|---|---|
| `6a0134acb08b26b1cd3c6f0a4b8c63495ca89e3e` | freeze: declaration, frozen cases/mutants/battery, counters, candidates, pre-freeze controls, w1 evidence | LOG round 92 "Landed" |
| `243326cb884b04bf91c36e6c7565b6f079a8fb7f` | C1 tool, knowledge entry, S508–S510, round-91 entry correction, PROVINCE/SKILL/ledger/index rows, host replay | LOG round 92 "Landed" |
| `297e25153ceb3a4e119eed5b377d7547828d01b6` | C2 gate and its SKILL/ledger/PROVINCE rows | LOG round 92 "Landed" |
| `c7627393dc17dc99908c987c74dac18e96a8c8a8` | records (lesson, QUALITY 153–154, SCORECARD, LOG, round-90 correction, used-by, receipts, w1 results) | LOG round 92 entry itself |
| `fbcc2672b7068b3f536a849b0ec5b72da56bf7fd` | w1 evidence: R92MExecFuzz extended-generator disagreement list (1.3 MB, cited by its report) | LOG round 92 entry (w1 evidence) |

## Before → after measurements

- **C1 (coverage, capability)** — `python3 -I quality/counters/c1-r92-xdgmime-default.py --repo . --rev
  243326cb884b04bf91c36e6c7565b6f079a8fb7f --base-rev d992ef7494b054591ee9104df1da49264678df5d --cases
  .ufo/waves/round-92/controls/xdgmime-cases-r92.json --mutants .ufo/waves/round-92/controls/xdgmime-mutants-r92.json
  --oracle .ufo/waves/round-92/controls/xdgmime-oracle-r92.py --fuzz-gen .ufo/waves/round-92/controls/fuzz-gen-r92.py
  --expect-cases-sha256 3cb0cf45… --expect-mutants-sha256 f0d934f2… --expect-oracle-sha256 e5160399… --expect-fuzz-sha256
  891704bf… --expect-bin-sha256 <xdg-mime,bash,grep,gawk,realpath,basename> --fresh 120 --scratch-root DIR` (full digests in
  the declaration and SCORECARD). Measured at `243326cb`: MIME types a lane tool answers xdg-open's default for 0 → every
  RFC 6838 type (tool absent at base); `TARGET_MET cases=270 correct=270 answered=270/270 fresh=120/120 mutants=81 killed=81
  crashed_not_killed=0 oracle_agree=270/270 bytes_clause=ok`, controls do-nothing 101, naive 78, GLib resolver 139, base 0 —
  `receipts/c1-measured-r92.txt`, rc 0. Separability: C1 at the C2 revision `TARGET_MET` (`receipts/c1-at-c2-r92.txt`).
- **C2 (operability)** — `python3 -I quality/counters/c2-r92-gate-defects.py --repo . --rev
  297e25153ceb3a4e119eed5b377d7547828d01b6 --base-rev d992ef7494b054591ee9104df1da49264678df5d --battery
  .ufo/waves/round-92/controls/gate-defects-battery-r92.json --mutants .ufo/waves/round-92/controls/gate-defects-mutants-r92.json
  --expect-battery-sha256 a0cfaeb3… --expect-mutants-sha256 fe931e76… --r91-argv .ufo/waves/round-92/controls/r91-c2-argv-r92.json
  --expect-r91-argv-sha256 d21b1979… --expect-r91-counter-sha256 c74f5baa… --fresh 60 --scratch-root DIR`. Measured at
  `297e2515`: battery fixtures met 19/45 (base) → **45/45** (F1 9/9, F2 5/5, F3 3/3, F4 3/3, F5 4/4, MC 13/13, P 8/8);
  `TARGET_MET fresh=60/60 selftest checks=23 failed=0 mutants=37 killed=37 base_met=19 always_ok_met=7 always_refuse_met=15
  r91_counter=TARGET_MET` (round-91 leg 59/59, fresh 60/60, 55/55) — `receipts/c2-measured-r92.txt`, rc 0. Separability: C2
  counter at `243326cb` `SETUP_ERROR mutant N01: find occurs 0 times`, rc 2 — the check there has none of the fixes
  (`receipts/c2-at-c1-r92.txt`).
- Harm watch at `297e2515` (`receipts/harm-final-r92.txt`): gate selftest 460/460, `--no-live` CLEAN 29, index 113/113,
  ledger 176/176, mako 62/62, portals 22/22, mime 17/17, xdgmime 12/12, seat-reports 23/23, receipt-presence 6/6,
  round-90 C2 83/83 28/28, round-90 C1 229/229 60/60 — all rc 0; round-91 C2 TARGET_MET inside the C2 measurement;
  `tools/mado-mime.py` and `tools/mado-portals.py` unchanged since the base. No axis harmed.

## Sources & frontier

- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`:
  start `mado ok` rc 0 (`receipts/census-start-r92.txt`); end `mado ok` rc 0, 55 W04 as at start
  (`receipts/census-end-r92.txt`; re-run at `fbcc2672`: `mado ok`, rc 0). Rows by `grep -cE '^ {0,3}\| S[0-9]{3,} '
  corpus/SOURCES.md`: 442 → 445.
- Rows added by tier: A 3 — S508 xdg-utils v1.2.1 (`xdg-mime.in`, `xdg-utils-common.in`, `xdg-open.in`, tag archive;
  installed script functions byte-identical), S509 bash(1) 5.3.20 installed manual, S510 grep(1) 3.12 installed manual;
  each opened by the L1 this round with sha256 and a ≤25-word located quote in the lesson `## Gate`; R92MScoutSources
  independently fetched the xdg-utils files twice and reproduced every digest.
- Rows touched old→new: S508–S510 used-by `corpus/knowledge/xdg-mime-default-resolution-r92.md` (C1) →
  `+corpus/lessons/round-92.md` (records). Logged in the lesson.
- Frontier: the default-application plane splits by caller — `xdg-open`'s resolver moves from absent to core
  (`corpus/README.md` round-92 frontier line; index 112 → 113); MIME sniffing (`query filetype`) and launch stay frontier.
- Mistakes mined: M92-1 (frozen-instrument coupling; fix shown able to fail — transcripts D-a/D-b; QUALITY 153), M92-2
  (round 91's "xdg-open reduces to GLib"; QUALITY 154; host 378/1133), M92-3 (a crashing forgery read as defeated; fix
  shown able to fail — `receipts/m92-3-answered-r92.txt`, `answered=0/270`), M92-4 (belief-as-assertion selftest, second
  occurrence of M91-2), M92-5 (over-broad regex claim, scoped before the freeze).
- Gate decisions: 1 admit (knowledge entry), 6 reject (round-91 xdg-open sentence, round-90 UTF-8 sentence, landing the
  portals port this round, non-RFC-6838 regex modelling, assimilation, F6) — all in one table (routed defect 3).
- Assimilation: none — R92MConnector found no staged xdg-utils/xdg-open/mimeapps entry in `merge/mado/`; collision check
  (`reg-ids` 442, `staged-ids` 147, `collisions` 94, 53 staged ids below the registry tip); nothing appended.
- considerthese: `considerthese/2026-11-06.md` proposal 4 mined into C1 (lesson `## Considerthese`).

## Trend verdicts

- **expansion — improved:** a new caller plane (what `xdg-open` launches) with an admitted entry on ground the coverage map
  did not hold (index 112 → 113), three tier-A rows, one capability row; the host's 1133 types resolve, and 378 of them are
  shown to open differently (375 not at all) under `xdg-open` than under gio.
- **quality — improved:** C1 270/270 against the installed xdg-mime with 81/81 mutants, a fresh leg a label table fails
  (58/120), a sandbox the shell-out forgery cannot cross and a bytes clause the bundled-interpreter forgery fails; C2 45/45 +
  fresh 60/60 + 37/37 with the round-91 frozen leg intact; two knowledge errors corrected append-only (round-91 xdg-open
  sentence, round-90 GKeyFile sentence); QUALITY 153 with a shown failure; harm watch green. Open: the portals port (routed).
- **discernment — improved:** six reject decisions with evidence, a scope narrowed before the freeze by a declared rule
  applied to case bytes (not by running the tool), two seat findings that would have been false greens (bundled
  interpreter; quotable battery) turned into predicate clauses, and the lane's gate shows every round-92 seat retained its
  report (13/13). Non-author closure spot-check pending.

## Round shape and extras

- Shape: ONE v1 wave `w1` of 13 seats (scout 1, scribe 1, executor 5, connector 1, reviewer 2, critic 1, mutation-tester 2;
  attack 5/13 = 38 %), validated under `ufo-wave-policy.json` and spawned via the inline handoff (`w1.ready`, l1
  `MadoR92`); no residual call. Round total 13; dead seats 0; WAVE-DONE received; `w1-results.json` retains every seat's
  output. Planner seat held by the L1. Routing per the live `task.agentModelOverrides` (no model passed).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `.scratch/` (orchestrator-owned) and
  `trail-ids.txt` (predates round 91; not this lane's) — none misrooted by round-92 seats.
- Scratch: `$HYAKU_SCRATCH/mado-r92` removed after landing.
- Routed to round 93: the `tools/mado-portals.py` GKeyFile port (`build/mado-portals.d1.py`, 16/16 + 229/229) with its own
  frozen counter and regenerated round-90 mutants; a selftest-label instrument (M92-4); the C2 selftest-coverage limit
  (R92MMutC2 §4).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none. L0 questions: none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — registry extended with `mado-r92-xdgmime-default`, `mado-xdgmime`, `mado-r92-gate-defects` and the updated `mado-seat-reports` row (`mado-shokunin/SKILL.md`, rows after `mado-seat-reports`); no non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `xdg-open`'s default resolved end to end for the host's 1133 types, all agreeing with xdg-mime (`receipts/host-run-r92.txt`, LOG.md round 92); lane-authored.
- [~] Instructions executable by an agent without oral context — registry rows carry full argv and verdict maps; the declaration holds the frozen argv the measurements reproduce; outside-lane test not run.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round-92 refinements correct the round-91 xdg-open sentence and add the read-only xdg-mime replay; no outside-lane approval.
