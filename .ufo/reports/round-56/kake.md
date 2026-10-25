# Round 56 — kake report

Lane `kake-shokunin`, base `e48354b7c26bb6dc544ab6bbdc534fabe0daf7b6`, measured content commit `4cb225fb032b04166fb0232bc98a7bcce72675ec`,
final lane tip `413c3b4a5eb52202ae20fc7212ceaf87a75f613d` (`git ls-remote origin refs/heads/master` prints it). Inherited state: no
`lane-dead-no-report kake round=56` line; nothing inherited. Round-55 verifier spot-check read; routed defects 1–4 addressed below.

## Work performed

Declared claims (frozen in `.ufo/waves/round-56/contract.md` at `2d308e808bfd` before any data; counter versions disclosed in its §Counter versions):
**C1 calibration** — the ten `SKILL.md` gate-registry rows that state a selftest tally state what their documented command prints. **Axis note for the
operator:** calibration is the round-54 bounded sub-axis (score 1, lowest non-retired) and is outside the prompt-declared operability + freshness axes;
two critics (`w1/CriticAxisClaim.md`, `w2/CriticClaimsAdmission.md`) argue C1's surface is operability (a runnable checklist item) rather than calibration as
`AXES.md` defines it, so the lowest-axis obligation is reported **open pending the ownership ruling**; calibration stays 1/10. **C2 freshness (sourced)** —
three Yahoo! JAPAN crawl-handling entries, quote-true, on rows opened or re-opened this round (S367 re-opened; S419 and S420 new); the same critics argue its
counter has no drift condition and the surface is coverage/expansion. No exploratory claim.

- Round shape: two v1 waves — W1 build + pre-data attacks 43 seats, W2 falsify 41 seats, **84 total**, no residual call; the L1 held the planner seat (data walk by scouts and connectors). W1 roles: executor 18, scout 7, critic 6, scribe 5, reviewer 4, connector 2, mutation-tester 1. W2: executor 20, critic 7, reviewer 5, mutation-tester 3, scout 2, sentinel 1, connector 1, revenger 1, simplifier 1. `labrat` and `sonic` are not swarm roles under policy v1 (validator refusal `unknown_role`); those items ran as critic/executor seats. Settlement: `.ufo/waves/round-56/settlement.md`, `w1-results.json`. Dead/misdirected seats: none (84 of 84 seat reports committed, `ls .ufo/waves/round-56/w[12]/*.md | wc -l`). W2 `w2-results.json` (41 of 41 settled) arrived after the first filing and is committed with the final lane tip.
- Counters attacked before and after build: W1 attacks found the version-1 C1 counter met by a fake `python3 -c` span, a duplicate earlier row, a host-exported pin, padded claims and a rewritten helper (`w1/CriticC1Contract.md` A1–A10, `CritCheatC1.md`, `MutC1Counter.md` 6 of 16 mutants survived, `ReviewerSelftallyCode.md`), and the version-1 C2 counter rejecting a truthful build (7 of 8: S367's row title is not a substring of the page; `w1/CriticC2Contract.md` WR-1) while a 16-file junk tree reached 8 of 8 (`w1/CritCheatC2.md`) → C1 v2 / C2 v2. W2 attacked version 2: `w2/CriticJunkC1v2.md` (5 trees reached met: two commands per cell, unvalidated pin, hollowed fixture), `w2/MutC1V2.md` (8 survivors), `w2/MutC2Selftest.md` (40 mutants, 14 killed → 19 validated fixtures ported, 7 structurally masked) → C1 v2.1 (59-check selftest) and C2 selftest 86 checks. `w2/CriticJunkC2v2.md`: a 3-file junk tree still reaches 8/8 — C2 certifies quote literalness, not support (stated limit).
- Entries: `corpus/knowledge/yahoo-japan-link-target-crawl-restriction.md` (S367), `yahoo-japan-deleted-url-recrawl.md` (S419), `yahoo-japan-nonexistent-url-recrawl.md` (S420). Wave-2 repairs after 3 critics and 3 reviewers (`w2/CriticEntry*.md`, `w2/ReviewerEntry*.md`): deleted-URL title and outcome restored to the page's 可能性 hedge, a false negative about the page's own robots meta tag removed, "third surface" miscount fixed, のほかに gloss, the S420 conditional and verb span, page-silence sweeps with commands in all three, entry 2/3 quote-class wording, S419 row headline/teaches hedged, PROVINCE check-vs-set wording.
- Re-verification (freshness): fresh GETs of all three pages equal the retained bodies (S367 equals the round-53 body, sha256 0188de9d…; `w1/ScoutFreshness.md`, `w2/ExecReopenS367.md`, `ExecReopenS419.md`, `ExecReopenS420.md`); recheck commands re-run, count 1 each; no drift; the site's robots.txt does not mention `archives`.
- Assimilation: theme Yahoo! JAPAN crawl handling from `merge/kake/`; id lists/collisions/renumber map in `corpus/lessons/round-56.md` §Assimilation: reg 156, staged 129, collisions 8 (S312 S329 S367 S372 S373 S374 S390 S409, all the same document), map S375→S419, S376→S420, S367→S367; guard proof `w1/ExecIdGuard.files/`; quarantine slice (12 rows) not adopted/not hand-checked. Considerthese: proposal 1 (landed-vs-claimed check) implemented as `scripts/landed_check.py` (selftest 14/14; run on the round-55 report: 10 cited hashes, 10 ancestors of `master`, exit 0; mutation-tested by `w2/MutLandedCheck.md`: 10 of 18 killed, 6 survivors with proposed fixtures not ported — disclosed).
- Routed defects (r55 spot-check): 1 stale registry tallies — fixed and measured (C1); 2 axis ownership — named above; 3 dead scribe seats — none this round, settlement before each hand-off; 4 S367 31 units — re-cut into pieces of at most 24 units in the new entry (row cells unchanged).
- Tools installed: none. Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`, `w2/ExecMisroot.md`): 0 of 262 lane paths outside scope, 0 deletions, no kake round-56 file at the fleet root other than harness state. Open L0 questions: none appended.
- Disclosed limits: C1 pins ten named rows only; outside them `SKILL.md` carried two more stale tallies (two corrected in place, not claimed) and 8 unmeasured mentions (`w2/ExecSkillCells.md`, `w1/ReviewerSkillRegistry.md`), so a met C1 does not certify SKILL.md's tallies as a whole; the two new registry rows are accurate (59 and 86 checks) but outside the population. The counters execute revision-controlled code with the caller's HOME and network (`w2/SentinelRound.md` S2). `used-by` of five reused held rows (S372 S374 S286 S273 S274 S050) is not extended to the new entries (it would break the C8 append-only condition; `w2/ExecEntryLinks.md` F1).

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Frozen contract, counters v1, base controls, retained sources, pre-append mirror | Round 56 | `2d308e808bfd` |
| W1 spec/dispatch | Round 56 | `6b3df99d694f` |
| Build: 3 entries, S419/S420 rows, S367 used-by, coverage rows, SKILL tally cells, counters v2, landed_check, W1 reports | Round 56 | `d5afc48acd72` |
| Counters C1 v2 / C2 v2.1, contract amendment | Round 56 | `3691e9689a03` |
| SKILL registry rows, QUALITY round-56 criteria, W1 settlement | Round 56 | `a450e43e696d` |
| W2 spec/dispatch | Round 56 | `7ad7db51dfcf` |
| Wave-2 repairs, C1 v2.1, validation receipts, W2 reports | Round 56 | `f8438a282d59` |
| C2 selftest 86, SKILL pin, SCORECARD, LOG, settlement (measured content revision) | Round 56 | `4cb225fb032b` |
| Receipts, revision pins | Round 56 | `ad06cb8a17bd` |
| W2 results, ready markers (tip) | Round 56 | `413c3b4a5eb5` |

## Before → after measurements

| Claim | Command (revision) | Before (base `e48354b7`) | After (`4cb225fb`) |
|---|---|---|---|
| C1 calibration | `python3 -B .ufo/waves/round-56/c56_selftally.py --root . --revision <rev>` | `tally_mismatches=7 rows_checked=10 met=False`, exit 1 (`controls/base-c1-selftally-v2.txt`; version 1 gave the same) | `tally_mismatches=0 rows_checked=10 met=True`, exit 0 (`controls/after-c1-selftally.txt`); selftest 59/59 (`controls/c1-selftest.txt`) |
| C2 freshness | `python3 -B .ufo/waves/round-56/c56_quote_truth.py --root . --revision <rev>` | `0/8 met=False`, exit 1 (`controls/base-c2-quote-truth.txt`) | `8/8 met=True`, exit 0 (`controls/after-c2-quote-truth.txt`); selftest 86/86 (`KAKE_R56_SELFTEST_REV=f8438a28…`, `controls/c2-selftest.txt`) |

Independent recounts: `w2/ExecRunC1.md` (0/10, byte-identical twice, ten tallies reproduced by hand-run commands, base reproduced), `w2/ExecRunC2.md` (8/8 twice, counter-free recount a–e agree), `w2/ExecDeterminism.md` (counters read committed bytes only). No regression of earlier counters (`w2/ExecRegress.md`: the frozen round-55 quote-truth counter fails at the tip by design — 158 rows against its 155+1 — and is restored by reverting the registry delta alone; round-55 readme-index counter met, 52 files). Verdict words are author-side; admission belongs to the non-author closure. SCORECARD calibration stays 1/10; operability and freshness unchanged at 10.

## Sources & frontier

- Round-start census: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake` → exit 0, 156 rows, 14 W04 (`controls/census-before.txt`). Round-end: exit 0, 158 rows, same 14 W04 ids (`controls/census-after.txt`, `w2/ExecCensus.md`). Rows: 156 → 158 (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` over `git show <rev>:corpus/SOURCES.md`).
- Added by tier: A 2 (S419, S420). Touched old→new: S367 used-by `…rel-nofollow-semantics.md` → + `…link-target-crawl-restriction.md` (other cells byte-equal).
- Frontier rows advanced: per-engine crawl hygiene (Yahoo! server status answers and link-target refusal), the README frontier ground map (one row, 6 → 9 per-engine entries).
- Assimilation: one theme, 3 entries; rejects with reasons/flips in the lesson Gate: staged S388 canonical-notification, S389 redirect-indexed-url, S387 dynamic-page-indexing, plus the staged soft-404 name and unsupported staged claims. Non-author spot-check pending (admits S367/S419/S420, rejects S388/S389/S387; `w2/ScoutSpotcheckPrep.md` lists the commands).
- Mined mistakes: four rows in `corpus/lessons/round-56.md` §Mistakes (number-drift, stale-premise, vacuous, attribution), each with a falsifier in `corpus/QUALITY.md` §Round-56 criteria; red-before: `controls/base-c1-selftally-v2.txt` exit 1.
- Sourced claim: C2 rests on S419/S420 (opened this round) and S367 (re-opened); the entries cite them.

## Trend verdicts

- expansion: **improved** — three entries on Yahoo! JAPAN status-answer and link-target ground the coverage map did not hold (the round-55 PROVINCE sentence "deleted-URL page not adopted" is superseded), each citing a `mined` row; coverage map 49 → 52 files.
- quality: **improved** — ten registry tallies now equal what their commands print (7 stale), a rotted selftest pinned, four entry overreads/modal losses corrected by attack, counters hardened by 7 pre-data and 9 post-build attacks; bounded: entry fidelity is reviewer-evidenced, not counter-proved.
- discernment: **unchanged** — admits and rejects are recorded with reasons and flips, but no non-author spot-check exists yet; the closure decides.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## SHONEN

- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources (registry rows and tally cells touched this round; no promotion claim)
- [ ] At least one end-to-end domain task executed and logged in LOG.md (untouched as a promotion box)
- [ ] Instructions executable by an agent without oral context (untouched this round)
- [ ] No cross-domain bleed (PROVINCE.md still accurate) (adjacent scan: `w1/ConnSiblingOverlap.md` found zero sibling overlap; no non-author verifier yet)
