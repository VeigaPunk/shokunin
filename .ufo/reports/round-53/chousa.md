# chousa — round 53

## Work performed

Declared claims (frozen before any seat scored): **R53-C1 operability** (lowest scored non-retired axis, 3/10; capability extension, section-10 adopter v4 twin/recheck/refusal behaviour) and **R53-C2 depth** (sourced search-record-instruments theme, three entries and five candidate documents). Freeze: `chousa-shokunin/corpus/evidence/round53/claims.md`, commit `a6ff732c70011f11c9beb681d832cedc6e75f566`.

- **C1 baseline and freeze controls.** Base adopter `LEGS=1/8` (REGRESS only); const 0/8, always-refuse 0/8, relabel-only 5/8, all-twin 2/8; evidence `corpus/evidence/round53/controls/c1-before.txt`, frozen at `a6ff732c`.
- **C2 baseline and do-nothing controls.** `ENTRIES=0/3 BOUND=0/5 C2=FAIL`; staged-copy `REF_ID_UNBOUND=12`; mechanically adopted copy `BOUND=5/5` but `REF_ID_UNBOUND=4`, `ANCHOR_BOUND=0/5`, C2 FAIL; `corpus/evidence/round53/controls/{c2-before,c2-controls}.txt`, frozen at `a6ff732c`.
- **C1 candidate.** Applied the round-52 W1 routed twin/order fix, with self-test cases and digest `9822ad59544cd42d6c6a8c3d34cb14d4d7c98d21e4f388d604486d70dd5db4a6`; `python3 tools/assimilate-rows.py --selftest` → `SELFTEST=PASS findings=40 expected=40`. Commit `32aab5edd70e43145cae72ec872278f3bc6efba7`.
- **Sourced theme and entries.** Re-grounded three package entries; adopted JMLA, the issued guideline, its release notice and Cochrane chapter 4 as S117–S120. S118 is a single registry row for twin staged ids S185/S195. The S190 2019 NMPA notice print is refused; see lesson `corpus/lessons/round-53.md` `## Gate` and `refused-doc` line. Evidence `corpus/evidence/round53/{quotes.tsv,spans.tsv}` and `corpus/lessons/round-53.md`.
- **Quote/PDF verification.** 63 located quotes accepted by the span builder and substance check; 49 quotes on the two PDF captures independently checked with pypdf (`PDF_QUOTES=49 NOT_IN_INDEPENDENT=0`). `corpus/evidence/round53/pdf-crosscheck.py`.
- **Routed calibration work.** Seven anchored correction successors; `pointer-anchor-check.py` → `ANCHORED=7/7`. The round-52 erratum range is corrected to E1–E6 and the round-51 SKILL row to E1–E5. CJK polarity fixture: base tool 2/6, landed tool 6/6; C2 passes with both the base and changed `inference-ground.py` (claims-erratum E4). Evidence `corpus/evidence/round53/cjk-polarity-check.py`, `claims-erratum.md`.
- **SOURCES/frontier.** 35 section-10 id collisions; indented-row guard proof in `.ufo/waves/round-53/assimilation/guard-proof.txt`. Adopter map for admitted set: S134→S117, S185→S118, S186→S119, S193→S120, S195→S118 twin. Considerthese proposal 2 implemented as `weakness-streak.py` / `recurring.tsv` → `WEAKNESS_ROWS=2 FAILING=0`.
- **Waves.** W1: 49 seats; 49/49 results, no error field. Role mix: 18 scribe, 12 executor, 6 critic, 4 reviewer, 3 scout, 2 mutation-tester, 2 connector, 1 sentinel, 1 simplifier. W2: 43 seats dispatched; dispatch role mix: 16 executor, 10 critic, 5 reviewer, 4 scribe, 3 mutation-tester, 2 connector, 1 scout, 1 sentinel, 1 simplifier. **W2 WAVE-DONE/results had not arrived by the user's wrap directive; its seat outcomes and dead-seat count are unverified.** The W2 ready/dispatch artifacts are committed, but its reports/results remain unintegrated. This is an explicit round-completion/conformance limitation, not a pass.

## Landed changes

| commit | change | LOG |
|---|---|---|
| `a6ff732c70011f11c9beb681d832cedc6e75f566` | Frozen claims, counters, controls, before receipts and census start | `chousa-shokunin/LOG.md`, Round 53 |
| `32aab5edd70e43145cae72ec872278f3bc6efba7` | Adopter v4 candidate and self-test cases | same |
| `6365f15b64b89d1ad1ac66fe7d7b81c92e74d90f` | W1 spec/dispatch (49 seats) | same |
| `f4343163b70ce20e6b6d4f52b39935156e8afb26` | W1 integration: three entries, S117–S120, 63 spans, lesson, CJK polarity window/fixtures, anchored pointer check, C1 supplement, QUALITY 91–96, SKILL Gates, README and W1 reports | same |
| `934975ef4c38953f86dec51a738a2a63675d51d6` | W2 spec/dispatch (43 seats) | same |
| `d21eb285ea2f7efa17e38d2df4f92588ab23122d` | Final lane verdict, LOG, erratum, census end and W2-ready artifact | same |

## Before → after measurements

| claim | before | after | counting command | measured revision / verdict |
|---|---|---|---|---|
| R53-C1 operability | Base adopter `LEGS=1/8 C1=FAIL`; control scores 0–5/8 | Candidate `LEGS=8/8 C1=PASS` on three unseeded runs and `--seed 7`; after-state `SUPPLEMENT_LEGS=3/3`; forge `1/3` supplement | `python3 corpus/evidence/round53/c1-count.py`; post-freeze `python3 corpus/evidence/round53/c1-supplement.py` | candidate `32aab5ed`; **improved narrowly**. W1 `R53CritForgeC1` demonstrates the frozen counter remains forgeable on REAL, date-shape edge cases and the R50 selftest string check. The supplement is not the frozen claim rule (erratum E1). |
| R53-C2 depth | `ENTRIES=0/3 BOUND=0/5 C2=FAIL`; staged and mechanical-copy controls fail | `ENTRIES=3/3 BOUND=4/5 REFUSED=1 QUOTE_ROWS=63 CAPTURE_BOUND=63/63 ANCHOR_BOUND=4/4 INFERENCE_GROUNDED=3/3 QUARANTINE_VERDICTS=0/0 C2=PASS` | `python3 corpus/evidence/round53/c2-count.py` | W1 integration `f4343163`; **improved**, as presence/binding/located support; entailment remains a human review obligation. C2 also passes with the base inference-ground tool; the post-freeze polarity patch is disclosed in erratum E4. |

The operability score remains 3/10: that numeric scale is the round-1 archived-export observable, not this round's adopter counter. No other numeric expertise score is invented.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`.

- **Round start:** exit 0, `ok`, five pre-existing W04 (S051 S053 S073 S074 S075), `corpus/evidence/round53/census-start.txt`.
- **Round end:** exit 0, `ok`, the same five W04, `corpus/evidence/round53/census-end.txt`.
- **Rows:** 116 → 120; counting command `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`. Added by tier: A S117 and S120; B S118 and S119. Rows touched old→new: none; all four are append-only new rows.
- **Frontier:** four unique documents absent at the base (`5b550133`); S118's twin staged row does not earn a second-document credit. Coverage map advances the per-source tracking-record field set and the carrier distinction (notice proves release facts; PDF proves wording). No claim that a reporting standard or the 2019 regulator copy is primary was absorbed.
- **Assimilation:** one theme, “search-record instruments”; three entries from `merge/chousa/`, opened and re-grounded this round. Collision guard proof and renumber map above. S190 refused as a document with reason and flip in the lesson.
- **Quarantine:** 24 data rows in the lane's absent-defect slice; zero theme-URL rows, verified against 325 register rows under URL spelling variants. Counter `QUARANTINE_VERDICTS=0/0`; W1 found 18 rows lack a canonical verdict line in any lesson but none is unadjudicated; no theme row is affected.
- **considerthese:** `considerthese/2026-10-26.md` proposal 2 (recurring weakness streaks) implemented in `corpus/evidence/round53/weakness-streak.py` and `recurring.tsv`; the five-round forge-class streak is exposure, not itself a failure.
- **Sourced claim:** C2 rests on S117–S120, opened this round.

## Trend verdicts

- **expansion — improved.** Four unique, previously absent documents are bound; one staged twin is counted once. The JMLA entry moves the per-source/route fields frontier; S190 is refused and gets no credit.
- **quality — improved narrowly.** Three entries are re-grounded, staged quotes are re-cut to located spans, and the tool's named CJK polarity blind spot is fixed with a red-before fixture. The frozen C1 counter's forgeability and other limits are disclosed, not claimed closed. No earlier admitted entry received a full re-check this round.
- **discernment — unchanged pending non-author closure.** W2 seats are lane-dispatched authors; they are not the required outside spot-check. The round-52 non-author disagreement was converted to a lesson/QUALITY criterion, but this round's admit/reject gate still awaits a non-author re-open.

## SHONEN

- [~] Decision tables, error patterns, cited sources — `SKILL.md` Gates rows; `corpus/QUALITY.md` 91–96.
- [~] End-to-end task executed and logged — `LOG.md` Round 53; `corpus/evidence/round53/` receipts.
- [~] Instructions executable without oral context — commands in the round-53 Gates rows and counters.
- [~] Province fit — `PROVINCE.md`; lesson Gate narrows the regulator material and refuses S190 as a document.

## Round shape, stale lane, tooling, L0

**Shape:** two v1 waves, 49 + 43 = 92 dispatch seats; no residual call; L1 held the canonical planner seat (planner is not a validator role). W1 results: 49 seats, no errors. W2 results were unavailable at filing under the explicit wrap instruction; no dead-seat claim is made. **Stale-lane:** progressing through committed lane work; respawn-per-round, no other lane mission owned. **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed an unrelated untracked `.ufo/reports/round-52/mori.md`; it was not a chousa round-53 seat file and was untouched. No chousa seat misroot was found. **Tooling:** no persistent system tool install; pypdf 6.21.2 used ephemerally via `uv run --with pypdf` (PyPI) for independent offline PDF extraction. **L0:** `8d77e6c1` remains open; no new question appended.
