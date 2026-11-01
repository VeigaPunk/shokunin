# mori — round 70

Lane: `fleet/mori-shokunin` (branch master; helper-only writes). Entering
`9dc4314d1572fe3e2ae18dd8c9c8f51f1263736f` (r69 verifier spotcheck tip) ·
landed `de431a7484f250d46ecd3f6c008524f47134aa1e` (pushed origin master;
`git ls-remote origin refs/heads/master` prints it; 24 files, +2740/−3,
every path inside the lane repo, entering rev ancestral).

## Work performed

Declared claims (two, one axis-move each on distinct axes, causally
separable; fresh-start duty re-performed before declaring — see below):

1. **C1, depth (sourced S581, opened this round)** — the short-window
   rotation-bound receipts: three same-UA A/A pairs on the S241
   instrument-UA body at computed windows 31 s / 91 s / 304 s, chosen at and
   below the documented AWS WAF token-immunity scale (S581: default 300 s,
   challenge minimum 300 s, CAPTCHA minimum 60 s), each receipt stating its
   own window (QUALITY 161), counts and shapes only. Finding: rotation is
   NON-UNIFORM at the documented scale points — caught within the 91 s
   window (`per-response=4 same-bytes=false`), absent within the 31 s and
   304 s windows (`per-response=0 same-bytes=true`) — so the observed
   rotation tracks no single per-interval clock at these scales. Byte-identity
   spans are receipted in the shas (pair B's capture B == pair C's capture A
   `6e7b906d…`; pair A's body == pair B's capture A `e4bf924c…`). No TTL
   value decided, no mechanism named (the client answers no challenges —
   S581's update mechanism describes challenge responses this client never
   performs), no row re-classed, no grammar taught (QUALITY 159/161
   intact). Receipts: `.ufo/waves/round-70/evidence/shortwin-a-r70.txt`,
   `shortwin-b-r70.txt`, `shortwin-c-r70.txt` (lane repo, commit
   `de431a74`). This executes the r69 SCORECARD planned item.
2. **C2, operability (sourced S582, opened this round; capability
   acquisition)** — `tools/mori-uptime-win.py`: the Windows host-uptime
   read — one-shot read-only GetTickCount64 via ctypes, standard library
   only, restype pinned `c_ulonglong` (the selftest pins the exact
   unsigned-64-max rendering so a truncating build cannot pass). It reads
   the boot window of this host's own evidence (the r63 event-log counts
   and the r64 runway reads accumulate inside it; live `uptime_d=5` — the
   r63/r64/r70 evidence shares ONE boot window). The caveats travel on
   every receipt line: `count=biased` (S582:842 — includes
   sleep/hibernation; QueryUnbiasedInterruptTime stays unopened),
   `boot_identity=absent` (the API returns none, never inferred), the
   debug-build ~49-day shift recorded (S582:845), system-timer resolution
   10–16 ms (S582:836). No liveness verdict (a hung host still accrues
   uptime); not a census surface; boot-state diagnosis stays
   tsukuroi/operator. Selftest 8/8 rc 0 ×3
   (`.ufo/waves/round-70/evidence/uptime-win-selftest-r70.txt`); live rc 0
   ×3, separate one-shot counts never a rate
   (`.ufo/waves/round-70/evidence/uptime-win-live-r70.txt`); entry
   `corpus/knowledge/uptime-win-r70.md` K1–K5 line-located in the pinned
   S582 copy; capabilities row entered in SCORECARD the same round.

Work items:

- Fresh-start duty: r59/r60/r61 rejected closures re-read and re-derived
  with own receipts (`evidence/freshstart-spotchecks-r70.txt`): frozen r61
  counter at the r61 data tip → `C2=unmet` rc 1 (same verdict as the r61
  closure and the r65–r69 re-derivations); r59/r60/r61 cited lane revs
  PRESENT and ancestral; fleet report commits PRESENT. **Ruled out, and
  why**: (1) re-declaring the r59–r61 entry-claims instruments — their
  met-flip counterexamples stand on frozen bytes (re-derived unmet again);
  (2) scalar score moves — no closure states a new number; (3) claims on
  the old Linux host's live surfaces — absent here, honestly unavailable;
  (4) editing the frozen bytes (SKILL.md, mori-source-drift.py,
  mori-drift-adjudicate.py, PROVINCE.md, AGENTS.md, corpus/README.md) —
  the SKILL:905 tally pin and the r65–r69 receipts bind them; (5) a bare
  re-run of the admitted r64–r69 sweep/disposition/re-check/separation
  work — re-declaration, not an axis-move; (6) a third churn grammar —
  r67's ruling stands, QUALITY 159 untouched; (7) a live observation of
  the cross-check arm's inconsistent branch — the vendor decides that;
  the arm stays standing; (8) a boot-identity read — the API returns none
  and the province refuses boot-state diagnosis. All declared claims are
  unreachable by a do-nothing round (`evidence/controls-r70.txt`: every
  r70 receipt/tool/entry/pin absent at entering rc 128; SOURCES 353 rows
  at entering, zero URL matches; lesson absent rc 128).
- SOURCES curation (contract v1): S581 + S582 opened this round, QUALITY
  155 duplicate sweeps run INTO the receipts before each fetch
  (`evidence/source-s581-r70.txt`, `source-s582-r70.txt`), rows appended
  INSIDE the Registry section immediately after S580, both `mined`.
- Mistake mining: four mistakes in `corpus/lessons/round-70.md`
  (placeholder digest typed from memory into a drafted citation, caught by
  the verify-before-land re-read; an existence check run against the wrong
  repo, corrected on the receipt with an explicit correction line; a
  receipt header transcribing the wrong file, fixed in place before
  landing; a lesson edit that duplicated its own sentences, caught by the
  read-back rule).
- Standing battery green on unchanged bytes: register 12/12, settlement
  10/10, vote-bind 16/16, pin-check 125/125, adjudicate 5/5, recheck
  10/10, ua-variance 14/14 (`evidence/selftests-battery-r70.txt`).
- Frozen-set check by content, not git status (this host's index is the
  standing garbage condition; treecommit plumbing only): all six frozen
  files' worktree sha256 == `git show HEAD:<file>` sha256
  (`evidence/orphan-scan-r70.txt`); the round diff contains none of them.
- L2 concurrency (MISSION): the batched ≥8-L2 dispatch surface is absent
  in this lane session on this Windows host (standing since r62) — round
  70 ran L1-only over committed bytes, this host's network and this
  host's own surfaces; no wave-based evidence is claimed. The mori |
  round-62 and mori | round-65 L0 lines were re-verified unanswered this
  round (`evidence/l0-considerthese-r70.txt`) and routed around, never
  treated as answered; the SKILL:905 python3-naming rule was honored
  (every command used `python`).

## Landed changes

All tied to the `LOG.md` "Round 70" entry; one commit by the lane
identity: `de431a7484f250d46ecd3f6c008524f47134aa1e`.

- `corpus/SOURCES.md` (+2 rows: S581, S582, append-only verified by
  `tools/mori-sources-appendonly.py <entering> --round-base <entering>` →
  `round_changed=[]` exit 0, receipt
  `.ufo/waves/round-70/evidence/sources-appendonly-r70.txt`; the 50
  historical violations are pre-existing history, unchanged —
  `round_changed=[]` is the gate's round-scoped verdict).
- `tools/mori-uptime-win.py` (new, 278 lines) + `corpus/knowledge/uptime-win-r70.md`
  (new, K1–K5).
- `corpus/lessons/round-70.md` (new: gate + 4 mistakes + wave/assimilation).
- `SCORECARD.md` (+49 lines, append-only at EOF: round-70 section, claim
  table, capabilities row, planned r71), `LOG.md` (+92, append-only),
  `SHONEN.md` (3 evidence lines updated, marks untouched `[~]`).
- `.ufo/waves/round-70/evidence/` — 15 receipts (census start/end,
  controls, freshstart spotchecks, l0+considerthese, selftests battery,
  shortwin a/b/c, source openings ×2, appendonly gate, orphan scan,
  uptime selftest/live).
- Report filed at `.ufo/reports/round-70/mori.md` (fleet repo; not
  lane-committed, per contract the orchestrator commits it).

## Before → after measurements

- **C1 (depth 5):** before —
  `git cat-file -e 9dc4314d:.ufo/waves/round-70/evidence/shortwin-b-r70.txt`
  rc 128 (no short-window receipt existed; the smallest stated window
  anywhere in the tree was the r68 receipt's derivable-but-unstated
  1268 s). after — `grep -oE "window-s=[0-9]+" .ufo/waves/round-70/evidence/shortwin-{a,b,c}-r70.txt | sort -u`
  → 31, 91, 304; `grep -h "UA_VARIANCE" <same receipts> | grep -c "per-response=4"`
  → 1 and `per-response=0` → 2, rc 0 each (measured at commit
  `de431a74`). Self-verdict: **verified met** (closure to re-derive).
- **C2 (operability 7):** before —
  `git cat-file -e 9dc4314d:tools/mori-uptime-win.py` rc 128 (tool, entry
  and pins absent). after — `python tools/mori-uptime-win.py --selftest` →
  `UPTIME_WIN_SELFTEST: PASS (8 cases)` rc 0 ×3 at the final bytes;
  `python tools/mori-uptime-win.py` → `UPTIME_WIN: AVAILABLE surfaces=1
  ok=1` rc 0 with `count=biased boot_identity=absent` on the line (live
  receipt `evidence/uptime-win-live-r70.txt`, measured at commit
  `de431a74`). Self-verdict: **verified met** (closure to re-derive).
- **SOURCES (frontier):** `grep -c "^| S" corpus/SOURCES.md` 353 (at
  entering, verified against `git show 9dc4314d:corpus/SOURCES.md`) →
  355 (at `de431a74`).
- **Census (validator):** start
  `.ufo/waves/round-70/evidence/census-start-r70.txt` (2026-11-01, rc 0,
  tolerated W04 duplicate-URL class only, command + rc embedded) → end
  `.ufo/waves/round-70/evidence/census-end-r70.txt` (rc 0, same tolerated
  class). Exit 0 required at round end: met.

## Sources & frontier

SOURCES rows 353 → 355 (counting command `grep -c "^| S" corpus/SOURCES.md`;
census validator rc 0 before and after):

- **S581** — AWS WAF Developer Guide, "Setting timestamp expiration and
  token immunity times in AWS WAF" (docs.aws.amazon.com), opened
  2026-11-01T19:52:49Z, pinned `corpus/evidence/sources-r70/S581.html`
  sha256 `5e5b941e97c0aa6e2d7bd958bdc66a6fbb2a260508880e99becda543e71fc865`
  (16179 bytes), duplicate sweeps 0/0/0 receipted INSIDE the receipt
  before the fetch; located quotes `S581.html:54` (10 words), `:59-60`
  (19 words), `:70-71` (15 words), `:83-84` (11 words). Teaches the
  documented token-clock machinery and its scale; used-by C1 and
  `corpus/lessons/round-70.md`.
- **S582** — Microsoft Learn, "GetTickCount64 function (sysinfoapi)",
  opened 2026-11-01, pinned `corpus/evidence/sources-r70/S582.html` sha256
  `580f1935fb47b5c992a48d22299f7452aaeb00099f2ac96ba74c92002a18277f`
  (52661 bytes), sweeps 0/0 receipted INSIDE the receipt before the fetch;
  located quotes `S582.html:829` (14 words), `:833`, `:836`, `:842`
  (20 words), `:845`. Teaches the host-uptime read and its boundaries;
  used-by C2's entry `corpus/knowledge/uptime-win-r70.md`.
- Frontier moves: none closed. FR-boundaries honored (no census surface,
  no baseline re-pin, no threshold); the C1 receipts decide no TTL value;
  QueryUnbiasedInterruptTime stays unopened (recorded in the S582 row and
  the entry).

## Trend verdicts

- **expansion: improved** — SOURCES 353 → 355, both rows opened, pinned
  byte-receipted and mined this round; one capability entered the
  repertoire table with a demonstrated run (selftest ×3 + live ×3); both
  claimed axes carry falsifiable before→after data (claims table in
  SCORECARD at `de431a74`). No admitted entry failed its bar.
- **quality: improved** — the C1 finding sharpens the r68/r69 rotation
  record with stated-window receipts at new scales and an honest
  non-uniformity result; C2's tool carries the caveats on its output line
  so they cannot be lost in copying; the four round defects were caught
  before landing, fixed, and mined; the standing battery is green on
  unchanged bytes; no entry found false and left unmarked.
- **discernment: improved** — the round declined the overreach reading of
  its own best data (rotation within 91 s vs the documented 300 s floor is
  reported as observed non-uniformity, never as mechanism or TTL); the
  inconsistent-branch live observation was refused as unmanufacturable;
  eight fresh-start rule-outs are named with reasons; four mistakes are
  mined with captured-by and fix; the L0s were re-verified unanswered and
  routed around without being treated as answered.

## Per-axis verdicts (self-assessed; closure re-derives)

| Axis | Verdict | Basis |
|---|---|---|
| depth | improved | C1 (sourced S581) — the rotation-bound receipts |
| operability | improved | C2 (sourced S582) — the uptime capability runs and verifies |
| freshness | unchanged | no freshness claim; the standing sweep/separation work untouched (r66/r68 bytes unmodified) |
| coverage | unchanged | no coverage claim; the surface gain is recorded as capability + entry, the PROVINCE head stays byte-frozen (r65 L0 set) |
| calibration | unchanged | no calibration claim; the window grammar (QUALITY 161) was applied, not extended |
| adjacency | unchanged | no sibling surface touched; boot diagnosis stays tsukuroi (the entry's Boundaries) |

No axis harmed: the axes-table cells are untouched (append-only
SCORECARD; `git diff 9dc4314d..de431a74 -- SCORECARD.md` has 0 deletions
outside the SHONEN file, whose marks stayed `[~]`), all standing
selftests are green on unchanged bytes, and the frozen set is absent from
the round diff.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — untouched this round (frozen byte; the r69-entry tally
  pins bind it); QUALITY 161 was applied as practice
  (`window-s=` on all three r70 receipts).
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  `LOG.md` Round70 (C1 the short-window rotation-bound receipts, sourced
  S581 — rotation caught within the 91 s window, absent at 31 s and
  304 s, byte-identity spans in the shas, no TTL decided; C2 the Windows
  host-uptime read `tools/mori-uptime-win.py`, sourced S582 — live rc 0
  with `count=biased boot_identity=absent` on the line); receipts
  `.ufo/waves/round-70/evidence/` (15 files, all in commit `de431a74`);
  and the carried Round69/Round68/Round67/Round66/Round65/Round64 entries
  with their evidence dirs.
- [~] Instructions executable by an agent without oral context —
  `python tools/mori-uptime-win.py --selftest` (8/8, the round-70 build —
  a new tool, not an edit of any pinned instrument; three consecutive
  runs in `.ufo/waves/round-70/evidence/uptime-win-selftest-r70.txt`);
  round-70 standing battery on this Windows workspace host
  `.ufo/waves/round-70/evidence/selftests-battery-r70.txt` (interpreter is
  `python` here — `python3` is a non-functional Store stub, the standing
  SKILL:905 L0 routed around; the loopback-transport disclosure of r64-r68
  is carried).
- [~] No cross-domain bleed (PROVINCE.md still accurate) —
  `corpus/knowledge/uptime-win-r70.md` Limits+Boundaries (the uptime read
  is fleet-evidence context only — no boot identity, no liveness verdict,
  no census surface; boot-state diagnosis stays tsukuroi/operator; the
  PROVINCE head stays byte-frozen and takes no edit); the C1 receipts
  teach no grammar and re-class no row (QUALITY 159 untouched).

## Assimilation

considerthese re-mined (2026-10-19…2026-10-26, all eight files; no newer
file exists — checked this round, receipt
`.ufo/waves/round-70/evidence/l0-considerthese-r70.txt`): the 2026-10-26
suggestion 1 (split pin-check mismatches into "can't run here" vs "stale")
remains the one still-unimplemented proposal and remains behind the
operator's open instrument-change ruling (the mori | round-65 L0 line).
Adopted nothing. Assimilation: none — shokuknow unreachable.
