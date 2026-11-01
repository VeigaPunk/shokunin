# tameshi round 64 — report (L1 `TameshiR64`, 2026-11-01, win32 host)

Base `d0baf616bb8a9fc1be6394e370e0f30a952470af` (= origin/master, the r63
verifier spot-check landing). Lane head at close:
`c7d28b19e5f984d55c972e9423cd0c75a130f596` (= `refs/heads/master` =
`origin/master`, pushed). Work commits: `33cb4b0d627f1b06067bf002c256bc6da1eed962`
(R64-C1 declared + ledger + lesson + LOG + rehearsal receipts),
`b31e81456b9860a1bf5dddfa678cfd2df59149d9` (R64-C2: tool + SOURCES +
fetch receipts), `1763db52b42c7e0776a2d03b39dbf0db5d6adc59` (rekey
`r64-batch-1`), `be76552d4bf933993247d09e9e3f38ba80649fc9` (measured rows +
capability row + receipts), `6876d746…` + `c7d28b19…` (the post-landing
tip-confirmation receipt — evidence-file-only commits; every monitored and
protected file is byte-identical from `1763db52` to the tip).

CLOSURE-PREP: base `d0baf616` → head `c7d28b19` pushed=yes; claims=2
(R64-C1 calibration — the r63 closure's carry-in observation 1, sourced on
new row S295; R64-C2 operability + capability — considerthese proposal 1's
cited-receipt-exists half, ground re-opened on held S289), both self-verdict
"verifies (measured)"; no-harm guard at the pushed tip:
`COLDREAD_PRECHECK floor=d0baf616bb8a floor_credited=64 cand=c7d28b19e5f9
cand_credited=64 lost=0 ok` and `floor=8b0042bde0ca floor_credited=46
cand_credited=64 lost=0 ok` (64/64; probe sampled=20 mismatches=0
everywhere; committed receipt
`.ufo/evidence/round-64/win-host/tip-confirmation.txt` — guard at
`be76552d` and `6876d746`, additivity C→D, the self-sweep, all
re-runnable);
receipts `.ufo/evidence/round-64/win-host/`; lesson
`corpus/lessons/round-64.md` (4 mistakes mined, 3 self-caught pre-landing;
Gate states its reject sample explicitly per the r63 carry-in); SOURCES
154 → 155 (S295; the S289 used-by re-open logged old → new); census exit 0
start and end; ledger 693 → 706 with `rekey_batch` on all 62 run-book
entries (18/18/13/13); SCORECARD/LOG appends raw_old_only=0, one disclosed
mid-file insertion (the capability row) + one disclosed in-place registry
edit (the S289 used-by cell, old → new logged in the round-64 note).

## Work performed

- **Carry-in addressed first (both r63 closure observations, status-neutral
  as routed).** (1) `rekey_round: 61` on r63-created entries: root cause
  located — the field is a hardcoded constant in the as-run rebind tool,
  inherited r61 → r63 (lesson mistake 4); the precision correction is R64-C1
  (the `rekey_batch` field, in data + convention + machinery). (2) the Gate
  reject sample is stated explicitly in `corpus/lessons/round-64.md`
  `## Gate` (fresh rejections: none — both openings were adopted as claim
  grounds, said in terms; price-outs named; the standing S293 W04 marker
  cited).
- **R64-C1 (calibration, the lane's lowest scored axis at 8; sourced on new
  row S295 = W3C PROV-DM, opened this round).** The ledger's run-book batch
  attribution became explicit, addressable and self-recording: all 49
  run-book entries now carry `rekey_batch` (`r61-batch-1` 18, `r61-batch-2`
  18, `r63-batch-1` 13 — insert-before pure insertions, CRLF), the
  convention is stated of record (`rekey_round` = run-book generation id 61;
  `rekey_batch` = executing run id), and the r64 rebind machinery itself
  emits `rekey_batch: r64-batch-1` on its 13 fresh entries (criterion 120's
  grep-addressable shape). Provenance ground: PROV-DM's generation relation.
  No-harm measured, not assumed: the ledger edit alone leaves the guard
  green (live at `33cb4b0d`: `lost=0 ok`, probe 20/20) — the frozen selector
  ignores the ledger as an input and no credited entry pins it. Evidence:
  `.ufo/evidence/round-64/win-host/live-A-guard.txt`,
  `live-counting.txt`, `live-additivity-battery.txt`.
- **R64-C2 (operability, verdict-only; capability; adopts considerthese
  2026-10-28 proposal 1's cited-receipt-exists half — the one unimplemented
  proposal this round adopts; ground re-opened on held S289 with a fresh
  located quote, byte-identical fetch to the r61 extract).** New tool
  `tools/receipt-exists.py` (228 lines): named docs read at a pinned rev via
  git objects, backtick-cited `.ufo/`+`tools/` paths resolved by
  `git cat-file -e REV:path` (blob or tree), disclosed skip rules,
  `--extra-root` for the lane's fleet-root-surface cites; 4-arm hermetic
  selftest (`RECEIPT_EXISTS_SELFTEST: 4/4 pass`). Demonstration at the tip
  on the r63 records: `docs=2 paths=16 missing=0 extra=2` — the sweep
  genuinely catches the cross-surface class: the r63 records cite
  `.ufo/l0-questions.md` and `.ufo/reports/round-63/tameshi.md`
  lane-relatively; both resolve at the named fleet root (EXTRA lines), none
  is missing. The SOURCES edits that carry the sourcing staled exactly the
  forecast: live RED at `b31e8145` `cand_credited=51 lost=13 RED` — the same
  13 headings the planned block named, miss = 0 — and the r61 run-book
  (reused: the r63 as-run machinery re-driven at this round's constants,
  diff receipted `rehearsal/make-rebind-r64.diff`) restored the monitor at
  `1763db52`. Capability row `receipt-existence sweep` entered. Evidence:
  `live-selftest.txt`, `live-demo-sweep.txt`, `live-B-red.txt`,
  `live-C-green.txt`, `live-C-green-hist.txt`, `live-C-revmode.txt`,
  `live-rebind.txt`.
- **Criterion-110 forecast, measured before landing.** A `--no-checkout`
  scratch clone (the lane tree carries the NTFS-uncheckoutable r57 receipt
  path `a:b.txt`; plumbing and the plumbing-commit helper do not need the
  worktree) rehearsed every stage BEFORE the declaration landed: A
  (`37d1bca1`, ledger alone → `lost=0 ok`), B (`b5568919`, SOURCES+tool →
  `lost=13 RED`), C (`1144148e`, rekey → `lost=0 ok` both floors). The
  measured forecast is in the SCORECARD planned block, committed at
  `33cb4b0d` — before the SOURCES edit landed; the live B matched it
  exactly. Rehearsal receipts: `.ufo/evidence/round-64/win-host/rehearsal/`
  (12 files); the clone is deleted with the scratch.
- **Fresh-start duty.** The last three rejected closures (r58, r59, r60
  spot-checks) re-read before declaring; the premise is stale (r61/r62/r63
  admitted) but the duty was performed and the standing rulings honored
  (r58 certification/controls discipline; r59 cheat-discriminating counters;
  r60 the guard verified on this host — it ran at every measured rev).
  Ruled out, with reasons (SCORECARD planned block; lesson): any edit to the
  guarded probe (digest `892a045d…` pinned; the round-64 win-host copy is
  byte-identical, digest re-verified); the standing r59–r62 rulings;
  SKILL/QUALITY/README/PROVINCE edits (measured pin sets price this round's
  SOURCES edit at exactly one rekey: 9 SKILL / 6 QUALITY / 7 README / 13
  SOURCES, QUALITY ⊂ SOURCES — receipt `rehearsal/pin-sets.txt`); a
  full-corpus receipt sweep over all lessons since round 1 (declared future
  work, not a smuggled claim); fetching the ls-tree docs to stage a
  rejection (refused as dishonest — see Gate).

## Landed changes

| Commit | Carries | LOG entry |
|---|---|---|
| `33cb4b0d…` | ledger `rekey_batch` (49 insertions); SCORECARD planned block (frozen pre-data + the measured criterion-110 forecast); lesson round-64 (claims, Gate, 4 mistakes); LOG round-64 entry; rehearsal receipts (12 files) | round-64 entry |
| `b31e8145…` | `tools/receipt-exists.py`; SOURCES S295 row + S289 used-by re-open (old → new logged in the note) + round note (154 → 155); fetch receipts + extracts | round-64 entry |
| `1763db52…` | rekey `r64-batch-1`: ledger 693 → 706 + 13 trace receipts; union plan, manifest, rebind machinery as-run copies (precheck copy digest `892a045d…` verified) | round-64 entry |
| `be76552d…` | SCORECARD measured rows + capability row `receipt-existence sweep` (disclosed mid-file insertion); LOG finalization; live receipts (guard RED+green, selftest, demo sweep, additivity battery, counting, census end) | round-64 entry finalized |
| `6876d746…` + `c7d28b19…` | the post-landing tip-confirmation receipt only (guard at `be76552d`/`6876d746` both floors, additivity C→D, the lesson's own sweep) — evidence-file-only; no monitored or protected file changes `1763db52` → tip | round-64 entry (receipt note) |

Diff footprint `d0baf616..c7d28b19`: 56 paths, 48,488 insertions,
1 deletion — the deletion is the S289 used-by cell replacement in
`corpus/SOURCES.md` (the rule-2 in-place registry edit, logged old → new in
the round-64 note; SOURCES is outside the append-only convention's scope by
its own contract, the r63 RD4-repair precedent). LOG.md, SCORECARD.md and
the ledger are additivity-clean (`raw_old_only=0`; the ledger and the
SCORECARD capability row are disclosed mid-file insertions,
`verbatim_prefix=false`, `eol_rewrite_disclosed=false` everywhere).
PROVINCE.md, SKILL.md, README.md, `tools/registry.json` and the guarded
probe byte-unchanged base → tip (blob ids `8388c23a…`, `95d1f935…`,
`451e8236…`, `62c4670d…`, `e827e6e5…` — the same set the r63 verifier
recorded).

## Before → after measurements

- **R64-C1 (calibration).** Before (at base `d0baf616`):
  `git show d0baf616:.ufo/evidence/round-21/coldread/ledger.json | grep -c
  '"rekey_batch"'` → 0; the 49 run-book entries carry only
  `rekey_round: 61` across read_revs `19d7e996…`/`0a29e3cf…`/`8616d47…`.
  After: 49 at `33cb4b0d` (batches 18/18/13), 62 at `1763db52` (18/18/13/13)
  — receipts `live-counting.txt`; guard green with the ledger edit alone
  (`live-A-guard.txt`: `cand_credited=64 lost=0 ok`, exit 0); ledger 693 →
  706, JSON valid; additivity `raw_old_only=0` on the ledger at both edit
  points. Measured commit: `33cb4b0d627f1b06067bf002c256bc6da1eed962`
  (C1's own landing), batch field complete at `1763db52…`.
- **R64-C2 (operability).** Before: `git show
  d0baf616:tools/receipt-exists.py` → path does not exist;
  `git ls-tree d0baf616 tools/ | grep -c receipt-exists` → 0; S295 → 0;
  rows 154. After (at `1763db52`/`be76552d`): tool present (0 → 1);
  `RECEIPT_EXISTS_SELFTEST: 4/4 pass` exit 0; demo sweep
  `docs=2 paths=16 missing=0 extra=2` exit 0 (the 2 EXTRA lines name the
  fleet-root surfaces); S295 0 → 1; rows 154 → 155; RED at `b31e8145`
  (`lost=13`, miss = 0 vs the forecast) → `lost=0 ok` at `1763db52` at both
  floors + rev mode `credited=64/64`, probe 20/20; tip confirmation at the
  pushed head: both floors `lost=0 ok`, exit 0. Measured commit:
  `1763db52b42c7e0776a2d03b39dbf0db5d6adc59`.

## Sources & frontier

- SOURCES rows 154 → 155: one row added (S295, W3C PROV-DM, tier A docs,
  mined by the round-64 lesson, opened 2026-11-01; fetch receipt + extract
  `.ufo/evidence/round-64/win-host/sources/s295-prov-dm.html`; URL
  previously unheld: `grep -c prov-dm` → 0 at base). Counting command:
  `git show be76552d:corpus/SOURCES.md | grep -cE '^\| S295 '` → 1. One
  in-place rule-2-class edit logged old → new in the round note (the S289
  used-by cell gains the round-64 lesson; the fresh fetch is byte-identical
  to the r61 extract — 79,360 B, sha256 `624464ef…`; new located quote for
  the C2 existence ground: the `-e` option, fetched-page lines 2246–2247,
  12 words). No held row's status/recheck changed.
- Census: round start `bash scripts/sources-census.sh validate --root
  <fleet-root> tameshi` → exit 0 (154 rows; 17 W04 + 1 W01, all
  pre-existing); mid-round exit 0 at the working tree with S295 in
  (census-clean, no new warning); round end → exit 0, 155 rows, the same
  17 W04 + 1 W01 set (`census-end.txt` committed).
- Mistake mining (`corpus/lessons/round-64.md` `## Mistakes`, four rows,
  each with class · evidence · captured-by · fix): 1
  option-invention-in-instrument (`--quiet` is not a cat-file option, exit
  129 — caught by the selftest's GREEN arm on an existing object; probed
  receipt `rehearsal/catfile-quiet-probe.txt`); 2
  bounded-assumption-in-byte-surgery (the 400-line scan-back vs in-entry
  distances up to 7,709 lines — measured `rehearsal/ledger-distance.txt`;
  fail-closed refusal, no bad bytes); 3 prefix-map-constant-typo (7- vs
  8-char key, trailing comma — both fail-closed refusals); 4
  inherited-constant-in-as-run-tooling (`'rekey_round': 61` hardcoded in
  the as-run rebind, inherited r61 → r63 — captured-by the r63 non-author
  closure; fixed this round in data, convention and machinery). Three of
  four self-caught pre-landing.

## Trend verdicts

- **expansion: unchanged** — no new knowledge entry, no frontier move; the
  one new SOURCES row is C1's claim ground; PROVINCE/README/SKILL
  untouched. A precision-and-adoption round, declared as such.
- **quality: improved** — the top unadopted proposal's
  cited-receipt-exists half is now a working instrument with a 4-arm
  selftest and a real demonstration (it found and classified the
  cross-surface citation class on the r63 records); the run-book executed
  end to end a third time, reused rather than re-derived; the monitor is
  green at the pushed tip at both floors; the S289 re-open's fresh fetch is
  byte-identical to the r61 extract.
- **discernment: improved** — four mistakes mined with captured-by fixes,
  three self-caught pre-landing by fail-closed gates (the refusals are the
  discipline working and are receipted); the Gate states its reject sample
  explicitly per the carry-in, including the refusal to stage a fetch for
  the sake of a rejection; the criterion-110 forecast was measured in a
  clone before the declaration landed and the live round matched it with
  miss = 0.

## SHONEN

SHONEN.md is unchanged this round (four boxes, all lane-asserted `[~]`, no
independent promotion verifier on record — none written by this round):

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — [resolvable pointer: SHONEN.md; SKILL.md byte-unchanged
  this round (blob `95d1f935…`); the 13 staled sections re-read in full and
  re-pinned with 13 committed trace receipts at pin `b31e8145`]
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  [resolvable pointer: LOG.md round-64 entry; the end-to-end task is the
  carry-in→field arc (C1) and the proposal-1→instrument→demonstration arc
  (C2), both receipted]
- [~] Instructions executable by an agent without oral context —
  [resolvable pointer: `.ufo/evidence/round-21/coldread/ledger.json`; the
  monitor reads `credited=64/64 lost=0 ok` at the pushed tip with the probe
  gate green at both floors (`live-C-green.txt`, `live-C-green-hist.txt`)]
- [~] No cross-domain bleed (PROVINCE.md still accurate) — [resolvable
  pointer: PROVINCE.md byte-unchanged `d0baf616` → `be76552d` (blob
  `8388c23a…`); the demo sweep's two fleet-root-surface citations were
  resolved and named, not absorbed]

Assimilation: considerthese 2026-10-28 proposal 1's cited-receipt-exists
half ADOPTED and demonstrated this round (`tools/receipt-exists.py`,
capability row entered; its byte-for-byte quoted-line half remains open;
proposals 2–5 unadopted, at most one per round); shokuknow unreachable.
L2 floor: no dispatch surface on this host — an L1-only round, disclosed in
the lesson; the r60 L0 question (`.ufo/l0-questions.md` at the fleet root,
tameshi | round-60, option (b)) stands unanswered and open.
