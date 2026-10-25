# chousa — round 50

## Work performed

Declared claims, frozen at lane commit `6a068f2ae4847a1e4aa959f088a39ddc1b167bc0` (`corpus/evidence/round50/claims.md`) after their do-nothing controls were scored:
**R50-C1 operability** (the lowest scored axis, 3/10; capability extension, plumbing): `tools/assimilate-rows.py --selftest`, a hand-expected fixture self-test scored on six perturbed copies against echo and constant controls.
**R50-C2 depth** (sourced, ground; the assimilation theme): "what a Chinese citation-checking feature compares, and which CNKI manuals document it" adopted by document as three entries.

- C1 candidate `ec52e632`; hardened after W1 at `2573dc16` (multiset compare, work floor, option clash, dash for id-less entries, timeout, tab-free findings; `used-by` across twin staged ids). `python3 corpus/evidence/round50/c1-count.py` → `LEGS=5/5 C1=PASS` (`corpus/evidence/round50/measure-after.txt`). Controls: base tool `LEGS=2/5`, echo `4/5`, constant `2/5` (`controls/c1-before.txt`).
- C2 adoption `74794db0`, then narrowed after W2 in the final commit `1d7aba09`: `corpus/knowledge/cnki-citation-check-r40.md`, `citation-matching-semantics-r41.md`, `istic-citation-verification-r39.md`; rows S104–S106; the CNKI 教师 manual refused; 67 located quotes (`spans.tsv`). `c2-count.py` → `BOUND=3/4 REFUSED=1 … CAPTURE_BOUND=67/67 SUBSTANCE=PASS INFERENCE_GROUNDED=3/3 C2=PASS`.
- Findings that changed the work: the staged "amber" is the PDF's 橙色 (W1 `GroundSxuStates`, `w1/` and my own render of PDF page 43); the §6.1 hover screenshots name three compared parts (篇名, 作者, 刊名), which a text-form sweep cannot see (W2 `R50CritEntryR41`; I rendered the page and read them); the ISTIC page's reuse concession is for 中国科学院 users and its review/archive steps are the retrieval officer's.
- Post-freeze changes (all outside the frozen counters, disclosed in `claims-erratum.md` with the wave-2 corrections to it): the two tool changes above and `tools/inference-ground.py` `has_two_words` (four CJK characters; before it a correctly grounded pure-Chinese bullet read as zero tokens — round-46/47/48 counters output-identical); a frozen control script edit (the builder no longer copies the landed manifest).
- Round-49 routed defects: late seat reports committed (`4d13657e`, `ec52e632`, `2573dc16`); stale 28 → 31 counts corrected by append-only `correction:` lines and checked (`stale-count-check.py` exit 1 → 0, `stale-count-before.txt`/`-after.txt`); decode form named next to offsets (QUALITY 76); self-test and digest pin (QUALITY 73); report filed after WAVE-DONE of both waves.
- **Honest limits found by my own wave 2**: the frozen C1 counter is replayable — a 42-line forge prints the six literal DIFF lines and passes `LEGS=5/5` (`controls/forge-tool.py`); the supplementary, post-freeze `c1-supplement.py` passes the real tool 5/5 and fails the forge 1/5, echo 2/5, constant 0/5, base 1/5 (`c1-supplement-receipt.txt`). The C2 counter measures binding and presence, not entailment (boilerplate quotes and polarity-inverted bullets pass it: W2 `R50CritForgeC2`, `R50ExecInfLanded`); the CJK polarity rule is unreachable (named limit, QUALITY 79); a mechanical adoption binds every registry leg once `used-by` is widened (`controls/c2-controls-at-landing.txt`: TOOLED `BOUND=4/4`, still `C2=FAIL`).

## Landed changes

| commit | change | LOG |
|---|---|---|
| `6a068f2a` | frozen claims, counters, pinned fixtures, controls and before receipts | `LOG.md` Round 50 |
| `ec52e632` | `--selftest` and default fixtures (C1 candidate); late round-49 reports | same |
| `77541727` | wave-1 spec and validated dispatch | same |
| `2573dc16` | selftest hardening, `used-by` widening, W1 seat reports | same |
| `74794db0` | C2 adoption (entries, S104–S106, quotes, lesson, QUALITY 73–79, SKILL rows), CJK fix, checks and receipts | same |
| `c5b8dca8` | wave-2 spec and validated dispatch | same |
| `1d7aba0948cf62f6158f77e220f64320a5b6c6cc` | W2 narrowing of the three entries, `c1-supplement.py`, hardened checks, erratum, QUALITY 80, LOG, SCORECARD, final measurement, W2 seat reports (lane tip; `git ls-remote origin refs/heads/master` prints this hash) | same |

## Before → after measurements

Measured at lane tip `1d7aba09` (`corpus/evidence/round50/measure-after.txt`; the tracked tree equals the commit: `jj-lane.sh state` → `local=remote=1d7aba09 ahead=0 behind=0`, no untracked).

| claim | before | after | command | verdict |
|---|---|---|---|---|
| C1 operability | base tool `BASELINE=FAIL rc=2 LEGS=2/5 C1=FAIL` exit 1; echo control `PERTURB_PASS=0/6 LEGS=4/5`; constant `LEGS=2/5` | `LEGS=5/5 PERTURB_PASS=6/6 C1=PASS` exit 0; supplement `C1_SUPPLEMENT=PASS` 5/5 | `python3 corpus/evidence/round50/c1-count.py` | **Improved narrowly.** Conformance on pinned fixtures; the frozen counter is replayable (forge passes it) and the supplement is post-freeze. |
| C2 depth | `ENTRIES=0/3 BOUND=0/4 NEW_GROUND=0/3 C2=FAIL` exit 1; staged copy `REF_ID_UNBOUND=15 C2=FAIL` | `BOUND=3/4 REFUSED=1 NEW_GROUND=3/3 QUOTE_ROWS=67 CAPTURE_BOUND=67/67 ANCHOR_BOUND=3/3 INFERENCE_GROUNDED=3/3 C2=PASS` exit 0 (also `--lane-only`) | `python3 corpus/evidence/round50/c2-count.py` | **Improved**, as presence and binding; entailment is the closure's. |

## Sources & frontier

Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`.

- **Round start:** exit 0, `ok`, five pre-existing W04 warnings (S051, S053, S073, S074, S075).
- **Round end:** exit 0, `ok`, the same five W04 (`measure-after.txt`).
- **Rows:** 103 → 106 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Tiers A 92→93, B 6→8, C 5→5; mined 79→82, queued 19, rejected 5. Added by tier: A S104; B S105, S106. Rows touched old→new: none.
- **Frontier:** three entries on ground the lane did not hold (`git grep -e 引文核对 -e 引证检索 3c51da77 -- corpus/knowledge` finds nothing); expansion credit is per document (three), not per entry (W2 `R50CritTheme`: r40 and r41 both rest on one PDF).
- **Assimilation:** theme "Chinese citation-checking features" from `merge/chousa/`. Section-10 collision check: 22 collisions (S082–S103; 25 against the landed registry), guard proved on an indented-row fixture (`assimilation/guard-proof.txt`); renumber by document: S118→S104, S124/S135→S105, S136→S106, S145 refused. Admitted three entries; rejected or deferred r42, r43, r46, r47, r48 and the 教师 document, each with reason and flip in the lesson Gate. Quarantine slice: 24 rows, 0 on the theme URLs (the counter's `QUARANTINE_VERDICTS=0/0` is vacuous; the record is the sweep).
- **considerthese:** `considerthese/2026-10-25.md` — the capture-age proposal was mined in round 49 (QUALITY 71); the rest concern the reflection's own format; nothing left to mine.
- **Freshness:** Freshness: newest readable capture 2026-10-24 23:26 -03 (qcache); this round's captures 2026-10-23; no fetch (L0 8d77e6c1).
- **Mined mistakes:** eight, in the lesson's `## Mistakes`.
- **Sourced claim:** C2 rests on S104–S106, all opened this round.

## Trend verdicts

- **expansion — improved narrowly.** Three documents on new coverage ground (S104–S106); r40/r41 share one PDF, so the entry count overstates it.
- **quality — improved.** W2 found and the lane applied 30+ narrowing corrections to the admitted entries, four checks were each shown able to fail, two tool defects fixed. Post-freeze changes are disclosed; the frozen counter's replay weakness and the unreachable CJK polarity rule are reported, not repaired.
- **discernment — unchanged pending closure.** Every seat was dispatched by this lane, so none is a non-author. The closure should re-open the S105 hover screenshots (PDF page 43), the refused 教师 document, and the r39 reuse-scope narrowing.

## SHONEN

- [~] Decision tables, error patterns, cited sources — `SKILL.md` Gates rows `assimilate-rows` and `chousa round-50 counters and checks`; `corpus/QUALITY.md` 73–80.
- [~] End-to-end task executed and logged — `LOG.md` Round 50; `corpus/evidence/round50/measure-after.txt`.
- [~] Instructions executable without oral context — `python3 tools/assimilate-rows.py --selftest`; `corpus/evidence/round50/c1-count.py` docstring.
- [~] Province fit — `PROVINCE.md`; W2 `R50ReviewProvince` (all three in province; three generic ISTIC bullets cut), `R50ConnSiblings` (no overlap).

## Round shape, stale lane, tooling, L0

**Shape:** two v1 waves via the inline handoff, 42 + 43 = 85 seats; no residual call. L1 held the planner seat.
- **W1 (42):** scribe 18, executor 10, critic 4, reviewer 3, mutation-tester 2, connector 2, scout 2, simplifier 1.
- **W2 (43):** reviewer 9, critic 9, executor 7, scout 6, mutation-tester 6, scribe 3, connector 2, simplifier 1.
- **Dead/misdirected seats (W1, 13):** MineConsider, ExecMirrorCensus, ExecInfStaged, ExecReplayC1, ExecFormProbe, CritForgeC1, CritForgeC2, ReviewProvince, ReviewQuarMap, CritTheme, ConnSiblings, ConnCrossClaim, ScoutCoverage reused round-49 seat names; the dispatcher resumed the parked round-49 agents, which returned their round-49 reports (no error text; `w1-results.json` names `.ufo/waves/round-49/w1/<name>.md`). Not replaced under the same identity; their work was re-assigned to W2 items under `R50`-prefixed names. `wave-complete-check.py` on `w1-spec.json` prints those 13 `MISSING` (`OK 29/42`); on `w2-spec.json` `OK 43/43`; `name-collision-check.py` on w2 → 0.
- This report is filed after WAVE-DONE of both waves.

**Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only operator/orchestrator state files modified (`.scratch`, `.ufo/state`) and one untracked path, `.ufo/waves/round-30/`, another lane's round-30 seat output that I did not touch; no file of this lane's seats is misrooted.

**Stale-lane:** launched 17:45 -03; progressing with lane commits throughout.

**Tool installs:** none. **L0:** `8d77e6c1` still open; no new question appended.
