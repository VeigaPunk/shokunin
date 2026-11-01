# kasegi — round 53 report (2026-11-01)

Lane: `fleet/kasegi-shokunin` (branch `master`). Base `e276dbf6255e0cea5e70456aada7e59e971f5853` (the round-52
verifier spot-check commit). Tip `743084a827d08078e7fb638cee686809f23eefb7`, pushed to origin master. Host: Windows
workspace, `python` 3.13.15; `python3` = Microsoft Store stub (exit 49); /home and /fast absent — unchanged from
rounds 50-52.

## Work performed

Two declared claims, frozen at `.ufo/waves/round-53/claims.json` (freeze commit `23448a2`) before implementation,
plus the r52 closure's two routed items addressed first:

- **D1 carry-in (claim C1, depth:verifiability 4, the lane's lowest non-retired axis — nominal move, score HELD,
  labelled per QUALITY R58).** The expected-list equality limb of `corpus/instruments/recheck-audit.py` is repaired
  POSIX-preserving (both sides normalized; the committed list is never rewritten to host separators), and
  `corpus/instruments/knowledge-expected.txt` is synced with exactly the 2 entries the closure routed (F31
  `osv-affected-range-events.md` r50, F32 `cisa-vulnrichment-adp-enrichment.md` r51; 69 -> 71). Evidence:
  `corpus/instruments/recheck-audit.py` (commit `586cdda`); receipts `.ufo/waves/round-53/controls/c1-donothing-r53.txt`
  (base state: `expected=69 missing=69 unexpected=71` + selftest `UnicodeDecodeError` crash),
  `c1-after-selftest-r53.txt` (18 case lines all ok, exit 0), `c1-after-lane-r53.txt` (`expected=71 missing=0
  unexpected=0`, overall exit 1 stated beside its disclosed host-bound cause: strict pass=1/71 cdroot_fail=67,
  cwd_fail=3 — both byte-identical to the do-nothing baseline), `c1-catch-r53.txt` (the repaired instrument over the
  UNSYNCED base list names exactly the two routed entries: `missing=0 unexpected=2`),
  `c1-fixture-red-r53.txt` (the pre-repair bytes FAIL the fixture's exact scenario; the r31 ledger RA-expect find
  tokens stay exactly-once 1/1). Two further members of the same host-broken class were repaired and disclosed in the
  frozen sentence: selftest fixture writes pinned utf-8 (the base selftest crashed writing the em-dash fixture with the
  cp1252 Windows default), and the cwd-isolating fixture made interpreter-free (the Store stub had broken its
  want=False). The committed selftest fixture `expect-separator` pins the Windows-separator behavior host-independently
  (relpath stub emitting backslashes vs the POSIX list).
- **D2 carry-in (routed, non-claim).** One-line append-only wording correction to `.ufo/waves/round-52/claims-erratum-1.md`
  (an `Erratum (round 53)` block: the opening sentence's filed-vs-committed wording superseded — authored before,
  committed with 227d3ed, transparent in r52 freeze rev 1b). The filed sentence stays byte-identical; counts 1 -> 1
  filed / 0 -> 1 marker (receipt `controls/d2-base-greps-r53.txt`; commit `d9710d2`).
- **C2 (coverage 8, frontier 33 -> 34; score HELD — the denominator is the operator-owned lost-root 18-surface set).**
  Frontier row F34 admitted: the NVD Vulnerability Data API 2.0 response schema document — the artifact the F33 entry's
  Limits named as "the natural next capture" — grounded on NEW registry row S085 (tier A, kind spec, status mined,
  opened 2026-11-01), capture `corpus/source-snapshots/round-53/S085.txt` (sha256 `4d1c4e77...`, 10394 raw bytes — the
  same count the r42 S066 screen recorded, so the artifact is unchanged across the two opens; 13 assertions Q1-Q13
  exactly-once, `source-recheck --source S085` exit 0). S066 is re-opened under the UNSPENT term of its own flip (the
  evaluator*/cisa* mirror fields; the interface-contract term was the one F33 spent), the rejected row byte-identical,
  per the S065->S080 precedent. Evidence: `corpus/knowledge/nvd-api-2.0-response-schema.md`, README F34 row + r53
  amendment (EOF append per R6), SOURCES S085 row + search-log + 2 leads + registry bullet 84 -> 85, PROVINCE r53
  frontier amendment, `knowledge-expected.txt` 71 -> 72 sorted (commit `3ffd663`). The extended pre-freeze neighbor
  screen incl. the downstream-consumer sweep ran BEFORE the freeze commit (`controls/neighbor-screen-r53.txt`: the
  schema URL named only by the rejected S066 row and the r42 screen records; mirror fields only in F33's Limits
  disclaimer; zero consumers across corpus/source-snapshots/).
- **Claims erratum 1 (pre-results, own catch).** Two misderived after-literals in the frozen sentences superseded by
  `.ufo/waves/round-53/claims-erratum-1.md` (freeze rev 1b, commit `1b91754`) BEFORE the results landed: C1 selftest
  completeness `total=15` not 14 (the pre-written `target.md` missed in the derivation); C2 `33` inherited FAIL entry
  records not 34 — the figure BOTH cited controls printed, so the frozen sentence contradicted its own control in the
  R43 shape, after side. Both corrected figures are what the frozen sentences' own controls printed; verdicts
  unaffected. Class mined in the lesson: R25 was applied to the state literals but not to the derived literals.
- **Mistake mining (contract 2b-3):** `corpus/lessons/round-53.md` section Mistakes — 5 rows, each with class,
  evidence pointer, captured-by and fix, including the round's own worked catches: the frontier counter's first run
  FAILED the draft F34 entry (a Limits bullet beginning with an S-id parsed as an evidence-list source declaration —
  the counter's limb A working as designed), and the first D2 erratum wording QUOTED the phrase its own frozen counter
  greps (count 1 -> 2 against "frozen stays 1"), caught by re-running the counter before committing.
- **L0 routed-around (unchanged):** the 67 host-bound recheck lines, the 3 cwd_fail lines and the limb-mutation
  replay's `python3` dependency stay operator-owned disclosed debt (L0 kasegi round-50/46 unanswered; the replay reads
  `invalid:live-baseline` on every row here — disclosed in the lesson, not fixed, not re-declared as a lane target).
  The r52 planned-for-53 "figure-audit sibling" question stays open for round 54 (SCORECARD planned section).

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Freeze: claims.json + S085 capture + manifest + base receipts (c1-donothing, do-nothing-c2, d2-base-greps, s085-recheck, neighbor-screen) + freeze.txt rev 1 | round-53 entry (below) | `23448a2934cb9419bb0475d6262a458b38f2fe3a` |
| `.ufo/waves/round-52/claims-erratum-1.md` +1 line (D2 Erratum (round 53), append-only; filed line byte-identical) | round-53 entry, D2 bullet | `d9710d21b0f004f7f17eaaefa12af6c7060134ba` |
| `corpus/instruments/recheck-audit.py` (equality limb POSIX fix + utf-8 fixture writes + interpreter-free cwd fixture + expect-separator case + docstring) + `knowledge-expected.txt` 69 -> 71 + C1 receipts (after-selftest, after-lane, catch, fixture-red) | round-53 entry, C1 bullet | `586cdda48a139aeb43976e081d5f93d5bbcde4b0` |
| `.ufo/waves/round-53/claims-erratum-1.md` + freeze.txt rev 1b (two misderived after-literals superseded pre-results) | round-53 entry, erratum bullet | `1b91754b08c959df496ad0fb8cfee7c2ecfac579` |
| `corpus/knowledge/nvd-api-2.0-response-schema.md` (new F34 entry) + `corpus/README.md` F34 block + `corpus/SOURCES.md` S085 row/search-log/2 leads/registry bullet + `PROVINCE.md` r53 amendment + `knowledge-expected.txt` 71 -> 72 + counter-final + capture-binding receipts | round-53 entry, C2 bullet | `3ffd663e70cabc988de9643249b26fbad257c895` |
| `SCORECARD.md` round-53 section + `LOG.md` round-53 entry + `corpus/lessons/round-53.md` + census of record regenerated (citation-survival.md/.tsv) + gate receipt rev 2 (`CENSUS-FRESH=ok`, SCORECARD 2165 / LOG 2400 at receipt) + freeze.txt rev 2 pins | round-53 entry | `743084a827d08078e7fb638cee686809f23eefb7` |

Committed range `e276dbf..743084a`: 29 files, +1487/−164 (`git diff e276dbf..743084a --stat`).

## Before → after measurements

- **C1 (depth:verifiability, nominal, held 4):** counting command `python corpus/instruments/recheck-audit.py --selftest`
  and `python corpus/instruments/recheck-audit.py --root . --cdroot .` (lane root). BEFORE (base bytes, receipt
  `controls/c1-donothing-r53.txt`, measured at freeze over base `e276dbf`): `expect=present expected=69 missing=69
  unexpected=71 exit=1` (pure separator artifact — every expected entry "missing", every tree entry "unexpected") and
  `--selftest` crashing `UnicodeDecodeError` byte 0x97 before any case runs. AFTER (receipts
  `c1-after-selftest-r53.txt` / `c1-after-lane-r53.txt` / `c1-catch-r53.txt`, measured at `586cdda`): selftest 18 case
  lines all ok, exit 0; lane `expect=present expected=71 missing=0 unexpected=0` (limb green; overall exit 1 from the
  disclosed host-bound class only, figures unchanged); repaired instrument over the UNSYNCED list: `expected=69
  missing=0 unexpected=2` naming exactly `corpus/knowledge/cisa-vulnrichment-adp-enrichment.md` and
  `corpus/knowledge/osv-affected-range-events.md`. Do-nothing control: the base state itself (the after-state is
  unreachable without the repair — no committed counter here could name a real drift).
- **C2 (coverage, held 8; frontier measure 33 -> 34):** counting command `python
  corpus/instruments/frontier-recheck-count.py` (lane root). BEFORE (receipt `controls/do-nothing-c2-r53.txt`, base
  export of `e276dbf` built per-file 513/513): `FRONTIER-CENSUS rows=33 admitted=33 closed=3 problem-rows=30
  registry=84`, `entries=36 pass=3` (PASS F31/F32/F33 only), zero F34 lines. AFTER (receipt
  `controls/c2-counter-final-r53.txt`, at `3ffd663`): `FRONTIER-CENSUS rows=34 admitted=34 closed=4 problem-rows=30
  registry=85`, `entries=37 pass=4`, `FRONTIER-PASS F34 ids=S085`, 33 FAIL entry records all exactly
  `recheck-exit-1`, 30 row records all `missing-pass-line`; `source-recheck --source S085` exit 0; capture-binding
  `records=68 bound=68 unbound=0` exit 0. Do-nothing control: no F34 line exists anywhere in the base output.
- **D2 (routed, non-claim):** `grep -c "Filed BEFORE the implementation commit" .ufo/waves/round-52/claims-erratum-1.md`
  = 1 -> 1 (filed line byte-identical) and `grep -c "Erratum (round 53)" ...` = 0 -> 1 (receipt
  `controls/d2-base-greps-r53.txt` for the before-state, both re-derivable on the landed tree at `d9710d2`).
- **Score gaps (R26):** depth:verifiability stays 4 — the score-5 bar is unchanged (`score-gap.py`'s gated lines on the
  lost domain bases, operator-owned); coverage stays 8 — the denominator is the operator-owned lost-root 18-surface
  set; depth:density stays 9 — SKILL.md untouched. Disclosure: `python -I corpus/instruments/score-gap.py` itself
  CRASHES on this host (`TypeError` at `field_anchorcheck`, a subprocess read returning None) — another host-bound
  instrument, recorded here per R1 rather than repaired this round; the gap statements rest on the SCORECARD threshold
  lines, not on a fresh gap run.

## Sources & frontier

SOURCES.md rows before -> after: registry 84 -> 85 rows; counting command `grep -c "^| S" corpus/SOURCES.md` (before
84 data rows at base, after 85; the +1 is S085 mined, opened and captured this round). Rejections this round: none —
the round's source hunt opened exactly the deferred artifact (S085); the two other planned-for-53 leads (OpenSSF
Scorecard, CISA ADP list page) were NOT opened and are recorded as Leads, not rows. Sourced claim: C2 rests on S085,
opened this round (Gate in `corpus/lessons/round-53.md`: URL, access date, fetch provenance, 9-word located quote
`"Metric scores for a vulnerability as found on NVD."` at S085.txt:96 by `wc -w`). Census validate: round start exit 0,
round end exit 0 (the S085 W04 duplicate-url warning is the known informational multi-row class with the byte-identical
rejected S066 row — capture-binding prints `multi_row_url=7` and exits 0).

## Trend verdicts

- **expansion: improved (coverage of the frontier, not the score).** The frontier measure moved 33 -> 34 (F34 admitted
  on a first-party NIST schema artifact with 13 exactly-once pinned assertions, a zero-consumer screen, and a
  flip-disciplined re-open of the rejected S066 row); the coverage SCORE is held at 8 because its denominator is
  operator-owned — recorded, not gamed.
- **quality: improved.** The round's instrument work made a drift class catchable that was previously
  indistinguishable from host noise (the equality limb now names real drift: `unexpected=2` with both filenames,
  where the base printed 69/71 all-red artifact), and the selftest grew a committed Windows-separator fixture plus
  two same-class repairs (utf-8 fixture writes, interpreter-free cwd fixture). No owned-axis metric moved; quality
  here is the gate's discriminative power, evidenced by the receipts.
- **discrimination: improved (own-catch evidence).** The round caught and corrected its own defects before any
  closure could: the draft-entry declaration-shape defect (frontier counter limb A), the counter-literal self-quote
  (frozen D2 counter), and two misderived frozen after-literals (the erratum filed pre-results, freeze rev 1b). All
  are mined with class/captured-by/fix in the round-53 lesson; the erratum is on record rather than smoothed over.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — untouched this round
      (density guard); outside promotion verification remains required.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — unchanged this round; source and
      diagnostic work only (no SHONEN box moved; no non-author verifier named for one).
- [~] Instructions executable by an agent without oral context — the round's receipts are re-derivable from their
      own embedded commands (every control receipt quotes its command); not promotion evidence.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the r53 amendment is an appended frontier line inside the
      declared domain; S013 stays out of scope; live-target testing still refused.

Assimilation: none — shokuknow unreachable. considerthese unchanged: no new proposal file exists at round start
(`considerthese/` holds 2026-10-19..2026-10-26 only); 2026-10-26 proposal 1 already implemented (round-39
distance-to-next-score section), proposal 2 stays noted-not-adopted (full-round-scale project).

## Closure notes for the non-author judge

- Re-derivation entry points: `.ufo/waves/round-53/claims.json` (frozen predicates), `claims-erratum-1.md`
  (the two superseded after-literals + the kill-rule reading of the draft-run FRONTIER-FAIL), `freeze.txt` (rev 1 +
  1b + 2 pins), `corpus/lessons/round-53.md` (Mistakes + Gate + Limits), and the controls receipts named above.
  Known self-catches recorded, not smoothed over: the draft-entry EVIDENCE_LINE catch; the counter-literal self-quote
  catch; the two after-literal corrections filed pre-results.
- C1's verification shape, stated plainly: the equality limb is green on this host; the audit's OVERALL exit stays 1
  for the disclosed operator-owned host-bound class only (cdroot_fail=67 / cwd_fail=3, byte-identical to the
  do-nothing baseline) — the claim is the limb, not the whole-audit exit, and the frozen sentence says so.
- The limb-mutation replay is host-bound here (every row `invalid:live-baseline`; kill commands need a real `python3`);
  C1's load-bearing evidence is the committed red-before/green-after pair (`c1-fixture-red-r53.txt` driver vs the
  `expect-separator` selftest case) plus the named-drift receipt, with the r31 ledger find tokens preserved exactly-once.
- Round-start census validate exit 0; round-end census validate exit 0; committed-state gate `CENSUS-FRESH=ok` (rev 2,
  over the truly final tree: SCORECARD 2165 / LOG 2400 at receipt); S085 recheck exit 0; capture-binding exit 0.
- Scratch `scratch/kasegi-r53` deleted at round end (it held only the base export and receipt-run intermediates; every
  committed receipt is in `.ufo/waves/round-53/controls/`).
