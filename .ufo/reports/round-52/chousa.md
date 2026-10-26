# chousa — round 52

## Work performed

Declared claims, frozen at lane commit `37468eadd8d098e80289b2f31a22de3872d4a1f6` (`corpus/evidence/round52/claims.md`) after their do-nothing controls were scored:
**R52-C1 operability** (lowest scored axis, 3/10; capability acquisition, plumbing): `tools/capture-text.py` prints the text form of an OOXML `.docx` capture and locates a quote's offset in it; counted by a nonce counter that generates every package, member and file name at counting time.
**R52-C2 depth** (sourced, ground; the section-10 search-record theme continued): three lane entries on four documents adopted by document, including the NIPH `.docx` round 51 refused for its capture form.

- C1: candidate `804a4537`, hardened after W1/W2 (`e769c037`, `643ac77b`; erratum E2). `python3 corpus/evidence/round52/c1-count.py`: base `LEGS=0/9` → `LEGS=9/9 C1=PASS` (three runs, `--seed 7`); controls naive 4/9, cache-txt 0/9, const 0/9 (`controls/c1-before.txt`).
- C2: entries `corpus/knowledge/japanese-search-record-niph-form-r52.md`, `japanese-prisma-item-wording-r40.md`, `chinese-prisma-s-reception-r52.md`; rows S113–S116 (staged S111 S112 S125 S129 by document). `python3 corpus/evidence/round52/c2-count.py`: `ENTRIES=0/3 BOUND=0/4 C2=FAIL` → `BOUND=4/4 QUOTE_ROWS=39 CAPTURE_BOUND=39/39 ANCHOR_BOUND=4/4 INFERENCE_GROUNDED=3/3 QUARANTINE_VERDICTS=1/1 C2=PASS`.
- **Findings that changed the work:** (1) W1 `R52CritForgeC1` passed the frozen C1 counter 9/9 with an 85-line regex forge keyed to the generators' XML spelling (`controls/forge-shape.py`); the post-freeze `c1-supplement.py` (re-spelled XML, pinned NIPH text digest) passes the tool 4/4 and fails the forge 0/4 — and W2 `R52W2CritForgeSupplement` passed both with a 54-line regex tool plus a memoised NIPH text; (2) the candidate accepted `.xlsx` and an OLE-embedded zip with an empty form, rendered a 525 KB package into 60 M characters, and crashed on encrypted or corrupt members — all now refused (`corpus/lessons/round-52.md` Mistakes 5, 6; erratum E2); (3) round 51's S120 verdict offset `char 39411` is an offset of nothing in its stated XML form; re-located as 8996 in the capture-text form (Mistakes 2); (4) the 梅斯医学 record (S113) is a second carrier of an article the lane holds — no expansion credit; (5) W2 entailment attacks narrowed bullets in all three entries and the S113 row (erratum E5).
- Routed round-51 defects: 1 and 3 done; 2 (adopter twin-id) and 4 (anchored corrections) built in scratch by W1 seats and planned, not landed; 5 already in the round-51 Gates row (lesson `## Spot-check intake`).

## Landed changes

| commit | change | LOG |
|---|---|---|
| `37468ead` | frozen claims, counters, span builder, controls, before receipts, census start | `LOG.md` Round 52 |
| `804a4537` | C1 candidate `tools/capture-text.py` | same |
| `13bc2806` | wave-1 spec and dispatch (45 seats) | same |
| `01c17ce3` | W1 integration: tool hardening, C1 supplement, entries, S113–S116, spans, lesson, QUALITY 87–90, README, SKILL Gates rows, verdict-gap, erratum | same |
| `e769c037` | W1 reports and results; encrypted/percent-encoded/empty-locate fixes | same |
| `d1d972cf` | wave-2 spec and dispatch (38 seats) | same |
| `643ac77b` | post-W2: entries narrowed, corrupt-stream and size-lie refusals, search log, SCORECARD verdict, LOG | same |
| `1a170f55` | after-measurement receipt `corpus/evidence/round52/measure-after.txt` (`tool-rev:` header; `receipt-check.py` → `RECEIPT_CHECK=PASS`) | same |
| `f80a9a255908389992faa6daa495fc6b9276af15` | wave-2 reports and results (lane tip; `git ls-remote origin refs/heads/master` prints this hash) | same |

## Before → after measurements

Measured at the lane working tree of `643ac77b` (receipt `corpus/evidence/round52/measure-after.txt`); later commits add only the receipt and wave-2 reports.

| claim | before | after | command | verdict |
|---|---|---|---|---|
| C1 operability | tool absent `LEGS=0/9 C1=FAIL` (base `00f8c7f5`) | `LEGS=9/9 C1=PASS` ×3 and `--seed 7`; supplement `SUPPLEMENT_LEGS=4/4` (forge-shape 9/9 frozen, 0/4 supplement) | `python3 corpus/evidence/round52/c1-count.py`; `…/c1-supplement.py` | **Improved narrowly**: the frozen counter is forgeable by XML spelling, the supplement is post-freeze and itself passable by a regex tool with a memoised text, and the post-candidate refusals are measured by no frozen leg. |
| C2 depth | `ENTRIES=0/3 BOUND=0/4 C2=FAIL` | `BOUND=4/4 … C2=PASS` (also `--lane-only`) | `python3 corpus/evidence/round52/c2-count.py` | **Improved**, as presence and binding; entailment is uncounted and the CJK polarity check is inert on these entries (W2 `R52W2ExecInfRegression`). |

## Sources & frontier

Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`.

- **Round start:** exit 0, `ok`, five pre-existing W04 (S051 S053 S073 S074 S075) — `corpus/evidence/round52/census-start.txt`.
- **Round end:** exit 0, `ok`, the same five W04 (`measure-after.txt`).
- **Rows:** 112 → 116 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Added by tier: A S114 S115; B S113 S116. Rows touched old → new: none (S113's teaches cell was narrowed inside the round that wrote it, erratum E5). Search log: Round 52 note.
- **Frontier:** the theme's three credited documents were absent at base (`git grep -l -e 文献検索期間 -e 完全な検索戦略 -e 检索报告清单 00f8c7f5… -- corpus/knowledge` → exit 1); a new capture form (OOXML) is readable.
- **Assimilation:** theme "Japanese/Chinese search records" continued from `merge/chousa/` (section 10). Collision check: 31 collisions S082–S112, guard proved on an indented-row fixture (`.ufo/waves/round-52/assimilation/guard-proof.txt`); renumber by document S111→S113, S112→S114, S125→S115, S129→S116; admitted three entries (narrowed), refused or deferred five neighbours with reason and flip in the lesson Gate. Quarantine slice: 24 rows, one on a theme URL (S120), verdict `present` at chars 8996/9020/9428.
- **considerthese:** `considerthese/2026-10-26.md` proposal 3 (lane-vs-verifier verdict gap) implemented as `corpus/evidence/round52/verdict-gap.py` (`VERDICT_GAPS=2 UNPARSED=1`).
Open operator items: 8d77e6c1 since round 42 (10 rounds)
- **Freshness:** newest readable capture 2026-10-24; no fetch (L0 `8d77e6c1`).
- **Mined mistakes:** six in `corpus/lessons/round-52.md` `## Mistakes` (five with a check shown able to fail).
- **Sourced claim:** C2 rests on S113–S116, all opened this round.

## Trend verdicts

- **expansion — improved narrowly.** Three documents on ground the base did not hold; one bound document (S113) earns no credit as a second carrier; a capability row (OOXML capture text form).
- **quality — improved.** Wave 2 narrowed entries and a row before landing; the tool's refusal contract now covers non-Word, inflated, encrypted and corrupt packages; the counters' weaknesses (shape forge, supplement forge, CJK polarity) are reported, not repaired.
- **discernment — unchanged pending closure.** Every seat was dispatched by this lane. The closure should re-open the NIPH entry (section 3.1 at 8996; section 7 at 19496), the S113 no-credit judgment (梅斯医学 vs SinoMed `.txt`), and reject `search-log-fields-r36` (265-character challenge page).

## SHONEN

- [~] Decision tables, error patterns, cited sources — `SKILL.md` Gates rows `capture-text` and `chousa round-52 counters and checks`; `corpus/QUALITY.md` 87–90.
- [~] End-to-end task executed and logged — `LOG.md` Round 52; `corpus/evidence/round52/measure-after.txt`.
- [~] Instructions executable without oral context — `python3 tools/capture-text.py <raw> --locate '<quote>'`; `corpus/evidence/round52/c1-count.py` docstring.
- [~] Province fit — `PROVINCE.md`; W1 `R52ReviewProvince` (in province, HTA content not absorbed), W1 `R52ConnSiblings` and W2 `R52W2ConnSiblingsFinal` (no overlap).

## Round shape, stale lane, tooling, L0

**Shape:** two v1 waves via the inline handoff, 45 + 38 = 83 seats; no residual call; the L1 held the planner seat (no planner role in the validator). Filed after WAVE-DONE of both waves.
- **W1 (45):** scribe 17, executor 11, critic 5, reviewer 3, scout 3, mutation-tester 2, connector 2, sentinel 1, simplifier 1.
- **W2 (38):** critic 10, reviewer 9, executor 8, mutation-tester 3, scribe 3, connector 2, scout 2, sentinel 1.
- **Dead seats:** none — `w1-results.json` 45 entries and `w2-results.json` 38 entries carry no error status; 45 and 38 report files on disk.

**Misroot sweep:** W1 `R52MutBuildSpans` wrote `p.out` (62 B) and `p.err` (0 B) at the fleet root (20:10:49); the orchestrator moved them to `.tower/quarantine/fleet-root-strays-20261026T2010/` before the sweep; recorded as lesson Mistakes row 4. `git -C /home/vgpnk/Projects/shokunin status --porcelain` at report time: empty (nothing of this lane at the fleet root). Lane-root strays: four control-output files (`forge.out`, `naive.out`, `sup-forge.out`, `sup-naive.out`, 1,046 bytes, supplement/counter outputs) written into the lane root by a W2 seat with relative redirects (their names appear in the reports of `R52W2DraftLogEntry`, `R52W2DraftReportSections` and `R52W2DraftScorecardVerdict`); never committed, removed by the L1 before filing; the same class as lesson Mistakes row 4.

**Stale-lane:** launched 19:51 -03; progressing with lane commits throughout (respawn-per-round driver; no other mission of this lane open). **Tool installs:** none. **L0:** `8d77e6c1` still open; no new question appended.
