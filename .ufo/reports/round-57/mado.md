# mado — round 57 (hyaku run 12, 2026-10-31): the host changed

Base `5337d2509f5c91c6f200b6637cf77bd0ad1cd67f` → lane tip
`f71c0f98e0b38e56f811bdc6018498f6413ed9be` (commits `13b00d5c` + `f71c0f98`,
both helper-committed and pushed to `origin/master`; `git ls-remote` verified
local=remote). The live host changed after round 56: this round ran on
**Windows 11 Home, build 26200** (`HOME=/c/Users/jpvei`, MINGW64_NT-10.0-26200;
Python 3.13.15 as `python`, no `python3`). Three claims: C1 **freshness**
(lowest scored non-retired axis, 9.6552), C2 **operability** (capability), C3
**coverage** (sourced). Security boundary held: no r56-era credential material
was printed, copied, excerpted or surfaced; the affected r56 wave receipt was
never opened; the new instrument reads no environment values and no window
titles (M56-17's routed criterion applied).

## Work performed

- **C1 freshness — host-change drift detected, flagged, recorded; freshness
  rubric re-baselined.** Probes showed every omarchy-era surface absent
  (11/11 tool binaries via `command -v`; 10/10 config/doc trees via `test -e`
  under `$HOME`), and the gate confirms the drift as an absence record, not a
  regression: `bash tools/mado-verify.sh --no-live` →
  `MADO_VERIFY: DIVERGED (17 fail, 7 unknown, 2 pass)`, first fail
  `hypr.file.root` (missing `~/.config/hypr/hyprland.conf`),
  `gate.boundary.readonly` PASS
  (`.ufo/waves/round-57/receipts/gate-nolive-windows.txt`). Landed: dated
  host-change record + surface state register in `PROVINCE.md` (8 groups: 7
  absent with re-derivation probes, 1 observed — the Windows desktop plane),
  a `tools/mado-win-desk.py` tool row in the province table, and `SKILL.md`
  § Round 57 (omarchy-host claims frozen as host-scoped; six carried rules;
  secret/titles/env boundaries restated). Evidence: `PROVINCE.md:128-162`
  (host-change record, probe block, register, tool row), `SKILL.md:2366-2404`.
- **C2 operability (capability acquisition) — `tools/mado-win-desk.py`.**
  Read-only Windows desktop observer: live mode spawns exactly one fixed
  PowerShell child (CIM OS identity, `Screen.AllScreens`, `AppliedDPI`/
  `LogPixels` via two in-process registry layers, `dwmapi!
  DwmIsCompositionEnabled`, `Get-Process` census + `GetForegroundWindow`),
  parses stdout as JSON, re-prints whitelisted fields only; `--from-file`
  re-derives a verdict from a captured snapshot; `--selftest` spawns nothing.
  Verified: selftest 9/9 exit 0 (`receipts/selftest.txt`); live
  `MADO_WINDESK: CLEAN (screens=1 dpi=96 dwm=on windows=6)` exit 0
  (`receipts/windesk-live1.txt`); cross-check **5/5 stable fields AGREE**
  against independently executed probes (`receipts/xprobe-indep.txt` +
  `receipts/crosscheck.txt`; window census bound-only, point-in-time);
  malformed snapshot → `MADO_WINDESK: ERROR` exit 2 with raw bytes never
  echoed; tool ledger population 98 → 99
  (`LEDGER: population=99 ledger_rows=99 uncovered=0 dangling=0 …
  verdict=TARGET_MET` at `f71c0f98`). Tool sha256 at landing
  `92a51aec1cf1bd57…` (work-window hash `92a51aec1cf1bd57` re-bound at commit,
  QUALITY 7).
- **C3 coverage (sourced) — `corpus/knowledge/windows-desktop-plane-r57.md`.**
  First sourced record of the new host's desktop plane: 5 host rows (H01-H05,
  each with its re-derivation command), 7 dated `[INF-docs]` rows (K01-K07),
  4 claim-to-host joins (J01 `agreement*` — at 96 DPI the bitmap-stretch path
  is never exercised; J02 `agreement` carrying S400's own manifest caveat),
  divergence D01 (S399's Vista/7-era "runs as a Windows service … can be
  enabled and disabled" sentence versus the same doc set's "As of Windows 8,
  DWM composition is always enabled" and the observed TRUE), limits section.
  Sources: rows **S398-S401** (Microsoft Learn High-DPI page, DWM overview,
  `DwmIsCompositionEnabled`, `Screen` class — all four opened in full
  2026-10-31 with ms.date/git_commit recorded, ≤25-word verbatim quotes).
  Index row + route paragraph added to `corpus/README.md`.
- **Protocol work (§6 absent-surface correction, not a failure):** the
  freshness sub-axis re-baseline recorded in `SCORECARD.md` — new rubric
  "surface-state audit currency" (0/8 → 8/8), old rubric "file-plane gate
  agreement" marked **dormant, host-absent** (not silently retired; disposal
  routed to L0).
- **L2 disclosure:** MISSION's ≥8-L2 batched-dispatch floor is **not met —
  no dispatch surface is reachable from this lane session on this host**; the
  round is L1-only work, disclosed in SCORECARD, LOG, and an appended L0 line
  asking for a ruling or a route.
- Mistake mining: **M57-1..M57-4** in `corpus/lessons/round-57.md` (checker
  scratch policy refuses this host's canonical scratch; the tool's Windows
  temp-file lock; a mis-drafted counting command caught pre-freeze; an import
  slip caught by the selftest with an orphaned temp dir swept).

## Landed changes

| Change | Commit |
|---|---|
| `PROVINCE.md` host-change record + register + tool row; `SKILL.md` § Round 57; `SCORECARD.md` round-57 section; `LOG.md` entry; `tools/mado-win-desk.py`; `quality/tool-ledger.md` row; `corpus/knowledge/windows-desktop-plane-r57.md`; `corpus/README.md` index+route; `corpus/SOURCES.md` S398-S401 + search log; `corpus/lessons/round-57.md` | `13b00d5cb0a6989398d2ae522914deb0e58a1aaf` |
| Committed receipts (`.ufo/waves/round-57/receipts/`: census both ends, gate absence, tool selftest/live/independent-probes/crosscheck/snapshot/from-file/PINS) + receipt pointers re-pointed from scratch to committed paths | `f71c0f98e0b38e56f811bdc6018498f6413ed9be` |

Every change has a LOG.md entry (round-57 block). No existing knowledge entry,
registry row cell, or gate byte was modified: `tools/mado-verify.sh` sha256 is
equal at base and tip (`050efc720599345a…` both), verified from
`git show`.

## Before → after measurements

- **C1 (freshness).** Register rows:
  `git show 5337d2509f5c91c6f200b6637cf77bd0ad1cd67f:PROVINCE.md | grep -cE '^\| .* \| (absent|observed) \(2026-10-31\) \|'` → **0**;
  `git show f71c0f98e0b38e56f811bdc6018498f6413ed9be:PROVINCE.md | grep -cE '^\| .* \| (absent|observed) \(2026-10-31\) \|'` → **8**.
  Supporting host probes (2026-10-31): 11/11 binaries absent, 10/10 trees
  absent, gate `--no-live` DIVERGED (17/7/2). New freshness rubric:
  `10 × dated register rows / declared surface groups` = 0.0000 → **10.0000**
  (8/8; finite-denominator limit noted, as with the navigation rubric).
- **C2 (operability, capability).**
  `git ls-tree 5337d25 --name-only tools/ | grep -c win-desk` → **0**;
  `python tools/mado-win-desk.py --selftest` →
  `MADO_WINDESK_SELFTEST: 9/9 assertions passed`, exit 0;
  `python tools/mado-win-desk.py` → `MADO_WINDESK: CLEAN (screens=1 dpi=96
  dwm=on windows=6)`, exit 0; cross-check receipt → `CROSSCHECK: 5/5 stable
  fields AGREE`; `python quality/check-tool-ledger.py --repo . --rev f71c0f98`
  → `population=99 ledger_rows=99 … TARGET_MET` (base rev: 98/98).
- **C3 (coverage, sourced).** `ls corpus/knowledge/*.md | wc -l`: 71 → **72**;
  `grep -cE '^\| \`knowledge/[^\`]+\.md\`' corpus/README.md`: 71 → **72**;
  `grep -cE '^[[:space:]]*\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: 334 → **338**;
  navigation counter (SCORECARD § Counting command, fleet round 1, run with
  `python` — the host has no `python3`) at `f71c0f98`:
  `indexed=72/72 missing=0 dangling=0 duplicates=0 coverage=10.0000/10`, exit 0.

All counts re-derived at the landing tip `f71c0f98` (not transcribed).

## Sources & frontier

SOURCES registry rows **334 → 338** (S398-S401, tier A, `mined`, opened
2026-10-31; counting command above). Census before:
`.ufo/waves/round-57/receipts/census-before.txt` → `mado ok`, exit 0; after:
`receipts/census-after.txt` → `mado ok`, exit 0; the two emits are
byte-identical (36 W04 duplicate-URL-across-scopes warnings + 1 W01, all
pre-existing; the diff is empty — no new warning for S398-S401). Search log §
Round 57 records the bounded sweep (4 candidates identified, 4 opened, 4
included, 0 excluded — no rejected-row event; stated, not hidden). Mistake
mining: M57-1..M57-4 (lesson § Mistakes), including the sweep that found the
checker-scratch incompatibility. Frontier: the lane's live surface moved from
the omarchy plane (now absent, registered) to the Windows desktop plane
(observed, sourced entry); the D01 flip, per-monitor DPI joins and the
checker-scratch portability fix are the named round-58 leads.

## Trend verdicts

- **expansion: improved** — one new declared surface group observed and
  sourced (the Windows desktop plane, 0 prior citations → 4 sourced rows + an
  indexed entry at 72/72 reachability), with the abandoned plane's absence
  registered rather than dropped.
- **quality: improved** — the drift every present-tense claim silently carried
  after the host swap is now named, dated and probed; the instrument landed
  with its own able-to-fail receipts (selftest red on first Windows run —
  M57-2 — before landing green); no existing artifact's bytes were rewritten
  to fake continuity (gate sha equal base↔tip).
- **discernment: unchanged** — no non-author admit/reject sample exists this
  round (no dispatch surface; L1 only), so by the round-53/56 precedent the
  trend cannot be scored improved. What the round can show: layers are kept
  separate (7 `[INF-docs]` rows never host facts; J01 marked a vacuous
  agreement; D01 named as doc-era drift instead of being resolved by taste),
  and the honest-stop discipline is visible in what was *not* claimed (no
  retired rubric, no invented Windows pins, no per-monitor claims). The
  claimed-but-unverifiable improvement is recorded as an outside spot-check
  list in the lesson § Outside spot-check, ready for the closure; absent that
  judgment the verdict stays `unchanged`.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — historical assertion
  (`corpus/knowledge/executor-test-sufficiency.md`); this round adds § Round 57
  (host boundary) without outside-lane verification. No non-author verifier
  available (L1-only round).
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  historical assertion (`config-health-report-r3.md`, VER-M3); this round's
  end-to-end work (absence sweep → register → observer → sourced entry) is
  lane-asserted, not outside-verified.
- [~] Instructions executable by an agent without oral context — historical
  assertion; the round-57 § Verify blocks (entry + SKILL + PROVINCE probes)
  are written to that standard, unverified from outside.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE was
  corrected this round precisely to keep it accurate on the new host (absent
  surfaces recorded, Windows plane declared read-only, tool row added);
  historical assertion (VER-M4B) otherwise stands.

## Assimilation

`considerthese/` mined (nine files, 2026-10-19..2026-10-28): nothing adoptable
this round — 2026-10-28 proposal 2 was already addressed (r56 attempt-2
receipt), the 2026-10-19 "refresh the live plane" proposal is void (its object
host is gone; answered by C1's absence register), and the remainder are
operator-process suggestions outside the lane's write surface. **Assimilation:
none — shokuknow unreachable.**

## Open L0 (report-time grep, M56-13 routed fix)

`grep '^mado |' .ufo/l0-questions.md` shows unresolved lines from rounds 1
(:37), 21 (:78), 22 (:83), 23 (:103), 28 (:133, :134), 29 (:135), 34 (:149,
:150, :151), and the r56 resolution pair (:212, :224) — more than the four
named in M56-13; all remain open, none treated as answered. Added this round:
`mado | round-57 |` (freshness-rubric disposal + L2-floor waiver/route on this
host).
