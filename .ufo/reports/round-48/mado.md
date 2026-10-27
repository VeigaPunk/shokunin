# mado — round 48 report (hyaku run 9, attempt 4)

Lane repo `/home/vgpnk/Projects/shokunin/mado-shokunin`, branch `master`, final lane hash **`b361c8466bd203cda8ce38add796883cf8f97302`** (`git ls-remote origin refs/heads/master` prints it). Base `579f694b45c797a9c39761fdb4f9e0a1b71b3585`. Round shape: **two v1 waves** (policy v1, band 32-64) — `w1` build 41 seats, `w2` falsify 48 seats — plus **one residual attack call** `a4r1` of 8 reviewer/critic seats against the committed data (attempt 4). **Round total 97 seats.** Attempts 1-3 ran w1 and w2; attempt 3's L1 died in the orchestrator session exit (2026-10-26 23:57:36 -03) and its uncommitted outputs were salvaged by the orchestrator as `cf3deeec`. Attempt 4 (this L1, `MadoR48a4`) re-verified that salvage, landed the data, ran `a4r1`, and files this report.

## Work performed

Declared claims (`.ufo/waves/round-48/claims.md`, commit `5ff16742`, before w1); v1 frozen at `3e6c848a`; re-registered **before any data** as v2 at `0216560077efe575b7438dfbefc57e45c94039f7` (`registration-v2.md`), after w2 broke both v1 counters' own control rules. v2 was written after reading w2 (disclosed at `registration-v2.md:11-15`); every w1/w2 candidate was re-scored against it and must miss.

- **C1 — operability (capability acquisition): the warm-cache path of `tools/mado-terminal.py`.** Given a tree, an environment and an existing `$XDG_CACHE_HOME/xdg-terminal-exec`, the tool predicts xdg-terminal-exec 0.14.3's stdout and exit status (hit, stale, invalid, disabled; symlinked, unreadable and default-location caches), names the cache verdict in `explain`, models HOME unset as the pin, and starts no process, opens no socket, writes nothing. Judge: the real pinned resolver in bwrap (`PRED-C1-r48-v2`).
- **C2 — coverage (sourced): `corpus/knowledge/xkb-keymap-compile-r48.md`.** Which `kb_rules/kb_model/kb_layout/kb_variant/kb_options` names compile into a keymap on this host (libxkbcommon 1.13.2, xkeyboard-config 2.48), which fail (layout, variant, rules: rc 1) and which are dropped (option with XKB-595, model silently); rows S340-S351 opened 2026-10-26; read-only `xkbcli compile-keymap` receipt (`PRED-C2-r48-v2`).

Lowest-axis rule: every published axis tied at its maximum at base (round-47 `receipts/axis-tip.txt`, `checked=3 mismatched=0`); the trend furthest behind was **quality** (round-47 closure `unprovable-but-better`), worked by C1. Paths below are under `mado-shokunin/.ufo/waves/round-48/` unless rooted.

- **w1 build (41 seats):** two independent C1 references (`w1/ExecRefCacheA`, `ExecRefCacheB`), `ls -LRl` emulator and fuzz (`w1/ExecLsEmu`), fixture schema v2 and oracle (`w1/ExecFixturesV2`, `ExecOracleV2`), both counters (`w1/ExecCounterC1`, `ExecCounterC2`), XKB pins and live receipt (`w1/ScoutXkbSpecs`, `ExecXkbLive`, `ExecXkbSource`), routed round-47 items D1-D4/R3/R4b (`w1/ExecHomeUnset`, `ScrD1Line`, `ExecD2Receipt`, `ScrErrataD4`, `ExecSessionMarker`, `ExecErrataR45`), id guard (`w1/ExecIdGuard`), premise critics (`w1/CritPremiseC1`, `CritPremiseC2`).
- **v1 freeze `3e6c848a`:** `PRED-C1-r48` (204 warm fixtures), `PRED-C2-r48`, XKB pins (`fetch/`), receipt `receipts/xkbcli-compile-keymap-r48.txt`.
- **w2 falsify (48 seats, 47 reports):** a cache write, a fork, a cold-different `--print-content` hit, `command -v` executability, multi-line cached commands, an unreadable cache, `ls -L` symlinks and a basename `--observed` comparator met C1 v1; a mode-755 pin, a 600-character quote and a PATH-shimmed replay met C2 v1 (`registration-v2.md:19-34`, each with its seat). Every w2 seat is routed with a disposition (`corpus/lessons/round-48.md` `### w2 routing`).
- **v2 freeze `02165600`:** write/fork tripwire, `links` schema, 24 new pin-measured fixtures (228 warm), foreign-root `--observed` capture; C2 pin mode, quote length, `/usr/bin/xkbcli` clean-env replay. Controls: `receipts/v2/ctl-c1v2.txt` — `CTL_C1v2 VERDICT: PASS (controls scoring TARGET_MET: 0 of 66 …)`, landed tool `TARGET_MET`; C2 98-variant harness `receipts/v2/c2v2-revc2counter-matrix.txt` (two v1 admits flip to missed).
- **Attempt-4 salvage re-verification:** `git diff --stat 02165600 cf3deeec -- quality/counters` empty; counter/fixture sha256 `5bb9aead…`/`3ab1f5d0…`/`bb0f0605…` as registered; landed tool sha256 `143820476403…` = the bytes the v2 control set scored (`receipts/v2/ctl/FINAL.txt:1`); a scratch mirror of salvage + entry scores C1/C2 v1 and v2 `TARGET_MET` and census exit 0 (`receipts/a4/pre-c1v2.txt`, `pre-c2v2.txt`, `pre-c1v1.txt`, `pre-c2v1.txt`, `pre-census.txt`). Reused: everything in `cf3deeec` (rows, tool, SKILL/QUALITY/README, errata, receipts) and the untracked entry/lesson/instruments. Corrected (not reverted): two transcribed facts in the lesson (M48-11). Discarded: nothing.
- **Do-nothing controls (§9):** `receipts/a4/ctl-do-nothing.txt` — C2 stub (head + one sentence) `admitted=0/1` (e/f/r fail); held round-46 body under the round-48 head `admitted=0/1` (d/e/f/r fail); C1 base tool (no warm work) `warm=149/228 … TARGET_MISSED`; always-cold `warm=154/228 … TARGET_MISSED`.
- **Round-47 closure items:** D1 (HOME unset modelled as the pin; delta line), D2 (`findings=` receipted at three revisions), D3 (ten readdir fixtures), D4 (append-only erratum, `terminal-route-r17.md:149-150`), R3 (session-material gate v2 + waivers, selftest 69/69), R4b (round-45 errata; frozen `PRED-C2-r45-v2` still `admitted=1/1` at the tip, `a4r1/MadoA4CritSalvage.md:9`), M47-10 (schema v2), CritC1Explain (clause x compares `cmd=`), SentC1Sandbox F1-F4.
- **Residual `a4r1` (8 seats, attempt 4):** attacked the committed data. Four reports, **no release blocker**: `a4r1/MadoA4RevC1v2Diff.md` (21/26 counter hunks registered, 3 partly, 2 unregistered but docstring-stated — residual prose gaps; 204 v1 fixtures unchanged, 24 new match their classes; `TARGET_MET` re-derived), `MadoA4CritEntry.md` (no false sentence in the sample; six `xkbcli` probes agree with the receipt), `MadoA4CritSalvage.md` (errata append-only 187+/0-, frozen round-45 counter still MET, SKILL/README traced), `MadoA4CritAdmission.md` (withheld admission on three evidence gaps — round-47 C1 harm receipt read mid-write, axis at tip, do-nothing controls — each closed after it ran: `receipts/a4/c1-r47-at-tip*.txt`, `receipts/axis-tip.txt`, `receipts/a4/ctl-do-nothing.txt`; it ruled v2 a pre-data repair and C2 a frontier-to-core move). `MadoA4RevLesson` left no report file, but its output (in `a4r1-results.json`) found the lesson's README Frontier locator `:110` blank at the tip — fixed to `:112`. Four seats were lost to the 1 MiB file cap colliding with the clone recipe I prescribed (M48-13). Routing table: lesson `## a4r1 routing`.

## Landed changes

| Commit | Change | LOG.md Round 48 bullet |
|---|---|---|
| `5ff167423ee410251da0ef0c82f8e6fa25875665` | claims, w1 spec + dispatch, census before | 1 |
| `3e6c848a0e1bbc9c7058226b86d0faefc5351c9d` | v1 freeze: registration, counters + warm fixtures, XKB pins + receipt, w1 evidence (41), controls | 2 |
| `0216560077efe575b7438dfbefc57e45c94039f7` | v2 freeze before data: registration-v2, v2 counters + fixtures, S351 pin, controls, w2 evidence | 3 |
| `cf3deeecab6e6633e4204e76d242470cc0cd759a` | orchestrator salvage of attempt 3 (lane identity): rows S340-S351, extended tool, SKILL/QUALITY 96-99/README, r45/r47 errata, round-47 lesson lines, gate v2, w2 results + receipts | 4 |
| `e5d0130d4c68fcf7037dd413907a40dd380860cb` | **data** (attempt 4): entry, lesson round-48, QUALITY 96/99 instruments, waivers, census after, pre-data mirror receipts | 5 |
| `d8e3d6003bf3b5de98e8eb116e1b6d416b2ef883` | SCORECARD/LOG Round 48 (axis publication), after-data receipts | 5-6 |
| `f029de3a7d0b7f8f4a73d9e8b974d9fc3760bb2c` | harm watch (round-47 counters), do-nothing controls, axis at scorecard, a4r1 dispatch, M48-12, S340-S351 range fixes | 6 |
| `627914f6a17665a69a506c8abfce33b761525ca0` | a4r1 evidence + results, lesson a4r1 routing + M48-13, README locator fix, LOG a4r1 line, tip receipts at `f029de3a` | 7 |
| `b361c8466bd203cda8ce38add796883cf8f97302` | final tip receipts at `627914f6` (C1/C2 MET, axis 3/3, outcome-first PASS, census exit 0) | 7 |

Inherited state: the 52 untracked `*.synthetic` files under `.ufo/waves/round-45/` and `round-46/` predate this round and were left untouched (not lane-authored this round). Nothing else untracked at the tip.

## Before → after measurements

- **C1:** `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/counters/c1-r48-terminal-cache-v2.py --repo . --rev <rev> --work <scratch> --nonce 4848`
  - Before (base tool under v2): `cold=190/190 warm=149/228 explained=234/418 generated=210/230 selftest=fail readonly=ok tool=present verdict=TARGET_MISSED`, exit 1 (`receipts/v2/ctl/BASE.txt`).
  - Data `e5d0130d`: `cold=190/190 warm=228/228 explained=418/418 generated=230/230 selftest=ok readonly=ok tool=present verdict=TARGET_MET`, exit 0 (`receipts/c1-after-data.txt`); also at salvage `cf3deeec` (`receipts/a4/c1v2-at-salvage.txt`).
  - Tip: `f029de3a` and final-content `627914f6`: the same `TARGET_MET` line, exit 0 (`receipts/c1-tip.txt`, `receipts/c1-tip-final.txt`; `b361c846` adds only those receipt files).
  - v1 beside it at data: `warm=204/204 explained=394/394 … TARGET_MET` (`receipts/c1v1-after-data.txt`). Self-verdict **TARGET_MET**.
- **C2:** `cd /home/vgpnk/Projects/shokunin/mado-shokunin && TMPDIR=<scratch> python3 -I quality/counters/c2-r48-xkb-entry-v2.py --repo . --rev <rev>`
  - Before (base `579f694b`): `admitted=0/1 verdict=TARGET_MISSED`, exit 1 (`receipts/a4/c2v2-before-base.txt`).
  - Data `e5d0130d`: `clauses=a:1 … r:1 admitted=1/1 verdict=TARGET_MET`, exit 0 (`receipts/c2-after-data.txt`); v1 beside it `admitted=1/1` (`receipts/c2v1-after-data.txt`).
  - Tip: `f029de3a` and `627914f6`: `admitted=1/1 verdict=TARGET_MET`, exit 0 (`receipts/c2-tip.txt`, `receipts/c2-tip-final.txt`). Self-verdict **TARGET_MET**.
- **Harm watch:** axis `python3 -I quality/check-axis-scores.py --rev <rev> --repo .` → `MADO_AXIS: checked=3 mismatched=0` at `d8e3d600` (navigation 65/65, calibration 86/86, operability 12/12; `receipts/a4/axis-at-scorecard.txt`); the data commit reads STALE in the two-phase window (`receipts/axis-data.txt`). Round-47 counters at `d8e3d600`: `PRED-C2-r47 admitted=1/1 TARGET_MET` (`receipts/a4/c2-r47-at-tip.txt`); `PRED-C1-r47` `TARGET_MET` on 3 of 4 runs, the fourth `readonly=fail` from a lone `???( <detached ...>` strace line (bwrap attach noise, M48-12; `receipts/a4/c1-r47-at-tip.txt:196`, `-run2..4.txt`).
- **Live host capture:** `receipts/live-terminal-cache-r48.txt` — tool sha256 = landed bytes, resolver sha256 = the v0.14.3 pin, cold and primed-warm states AGREE with the real resolver, cache in scratch.

## Sources & frontier

Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`:
- Before (`receipts/census-before.txt`): W04 ×17, W01 ×1, `mado ok`, exit 0.
- After (`receipts/census-after.txt`): W04 ×17, W01 ×1, `mado ok`, exit 0 (identical apart from the exit line; no new URL repeats a held one).

- **Rows:** 276 → **288**, `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- **Added by tier:** A ×12 (S340-S349, S351 code pins of libxkbcommon 1.13.2 / xkeyboard-config 2.48; S350 own-work host receipt); all `mined`, opened 2026-10-26, used-by the XKB entry. Gate lines with URL, access date and located ≤25-word quote: `corpus/lessons/round-48.md` `## Gate`; rejects (ArchWiki keyboard page, unpinned xkbcommon.org index, held-duplicate Hyprland `IKeyboard.cpp`) with reason and flip.
- **Rows touched old→new:** none (append-only after `| S339 |`; held S318/S319 byte-identical).
- **Frontier advanced:** README Frontier bullet "Round 48 moves the input-device XKB compile itself onto sourced ground", which also moves the round-47 bullet's "warm-cache path" from open to executed ground. Knowledge entries 64 → 65.
- **Sourced claim:** C2 rests on S340-S351.
- **Assimilation: none.** No `merge/mado/` theme on either plane (`w1/ScoutShokuknow`). Id guard (`assimilation/`): reg-ids 276 (S001-S339), staged-ids 147 (S203-S349), collisions 84 (S203-S221, S253, S258, S277-S339); guard proven on an indented `  | S002 |` fixture (`w1/ExecIdGuard`). Renumber map: none (no staged row adopted). Quarantine slice: 13 rows (S189, S195, S201, S205, S224, S228 payload-absent; S199, S200, S209, S222, S223, S225, S235 unchecked), none appended or hand-checked.
- **considerthese:** `considerthese/2026-10-26.md` proposal 6 ("Lead with round-level outcomes, not counter internals") landed as QUALITY 99 with `quality/check-round-outcome-first.py`; round 48's SCORECARD section reads `OUTCOME_FIRST: round=48 verdict=PASS` at `d8e3d600`.
- **Mistakes mined:** M48-1..13 (`corpus/lessons/round-48.md` `## Mistakes`), QUALITY 96-99.

## Trend verdicts

- **expansion: improved.** One new entry on ground held open at base (`hyprland-input-devices-r46.md:69`, README Frontier), rows 276 → 288, one capability row (warm-cache terminal selection) with a live capture.
- **quality: improved.** C1 is judged by the real resolver with 228 warm fixtures and a write/fork tripwire; v2 closed every v1 hole w2 found before data, and 66 control candidates miss; entry errors found by w2 (step 9 severity, `--model nope`, include-path attribution) were corrected before data. Limits: the session-material gate is installed but red at the tip (`SESSION_MATERIAL: … findings=159`, `receipts/a4/session-material-tip.txt`; selftest 69/69), M48-8 coverage gap routed.
- **discernment: improved** (self-assessed, pending the non-author closure). The v1 control rule was not run at freeze (M48-9) and w2 caught it; the repair re-scored the complete control set before data and discloses that v2 is not blind to w2. Attempt 4 caught two transcribed facts in the salvaged lesson (M48-11) and a flaky harm-watch read (M48-12) instead of reporting them as green or red. Against it: the residual dispatch's file cap and clone recipe were incompatible and cost 4 of 8 attack seats (M48-13).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. New sections "XKB keymap compile (round 48)" and "Terminal cache (round 48)" (`SKILL.md:2226`, `:2294`, salvage `cf3deeec`); traced row by row by `a4r1/MadoA4CritSalvage.md:11-12`, a seat this lane dispatched — not a non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Live read-only warm-cache capture with AGREE (`.ufo/waves/round-48/receipts/live-terminal-cache-r48.txt`) and host `xkbcli compile-keymap` receipt; LOG.md Round 48. No non-author verifier.
- [~] Instructions executable by an agent without oral context. Two independent w1 references rebuilt the cache path from the pin (`w1/ExecRefCacheA.md`, `w1/ExecRefCacheB.md`). Dispatched seats are not outside-lane verifiers.
- [~] No cross-domain bleed (PROVINCE.md still accurate). `w1/ConnSiblings.md`: no sibling lane claims the resolver cache or the XKB compile. No non-author verifier.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none (bwrap, strace, python3, xkbcli present; no seat reports an install; pacman untouched).

Seats: w1 41 (executor 17, scribe 10, scout 4, critic 4, connector 2, sentinel 2, reviewer 1, revenger 1); w2 48 (executor 23, critic 10, reviewer 6, connector 3, sentinel 3, mutation-tester 2, scout 1); a4r1 8 (reviewer 5, critic 3). Dead seats: w2 `CritCounterTiming` (hung on a 900 s budget attack; its output is a reasoning fragment, no report file). a4r1 `MadoA4RevC1Write` and `MadoA4RevGate` aborted ("RLIMIT_FSIZE=1 MiB rejects numerous committed large files"), `MadoA4RevC2v2Diff` ended without a report ("Index lock >1MiB"), `MadoA4RevLesson` ended without a report file (its findings are in the results output); all four are M48-13. So the new clause-r mutant attack and the gate both-ways demonstration did not run this round. Planner seat: held by the L1 (validator rejects `planner`). Reused from earlier attempts: all 89 w1+w2 seats; new this attempt: 8.

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists only `.ufo/reports/round-45/kengaku.md` (another lane's; untouched) and this report; no mado seat file at the fleet root.

Scratch: `/fast/scratch/hyaku/mado-r48` removed after landing (`ls /fast/scratch/hyaku | grep -c mado-r48` → 0).

Open L0 questions: none filed. The attempt-3 lesson's "L0 question filed" for M48-10 was false and is corrected; the operator cache it concerned was rewritten by a resolver run at 23:59:27 (metadata only read), so no decision is open.
