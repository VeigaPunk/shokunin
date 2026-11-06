# kotodama — round 99 report (hyaku run 15, attempt 2)

Lane: kotodama (linguistic-cultural worldbuilding). Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Lane HEAD at landing: `3f415f84ecdb8f700899b15cc5741f40ced89ac3` (branch `main`). `git ls-remote origin refs/heads/main` → `3f415f84ecdb8f700899b15cc5741f40ced89ac3`.
Base `527df3fee305b3454446946e6779ece45456307e`. Freeze `b1b80562edfc8f6082aec74bbbf0f25e152708a8`, made by attempt 1 before any seat ran. Round commits `60ead722` (work and lands receipt) and `3f415f84` (w1 results handoff).
Attempt 1 (L1 `KotodamaR99`) dispatched w1 and then ended mid-work (`.ufo/watchdog.log`: `lane-dead-no-report kotodama round=99`, 07:56:44). This attempt (L1 `KotodamaR99a2`) inherited its outputs, re-verified them, applied the outstanding critic repairs, and landed the round.

## Work performed

Declared claims (`reports/round-99/claims.json`). There are 2 claims on distinct axes, and each can be verified without the other. Attempt 1 froze them and they were not changed:

- **Claim O — operability (harm repair, grader v10 → v11).** It removes the two v10 false-refusal surfaces that the round-98 closure ruled a harm: F4, Mc heading marks; and F1, a bare non-ASCII numeral heading. It also removes the pre-existing virama over-refusal (DEVAOK1). Every v10 refusal must stay. Legs O0–O6.
- **Claim C — coverage (sourced frontier → core entry).** `corpus/knowledge/linguistics/praise-poetry-panegyric.md`. At base, nothing owns this surface in a topic line or heading: C8 owners=0 in `reports/round-99/predispatch-base.txt`. Legs C1–C9.
- **Lowest-axis note:** freshness is the lowest non-retired axis. It stays paused by the open L0 round-11 and round-89 questions. No claim moves it, so the obligation is neither met nor waived. The stagnation nudge is not invoked.

Work items. The wave dir is `.ufo/waves/round-99/w1/`. Each seat writes its report to `w1/<Seat>.md` and its stage files to `w1/stage/<Seat>/`.

1. **Freeze (attempt-1 L1, re-verified).** The freeze commit `b1b80562` holds:
   - the counter `reports/round-99/predispatch.py`;
   - the do-nothing control `predispatch-base.txt` → `PREDISPATCH-99: FAIL legs=6/16`;
   - forgery and feasibility controls in `reports/round-99/controls/forgery/`. F-O-SHA fails O1, O2 and O4. F-O-LOOSE fails O2 with survivors=2, so deleting protection does not pass. P-O-FEAS passes O2 and O4, so the target is reachable;
   - battery99, its pin and its v10 receipt (`battery99-control-v10.txt`: not-clean=6);
   - `critic98-on-v10.txt` (OVERREFUSAL n=2).
2. **ExecGraderV11 (executor).** Wrote grader v11 (`717341dc…`). A heading mark is now refused only when it changes what the heading anchors; the HEADING-NUMBER loop is removed; the dead Me branch is removed; NFKD Me is pinned. Selftest 175/175. Each repaired branch was reverted on a scratch copy and turned the selftest red. Evidence: `w1/ExecGraderV11.md` §4.
3. **MutationTester99 (attack).** Wrote 136 mutants, including widening mutants. The driver was pinned before measuring: `controls/mutants99.sha256` = `cf58e126…` = line 1 of the receipt. First measurement on v11: 136/136 killed. Red-before on v10: 128/136, 2 survived, 6 broken-pattern. Evidence: `w1/MutationTester99.md`.
4. **CriticO99 (attack).** Ran 75 classes. On v11 all 28 benign classes are clean (0 over-refusal) against 23 over-refusals on v10. Six attack classes newly pass, and all six are measured anchor-neutral, so none forges an anchor. Two load-bearing reopenings found on intermediate bytes (`—<U+093E>`, `I<U+0301>.`) are refused on the final bytes. Evidence: `w1/CriticO99.md`.
5. **ReviewerO99 (non-author attack).** Ran the frozen counter: `PREDISPATCH-99: PASS legs=16/16`, rc 0. It also checked the pin/order table and reproduced the v10 control receipt byte-for-byte. Evidence: `w1/ReviewerO99.md` §1–2.
6. **ScoutSurface99 and ConnectorOverlap99.** Mapped the surface and the adjacent owners; the entry defers to `orality-formulaic-language.md` §3. These two seats carried the planning data-walk. Evidence: `w1/ScoutSurface99.md`, `w1/ConnectorOverlap99.md`.
7. **ScoutSources99.** Opened 14 candidates: 11 admitted (tier A 6, B 5) and 3 rejected, each rejection with a reason and a flip condition. Evidence: `w1/stage/ScoutSources99/candidates.md`.
8. **ExecRegistry99.** Sole registry writer. Appended S1007–S1017 and wrote `reports/round-99/evidence/manifest.json`. Census rc 0.
9. **ScribeEntry99.** Wrote the entry (13 h2) and its README index row.
10. **ReviewerC99 (non-author attack).** C1–C9 PASS. Re-opened 11/11 sources on fresh bytes: HTTP 200, count 1 (`w1/stage/ReviewerC99/reopen.json`).
11. **CriticC99 (attack).** Claim C survives. It found three support defects: an unsourced Yoruba table cell, the setting word "rally" for S1008, and two neighbour sections restated without deferral (`w1/CriticC99.md`).
12. **ScribeOath99.** Repaired the three oath-entry weak lines routed by the round-98 closure (L49/L51/L53). Each decisive span has count 1 in its round-96 capture (`w1/ScribeOath99.md`).
13. **Attempt-2 L1 integration:**
    - Re-ran the counter's O0–O5 on the inherited tree: all PASS.
    - Applied CriticC99's three repairs: entry lines 154, 179, 188 and 193; `grep -c 'public property\|Xhosa rally'` → 0. Recorded as lesson R99-M2.
    - Wrote the lesson's §Inherited section, the SCORECARD round-99 block and the LOG entry.
    - Ran the final counter → `reports/round-99/predispatch-lands.txt`, PASS 16/16.
    - Ran the round-end census.

Round shape and seat mix:

- One v1 wave `w1` of 12 seats (validated: `w1-spec.json`, `w1-dispatch.json`), dispatched by attempt 1 through the inline handoff. No residual call. **Round total: 12 seats.**
- Roles: executor 2, mutation-tester 1, critic 2, reviewer 2, scout 2, connector 1, scribe 2.
- Attack seats: 5 of 12 (42%).
- **Dead seats: 0.** Every seat left its report and a `DONE` stage marker. `w1-results.json` (landed in `3f415f84`) records `output: null` for all 12 seats, with the note "orchestrator kernel restarted mid-wave". Because of that restart, the seat evidence is the wave-dir reports, not results.json.
- WAVE-DONE for w1 was received from Main before this report was filed.
- Planner: the L1 holds the canonical planner seat. The planning data-walk rode ScoutSurface99 and ConnectorOverlap99.

## Landed changes

| change | file(s) | LOG entry | commit |
|---|---|---|---|
| freeze: claims, counter, do-nothing and forgery controls, battery99 + pin + v10 receipt, critic98-on-v10 | `reports/round-99/{claims.json,predispatch.py,predispatch-base.txt}`, `reports/round-99/controls/*` | round 99 | `b1b80562` |
| claim O: grader v11 | `tools/check-advance-evidence.py` | round 99 | `60ead722` |
| claim O: mutation pin and first receipt (driver in the stage dir) | `reports/round-99/controls/{mutants99.sha256,mutation99-first.txt}`, `.ufo/waves/round-99/w1/stage/MutationTester99/mutants99.py` | round 99 | `60ead722` |
| claim C: entry (with the CriticC99 repairs) | `corpus/knowledge/linguistics/praise-poetry-panegyric.md` | round 99 | `60ead722` |
| claim C: registry S1007–S1017, evidence captures, manifest, L1 re-open receipt | `corpus/SOURCES.md`, `reports/round-99/evidence/*`, `reports/round-99/l1-reopen/*` | round 99 | `60ead722` |
| README index row and revision 2.25 | `corpus/README.md` | round 99 | `60ead722` |
| oath entry L49/L51/L53 repairs | `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` | round 99 | `60ead722` |
| QUALITY criterion 41 | `corpus/QUALITY.md` | round 99 | `60ead722` |
| lesson, SCORECARD, LOG | `corpus/lessons/round-99.md`, `SCORECARD.md`, `LOG.md` | round 99 | `60ead722` |
| lands receipt and census start/end | `reports/round-99/predispatch-lands.txt`, `.ufo/waves/round-99/census/*` | round 99 | `60ead722` |
| wave evidence: spec, dispatch, ready markers, 12 seat reports and stages | `.ufo/waves/round-99/w1*` | round 99 | `60ead722` |
| w1 results handoff | `.ufo/waves/round-99/w1-results.json` | round 99 | `3f415f84` |

## Before → after measurements

Counting command, the same frozen bytes for both claims:
`python3 -B reports/round-99/predispatch.py --root . --work <scratch> --base-rev 527df3fee305b3454446946e6779ece45456307e`

- **Claim O.**
  - Before, base `527df3fe` (`predispatch-base.txt`): O0 FAIL (v10 sha); O1 FAIL 161/161 against floor 168; O2 FAIL 0/0/37/0/3/6; O4 FAIL overrefusal=2; O6 FAIL (driver missing).
  - After, tree at `60ead722` (`predispatch-lands.txt`): O0 PASS `717341dc…`; O1 PASS 175/175; O2 PASS 0/0/37/0/9/0; O3 PASS 34/34 REG; O4 PASS overrefusal=0 with survivors=24; O5 PASS; O6 PASS 136/136 killed.
- **Claim C.**
  - Before: C1 FAIL (entry absent); C2 FAIL rows=930, highest S1006, qualifying 0; C6, C7 and C9 FAIL.
  - After, tree at `60ead722`: C1 PASS bytes=45197, h2=13, 6/6 phrases, topic equal; C2 PASS rows=941, highest S1017, qualifying 11; C3 PASS added 11, illegal 0; C4 and C5 PASS; C6 PASS 11/11; C7 PASS 11/11 with 20 captures verified; C8 PASS 0 other owners; C9 PASS 11 re-opened.
- Summary line: `PREDISPATCH-99: PASS legs=16/16`, rc 0.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`.
  - Round start: rc 0 (`.ufo/waves/round-99/census/census-start.txt`).
  - Round end: rc 0 (`.ufo/waves/round-99/census/census-end.txt`). Warnings W01 (S893, S907) and W04 (S927, S928) are pre-existing.
- Rows before → after: 930 → 941 (`grep -c '^| S[0-9]' corpus/SOURCES.md`). Added by tier: A 6 (S1008–S1013), B 5 (S1007, S1014–S1017). Every new row went absent → mined, recheck 180d, used-by the praise entry.
- Rows touched old→new: none. No supersedes.
- Rejected candidates (3), each with its reason and flip condition in the lesson Gate: C6 Iranica (403), C8 Skaldic Project (timeouts), C14 Gourlay (scope).
- Frontier advanced: praise poetry and panegyric moved from frontier to core.
- Sourced claim: C rests on S1007–S1017, opened this round and cited in the entry.
- Mistakes mined:
  - **R99-M1:** a refusal was widened without a benign twin. Captured-by: none. Fix: battery99's benign controls, leg O4 and QUALITY 41. The fix was shown able to fail on v10 (not-clean=6, overrefusal=2).
  - **R99-M2:** a table cell and a setting word outran their captures. Captured-by: none. Fixed by repair only; it is routed to round 100 as a gate.
- Assimilation: none. No shokuknow package was adopted. `considerthese/` is absent from this lane. No `corpus/lessons/operator-*.md` files exist.
- Round-98 verifier spot-check: routed defects 1–3 (F4, F1, F2, F3) are closed by claim O, and item 5 (oath L49/L51/L53) by ScribeOath99. Item 4, CriticO98b's 24 survivors, stays open: O4 bounds it at ≤24 and it is routed to round 100.

## Trend verdicts

- **expansion: improved.** One new core entry and 11 new sourced rows (C1–C9 PASS, `predispatch-lands.txt`).
- **quality: improved.** Grader v11 repairs the closure-ruled harm (critic98 over-refusal 2 → 0; benign 28/28 clean in CriticO99) with no lost refusal: battery99 refused stays 37, critic97 is unchanged, mutation is 136/136. Three oath weak lines and three praise-entry support defects were also repaired.
- **discernment: unchanged.** QUALITY 41 adds a rule that can fail. However, R99-M2 shows the C legs still cannot see table-cell support, and no outside spot-check has run yet. The non-author closure is pending.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence `corpus/knowledge/linguistics/praise-poetry-panegyric.md` (decision procedure, failure modes, S1007–S1017); no non-author verifier named this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence LOG.md round-99 entry; `reports/round-99/predispatch-lands.txt` PASS 16/16.
- [~] Instructions executable by an agent without oral context — evidence `tools/check-advance-evidence.py --selftest` 175/175; ReviewerO99 reran it independently (`w1/ReviewerO99.md` §1). That is a lane seat, not an outside verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence `w1/ConnectorOverlap99.md`, `w1/CriticC99.md` (boundary deferrals added to yoruba.md and germanic-norse.md).

## Extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none, by the L1 or by any seat (each seat report says none).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows one untracked file, `w4lines.txt` (Nov 5, no kotodama/round-99 content). It is not this lane's and was left untouched.
- Inherited state: every uncommitted output of attempt 1 was re-verified and committed in `60ead722`. Nothing was discarded.
- Open L0 questions: kotodama round-11 and round-89 (freshness) remain unanswered. No new questions.
- Scratch `/fast/scratch/hyaku/kotodama-r99` removed after landing.
