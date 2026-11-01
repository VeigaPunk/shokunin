# tameshi round 63 — report (L1 `TameshiR63`, 2026-11-01, win32 host)

Base `0b81e8f575627d8de2e3a9cf598d5360c42bfeb6` (= origin/master, the r62
spot-check landing). Lane head at close: `e9673d2ddfa3e2b445d93c21f20c4b34dc55ab07`
(= `refs/heads/master` = `origin/master`, pushed). Work commits:
`8616d47ebbb825ecbe0e15be142d77946710a026` (declared work),
`a18c20f07bb830245940c5d0a52b19d772f1f126` (rekey + restoration),
`e9673d2ddfa3e2b445d93c21f20c4b34dc55ab07` (receipts + measured rows).

CLOSURE-PREP: base `0b81e8f5` → head `e9673d2d` pushed=yes; claims=2
(R63-C1 calibration/RD5, R63-C2 operability+capability/RD6), both
self-verdict "verifies (measured)"; no-harm guard at the tip:
`COLDREAD_PRECHECK floor=0b81e8f5 floor_credited=64 cand=e9673d2ddfa3
cand_credited=64 lost=0 ok` and `floor=8b0042bd … lost=0 ok` (64/64; probe
sampled=20 mismatches=0); receipts `.ufo/evidence/round-63/win-host/`;
lesson `corpus/lessons/round-63.md` (4 mistakes mined, 2 self-caught
pre-push); SOURCES 153 → 154 (S294); census exit 0 start and end; ledger
680 → 693; SCORECARD/LOG/QUALITY appends raw_old_only=0, one disclosed
mid-file insertion (the capability-table row), one disclosed in-place
registry repair (the RD4 site).

## Work performed

- **R63-C1 (calibration, the lane's lowest scored axis at 8; closes the r62
  closure's routed defect RD5; sourced on new row S294).** The RD5
  correction became a standing convention with an instrument:
  `tools/additivity-receipt.py` (new, 232 lines) computes append-only
  receipts on COMMITTED bytes (`git cat-file` at pinned revs) with the
  normalization declared — raw AND CR-normalized old-only/new-only counts,
  `eol_rewrite_disclosed`, the verbatim-prefix property (empties dropped on
  both sides), append-only judged on the normalized comparison,
  `--require-raw` for rewrite-forbidden contexts — with a five-arm selftest
  whose green arms include the exact r62 defect shape (append + LF→CRLF
  rewrite of pre-existing lines: raw>0, norm=0, disclosed). The RD5
  correction-of-record erratum is in SCORECARD (re-measured pre-data: the
  r62 receipts as stated measure 80/30 on raw committed bytes; content
  truth 0/0 CR-stripped with a verbatim prefix). Evidence:
  `.ufo/evidence/round-63/win-host/red-before/additivity-redbefore.txt`
  (pre-data), `…/additivity/receipts.txt` (the battery),
  `…/additivity/r62-pair.txt`, `…/additivity/selftest.stdout`; SCORECARD
  `## Erratum — round 62 routed defect RD5`.
- **R63-C2 (operability, verdict-only; capability; closes the r62 closure's
  carried defect RD6 and repairs the RD4 registry-note site).** The QUALITY
  criterion proposal landed through the payment it was waiting for:
  Criterion 120 appended ("a described fix is grep-addressable in the
  shipped bytes, with the counting command in the claim", citing the r62
  lesson mistake 1); SOURCES row S294 appended (gitattributes documentation,
  fetched this round, census-clean, 153 → 154); the RD4 site repaired
  in place ("12 words" → "8 tokens" at the round-61 note, logged old → new).
  The record edits staled 13 cold-read sections; the r61 rebind run-book
  (analyze → union plan → manifest from genuine section re-reads → rebind →
  monitor) regenerated 13 fresh input-keyed ledger entries (11,012 input
  pins at pin rev `8616d47`) with committed trace receipts and restored the
  monitor. Evidence: `.ufo/evidence/round-63/win-host/rekey-plan.json`,
  `union-plan.json`, `rekey-manifest.json`, `entries-batch.json`,
  `rekey-summary.json`, `coldread-rekey-rebind-r63.py` (as-run r63 copy),
  `red-at-work-commit.txt` + `live-red.json` (the guard catching this
  round's own edits), `precheck-b.json`, `precheck-b-histfloor.json`,
  `precheck-rev-b.json`; traces `.ufo/evidence/round-63/rekey/traces/`;
  ledger `.ufo/evidence/round-21/coldread/ledger.json` (680 → 693).
- **Pre-landing scratch rehearsal (disclosed).** A content-identical clone
  (same plumbing helper) ran the whole pipeline first: stale set fixed at
  13, rebind validated (64/64 restored at rehearsal tip `f0eefec9`),
  receipts-commit safety validated (post-rekey SCORECARD/LOG appends keep
  `lost=0` in both floor modes), and it produced lesson mistakes 3–4. The
  clone is deleted with the scratch.
- **Fresh-start duty.** The last three rejected closures (r58, r59, r60
  spot-checks) re-read before declaring; r61/r62 were admitted (premise
  stale, duty performed). Ruled out, with reasons (SCORECARD planned block;
  lesson): standing r59–r62 rulings; any edit to the guarded probe
  (digest `892a045d…` pinned; a probe edit re-owes the probe-arms re-run);
  an unpriced registry edit (this round pays the rekey deliberately
  instead); building considerthese 2026-10-28 proposal 1 this round (would
  compete with the rekey; recorded as a proposal).

## Landed changes

| Commit | Carries | LOG entry |
|---|---|---|
| `8616d47ebbb825ecbe0e15be142d77946710a026` | `tools/additivity-receipt.py`; SCORECARD planned block (frozen pre-data) + RD5 erratum; QUALITY Criterion 120; SOURCES S294 row + RD4 site repair + round note; `corpus/lessons/round-63.md`; LOG round-63 entry; red-before receipts + S294 fetch/extract | round-63 entry |
| `a18c20f07bb830245940c5d0a52b19d772f1f126` | the rekey: ledger 680 → 693 + 13 trace receipts; union plan, manifest, rebind as-run copies; rekey-summary; SCORECARD CRLF byte-restoration (lesson mistake 4 — the amendment rewrite caught pre-push, restored at binary level before this commit); lesson mistakes 3–4 | round-63 entry (finalized at C) |
| `e9673d2ddfa3e2b445d93c21f20c4b34dc55ab07` | additivity battery + guard/census receipts; red-at-work-commit receipt; SCORECARD measured rows + capability row `monitored-record rekey run-book`; LOG receipt lines | round-63 entry finalized |

Diff footprint `0b81e8f5..e9673d2d`: 39 paths — 5 modified (LOG.md,
SCORECARD.md, corpus/QUALITY.md, corpus/SOURCES.md, the ledger
machine-file) + 34 additions (tool, lesson, evidence). PROVINCE.md,
SKILL.md, README.md, `tools/registry.json` and the guarded probe
(digest `892a045d…`) byte-unchanged.

## Before → after measurements

- **R63-C1 (calibration).** Before (at base `0b81e8f5`, red-before receipt
  committed pre-data): `git show 0b81e8f5:tools/additivity-receipt.py` →
  path does not exist; `ls tools/ | grep -c additivity` → 0; the r62 pair
  as stated measures `comm -23` → 80 (LOG.md) / 30 (SCORECARD.md) on raw
  committed bytes. After (measured at `a18c20f0`): `python -I
  tools/additivity-receipt.py --selftest` → `ADDITIVITY_SELFTEST: 5/5
  pass` exit 0; `python -I tools/additivity-receipt.py --repo . --base
  ed3a66c2… --tip 5721f7d5… --file LOG.md --file SCORECARD.md` →
  LOG.md raw_old_only=79 norm_cr_old_only=0, SCORECARD.md 29/0,
  verbatim_prefix=true, eol_rewrite_disclosed=true, exit 0 (raw one line
  under the closure's sort-u count: the inserted empty line is not a
  content member — stated in the erratum). Measured commit: tool bytes at
  `8616d47` (unchanged to `a18c20f0`); receipts at `a18c20f0`.
- **R63-C2 (operability).** Before: `git show
  0b81e8f5:corpus/QUALITY.md | grep -c "### Criterion 120"` → 0; `git show
  0b81e8f5:corpus/SOURCES.md | grep -cE '^\| S294 '` → 0; rows 153; ledger
  680; at the post-edit pre-rekey work commit `8616d47`: `python -I
  tools/coldread-precheck-portable.py --repo . --floor 0b81e8f5… --cand
  8616d47… --work WORK` → `cand_credited=51 lost=13 RED` (exit 1; LOST
  lines name `corpus/QUALITY.md`/`corpus/SOURCES.md`; rev mode
  `credited=51/64`). After (at `a18c20f0`): criterion grep → 1; S294 grep
  → 1; ledger count
  `python -c "import json;print(len(json.load(open('.ufo/evidence/round-21/coldread/ledger.json',encoding='utf-8'))['entries']))"`
  → 693; `… --floor 0b81e8f5… --cand a18c20f0…` → `cand_credited=64
  lost=0 ok` exit 0; `… --floor 8b0042bd… --cand a18c20f0…` → `lost=0 ok`
  exit 0; rev mode `credited=64/64`; probe sampled=20 mismatches=0
  everywhere; re-confirmed at the true tip `e9673d2d` (both floors
  `lost=0 ok`). Measured commit: `a18c20f07bb830245940c5d0a52b19d772f1f126`.

## Sources & frontier

- SOURCES rows 153 → 154: one row added (S294, gitattributes documentation,
  tier A docs, mined, opened 2026-11-01; fetch receipt + extract
  `.ufo/evidence/round-63/win-host/sources/s294-gitattributes.html`; no
  within-scope duplicate — `git show 0b81e8f5:corpus/SOURCES.md | grep -c
  gitattributes` → 0). Counting command: `git show e9673d2d:corpus/SOURCES.md
  | grep -cE '^\| S294 '` → 1. One in-place rule-2-class repair logged
  old → new in the round note (the RD4 count label). No held row's
  status/recheck/used-by changed.
- Census: round start `bash scripts/sources-census.sh validate --root
  <fleet-root> tameshi` → exit 0 (153 rows; 17 W04 + 1 W01, all
  pre-existing); round end → exit 0 at the content-final state
  (`.ufo/evidence/round-63/win-host/census-end.txt`) and re-run exit 0 at
  the pushed tip `e9673d2d` (154 rows; the same 17 W04 + 1 W01 set — S294
  adds no warning; the S293 W04 stands as that rejection's marker).
- Mistake mining (`corpus/lessons/round-63.md` `## Mistakes`, four rows,
  each with class · evidence · captured-by · fix): 1
  normalization-asymmetry-in-instrument (the tool's own first real-pair run
  disagreed with the verbatim-prefix truth; fixed pre-landing);
  2 instrument-first-run-shakeout (bytes/str + CLI wiring, fixed before the
  selftest passed); 3 commit-plumbing-path-discipline (directory paths
  no-op and backslash globs mangle in treecommit — caught by the
  rehearsal's `trace-missing` receipts at 51/64 across two clone commits);
  4 universal-newlines-rewrite (the amendment script rewrote SCORECARD.md
  CRLF→LF — the RD5 class recurring in this round's own tooling; caught by
  the diff-stat review pre-push, byte-restored, disclosed with the
  instrument's own receipt: raw_old_only=2388, norm=0, rewrite disclosed at
  commit `8616d47`).

## Trend verdicts

- **expansion: unchanged** — no new knowledge entry, no frontier move; the
  one new SOURCES row is claim-grounding for C1; PROVINCE/README/SKILL
  untouched. A repair-and-convention round, declared as such.
- **quality: improved** — the r62 stated-command defect has a correction of
  record, a standing convention and a committed red/green instrument; the
  defect class was caught recurring in this round's own tooling before
  push; the RD6 criterion and the RD4 site repair landed; the monitor is
  green at the tip.
- **discernment: improved** — four mistakes mined with captured-by fixes,
  two of them self-caught before landing (mistakes 3–4); the guard catching
  the lane's own record edits is receipted as the designed behavior; the
  SOURCES in-place repair is logged old → new rather than silently made.

## SHONEN

SHONEN.md is unchanged this round (four boxes, all lane-asserted `[~]`, no
independent promotion verifier on record — none written by this round):

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — [resolvable pointer: SHONEN.md; the round re-read 13
  SKILL.md sections in full and re-pinned them with 13 committed trace
  receipts; the 13 section reads verified-record with the r61 manifest's
  patterns re-validated at pin `8616d47`]
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  [resolvable pointer: LOG.md round-63 entry; the end-to-end task is the
  RD5→convention+instrument arc and the RD6→rekey arc, both receipted]
- [~] Instructions executable by an agent without oral context —
  [resolvable pointer: `.ufo/evidence/round-21/coldread/ledger.json`; the
  monitor reads `credited=64/64 lost=0 ok` at the pushed tip with the probe
  gate green (`precheck-b.json`, `precheck-rev-b.json`)]
- [~] No cross-domain bleed (PROVINCE.md still accurate) — [resolvable
  pointer: PROVINCE.md byte-unchanged `0b81e8f5` → `e9673d2d` (diff-tree);
  nothing absorbed; the win32 host correction of record stands from r60]

Assimilation: considerthese 2026-10-28 proposal 1 (receipt-existence
linter) considered and priced out this round — it would compete with the
rekey for round scope; its counting-command half is criterion 120's ground
(landed this round), its cited-receipt-exists half remains proposal;
shokuknow unreachable. L2 floor: no dispatch surface on this host — an
L1-only round, disclosed in the lesson; the r60 L0 question
(`.ufo/l0-questions.md`, tameshi | round-60, option (b)) stands unanswered
and open. Assimilation: none — shokuknow unreachable.
