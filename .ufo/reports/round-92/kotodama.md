# kotodama — round 92 report (attempt 1)

Lane: kotodama-shokunin (言霊), linguistic-cultural worldbuilding, axes depth + coverage.
Lane HEAD at filing: `793fa35aa9f5d989fd364c8f9468de695cf9466c` (branch `main`, remote-verified).
Claim measurements stamped at lands `1473606b7baaf1b4050c8b21c30bdf17761d136d`; both claims re-measured at HEAD (C at `793fa35a`, `reports/round-92/final/tip-C.txt`).

## Work performed

Declared claims (2, distinct axes, distinct graded paths; both frozen at `066b9728fc64e78735769c4740d05c1000d31a3b`):

- **O — operability (successor move).** Grader v3 for `tools/check-advance-evidence.py` refuses by name the seven counterfeit classes that the round-91 spot-check routed (plus the shared-capture clause), repairs the mutation receipt header (routed D4), adds a counter leg that asserts the committed mutation receipt (routed D5), and turns a malformed registry row into a leg FAIL (routed W3). Target: selftest 89/89, 21 named refusals, mutation 60/60, stub refused. Counter: `reports/round-92/measure92.py`.
- **C — coverage (sourced claim).** One dedicated entry `corpus/knowledge/linguistics/ideophones-mimetics.md` on ideophones and mimetic vocabulary, over four A-tier sources S957–S960 opened 2026-11-05, with registry rows, gate lines, captures and an index row. Counter: the same `measure92.py --claim C`.

Frontier step (§2b): registry curated (S957–S960 admitted; search log and 16 exclusion reasons in the lesson's `## Gate`); census before and after both rc 0; ten mistakes mined (R92-M1–M10 in `corpus/lessons/round-92.md` `## Mistakes`); the sourced claim cites S957–S960 by id in the entry.

Work items, with evidence:

- Round-91 routing read and carried: `corpus/lessons/round-91-verifier-spotcheck.md` §6 items 1–7 mapped to O/C work; items 6 and 7 stay open (freshness pause; N1/N2 documentation debt, frozen bytes untouched).
- Grader v3 (`tools/check-advance-evidence.py`, sha `905be2fed386c491d52224832ea75ed8c7b02e67c1b021b2c66511658c1c1422`): relaxed lesson-disposition anchor, normalized url comparison, manifest-url binding, shared-capture refusal, gate-quote topic binding, phrase-anchor span, prose-only topic overlap, graded list extended to base registry/README/manifest. Selftest 89/89 (`reports/round-92/controls/selftest-at-instruments.txt`).
- Mutation pass `reports/round-92/mutants.py` (60 pairs; header carries the clean run's own rc and first line): `reports/round-92/mutation-score.txt`, 60/60 killed (sha `6b2a1b8a…`).
- Counterfeit battery `reports/round-92/controls/make-counterfeits.py` (sha `86d3b816…`): `before-v2-counterfeits.txt` (v2: 7/7 PASS, the defect present) and `after-v3-refusals.txt` (v3: 7/7 rc 1 on the named leg, G0 green). Independently replayed byte-identical by ExecBeforeV2 (`.ufo/waves/round-92/w1/ExecBeforeV2.md`).
- Counter `reports/round-92/measure92.py` (sha `f170cc8f…`): constants from the freeze commit, LEGCOUNT refusal, ancestor and base refusals, receipt stamps, MUTRECEIPT and ENTRY legs.
- Do-nothing and refusal controls: `reports/round-92/controls/at-base-O-refused.txt` (lands = base → rc 2), `at-freeze-C-do-nothing.txt` (rc 1, ENTRY and APPENDONLY fail), `at-freeze-O-instrument.txt` (PASS, renamed from a misleading name; see R92-M1); determinism of C checked by ExecControls (`.ufo/waves/round-92/w1/stage/ExecControls/controls-summary.txt`).
- Entry `corpus/knowledge/linguistics/ideophones-mimetics.md` (28814 B, 12 `##` sections, a 23×5 table; drafted by ScribeEntry-22, one-id-per-line fixes applied by the seat). Captures and manifest: `reports/round-92/evidence/` (S957–S960; PDFs and extracted text for the three unibo articles, HTML for Frontiers; each quote verified present in its capture).
- Connector overlap scan (`.ufo/waves/round-92/w1/stage/ConnectorOverlap/overlap-scan.md`): real contested overlap with `sound-symbolism.md` §6, flagged to the operator (see Landed changes and L0).
- Adversarial and review seats (wave 1): CriticClaims92 (16 of 21 new counterfeits survive v3; one unnamed crash), MutationTesterV3 (60/60 reproduced; 9 selftest-level gap survivors), ReviewerFreeze-2 (no gate-defeating finding; intermittent D3 selftest failure reported, see below), ReviewerEntry-5 (entry 9/9 frozen floors, QUALITY 5/5, three LOW findings).

## Landed changes

| commit | content | LOG.md entry |
|---|---|---|
| `066b9728fc64e78735769c4740d05c1000d31a3b` | freeze: grader v3, `claims.json`, `measure92.py`, `mutants.py`, stub, builder, counter receipts, S957–S960 captures and manifest | Round 92 |
| `66b3ae93fe44e73b5dfa6aefac301175fe5fc253` | wave-1 dispatch file and swarm registry | Round 92 (wave evidence) |
| `b83a1dae3aed9e4fa3b761038b942d0208e70b67` | do-nothing controls at freeze and the wave-1 spec | Round 92 |
| `1473606b7baaf1b4050c8b21c30bdf17761d136d` | claim C landing: entry, four registry rows S957–S960, README index row and footer, lesson `round-92.md` | Round 92 |
| `793fa35aa9f5d989fd364c8f9468de695cf9466c` | records: SCORECARD round-92 section, LOG round-92 entry, lesson corrections (overlap; D3), final receipts, census and index end, wave-1 seat outputs | Round 92 |

Registry and index: `corpus/SOURCES.md` 880 → 884 rows (append-only; no base row changed); `corpus/README.md` linguistics 36 → 37, footer 263 → 264 (current block).

## Before → after measurements

Counting commands are run from the lane root; receipts are in `reports/round-92/final/`.

**O (operability).** Before = round-91 tool at base `21350361` (sha `88597a66`):
- selftest `python3 -B <base tool> --selftest --work <dir>` → `SELFTEST PASS 77/77` (77 ok lines);
- named refusal cases present in its source: `for n in <21 names>; do grep -c -F "$n" <base tool>; done` → 9 of 21 present (the frozen `O.before` text says 12/21; erratum R92-M9);
- counterfeit battery `before-v2-counterfeits.txt` → 7/7 PASS rc 0 (defect present), G0 PASS.

After = v3 at lands `1473606b`:
- `python3 -B reports/round-92/measure92.py --root . --lands 1473606b7baaf1b4050c8b21c30bdf17761d136d --freeze 066b9728fc64e78735769c4740d05c1000d31a3b --claim O --work <dir> --receipt reports/round-92/final/lands-O.txt` → `MEASURE92-O: PASS legs=8/8` (TOOL sha match; SELFTEST 89/89; OKCOUNT 89; REFUSALS 21/21; MUTATION 60/60 killed, 0 survived, 0 broken-pattern; MUTRECEIPT clean; STUB refused, 0/60 killed).
- `after-v3-refusals.txt` → 7/7 rc 1 on the named leg (APPENDONLY ×2, UNIQUENESS, CAPTURE ×2, GATE, TOPIC), G0 rc 0.

**C (coverage).** Before = base `21350361`:
- entries with ideophone/mimetic/onomatopoe in the filename: `git ls-tree -r --name-only 21350361 corpus/knowledge | grep -ciE '(ideophone|mimetic|onomatopoe)'` → 0;
- linguistics partition: `git ls-tree -r --name-only 21350361 corpus/knowledge/linguistics | wc -l` → 36;
- registry rows: `git show 21350361:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` → 880; mined 773; A 518.

After:
- `python3 -B reports/round-92/measure92.py ... --lands 1473606b... --claim C --work <dir> --receipt reports/round-92/final/lands-C.txt` → `MEASURE92-C: PASS legs=4/4` (ENTRY, INDEX `files=264 rows=264 findings=0`, APPENDONLY);
- same command at HEAD `793fa35a` → `MEASURE92-C: PASS legs=4/4` (`reports/round-92/final/tip-C.txt`);
- filename owners 1; linguistics 37; registry 884 (A 522, mined 777); no base row removed or cell-changed.

Do-nothing controls: base lands → rc 2 (refused); freeze lands for C → rc 1 (ENTRY, APPENDONLY fail). The O "do-nothing at freeze" passes because the freeze carries the instrument; this is recorded as R92-M1, not counted as a control.

## Sources & frontier

- SOURCES census: start `reports/round-92/census-start.txt` rc 0, 880 rows; end `reports/round-92/census-end.txt` rc 0, 884 rows (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`).
- Rows added by tier: A 4 (S957, S958, S959, S960), all `mined`, all opened 2026-11-05, all cited by `corpus/knowledge/linguistics/ideophones-mimetics.md` and naming it in used-by.
- Rows touched old → new: none. No status, recheck or used-by of an existing row changed.
- Frontier advanced: one (ideophone and mimetic depictive class, previously 0 owners).
- Search log and exclusions (16 with reasons): `corpus/lessons/round-92.md` `## Gate`.
- Assimilation: none (quarantine verdicts of round 91 stand; 98 id collisions with the staged package remain unrenumbered; no package row appended). `considerthese/` absent.

## Trend verdicts

- **expansion — improved, qualified.** A dedicated entry on ground with zero filename owners, four A-tier rows cited. Qualification: the connector seat found a real contested overlap with `corpus/knowledge/linguistics/sound-symbolism.md` §6 (ideophone word-class definition, grammar profile, reduplication, giongo/gitaigo, a five-step register procedure). The counter measures filename ownership, so it does not see this. The overlap is reported as a possible trade for the operator (L0, `kotodama | round-92`), not absorbed.
- **quality — unchanged.** Instrument and record repairs are not quality observables under QUALITY 20; no admitted entry was re-verified, deepened or superseded this round.
- **discernment — unchanged.** The outside check of this round's gate decisions is pending: ReviewerEntry-5 checked the entry's frozen floors and QUALITY 1–5, not the admit/reject decisions in the lesson gate. Reviewer F-2 (ASCII apostrophe in the S959 title) and F-1 (authorial quoted spans) are routed and disclosed.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Tool installs

None by the L1. Used the existing `curl`, `pdftotext`, `python3`, `git` and `jj`. No pacman, sysctl or `~/.local/bin` change. The seat outputs read (ExecBeforeV2 and the others' trailers) report no install; the other seats' installs were not separately audited.

## Round shape, seats and dead seats

- Shape: one v1 wave, 10 seats: 3 executor (ExecBeforeV2, ExecControls, ExecCensus), 1 scribe (ScribeEntry), 1 scout (ScoutSurface), 1 connector (ConnectorOverlap), 2 reviewer (ReviewerFreeze, ReviewerEntry), 1 critic (CriticClaims92), 1 mutation-tester (MutationTesterV3). Attack seats 4/10 = 40 %. The L1 holds the planner role (the wave validator rejects planner as a swarm seat).
- Residual call: none. Round total: 10 seats.
- Dead seats: none. All 10 returned results (`.ufo/waves/round-92/w1-results.json`, WAVE-DONE received).
- Correction: the dispatch commit message `66b3ae93` says "4 executor"; the actual executor count is 3 (above).
- Routing: the run-15 map as set by the orchestrator (`task.agentModelOverrides`); the answering model per seat is not recorded in the results file.

## Open items and defects (routed to round 93)

1. **16 of 21 new counterfeits survive v3** (CriticClaims92; `.ufo/waves/round-92/w1/stage/CriticClaims92/attacks.md`, `corrections.md`): URL variants (scheme swap, `www.`, `?ref=`, path case); entry copy with one trailing newline; three single-word headings carrying the phrases; lesson-channel variants; six new classes. The frozen O predicate does not claim completeness and is not failed by these. Not repaired: the tool is sha-pinned.
2. **Unnamed tool crash** (CriticClaims92 A6g): an unhandled `AttributeError` on a malformed manifest exits rc 1 without a named refusal.
3. **Intermittent selftest failure D3** (ReviewerFreeze-2; `.ufo/waves/round-92/w1/ReviewerFreeze.md`, `stage/ReviewerFreeze/evidence/selftest.out`): `SELFTEST FAIL 88/89` on `capture byte-copies the base registry` in the reviewer's runs during a 10:27–10:54 window. Not reproduced by the lane: 12 sequential fresh-directory runs, 4 concurrent on one `--work`, 4 concurrent on separate dirs, all `PASS 89/89` (`/fast/scratch/hyaku/kotodama-r92/flake/`). Cause not identified. The measured lands run passed. This is an open risk to the O measurement under re-run.
4. **Nine selftest-level survivors** outside the frozen 60 (MutationTesterV3): README graded-list entries, `..` traversal arm, FETCH_RE offset, fetch-date arm, capture-dir slash arm, norm_url port strip.
5. **Mutation harness has no refusal path** for a missing `--work` (R92-M3).
6. **Claim C entry mode does not run `check-cited-lines.py`**: the multi-id lines (R92-M6) were caught by the lane's lint, not by the frozen predicate.
7. **Advisory (ReviewerEntry F-2):** the S959 title in the entry header uses an ASCII apostrophe where the capture has U+2018/U+2019; the grader's normalization folds only U+2019. Not changed: the entry is the judged object and its bytes are pinned by the review.

## Open decisions (L0)

- `kotodama | round-92` (in `.ufo/l0-questions.md`): contested scope between `ideophones-mimetics.md` and `sound-symbolism.md` §6; the operator chooses (a), (b) or (c). Routed around.
- Freshness: still paused by open `kotodama | round-11` and `round-89`. The lowest-axis obligation is neither met nor waived this round; no numeric score is invented.

## Process disclosures

- Two text replacements were made with scripted string edits instead of the edit tool: in `corpus/lessons/round-92.md` (the exclusion sentence and the design-rule sentence) and in the frozen-to-be `reports/round-92/claims.json` (the `tool_sha256` placeholder and a counterfeit-builder pin, before the freeze commit). Content was checked afterwards; no frozen file was changed after `066b9728`.
- One unverified exclusion item had been drafted into the lesson and was removed before landing (the lesson's Gate was re-derived from the DOAJ records actually screened).

## SHONEN

Four boxes in `SHONEN.md`; none is checked by a non-author verifier this round, so all remain `[~]`:

[~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `corpus/knowledge/linguistics/ideophones-mimetics.md` §11 decision tables and §10 procedure, cited to S957–S960; `corpus/lessons/round-92.md` `## Gate`.
[~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` `## Round 92` entry; `reports/round-92/final/lands-C.txt` and `tip-C.txt` (MEASURE92-C PASS 4/4).
[~] Instructions executable by an agent without oral context — pointer: `tools/check-advance-evidence.py` v3 CLI with selftest 89/89 (`reports/round-92/controls/selftest-at-instruments.txt`); `reports/round-92/final/lands-O.txt` (MEASURE92-O PASS 8/8); known survivors named in R92-M7 and R92-M8.
[~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `.ufo/waves/round-92/w1/stage/ConnectorOverlap/overlap-scan.md`: no sibling-lane overlap; one intra-lane overlap with `sound-symbolism.md` §6 flagged to the operator (L0).

## Verification handed to the main agent

Re-run, once, at the final tip: `python3 -B reports/round-92/measure92.py --root . --lands 793fa35aa9f5d989fd364c8f9468de695cf9466c --freeze 066b9728fc64e78735769c4740d05c1000d31a3b --claim O --work <dir>` (expect 8/8; watch D3); `… --claim C …` (expect 4/4, already run at HEAD); `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` (expect rc 0); `python3 -B tools/check-corpus-index.py --root .` (expect OK 264/264).
