# mori round 68 — the per-response separation receipt (`tools/mori-ua-variance.py`, sourced S579) + the receipt-labeling discipline (the r67 routed erratum, QUALITY 160, per-block-labeled reproduction)

lane: mori-shokunin · branch master · entering `8440cf6c035a8f9af9cc8b3c95fc5584176c2d5c` (r67 verifier spotcheck tip) · landed `4fce1404e3f7bd08c1a564a5ded659a00e1eb384` (helper-printed, pushed origin, ahead=0; `8440cf6c..4fce1404` = 19 files, +1296/−2)

## Work performed

FRESH-START duty re-performed on the §7 rejections r59–r61 with own receipts
(`.ufo/waves/round-68/evidence/freshstart-spotchecks-r68.txt`): frozen r61
counter re-derived at the r61 data tip → `C2=unmet` rc 1 (the same verdict the
r61 closure and the r65/r66/r67 re-derivations reached); r59/r60 cited evidence
`git cat-file -e` PRESENT and both revisions ancestral of refs/heads/master
rc 0 each. Ruled out, and why: (1) the r59/r60 entry-claims instruments (their
met-flip counterexamples stand on frozen bytes — re-derived unmet again);
(2) scalar score moves (no closure states a new number); (3) old-Linux-host
live surfaces (absent here); (4) editing the frozen bytes (SKILL.md, the sweep,
the r65 adjudicator, PROVINCE.md, AGENTS.md, corpus/README.md — the SKILL:905
tally pin and the r65/r66/r67 receipts bind them; the r68 tool is new and
separate); (5) a third churn grammar for the bot-manager chrome (r67's ruling
stands — r68 receipts the variance instead, re-classing no row); (6)
re-declaring the admitted r64–r67 work; (7) adopting considerthese 2026-10-26
suggestion 1 (changes a tally-cited instrument's behavior — behind the
operator's open instrument-change ruling). Do-nothing controls:
`.ufo/waves/round-68/evidence/controls-r68.txt` — QUALITY `^160\.` = 0 rc 1,
`tools/mori-ua-variance.py` absent at entering rc 128, S579 row = 0 rc 1.

- **C1 (calibration 5): the receipt-labeling discipline** — the r67 closure's
  routed item 1. The r67 A/B receipt's heading ("live run at the FINAL bytes
  2026-11-01T10:30:24Z") sat above the reproduced run's block (its own header
  `run-start=2026-11-01T10:36:28Z` disproves its label), and the 10:30:25Z
  first post-fix run's raw output was quoted nowhere — swept: it appears only
  as CITED as-of values (`SCORECARD.md:3332`, `LOG.md:3575`). Discharged as
  the erratum + criterion + reproduction; evidence
  `.ufo/waves/round-68/evidence/abreceipt-labeling-erratum-r68.txt`,
  `.ufo/waves/round-68/evidence/s241-rerun-labeled-r68.txt`,
  `corpus/QUALITY.md` criterion 160.
- **C2 (depth 5, capability acquisition, SOURCED on S579): the per-response
  separation receipt** — `tools/mori-ua-variance.py` receipts what the r67
  receipt could only assert: two same-UA fetches of the same URL minutes apart
  cannot differ in page content, so differing line positions are per-response
  serving bytes and agreeing positions are stable chrome; stable lines are
  cross-counted against the pinning body WITHOUT deciding UA-conditional vs
  newer-build (QUALITY 159 untouched — no grammar taught, no row re-classed;
  classes stay the standing step's job); counts and shapes only, line values
  never emitted, capture bodies stay in scratch. This was the r67 SCORECARD's
  first planned item. Evidence
  `.ufo/waves/round-68/evidence/s241-uavariance-r68.txt`.
- Carry-in 2 routed around: the r65 L0 (SKILL:905 `python3` naming) stays open
  for the operator — no frozen byte edited (sha-verified identical:
  SKILL.md `01556f056cd7…`, sweep `eb5affa188b5…`, adjudicator `ed3cabd0b53f…`,
  PROVINCE `2af29312d287…`, AGENTS `f64e332c73e5…`, corpus/README
  `fbe94947b590…` at the landed tip; `git diff-tree` over the range for the
  frozen set is empty) and every command used `python`.
- Orphaned-evidence hygiene duty: both citation surfaces scanned (all filed
  fleet mori reports + the lane's own artifacts), 20 candidates triaged,
  NOTHING TO LAND — every mori-owned cited evidence file is committed at the
  tip and each absent name resolves to a documented disposition (deliberate
  redaction withholding r28; the documented r23 withdrawal with the
  falsification retained at lane commit `0d8f2d50`; fleet-repo-resident paths;
  sibling-lane files; old-host state; extraction truncations of committed
  names) — `.ufo/waves/round-68/evidence/orphan-scan-r68.txt`.
- No-harm battery green on unchanged bytes: register 12/12, settlement 10/10,
  vote-bind 16/16, pin-check 125/125, adjudicate 5/5, recheck 10/10, plus the
  new tool 6/6 — `.ufo/waves/round-68/evidence/selftests-battery-r68.txt`
  (loopback-transport condition carried; the intermittent loopback reset this
  round observed is itself receipted at
  `.ufo/waves/round-68/evidence/loopback-reset-r68.txt` and mined as mistake 3).

## Landed changes

One commit, `4fce1404e3f7bd08c1a564a5ded659a00e1eb384` (helper-printed;
`merge-base --is-ancestor` rc 0; `refs/heads/master` = `ls-remote origin
refs/heads/master` = `4fce1404…`, ahead=0). Every change is logged in
`LOG.md` Round 68: `tools/mori-ua-variance.py` (new); `corpus/QUALITY.md`
criterion 160 appended (158/159 counts unchanged, verified 1/1/1);
`corpus/SOURCES.md` S579 row (351 → 352, malformed=0, no duplicate ids);
`corpus/evidence/sources-r68/S579.html` pinned copy;
`corpus/lessons/round-68.md` (Gate + 5 mistakes + fresh start + carry-ins);
SCORECARD.md Round-68 section (claims table, capability row, planned);
SHONEN.md boxes 2–3 pointer extensions (still 4/4 `[~]`, no `[x]` — only a
non-author promotion review may write those); eleven receipts under
`.ufo/waves/round-68/evidence/`.

## Before → after measurements

- **C1** — counting commands + measured commit `4fce1404`:
  `git show 8440cf6c:corpus/QUALITY.md | grep -c "^160\."` → `0` rc 1
  (`controls-r68.txt`); after: `grep -c "^160\." corpus/QUALITY.md` → `1`.
  Reproduction label check (computed, in the receipt): block headings = 2,
  self-labeled blocks (`run-start=` on each block's own header) = 2,
  mismatches = 0; before, the r67 receipt's heading timestamp (10:30:24Z)
  disagreed with the block beneath it (`run-start=10:36:28Z`). Both fresh
  runs at the same final bytes print `S241 asset-churn as-of=2026-11-01T
  14:13:44Z` / `…14:23:12Z` rc 0 — the class reproduces at r68 moments.
- **C2** — counting commands + measured commit `4fce1404`:
  `git cat-file -e 8440cf6c:tools/mori-ua-variance.py` → rc 128 (absent);
  after: the tool is committed and `python tools/mori-ua-variance.py
  --selftest` → `MORI_UA_VARIANCE_SELFTEST: PASS (6 cases)` rc 0, three
  consecutive runs at the final bytes. Live A/A on S241: two instrument-UA
  fetches 21 minutes apart (13:53:46Z, 14:14:54Z; 54343 bytes each, shas
  `4e258124…`/`707eec3f…`, same-bytes=false), compare against the committed
  r42 pin (sha `1168b2a6…`): `per-response=4 stable=1497
  stable-not-in-pin=2 stable-in-pin=1495 lines-a=1499 lines-b=1499
  lines-pin=1499` rc 0 — before, no instrument existed and the instrument-UA
  body was unadjudicated (the r67 receipt asserted "one serving-injection
  line" from a single pin-vs-instrument diff; the A/A separation shows TWO
  per-response positions, 218 and 1498 — disclosed as a correction to that
  description in the receipt; the r67 verdicts did not rest on the line
  count).

## Sources & frontier

SOURCES rows 351 → 352, counted by `grep -c "^| S" corpus/SOURCES.md` (before
351 at the entering tip, after 352 at `4fce1404`). One row opened this round:
S579 (AWS WAF Developer Guide, "Token use in AWS WAF intelligent threat
mitigation" — a mitigation token is a per-client-session artifact the client
carries on every request), fetched with `curl -sS -m 60 -L`, pinned
byte-identical `corpus/evidence/sources-r68/S579.html` sha256
`41b601f1da6ad11b5cfb167c5e64c780c15b83b7609caac4e9d8fefeafda7a9e` (14127
bytes), quotes at `S579.html:49` + `:50` (14 + 14 words), heading `:48`,
status `mined`, used-by `corpus/lessons/round-68.md`; C2 rests on it.
Duplicate sweeps receipted (`.ufo/waves/round-68/evidence/source-sweeps-r68.txt`):
`grep -ci "waf"` = 0, `"docs.aws"` = 0, `"amazonaws"` = 0, `"bot management"`
= 0, `"bot-manager"` = 0 pre-row; the single `"fingerprint"` hit is S578's own
teaches cell. Honest order note: two scratch SELECTION fetches preceded the
sweeps; the sweeps predate the row and the claim. Census (validator): start
receipt rc 0 (tolerated W04 class) → end receipt rc 0
(`census-start-r68.txt`/`census-end-r68.txt`); the FIRST end run failed rc 1
(`mori E12 S579 row outside Registry section` — the row had been appended at
EOF; moved into the Registry after S578, re-validated clean; mined as lesson
mistake 5). Mistakes mined: 5, in `corpus/lessons/round-68.md`
(`## Mistakes`), each with class · evidence pointer · captured-by · fix.

## Trend verdicts

- **expansion: improved** — a new capability enters the repertoire table
  demonstrated running (per-response separation receipt, first-working 68);
  one tier-A source opened, pinned, mined (SOURCES 351 → 352, re-counted);
  PROVINCE unchanged (no surface claimed).
- **quality: improved** — both claims measured met with able-to-fail evidence
  (C1's rule fails against the r67 receipt's own disagreeing timestamps; C2's
  selftest carries a redaction arm and two able-to-fail rc arms); the standing
  battery is green on unchanged bytes (no operational axis traded); the erratum
  corrects the r67 record without rewriting it (append-only).
- **discernment: improved** — five mistakes mined with class · evidence ·
  captured-by · fix, including the validator-caught E12 and the discarded
  CRLF-contaminated scan pass; the not-captured 10:30:25Z bytes are disclosed
  as not-captured rather than approximated; the third-grammar temptation stays
  rejected (the variance is receipted, not grammar-ized); the considerthese
  instrument-change proposal stays behind the operator's open ruling.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — unchanged this round (frozen; sha-verified `01556f056cd7…`); pointers as filed
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round68 (C1 the receipt-labeling discipline with the fresh per-block-labeled S241 reproduction, mismatch=0; C2 the per-response separation capability with the live S241 A/A: `per-response=4 stable=1497 stable-not-in-pin=2`, positions 218 and 1498, sourced S579); `.ufo/waves/round-68/evidence/` receipts
- [~] Instructions executable by an agent without oral context — `python tools/mori-ua-variance.py --selftest` (6/6 x3, `.ufo/waves/round-68/evidence/s241-uavariance-r68.txt`) joins the standing battery, all green on unchanged bytes (`.ufo/waves/round-68/evidence/selftests-battery-r68.txt`; interpreter `python` — the r65 L0 `python3` Store-stub note stands open; loopback-transport condition carried and now itself receipted, `.ufo/waves/round-68/evidence/loopback-reset-r68.txt`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — frozen and sha-verified `2af29312d287…`; the round touched only lane files plus read-only vendor fetches (learn.microsoft.com, docs.aws.amazon.com); the kake/kotoba/kama files named by the orphan scan were reported to their owners, not absorbed (`.ufo/waves/round-68/evidence/orphan-scan-r68.txt`)

Wave: none — no dispatch surface on this host (carried disclosure; the mori
round-62 and round-65 L0 lines stand open, routed around, never treated as
answered). Round 68 ran L1-only over committed bytes and this host's network;
no wave-based evidence is claimed. Planned (round 69): a longer-gap A/A
(hours) to test whether the two per-response positions rotate on one clock or
different TTLs; a standing cross-check between the probe's stable-not-in-pin
and the re-check's `asset-churn` at the next vendor redeploy (deciding
nothing).

Assimilation: considerthese mined (2026-10-19…2026-10-26, all eight files; no
newer file exists — checked this round); suggestion 1 (split pin-check
mismatches) remains the one still-unimplemented proposal and stays behind the
operator's open instrument-change ruling; suggestion 3 was executed again (the
frozen r61 counter re-derived in the fresh-start receipt). Assimilation: none
— shokuknow unreachable.
