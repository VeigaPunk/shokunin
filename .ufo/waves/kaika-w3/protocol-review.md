# kaika W3 — non-author verification, protocol lane round 16

Reviewer: W3ReviewProtocol (non-author). Worktree `fleet-protocol` read-only; `git status --porcelain` empty after every run. Scratch: `/tmp/kaika-verify/protocol/`. Verdicts below are recommendations.

Commits (`31baf5c..HEAD`): `7c5b34f` (work, 50 files) and `3be33b6` (report, 1 file). Both `protocol-shokunin <protocol@shokunin.local>` as author and committer. PASS.

## Recommendation

**ADMIT CONDITIONALLY.** The restore, gate, and PROTOCOL amendments reproduce. Three items must be corrected before admission (B1–B3). Operator items (O1–O4) do not block the lane's commits but need a decision or a note.

## Per-claim verdicts

| # | Claim | Recommended verdict | Evidence |
|---|---|---|---|
| 1a | Restore fidelity (ledgers = `12f2da5` + declared changes) | **verified** | `LOG.md` 12f2da5→HEAD: +70, 0 removed lines. `SCORECARD.md` +63/−14; removed lines are only the gate-integrity and soundness score rows, the Planned bullet, the `— none yet —` capability placeholder, and the saturation placeholder, all declared in the report. Aggregator section sha256 `5b60f902…` at both revisions. Round-14 `registry-home-rerun` (12 files) byte-identical to `b2f2efa`. |
| 1b | Carry-forward of fleet entries = 0 lost (G6, commit subject, LOG correction) | **not verified as stated** (B2) | `classify.sh` reproduces exactly (diff 0 lines), but it is tautological. `31baf5c` ledger blobs are identical to kotoba `b7470d7` (`3fc970db…`, `99de619d…`), so every added line is "in kotoba" by construction. It cannot detect a lost fleet entry. What does hold: a git-object search finds no post-`12f2da5` ledger content on any ref or unreachable commit (only `31baf5c` touches the ledgers after `12f2da5`; the unreachable post-`12f2da5` commits are `r12@test` stubs carrying kotoba bytes). Uncommitted fleet-root content overwritten before the sweep is unverifiable from git. |
| 1c | Gate `root-ledgers.py`: live clean, `--rev 31baf5c` fails, frozen replays, self-test can fail | **verified** | Live HEAD `clean` exit 0. `--rev 31baf5c` exit 1 with the 4 expected findings. `--rev 12f2da5`/`7c5b34f`/`3be33b6` exit 0. `--frozen` ok/ok. `--selftest` 9/9. `mutate.sh` 9/9 killed. Tampered pinned sha → `snapshot_tampered`, exit 2. `--rev deadbeef0000` → `git_error`, exit 2. Gate sha256 `90867e31…c7557` matches runs.md. Fixtures cover all six section/row checks: `kotoba-clobber` (checks 1–2), `registry-lost` (3), `aggregator-lost` (4), `registry-below-aggregator` (5), `closure-row-lost` (6). |
| 2 | Protocol soundness amendments (4 rules, rows, pointers, essence) | **verified with a caveat** | `PROTOCOL.md` and `PROTOCOL-APPENDIX.md` diffs are additive only; essence sentences untouched. Four new appendix rows (44→48) match four new rules. Body pointers resolve 20→24 (`(§Appendix, "X")` template text excluded). Caveat: the `corpus/SOURCES.md` pointer targets `CORPUS.md` §"SOURCES.md — where a shokunin learns", which exists on no branch yet (`kaika/contract` and `kaika/census` have no commits; `grep -c 'where a shokunin learns' CORPUS.md` = 0 at head and base). It is disclosed as interim authority `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`, which exists only on `kaika/ledger`. |
| 3 | Report: counting commands, sections, SHONEN | **defects** (B1, B3, O5) | See the re-run table below and the defects list. |

### Re-run counting commands (base = `31baf5c` archive, head = `3be33b6` archive)

| # | Claim | base | head | Result |
|---|---|---|---|---|
| G1 | fleet headers line 1 | `# kotoba-shokunin — …` | `# shokunin (main repo) — …` | match |
| G2 | registry / aggregator heading count | 0 / 0 | 1 / 1; registry line 177 < aggregator line 234 | match |
| G3 | closure-check + root-ledgers gate rows above aggregator | **0** | **0** | **MISMATCH.** Report's command `(closure-check\|root-ledgers)` is literal `\|` in awk, matching nothing. With `(closure-check|root-ledgers)` (or `grep -cE`), head = **2**, which matches the claim. Command is wrong; value is right. (B1) |
| G6 | classify.sh | 41 hunks, carry 0 | identical output | reproduces; tautological (see 1b) |
| G7 | round-14 files | 0 | 12 | match |
| P8 | SOURCES.md / Sources & frontier / frontier step / mistake / root-ledgers | 0/0/0/0/0 | 3/2/5/2/2 | match; counts of term occurrences, not soundness evidence (O4) |
| P9 | appendix table rows | 44 | 48 | match |
| P10 | round-13 verifier | 3/8 failed, caps 513/470 | 3/8 failed, caps 533/470 | failed set match; caps gap grew 43→63 (O4) |
| P11 | wc -l -c | 513 44449 / 51 14390 | 533 46627 / 55 15863 | match |

Gate runs and mutation runs were executed from the worktree root; no file was written in the worktree.

## Defects

### Blocking before admission

- **B1 (medium) — G3 counting command does not reproduce.** As written, `awk '…/^\| (closure-check\|root-ledgers) \| gate \|/…'` returns 0 at base and at head (GNU Awk 5.4.1). The claimed "after = 2" needs `(closure-check|root-ledgers)`. Fix with an erratum; the claim's falsifiability depends on the command working.
- **B2 (medium) — carry-forward overclaim.** `classify.sh` tests whether the clobber's *added* lines appear in the clobber's own bytes, which is guaranteed by blob identity. The "0 fleet entries lost" wording in commit `7c5b34f`, the LOG correction ("no genuine fleet entry inside the clobber needed appending") and G6 ("independently re-derived") imply a lost-entry test that was not run. Required: narrow the claim to what was measured (no post-`12f2da5` ledger content in any git object; uncommitted fleet-root content unverifiable) and say so in an erratum (LOG is append-only). The difflib "1299/1299" figure in the report also differs from numstat 1356 with no explanation.
- **B3 (low–medium) — missing minimum-content item.** PROTOCOL.md §Round-robin rounds, minimum content, requires "cross-domain evidence encountered, with the domain it belongs to". The report has no such item (sections: Work performed, Landed changes, Before→after, Sources & frontier, Mistakes, Trend verdicts, Closure record, SHONEN, L0 questions, Integrator notes). A one-line "none encountered" item suffices.

### Operator items (non-blocking, must be stated in the report or a note)

- **O1 (medium) — unreported pre-existing divergence in fleet-root history.** Seven dangling commits from 2026-10-17 (`5870ee5`, `c8b4e56`, `8a23eb0`, `88b10d4`, `d62889a`, `88658c2`, `0922425`; author `ci`/Cursor/shokunin docs; parent `ee2c793`, an ancestor of `12f2da5`) carry LOG blobs with 2026-10-17 README entries (4–18 lines not present in `12f2da5`, `31baf5c` or kotoba). `12f2da5` has zero `## 2026-10-17` headers. These commits are not in any ref or master's reflog. Their entries predate `12f2da5` and are outside the report's stated scope, so the restore is not wrong, but "0 fleet entries lost" is not the whole picture. Operator decision needed on whether these are fleet entries.
- **O2 (medium) — the clobber is published.** `git -C fleet reflog show origin/master` shows `31baf5c refs/remotes/origin/master@{0}: update by push`. The report says "No push" for this lane, which is true for its own work, but origin already carries `31baf5c`. The restore will need a push and the operator should know the bad state is remote.
- **O3 (medium) — gate is not wired to a trigger.** PROTOCOL.md Invariants makes `root-ledgers` "the check", but nothing runs it at merge, closure, or commit time. The incident happened because no check ran. Recommend wiring it into the merge/closure step. Also low: `--rev` values beginning with `-` are parsed by git as options (`--rev=--output=…`); git then exits 0 with empty stdout and the gate reports `failed` (exit 1, `line 1 is ''`) instead of `could-not-evaluate`. Not exploitable here, but the mapping is wrong.
- **O4 (low) — trend verdicts overstated.** (a) "quality: improved" rests on G7, a restore, and P8, term-occurrence counts; recommend "restored" for G7 and "unchanged" for quality. (b) "no axis harmed" ignores P10: the caps value grew 513→533 against a 470 cap the round-13 verifier already fails, so the gap grew 43→63. Disclose it as a length regression. (c) Claim 1 "improved" with score "held at 9" is internally coherent only if the capability addition is credited as improvement; state that explicitly.
- **O5 (low) — stale and process notes.** (a) Integrator note says stray fleet-root commits `551478a`, `4b2123b`, `b21278d` "must not be dropped". Fleet `master` was already reset to `31baf5c` at 18:46:50 (reflog), and those commits are unreachable `r12@test` stubs. The instruction is moot; say so. (b) Mistake 2 records `git checkout -- LOG.md` run in the shared fleet root. It was self-reported as a +38/−0 revert, but it is a destructive git command in a shared tree; the lane should not do this again. (c) SHONEN boxes are `[ ]` with `n/a` and no pointer; the contract's box form requires `[x]/[ ]/[~]` + pointer. Nothing is `[x]`, so no unearned mark. (d) Fleet-root `LOG.md` and `SCORECARD.md` remain kotoba bytes (sha `998274c0…`, `a4ec5348…`) until merge; the report says so.

## Other checks performed

- Protocol essence: per-axis verdicts, 1–3 claims, non-author verification, append-only, provenance — unchanged in the diff.
- Fleet-root refs: no ref other than `31baf5c` touches `LOG.md`/`SCORECARD.md` after `12f2da5` (`for-each-ref` sweep).
- `ab707d9` (kotoba r42 note recording the earlier uncommitted overwrite) is an ancestor of `31baf5c`; the report's prior-warning citation is accurate.
- Protocol.round counter = 14 at head (`od -c`), consistent with the L0 question.
- Report commit `3be33b6` cites work commit `7c5b34f` and contains no `[x]`.

## Residual risk and verification gaps

- Uncommitted fleet-root content overwritten before the 17:03 sweep (the 07:35 overwrite noted in `ab707d9`) cannot be checked from git. Recovery requires the operator or the originating lane.
- Template §4 and the operator-side `CORPUS.md`, `scripts/sources-census.sh`, and round-prompt section 2b were not in the repo; their conformance is unverified.
- `AXES.md` wording on declaring saturation values was not checked against the declared 10 / N=3.
- Evidence pointers into `kaika/ledger` (`.ufo/waves/kaika-w1/*`, `SOURCES-CONTRACT-v1.md`, `lane-addendum.md`) were confirmed to exist on that branch, not on `kaika/protocol`.

## Verdict on gate-integrity and protocol-soundness

- **gate-integrity:** restore and gate verified; score **9 held** agreed; carry-forward half not verified (B2). Recommend admission after B1/B2 errata.
- **protocol-soundness:** amendments verified additive with pointers resolving; score **8 held** agreed; P8/P10 framing to be corrected (O4).

## Trend verdicts

- expansion: **improved** agreed (first capability row present, gate reproduces).
- quality: **restored**, not improved (O4a).
- discernment: **unchanged** agreed.

## Admit / reject

**ADMIT CONDITIONALLY** on: B1 (fix G3 command), B2 (narrow the carry-forward claim by erratum), B3 (add the cross-domain item). Route O1 and O2 to the operator before merge. Re-run the gate after merge against the fleet root: `python3 .ufo/gates/root-ledgers.py --root <fleet root>` should read `clean` only after the restore lands.
