# ReviewerSeat — round-9 non-author citation re-execution

Stamp: `2026-09-29T00:49:09Z` for the first HEAD capture; main `62fdfbe`; child HEADs then were kasegi `b7180b0` dirty 7, kengaku `f09ff1f` dirty 2, kake `a209441` clean, kumitate `ed991d0` clean, kotoba `63ceba7` clean, kagi `4391b3b` dirty 21. HEADs moved during measurement; later commands print their own observed revisions and are not silently merged with the first stamp. All child lesson counts below use `git show HEAD:corpus/lessons/round-8-aggregator-box3-coldrun.md`.

## Cell grades

| Cell | Grade | Re-execution and observed value |
|---|---|---|
| X1, six repos with committed verdict | **PASS (with count discrepancy)** | Corrected per-repo command: `git -C <repo> cat-file -e <hash>^{commit}` + `git -C <repo> show -s --format='%an <%ae>' <hash>` + `merge-base --is-ancestor <hash> HEAD`. All 15 hashes printed in the X1 parenthetical resolved, were authored by `aggregator-shokunin <aggregator@shokunin.local>`, and returned ancestor status 0. The report/LOG enumerate 16 round-8 child commits only when adding kotoba self-repair `2839f60`; X1's parenthetical itself names 15. The six-repo 6/6 verdict claim reproduces; the “16” wording is internally inconsistent but not a missing commit.
| X2 commands 115 / 105 ok / 10 fail | **FAIL** | Strict indexed-row command count over committed lessons: `17+20+16+10+16+20 = 99` command rows (the published 18/20/16/10/25/26 includes multi-command/semantic rows not represented as one indexed table row). The literal table count therefore does not reproduce 115. Exit-code text is not the published semantic ok/fail split; e.g. kagi has documented negative exits while published as 26/26/0. |
| X3 break points 28 | **FAIL** | Strict indexed break-point count: `5+0+3+4+0+5 = 17`, not 28. The published per-repo values are not reproducible by the committed lesson tables. |
| X4 gated 30 (12 with / 18 without) | **FAIL** | The committed lesson files have no numerically indexed `Gated steps` rows under the published table shape; a naive pipe-row count produced 37 including headers/continuations. The only reproducible aggregate is the prose table's 30 (7+3+12+0+1+7), not a mechanically countable 12/18 split from the six committed files. |
| X5 12/12 | **STALE** | Not a requested primary cell; §13.6 standing tables are cutoff claims at `46e9ec3`, while main and child trees moved. |
| X6 4/4 | **STALE** | Round-7 landing was true at the round-8 cutoff but main tree has advanced. |
| X7 84 distinct keys / next D-87 / folds | **STALE** | Published command `grep -oE '^\\| D-[0-9]+' ... | tail -1` is host-sensitive. Current ledger has later D-rows; the cell is cutoff-stamped and no longer live. The cited folds `D-39⊇D-85` and `D-51⊇D-84` are present in §13.2 prose. |
| X8 41 = 30/8/3 | **FAIL** | No committed round-8 reviewer transcript or 41-cell ledger exists under `.ufo/waves/round-8/`; §13.6-Q is only two commands and cannot reproduce 41/30/8/3. The three historical FAIL descriptions are prose-only self-defects 13–15, not a cell ledger. |
| §11.1 audited HEAD existence/age | **PASS (existence); STALE (age)** | `git -C <repo> rev-list --count <hash>..HEAD`: kasegi `fb9ac8e`=6; kengaku `f147a27`=7 and `1bd17ec`=4; kake `dd4eabf`=7; kumitate `7a4c9a0`=16 and `31f09cd`=12; kotoba `8e22a41`=17; kagi `e64e81b`=7. All resolved; these are stale relative to moved child HEADs. |
| report 15 seats | **PASS** | Counting L2 wave-digest table rows in `.ufo/reports/round-8/aggregator.md` yields 15 named seats. |
| report 17 aggregator-identity child commits | **FAIL** | `git -C <child> log --author=aggregator-shokunin` lists round-8 child commits as 3+2+2+3+4+3 = 17 only if counting kotoba's `2839f60`; the report's own §13.1 says 16 and LOG enumerates 16. The X1 lesson-parenthetical names 15. Internal contradiction; 17 is not a stable cell. |
| report 24 new D-rows | **PASS at stamp; STALE live** | §13.2's numbered fresh range `D-87..D-110` is 24 (`110-87+1`); later D-111..D-120/revisions are outside that cutoff count. |
| report 6/6 amendments | **PASS** | Each of six committed lesson files has at least one `## Round-8 amendment (critic-absorbed)` section. Kagi has two amendment sections; the claim is repo coverage, not exactly-one count. |
| LOG round-8 3 FAIL tally | **PASS** | LOG lines 247–252 name the same three defects: kotoba self-healed timing, host-broken R4 token scan, and round-7 report L0 count. They are re-derivable as defect descriptions, though not as a 41-row evidence ledger. |

## §13.6 execution notes

Commands were read from `.ufo/reports/AGGREGATE.md:1366-1428`. B/B2/W/R/K-S-U-G-A/Q are cutoff-stamped scripts, not all current-tree facts. B's published `tail -1` grade rule is itself contradicted by the committed kumitate lesson: `git show HEAD:.../kumitate...md` contains only `**[ ]**` grade markers (lines 36 and 121); the operative `[x]` is prose (`Operative box-3 grade: [x]`), so B's `grep -oE '\*\*\[[x~ ]\]\*\*' | tail -1` cannot emit `[x]` for kumitate. This is a citation FAIL in the self-repair mechanism.

## Rule 8 literal-text re-execution

`CORPUS.md:43-46` literally forbids vault ref paths `op://…`, including examples. Commands run:

```sh
git -C <repo> grep -n 'op://' HEAD -- corpus/
```

Observed at one later moving-tree invocation: kasegi 2, kengaku 1, kake 2, kumitate 1, kotoba 3, kagi 75 (the command output listed every file:line; kagi's HEAD had moved to `4b8c018` during this invocation). SentinelSeat's landed-corpus sweep reported 2/1/2/1/3/55 at its stamp; the first five agree, kagi disagrees because the kagi tree moved from `4391b3b` to `4b8c018` while measuring. The hits are corpus prose, sweep patterns, and schematic examples; no secret value was printed. Under literal rule 8, every repo is **FAIL-literal / PASS-intent** where hits are schematic, because the rule forbids paths regardless of whether the referenced item is a placeholder. The inherited round-6 “clean” ruling is therefore not a literal-text PASS. This is routed to operator/integrator as a rule-8 interpretation contradiction.

## Historical three-F​​AIL recheck

The three failures are supported by the committed prose and are not silently upgraded: (1) the LOG says kotoba’s “self-healed by 22:55Z” was landed at 23:27:55Z; (2) §13.6 explicitly records the §12.5-R4 `grep -oE '[0-9]+$'` form as broken on pi-uu-grep 0.2.0; (3) LOG says the round-7 L0 claim was 7 while the cutoff blob had 6 lines. These remain FAILs for the original reviewer citation set.

## Scope / authorship

This review is non-author only with respect to child lane source files. The aggregator lane authored the lessons and the ledger citations; therefore these are self-defects, not non-author proof of aggregator conformance. No child or main source files were modified; this file is the sole artifact written by ReviewerSeat.
