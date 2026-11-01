# mado — round 63 (2026-11-01, hyaku run 12)

Base `cb442f663ca616c0825ed10beccece26bf920b35` (the r62 verifier
spot-check). Lane tip at report time `ce7f7673482c58dcdfc9130812e6cd7e3d5f8e39`
(branch `master`, pushed local==remote via `git ls-remote origin
refs/heads/master`). L1-only round again — the MISSION ≥8-L2 dispatch floor
has no surface on this host (disclosed since r57; L0 open, routed around,
never treated as answered). Security boundary held: no r56-era credential
material was opened, diffed, or surfaced; the round touched only the lane
files named below.

## Work performed

- **C1 calibration — the r62 carry-in corrections** (the closure's six
  routed number-shape drifts, all M62-1 class, in the round's own report
  records), addressed FIRST as ONE append-only correction block with
  re-derivation commands: `## Corrections (round 63)` in
  `corpus/lessons/round-62.md` (six items: (1) total-range mislabel —
  "34 files +1806/−1" superseded by 35 files +1830/−1 at the receipts tip
  `4c5435d8→4fe4544`, 34 files +1806/−1 only for `4c5435d8→bd06d021`, 35
  files +1860/−1 true final `4c5435d8→df415ef3`; (2) "wave receipts +441"
  → 21 files +359 receipts-only / 23 files +466 wave total at `4fe4544`,
  22 files +442 at `bd06d021`, 441 matches neither; (3) "18 receipt
  files" → 20 at `19407ef2`; (4) "Four commits" → 5 first-parent commits
  in `4c5435d8..df415ef3`; (5) census endpoint "161-170" → committed
  all-run range **160-170** (probe run 2 records `top_level` 160); (6)
  declaration S418-S422 vs landed S418-S423 noted), plus the in-file
  `## Errata (round 63)` on entry row H22 in
  `corpus/knowledge/windows-dwm-attributes-r62.md` (defect row
  untouched). Defect bytes preserved everywhere (ORIGINAL_PRESERVED:
  `git show cb442f66:corpus/lessons/round-62.md | wc -l` → 254 and
  `…/windows-dwm-attributes-r62.md | wc -l` → 72; `head -n <N> <file> |
  diff - <(git show cb442f66:<file>)` → empty for both). The fleet-root
  r62 report file is not lane-edited — this report restates the erratum.
  One drift in the round's own draft correction block ("255 lines at
  base" against base 254) was caught and fixed before landing.
- **C2 coverage (sourced) — the DisplayConfig (CCD) path/target plane**,
  the second documented refresh getter the r62 D04 route named: entry
  `corpus/knowledge/windows-displayconfig-r63.md` (4 host rows
  H25-H28 with re-derivation commands; 11 dated `[INF-docs]` rows
  K44-K54; 4 joins J25-J28; finding **D05**). Measured: the active-path
  query answers rc 0/rc 0 with 1 active path carrying
  `DISPLAYCONFIG_PATH_ACTIVE`; `targetInfo.refreshRate` = **64/1**; the
  mode table `[2, 1]` = TARGET/SOURCE at the path's indexes; the target
  mode's `activeSize`/`totalSize` read 1920x1080 while its
  `pixelRate`/`hSyncFreq`/`vSyncFreq` all read the **undocumented
  sentinel 0xFFFFFFFE** in every committed execution (probe x2, tool x2,
  crosscheck, raw-byte dump at the documented offsets — layout error
  distinguished from host fact), cause `[UNK]`, residue and flip
  condition named; the CCD 64/1 **agrees with r61's GDI 64 Hz** across
  two documented OS planes (J27) while the DWM timing side re-measured
  unchanged this round (`MADO_WINDWM: CLEAN (composition=on
  reasons=app+shell timing=unavailable(hr=0x88980090))` — D04 stands).
- **C3 operability (capability acquisition) —
  `tools/mado-win-displayconfig.py` (`VERSION r63-v1`)**, the durable
  read-only CCD observer: selftest **13/13** exit 0 after two disclosed
  red runs (M63-1: the first on-disk write lost the embedded script's
  two-line tail; the tokenizer reported it 190 lines away as an "invalid
  character" in an ordinary docstring; the odd triple-quote count was the
  diagnosis. M63-2: the M62-3 class's fourth recurrence — a static count
  assertion `intptr.zero == 2` written against a remembered comment
  shape; actual sites 1; fixed to the implementation with its site
  list); live `MADO_WINDISPLAYCONFIG: CLEAN (paths=1 refresh=64/1
  vsync=unavailable(0xfffffffe))` exit 0 twice, **outputs byte-identical
  by `cmp`** (the CCD topology moves only on a display change — a named,
  different churn class than the r62 census); `--from-file` re-derives
  from the committed snapshot rc=0; malformed snapshot →
  `MADO_WINDISPLAYCONFIG: ERROR (stage=parse …)` rc=2, raw bytes never
  echoed; crosscheck **5/5** stable fields AGREE against the
  independently executed probe (+ verdict structure); no Set*/Change*
  verb exists in the tool and the documented name getter
  (`DisplayConfigGetDeviceInfo`) is deliberately not called; tool ledger
  population 102 → 103. Capability row entered the SCORECARD table the
  same round.
- **Landing defects caught and repaired in-round (disclosed)**: (a) the
  used-by counter's setup gate fired red at the landing `c9a70974` —
  S430's teaches cell carried two unescaped pipes (13 cells, not 11);
  the cell was re-keyed on the row id, repaired at `cdacf215`, green
  `TARGET_MET entries=78 rows=371` (red-green in
  `landing-counters-r63.txt`, lesson Addendum, LOG + SCORECARD
  amendments); (b) the landing commit named the receipts directory and
  the plumbing helper landed none of its 24 files — caught by the
  prescribed post-landing `ls-tree` check and re-landed by explicit path
  at `49b053e8` (lesson Addendum 2; the commit-side twin of M63-1).

## Landed changes

Five first-parent commits, all through the plumbing helper and pushed
(`git rev-list --first-parent --count cb442f66..ce7f7673` → 5; the same
command is in the correction block for r62's "Four commits"):

| commit | content |
|---|---|
| `c9a70974` | the landing: entry (105 L), tool (758 L), SOURCES +11 rows + search log, README index row + frontier bullet, PROVINCE refinement + tool row, SKILL round-63 section, r62-lesson Corrections block + r62-entry Errata block, round-63 lesson (234 L), SCORECARD round-63 section + Corrections, LOG round-63 entries, ledger row, claims declaration |
| `cdacf215` | used-by repair: S430's teaches cell re-keyed on the row id (two unescaped pipes → slashes; proposition text otherwise untouched) |
| `f0c2308b` | receipts: landing-counters (red/green named sections), census-after, lesson Addendum + LOG + SCORECARD amendments disclosing the used-by red-green |
| `49b053e8` | receipts re-landing: all 24 receipt files by explicit path (the helper had landed none of the directory at `c9a70974`) |
| `ce7f7673` | record amendments: lesson Addendum 2 + LOG bullet disclosing the receipts-directory drop |

True final range `cb442f66→ce7f7673`: **39 files, +2248/−0**
(`git diff-tree -r --numstat cb442f66 ce7f7673 | awk '{a+=$1; d+=$2; n++}
END {print n" files "a" added "d" deleted"}'`); the landing's own range
`cb442f66→c9a70974` = 13 files +1556/−0; the wave dir holds 27 files
+680/−0 across the range (`-- .ufo/waves/round-63`); 25 files under
`.ufo/waves/round-63/receipts/` at the final tip (`git ls-tree --name-only
HEAD:.ufo/waves/round-63/receipts | wc -l`).

## Before → after measurements

- **C1 (calibration)**: `grep -c '^## Corrections (round 63)'
  corpus/lessons/round-62.md` → **0** at base `cb442f66`, **1** at
  `ce7f7673`; `grep -c '^## Errata (round 63)'
  corpus/knowledge/windows-dwm-attributes-r62.md` → **0 → 1**;
  ORIGINAL_PRESERVED both files (commands above). Measured at
  `ce7f7673`.
- **C2 (coverage, sourced)**: `ls corpus/knowledge/*.md | wc -l` → **77
  → 78**; `grep -cE '^\| `knowledge/[^`]+\.md`' corpus/README.md` → **77
  → 78**; `grep -cE '^[[:space:]]*\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  corpus/SOURCES.md` → **360 → 371**; entry rows
  `grep -cE '^\| [HJK][0-9]{2} '
  corpus/knowledge/windows-displayconfig-r63.md` → **19** (4 H + 11 K +
  4 J; D05 is a Findings bullet); navigation counter (SCORECARD §
  Counting command, fleet round 1, `python` for `python3`) at
  `cdacf215`/`ce7f7673` → `indexed=78/78 missing=0 dangling=0
  duplicates=0 coverage=10.0000/10`, exit 0 (receipt
  `landing-counters-r63.txt`). Measured at `ce7f7673`.
- **C3 (operability)**: `git ls-tree cb442f66 --name-only tools/ |
  grep -c win-displayconfig` → **0**; `python
  tools/mado-win-displayconfig.py --selftest` →
  `MADO_WINDISPLAYCONFIG_SELFTEST: 13/13 assertions passed`, exit 0
  (receipt `windisplayconfig-selftest.txt`; red runs' stderr committed);
  live x2 byte-identical rc=0 (receipts `windisplayconfig-live-run1/2.txt`);
  `--from-file` rc=0; error path rc=2; crosscheck 5/5;
  `python quality/check-tool-ledger.py --repo . --rev <rev>` →
  `population=102 … ` at base → `population=103 ledger_rows=103
  uncovered=0 … verdict=TARGET_MET` at `cdacf215`/`ce7f7673`. Measured
  at `ce7f7673`.

## Sources & frontier

- SOURCES rows: **360 → 371** (counting command above): rows
  **S424-S434** added, tier A, `mined`, opened 2026-11-01 in full via
  fetch BEFORE any row was written (the M58-2 discipline; the lesson's
  Gate records URL, access date, ms.date/git_commit/updated_at, and a
  ≤25-word verbatim quote per row). One bounded sweep, search log §
  Round 63 appended to `corpus/SOURCES.md`: 11 identified / 11 screened
  / 11 included / 0 excluded; one locator event before any row or code
  was written (the remembered DISPLAYCONFIG_MODE_INFO_TYPE order
  overruled by the opened page: SOURCE=1, TARGET=2 — mined M63-3); no
  404 event; the outputTechnology/rotation/scaling/scanLineOrdering enum
  pages deliberately not opened (the tool emits integers; stated in the
  entry's limits). C2 rests on S424-S434.
- Census before→after: start exit 0 (`mado ok`, 36 W04 + 1 W01 — the
  r57-r62 warning set unchanged; 360 rows), tee'd to
  `.ufo/waves/round-63/receipts/census-start-r63.txt`; end exit 0 (`mado
  ok`, warning set byte-identical by sort-diff, 371 rows), receipt
  `.ufo/waves/round-63/census-after-r63.txt`. No new W04 (none of the
  eleven URLs was previously held).
- Mistakes mined: M63-1..M63-3 in `corpus/lessons/round-63.md` §
  Mistakes (class · evidence pointer · captured-by · fix each) plus two
  in-round landing defects caught by the prescribed checks (lesson
  Addendum, Addendum 2; the class rule applied to the round's own
  records — including one drift in the round's own draft correction
  block, fixed pre-landing).
- Considerthese: all nine files re-screened 2026-11-01 (directory
  listing unchanged since the r58 mining; mtimes unchanged) — no
  adoptable proposal. **Assimilation: none — shokuknow unreachable.**

## Trend verdicts

- **expansion — improved**: one new sourced plane on uncovered ground
  (the CCD path/target surface): 11 new mined tier-A rows, 1 new indexed
  entry whose `source:` cites them (navigation 78/78 exit 0), 1 new
  capability row; knowledge files 77 → 78, registry 360 → 371, all
  counted above.
- **quality — improved**: a durable read-only CCD observer with red/
  green-disclosed assertions, byte-identical live receipts, from-file
  determinism, a 5/5 crosscheck and a raw-byte finding receipt; the r62
  carry-in corrections landed append-only with preserved defect bytes;
  the r61/r62 tools' harm-watch surfaces re-measured unchanged (55/55,
  63/63, verify sha `050efc720599345a`, D04 verdict unchanged).
- **discernment — improved**: three red runs and two landing defects
  disclosed rather than smoothed (the correction block's own "255 vs
  254" drift fixed pre-landing; the used-by setup-gate red repaired and
  receipted; the receipts-directory drop caught by the prescribed
  ls-tree check and re-landed); D05 recorded as `[UNK]` with residue and
  flip conditions instead of a guessed cause; the sentinel prints as
  `vsync=unavailable(0xfffffffe)`, never a measurement.

No axis harmed: census exit 0 both ends with the identical warning set;
navigation 78/78; used-by `TARGET_MET` (missing=0 extra=0) at
`cdacf215`/`ce7f7673`; ledger 103/103 `TARGET_MET`; `tools/mado-verify.sh`
bytes untouched (sha256 prefix re-measured `050efc720599345a`); both
fail-closed checkers' selftests green at current bytes (55/55, 63/63 —
receipt `harmwatch-selftests-r63.txt`); the two corrected r62 records are
pure appends (ORIGINAL_PRESERVED verified); no existing knowledge entry
body or registry proposition cell changed. Verdicts are the closure's to
rule.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — evidence pointer: `corpus/knowledge/`
  (78 entries incl. `windows-displayconfig-r63.md` with 19 table rows +
  a finding, sources S424-S434 dated and quoted); still lane-asserted, no
  named non-author verifier to date.
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  evidence pointer: LOG.md round-63 entries (the CCD plane observed
  end-to-end on the live host this round: sweep → entry → tool →
  counters); historical boxes unchanged, still no outside-lane verifier.
- [~] Instructions executable by an agent without oral context —
  evidence pointer: the entry's § Verify block re-derives every claim
  from committed bytes (`bash`/`python` commands, no oral context);
  outside-lane executor independence still not established.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence
  pointer: PROVINCE round-63 refinement appended; the Windows desktop
  plane stays read-only observation, kagi keeps secret-shaped values, no
  Shell or capture surface entered.

Routed-around L0 questions (never treated as answered): omarchy freshness
disposal (r57), gate-selftest host gap (r58), calibration resolved-active
re-derivability (r59), screen-capture scope (r60), the L2 dispatch floor
(standing). The four SHONEN boxes remain `[~]` lane-asserted; the closure
judge may commission the non-author review the operator note names.
