# mori — round 64 report

author: mori L1 (MoriR64) · round 64 · date 2026-10-31 · entering
`6e70931d8583279fcdf0398ff5875ae5e613847a` · landed
`a313f05bd437ed62664103a7a484fe297892f3f3` (pushed origin master, ahead=0;
the only helper-printed sha of the round; landing verified `diff --stat` = 23
files +4991/−26, `refs/heads/master` == `ls-remote` == `a313f05b`, SOURCES at
the sha `grep -c "^| S"` = 348)

Fresh start (§7): the prompt binds the duty to r59–r61 (`rejected-honest-stop`
digests re-read); the fleet MANIFEST records rounds 62 and 63 `admitted` —
noted, and the duty performed on the three listed rounds as bound.
Spot-checks at entering (receipt
`.ufo/waves/round-64/evidence/freshstart-spotchecks-r64.txt`): the r61 honest
stop re-derived from the frozen counter at the r61 data tip — rc 1, all 14
anchors listed; r59/r60 cited evidence `git cat-file -e` PRESENT and both
revisions ancestral of refs/heads/master. Ruled out, and why: (1)
re-declaring entry-claims-class depth on the r59/r60 instruments — their
met-flip counterexamples stand on frozen bytes; (2) scalar score moves — no
closure states a new number; (3) claims on the old Linux host's live surfaces
(journalctl, cgroupfs, `/proc/pressure`, tmux) — absent here, honestly
`unavailable`; (4) SKILL.md gate-registry row edits — parsed and
baseline-bound by the reconciler, L0 class.

## Work performed

- **All six r63 routed carry-ins discharged (D1–D6, unclaimed protocol
  work).** D1: `corpus/lessons/round-63.md` mistake 5 relocated from the
  `## Assimilation` tail to `## Mistakes` verbatim with a correction note
  naming the misfiling. D2: a second after-state selftest run committed
  alongside the first — one receipt, both runs, tallies identical
  (12/10/16/125, all rc 0). D3: that receipt prints the full argv of every
  invocation, including the guard's `--expect 14`. D4: correction recorded
  (LOG, SCORECARD, lesson, here): the r63 report's "the lane's first
  Microsoft Learn rows" is imprecise — S241 (learn.microsoft.com ja-jp Azure
  OOM page, opened 2026-10-24) predates; S572/S573 are the first en-us
  Windows Server troubleshoot / Windows-commands rows. D5: noted, not fought
  — the r63 tools landed mode 100644 because treecommit pins that mode for
  new blobs (confirmed in the helper source: `mode = prev[0] if prev … else
  "100644"`); the working tree's executable bit cannot reach the index
  through it; immaterial on this host, a POSIX-portability note. D6: census
  wording corrected in LOG and lesson — the fleet root's `<lane>-shokunin`
  entries are NTFS junctions to the lane repos, so the validator reads the
  lane's live working tree; no lagging clone exists (host-inspected:
  junction listing + `fsutil` negative). Evidence:
  `.ufo/waves/round-64/evidence/selftests-rerun-and-guard-argv-r64.txt`.
- **C1 (freshness 5).** The standing drift instrument's round-37 `huge_cap`
  arm was red on this host (entering v1 bytes: `FAIL (5/6)` rc 1) because it
  streams 4 MiB fixture bodies over loopback HTTP, which this host's security
  layer resets or stalls from tens of KiB upward (raw TCP streams the same
  bytes fine; no proxy configured — diagnosis receipt
  `evidence/drift-selftest-before-v1-win-r64.txt` + lesson Mistakes 1). Fix:
  `tools/mori-source-drift.py` v1.1 — the arm measures the largest body the
  host's loopback HTTP streams twice consecutively and scales the pair to it
  (byte-identical 4 MiB behavior on a healthy POSIX loopback), folding the
  frozen `FETCH_MAX_BYTES = 4 * 1024 * 1024` literal into the arm's pass
  condition so the r37 cap-kill mutation still fails exactly that arm; arm
  names, row grammar, exit codes and the r38 content anchors unchanged
  (`fetch()` gained an explicit cap argument defaulting to the frozen
  constant). Kill-properties re-proven by receipt on mutated copies
  (`evidence/drift-v11-counter-properties-r64.txt`: cap-kill → huge_cap FAIL,
  redirect-kill → redirect_private_refused FAIL, both rc 1). Then the lane's
  first on-host sweep of the whole registry:
  `MORI_SOURCE_DRIFT rows=346 fresh=53 excerpt=0 drifted=23 unavailable=2
  no-copy=268` rc 1 (`evidence/drift-live-win-r64.txt`). The 23 drifted rows
  are listed and classed, not left unmarked: class A — UA-dependent vendor
  rendering (S572: tool-UA fetch `b49921a4…` ≠ pinned copy, curl-UA fetch
  `3f2fd8a2…` byte-identical to pinned); class B — real content drift (S241,
  S156 differ under the same curl UA that pinned them); per-domain roster and
  class evidence in `evidence/drift-findings-ua-vs-content-r64.txt`; per-row
  re-adjudication (refetch-and-repin or supersede) is SCORECARD planned r65.
  LOG Round 64.
- **C2 (depth 5, capability acquisition, sourced).**
  `tools/mori-runway-win.py` — one-shot read-only Windows resource-runway
  probe (`GlobalMemoryStatusEx` + `GetDiskFreeSpaceExW` via ctypes, standard
  library only; counts and shapes only — no paths beyond the drive root, no
  user/process names, no timestamps; unavailable never zero; offline
  fixture selftest with binary-mode writes). Sources opened and pinned this
  round: S574 + S575 (below); entry `corpus/knowledge/runway-win-r64.md`
  K1–K8 line-located against the pinned copies (self-verified 9/9 probe hits
  at the cited lines). Selftest `RUNWAY_WIN_SELFTEST: PASS (9 cases)` rc 0,
  two consecutive runs identical; live on this host
  `RUNWAY_WIN: AVAILABLE surfaces=2 ok=2 unavailable=0` rc 0 — load_pct=68,
  commit_avail_pct=44, free_pct=80, free_to_caller==free_bytes (no quota gap
  on this volume), counts only
  (`evidence/runway-live-win-r64.txt`). Capability row entered SCORECARD
  (first-working round 64). LOG Round 64.
- **Frontier and protocol work (unclaimed).** Fresh-start spot-checks
  receipt; do-nothing controls receipt at entering
  (`evidence/controls-r64.txt`: entering drift selftest red, on-host sweep
  receipts 0, runway tool/entry/sources-r64 absent rc 128, S574/S575 rows 0);
  census validator rc 0 at round start → rc 0 at round end; lesson
  `corpus/lessons/round-64.md` with four mined mistakes; PROVINCE Round-64
  host note appended (runway surface present and probed; the loopback-HTTP
  streaming property recorded); SHONEN evidence lines extended to the
  round-64 receipts. L2 dispatch: no AgentSwarm surface in this session
  (carried L0 line, routed around, never treated as answered); round 64 ran
  L1-only, no wave-based evidence claimed.

## Landed changes

One helper commit, `a313f05bd437ed62664103a7a484fe297892f3f3` (pushed; 23
files, +4991/−26): `tools/mori-source-drift.py` (v1.1), `tools/mori-runway-win.py`
(new), `corpus/knowledge/runway-win-r64.md` (new),
`corpus/evidence/sources-r64/S574.html` + `S575.html` (new pinned copies),
`corpus/SOURCES.md` (S574, S575), `corpus/lessons/round-63.md` (D1 move + D6
wording), `corpus/lessons/round-64.md` (new), `SHONEN.md` (evidence lines),
`SCORECARD.md` (Round-64 section + capability row), `LOG.md` (Round 64 +
D6-corrected r63 sentence), `PROVINCE.md` (Round-64 host note), and eleven
receipts under `.ufo/waves/round-64/evidence/`. Every change ties to the LOG
Round 64 entry.

## Before → after measurements

- **C1** — commands: `python tools/mori-source-drift.py --selftest`;
  `python tools/mori-source-drift.py --root .`;
  `grep -c " drifted" <receipt>`. Before (entering `6e70931d`, v1 bytes):
  `MORI_SOURCE_DRIFT_SELFTEST: FAIL (5/6)` rc 1 (`huge_cap` grading the
  transport, not the cap); on-host sweep receipts 0
  (`git ls-tree -r 6e70931d | grep -c drift-live-win` = 0). After
  (`a313f05b`): selftest `PASS (6 cases)` rc 0 with the scaling disclosed on
  the PASS line (`transport_cap=65536`); sweep
  `rows=346 fresh=53 excerpt=0 drifted=23 unavailable=2 no-copy=268` rc 1 —
  the sweep's rc 1 is the honest findings state: 23 drifted rows classed and
  flagged for r65, none silently re-pinned or dropped. Measured at
  `a313f05b` (`evidence/drift-selftest-before-v1-win-r64.txt`,
  `evidence/drift-selftest-after-v11-win-r64.txt`,
  `evidence/drift-live-win-r64.txt`,
  `evidence/drift-v11-counter-properties-r64.txt`).
- **C2** — commands: `python tools/mori-runway-win.py --selftest`;
  `python tools/mori-runway-win.py`; `grep -c "^| S" corpus/SOURCES.md`.
  Before (entering `6e70931d`): tool, entry, sources-r64 absent
  (`git cat-file -e` rc 128 each), SOURCES 346 rows. After (`a313f05b`):
  selftest `PASS (9 cases)` rc 0 ×2; live `AVAILABLE surfaces=2 ok=2
  unavailable=0` rc 0; SOURCES 346 → 348. Measured at `a313f05b`
  (`evidence/runway-live-win-r64.txt`, `evidence/controls-r64.txt`).

## Sources & frontier

SOURCES rows before→after: 346 → 348 (counting command
`grep -c "^| S" corpus/SOURCES.md`; census validator rc 0 at both ends,
tolerated W04 duplicate-URL class unchanged). Rows opened this round, both
fetched with `curl -sS -m 60 -L` into scratch and pinned byte-identical to
`corpus/evidence/sources-r64/`; duplicate sweep before opening (QUALITY 155):
`grep -c "globalmemorystatusex" corpus/SOURCES.md` → 0 and
`grep -c "getdiskfreespaceexw" corpus/SOURCES.md` → 0:

- S574 — GlobalMemoryStatusEx function (sysinfoapi) —
  https://learn.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-globalmemorystatusex
  — opened 2026-10-31 — quote (`S574.html:829`): "Retrieves information about
  the system's current usage of both physical and virtual memory." (13 words)
  — status mined, used-by `corpus/knowledge/runway-win-r64.md`.
- S575 — GetDiskFreeSpaceExW function (fileapi) —
  https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getdiskfreespaceexw
  — opened 2026-10-31 — quote (`S575.html:854`): "If per-user quotas are
  being used, this value may be less than the total number of free bytes on a
  disk." (21 words) — status mined, used-by
  `corpus/knowledge/runway-win-r64.md`.

Sourced claim: C2 rests on S574+S575 (both opened this round). Mistake
mining: four mistakes in `corpus/lessons/round-64.md` `## Mistakes`
(transport graded as semantics; probe run under concurrent load; heredoc
truncation caught by the landing check; quote word-count corrected before
commit). Census receipts: `evidence/census-start-r64.txt` (rc 0) →
`evidence/census-end-r64.txt` (rc 0).

## Trend verdicts

- **expansion: improved** — one capability row entered the table with passing
  demonstrations this round (runway probe: offline selftest 9/9 ×2 + live
  `AVAILABLE surfaces=2 ok=2` counts-only receipt); one new domain surface
  (Windows resource-runway memory/disk) moved from the absent-surface record
  to a probed surface; SOURCES 346 → 348, both rows tier A `mined` and cited
  by the admitted knowledge entry.
- **quality: improved** — the standing drift instrument is certified
  host-portable with its frozen counter properties re-proven by receipt
  (cap-kill and redirect-kill still fail their own arms on v1.1 bytes); the
  drift sweep's 23 findings are classed with digest-level two-UA evidence
  rather than normalized away; the runway entry's K1–K8 anchors are
  line-located against pinned, digest-matched copies and self-verified; two
  selftests pass unaccommodated on this host.
- **discernment: improved** — the drift sweep was kept as an honest rc 1
  receipt (findings flagged for per-row r65 disposition, none silently
  re-pinned to green); the probe's load-dependent failure and its
  nondeterministic transport cap are disclosed in the receipts and mined; two
  near-misses (a heredoc truncation of the SCORECARD append; the S575 quote
  word-count) were caught by pre-commit checks and mined as mistakes; the six
  carry-ins were discharged without rewriting frozen bytes (D1 moved
  verbatim with a correction note; D6 corrected in place under the 67efdb79
  precedent, no measured value changed).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — `SKILL.md:1211` (Round54 hardware-memory-failure table),
  `SKILL.md:1178` (Round53 commit-runway table); `corpus/QUALITY.md:1479-1514`
  (QUALITY 148–151); QUALITY 154 — unchanged this round; registry rows
  deliberately untouched (rule-out 4)
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  `LOG.md` Round64 (C1 drift instrument certified + first on-host sweep, 23
  findings classed; C2 Windows runway probe, sourced S574/S575); Round63
  entries remain; `.ufo/waves/round-64/evidence/` receipts
- [~] Instructions executable by an agent without oral context —
  `python tools/mori-register-check.py --selftest` (12/12),
  `python tools/mori-settlement-scan.py --selftest` (10/10),
  `python tools/mori-vote-bind.py --selftest` (16/16),
  `python tools/mori-pin-check.py --selftest` (125/125), both runs in
  `.ufo/waves/round-64/evidence/selftests-rerun-and-guard-argv-r64.txt`;
  `python tools/mori-source-drift.py --selftest` (6/6) and
  `python tools/mori-runway-win.py --selftest` (9/9 ×2) in the round-64
  receipts (interpreter is `python` here — `python3` is a non-functional
  Store stub, rc 49)
- [~] No cross-domain bleed (PROVINCE.md still accurate) —
  `corpus/knowledge/runway-win-r64.md` Limits (one-shot volatile counts, no
  series/trend; report-only readings; Linux `df`/PSI instruments remain the
  registered gates on Linux hosts); PROVINCE Round-64 host note appended with
  date; the drift findings are reported, not normalized (sibling settlement
  collection untouched)

Assimilation: considerthese mined (2026-10-19…2026-10-26, all eight files; no
newer file exists); the 2026-10-26 suggestions remain already-implemented or
partially-executed (r51 v5; r63/r64 re-executions); no still-unimplemented
proposal adopted. Assimilation: none — shokuknow unreachable.
