# Kagi gate re-run (independent)

Observer: KagiGateRerun. Read-only. Lane files not edited. No commit. This file is advisory data, not a judge verdict, receipt, or admission.

Lane: `kagi-shokunin`. cwd: `/home/vgpnk/Projects/shokunin/kagi-shokunin`. The nine-gate batch ran at assigned identity `5b0d4b784624a15506d3c85c77c3ae619e07467f` (author `kagi-shokunin <kagi@shokunin.local>`). `git status --porcelain` before and after that batch: `?? plans/` only. Host clock at the start of that batch: `2026-10-14T21:17:33-0300` (`2026-10-15T00:17:33Z`). Delivery HEAD later moved; see below.

Compared against `corpus/lessons/round-19-recensus.md` lines 6-15 (the round-19 verdict block), not against rounds 9-18 historical cells. Live modes of `transcript-scan.sh`, `checklist-run.sh`, `surface-census.sh`, and `drift-pins.sh` were not run.

## Claim vs observed

| Lesson claim | Observed at `5b0d4b78` | Verdict |
|---|---|---|
| `bash corpus/claim-ledger.sh citations` exit 0, `CITATION_GATE: CLEAN (cites=912 docs=53 unresolved=0 ephemeral=0 labeled=13)` | exit 0, `CITATION_GATE: CLEAN (cites=918 docs=54 unresolved=0 ephemeral=0 labeled=13)` | disagree on the two counts. Exit, unresolved, ephemeral, and labeled agree. 912/53 is the parent tree, not this commit. |
| `bash corpus/claim-ledger.sh docs` exit 0, `DOC_AUDIT: CLEAN (entries=21 row_linked=18 by_hand=3 undeclared=0 missing_ids=0 …)` | exit 0, `DOC_AUDIT: CLEAN (entries=21 row_linked=18 by_hand=3 undeclared=0 missing_ids=0 unpinned=0 duplicate_reasons=0)` | agree on every stated field and on exit. The lesson ellipsis is not the full line; the full line matches the fecee874 receipt. |
| `bash corpus/claim-ledger.sh --selftest` exit 0, `SELFTEST: PASS (97 cases)` | exit 0, same last line; preceding line `ok-case  97 defer-substrate-line` | agree |
| `bash corpus/drift-pins.sh --selftest` exit 0, `DRIFT_SELFTEST: PASS (13 cases)` | exit 0, same last line (only line) | agree |
| `bash corpus/surface-census.sh --selftest` exit 0, `SELFTEST: PASS (16 cases)` | exit 0, same last line | agree on the verdict line. Cases 15 and 16 printed `skip-case` substrate-absent before it. |
| `bash corpus/scope-gate.sh --selftest` exit 0, `SCOPE_SELFTEST: PASS (61 cases)` | exit 0, same last line (only line) | agree |
| `bash corpus/op-ref-probe.sh --selftest` exit 0, `OP_REF_SELFTEST: PASS (29 cases)` | exit 0, same last line (only line) | agree |
| `bash corpus/checklist-run.sh --selftest` exit 0, `CHECKLIST_SELFTEST: PASS (34 cases)` | exit 0, same last line (only line) | agree |
| `bash corpus/transcript-scan.sh --selftest` exit 0, `SELFTEST OK (seeded hit + wal-resident hit)` | exit 0, `SELFTEST OK (seeded hit + wal-resident hit detected; clean db passed)` | disagree as a full-line quote. The lesson string is a proper prefix. Exit agrees. The full line matches the fecee874 receipt and `transcript-scan.sh:256`. |

No selftest exit disagreed. The numeric miss is the citation summary. The transcript miss is quotation, not a failed selftest.

## Commands (argv, exit, last line)

All nine from the lane root, in one parallel batch. stderr was empty on every run. Porcelain did not change.

1. `bash corpus/claim-ledger.sh citations`
   - exit 0
   - elapsed 35.225s
   - stdout 1369 bytes, 14 nonempty lines, sha256 `f5307847c16709a8a71da1ed234df20485f2a81fcedab6151168a48c59ff7a17`
   - last line: `CITATION_GATE: CLEAN (cites=918 docs=54 unresolved=0 ephemeral=0 labeled=13)`

2. `bash corpus/claim-ledger.sh docs`
   - exit 0
   - elapsed 0.065s
   - stdout 1660 bytes, sha256 `8e5056a130c587b57dfaa56096a2f0b320114e6169e919bced5b3f967217f53c`
   - line above: `DOC_AUDIT_RATIO: row_linked=18/21 floor=11 by_hand=3 duplicate_reasons=0`
   - last line: `DOC_AUDIT: CLEAN (entries=21 row_linked=18 by_hand=3 undeclared=0 missing_ids=0 unpinned=0 duplicate_reasons=0)`

3. `bash corpus/claim-ledger.sh --selftest`
   - exit 0
   - elapsed 2.038s
   - stdout 5264 bytes, 98 nonempty lines, sha256 `8ea78e2e6fd4aee436694d6350198320411196c13dba13a6d6da10701fa0fea3`
   - last line: `SELFTEST: PASS (97 cases)`

4. `bash corpus/drift-pins.sh --selftest`
   - exit 0
   - elapsed 0.241s
   - stdout sha256 `701deed25230cbc6b8f108720654321446ba94a7f98941b7e89545c0b5a71bc8`
   - last line: `DRIFT_SELFTEST: PASS (13 cases)`

5. `bash corpus/surface-census.sh --selftest`
   - exit 0
   - elapsed 1.098s
   - stdout 1202 bytes, sha256 `09c21ee26b8b8b16618fe68a30043c612811da6bf008840a7a85bd3bce8a2fca`
   - lines above the verdict: `skip-case 15 verbs-sandboxed substrate-absent (handler not on PATH)` and `skip-case 16 verbs-break-injection substrate-absent (handler not on PATH)`
   - last line: `SELFTEST: PASS (16 cases)`

6. `bash corpus/scope-gate.sh --selftest`
   - exit 0
   - elapsed 5.550s
   - stdout sha256 `1861dc3de9ae3c354b69b494c22ab050e24979640adc184b77eacaab6d50d64d`
   - last line: `SCOPE_SELFTEST: PASS (61 cases)`

7. `bash corpus/op-ref-probe.sh --selftest`
   - exit 0
   - elapsed 0.994s
   - stdout sha256 `693edaacafe1355e3679b0a3ea84dcb7e094579ed0d44fd1b8c0dbc803b99c45`
   - last line: `OP_REF_SELFTEST: PASS (29 cases)`

8. `bash corpus/transcript-scan.sh --selftest`
   - exit 0
   - elapsed 3.030s
   - stdout 1215 bytes, sha256 `c42654d264ae93af9ffe9048b525132eb7e32dccab7772529b489d609dd7fb58`
   - last line: `SELFTEST OK (seeded hit + wal-resident hit detected; clean db passed)`
   - the line above is a scratch TRANSCRIPT_SCAN line whose db path is a fresh /tmp directory and is not part of the verdict

9. `bash corpus/checklist-run.sh --selftest`
   - exit 0
   - elapsed 2.012s
   - stdout sha256 `b03bc148509bd3ce7e602339c7ffe9103a163c5fba650dea580b98d98bf16611`
   - last line: `CHECKLIST_SELFTEST: PASS (34 cases)`

## Citation counterexample

`5b0d4b78` adds only `LOG.md` (+7), `SCORECARD.md` (+6), and new `corpus/lessons/round-19-recensus.md`. That is the commit whose lesson prints `cites=912 docs=53`. The citation scan set is `default_docs` in `corpus/claim-ledger.sh`: root docs plus `corpus/knowledge/*.md` and `corpus/lessons/*.md`. The new lesson is a new doc. Untracked `plans/wwkd-round-19-recensus.md` is outside that set and did not move the count.

Parent `fecee8743e52eb8fb5fbb40782934cb619a1a96e`:

- Repair receipt `kagi-after-corpus_claim-ledger.sh-citations.json` (not this run): exit 0, `CITATION_GATE: CLEAN (cites=912 docs=53 unresolved=0 ephemeral=0 labeled=13)`, stdout 1369 bytes. Same width as this run's 1369-byte stdout; the bytes are not the same claim. Resolved cites are not printed, so 912 to 918 and 53 to 54 do not change the byte count.
- Independent re-measure, this audit: `git archive fecee874` extracted under `/tmp/kagi-fecee-archive` (no `round-19-recensus.md`; 25 lesson files), then `bash corpus/claim-ledger.sh citations`. Last line `CITATION_GATE: BROKEN (cites=912 docs=53 unresolved=44 ephemeral=0 labeled=19)`, exit 1. Exit 1 is the archive not sitting beside sibling lanes. The cites and docs fields match the lesson. Do not read that exit as a red gate on the lane.

HEAD, fleet layout, this run: exit 0, `cites=918 docs=54`.

Per-file `bash corpus/claim-ledger.sh citations --docs FILE` on the live script, exit 0 each:

- `corpus/lessons/round-19-recensus.md` alone: `cites=4 docs=1`
- `LOG.md` at HEAD: `cites=100`; parent bytes: `cites=99` (delta +1)
- `SCORECARD.md` at HEAD: `cites=145`; parent bytes: `cites=144` (delta +1)

4+1+1 = 6. 912+6 = 918. 53+1 = 54. The arithmetic closes.

The six tokens the counter actually increments (lesson isolate matched cites=4):

1. `corpus/lessons/round-19-recensus.md:8` `corpus/claim-ledger.sh`
2. `corpus/lessons/round-19-recensus.md:10` `corpus/claim-ledger.sh`
3. `corpus/lessons/round-19-recensus.md:34` `SKILL.md`
4. `corpus/lessons/round-19-recensus.md:40` `corpus/lessons/round-13.md`
5. `LOG.md:768` `corpus/lessons/round-19-recensus.md`
6. `SCORECARD.md:452` `corpus/lessons/round-19-recensus.md`

`LOG.md:769` (the `.ufo/waves/shokunin12h-20261014-p1-repair/members/` line) isolated to its own file: the same script prints `cites=0`. It is not part of the +6. `bash -x` on a copy of the script showed `while read` never entered the body: `printf '%s'` plus `tr` emits that space-free line with no newline, so the last record is dropped. Observed, not patched.

Ledger row `R11-08` expects `^CITATION_GATE: CLEAN \(cites=[1-9][0-9]* docs=[1-9][0-9]* unresolved=0 ephemeral=0`. The HEAD line matches. The gate is green. The stale exact count is prose in the lesson, not the ledger pin. `LOG.md:762` (parent context, not added by this commit) already says the count moves with every doc edit, then records 912/53. That sentence was true of `fecee874`. It is not the current gate line.

The lesson header says full lines were retained in the wave receipts. Those receipts are measured_revision `fecee874`, not `5b0d4b78`. They agree with the lesson's 912/53 and with this run's docs and selftest full lines. They are not a measurement of the tree that contains the lesson.

## Delivery HEAD (tree moved during this audit)

After the nine-gate batch, `git rev-parse HEAD` was no longer `5b0d4b78`. Commits landed on the lane, not by this seat: `0eae46a`, `1eaf34d`, `bad9088f`, `eab4bec` (newest). Net diff `5b0d4b78..eab4bec7b2bb81adf72aca8a576d39695d458504` is `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-18.md`, `corpus/lessons/round-19-recensus.md`. No `corpus/*.sh` changed. Porcelain still `?? plans/` only.

Second measurement, clock `2026-10-14T21:28:03-0300`, HEAD `eab4bec7b2bb81adf72aca8a576d39695d458504`:

1. `bash corpus/claim-ledger.sh citations`
   - exit 0
   - elapsed 34.592s
   - stderr empty
   - stdout sha256 `0e0f1cfcfd8378c482884a376779a043db95d0378e0d435efa5c94c7f0ab7494`
   - last line: `CITATION_GATE: CLEAN (cites=925 docs=54 unresolved=0 ephemeral=0 labeled=13)`
2. `bash corpus/claim-ledger.sh docs`
   - exit 0
   - elapsed 0.055s
   - stderr empty
   - stdout sha256 `8e5056a130c587b57dfaa56096a2f0b320114e6169e919bced5b3f967217f53c` (same bytes as the assigned-commit docs run)
   - last line unchanged: `DOC_AUDIT: CLEAN (entries=21 row_linked=18 by_hand=3 undeclared=0 missing_ids=0 unpinned=0 duplicate_reasons=0)`

Lesson lines 8-15 are still the `cites=912 docs=53` block. The appended erratum (lines 43-49) says the seven safe gates re-ran green and repeats the selftest counts. It does not correct 912/53. It sits in the scan set, so it moved the count again.

Per-file `citations --docs` isolates, `5b0d4b78` bytes vs `eab4bec`, all exit 0:

- `LOG.md` 100 → 100
- `SCORECARD.md` 145 → 147
- `corpus/lessons/round-18.md` 1 → 3
- `corpus/lessons/round-19-recensus.md` 4 → 7

+2+2+3 = 7. 918+7 = 925. `docs` stayed 54.

Tokens that account for the +7:

- `SCORECARD.md:458` `corpus/knowledge/config-layering.md`
- `SCORECARD.md:464` `corpus/drift-baseline.tsv`
- `corpus/lessons/round-18.md:78` `corpus/surface-census.sh`
- `corpus/lessons/round-18.md:79` `corpus/drift-baseline.tsv`
- `corpus/lessons/round-19-recensus.md:49` `.ufo/waves/shokunin12h-20261014-p1-audit/members/KagiDeadPathSweep.md`
- `corpus/lessons/round-19-recensus.md:49` `SKILL.md`
- `corpus/lessons/round-19-recensus.md:49` `SCORECARD.md`

Selftests were not re-run on `eab4bec`. No gate script changed in that diff, so the assigned-commit selftest lines remain the script outputs. They were not re-measured after the doc commits.


## Named debt (not fixed)

1. Round-19 lesson line 9 still prints `cites=912 docs=53` as the measured citation verdict, including after the erratum at lines 43-49. That figure describes parent `fecee874`. Assigned identity `5b0d4b78` printed `cites=918 docs=54` at exit 0. Delivery HEAD `eab4bec` printed `cites=925 docs=54` at exit 0. Owner: kagi record (`corpus/lessons/round-19-recensus.md`, and `LOG.md:762` if that sentence is read as current). Unblock: re-run `bash corpus/claim-ledger.sh citations` after the last doc edit and record that line, or label 912/53 as the pre-lesson parent measurement. Do not tighten `R11-08` to hide the move. This audit did not patch it.
2. Lesson transcript quote drops ` detected; clean db passed`. Exit 0 and the full line are stable across this run and the fecee874 receipt. Owner: kagi record, only if the lesson must carry the full printf. Unblock: quote `SELFTEST OK (seeded hit + wal-resident hit detected; clean db passed)`. Not a red gate.
3. Not a lesson-number miss, recorded so it is not repaired: surface-census selftest cases 15 and 16 skip `substrate-absent` and the verdict is still `SELFTEST: PASS (16 cases)`. That matches the lesson's verdict line and the `R11-03` note. Handler absence remains carried substrate debt. Owner: operator. Unblock: reinstall the-janitor tree. Live modes stayed excluded.
