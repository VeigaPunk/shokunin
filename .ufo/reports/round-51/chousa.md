# chousa — round 51

## Work performed

Declared claims, frozen at lane commit `d603f6f00f78d64f123d3aed2dd9f8701547a4ba` (`corpus/evidence/round51/claims.md`) after their do-nothing controls were scored:
**R51-C1 operability** (lowest scored axis, 3/10; capability extension, plumbing): `tools/assimilate-rows.py` cites only header `source:` ids, per entry, with refusals and body-only listing; counted by a nonce counter that generates its packages at counting time.
**R51-C2 depth** (sourced, ground; the assimilation theme): "what a Japanese or a Chinese systematic-review search record must carry" adopted by document as three entries on six documents.
**R51-C3 calibration** (plumbing): every repo-path pointer in SCORECARD capability rows and SHONEN evidence lines resolves.

- C1: adopter v3 at `41b4dca86fc86dd2f50df17dd779acb3379e8275` (v1 `2a3389da`, v2 `cf642c66`, then fixes after the wave-1 `R51ReviewAdopterCode` and wave-2 `R51W2ReviewToolV2` reviews). Frozen counter `python3 corpus/evidence/round51/c1-count.py`: lane tool at base `LEGS=1/5 C1=FAIL` (`controls/c1-lane-before.txt`) → `LEGS=5/5 C1=PASS`. Controls (`controls/c1-before.txt`): base tool 1/5, echo 2/5, const 1/5, flag-noop 2/5.
- C2: entries `corpus/knowledge/japanese-search-record-r38.md`, `chinese-search-record-r39.md`, `japanese-search-record-r38-amendment-2026-10-23.md`; rows S107–S112 (staged S109 S110 S116 S117 S119 S126, by document); staged S125 (a `.docx`) refused. `python3 corpus/evidence/round51/c2-count.py`: `ENTRIES=0/3 BOUND=0/7 C2=FAIL` (`controls/c2-before.txt`) → `BOUND=6/7 REFUSED=1 QUOTE_ROWS=70 CAPTURE_BOUND=70/70 ANCHOR_BOUND=6/6 INFERENCE_GROUNDED=3/3 QUARANTINE_VERDICTS=6/6 C2=PASS`.
- C3: `python3 corpus/evidence/round51/c3-count.py`: `DANGLING=5 C3=FAIL` → `DANGLING=0 C3=PASS` (four append-only `correction:` lines at the end of `SCORECARD.md`, one `SHONEN.md:10` path).
- **Findings that changed the work:** (1) the frozen C1 counter is forgeable — a 94-line tool keyed on its fixed directory names passes `LEGS=5/5` (wave 1 `R51CritForgeC1`, `corpus/evidence/round51/controls/forge-dirname.py`); the post-freeze `c1-supplement.py` (ten legs, random directory and entry names) passes the real tool 10/10 and fails that forge 1/10, the wave-2 forge-dual 3/10 and the first candidate 3/10 (`controls/c1-supplement-controls.txt`); (2) the NIPH `.docx` has no text form the frozen span pipeline reads (`.txt` is the zip with 72117 U+FFFD) so it is refused for capture form, not source quality; (3) all three staged entries carried claims their captures do not support (a negated "not restated in the checklist body" that item 7's cell reverses, `表3` that is 表1, a comment-only `学科分类号`, "peer-reviewed", a searcher conclusion from a four-token sweep) — narrowed after wave 2 (lesson Mistakes row 9); (4) the first C3 run printed 8 because its tokenizer stripped a leading dot (erratum E1, found before any seat existed).
- Round-50 routed defects: pinned receipt (`measure-after.txt` with a `tool-rev:` header, `receipt-check.py` → `RECEIPT_OK`; the round-50 receipt re-measured at its tip in `measure-r50-at-tip.txt`, four of thirteen blocks), nonce counter, unique seat names (`NAME_COLLISIONS=0` on both specs), filename-drift correction in `corpus/README.md`.

## Landed changes

| commit | change | LOG |
|---|---|---|
| `d603f6f0` | frozen claims, counters, controls, before receipts | `LOG.md` Round 51 |
| `2a3389da` / `cf642c66` | adopter candidate and v2, fixtures | same |
| `75a9406a` `cfe6c9fb` | wave-1 spec and dispatch (48 seats); C3 extractor erratum E1 | same |
| `4436e279` | C2 adoption (three entries, S107–S112, manifest, lesson), QUALITY 81–86, SKILL Gates rows, README blocks, receipt and open-items checks | same |
| `72566c84` | wave-2 spec and dispatch (41 seats) | same |
| `41b4dca8` | post-W2: adopter v3, supplement v2, receipt-check, entries/row/README/QUALITY/lesson narrowed, errata E2–E5 | same |
| `871c0d79` | LOG, SCORECARD verdict, SKILL `tool-rev` pin, after-measurement | same |
| `a84edcf960caec156251e5d9843afecf9ad870f4` | wave-2 reports and results, README wording (lane tip; `git ls-remote origin refs/heads/master` prints this hash) | same |

## Before → after measurements

Measured at the lane working tree of `871c0d79` (receipt `corpus/evidence/round51/measure-after.txt`, header `tool-rev: 41b4dca8…`; `receipt-check.py` → `RECEIPT_OK`, `SKILL_PIN_OK`); the later commit adds only wave-2 reports and one README sentence (C2/C3 re-run after it: pass).

| claim | before | after | command | verdict |
|---|---|---|---|---|
| C1 operability | lane tool at base `LEGS=1/5 C1=FAIL` | `LEGS=5/5 C1=PASS` (also `--seed 7`); supplement `SUPPLEMENT_LEGS=10/10` | `python3 corpus/evidence/round51/c1-count.py`; `…/c1-supplement.py` | **Improved narrowly.** The frozen counter is forgeable; the supplement is post-freeze and a tool that reimplements the adopter passes both; the round-49/50 one-shot counters fail at the new default (round-49 passes with `ASSIMILATE_CITES=all`; round-50 cannot reach 5/5). |
| C2 depth | `ENTRIES=0/3 BOUND=0/7 C2=FAIL` | `BOUND=6/7 REFUSED=1 … C2=PASS` (also `--lane-only`) | `python3 corpus/evidence/round51/c2-count.py` | **Improved**, as presence and binding; entailment is uncounted (wave 2 found 30+ prose overstatements, narrowed). |
| C3 calibration | `CAP_ROWS=36 POINTERS=74 DANGLING=5 C3=FAIL` (first run 8, E1) | `DANGLING=0 C3=PASS` | `python3 corpus/evidence/round51/c3-count.py` | **Improved narrowly**: existence, not truth; wave 2 found eleven routes that print PASS without a content repair. |

Open defects named, not fixed: adopter twin-id `held` label and refusal ordering (W2 `R51W2ReviewToolV2` F5/F6); C3 reads corrections in any order and only for SCORECARD rows; the frozen C1 counter's hang and ambient-env sensitivity (E2/E3).

## Sources & frontier

Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`.

- **Round start:** exit 0, `ok`, five pre-existing W04 (S051, S053, S073, S074, S075) — `corpus/evidence/round51/census-start.txt`.
- **Round end:** exit 0, `ok`, the same five W04 (`measure-after.txt`).
- **Rows:** 106 → 112 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Tiers: A 93 → 98, B 8 → 9, C 5 → 5. Added by tier: A S107 S108 S109 S110 S112; B S111. Rows touched old → new: none (S107's source cell was corrected inside the round that wrote it, W2 `R51W2ReopenRowS107`).
- **Frontier:** the theme was absent at base (`git grep -l -e 検索式 -e 検索期間 -e 检索策略 9ec1751a…` finds nothing in `corpus/knowledge`); six documents, per-document credit (README block).
- **Assimilation:** theme "Japanese/Chinese search records" from `merge/chousa/` (section 10). Collision check: 25 collisions S082–S106 (31 against the landed registry), guard proved on an indented-row fixture (`.ufo/waves/round-51/assimilation/guard-proof.txt`); renumber by document S109→S107, S110→S108, S116→S109, S117→S110, S119→S111, S126→S112, S125 refused. Admitted three entries (narrowed); rejected or deferred seven neighbouring entries with reason and flip in the lesson Gate (`search-log-fields-r36` refused: its PRISMA-S capture is a challenge page). Quarantine slice: six rows on theme URLs hand-checked (2 present, 4 absent-as-written, none blocks).
- **considerthese:** `considerthese/2026-10-25.md` — the still-open "waiting on you" age proposal implemented as `open-items-age.py` (below).
Open operator items: 8d77e6c1 since round 42 (9 rounds)
- **Freshness:** newest readable capture 2026-10-24 (qcache); no fetch (L0 8d77e6c1).
- **Mined mistakes:** nine in `corpus/lessons/round-51.md` `## Mistakes`.
- **Sourced claim:** C2 rests on S107–S112, all opened this round.

## Trend verdicts

- **expansion — improved narrowly.** Six documents on ground the lane did not hold; per-document, not per-entry credit; one document refused.
- **quality — improved.** Wave 2 found and the lane applied 30+ narrowings to the entries, the registry row and the lesson; two tool defects fixed (N1–N5); the counters' weaknesses (forgeable C1, existence-only C3, uncounted entailment) are reported, not repaired.
- **discernment — unchanged pending closure.** Every seat was dispatched by this lane. The closure should re-open `chinese-search-record-r39.md` (S111 comment-only `学科分类号`), `japanese-search-record-r38.md` (footer 122 vs staged p.121) and the refused `.docx`, and sample `search-log-fields-r36` as the reject.

## SHONEN

- [~] Decision tables, error patterns, cited sources — `SKILL.md` Gates rows `assimilate-rows` and `chousa round-51 counters and checks`; `corpus/QUALITY.md` 81–86.
- [~] End-to-end task executed and logged — `LOG.md` Round 51; `corpus/evidence/round51/measure-after.txt`.
- [~] Instructions executable without oral context — `python3 tools/assimilate-rows.py --selftest`; `corpus/evidence/round51/c1-count.py` docstring.
- [~] Province fit — `PROVINCE.md`; W2 `R51W2ReviewEntryJa`, `R51W2ReviewEntryZh`, `R51W2ReviewEntryJa2` (all in province, admit-with-narrowing), `R51W2ConnSiblingsFinal` (no overlap).

## Round shape, stale lane, tooling, L0

**Shape:** two v1 waves via the inline handoff, 48 + 41 = 89 seats; no residual call; the L1 held the planner seat. Filed after WAVE-DONE of both waves.
- **W1 (48):** scribe 22, executor 12, critic 4, scout 3, reviewer 2, connector 2, mutation-tester 1, sentinel 1, simplifier 1.
- **W2 (41):** reviewer 12, critic 10, executor 8, mutation-tester 3, scribe 3, connector 2, scout 2, sentinel 1; two seats (`R51W2ExecReplayAll`, `R51W2MutSupplement`) have a second report file (`-2`) from a resumed identity.
- **Dead seats:** none reported by the results files (`w1-results.json`, `w2-results.json` carry no error status); `wave-complete-check.py` → `OK 48/48` and `OK 41/41`. Seat violations: one W1 seat wrote `corpus/evidence/round51/zero.txt` into the lane through a symlinked scratch root (removed; W1 `R51SentScope`); a W1 seat edited its report late (committed).

**Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only other lanes' untracked paths (`.tower/`, `.ufo/reports/round-41/mado.md`, `.ufo/waves/round-30/`, `demo-cwd.txt`) and operator state; none names chousa; nothing touched.

**Stale-lane:** launched 19:46 -03; progressing with lane commits throughout. **Tool installs:** none. **L0:** `8d77e6c1` still open; no new question appended.
