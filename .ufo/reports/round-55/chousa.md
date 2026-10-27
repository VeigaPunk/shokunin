# chousa — round 55 report

Lane: chousa-shokunin. Base `dba605deb5cd5ed4874e0e3c39ba24737409cd80` → final lane hash `53f1ce6b8a479c05c27436026557f05658929313` (`git -C chousa-shokunin ls-remote origin refs/heads/master` → `53f1ce6b…`). Freeze `1fc5d92b5a7866ec16f1cac2de749fccfa6b49cb`. No external fetch (L0 `8d77e6c1` open). The round was wrapped on the L1's request budget (operator notice): W1 had not settled at filing and W2 was not dispatched — see Work performed and Mistakes row 4.

## Work performed

Declared claims (frozen in `corpus/evidence/round55/claims.md`): **C1 operability** (lowest scored axis, capability acquisition — an OLE-aware span builder `tools/build-spans.py`); **C2 depth** (sourced — the NMPA grey-literature search-record field by document, rows S124–S126); **C3 calibration** (eleven lane statements round-54 W2 falsified, corrected by anchored errata a counter re-derives).

- Protocol load, r54 spot-check §6 intake, claim design, three frozen counters plus before/control receipts — freeze `1fc5d92b` (`corpus/evidence/round55/c{1,2,3}-count.py`, `controls/`).
- C1 candidate `6ca92499` (`tools/build-spans.py`); after-measurement `corpus/evidence/round55/c1-measure-after.txt` (`LEGS=4/4 C1=PASS` on `--seed 7` + three unseeded); 40/40 seed sweep `c1-seed-sweep-L1.txt`.
- C2: entry `corpus/knowledge/grey-literature-and-chinese-search-record-r40.md`, rows S124–S126 (`corpus/SOURCES.md:134-136`), 19 quotes built by the C1 builder (`corpus/evidence/round55/quotes.tsv`, `spans.tsv`), lesson Gate + quarantine verdict (`corpus/lessons/round-55.md`); `c2-measure-after.txt` `C2=PASS` — commit `5a35ebd6`.
- C3: `SCORECARD.md` "Round 55 statement errata" E01–E11; r36 `#### Corrections (round 55)`; QUALITY 101; lesson `## Corrections`; `c3-measure-after.txt` `ERRATA=11/11 C3=PASS` — commit `5a35ebd6`.
- Routed/integration: r37 corrections (3 further W2 findings) and `recurring.tsv` — `29cfb12a`; QUALITY 102–105; `wave-settled-check.py` (round 54 → `UNSETTLED w2`, exit 1); successors of the round-54 ledger and PDF checks with W2 attacks as failing fixtures (`considerthese-ledger-check.txt`, `pdf-crosscheck.txt`); W04 adjudicated (no change); SKILL rows `build-spans` + round-55 counters; README Round55 section — `5a35ebd6`.
- Round shape: **one v1 wave, W1 = 48 seats** (executor 11, scribe 14, critic 7, reviewer 5, mutation-tester 4, scout 3, connector 2, sentinel 1, simplifier 1; attack share 33%), dispatched (`w1.ready.dispatched`); **35/48 reports at filing, 13 still running** (DraftC3Fixes, DraftEntry, DraftRows, ExecC1Seeds, GroundMedsci, GroundNmpaEn, MutC1Builder, MutC2Counter, MutC3Counter, RegisterW2A, ScoutFrontier, SentC1, SimplifyBuilder); no `w1-results.json` yet. **W2 (36 falsify items, `w2-spec.json`) prepared, never dispatched.** Round total 48 seats — **below the 64 floor (conformance defect)**. No residual call. Planner seat held by the L1. Dead seats: none known (results file absent).
- Final summary sweep: 3 claims; L0 questions: none new.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: claims, counters, controls, census start, assimilation scratch | LOG "Round 55" | `1fc5d92b` |
| C1 candidate `tools/build-spans.py` | same | `6ca92499` |
| W1 spec/dispatch | same | `d5018747` |
| W1 integration: C2 entry/rows/spans/lesson, C3 errata + corrections, QUALITY 101–105, checks, SKILL/README | same | `5a35ebd6` |
| r37 corrections, recurring table | same | `29cfb12a` |
| SCORECARD verdict + capability row, LOG, lesson row 4, census end, measurements, 35 W1 reports, W2 spec | same | `53f1ce6b` |

## Before → after measurements

- **C1** `python3 corpus/evidence/round55/c1-count.py` — before (tool absent at base) `LEGS=0/4 C1=FAIL` ×4 (`controls/c1-before.txt`); controls R54SHIM 1/4, TXTONLY 1/4, DELEGATE 0/4 → after `LEGS=4/4 C1=PASS` ×4, measured at `6ca92499` (tool sha256 `1ed2650a…`).
- **C2** `python3 corpus/evidence/round55/c2-count.py` — before `ENTRIES=0/1 BOUND=0/3 C2=FAIL`; STAGED/REWRITE controls FAIL → after `BOUND=3/3 QUOTE_ROWS=19 CAPTURE_BOUND=19/19 ANCHOR_BOUND=3/3 QUARANTINE_VERDICTS=1/1 C2=PASS`, measured at `29cfb12a` (`c2-measure-after.txt`); re-run at `53f1ce6b` `C2=PASS`.
- **C3** `python3 corpus/evidence/round55/c3-count.py` — before `ERRATA=0/11`; RESTATE `WRONG=11`, PARAPHRASE `ANCHOR=11` → after `ERRATA=11/11 C3=PASS`, measured at `29cfb12a` (`c3-measure-after.txt`).

## Sources & frontier

SOURCES rows 123 → 126 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`); added S124 (B), S125 (B), S126 (A); no row touched (S113, S070 unchanged). Census start/end `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa` exit 0, five pre-existing W04 (adjudicated, kept) — `census-start.txt`, `census-end.txt`. Assimilation: theme = NMPA grey-literature field; staged r40 admitted narrowed (S130→S124, S131→S125, S143→S126; S133 = held S113, not cited); r43 refused; collisions 42, guard proven (`.ufo/waves/round-55/assimilation/`); register S125 (round6) `absent-as-written`. Frontier advanced: regulator search-record field; `.doc` captures end to end to spans; the 2019 NMPA notice (S126). considerthese: swept, none new (ledger `BAD=0`). Mined mistakes: lesson rows 1–4.

## Trend verdicts

- **expansion — improved**: three documents absent at base bound to one admitted entry (`git grep -c 是否检索灰色文献 dba605de -- corpus/knowledge` → exit 1).
- **quality — improved**: spans now taken from defined forms (C1); r36/r37 and QUALITY 97/98 corrected by appended errata; round-54 checks hardened.
- **discernment — unprovable-but-better** pending the non-author closure: C3 errata are counter-recomputed, quarantine verdict and r43 refusal recorded, but the falsify wave did not run.

Stale-lane: respawn-per-round driver; no other mission of this lane open. Tool installs: none (pypdf 6.21.2 via `uv run --with`, uv cache, no PATH install).

## SHONEN

- [~] Craft rows: SKILL.md `build-spans` and round-55 counter registry rows; QUALITY 101–105 (`chousa-shokunin/SKILL.md:142-143`, `corpus/QUALITY.md:945-953`).
- [~] Logged rounds: LOG.md "Round 55" with `c1-measure-after.txt`, `c2-measure-after.txt`, `c3-measure-after.txt`.
- [~] Runnable checks: `c1/c2/c3-count.py`, `wave-settled-check.py`, `considerthese-ledger-check.py`, `pdf-crosscheck.py` with receipts under `corpus/evidence/round55/`.
- [~] Province fit: adjacency of drug-safety practice reported, not absorbed (`corpus/knowledge/grey-literature-and-chinese-search-record-r40.md` Unknown; W1 `R55ReviewProvinceC2`).
