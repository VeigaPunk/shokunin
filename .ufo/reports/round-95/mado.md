# mado — round 95 report (hyaku run 15, attempt 3)

L1 `MadoR95a3`. Lane `mado-shokunin`, branch `master`, base `4a2af6817024f6ed47084a5217c1825ae247f4fe` (round-94 closure
tip), final lane hash **`5ef746b7a678185d1fd1b84283af1f18aee33816`** (`git ls-remote origin refs/heads/master` prints it).
Attempts 1–2 of round 95 were abandoned mid-flight by earlier L1 instances (watchdog log shows the relaunches); this
attempt re-verified every inherited artifact against the frozen digests before landing anything — all matched — and
carried the round to closure. Nothing from the earlier attempts was trusted unverified.

## Work performed

Declared claims (`mado-shokunin/.ufo/waves/round-95/claims-declaration-r95.md`, frozen at `a689d2e3`):
**C1 — coverage (new surface, capability):** `tools/mado-mimesniff.py` answers, read-only, which MIME type and
uncertainty flag GLib 2.90.1 `g_content_type_guess_for_data` gives file bytes with a name, cache and text mode — the
magic/alias/parent sections of `mime.cache` plus round-94's filename step. **C2 — operability:** kill-sets that let the
round-93 selftest-strength gate guard `tools/mado-mimeglob.py` and `tools/mado-portals.py` (round-94 spot-check routed
defect 3, two of the five unguarded tools). Sourced claim: C1 (S519–S523 opened this round, S505 re-opened). Inputs: the
round-94 non-author spot-check and `considerthese/2026-11-06.md` proposal 4 (a content-sniffing step).

- Protocol load and inputs: the round-94 non-author spot-check (five routed defects; defect 3 → C2, defects 1/2/4/5
  dispositioned in the lesson Gate), `considerthese/2026-11-06.md`, round-94 lesson/report/SCORECARD. Sources opened by
  the L1 and seats, two fetches each with sha256: GLib 2.90.1 `xdgmimecache.c` (magic/data sections), `xdgmimeint.c`,
  `gcontenttype-fdo.c`, `glocalfileinfo.c`, shared-mime-info spec 0.21 at its moved locator (`receipts/sources-open-r95.txt`
  plus the append-only 301-stub correction, lesson M95-2). The L1 wrote the oracle
  (`controls/mimesniff-oracle-r95.c`, against the installed glib2 2.90.1-1) and the first candidate before the wave.
- Wave w1 (14 seats) built and attacked: 204→300 oracle-labelled cases in 20 classes and a fresh generator
  (R95MExecCasesC1; its DRAFT run found 7 real candidate deviations), the C1 counter implementing every PRED-C1
  conjunct incl. the audit-hook launcher and forgery leg (R95MExecCounterC1), a 4911-path host file list and the harm
  harness (R95MExecHostC1; 19,644 DRAFT comparisons, 0 differences), 87 counted mutants with 2 not countable for stated
  reasons (R95MMutC1), F1 VT/`isspace` falsification with a 256-value sweep (R95MProbeC1, R95MReviewC1), first-draft
  kill-sets covering all labels (R95MExecKillsC2), the C2 counter and 24+ panel weakenings (R95MExecCounterC2),
  escapes and closing kills for both tools (R95MMutC2), a blanket-production-rebinding forgery met by 2 kills
  (R95MReviewC2), freeze-ready repairs (R95MCritic), the sibling/assimilation sweep — mado uniquely owns XDG content
  sniffing, `merge/mado/` holds no staged MIME-magic entry (R95MConnector), the entry draft (R95MScribeEntry), source
  re-audit confirming all 8 GLib digests (R95MScoutSources).
- L1 integration before the freeze (lesson "Wave findings routed"): candidate rewritten `c1` → `c1b` → `c1c` (VT/isspace
  table port per the 256-sweep, wrapped-compare recursion fix, no-database and text-mode refusals); frozen set 300 cases
  / 2863 inputs / 20 classes (min 9 per class); 94 counted mutants, 5 excluded with arguments; C1 predicate enumerates
  the 20 classes plus `class_kills=20/20` and `real_rebuild` conjuncts; C2 kill-sets re-drafted to the c2b candidates
  (mimeglob 22 kills `fab72daf…`, portals 42 kills `4c7fc2b3…`), panel 75 hand weakenings + 47 single-check
  neutralisations + 6 neutrals, conjunct (vii) first-draft control (28/75) and (viii) ≥36 singleton labels.
- Pre-freeze controls executed and committed in the freeze: C1 candidates DRAFT_TARGET_MET for `c1c`, wave `c1`/`c1b`
  MISS; forgery-as-candidate rejected through the static leg with `audit_denials=4`
  (`receipts/c1-controls-prefreeze-r95.txt`); C2 frozen candidates DRAFT_TARGET_MET 75/75 + 47/47, first drafts 28/75
  MISSED, the R95MReviewC2 blanket forgery 34/75 MISSED, empty kill-sets 0/47 + 0/75 MISSED
  (`receipts/c2-controls-prefreeze-r95.txt`).
- Freeze `a689d2e3dc968c6909a7dce0575cd392ecc57109`; C1 `9afa39f5342fe19b661513b4de9854324508da84`; C2
  `6f6955f9cf6ff9bf8f5e769f6b8d8ff79ac55ce3`; records `5a41b43821e135a3ab576c7bb239d7924b4e4c12` + addendum
  `5ef746b7a678185d1fd1b84283af1f18aee33816` (the frozen 300-case set and two w1 case dumps landed only in the
  addendum — they post-date the freeze commit; disclosed here and in the lesson).
- **Cross-domain evidence** encountered: GLib xdgmime/gcontenttype/glocalfileinfo (GNOME/GLib), the shared-mime-info
  format and `update-mime-database` (freedesktop.org), `g_content_type_guess_for_data` callers in gio (R95MConnector §:
  `glocalfileinfo.c` sniffs only when the name guess is uncertain, up to the caches' magic extent ≤16384 B; on Hyprland
  `xdg-open` falls back to `file(1)` via `xdg-mime` rather than GIO). R95MConnector swept every sibling `PROVINCE.md`:
  only mado reads MIME database bytes; no other lane owns the surface.

(Receipt paths are under `mado-shokunin/.ufo/waves/round-95/`.)

## Landed changes

| Commit | What | LOG.md |
|---|---|---|
| `497c6fcd372b817d8423dcd37ece08216012433c` | w1 dispatch evidence: declaration draft, first candidate, oracle source, sources-open, census start, assimilation check | LOG round 95 "Landed" |
| `a689d2e3dc968c6909a7dce0575cd392ecc57109` | freeze: declaration with w1 amendments, frozen cases/mutants/panel/candidates/kill-set drafts, both counters, pre-freeze controls, w1 evidence | LOG round 95 "Landed" |
| `9afa39f5342fe19b661513b4de9854324508da84` | C1: `tools/mado-mimesniff.py` (= frozen candidate `build/mado-mimesniff.c1c.py`), `corpus/knowledge/mime-magic-sniff-r95.md`, S519–S523, S505 used-by, PROVINCE/SKILL/ledger/index rows | LOG round 95 "Landed" |
| `6f6955f9cf6ff9bf8f5e769f6b8d8ff79ac55ce3` | C2: `quality/selftest-kills/mado-mimeglob.json` (22 kills), `quality/selftest-kills/mado-portals.json` (42 kills), SKILL/ledger/PROVINCE rows | LOG round 95 "Landed" |
| `5a41b43821e135a3ab576c7bb239d7924b4e4c12` | records: lesson (M95-1…M95-4, Gate), QUALITY 163–165, SCORECARD round 95 + capability row, LOG entry, used-by updates, measurements, separability, harm watch, census end, records gates, w1 stragglers | LOG round 95 entry itself |
| `5ef746b7a678185d1fd1b84283af1f18aee33816` | records addendum: frozen 300-case set (`controls/mimesniff-cases-r95-frozen.json`, sha `ee815b4f…`), `w1/R95MProbeC1-cases.json`, `w1/R95MReviewC1-cases.json` | same |

## Before → after measurements

- **C1 (coverage, new surface)** — `python3 -I quality/counters/c1-r95-mimesniff.py --repo . --rev
  9afa39f5342fe19b661513b4de9854324508da84 --base-rev 4a2af6817024f6ed47084a5217c1825ae247f4fe --cases
  .ufo/waves/round-95/controls/mimesniff-cases-r95-frozen.json --expect-cases-sha256 ee815b4f… --mutants
  .ufo/waves/round-95/controls/mimesniff-mutants-r95-frozen.json --expect-mutants-sha256 0e45964a… --oracle-src
  .ufo/waves/round-95/controls/mimesniff-oracle-r95.c --expect-oracle-sha256 99df35f8… --fresh-gen
  .ufo/waves/round-95/controls/mimesniff-fresh-r95.py --expect-fresh-gen-sha256 15396113… --host-files
  .ufo/waves/round-95/controls/mimesniff-host-files-r95.txt --expect-host-files-sha256 9d5947a7… --expect-tool-sha256
  4ef019c6… --expect-mimeglob-sha256 65f80a6c… --forgery .ufo/waves/round-95/controls/forgery-sibling-ctypes-r95.py
  --expect-forgery-sha256 5cb0fbad… --fresh 120 --workers 28 --scratch-root DIR` (full digests in the declaration and
  SCORECARD). Measured at `9afa39f5`: frozen cases answered as the installed GLib does, base **0/300 (no tool) →
  300/300**; `TARGET_MET tool_pin=ok cases=300 correct=300 classes=20/20 fresh=120/120 host=9822/9822 mutants=94
  killed=94 class_kills=20/20 real_rebuild=11/11 static_no_external_resolver=ok audit_denials=0`, controls do-nothing 17,
  name-only 57, naive 186, memoriser_fresh=0/120, forgery rejected — `receipts/c1-measured-r95.txt`, rc 0. Separability:
  C1 re-run at the C2 tip `6f6955f9` `TARGET_MET` with memoriser_fresh=1/120 (`receipts/c1-at-tip-r95.txt`).
- **C2 (operability)** — `python3 -I quality/counters/c2-r95-selftest-kills.py --repo . --rev
  6f6955f9cf6ff9bf8f5e769f6b8d8ff79ac55ce3 --panel .ufo/waves/round-95/controls/selftest-panel-r95-frozen.json
  --expect-panel-sha256 8c6dfdac… --expect-gate-sha256 2d6f1219… --expect-kills-sha256 fab72daf…,4c7fc2b3…
  --control-kills .ufo/waves/round-95/build/mado-mimeglob-kills.c2.json,.ufo/waves/round-95/build/mado-portals-kills.c2.json
  --expect-control-kills-sha256 f4b80be6…,64b3c10d… --workers 16 --scratch-root DIR`. Measured at `6f6955f9`:
  weakenings of the two tools' selftests flagged by a lane instrument **0/75 → 75/75** (before = the do-nothing
  instrument; no kill-set existed; the wave's first drafts flagged 28/75), single-check neutralisations **0/47 → 47/47**;
  `TARGET_MET positive=OK:0,OK:0 neutralised_flagged=47/47 hand_flagged=75/75 neutral_ok=6/6 do_nothing_flagged=0
  always_ok_flagged=0 always_weak_positive=WEAK:1,WEAK:1 shadiff_neutral_ok=0/6 gate_selftest=ok
  control_hand_flagged=28/75 singleton_labels=36/47 tool_pin=ok,ok` — `receipts/c2-at-tip-r95.txt`, rc 0.
  Separability: C2 counter at `9afa39f5` `SETUP_ERROR … kill-sets absent`, rc 2 (`receipts/c2-at-c1-r95.txt`).
- Harm watch at `6f6955f9` (`receipts/harm-final-r95.txt`): gate selftest 460/460, `--no-live` CLEAN 29, index 116/116,
  ledger 185/185, mako 62/62, portals 28/28, mime 17/17, xdgmime 12/12, mimeglob 19/19, mimesniff 26/26, seat-reports
  23/23, receipt-presence 6/6, selftest-strength 11/11 with OK 32/32 on the real gate, the two new kill-sets OK 22/22 and
  42/42, round-90 C2 83/83 28/28, round-92 C2 45/45 with its round-91 leg, round-93 C2 TARGET_MET, round-94 C1 TARGET_MET
  370/370 and C2 TARGET_MET 29/29; the round-90 C1 counter's SETUP_ERROR on the ported portal tool as declared in round
  93; unchanged-tool diff empty. No axis harmed.

## Sources & frontier

- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`:
  start `mado ok` rc 0 (`receipts/census-start-r95.txt`); end `mado ok` rc 0 (`receipts/census-end-r95.txt`). Rows by
  `grep -cE '^ {0,3}\| S[0-9]{3,} ' corpus/SOURCES.md`: 453 → 458.
- Rows added by tier: A 5 — S519 `xdgmimecache.c` magic/data sections, S520 `xdgmimeint.c` binary/text fallback, S521
  `gcontenttype-fdo.c` guess-given-data, S522 `glocalfileinfo.c` sniff caller, S523 shared-mime-info spec 0.21 §2.5/§2.9/
  §2.12 at its moved locator (the S517 locator now 301s; fetched twice at HTTP 200, lesson M95-2); each carries a
  ≤25-word located quote and `corpus/knowledge/mime-magic-sniff-r95.md` used-by; S505 used-by extended.
- Rows touched old→new: S519–S522 used-by entry → `+corpus/lessons/round-95.md`; S523 new. Logged in the lesson.
- Frontier: the bytes→type step of the content-sniffing plane moves to core (`corpus/README.md` round-95 frontier line;
  index 115 → 116); `xdg-open`'s `file(1)` fallback and launch stay frontier.
- Mistakes mined: M95-1 (the L1 ported `g_ascii_isspace` from C `isspace` — VT 0x0b differs; its own selftest encoded
  the error; shown able to fail — wave candidate misses the frozen `lltext` cases; QUALITY 163), M95-2 (a 301 redirect
  body hashed as the source; QUALITY 164), M95-3 (the selftest-strength gate cannot carry a kill-set for its own
  selftest — `non_selftest_prefix` blind spot; routed), M95-4 (the draft C1 predicate scored refusals as a label class
  and let one crashing input relabel siblings; QUALITY 165).
- Gate decisions: admit/reject table in the lesson `## Gate` — the wave candidate `c1`/`c1b` rejected (replaced by
  `c1c`), the scribe's digest sentence rejected (301 stub), the first-draft kill-sets superseded by c2b, the blanket
  forgery rejected as a kill-set, assimilation rejected (no staged entry; `reg-ids` 453, `staged-ids` 147,
  `collisions` 94 at `.ufo/waves/round-95/assimilation/`).
- Assimilation: none — no staged MIME-magic entry in `merge/mado/` (R95MConnector §3).
- considerthese: `considerthese/2026-11-06.md` proposal 4 mined into C1 (lesson `## Considerthese`).

## Trend verdicts

- **expansion — improved:** a new desktop surface (file bytes → MIME type with name/cache/text mode) moves into core with
  an admitted entry (index 115 → 116), five tier-A rows and one capability row; at base no lane tool answered it
  (0/300 → 300/300).
- **quality — improved:** C1 300/300 with 94/94 mutants, fresh 120/120, host 9822/9822, class_kills 20/20 and
  real_rebuild 11/11 against the installed GLib, plus an audit-hook launcher and a forgery leg; C2 75/75 hand weakenings
  and 47/47 neutralisations where no instrument existed before (first drafts 28/75); harm watch green incl. both prior
  rounds' counters.
- **discernment — improved:** the wave's attacks became predicate clauses before any measurement (VT table port,
  oracle-exec/ctypes forgery, blanket kill-set forgery, refusal-as-label); the spec departures (word_size never read,
  priority-80 threshold, per-cache ordering) are recorded as GLib's behaviour; four reject decisions with evidence; two
  L1-authored defects (M95-1, M95-2) are named and mined rather than silently fixed. Non-author closure spot-check
  pending.

## Round shape and extras

- Shape: ONE v1 wave `w1` of 14 seats (scout 1, scribe 1, executor 5, connector 1, reviewer 3, critic 1, mutation-tester
  2; attack 6/14 = 43 %), spawned via the inline handoff (`w1.ready`, l1 `MadoR95a3`); WAVE-DONE received; no residual
  call — w1's ≥32 attack items were folded into the frozen predicates pre-freeze. Round total 14; dead seats 0;
  `w1-results.json` retains every seat's output. Planner seat held by the L1. Routing per the live
  `task.agentModelOverrides` (no model passed).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only orchestrator-owned `.scratch/`
  churn, `trail-ids.txt` and `f.txt` (both predate this round, name no lane) — no mado-r95 seat files at the fleet root;
  nothing moved.
- Attempts: this is attempt 3; attempts 1–2 left the freeze inputs, w1 results and build artifacts intact — every frozen
  digest was re-verified against the declaration before the first commit of this attempt (all matched).
- Scratch: `$HYAKU_SCRATCH/mado-r95` retained under `/fast/scratch` for the counter receipts' `--scratch-root` audit
  trail.
- Routed to round 96: `tools/mado-mako.py`, `tools/mado-verify.sh`, `quality/check-receipt-presence.py` still without
  kill-sets (three of the five unguarded tools from round-94 defect 3 remain); the gate's own selftest kill-set is
  structurally impossible under `non_selftest_prefix` (M95-3 — needs a predicate change, not a kill-set); QUALITY 158
  instrument and the portal entry §8 frozen cases (round-93 routed defects, still open); the C1 tool docstring's
  citation check.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (pacman paused host-wide; nothing needed; every seat reported none). L0 questions: none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — registry rows `mado-mimesniff`, `mado-r95-mimesniff`, `mado-r95-selftest-kills` added and `mado-selftest-strength` updated to five kill-sets (`mado-shokunin/SKILL.md`, rows after `mado-r94-selftest-kills`); no non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — GLib's content-type guess given bytes on 300 frozen fixtures, 120 fresh cases and 9822 host files, all agreeing with the installed library (`receipts/c1-measured-r95.txt`, LOG.md round 95); lane-authored.
- [~] Instructions executable by an agent without oral context — the registry rows carry argv and verdict maps; the declaration holds the frozen argv both measurements reproduce; outside-lane test not run.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — round-95 refinements (C1 read-only MIME database reads, C2 data for the unchanged gate) and the cross-domain item above (GLib, freedesktop; cited, not absorbed); no outside-lane approval.
