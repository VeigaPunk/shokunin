# mado — round 91 report (hyaku run 15, attempt 1)

L1 `MadoR91`. Lane `mado-shokunin`, branch `master`, base `cc0381db585cc44c3dfc13ced807409c32c45bb0` (round-90 closure
tip), final lane hash **`847f589a1f2b772f5dac7e32a9cbb599a7aa09fc`** (`git ls-remote origin refs/heads/master` prints it).
No earlier attempt of round 91 (`.ufo/watchdog.log` has no `lane-dead-no-report mado round=91`); nothing inherited.

## Work performed

Declared claims (`mado-shokunin/.ufo/waves/round-91/claims-declaration-r91.md`, frozen at `fa71279f`):
**C1 — coverage (capability acquisition):** which `.desktop` application GLib 2.90.1 opens a MIME type or URI scheme with
(default, registered and recommended lists, as `gio mime TYPE` prints them) — a new desktop plane (considerthese
2026-11-06 proposal 4). **C2 — operability:** a runnable seat-report retention gate over the lane's wave dispatches
(round-90 lesson M90-4 / spot-check routed defect 2). Sourced claim: C1 (S504–S507 opened this round, S502 reused).

- Protocol load and inputs: round-90 non-author spot-check (three routed defects), `considerthese/2026-11-06.md`, the
  round-90 lesson; GLib 2.90.1 sources fetched and read by the L1 (`receipts/sources-open-r91.txt`, 20 commands, rc 0).
- Candidate and instruments written before the wave: resolver draft `build/mado-mime.c1.py`, gate draft
  `build/check-seat-reports.c2.py`, gio oracle `controls/mime-oracle-r91.py` (read form `gio mime TYPE` only, `env -i`,
  fixture XDG roots), L1 case generator, both counters, L1 mutants.
- Wave w1 (14 seats) attacked and extended them; the w1 findings changed the candidate (ported `g_shell_parse_argv` and
  `g_find_program_for_path`, GKeyFile byte rules, xdgmime's own `getenv` dirs, libc `qsort`/`bsearch` replay for repeated
  aliases, readdir order for colliding ids), the counters (fresh legs in both predicates, narrowed sandbox, opaque tool
  paths, selftest compared per mutant, generator-truth C2 fixtures) and the sets — all before the freeze; the list is in
  `corpus/lessons/round-91.md` "Wave findings routed".
- Pre-freeze controls executed and committed in the freeze (`receipts/c1-controls-prefreeze-r91.txt`,
  `receipts/c2-controls-prefreeze-r91.txt`): label-table forgery 265/268 frozen but fresh 19/120 (MISSED); gio shell-out /
  ctypes-libgio forgery 63/268 = do-nothing (sandbox hides the oracle); C2 always-OK 5/59, always-MISSING 0/59.
- Freeze `fa71279fc927f86df2d14a62f1f60230a7cf4ada`: declaration with verbatim predicates, pins and argv; 268 cases, 65
  mutants, 59-expectation set, 55 mutants; counters; all w1 evidence.
- C1 `54a0683ce5c1c746fa02fa9f36b530c44772bfa2`: `tools/mado-mime.py` (= frozen candidate, sha256 `2532ccb5…`), knowledge entry
  `corpus/knowledge/mime-default-resolution-r91.md`, S504–S507, PROVINCE round-91 refinement, SKILL registry rows, ledger
  and index rows, host replay `receipts/host-run-r91.txt` (1211 types, 1211 agree with gio).
- C2 `0e09349e2c735c9fe1d4ba8d5c4ef79506f2d0bc`: `quality/check-seat-reports.py` (= frozen candidate, sha256 `13c4b0a7…`)
  and its rows.
- D1 `cbbeb862455d9bc65f6b837083618bd6d69e475a` (routed defect 1): `quality/check-receipt-presence.py --selftest` (87 added
  lines, 0 removed; three mutants each make it exit 1, `receipts/d1-selftest-r91.txt`).
- Residual r1 (2 seats) on the measured bytes: both claims re-measured identically; C1 no defect (18 new fixtures agree);
  C2 six gate defects outside the frozen set routed to round 92.
- Records `847f589a1f2b772f5dac7e32a9cbb599a7aa09fc`: lesson `corpus/lessons/round-91.md` (M91-1…M91-4, Gate, D3 note),
  QUALITY 152, SCORECARD round 91 + capability row + errata, LOG entry, S-row used-by updates, measurement/harm/census
  receipts; gated by `check-receipt-presence.py --worktree` (`receipts/records-gate-r91.txt`, OK 25/25) and the new
  gate on round 91 itself (`receipts/c2-gate-round91-r91.txt`, 16/16 present).

(Receipt paths are under `mado-shokunin/.ufo/waves/round-91/`.)

## Landed changes

| Commit | What | LOG.md |
|---|---|---|
| `fa71279fc927f86df2d14a62f1f60230a7cf4ada` | freeze: declaration, frozen controls, counters, pre-freeze receipts, w1 evidence | LOG round 91 "Landed" |
| `54a0683ce5c1c746fa02fa9f36b530c44772bfa2` | C1 tool, knowledge entry, S504–S507, PROVINCE/SKILL/ledger/index rows, host replay | LOG round 91 "Landed" |
| `0e09349e2c735c9fe1d4ba8d5c4ef79506f2d0bc` | C2 gate and its PROVINCE/SKILL/ledger rows | LOG round 91 "Landed" |
| `cbbeb862455d9bc65f6b837083618bd6d69e475a` | D1 receipt-presence selftest + registry row | LOG round 91 "Landed" |
| `847f589a1f2b772f5dac7e32a9cbb599a7aa09fc` | records (lesson, QUALITY 152, SCORECARD, LOG, used-by, receipts, r1 evidence) | LOG round 91 entry itself |

## Before → after measurements

- **C1 (coverage, capability)** — `python3 -I quality/counters/c1-r91-mime-resolution.py --repo . --rev
  54a0683ce5c1c746fa02fa9f36b530c44772bfa2 --base-rev cc0381db585cc44c3dfc13ced807409c32c45bb0 --cases
  .ufo/waves/round-91/controls/mime-cases-r91.json --mutants .ufo/waves/round-91/controls/mime-mutants-r91.json --oracle
  .ufo/waves/round-91/controls/mime-oracle-r91.py --expect-cases-sha256 15e4b3fc… --expect-mutants-sha256 ed771654…
  --expect-oracle-sha256 c3a13e26… --expect-gio-sha256 d2164260… --expect-libgio-sha256 b38001cc… --fuzz-gen
  .ufo/waves/round-91/controls/fuzz-gen-r91.py --expect-fuzz-sha256 0d147b83… --fresh 120 --scratch-root DIR` (full digests
  in the declaration and SCORECARD). Measured at `54a0683c`: MIME types a lane tool resolves 0 → every type (tool absent at
  base); `TARGET_MET cases=268 correct=268 fresh=120/120 mutants=65 killed=65 crashed_not_killed=0 oracle_agree=268/268`,
  controls do-nothing 63, naive 62, cache-only 102, base 0 — `receipts/c1-measured-r91.txt`, rc 0. Separability: C1 at the
  C2 revision `TARGET_MET` (`receipts/c1-at-c2-r91.txt`).
- **C2 (operability)** — `python3 -I quality/counters/c2-r91-seat-reports.py --repo . --rev
  0e09349e2c735c9fe1d4ba8d5c4ef79506f2d0bc --base-rev cc0381db585cc44c3dfc13ced807409c32c45bb0 --set
  .ufo/waves/round-91/controls/seat-reports-set-r91.json --mutants .ufo/waves/round-91/controls/seat-reports-mutants-r91.json
  --expect-set-sha256 9a05fa8a… --expect-mutants-sha256 7cf06df7… --fresh 60 --scratch-root DIR`. Measured at `0e09349e`:
  lane checks that detect a missing seat report for a dispatched seat 0 → 1; `TARGET_MET expectations=59 met=59
  fresh=60/60 selftest checks=16 failed=0 mutants=55 killed=55`, controls base 0, always-OK 5, always-MISSING 0,
  receipt-presence 11 — `receipts/c2-measured-r91.txt`, rc 0. Separability: C2 counter at `54a0683c` `SETUP_ERROR … absent`
  rc 2 (`receipts/c2-at-c1-r91.txt`).
- Harm watch at `cbbeb862` (`receipts/harm-final-r91.txt`): gate selftest 460/460, `--no-live` CLEAN 29, index 112/112,
  ledger 173/173, mako 62/62, portals 22/22, mime 17/17, seat-reports 16/16, receipt-presence 6/6, round-90 C2 83/83 28/28 on
  the D1-changed check, round-90 C1 229/229 60/60 — all rc 0. No axis harmed.

## Sources & frontier

- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`:
  start `mado ok` rc 0 (`receipts/census-start-r91.txt`); end `mado ok` rc 0, 55 W04 as at start
  (`receipts/census-end-r91.txt`; re-run at `847f589a`: `mado ok`, rc 0). Rows by `grep -cE '^ {0,3}\| S[0-9]{3,} '
  corpus/SOURCES.md`: 438 → 442.
- Rows added by tier: A 4 — S504 GLib 2.90.1 `gdesktopappinfo.c` + `gio-tool-mime.c`, S505 the xdgmime set +
  `gcontenttype-fdo.c`, S506 `gshell.c` + `gutils.c`, S507 freedesktop mime-apps spec 1.0.1; each opened by the L1 this
  round with sha256 and a ≤25-word located quote in the lesson `## Gate`; R91MScoutSources independently fetched the same
  ten files twice and reproduced every sha256.
- Rows touched old→new: S502 used-by `…r90.md,…round-90.md` → `+corpus/knowledge/mime-default-resolution-r91.md` (C1) →
  `+corpus/lessons/round-91.md` (records); S504–S507 used-by knowledge → knowledge + lesson. Logged in the lesson.
- Frontier: the default-application plane moves from absent to core (`corpus/README.md` Frontier round-91 line; index
  111 → 112); launch (does the application start, does OpenURI answer) stays frontier.
- Mistakes mined: M91-1 (reused GKeyFile model; fix shown able to fail — restoring mutants X24/X36/M28/M29 killed;
  QUALITY 152), M91-2 (belief-as-assertion selftest), M91-3 (fixture id vs bytes, second occurrence), M91-4 (C2 premise
  overstatement; erratum).
- Gate decisions: 1 admit (knowledge entry), 4 reject (spec's "default must be associated", shlex as `Exec` parser,
  assimilation, R91MResidC1's NoDisplay erratum — refuted with gio, `receipts/nodisplay-check-r91.txt`).
- Assimilation: none — R91MConnector found no staged MIME/default-application/desktop-entry entry in `merge/mado/`;
  collision check `mado-shokunin/.ufo/waves/round-91/assimilation/` (`reg-ids` 438, `staged-ids` 147, `collisions` 94, plus
  53 staged ids below the registry tip); nothing appended.
- considerthese: `considerthese/2026-11-06.md` proposal 4 mined into C1 (lesson `## Considerthese`).

## Trend verdicts

- **expansion — improved:** a new desktop plane (default applications) with an admitted entry on ground the coverage map
  did not hold (index 111 → 112), four tier-A rows, one capability row; the host's 1211 named types resolve.
- **quality — improved:** C1 268/268 against the installed gio with 65/65 mutants, a fresh leg a stored-label forgery
  fails (19/120) and a sandbox the oracle shell-out cannot cross; C2 59/59 + fresh 60/60 + 55/55; QUALITY 152 with a shown
  failure; D1 selftest with mutant proof; harm watch green. Six C2 gate defects outside the frozen set are open (routed).
- **discernment — improved:** four reject decisions with evidence (two of them refuting a seat's or the specification's
  claim with gio runs), a premise overstatement caught and corrected by erratum rather than rewrite, and the lane's own
  gate now shows every round-91 seat retained its report (16/16). Non-author closure spot-check pending.

## Round shape and extras

- Shape: ONE v1 wave `w1` of 14 seats (scout 2, scribe 1, executor 5, connector 1, reviewer 2, critic 1, mutation-tester 2;
  attack 5/14 = 36 %), validated under `ufo-wave-policy.json` and spawned via the inline handoff (`w1.ready`, l1
  `MadoR91`); residual call `r1` of 2 attack seats (reviewer 1, critic 1) on the measured bytes, rendered in the v1 shape
  (the validator refuses < 8 lanes: `r1-run.err`). Round total 16; dead seats 0; WAVE-DONE received for both waves;
  `w1-results.json` and `r1-results.json` retain every seat's output. Planner seat held by the L1. Routing per the live
  `task.agentModelOverrides` (no model passed).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `.scratch/` (orchestrator-owned) and
  `trail-ids.txt` (created 20:36, before this round started; not this lane's) — none misrooted by round-91 seats.
- Scratch: `$HYAKU_SCRATCH/mado-r91` removed after landing.
- Routed to round 92: C2 gate defects F1–F6 (R91MResidC2 §5); `tools/mado-portals.py` GKeyFile divergences (M91-1).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none. L0 questions: none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — registry extended with `mado-r91-mime-resolution`, `mado-mime`, `mado-r91-seat-reports`, `mado-seat-reports` and the D1 selftest (`mado-shokunin/SKILL.md`, rows after `mado-receipt-presence`); no non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the host's default applications resolved end to end, 1211/1211 against gio (`receipts/host-run-r91.txt`, LOG.md round 91); lane-authored.
- [~] Instructions executable by an agent without oral context — registry rows carry full argv and verdict maps; the r1 seats re-ran both measurements from the declaration's argv alone and reproduced them; outside-lane test not run.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the default-application plane added as a read-only PROVINCE refinement (round 91); no outside-lane approval.
