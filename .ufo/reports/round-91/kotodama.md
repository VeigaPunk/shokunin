# kotodama — round 91 (hyaku run 15, attempt 1)

lane: kotodama-shokunin · round: 91 · campaign: hyaku · date: 2026-11-05 (−03:00)
base: `d39434b3bc8458e1b66edd2d0d0fea9ea32f3331` · freeze: `691aebf247ebea4dd50577bb64ac99d12fa1145a`
claim lands: `6656cef3da3e5d97d2540312a1cfb1e9d299f3ca` · receipts/bookkeeping: `4e0d5f9b384ba71c52750a3b5963fc8ad525d31a` · wave evidence: `28057e09fc6d151584ce27b2c187d0dd174baa30`
measured at: `28057e09fc6d151584ce27b2c187d0dd174baa30` · lane tip at report: `b71f348c156196d8cb1883ca79fd372dd7aff09f` — `git ls-remote origin refs/heads/main` prints the same hash.

## Work performed

Declared claims (frozen before data, `reports/round-91/claims.json`):

- **O / operability — successor move to the round-90 advance-evidence grader.** `tools/check-advance-evidence.py` v2 refuses nine named entry-mode counterfeit classes the round-90 grader passed, with a 77-check selftest and a committed 53/53 mutation receipt; tool sha256 `88597a66…` is the freeze pin.
- **C / coverage — sourced claim.** One new linguistics entry, `corpus/knowledge/linguistics/secret-and-ludic-languages.md`, over four sources opened this round (S952–S955 admitted; S956 registered as a rejection).

Freshness is the lane's historically lowest non-retired axis and is **paused** by the open L0 questions `kotodama | round-11` and `kotodama | round-89`. No ruling lifting that pause is on record, so the lowest-axis obligation is neither met nor waived this round; the report states the gap instead of inventing a waiver.

Work items, each with its evidence pointer:

- **Freeze and controls before any data** — `691aebf2`: claims, counter `reports/round-91/measure91.py`, mutant generator `reports/round-91/mutants.py`, the v2 grader, the stub control, `controls/before-v1-selftest.txt`, `controls/at-freeze-C-do-nothing.txt`, `mutation-score.txt` (53/53) and `census-start.txt` (rc 0, 875 rows).
- **Inherited attempt resolved** — earlier attempts of this round (02:11–02:19 and the 07:31 L1) died on provider failures after the freeze. Reused after re-verification: the freeze commit, the v2 tool, the mutants, the stub, the four committed captures S952–S955 and the register slice. Self-produced this attempt: the entry landing and its integration, the before-v1 receipt, the consolidated quarantine verdicts, the README moves, all measurements and this report.
- **Claim C landing** — the entry copied byte-for-byte from the scribe's stage file (`cmp` clean), `corpus/SOURCES.md` rows S952–S956, `corpus/README.md` index row plus a round-91 section and count moves, lesson gate lines with one located quote per id. Lands `6656cef3`; entry 21,472 B.
- **Claim O hardening measured through the public path** — the v2 tool's selftest (77/77, exactly 77 `ok` lines, 9/9 refusal names), the frozen mutation pass (53/53 killed, 0 survived, 0 broken-pattern) and a live stub run (22 `ok` lines, refused by OKCOUNT; 0/53 killed, 53 broken-pattern) are all executed by the frozen counter at the lands revision, not read from prose: `reports/round-91/final/lands-O.txt`.
- **Before-state receipt for O** — `reports/round-91/controls/before-v1-entry.txt`, produced **after** the freeze (the file the frozen text names did not exist; ReviewerFreeze D1). It rebuilds the round-90 critic's fixture: a topic-line-padded bakery entry with two new rows sharing one URL and gate quotes copied from the teaching cells. Base v1 scores it PASS 6/6; frozen v2 refuses it on TOPIC (0/6 phrase anchors), UNIQUENESS (shared URL) and GATE (self-quote). The same receipt records the correction that v1 already refused a plain off-topic body (4 shared content words < 10), so the padded variant, not the whole class, is what v2 adds (lesson R91-M6). The `ExecBeforeBundles` seat reproduced the same three classes on independently built bundles (`.ufo/waves/round-91/w1/stage/ExecBeforeBundles/`): v1 PASS 6/6 on each, v2 refusing TOPIC, UNIQUENESS and GATE respectively.
- **Quarantine frontier step** — the kotodama slice of the shokuknow absent-defect register was re-derived (21 data rows) and hand-checked four times over: `ExecQuarantineA` (S776–S804), `ExecQuarantineB` (S807–S835), `ReviewerQuarantine` (seven rows, fetch-first and blind to A's file) and an L1 pass (`reports/round-91/quarantine/l1-handcheck.py` with retries, pdftotext, charset sniffing, bot-wall detection and punctuation folding). Consolidated verdicts in `reports/round-91/quarantine/verdicts.json`; nothing adopted.
- **Id-collision guard** — `.ufo/waves/round-91/assimilation/`: 880 lane ids vs 132 staged ids, 98 collisions, so any later adoption round must renumber in scratch.
- **Measurement** — `final/lands-O.txt` `MEASURE91-O: PASS legs=7/7`, `final/lands-C.txt` `MEASURE91-C: PASS legs=4/4` at `6656cef3`, both run in a caller-owned directory with the freeze-pinned counter, tool, mutants and stub.
- **Scope and sweep** — no write outside `kotodama-shokunin/` and this report. Fleet-root sweep after the wave: `MANIFEST.json` (driver), `.scratch/` (orchestrator) and two empty `git init` directories `p/` and `bashx/` (created 08:18 during the w1 window, no refs, no commits, naming neither this lane nor this round) — not kotodama evidence, left in place and recorded here.

### Falsification findings the frozen instrument does not cure

W1 attacks were dispatched against the frozen bytes; none of these was repaired inside the round, and each bounds what O and C prove.

| attack (seat) | claim/leg | verdict | what it means here |
|---|---|---|---|
| `O.before` names `reports/round-91/controls/before-v1-entry.txt`, a receipt that existed at no revision (ReviewerFreeze D1) | O | broken as filed | the receipt was produced after the freeze and is labelled as such; its measurement also corrects the frozen sentence (the naive off-topic body is refused by v1, the topic-line-padded one is not) — lesson R91-M6 |
| the mutation receipt header prints the last mutant's first line beside a hardcoded `clean_rc: 0` (ReviewerFreeze D4) | O | display defect | killed/total/survived counters and every graded leg are unaffected; the receipt is not citable as a clean-run tally — routed |
| no leg checks the "mutation receipt over every v2 sub-check" clause (ReviewerFreeze D5) | O | unchecked clause | the MUTATION leg re-runs the frozen mutants, so the run still binds to the freeze bytes; the receipt artifact is checked by nothing — routed |
| the mutant generator's clean gate is rc-only (ReviewerFreeze W2) | O | composition precondition | TOOL/SELFTEST/OKCOUNT legs absorb it this round |
| `grade_c` indexes cells without a column-count guard (ReviewerFreeze W3) | C | latent crash | a malformed short row would abort instead of scoring — routed |
| `C.surface`'s "13 linguistics entries" (ReviewerFreeze W1) | C | unreproducible | the same reading gives 3 at base; the operative unmoved-command holds |
| `ExecQuarantineA` matched backtick-wrapped cells, and its late trailer then reported S786's fragments inverted (ReviewerQuarantine, L1 fold pass) | frontier | matching-method defect | verdicts re-derived from the same bytes; `pdftotext` finds the English gloss at offset 79 and not the Chinese sentence, so S786 is PARTIAL — recorded as R91-M7 |
| `MutationTesterV2` wrote 16 new single-point mutants of the v2 grader: 9 killed, 7 survived (one of them equivalent: `newids-cited-closure-off` is unreachable by construction, so 6 real gaps) | O | weakened | the 77-check selftest does not isolate every arm: NEWIDS non-mined status, GATE "no lesson line", CAPTURE fetched-date and path-confinement arms, TOPIC's table-cell text source, and the graded auto-include are unexercised. The frozen claim does not assert exhaustive coverage and its `bounds` sentence says so; the survivors are routed with fixture ideas in that seat's `survivors.md` |
| `CriticClaims91` ran 13 counterfeits plus one control against the frozen v2 entry mode: the control passes 8/8, six named refusal classes hold, **seven counterfeits still pass rc 0** — lesson-channel dispositions behind a blockquote or with no dash, a chrome quote carried as the entry's own sentence, a base-URL shadow distinguished only by a `#fragment` suffix, phrase-list heading stuffing, a capture byte-copied from the base registry, and one capture path shared by two qualifying ids | O, C | weakened | the frozen claim does not assert that no other class exists; its `bounds` sentence says so, and the seven survivors with their smallest corrections are routed to round 92 (`CriticClaims91/attacks.md`, lesson R91-M8). The landed entry was checked against each class and exhibits none |

## Landed changes

Each change is tied to the `LOG.md` round-91 entry and to the commit that carries it.

| change | commit |
|---|---|
| claims, frozen counter `reports/round-91/measure91.py`, mutant generator, v2 grader `tools/check-advance-evidence.py`, stub control, at-freeze and before-selftest controls, 53/53 mutation receipt, census start | `691aebf2` |
| claim-C landing: `secret-and-ludic-languages.md`, rows S952–S956, lesson, README index row and round-91 section, evidence captures plus manifest, before-v1 receipt, 21 consolidated quarantine verdicts, WAVE-1 spec/dispatch/ready and the seat reports then on disk | `6656cef3` |
| claim receipts at lands (O 7/7, C 4/4), before-v1 receipt with three counterfeit arms, SCORECARD round-91 sections and capability row, LOG round-91 entry, SHONEN pointers, census end | `4e0d5f9b` |
| W1 results file, all ten seat reports and the critic's counterfeits as wave evidence; R91-M8 | `28057e09` |
| final re-measurement receipts at `28057e09` (`final/lands-O-final.txt`, `final/lands-C-final.txt`) | `b71f348c` |

## Before → after measurements

Both claims were measured with the freeze-pinned counter, from a caller-owned work directory (removed after the round), against the same lands revision.

| claim | counting command | before | after (measured) |
|---|---|---|---|
| O / operability | `python3 -B reports/round-91/measure91.py --root <lane> --freeze 691aebf247ebea4dd50577bb64ac99d12fa1145a --lands 28057e09fc6d151584ce27b2c187d0dd174baa30 --claim O --work <existing-dir>` | base tool sha256 `121888f0…` ≠ pin; its selftest prints 67 `ok` lines and 0 of the 9 named refusals; its entry mode scores a topic-line-padded bakery entry with a shared URL and self-quote gates PASS 6/6 (`controls/before-v1-entry.txt`) | `TOOL` sha = `88597a66…`; `SELFTEST PASS 77/77`; `OKCOUNT` 77; `REFUSALS` 9/9; `MUTATION-SCORE: 53/53 killed, 0 survived, 0 broken-pattern`; stub 22 `ok` lines (refused) and 0/53 killed → `MEASURE91-O: PASS legs=7/7` (`final/lands-O-final.txt`), measured at `28057e09`; an earlier pass at `6656cef3` is kept in `lands-O.txt`, and `lands-O-final.txt` holds the later run at `28057e09` (a `4e0d5f9b` run used the same path and was overwritten) |
| C / coverage | `python3 -B reports/round-91/measure91.py --root <lane> --freeze 691aebf2… --lands 28057e09… --claim C --work <existing-dir>` | entry absent; linguistics 35 files; registry 875 rows, last id S951; 0 filename owners of the surface | entry 21,472 B, 9 `##` sections, 6×4 table, 6/6 sub-topic phrases anchored in headings/table; S952–S955 mined and cited; index `CORPUS-INDEX: OK files=263 rows=263 findings=0`; no base row changed → `MEASURE91-C: PASS legs=4/4` (`final/lands-C-final.txt`), measured at `28057e09`; an earlier pass at `6656cef3` is kept in `lands-C.txt`, and `lands-C-final.txt` holds the later run at `28057e09` (a `4e0d5f9b` run used the same path and was overwritten) |

Surface commands, re-run at the tip `b71f348c`:
`git ls-tree -r --name-only <rev> corpus/knowledge | grep -Eic '(secret|ludic|argot|slang|cant|jargon)'` → 0 at base, 1 at tip;
`git ls-tree -r --name-only <rev> corpus/knowledge/linguistics | wc -l` → 35 at base, 36 at tip.

Frozen-surface defect (ReviewerFreeze W1, confirmed by the L1): `C.surface` says "Topic lines name the register in 13 linguistics entries". The reproducible count under that reading is **3** (`- topic:` lines matching the term set at base); the frozen text is not edited and the operative unmoved-command above holds.

## Sources & frontier

Census command (both ends): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`

- start: rc **0**, 875 rows (`reports/round-91/census-start.txt`)
- end: rc **0**, 880 rows (`reports/round-91/census-end.txt`)

| quantity | base `d39434b3` | tip `b71f348c` |
|---|---|---|
| rows | 875 | 880 |
| tier A / B / C | 517 / 330 / 28 | 518 / 333 / 29 |
| status mined / queued / rejected | 769 / 58 / 48 | 773 / 58 / 49 |

Rows added by tier: **A +1, B +3, C +1** — S952 (B, Polari overview), S953 (B, Polari book description), S954 (A, Harman's *Caveat* in LEME), S955 (B, Messili on verlan), all `mined`, `opened 2026-11-05`, `used-by` the new entry with a lesson gate line, a located quote and a committed capture; S956 (C, Wikipedia *Argot*) is a `rejected` row with its reason and flip in the gate line. Rows touched old→new: **none** — no old row's status, recheck or used-by changed (`APPENDONLY` leg clean; `git diff --numstat d39434b3 b71f348c -- corpus/SOURCES.md` → `6 0`).

Frontier rows advanced: the kotodama slice of the shokuknow absent-defect register, 21 data rows, each hand-checked and dispositioned this round — LOCATED 3 (S778, S804, S827), PARTIAL 3 (S776, S786, S825), ABSENT 10, UNREACHABLE 3 (S791, S823, S835), UNVERIFIABLE 2 (S807, S812) in `reports/round-91/quarantine/verdicts.json`. **Adoption stays closed**: this is a quarantine-first round and nothing from the package is appended. The id-collision guard found 98 collisions between the lane's 880 ids and the package's 132 staged ids. `considerthese/` is absent, so no proposal was mined.

Assimilation: **none** (quarantine-only round; package adoption starts a later round).

Duplication check against the four adjacent owners (normalised 8-word shingles over the new entry vs
`linguistics/linguistic-anthropology.md`, `synthesis/religion-language-co-evolution.md`,
`linguistics/register-lexicon-ceilings.md`, `linguistics/dialect-register-consistency.md`): **0 shared
shingles** with each.

## Trend verdicts

- **expansion — improved.** The linguistics partition gains a dedicated owner for a surface that had none (`0 → 1` filename owners for secret|ludic|argot|slang|cant|jargon), with four new sourced rows and one registered rejection; the adjacent-owner scan names exactly what the new entry does **not** absorb.
- **quality — improved.** Claim O adds nine named entry-mode refusals with a 77-check selftest and a 53/53 mutation receipt, and the before receipt shows the base grader passing the same counterfeit 6/6; claim C lands an entry whose every cited line carries one id (`CITED-LINES: 0 finding(s)`), with located quotes bound to committed captures.
- **discernment — improved.** The round re-checked its own evidence rather than trusting it: the frozen `O.before` receipt was found missing and its premise partly false (R91-M6), a seat's backtick-poisoned matching was caught by an independent re-check and re-derived (R91-M7), and 21 register rows were dispositioned without adopting any of them.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SHONEN.md` line 5 updated this round: SKILL sections plus `corpus/lessons/round-91.md` Gate (S952–S955 admitted, S956 rejected) and `reports/round-91/final/lands-C.txt` PASS 4/4.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round-91 entry; the entry, the shipped grader and the w1 seats' surface/overlap/quarantine work; no historical certification or lore handoff acceptance claimed.
- [~] Instructions executable by an agent without oral context — `tools/check-advance-evidence.py` public CLI, `--selftest` 77/77, mutation 53/53, `final/lands-O.txt` PASS 7/7 and `lands-C.txt` PASS 4/4 at the same lands revision; named survivors and the frozen-receipt defects (ReviewerFreeze D4/D5) stay in the record.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the diff touches only the new entry, its registry rows, `corpus/README.md` and the lane's receipts; `ConnectorOverlap` names `linguistic-anthropology.md` §5.3 and `synthesis/religion-language-co-evolution.md` §6 as the adjacent owners, canon stays lore's and research method chousa's.

No `[x]`: every box still rests on author-side evidence plus dispatched seats, which are the lane itself; the non-author closure is the check that can promote one.

## Round shape

One v1 wave (`w1`), ten seats under `ufo-wave-policy.json` (band 8–16), dispatched through the inline
handoff `<wave>.ready` at 08:07:32 and taken by the orchestrator:

| role | seat | outcome |
|---|---|---|
| scribe | ScribeEntry-20 | delivered `entry.md` (21,472 B) plus draft-shape checks (0 `CITED-LINES` findings, 9 headings, 6×4 table, 6/6 phrase anchors) |
| scout | ScoutSurface-8 | delivered the base-vs-tip coverage surface with commands, rc and counts |
| connector | ConnectorOverlap-13 | delivered the per-sub-topic sibling-overlap verdicts and the PROVINCE read |
| executor | ExecQuarantineA | delivered verdicts for S776–S804 (10 rows) and committed capture copies |
| executor | ExecQuarantineB | delivered verdicts for S807–S835 (11 rows) and committed capture copies |
| executor | ExecBeforeBundles | delivered three independently built counterfeit bundles (bakery, shadow, self-quote); v1 PASS 6/6 on each, v2 refusing each class |
| reviewer | ReviewerFreeze | delivered a 33-row freeze review (D1/D4/D5, W1/W2/W3, N1/N2) |
| critic | CriticClaims91 | delivered 13 counterfeits + 1 control against the frozen entry mode: 6 refusal classes hold, 7 counterfeits still pass (`stage/CriticClaims91/{counterfeits,attacks}.md`) |
| mutation-tester | MutationTesterV2 | delivered a 16-mutant independent pass: 9 killed, 7 survived (one equivalent), plus one kill fixture idea per survivor |
| reviewer | ReviewerQuarantine | delivered an independent fetch-first re-check of seven rows and an agreement table |

Attack seats: reviewer ×2, critic, mutation-tester = 4 of 10 (40 %, above the 25 % floor). No residual
call and no replacement seat, and no dead seat: all ten settled and all ten left a report in the wave
directory. `w1-results.json` records `seats: 10` with every `output` null, because the orchestrator's
kernel restarted mid-wave and the seat payloads were not retained in the results file; the seat report
files are the record (`w1/<Name>.md`) and are committed as wave evidence. `WAVE-DONE kotodama r91 w1`
arrived at 09:08 (−03:00), before this report was written.
The canonical L2 `planner` seat is held by the L1 (the validator rejects a planner role); the bounded
planning data-walk rode `ScoutSurface` and `ConnectorOverlap`.

## Open items, routed

| id | item | route |
|---|---|---|
| ReviewerFreeze D4 | the mutation receipt header prints the last mutant's first line beside a hardcoded `clean_rc: 0`, because `head` is reused in the loop | next round: make the receipt header carry the clean run's own line, or drop the header; the frozen bytes are not amended |
| ReviewerFreeze D5 | no leg checks the "mutation receipt over every v2 sub-check" clause the frozen `O.after_target` names | next round's counter amendment: assert the receipt's existence, count and tool sha |
| ReviewerFreeze W3 | `grade_c`'s APPENDONLY arm indexes cells 3/7/8/10 without a column-count guard, so a short row aborts with a traceback instead of a scored verdict | next round: refuse malformed rows as a leg FAIL |
| ReviewerFreeze W2 | the mutant generator's clean gate is rc-only, so a tool printing `SELFTEST FAIL` while exiting 0 would pass it | named as a composition precondition; measure91's SELFTEST/OKCOUNT/TOOL legs absorb it |
| ReviewerFreeze N1/N2 | `claims.json` carries a duplicate top-level `legs` block, and the mutant narrative says 9 v2 pairs where 53 triples exist | documentation debt; the frozen file is not edited |
| R91-M6 | the frozen `O.before` receipt was missing and its premise holds only for the topic-line-padded fixture | receipt produced post-freeze and labelled; frozen text left as filed |
| W1 | `C.surface`'s "13 linguistics entries" is not reproducible (the reading gives 3) | disclosed; the operative unmoved-command holds |
| R89-M7 / round-11 | freshness pause with no operator ruling | L0 questions already open; no new line appended this round |

## Stale-lane

Respawn-per-round driver; no other kotodama mission is open.

## Tool installs

None. No pacman transaction, no `uv tool`, no binary install; `pdftotext` was already present on the host and only read PDFs.
