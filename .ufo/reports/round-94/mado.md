# mado — round 94 report (hyaku run 15, attempt 1)

L1 `MadoR94`. Lane `mado-shokunin`, branch `master`, base `a3de997289014e7dbf1d73ae206be1d6f8cdadd0` (round-93 closure
tip), final lane hash **`bcc21fcffafd9d8c7c06b849c41e8bea030b2a1f`** (`git ls-remote origin refs/heads/master` prints it).
No earlier attempt of round 94 (`.ufo/watchdog.log` has only `launch mado round=94 … attempt=1`); nothing inherited; the
lane tree was clean at start.

## Work performed

Declared claims (`mado-shokunin/.ufo/waves/round-94/claims-declaration-r94.md`, frozen at `bcc5429b`):
**C1 — coverage (new surface, capability):** `tools/mado-mimeglob.py` answers, read-only, which MIME type GLib 2.90.1
`g_content_type_guess (name, NULL, 0)` gives a file name and whether it is uncertain, in cache mode (`mime.cache`) and text
mode (`globs2`/`globs`). **C2 — operability:** kill-sets that let the round-93 selftest-strength gate guard
`tools/mado-xdgmime.py` and `tools/mado-mime.py` (round-93 spot-check routed defect 2). Sourced claim: C1 (S515–S518 opened
this round, S505 re-opened).

- Protocol load and inputs: the round-93 non-author spot-check (three routed defects), `considerthese/2026-11-06.md`
  (proposal 4), round-93 lesson/report/SCORECARD. Sources opened by the L1 before dispatch, two fetches each with sha256:
  GLib 2.90.1 `xdgmimeglob.c`, `xdgmimecache.c`, `xdgmime.c`, `xdgmimeint.c`, `gcontenttype-fdo.c`, shared-mime-info spec
  0.21 (`receipts/sources-open-r94.txt`). The L1 wrote the oracle (`controls/mimeglob-oracle-r94.c`, 15 lines against the
  installed glib2) and the first candidate before the wave (host cache mode 5424/5424, text mode 5427/5427 in a DRAFT probe).
- Wave w1 (14 seats) built and attacked: 235 oracle-labelled cases and a fresh generator (R94MExecCasesC1), the C1 counter
  (R94MExecCounterC1), 57 mutants (R94MMutC1), F1–F7 with 51 cases incl. one wrong answer, five refusals and a
  RecursionError (R94MReviewC1), the cache-vs-text hypothesis falsified with nine mechanisms, 117/9521 answers
  (R94MProbeC1), host names 9745/9745 and the harm harness (R94MExecHostC1), two kill-sets (R94MExecKillsC2), the C2
  counter and panel (R94MExecCounterC2), 46 escapes from those kill-sets with verified closing kills (R94MMutC2), a
  one-kill union forgery (R94MReviewC2), nine freeze-ready repairs incl. an oracle-exec wrapper that met every behavioural
  conjunct (R94MCritic), sibling/assimilation/caller sweep (R94MConnector), the entry draft (R94MScribeEntry), source
  re-audit with 15 spec/GLib divergences and update-mime-database 2.5.1 (R94MScoutSources).
- L1 integration before the freeze (lesson "Wave findings routed"): candidate rewritten to `build/mado-mimeglob.c1b.py`
  (sha256 `65f80a6c…2453`: HOME concatenation and `--home-unset`, iterative trie walks, text files parsed only without a
  cache, xdgmimeint.c byte decoding, zero-filled last cache page, bare `*` inert); 370-case frozen set (5 L1 cases for HOME
  unset and undecoded bytes); 60 counted mutants (13 re-anchored, 14 added, 11 excluded with arguments); C1 predicate
  amendments (20 enumerated classes, `static_no_external_resolver`, empty PATH, host DB digests); C2 kill-sets 27 → 46
  kills, panel 12 → 91 hand weakenings, conjunct (vii) first-draft control; the C2 counter's singleton print.
- Pre-freeze controls executed and committed in the freeze: C1 candidate DRAFT_TARGET_MET; wave candidate `c1.py` 355/370
  MISSED; R94MCritic's subprocess wrapper and an L1 ctypes-libgio forgery MISSED only through (vi) and the pin — the ctypes
  one is 370/370, fresh 60/60, host 9745/9745 otherwise (`receipts/c1-controls-prefreeze-r94.txt`); C2 candidates
  DRAFT_TARGET_MET, first-draft kill-sets 45/91 MISSED, empty kill-sets 0/29 MISSED (`receipts/c2-controls-prefreeze-r94.txt`).
- Freeze `bcc5429b68a8b60bc5238fa06f01818686a9d465`; C1 `38f77d89310bf9fc752e54e4e98844a9b6ce88cc`; C2
  `764d083ad83b8de41bb4331a71f9b8ce237997c1`; records `bcc21fcffafd9d8c7c06b849c41e8bea030b2a1f` (gated by
  `quality/check-seat-reports.py --worktree --round 94` → 14/14 present and `check-receipt-presence.py` → 19/19 cited
  receipts present, `receipts/records-gate-r94.txt`).
- Post-freeze attack, disclosed: R94MMutC2 re-ran its 112 weakenings against the frozen kill-sets (0 escapes; 4 check-count
  changers caught as setup errors, `w1/R94MMutC2-escapes-c2b.json`) and mutated the C2 counter: the do-nothing,
  always-WEAK, sha-diff and hand-count conjuncts cannot be broken by any probe (constructed controls) — recorded as a
  limit, not a pass.
- **Cross-domain evidence** encountered: GLib xdgmime/gcontenttype (GNOME/GLib), the shared-mime-info format and
  `update-mime-database` (freedesktop.org; the ALPM hook that runs it is tsukuroi's:
  `tsukuroi-shokunin/corpus/knowledge/pacman-hook-order-r38.md:53,97`), glibc `fnmatch(3)`/`qsort(3)`, binary-format
  parsing (kaidoku/revenger style, method only). R94MConnector §2 swept every sibling `PROVINCE.md` and knowledge tree:
  only mado reads MIME database bytes; no other lane owns the surface.

(Receipt paths are under `mado-shokunin/.ufo/waves/round-94/`.)

## Landed changes

| Commit | What | LOG.md |
|---|---|---|
| `5a164538438c2f101e44a79ad9e05aaf3ca910fb` | w1 dispatch evidence: declaration draft, first candidate, oracle source, sources-open, census start, assimilation check | LOG round 94 "Landed" |
| `bcc5429b68a8b60bc5238fa06f01818686a9d465` | freeze: declaration with w1 amendments, frozen cases/mutants/panel/kill-sets/candidates, both counters, pre-freeze controls, w1 evidence | LOG round 94 "Landed" |
| `38f77d89310bf9fc752e54e4e98844a9b6ce88cc` | C1: `tools/mado-mimeglob.py` (= frozen candidate), `corpus/knowledge/mime-glob-guess-r94.md`, S515–S518, S505 used-by, PROVINCE/SKILL/ledger/index rows | LOG round 94 "Landed" |
| `764d083ad83b8de41bb4331a71f9b8ce237997c1` | C2: `quality/selftest-kills/mado-xdgmime.json` (19 kills), `quality/selftest-kills/mado-mime.json` (27 kills), SKILL/ledger/PROVINCE rows | LOG round 94 "Landed" |
| `bcc21fcffafd9d8c7c06b849c41e8bea030b2a1f` | records: lesson (M94-1…M94-6, Gate), QUALITY 159–162, SCORECARD round 94 + capability row, LOG entry, used-by, measurements, separability, harm watch, census end, records gates, w1 results | LOG round 94 entry itself |

## Before → after measurements

- **C1 (coverage, new surface)** — `python3 -I quality/counters/c1-r94-mimeglob.py --repo . --rev
  38f77d89310bf9fc752e54e4e98844a9b6ce88cc --base-rev a3de997289014e7dbf1d73ae206be1d6f8cdadd0 --cases
  .ufo/waves/round-94/controls/mimeglob-cases-r94-frozen.json --expect-cases-sha256 c7b693d2… --mutants
  .ufo/waves/round-94/controls/mimeglob-mutants-r94-frozen.json --expect-mutants-sha256 0e74c57d… --oracle-src
  .ufo/waves/round-94/controls/mimeglob-oracle-r94.c --expect-oracle-sha256 9c4337b3… --fresh-gen
  .ufo/waves/round-94/controls/mimeglob-fresh-r94.py --expect-fresh-gen-sha256 ab76b97e… --host-names
  .ufo/waves/round-94/controls/mimeglob-host-names-r94.txt --expect-host-names-sha256 4b6d6a6c… --expect-tool-sha256
  65f80a6c… --fresh 120 --workers 24 --scratch-root DIR` (full digests in the declaration and SCORECARD). Measured at
  `38f77d89`: frozen cases answered as the installed GLib does, base **0/370 (no tool) → 370/370**; `TARGET_MET
  tool_pin=ok text=220/220 cache=122/122 mixed=28/28 classes=20/20 static_no_external_resolver=ok fresh=120/120 host=9745/9745
  mutants=60 killed=60 crashed_not_killed=0`, controls do-nothing 43, naive 63 (exact 58), base 0 — `receipts/c1-measured-r94.txt`,
  rc 0. Separability: C1 at the C2 revision `TARGET_MET` (`receipts/c1-at-c2-r94.txt`).
- **C2 (operability)** — `python3 -I quality/counters/c2-r94-selftest-kills.py --repo . --rev
  764d083ad83b8de41bb4331a71f9b8ce237997c1 --panel .ufo/waves/round-94/controls/selftest-panel-r94-frozen.json
  --expect-panel-sha256 2d35e83b… --expect-gate-sha256 2d6f1219… --expect-kills-sha256 d8a450bf…,1a0c4fe8… --control-kills
  .ufo/waves/round-94/build/mado-xdgmime-kills.c2.json,.ufo/waves/round-94/build/mado-mime-kills.c2.json
  --expect-control-kills-sha256 126b508a…,d930689e… --workers 16 --scratch-root DIR`. Measured at `764d083a`: single-check
  neutralisations of the two tools' selftests flagged by a lane instrument **0/29 → 29/29** (before = the do-nothing
  instrument; no kill-set existed); `TARGET_MET positive=OK:0,OK:0 hand_flagged=91/91 neutral_ok=6/6 do_nothing_flagged=0
  always_ok_flagged=0 always_weak_positive=WEAK:1,WEAK:1 shadiff_neutral_ok=0/6 gate_selftest=ok control_hand_flagged=45/91
  singleton_labels=22/29` — `receipts/c2-measured-r94.txt`, rc 0. Separability: C2 counter at `38f77d89` `SETUP_ERROR …
  kill-sets absent`, rc 2 (`receipts/c2-at-c1-r94.txt`).
- Harm watch at `764d083a` (`receipts/harm-final-r94.txt`): gate selftest 460/460, `--no-live` CLEAN 29, index 115/115,
  ledger 182/182, mako 62/62, portals 28/28, mime 17/17, xdgmime 12/12, mimeglob 19/19, seat-reports 23/23,
  receipt-presence 6/6, selftest-strength 11/11 with OK 32/32, 19/19 and 27/27 on the real gate, round-90 C2 83/83 28/28,
  round-92 C2 45/45 with its round-91 leg, round-93 C2 TARGET_MET; the round-90 C1 counter's SETUP_ERROR on the ported portal
  tool as declared in round 93; unchanged-tool diff empty. No axis harmed.

## Sources & frontier

- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`:
  start `mado ok` rc 0 (`receipts/census-start-r94.txt`); end `mado ok` rc 0, W04 56 → 57 (S518 shares S505's URL under a
  different scope) (`receipts/census-end-r94.txt`). Rows by `grep -cE '^ {0,3}\| S[0-9]{3,} ' corpus/SOURCES.md`: 449 → 453.
- Rows added by tier: A 4 — S515 GLib 2.90.1 `xdgmimeglob.c` (text lookup), S516 `xdgmimecache.c` (cache glob lookup),
  S517 shared-mime-info spec 0.21 §2.4/§2.9/§2.12, S518 `gcontenttype-fdo.c` (the guess); each fetched twice by the L1
  (the spec page four times) with sha256 and a ≤25-word located quote in the lesson `## Gate`; four seats reproduced the
  GLib digests independently.
- Rows touched old→new: S505 used-by `…mime-default-resolution-r91.md,corpus/lessons/round-91.md` →
  `+corpus/knowledge/mime-glob-guess-r94.md` (re-opened, same digest); S515–S518 used-by entry → `+corpus/lessons/round-94.md`.
  Logged in the lesson.
- Frontier: the name-to-type step of the default-application plane moves to core (`corpus/README.md` round-94 frontier
  line; index 114 → 115); content sniffing, `xdg-mime query filetype` (`file(1)`) and launch stay frontier.
- Mistakes mined: M94-1 (HOME path-joined instead of concatenated; fix shown able to fail — wave candidate 355/370; QUALITY
  159; the same defect sits in round-91 `tools/mado-mime.py`, routed), M94-2 (class list read from the judged data; QUALITY
  160), M94-3 (label coverage ≠ kill-set strength, 46/112 escapes; shown able to fail — first-draft kill-sets 45/91;
  QUALITY 161), M94-4 (oracle-exec forgery; shown able to fail — two forgeries `static_no_external_resolver=FAIL`; QUALITY
  162), M94-5 (the declaration's "every default-application answer" overstates the callers — recurrence of M92-2; QUALITY
  154 not applied by the L1), M94-6 (`labrat` refused by the wave validator, `receipts/validator-refusal-r94.txt`).
- Gate decisions: 2 admit (knowledge entry, S515–S518), 7 reject (the scribe's digest sentence, the wave candidate, the
  refusal allowance, 8 mutants as counted, a singleton conjunct, guarding the C1 tool in C2, assimilation) — one table in
  the lesson.
- Assimilation: none — no staged MIME-glob entry in `merge/mado/` (R94MConnector §3); collision check committed at
  `.ufo/waves/round-94/assimilation/` (`reg-ids` 449, `staged-ids` 147, `collisions` 94); nothing appended.
- considerthese: `considerthese/2026-11-06.md` proposal 4 mined into C1 (lesson `## Considerthese`: a hand-written package
  without `update-mime-database`, a stale user cache that silences the user's `globs2` — this host has both).

## Trend verdicts

- **expansion — improved:** a new desktop surface (file name → MIME type, both database modes) moves into core with an
  admitted entry (index 114 → 115), four tier-A rows and one capability row; at base no lane tool answered it (0/370 → 370/370).
- **quality — improved:** C1 370/370 with 60/60 mutants, fresh 120/120 and host 9745/9745 against the installed GLib, and a
  structural conjunct that rejects two forgeries the behavioural legs could not; C2 29/29 neutralisations and 91/91 hand
  weakenings where the wave's first kill-sets flagged 45/91; harm watch green.
- **discernment — improved:** the wave's attacks became predicate clauses before any measurement (tautological class
  clause, oracle-exec, label-coverage forgery, HOME/bytes/recursion defects); nine cache/text divergences and the spec
  departures are recorded as GLib's behaviour, not smoothed toward the spec; seven reject decisions with evidence; one
  over-broad declaration sentence (M94-5) is named rather than rewritten. Non-author closure spot-check pending.

## Round shape and extras

- Shape: ONE v1 wave `w1` of 14 seats (scout 1, scribe 1, executor 5, connector 1, reviewer 3, critic 1, mutation-tester 2;
  attack 6/14 = 43 %), validated under `ufo-wave-policy.json` (first validation refused `labrat`, fixed before dispatch) and
  spawned via the inline handoff (`w1.ready`, l1 `MadoR94`); WAVE-DONE received; no residual call. Round total 14; dead
  seats 0; `w1-results.json` retains every seat's output. Planner seat held by the L1. Routing per the live
  `task.agentModelOverrides` (no model passed).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `.scratch/` (orchestrator-owned),
  `trail-ids.txt` (2026-11-06 20:36, predates this round) and `f.txt` (`x`, 2 bytes, 04:40, names no lane or round — not
  attributable to a round-94 seat, left untouched) — none moved.
- Scratch: `$HYAKU_SCRATCH/mado-r94` removed after landing; every seat reported its own scratch deleted.
- Routed to round 95: `tools/mado-mime.py` HOME edges (M94-1); the C1 tool docstring's cache-validity citation
  (xdgmimecache.c:126-139, R94MScoutSources §2.2); a kill-set for `tools/mado-mimeglob.py` and the gate itself; QUALITY 158
  instrument (round-93 routed defect 1, still open); the portal entry §8 frozen cases (round-93 routed defect 3, still open).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (pacman paused; nothing needed; every seat reported none). L0 questions: none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — registry rows `mado-mimeglob`, `mado-r94-mimeglob`, `mado-r94-selftest-kills` added and `mado-selftest-strength` updated to three kill-sets (`mado-shokunin/SKILL.md`, rows after `mado-r93-selftest-strength`); no non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — GLib's filename-only type guess on 370 frozen fixtures, 120 fresh layouts and 9745 host names, all agreeing with the installed library (`receipts/c1-measured-r94.txt`, LOG.md round 94); lane-authored.
- [~] Instructions executable by an agent without oral context — the registry rows carry argv and verdict maps; the declaration holds the frozen argv both measurements reproduce; outside-lane test not run.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — round-94 refinements (C1 read-only MIME database reads, C2 data for the unchanged gate) and the cross-domain item above (GLib, freedesktop, glibc; tsukuroi owns the builder hook — cited, not absorbed); no outside-lane approval.
