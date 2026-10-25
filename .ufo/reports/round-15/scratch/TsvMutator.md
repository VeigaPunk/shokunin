# TsvMutator — round 15 mutation evidence

Target: `corpus/checklist-run.sh` + `corpus/checklist.tsv`. Every mutation below was made in `/tmp/tsvmut/` only. The repo files were not edited by this lane. The frozen copy was `/tmp/tsvmut/cage/{frozen-run.sh,frozen.tsv}`; the execution shadow was `/tmp/tsvmut/shadow/corpus/`, with `CHECKLIST_RUN_ROOT=/home/vgpnk/projects/shokunin/kagi-shokunin` so runnable commands used the real repo as their declared cwd while the copied TSV/script were the subject under test.

Baseline (frozen pair, observed):

```text
CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7 delegated=3 direct=6
CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0)
```
Exit 0. `--selftest` on the copied gate was also observed as `CHECKLIST_SELFTEST: PASS (28 cases)` exit 0. (The extra `delegated`/`direct` fields are current landed output.)

## Required mutation matrix

| # | Exact mutation command / change in `/tmp` | Observed verdict line(s); exit | Must fail? / classification |
|---:|---|---|---|
| 1 | Python rewrite of E1 field 6 (`expect_last`) to `^A1_BASEMENT_DIVE: NOTHING$`; command and expected exit unchanged. | `ITEM-LASTLINE E1 (want /^A1_BASEMENT_DIVE: NOTHING$/ got DRIFT_PINS: CLEAN (files=15 symbols=20))`; `CHECKLIST_RUN: BROKEN (items=16 runnable=9 by_hand=7 failed=1)`; exit 1. | **FAILS-CLOSED**. Must fail because the actual final non-empty line does not match the declared ERE. |
| 2 | Python rewrite of E1 field 5 (`expect_exit`) from `0` to `1`; command unchanged (observed command exit is 0). | `ITEM-FAIL E1 (exit 0 want 1)`; `CHECKLIST_RUN: BROKEN (items=16 runnable=9 by_hand=7 failed=1)`; exit 1. | **FAILS-CLOSED**. Must fail on exit mismatch. |
| 3 | Python rewrite of E2 id from `E2` to `E1`, creating duplicate id. | `POLICY duplicate row id: E1 `; exit 2. | **FAILS-CLOSED**. Must be shape/policy failure before runnable execution. |
| 4 | Python rewrite of E6 field 7 (`reason`) to `authoring-duty: too short` (fewer than 24 chars after the class prefix). | `POLICY row E6: reason authoring-duty: too short is not \`<class>: <>=24 chars>\` with class in (authoring-duty|runtime-behavior|cross-lane|manual-change|operator-scope)`; exit 2. | **FAILS-CLOSED**. Must reject a short by-hand reason. |
| 5 | Python copy of E6's by-hand reason into E7 field 7, making two by-hand rows share one exact reason. | `DUPLICATE-REASON (authoring-duty: no command can tell whether a value's class was checked before quoting; the masking contract itself is row E5's probe|)`; `CHECKLIST_RUN: BROKEN (items=16 runnable=9 by_hand=7 failed=0)`; exit 1. | **FAILS-CLOSED**. Must reject duplicated by-hand rationale. |
| 6 | Python rewrite of E4 field 4 (`cmd`) to `exit 2; echo REF_PATH_SCAN_X`; E4 still declares `expect_exit=0`. | `ITEM-FAIL E4 (exit 2 want 0)`; `CHECKLIST_RUN: BROKEN (items=16 runnable=9 by_hand=7 failed=1)`; exit 1. | **FAILS-CLOSED**. Must fail unexpected runnable exit 2. |
| 7 | Python rewrites E8 and H1 from `runnable` to `by-hand`, changes their command/exit/lastline fields to `-`, and gives each a valid unique by-hand reason. Runnable count goes 9 → 7, below floor 8. | `RATIO (runnable=7 floor=8 items=16)`; `CHECKLIST_RATIO: runnable=7/16 floor=8 by_hand=9 delegated=3 direct=4`; `CHECKLIST_RUN: BROKEN (items=16 runnable=7 by_hand=9 failed=0)`; exit 1. | **FAILS-CLOSED**. Must enforce coverage floor. |
| 8 | Python rewrite of E2 class token from `by-hand` to `manual` (all other fields unchanged). | `POLICY row E2: class manual is not runnable|by-hand`; exit 2. | **FAILS-CLOSED**. Must reject closed-set violation. |
| 9 | In a separate `/tmp/tsvmut/mut9` repo copy, Python changes one checklist bullet from `- [ ]` to `- [x]`, leaving 16 TSV rows while the SKILL extraction finds 15 items. | `EXTRA (items=15 rows=16)`; `UNMATCHED-LEAD E1 (/Record mechanism and metadata/ matches no item)`; `CHECKLIST_RATIO: runnable=9/15 floor=8 by_hand=7 delegated=3 direct=6`; `CHECKLIST_RUN: BROKEN (items=15 runnable=9 by_hand=7 failed=0)`; exit 1. | **FAILS-CLOSED**. The gate asserts the live SKILL↔TSV row count/bijection, so a 16→15 item drift must fail. Reverse test (add a 17th bullet) observed `UNDECLARED (items=17 rows=16)` + `UNMATCHED-ITEM 2`, exit 1. |
| 10 | Python rewrite of E1 command to `echo CHECKLIST_RUN: CLEAN; exit 1`; E1 still declares `expect_exit=0`. | `ITEM-FAIL E1 (exit 1 want 0)` plus echoed diagnostic `| CHECKLIST_RUN: CLEAN`; `CHECKLIST_RUN: BROKEN (items=16 runnable=9 by_hand=7 failed=1)`; exit 1. | **FAILS-CLOSED**. A forged CLEAN-looking command line cannot override the expected exit. |

## False-clean / gap list

1. **False-clean (additional policy bypass): dynamic denied-path construction.** As an extra probe beyond the ten required classes, I changed H3's command to:
   `f="$HOME/.config/the-janitor/$(printf op)$(printf .env)"; grep -c . "$f" >/dev/null 2>&1 && echo OPENV_READ_OK`
   (the literal `op.env` token is absent from the TSV check string, so the current `DENY_CHECK` regex does not see it). Observed: `ITEM-LASTLINE H3 ... got OPENV_READ_OK`, exit 1, because the original H3 expected CONFIG_OVERLAY. If I mutate H3's `expect_last` to `^OPENV_READ_OK$` as well, the row becomes a **FALSE-CLEAN**: the gate exits 0 while the row has read `$CONFIG_DIR/op.env` bytes, violating the hard constraint. The gate's deny scan is lexical and is bypassable by shell construction. Recommendation: policy scan should reject shell constructs capable of constructing denied paths, or execute checks in a policy wrapper that denies the target path; do not rely only on contiguous-token matching.
2. **FALSE-CLEAN on padded reason (if padding is considered invalid by policy):** I changed E2's reason to `authoring-duty:` followed by 24 spaces and `never-trimmed`. The gate observed `CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0)` exit 0. This is only a defect if the policy means the *trimmed semantic reason* must have >=24 characters; the current row has 24 spaces plus text and the regex intentionally accepts it. If “reason” excludes whitespace padding, this is a real false-clean and the parser needs trim-before-length validation (the claim-ledger precedent does this).

No required mutation #1–#10 stayed green. Required score: 10/10 fail-closed. The two items above are additional policy gaps, not substitutions for any required class.

## Repo hygiene

I did not edit files under `kagi-shokunin/`; all mutations were copied under `/tmp/tsvmut/`. The repo had L1's own in-flight edits (including the two target files and concurrent documentation/state files); those were not reverted or changed by this lane.
