# mado — round 90 report (hyaku run 15, attempt 2)

L1 `MadoR90a2` (attempt 2; attempt 1 `MadoR90` ran the wave and wrote the declaration, then ended before any commit —
`.ufo/watchdog.log` `lane-dead-no-report mado round=90` 20:22:51). Lane `mado-shokunin`, branch `master`, base
`5041acf99e27263872bf0441ad5f9d4316152605`, final lane hash **`1f07e84133921a8be0a2de074dc8f04e7e015cdf`** (`git ls-remote
origin refs/heads/master` prints it).

## Work performed

Declared claims (`.ufo/waves/round-90/claims-declaration-r90.md`, frozen at `1d9bc404`):
**C1 — coverage (capability acquisition):** xdg-desktop-portal backend routing resolved the way the installed 1.22.1
resolves it, for all 21 impl interfaces. **C2 — operability:** a runnable receipt-presence gate over the lane's records
changes (routed by the round-89 spot-check D1). Sourced claim: C1 (S501–S503).

- Inherited state re-verified: every sha256 pin in the declaration (candidates, cases, mutants, set, oracle, fuzz
  generator, both counters, oracle binary) recomputed equal; both draft controls re-run on the frozen bytes (attempt 1's
  C1 receipt held only its argv) — `mado-shokunin/.ufo/waves/round-90/receipts/c1-controls-prefreeze-r90.txt`,
  `c2-controls-prefreeze-r90.txt` (both `DRAFT_TARGET_MET`). Nothing inherited was discarded. Attempt-2 note added to the
  declaration before the freeze (`claims-declaration-r90.md:8-16`).
- Freeze `1d9bc40414a5d6bddd449cc633a12f2e7e338652`: declaration, counters, frozen controls, pre-freeze receipts, all w1 evidence.
- C1: `tools/mado-portals.py` landed from the frozen candidate bytes (sha256 `d1bd9b9a…`) at
  `7bec239929cdd1d7c796a89ddccefe47d802673a`; measured `TARGET_MET` 229/229 (`receipts/c1-measured-r90.txt`); host run
  `receipts/host-run-r90.txt` (gtk 11, hyprland 4, no backend 6: Background, Wallpaper, Secret, RemoteDesktop, Clipboard, Usb).
- C2: `quality/check-receipt-presence.py` landed from the frozen candidate bytes (sha256 `04b8be60…`) at
  `c09d3465299c53a8158a96b2214c2bcda44bcb41`; measured `TARGET_MET` 83/83 (`receipts/c2-measured-r90.txt`); used this round to
  gate both records commits (`receipts/c2-gate-records-r90.txt`, `receipts/c2-gate-final-r90.txt`, verdict OK).
- Routed D3 (round-89 spot-check): `tools/mado-mako.py` selftest 59 → 62 at `7c28090e99ca99b799e16a92797bf33f63aca372`;
  RS01/RS05/RS12 reconstructed mutants pass the base selftest and fail the new one (`receipts/d3-mako-survivors-r90.txt`).
- Routed D2: ten `SKILL.md` gate-registry rows `mado-r87-*` … `mado-receipt-presence` (records commit `6156d399`).
- Knowledge entry `corpus/knowledge/xdg-portal-routing-resolver-r90.md` (from w1 scribe draft, made final against measured
  receipts), SOURCES S501–S503, README coverage + frontier rows, QUALITY 150–151, tool-ledger rows (4), lesson
  `corpus/lessons/round-90.md` (M90-1…M90-4), SCORECARD round-90 section + capability row, LOG entry — records commit
  `6156d399895ed74faa431ebc688d55d3b47efaa0`.
- Harm watch at `6156d399` (`receipts/harm-final-r90.txt`): gate selftest 460/460, `--no-live` CLEAN 29, index 111/111, ledger
  169/169, mako selftest 62/62, portals selftest 22/22, receipt presence OK, round-89 C1 141/141 37/37 and C2 7/7 TARGET_MET.

(Receipt paths above are under `mado-shokunin/.ufo/waves/round-90/`.)

## Landed changes

| Commit | Content | LOG.md entry |
|---|---|---|
| `1d9bc40414a5d6bddd449cc633a12f2e7e338652` | freeze: declaration, counters, controls, pre-freeze receipts, w1 evidence | LOG.md "Round 90" bullet "Landed" |
| `7bec239929cdd1d7c796a89ddccefe47d802673a` | C1 `tools/mado-portals.py` | same |
| `c09d3465299c53a8158a96b2214c2bcda44bcb41` | C2 `quality/check-receipt-presence.py` | same |
| `7c28090e99ca99b799e16a92797bf33f63aca372` | D3 mako selftest kills + receipt | same |
| `6156d399895ed74faa431ebc688d55d3b47efaa0` | records (entry, S501–S503, README, QUALITY 150–151, ledger, SKILL rows, lesson, SCORECARD, LOG, receipts), gated | same |
| `1f07e84133921a8be0a2de074dc8f04e7e015cdf` | harm-watch receipt + final records line, gated | LOG.md "Harm watch at the records commit" |

The first push of `1f07e841` got `remote: Internal Server Error`; a helper `push` 45 s later printed `landed 1f07e841…`.

## Before → after measurements

- **C1** at `7bec239929cdd1d7c796a89ddccefe47d802673a`: `python3 -I quality/counters/c1-r90-portal-routing.py --repo . --rev
  7bec239929cdd1d7c796a89ddccefe47d802673a --base-rev 5041acf99e27263872bf0441ad5f9d4316152605 --cases
  .ufo/waves/round-90/controls/portal-cases-r90.json --mutants .ufo/waves/round-90/controls/portal-mutants-r90.json
  --expect-cases-sha256 66d4ffff70bd092bd2c900658b3b9a7566f8dedc2aacd4b334102acebc192da2 --expect-mutants-sha256
  e761a4e44ec6d8a692d8ac9b2feec7ef8609b4d30f5ed40c11f7c332129c2451 --expect-oracle-binary-sha256
  e1429fbe1bf6c2203ba07f478b9e92e9221437b13a92eebafb0982748583a4f8 --scratch-root DIR` →
  before: tool absent, `base_correct=0`, interfaces resolvable by a lane tool 0; after: `TARGET_MET cases=229 correct=229
  blind=66/66 fresh=120/120 mutants=60 killed=60 r12_rule_correct=70 host_table_correct=10 do_nothing_correct=35
  base_correct=0`, interfaces 21. Separability: also TARGET_MET at the C2 revision (`receipts/c1-harm-at-c2-r90.txt`).
- **C2** at `c09d3465299c53a8158a96b2214c2bcda44bcb41`: `python3 -I quality/counters/c2-r90-receipt-presence.py --repo . --rev
  c09d3465299c53a8158a96b2214c2bcda44bcb41 --base-rev 5041acf99e27263872bf0441ad5f9d4316152605 --set
  .ufo/waves/round-90/controls/receipt-presence-set-r90.json --mutants .ufo/waves/round-90/controls/receipt-mutants-r90.json
  --expect-set-sha256 f7ab86c25edbb806a9f947af09fab5cf971a42602c252966c0075b9aeefa7939 --expect-mutants-sha256
  68b39a805755f7685c00c847a48b0f8f679fdca2710773efb5f4469b7bebe82d --scratch-root DIR` → before: check absent, `base_met=0`,
  existing checks silent on `498855cb`/`51bf076f`; after: `TARGET_MET expectations=83 met=83 defects_detected=4/4
  population=38 mutants=28 killed=28 do_nothing_met=44 smart_always_ok_met=46 always_missing_met=0`. At the C1 revision the
  counter prints `SETUP_ERROR … absent` (`receipts/c2-at-c1-r90.txt`): the claims are separable.

## Sources & frontier

- Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado` —
  start `mado ok`, rc 0 (`receipts/census-start-r90.txt`); end `mado ok`, rc 0, 55 W04 warnings as at start
  (`receipts/census-end-r90.txt`). Rows by `grep -cE '^ {0,3}\| S[0-9]{3,} ' corpus/SOURCES.md`: 435 → 438.
- Rows added by tier: A 3 (S501 xdg-desktop-portal 1.22.1 tag tarball, S502 GLib 2.90.1 `gkeyfile.c`, S503 host
  `portals.conf(5)`), each re-opened by the L1 this round with sha256 re-derived and a located quote in the lesson's
  `## Gate`. Rows touched old→new: none.
- Frontier: portal backend routing moves from a hand-derived table (round 12) to a runnable resolver; runtime (a backend
  answering a call, ScreenCast sessions) stays frontier (`corpus/README.md` Frontier, round-90 line).
- Mistake mined: M90-1 (fixture concatenation merged lines; check shown able to fail, `receipts/m90-1-fixture-lines-r90.txt`,
  QUALITY 150); M90-2 (records-before-receipts, QUALITY 151); M90-3 and M90-4 routed.
- Assimilation: none — R90MConnector found no portal/GKeyFile/receipt theme in `merge/mado/` (its one portal-adjacent row is
  an unpinned master URL already held tag-pinned); collision check `mado-shokunin/.ufo/waves/round-90/assimilation/`
  (`reg-ids` 435, `staged-ids` 147, `collisions` 94) — nothing appended.
- considerthese: `considerthese/2026-11-06.md` proposal 4 (widen past bar + mako: xdg-desktop-portal) mined into C1; lesson
  `## Considerthese`.

## Trend verdicts

- **expansion — improved:** one admitted entry on ground the coverage map did not hold (index 110 → 111), three tier-A rows,
  one capability row (portal routing, 0 → 21 interfaces); five interfaces the round-12 table never listed now resolved.
- **quality — improved:** C1 229/229 against the installed binary's own decision lines with 60/60 mutants and a fresh leg
  a stored-label forgery cannot pass; C2 gate 83/83 with 28/28 mutants; three routed mako survivors killed; QUALITY 150–151
  each with a shown failure; harm watch green.
- **discernment — improved:** the lane now refuses its own records commit when it cites a receipt it does not carry — the
  gate flags the round-88 and round-89 records commits `MISSING` that two earlier closures had to catch by hand
  (`receipts/c2-measured-r90.txt`); the non-author closure spot-check is still pending.

## Round shape and extras

- Shape: ONE v1 wave w1 of 13 seats (scout 2, scribe 1, executor 4, connector 1, reviewer 2, critic 1, mutation-tester 2;
  attack 5/13 = 38 %), spawned via the inline handoff in attempt 1 (`w1.ready`, l1 `MadoR90`); WAVE-DONE received by attempt 2.
  No residual call (the declaration's optional `r1` was not dispatched). Round total 13; dead seats 0. Planner seat held by
  the L1. `w1-results.json` holds no seat outputs (orchestrator kernel restart); 11 seats left report files, the two scouts
  did not (M90-4).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/` (orchestrator-owned);
  none misrooted.
- Scratch: `$HYAKU_SCRATCH/mado-r90` removed after landing.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none. L0 questions: none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — gate registry extended through r90 (`mado-shokunin/SKILL.md`, rows after `mado-r86-clause-observations`); no non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — host portal routing resolved end to end (`receipts/host-run-r90.txt`, LOG.md round 90); lane-authored.
- [~] Instructions executable by an agent without oral context — registry rows carry full argv and verdict maps; outside-lane test not run.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — portal routing is a desktop-plane surface inside PROVINCE; no outside-lane approval.
