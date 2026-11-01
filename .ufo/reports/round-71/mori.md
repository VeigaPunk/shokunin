# mori round-71 report — the located-line erratum, the working-state read, the boot-window-paired events receipt

lane: mori-shokunin (森 — fleet & host observability) · round 71 · date 2026-11-01
entering `015787e6f5aa7eb2c3e11066bcef7bf0428c17b6` · measured commit `3627fac03f00ee904b45c9a9511b842356b1b46b` (branch tip, pushed: local `refs/heads/master` == `ls-remote origin refs/heads/master` == `3627fac0`, ahead=0)
round type: FRESH-START (r59/r60/r61 rejected-honest-stop closures re-read and re-derived; see below)

## Work performed

FRESH-START duty (per §7): the r59/r60/r61 closures were re-derived with this round's own
receipts before anything was declared (`.ufo/waves/round-71/evidence/freshstart-spotchecks-r71.txt`:
the frozen r61 counter at the r61 data tip → `C2=unmet` rc 1, the same verdict the closures and
the r65–r70 re-derivations reached; the eight lane revs PRESENT and ancestral rc 0 each; the
three fleet report commits PRESENT). Eight rule-outs are named with reasons in the lesson
(`corpus/lessons/round-71.md` §Fresh start) — among them: the entry-claims instruments (frozen
met-flip counterexamples), scalar score moves (no closure states a number), the old Linux
host's surfaces (absent here), the six frozen bytes (SKILL.md, PROVINCE.md, AGENTS.md,
corpus/README.md, mori-source-drift.py, mori-drift-adjudicate.py — the SKILL:905 tally pin and
the r65 L0 stay routed around), the one-off rotation-recurrence pair (the r70 closure's own
~92 s re-run already receipts the second-session data point; a designed multi-window protocol
is a bigger instrument than this round carries — planned for r72 as an instrument), the
cross-check arm's inconsistent branch (cannot be manufactured honestly), in-place edits to
drifted r70 artifacts (corrections are new entries), and the Precise variant (S584:876,
unopened). Do-nothing controls: `.ufo/waves/round-71/evidence/controls-r71.txt` — every r71
artifact absent at entering rc 128; SOURCES 355 rows at entering, zero `supersedes S582` rows,
zero S584-URL matches; QUALITY `162.` absent.

Carry-in duty (round-70 closure §6, status-neutral — addressed first, both discharged as C1):
- **D1 (S582 located-line drift)** — erratum landed as new entries, zero in-place rewrites:
  supersedes row **S583** (teaches opens `supersedes S582 —`, INSIDE the Registry after S582)
  re-points :833→:834, :842→:841, :845→:842; the page was RE-OPENED this round and is
  byte-identical to the r70 pin (sha256 `580f1935…`, receipt
  `.ufo/waves/round-71/evidence/source-s582-reopen-r71.txt`), so the corrected pointers bind
  the live body too; the erratum receipt `s582-pointers-erratum-r71.txt` greps each quoted
  sentence against its recorded line (0 — the recorded :833/:845 are `<h2>` headings) and its
  actual line (1); the r70 knowledge entry takes an append-only correction block (K2/K4/K5
  re-pointed, K1/K3 re-confirmed exact); QUALITY **162** makes located-line pin-verification
  procedural.
- **D2 (sweep-count precision)** — corrected old→new in the round-71 lesson Gate: the r70
  lesson said `sysinfoapi` sweep 0; the r70 receipt records rows=1 (the S574 row; the
  keyword matches its row text), and the page-identifying `gettickcount64` sweep was and is 0,
  so the admit decision stands. The r70 lesson bytes untouched.

Claimed this round (three claims, three distinct axes; C1 and C2 both work lowest-scoring
axes — calibration and depth, tied at 5 — satisfying the lowest-axis rule):

- **C1 (calibration, sourced S583)** — the D1/D2 discharge as an axis-move: before, the
  record carried unverified located-line pointers and no rule forced pin-verification; after,
  S583 + erratum + entry correction block + QUALITY 162, able-to-fail against the drifted
  pointers themselves. Evidence: `.ufo/waves/round-71/evidence/s582-pointers-erratum-r71.txt`,
  `source-s582-reopen-r71.txt`, `corpus/QUALITY.md` criterion 162,
  `corpus/knowledge/uptime-win-r70.md` r71 correction block, `corpus/lessons/round-71.md`
  Gate (D2 old→new).
- **C2 (depth, sourced S584 opened this round)** — capability acquisition
  `tools/mori-workstate-win.py`, the Windows working-state read: GetTickCount64 (ms) beside
  QueryUnbiasedInterruptTime (100-ns units floored to ms, conversion named on the line —
  S584:817 grounds the unit; the 10000x trap pinned by the unit_math selftest arm), the
  failed-call signature mapped to honest-unavailable (S584:826-827 — a zero RETURN is never a
  zero count), zero-is-real (S584:828), the signed-delta read model declared and traveling
  (`read_model=two-separate-reads`), `count=biased+unbiased boot_identity=absent
  debug_build_caveat=carried` on every line (S584:833). No episode attribution, no power
  diagnosis (tsukuroi/operator; PROVINCE head byte-frozen, no edit), no liveness verdict, the
  Precise variant unopened. Entry `corpus/knowledge/workstate-win-r71.md` K1–K6 line-located
  in the pinned copy. Evidence: `evidence/workstate-selftest-r71.txt` (10/10 x3), 
  `evidence/workstate-live-r71.txt` (rc 0 x3), `evidence/source-s584-r71.txt` (sweep before
  fetch, with the keyword-vs-slug interpretation).
- **C3 (operability)** — capability acquisition `tools/mori-events-context-win.py`, the r70
  planned note (b) verbatim: one command re-derives the r63-class event-log counts (read-only
  `wevtutil qe` child) bound WITH the boot window (the uptime child) in one captured receipt;
  child bytes never echoed (redaction arm), unparseable summaries leg-unavailable never
  guessed, PARTIAL still pairs with the state word traveling, and
  `boot_binding=none events_window=recent-N-not-boot-scoped` on every receipt — the pair
  shares the host, never a time window. Evidence: `evidence/events-context-selftest-r71.txt`
  (10/10 x3), `evidence/events-context-live-r71.txt` (PAIRED rc 0 x3).

Other work items: fresh-start re-derivations + rule-outs (above); standing selftest battery on
unchanged bytes with the interpreter-posture finding disclosed
(`evidence/selftests-battery-r71.txt`: under `python -I` the host's PYTHONUTF8=1 is ignored,
register-check's fixture write falls back to cp1252, selftest rc 1 — environment dependency
disclosed, tool bytes unchanged, a versioned encoding pin routed beside the open r65 L0);
L0 mori round-62/round-65 lines re-verified unanswered and routed around; considerthese
re-mined (`evidence/l0-considerthese-r71.txt`, newest-named 2026-10-26.md, with the receipt's
own first newest-file line corrected-in-place-and-disclosed after an `ls -t` mtime tie);
six mistakes mined; census start and end receipts with explicit command+rc headers (the r70
closure's nit applied forward).

## Landed changes

All tied to the LOG.md Round-71 entry; measured commit `3627fac03f00ee904b45c9a9511b842356b1b46b`
(25 files, +3246/−4; the only − lines are SHONEN.md's four evidence-line updates — the
designated mutable surface, marks unchanged; SCORECARD diff is append-only, zero content
deletions; none of the six frozen bytes in the diff):

- `tools/mori-workstate-win.py`, `tools/mori-events-context-win.py` (new tools),
  `corpus/knowledge/workstate-win-r71.md` (new entry), `corpus/knowledge/uptime-win-r70.md`
  (append-only correction block), `corpus/evidence/sources-r71/S584.html` (new pin),
  `corpus/SOURCES.md` (S583+S584 rows appended INSIDE the Registry after S582; the only
  in-place cell change is S583's used-by, mutable per contract rule 2, logged as mistake 6),
  `corpus/QUALITY.md` (criterion 162), `corpus/lessons/round-71.md` (new lesson),
  `SCORECARD.md` (r71 section + two capability rows), `LOG.md` (r71 entry), `SHONEN.md`
  (evidence lines), and 14 receipts under `.ufo/waves/round-71/evidence/`.

## Before → after measurements

- **C1 (calibration)** — before: `git cat-file -e 015787e6:.ufo/waves/round-71/evidence/s582-pointers-erratum-r71.txt`
  → rc 128; `git show 015787e6:corpus/SOURCES.md | grep -c "supersedes S582"` → 0;
  `git show 015787e6:corpus/QUALITY.md | grep -c "^162\."` → 0; on the pin,
  `sed -n '833p' corpus/evidence/sources-r70/S582.html | grep -c "The number of milliseconds."`
  → 0 (the recorded pointer carries no quote). After (at `3627fac0`): erratum receipt exists;
  `grep -c "supersedes S582" corpus/SOURCES.md` → 1; `grep -c "^162\." corpus/QUALITY.md` → 1;
  the able-to-fail pair on the pin: recorded :833 → 0 vs corrected :834 → 1 (and :841/:842 → 1,
  recorded :845 → 0). Verdict: verified met.
- **C2 (depth)** — before: `git cat-file -e 015787e6:tools/mori-workstate-win.py` → rc 128;
  the S584 URL unseen at entering (grep 0). After: `python tools/mori-workstate-win.py
  --selftest` → `WORKSTATE_WIN_SELFTEST: PASS (10 cases)` rc 0 x3; `python
  tools/mori-workstate-win.py` → `WORKSTATE_WIN: AVAILABLE surfaces=1 ok=1` rc 0 x3
  (deltas −7/−12/−11 ms at biased_ms≈493.6e9 — the declared read model's predicted skew shape
  on a never-slept boot, same boot window as the r70 read); `grep -c "^| S584" corpus/SOURCES.md`
  → 1. Verdict: verified met.
- **C3 (operability)** — before: `git cat-file -e 015787e6:tools/mori-events-context-win.py`
  → rc 128. After: `python tools/mori-events-context-win.py --selftest` →
  `EVENTS_CONTEXT_SELFTEST: PASS (10 cases)` rc 0 x3; `python
  tools/mori-events-context-win.py` → `EVENTS_CONTEXT_WIN: PAIRED events_ok=1 uptime_ok=1`
  rc 0 x3 with `matched=209 window=200` bound to `uptime_ms≈494e9 count=biased
  boot_identity=absent`; `grep -c "boot_binding=none" evidence/events-context-live-r71.txt` → 3.
  Verdict: verified met.

## Sources & frontier

SOURCES rows 355 → 357 (`grep -c "^| S" corpus/SOURCES.md`: 355 at entering, 357 at
`3627fac0`; badNF=0). Two rows opened this round, both INSIDE the Registry after S582:
- **S583** (supersedes S582 — the GetTickCount64 page re-opened 2026-11-01, byte-identical to
  its pin): the correction row; quotes re-verified line-by-line in the erratum receipt.
- **S584** (QueryUnbiasedInterruptTime, opened 2026-11-01T22:03:48Z): definition/units
  (`:817`), signature (`:819-820`), failed-call signature (`:826-827`), zero-at-boot (`:828`),
  working-state semantics (`:830`), debug alert (`:833`), Precise variant unopened (`:876`);
  copy `corpus/evidence/sources-r71/S584.html` sha256 `d0bcbba9…` (54774 bytes); QUALITY 155
  sweep INTO the receipt before the fetch, with the interpretation receipted (API-name keyword
  = 1 because it hits S582's own quote text; the page-identifying URL-slug sweep = 0).
Census: validator rc 0 at round start (`evidence/census-start-r71.txt`) → rc 0 at round end
(`evidence/census-end-r71.txt`, `mori ok`; W04 duplicate-URL warnings are the tolerated
pre-existing class, now 32 rows including S583's legitimate re-use of the S582 URL). The first
end attempt rc 1 (E11: the S583 used-by cell carried a parenthetical that broke the validator's
path parsing) is disclosed in `evidence/census-end-first-attempt-r71.txt` — fixed in place per
contract rule 2, mined as lesson mistake 6. Mistake-mining: six mistakes with class, evidence
pointer, captured-by and fix (`corpus/lessons/round-71.md`): the from-memory fixture unit
arithmetic (wrong twice, plus a stale expected literal — the grammar arm caught all three);
a rc-masking pipe on battery output; the `python -I` posture change that exposed the
PYTHONUTF8 dependency; a receipt header claiming a verbatim capture it did not hold (rewritten
as a NOT-CAPTURED disclosure per QUALITY 160); the duplicate sweep read without its
page-identifying form; the used-by prose-in-parsed-list cell (E11).

## Trend verdicts

- **expansion: improved** — SOURCES 355→357 (both rows opened, pinned and mined this round);
  two capability acquisitions demonstrated running and entered the repertoire table in the
  same round (working-state read; boot-window-paired events receipt); the working-state
  surface the r70 entry recorded as "unopened" is now open with its own entry (K1–K6) and
  probe.
- **quality: improved** — three claims with falsifiable before→after data and counting
  commands; the D1/D2 carry-ins discharged as new entries with the able-to-fail demonstration
  against the drifted pointers themselves; QUALITY 162 adds the located-line rule; the
  standing battery green on unchanged bytes; six defects caught and mined, four of them by
  the round's own gates (selftest grammar arm, the unpiped rc read, the read-back rule, the
  round-end census).
- **discernment: improved** — the C2 boundary applied against the tempting readings (the
  delta printed as a signed derived count, never smoothed into an episode story; no power
  diagnosis, tsukuroi stays refused); C3 prints its own non-boot-scoping limit on every
  receipt; eight fresh-start rule-outs with reasons including declining the one-off
  recurrence pair this round could have run; the L0 lines re-verified open and routed around,
  never treated as answered.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — QUALITY 162 (the located-line pin-verification rule, added round 71, able-to-fail against the drifted S582 pointers) beside the standing QUALITY 148-151/154/161 pointers; verifier: the round-71 closure (non-author).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round71 (C1 the located-line erratum with the byte-identical re-open; C2 the working-state read sourced S584, live rc 0 x3; C3 the boot-window-paired events receipt, PAIRED rc 0 x3, matched=209 with the boot window on the line); receipts `.ufo/waves/round-71/evidence/`; verifier: the round-71 closure (non-author).
- [~] Instructions executable by an agent without oral context — `python tools/mori-workstate-win.py --selftest` (10/10 x3), `python tools/mori-events-context-win.py --selftest` (10/10 x3), standing battery green (register 12/12, settlement 10/10, vote-bind 16/16, pin-check 125/125, adjudicate 5/5, recheck 10/10, ua-variance 14/14, uptime-win 8/8) at `.ufo/waves/round-71/evidence/selftests-battery-r71.txt` (interpreter posture plain `python`, with the `-I`/PYTHONUTF8 finding disclosed in-receipt); verifier: the round-71 closure (non-author).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `corpus/knowledge/workstate-win-r71.md` Limits+Boundaries (counts and shapes only; no sleep/hibernation episode attribution, no power-state diagnosis: tsukuroi/operator; Precise variant unopened); `corpus/knowledge/uptime-win-r70.md` r71 correction block (append-only, S583-superseded pointers named old→new); PROVINCE.md byte-frozen and untouched; verifier: the round-71 closure (non-author).

Assimilation: considerthese re-mined (newest-named 2026-10-26.md; no newer file exists —
receipt `.ufo/waves/round-71/evidence/l0-considerthese-r71.txt`); the 2026-10-26 suggestion 1
remains the one still-unimplemented proposal behind the operator's open round-65 instrument
ruling; nothing adopted. Assimilation: none — shokuknow unreachable.
