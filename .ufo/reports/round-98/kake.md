# kake — round 98 report (hyaku run 15, attempt 1)

L1: KakeR98. Lane `kake-shokunin`, branch `master`. Round base `e51328b63690c8aaa78c9c8f3b87d8735c0ccbf7`;
final lane hash `77adb17e9e0225f3cf36f7b74681353bfbe3d26b` (`git ls-remote origin refs/heads/master` prints it).
Freeze: `.ufo/waves/round-98/freeze.md` at `c3eace8b5c70453faff872c89d8443753e5d21b6`. The outside closure owns admission.

## Work performed

Declared claims (2): **C1 — calibration** (score 3, the lowest owned non-retired axis): the SCORECARD
`## Capabilities` table against the admitted-closure record in fleet `MANIFEST.json`. **C2 — freshness**
(HOLD 10), capability acquisition, sourced on S482: an RFC 5861 stale-while-revalidate / stale-if-error
decision under the RFC 9111 §4.2.4 prohibitions.

- Instruments, contract and control subjects committed before any seat ran: `c98_captable.py`, `c98_stale.py`,
  `stale-contract.md`, `frozen/` (positive control + six forgeries), RFC 5861 retained body
  (`sources/rfc5861.txt`, sha256 `1193f1c8…`), SKILL.md registry rows 223–224 — commit `2db76835`.
- Pre-freeze controls through the public CLIs on committed fixture revisions (`controls.sh`), receipts in
  `.ufo/waves/round-98/controls/`: C1 base `mismatches=46` exit 1; names-only forgery `mismatches=85`
  exit 1; mega-row forgery `mismatches=45` exit 1; junk-prose forgery `met=true` (declared limit → review
  conjunct); selftest 16/16. C2 base/instr `candidate=absent` exit 1; pos-oracle `met=true` exit 0; six
  forgeries all `met=false` exit 1 (constant hand 14/60, lookup 60/60 but generated 80/240, no-prohibit
  52/60, exclusive 56/60, request-sie-ignored 57/60, lenient 56/60) — freeze commit `c3eace8b`.
- C1 repair (`.ufo/waves/round-98/apply_c1.py`, rows from `gen_cap_rows.py`): 39 rows added, r20 row renamed,
  5 rows of non-admitted closures (r34, r35, r37, r61, r64) moved to a history table — `4446ce21`;
  receipt `controls/after-c1.txt` `mismatches=0 met=true` exit 0.
- One v1 wave of 13 seats (`w1-spec.json`, validated; `w1-results.json`). Outputs integrated:
  - ExecStale built `scripts/stale_extensions.py` from the contract alone (`w1/ExecStale/score-*.txt`, met on 4 seeds).
  - ExecTwinStale's twin differential (2505 inputs) found an oracle/candidate defect on >4 300-digit
    integers (`w1/ExecTwinStale/disagreements.md` A1–A4). L1 fixed it in the candidate before the scored commit.
  - ExecMetaLint wrote gate `scripts/knowledge_metatext_lint.py` (R98-D1): exit 1 at `7838981e`
    (`w1/ExecMetaLint/at-master.txt`), 0 after the fix.
  - ScribeEntry drafted `corpus/knowledge/stale-extensions.md` (31/31 quotes located). L1 corrected its
    `source:` line (S480 → S469/S457/S461).
  - ScoutRfc5861 re-fetched RFC 5861 byte-identically and opened the errata record (2 Verified Editorial).
    It drafted S482/S483.
  - ReviewCapB judged 45 rows: 43 agree, 2 disagree (`w1/ReviewCapB/verdicts.tsv`).
  - ReviewStale: hand cases 60/60 agree; 4 contract findings.
  - CriticClaims: 5 C1 escapes, 7 C2 escapes, 6 predicate holes (`w1/CriticClaims/attacks.md`).
  - MutCounters: captable 7/13 killed, stale 12/19 killed (`w1/MutCounters/survivors.md`).
  - SentinelScope: 15 vectors, 1 blocking (seed grind).
  - ConnectorScope: prior art in kaidoku/mori; RFC 5861 ground in siblings token-level only.
  - ScribeLesson: mistakes 5, proposal 2.
- C2 content commit `0f48ada0` contains:
  - the candidate;
  - the knowledge entry;
  - SOURCES rows S482/S483 and the `used-by` updates;
  - the README row;
  - the R98-D1 line deletion and its gate;
  - the two ReviewCapB row corrections.

  Scored by the frozen counter: `controls/after-c2.txt`.
- Lesson `corpus/lessons/round-98.md` (Gate, Mistakes M1–M7, criteria R98-A/R98-B, routes R98-1…5), LOG
  and SCORECARD round section + C2 capability row — `76f834aa`; tip receipts — `77adb17e`.
- Planner seat: held by the L1 (validator rejects `planner`; R97-D2 carried).

## Landed changes

| Commit | Change | LOG.md entry |
|---|---|---|
| `2db768356cd081092c3abc60f76b25487ec4c535` | instruments, contract, control subjects, RFC 5861 body, SKILL.md rows | Round 98, bullets C1/C2 |
| `c3eace8b5c70453faff872c89d8443753e5d21b6` | freeze + pre-freeze controls | Round 98, C1/C2 |
| `4446ce219b4f0c9f5f4fc81f7f772e3a7f24c95a` | C1 repair of the Capabilities table | Round 98, C1 |
| `7838981e4e40280176085e8aa1f6827eb7133a69` | w1 spec/dispatch, C1 after-receipt | Round 98, Wave |
| `0f48ada084fd3b0c1292e03294a5b44fe1f46e36` | C2 candidate, knowledge entry, S482/S483, README row, R98-D1 fix + gate, two row corrections | Round 98, C2 / Frontier / Correction |
| `76f834aabf020c4efca39eca9108454c39b78b7c` | lesson, LOG, SCORECARD section + C2 row, wave evidence, C2 receipts | Round 98, all bullets |
| `77adb17e9e0225f3cf36f7b74681353bfbe3d26b` | tip receipts (C1 at tip, census after) | Round 98, C1/Frontier |

## Before → after measurements

- **C1** — `python3 -B .ufo/waves/round-98/c98_captable.py --root . --revision <REV> --fleet-revision f86740064229897f53212e03ae3b6474dac66de4`
  - Base `e51328b6`: `entries=48 rows=14 matched=8 unlisted=40 unbacked=6 mismatches=46 met=false`, exit 1.
  - Repair `4446ce21`: `entries=48 rows=48 matched=48 unlisted=0 unbacked=0 mismatches=0 met=true`, exit 0.
  - Review conjunct: `cut -f3 .ufo/waves/round-98/w1/ReviewCap{A,B}/verdicts.tsv | sort | uniq -c` gives
    ReviewCapB 43 agree, 2 disagree. ReviewCapA has no file.
  - **Verdict: unmet** under the frozen kill rule.
  - Tip `77adb17e` (receipt `controls/tip-c1.txt`): `unbacked=1`. That row is the round-98 C2 row, as the
    freeze's ordering rule predicts.
- **C2** — `python3 -B .ufo/waves/round-98/c98_stale.py --root . --revision <REV> --work <scratch>`
  - Base `e51328b6`: `candidate=absent … met=false`, exit 1.
  - `0f48ada0`: `candidate=present sha256=f43895f1… hand=60/60 generated=240/240 refusals=35/35
    seed=2409304220 met=true`, exit 0. The scored sha256 equals the landed blob.
  - 20 extra seeds: 20/20 `met=true`.
  - Named attack probes: 12/12 (`controls/after-c2-named-probes.txt`).
  - **Verdict: met on the frozen predicate.** The capability row entered.

## Sources & frontier

- Census, `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`:
  - Round start: rc 0 (`controls/census-before.txt`).
  - Round end: rc 0 (`controls/census-after.txt`). The only findings are the pre-existing W04 warnings.
- Rows, counted with `grep -c '^ \{0,3\}|[[:space:]]*S[0-9]\{3,\}[[:space:]]*|' corpus/SOURCES.md`: 218 → 220.
- Rows added by tier: A +2 — S482 (spec, RFC 5861) and S483 (dataset, RFC 5861 errata search). Both
  opened 2026-11-05, status `mined`.
- Rows touched (old → new): `used-by` of S469, S457 and S461 each gained `corpus/knowledge/stale-extensions.md`.
  The lesson Gate lists the exact old and new cells.
- Frontier advanced: RFC 5861 serving-stale ground. The README has a new `## Round-98 frontier step` section.
- Sourced claim: C2 rests on S482, which is cited by `corpus/knowledge/stale-extensions.md`.
- Assimilation: none. `.ufo/waves/round-98/assimilation/` shows 218 registry ids against 129 staged ids,
  with 8 collisions (S312 S329 S367 S372 S373 S374 S390 S409). No renumber map exists, so nothing was appended.
- considerthese: proposal 2 of `considerthese/2026-11-05.md` (seat-yield ledger) was taken as QUALITY
  criterion R98-B in the lesson.

## Trend verdicts

| Trend | Verdict | Evidence |
|---|---|---|
| expansion | improved | New RFC 5861 ground: S482/S483, `corpus/knowledge/stale-extensions.md` and a working capability that the frozen counter scored met. |
| quality | improved | R98-D1 leak removed and gated; two over-claiming rows corrected; 40 admitted capabilities entered the self-assessment table (counter 46 → 0). C1 still fails its review conjunct. |
| discernment | improved | The lane's own review seat rejected 2 of its L1-written rows, and the claim was recorded unmet rather than re-scored. Attack seats routed counter blind spots (R98-1…3). No closure spot-check of this round exists yet. |

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `corpus/knowledge/shonen-ledger.json` box 1; registry rows SKILL.md:223–224 added this round
- [ ] At least one end-to-end domain task executed and logged in LOG.md — ledger box 2 status `gap` (unchanged this round)
- [~] Instructions executable by an agent without oral context — ledger box 3; new commands in SKILL.md:223–224
- [~] No cross-domain bleed (PROVINCE.md still accurate) — ledger box 4; the new entry cites no sibling lane path

## Round shape and extras

- Shape: one v1 wave (`ufo-wave-policy.json`), 13 seats.
  - Roles: scout 1, connector 1, executor 3, scribe 2, reviewer 3, critic 1, mutation-tester 1, sentinel 1.
  - Attack share: 5/13 (ReviewCapA, ReviewCapB, ReviewStale, CriticClaims, MutCounters; sentinel excluded).
  - No residual call. Round total: 13.
- Seat yield: 12/13. ReviewCapA is a dead seat: it settled with an empty final output and wrote no files
  (`w1-results.json`). It was not replaced. ReviewCapB fully covered the C1 rows (R98-D2 design).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists only `.scratch/` changes
  and untracked `C*_*.html/pdf` and `w4lines.txt` files. None of these names kake or round 98, so none is
  a kake misroot, and none was touched.
- Scratch: `/fast/scratch/hyaku/kake-r98` was removed after landing, together with ScribeLesson's residue
  file and dead ReviewCapA's leftover tree.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none.
- Open L0: R95-2, unchanged (fleet `.ufo/l0-questions.md` line 371). No new question.
