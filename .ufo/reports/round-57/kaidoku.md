# kaidoku — round 57 report (the r56-closure carry-in round)

Lane `shokunin-reverse-engineering` (kaidoku), branch `main`, L1-inline on the
Windows host, 2026-11-01. Base `63413677ec0531e38722b8dbfb0b89a0bc113d04` (= origin/main
at round start; the round-56 verifier spot-check commit). Tip at filing:
`67ec2c382478d2f16e1a38f7d8e84b79cc1f2d4b`. No wave (no dispatch surface on this
host; the kaidoku round-53 L0 question stays open and unanswered — routed
around, never treated as answered; ≥8-L2-seat dispatch remains unmet for the
same measured reason recorded since r53).

## Work performed

Declared claims (2, causally separable, distinct owned axes — coverage/depth/calibration
sit tied at 10.0 in `SCORECARD.md`, so each is a lowest axis): **R57-C1 —
calibration**: the eight r56-closure routed defects D1–D8 close with committed,
append-only artifacts; **R57-C2 — depth, capability acquisition**:
`tools/round-57/record-receipt-audit.py`, the named-path completeness gate
(the M56-4 rule as routed defect D4's fix clause extends it).

- **Fresh-start compliance executed first:** the §7 list (r50/r51/r52, all
  `rejected-honest-stop`) re-read and spot-checked before declaring. Spot-check
  finding: all three died on the AVM LE-SquashFS Frontier→Core target and
  wave-band/handoff defects (r50's frozen counter measured 2-of-4 carriers,
  exit 1, honest stop; r51's 36-seat single wave below the 64–128 band with no
  falsify wave; r52 never completed a freeze or data run) — none on offline
  committed-byte work, the class r53–r56 admitted on. Ruled out, with reasons
  (full list in `plans/round-57-claims.md` and the LOG declaration entry): the
  AVM LE-SquashFS re-freeze (host-absent surfaces; three rounds died on it); a
  census-safe W04 supersedes set (the W04 check precedes any status test and
  SOURCES.md is append-only — 19 warnings stay named debt); the r53-sized-out
  registry-drift census (over-declaration shape); any wave dispatch (no
  surface). §9 sizing: both claims close artifacts/instruments that do not
  exist at the base — a do-nothing control cannot reach them; before-arm
  receipts at the base prove the open state.
- **D1/D2 closed** — the erratum of record appended to
  `corpus/lessons/round-56.md` as `## Corrections (round 57)`, correction 1:
  the c1-after V-1/V-5 lines (probes printed 0, annotations concluded
  ">=1 -> closed") and the report's "1 / 1 / 0 at `22f77c34…` / 1" after-arm
  quote are superseded; the after-arm restated on markers that occur in the
  committed wording (`planted empty directory trees mirroring the pathspec`,
  `canonical-parameter clarification`, `supersedes M55-2` — each greps 1 at
  `31c2bd50`), re-run with observed outputs in
  `.ufo/waves/round-57/l1/scores/c1-after.txt`.
- **D3 closed** — the same erratum, correction 2: the r55 lesson's correction-1
  sentence "the four intended paths … exist at no path in that commit" is
  overbroad; object facts re-verified this round at `29a7477b` — `LOG.md`
  EXISTS there (rc=0, blob `70d3f2af8ba542f2550b2f0f4ee48267ee90cf5f`,
  byte-identical to parent `79421b75`'s, no round-55 content — the append never
  landed); only the THREE new-file paths are absent (rc=128).
- **D4 closed** — the third worktree-only receipt
  `.ufo/waves/round-56/l1/records/receipt-audit-green-r56.txt` landed at
  `e304cb0d` (worktree bytes unchanged; the r56 closure had verified them
  against its own green run); the r56 record section's 13-receipt list resolves
  13/13 from that commit on; M56-4's "fully resolvable" sentence, falsified at
  the r56 tip, is true from `e304cb0d` on.
- **D5 closed** — erratum correction 3: the report's "LOG insertions only:
  45/0 across the round" is base→close `047bd98e`; at the cited tip
  `b9434858` it is 49/0 (both `git diff --numstat` re-run and pasted; direction
  conservative).
- **D6 closed** — the r56 LOG freeze entry's "The discarded sha is disclosed
  here" clause printed no sha; the disclosure is completed by the carry-in
  landing LOG entry: the discarded first freeze attempt is
  `db3e94cdd155aea8c3cff2b0ced96bd16ceed1a9` (parent `31c2bd50`; located in the
  `main` reflog; not an ancestor of main, `git merge-base --is-ancestor` rc=1;
  absent from origin/main at round start; its container carries the bare-name
  T3 defect M56-2 describes). Never cited as evidence of round work.
- **D7 closed** — the R29 gate re-run at `047bd98e` and receipted:
  `.ufo/waves/round-57/l1/scores/gate-at-r56-close-tip.txt` — exit 0, audited
  31, clean 11, disclosures 31/31 exact, missing [], stray [], round-55/56
  CLEAN — matching the r56 report's transcription, which had been the only
  record of that run.
- **D8 closed** — the round-57 SCORECARD section's C1 row states the corrected
  item list ("r56 spot-check §7 items 1, 2, 3, 5 plus the D5-D8 notes") and
  names the r56 C1 row's "items 1-4" wording as superseded in that cell; the
  r56 row stays as filed.
- **R57-C2 landed** — the new instrument `tools/round-57/record-receipt-audit.py`
  (pin `3a5fff9adcb472e2cfb8ba42225520f49539b0493c2c144c9684fc296add8151`,
  frozen in the round-57 container): every backtick-quoted `.ufo/waves/round-N/`
  path a record section names must resolve at the named revision — section-
  sliced committed bytes (`git show REV:RECORD`, never the worktree), exact
  match against one `git ls-tree -r --name-only REV` listing; verdict map 0/1/2;
  zero named paths unevaluable, never vacuously clean (the QUALITY #66
  boundary); selftest 9 in-memory cases 0 failures; red demo on the D4 defect
  itself at the base (exit 1, named 14, missing 1); green demo at the carry-in
  landing (exit 0, named 14, missing 0); SKILL instrument-registry row;
  SCORECARD capability row (first-working round 57).
- **Freeze discipline:** declaration `5d5bcb92` (plans + instrument, committed
  before the claims file); operative freeze `bc261681` (first commit adding
  `.ufo/waves/round-57/claims.json`; 10 landed = 10 intended, `git diff-tree`
  re-derived; the container pins all three instruments, each named in
  frozen-atom values); R29 pre-flight at the freeze: round-57 CLEAN with all
  three instruments audited, disclosures 31/32 exact + missing [round-57]
  (the row lands with the record — the r55/r56 pattern, disclosed in the
  receipt; exit 1 expected pre-row, honestly printed); landing at the record
  commit `06caea12`: exit 0, audited 32, clean 12, disclosures 32/32 exact.
- **M57-3 ordering slip, self-caught and disclosed:** the declaration and
  carry-in LOG entries were appended in one batch before either commit
  existed, so the carry-in entry landed inside the declaration commit
  `5d5bcb92` and the carry-in commit `e304cb0d` carries the files its entry
  names but no LOG line of its own. Disclosed in the freeze LOG entry (not
  waived; LOG deletions 0); mined as M57-3. One worktree-only incident
  (a truncated heredoc append to the SCORECARD worktree copy, caught by the
  tail check, restored byte-exact from the committed blob
  `git show e4112db6:SCORECARD.md` before re-appending — history untouched).
- **Frontier step (§2b):** SOURCES curated — S257 opened and admitted this
  round (163 → 164 rows); census before→after receipted; three mistakes mined
  into `corpus/lessons/round-57.md` (M57-1 the D1/D2 receipt-annotation class,
  M57-2 the D4 single-naming-surface class, M57-3 self-caught); the sourced
  claim is R57-C2 (S257 grounds the gate's listing semantics — the R56
  reject-1 boundary applied consistently: the r56 gate anchored cat-file
  because its verdict was existence-at-revision; this gate's verdict IS the
  ls-tree listing).

## Landed changes

| commit | contents | LOG.md |
|---|---|---|
| `5d5bcb92ac0476d0d2480e248eaaec3c5f030f07` | declaration: `plans/round-57-claims.md`, `tools/round-57/record-receipt-audit.py`, LOG declaration + carry-in entries (the entry-ordering slip, M57-3) | "round 57 … declared" + "carry-in landing" entries |
| `e304cb0dbfc4140de984e938be0cf794964b2759` | carry-in landing: the D4 receipt A, `corpus/lessons/round-56.md` `## Corrections (round 57)` M, the D7 gate receipt A | the entries the commit carried ahead of itself (disclosed, M57-3) |
| `bc261681ef89833693c039c80762aa31189bfbed` | freeze: `claims.json` (3 pinned instruments), FREEZE, census-start, c1-before, c2-before, selftests, red-demo-at-base, s257/ snapshot + digests, LOG freeze entry — 10 landed = 10 intended | "freeze recorded; before-arms measured; one ordering slip disclosed" |
| `e4112db6cfedc81a20f893da55fff33a62c15c2b` | landing: SKILL registry row M, SCORECARD capability row M, `records/record-audit-green-r56.txt` A, `scores/gate-preflight.json` A, LOG landing entry | "landing: R57-C2 measured …" |
| `06caea12321ca6c1f7ae8ba6ec5007d38894da56` | record: SCORECARD round-57 section M (claims table, atoms T1-T12, D8 correction, receipts list), `corpus/lessons/round-57.md` A (Gate + M57-1..M57-3 + freeze), SOURCES S257 M (163→164), ledger row round-57 M, LOG record entry | "record landing …" |
| `67ec2c382478d2f16e1a38f7d8e84b79cc1f2d4b` | close: census-end A, c1-after A (pins the record commit), c2-after A, `records/record-audit-r57-at-close.txt` A, `scores/gate-landing.json` A, LOG close entry + T11 phrasing correction | "close" |

No-harm at the tip: LOG base→tip 47 insertions / 0 deletions (every one of the
6 commits insertions-only); PROVINCE diff empty; the three owned-axes rows
byte-identical base→tip (per-row sha256 equal); the SKILL v6 marker block
digest identical base→tip; the round's full delta is exactly the 26 files
named above.

## Before → after measurements

- **R57-C1 (calibration):** before at the base `63413677` — all eight routed
  defects open, probes pasted with observed outputs in
  `.ufo/waves/round-57/l1/scores/c1-before.txt` (D1 both annotations 1, D2
  erratum 0, D3 overbroad sentence 1, D4 receipt-in-tree 0, D6 clause 1 with no
  sha printed anywhere, D7 no committed tip-run receipt, D8 "items 1-4" 1;
  D5 measured as 45/0-vs-49/0 unreconciled). After at the record commit
  `06caea12` (receipt `scores/c1-after.txt`, landed with the close — the rev
  field pins the commit it measured): all eight closed — erratum 1, corrected
  markers 1/1/1 with stale prose 0, overbroad-sentence erratum 1 + object
  facts re-pasted, receipt-in-tree 1 with the gate's green demo exit 0
  (14/14), the 49/0 numstat re-derived, the printed sha `db3e94cd…` present in
  the LOG of record, the D7 receipt in the tree (exit 0, 31/31), and the
  corrected item list 1 + correction-of-record sentence 1 in the record
  section. Counting commands: `git show <rev>:<file> | grep -c`,
  `git ls-tree -r --name-only <rev> | grep -c`, `git diff --numstat` — all
  pasted with outputs in the two receipts.
- **R57-C2 (depth, capability acquisition):** before at the base — instrument
  absent (`git cat-file -e` rc=128), 0 SKILL registry rows, 0 capability rows
  (`scores/c2-before.txt`). After at the landing `e4112db6` (receipt
  `scores/c2-after.txt`): selftest 9 cases 0 failures; red demo exit 1
  `NAMED_PATH_ABSENT` on the D4 defect itself at the base (named 14, missing
  1, `records/red-demo-at-base.txt`); green demo exit 0 at the carry-in
  landing `e304cb0d` (named 14, missing 0, `records/record-audit-green-r56.txt`);
  registry row 1, capability row 1. Headline command:
  `python -X utf8 -I -B tools/round-57/record-receipt-audit.py --selftest`
  and the two demo invocations pasted in the receipts. The extended M56-4
  discipline on this round's own record: at the record commit the audit exits
  1 with exactly the two close-landing receipts (`records/record-audit-r57-at-close.txt`,
  named 12, missing 2 — disclosed ordering); at the close tip the same
  command re-derives named 12, missing 0, exit 0 (verified this round; atom
  T11's phrasing corrected by an appended measured line in the LOG close
  entry).
- **R29 gate:** pre-flight at the freeze `bc261681` — round-57 CLEAN, all
  three instruments audited, disclosures 31/32 exact + missing [round-57]
  disclosed, exit 1 expected pre-row (`scores/gate-preflight.json`); landing
  at the record commit — exit 0, audited 32, clean 12, disclosures 32/32
  exact, round-55/56/57 all CLEAN (`scores/gate-landing.json`); plus D7's
  receipted run at `047bd98e` (exit 0, 31/31).

## Sources & frontier

SOURCES rows before→after: 163 → 164 (`grep -cE '^\|\s*S[0-9]{3,}\s*\|'
corpus/SOURCES.md` at base and tip; one insertion, S257). S257: git-ls-tree
documentation, https://git-scm.com/docs/git-ls-tree, fetched read-only with
curl 2026-11-01, snapshot bytes + sha256 committed at
`.ufo/waves/round-57/l1/s257/` (`2c298383476164238c6e25ba804412a335c405ab9540650bb603778e2f4f8b64`),
located quote 11 words under OPTIONS (`--name-only`), tier A docs, mined —
grounds R57-C2's listing semantics; used-by paths all resolve at the tip
(`plans/round-57-claims.md`, `tools/round-57/record-receipt-audit.py`,
`corpus/lessons/round-57.md`). Census: start exit 0 (19 standing W04, 163
rows, receipt `census-start.txt`); end exit 0 (19 standing W04, 164 rows,
receipt `census-end.txt` at the record commit; re-run at the filing tip with
the same exit 0); the literal `kaidoku`-name form exits 2 on this host
(expected `<fleet-root>/kaidoku-shokunin/`), disclosed since r53 — the
host-adapted explicit-dir form is the receipted one. W04 stays named debt.
Mistake mining: M57-1, M57-2, M57-3 in `corpus/lessons/round-57.md` `## Mistakes`
(class · evidence pointer · captured-by · fix, each). Assimilation:
`considerthese/` does not exist in this lane (measured at round start);
shokuknow unreachable — Assimilation: none — shokuknow unreachable.

## Trend verdicts

- **expansion: unchanged** — PROVINCE diff empty base→tip (no Frontier→Core
  move); zero new `corpus/knowledge/` entries; SOURCES 163→164 is the only
  registry growth and S257 grounds a listing discipline (tool documentation),
  not an REA surface.
- **quality: improved** — all eight routed defects closed with committed,
  append-only artifacts (the erratum content-checked; the missed receipt in
  the tree with the record resolving 13/13; the discarded sha printed with its
  non-ancestor status; the previously transcribed-only gate run now receipted
  exit 0 31/31); a second unguarded naming surface mechanized shut by the new
  gate, demonstrated red on the true defect and green on the repaired tree;
  the round's own freeze audited CLEAN by the R29 gate (32/32 exact at the
  record commit); the extended M56-4 discipline executed on the extending
  round's own record before filing. No admitted entry failed its re-check.
- **discernment: unchanged** — the round executed the last closure's routed
  list verbatim and self-routed three mistakes (M57-1..M57-3, one self-caught
  pre-filing), and its own gate reproduced the routed D4 defect from committed
  bytes before demonstrating the closure — real taste evidence — but the
  round also shipped an entry-to-commit ordering slip (M57-3) that needed
  post-hoc disclosure, consistent with the existing level rather than a
  demonstrated rise. Pending the outside spot-check.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: the instrument-registry v2 row added this round (`grep -c 'round-57/record-receipt-audit' SKILL.md` → 1 at `e4112db6`), the v6 marker block digest identical base→tip, SOURCES S257 with used-by paths resolving at the tip.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: the receipted repair+capability chain this round (D4's receipt landed at `e304cb0d`, the D4 defect reproduced by the round's own gate at the base and demonstrated closed at the landing; LOG entries through the close commit `67ec2c38`).
- [~] Instructions executable by an agent without oral context — evidence: the pasteable re-derivation commands in `scores/c1-before.txt`, `scores/c1-after.txt`, `scores/c2-after.txt` and the three records receipts (each command re-runs against committed bytes at the pinned revisions; the freeze/landing gate receipts re-run with one line each).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `git diff --stat 63413677 67ec2c38 -- PROVINCE.md` empty; nothing promoted; S257 recorded as tool documentation, not an REA surface.
