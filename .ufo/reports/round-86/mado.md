# mado round 86 — hyaku run 15, attempt 2

Lane repo `/home/vgpnk/Projects/shokunin/mado-shokunin`. Base `a722c60493f24f83429112e9123058835b2cdd82`.
Attempt 1's in-flight bytes are preserved at `f72bba01` (its L1 died on a provider failure; that
commit is not a landed round). Declaration/instrument freeze `237ecf4e69a4986108f719f3beeafe111adaa033`.
Final lane tip **`500bef3c8782788b1e3b327845a3a0694b8594fe`**, pushed (`ls-remote` below).

## Work performed

The round declares **two claims**, each one axis-move with its own counter, control and
before→after:

1. **C1 — calibration: refusal *records*, not cause substrings.** The lane's refusal counter bound a
   refusal with `" cause=<token> " in stdout`, so an all-cause flooding tool scored 72/72 (r85
   spot-check §C1; QUALITY 141 named the fix without a detector). After: the refusal is one record —
   exactly one `MADO_BARFOOT: ERROR (stage=…` line, its stage and (where bound) its cause equal to the
   witness, and no vocabulary token outside that record's own cause — so the flood scores 48/75 while
   the held rule still scores it 75/75.
2. **C2 — operability: clause observation and the anchor witness.** The runbook counter matched 36/36
   with four of its own mutants alive (33/37) because deleting a clause could not lower a perfect
   score, and both frozen anchor patterns already carried `^`/`$` (r85 spot-check R1). After: the
   sample loop, the negative loop and the line-anchor branch are observed per case and a declared
   clause that did not run makes the case incorrect; one row (`border-size-int`, unanchored `[0-9]+`
   under `anchor: line`) supplies the witness the anchors needed. 37/37 matched, 37/37 killed.

Both counters are live: `quality/counters/c1-r86-refusal-records.py` (75 cases, 51 mutants, 72
carried) and `quality/counters/c2-r86-clause-observations.py` (37 cases, 37 mutants, 27 shapes).

Work items:

- **Protocol load and fresh-start reads** — `skill://shokunin`, MISSION/AXES, PROTOCOL, MISSION,
  AXES, CORPUS, LEARNING from `/home/vgpnk/Projects/shokunin`; lane `SKILL.md`, `PROVINCE.md`,
  `SCORECARD.md`, `corpus/QUALITY.md`, `corpus/README.md`; the three rejected closures and their
  spot-checks (`corpus/lessons/round-8{3,4,5}-verifier-spotcheck.md`), `round-85.md`, and
  `considerthese/2026-11-04.md`. Evidence: `LOG.md:4221–4244`.
- **Freeze** — declaration `.ufo/waves/round-86/claims-declaration-r86.md`, both counters, both
  control sets, the new runbook row: `237ecf4e`. The counters shipped by the dead attempt were run
  **before** anything was frozen; all four runs and the three repairs are in
  `.ufo/waves/round-86/receipts/instrument-repair-r86.md` (M86-1..M86-3). C1 needed no repair.
- **C1 control and measurement** — `receipts/control-c1-r86.txt` (flooding 48/75, held rule 75/75,
  honest 75/75, 72/72 carried) and `receipts/final-c1-r86.txt`
  (`cases=75 correct=75 mutants=51 killed=51 base_correct=75/75 carried=72/72 tool_selftest=152/152
  flooding=48/75 held_flooding=75/75 verdict=TARGET_MET`, rc 0, `rev=3afdb713`).
- **C2 control and measurement** — `receipts/control-c2-r86.txt`, `receipts/control-held-rule-r86.txt`
  (the r85 instrument at this tree: 36/36 with `killed=33`, the four survivors alive),
  `receipts/final-c2-r86.txt` (37/37, 27/27 shapes, 37/37 clauses observed, 37/37 kills,
  `held_rule_new_case=0/1`, rc 0, `rev=8528dfa6`).
- **Source work** — S491 (RFC 7493 §2.3) and S492 (CPython `re.rst` `fullmatch`) fetched, pinned and
  quoted from the bytes: `fetch/S491.bin` (12,849 B, sha256 `a44ccf14…`, quote at line 159) and
  `fetch/S492.bin` (78,262 B, sha256 `d252cc18…`, quote at line 957); `LOG.md` records the quote
  correction to the pinned bytes (`e2d7f63a`, M86-8).
- **Knowledge and lesson** — `corpus/knowledge/refusal-records-clause-observations-r86.md` (indexed,
  frontier bullet) and `corpus/lessons/round-86.md` (M86-1..M86-9, Gate with both rows and three
  rejects, census, considerthese, domain share).
- **Wave** — ONE v1 wave of 14 seats under `ufo-wave-policy.json` (band 8–16), spec/dispatch/ready
  `w1-spec.json`, `w1-dispatch.json`, `w1.ready` (landed `b24b03aa`), seats' reports under `w1/`,
  settlement `w1-results.json` + `receipts/final-wave-r86.txt`
  (`seats=14 dispatched=14 settled=14 verdict=OK`).
- **Harm watch at the round tip** — `final-index-r86.txt` 107/107; `final-ledger-r86.txt`
  population 158, ledger 158, uncovered 0, bad_pointer 0; `final-gate-r86.txt` 460/460;
  `final-axis-r86.txt` checked 3, mismatched 0; `selftest-c{1,2}-r86.txt` 127/127 and 114/114;
  `census-start/end-r86.txt` both exit 0.

## Landed changes

| change | LOG.md | commit |
|---|---|---|
| Attempt-1 in-flight bytes preserved (not a round) | `LOG.md:4221` | `f72bba01` |
| Declaration, both counters, both control sets, three pre-verdict instrument repairs | `LOG.md:4221–4244` | `237ecf4e` |
| Knowledge entry, lesson, registry rows S491/S492, SCORECARD row | `LOG.md:4235–4243` | `01be4234` |
| Counters registered in `SKILL.md` + instrument ledger, axis row re-derived | `LOG.md:4244` | `b33afc08` |
| Control receipts and the wave's findings on the frozen instruments | `LOG.md:4254–4264` | `3afdb713` |
| Wave attacks, source re-grounding, final C1 receipt (`rev=3afdb713`) | `LOG.md:4254–4272` | `8528dfa6` |
| Seat corrections and final C2 receipt (`rev=8528dfa6`) | `LOG.md:4264–4273` | `78baa05a` |
| Source quotes corrected to the pinned bytes | `LOG.md:4265–4268` | `e2d7f63a` |
| Wave spec, dispatch and ready handoff | `LOG.md:4270–4273` | `b24b03aa` |
| Settled wave, seat reports, final measurements, wave receipt | `LOG.md:4273–4280` | `e6b72872` |
| Freeze-revision receipt's provenance limit recorded | `LOG.md:4273–4280` (same entry, correction appended) | `500bef3c` |

Pre-report gate: `git -C mado-shokunin ls-remote origin refs/heads/master` →
`500bef3c8782788b1e3b327845a3a0694b8594fe refs/heads/master`.

## Before → after measurements

### C1 — calibration (refusal records)

```sh
python3 -I quality/counters/c1-r86-refusal-records.py --repo . --rev REV \
  --base-rev 2b6dd76b65de4dfe701db87db13b7e448b3538ee \
  --controls .ufo/waves/round-86/controls/c1-cases-r86.json \
  --carried .ufo/waves/round-85/controls/c1-cases-r85.json --scratch-root DIR
```

| | before (held r85 rule / held r85 tool) | after (r86 record rule) |
|---|---|---|
| honest tool | 75/75 | **75/75** |
| all-cause flood | **75/75** (gap 0/75) | **48/75** (gap 27/75) |
| mutants | — (r85 counter refuses a 75-case population: exit 2) | **51/51 killed** |
| carried cases | 72/72 | 72/72 parsed-equal |

Measured at `3afdb7136904b70b0a01ac31963b6e9b14320f1f` (`receipts/final-c1-r86.txt`, rc 0);
re-runnable at `500bef3c` with the same inputs (the counter and the tool are unchanged since
`3afdb713`; `git diff 3afdb713 500bef3c -- quality/counters/c1-r86-refusal-records.py
tools/mado-barfoot.py` is empty).

**Verdict: measured predicate TARGET_MET; not admitted as a causal proof.** The wave found reachable
holes in the *rule* that the predicate cannot see: `w1/R86ReviewerC1.md` scores four forgery classes
75/75 (stderr flood, one-leading-space duplicate record, result-path flood, homoglyph flood), and
`w1/R86CriticClaims.md` §(a) shows the negative observation exempts the record's own cause token by
identity rather than by position, so an own-cause echo tool scores 75/75 against a binding that
forbids the token outside the record. Both are routed to r87 with executable inputs.

### C2 — operability (clause observation)

```sh
python3 -I quality/counters/c2-r86-clause-observations.py --repo . --rev REV \
  --controls .ufo/waves/round-86/controls/c2-cases-r86.json \
  --carried .ufo/waves/round-85/controls/c2-cases-r85.json --scratch-root DIR
```

| | before (r85 instrument, 36 cases) | after (r86, 37 cases) |
|---|---|---|
| rows matched | 36/36 | **37/37** |
| declared clauses observed | not observed | **37/37** |
| mutants killed | **33/37** (four survivors) | **37/37** |
| held rule on the new witness | — | **0/1** |

Measured at `8528dfa665fbf34cf3c671cd683098c95d9b1637` (`receipts/final-c2-r86.txt`, rc 0,
`tree=bound`). At the freeze revision the same 37/37 was reproduced independently by the wave critic
from an extracted copy of `237ecf4e` (`w1/R86CriticClaims.md`, fixture `e6787d6b`); the seat's own
`receipts/final-c2-freezerev-r86.txt` is **not** cited as freeze evidence — it is byte-identical to
`c2-repaired-r86.txt` except its `rev=` cell, and the provenance limit is recorded in `SCORECARD.md`
(post-wave correction) and routed.

**Verdict: measured, improved, with a named limit.** The four survivors die exactly where claimed
(`w1/R86CriticClaims.md` §(e): both anchor mutants fail only `border-size-int`). A count-preserving
stub still passes case-level clauses (`w1/R86ReviewerC2.md` F1/F2): the observation counts calls, not
evaluations. Routed.

### Harm watch (no axis harmed within the exercised scope)

Navigation 107/107 (106→107, the new entry); calibration resolved-active 86/86; operability selftest
12/12, ledger 158/158 (156→158, two counters); standing gate `MADO_SELFTEST: 460/460`, byte-identical
this round; census rows 425→427. Receipts under `.ufo/waves/round-86/receipts/` (`final-*`). This is
the exercised scope, not a claim of global absence of harm.

## Sources & frontier

Census command (both ends, paste-ready):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado
```

- **Before:** exit 0 (`receipts/census-start-r86.txt`), 425 rows, standing `W04` duplicate-URL
  warnings unfiltered (…S490).
- **After:** exit 0 (`receipts/census-end-r86.txt`), **427** rows. Count:
  `git show master:corpus/SOURCES.md | grep -c '^| S[0-9]'` → 427 (425 at `237ecf4e~1`).
- **Rows added by tier:** S491 (RFC 7493 I-JSON §2.3, `spec`, tier **A**) and S492 (CPython v3.14.8
  `Doc/library/re.rst`, `docs`, tier **A**) — two rows, both `mined`, recheck 180d / on-release.
- **Rows touched old→new:** none — no status, `recheck` or `used-by` change to an existing row; the
  append is additive. Both new rows carry their access date (2026-11-04), byte span and ≤25-word
  located quote in `corpus/lessons/round-86.md` §Gate (S491 bytes 6364–6437, S492 bytes 39792–39901),
  plus three rejects with flip conditions.
- **Frontier rows advanced:** `corpus/README.md` index 106 → **107** (`MADO_INDEX: 107/107 missing=0
  dangling=0 duplicates=0`, `final-index-r86.txt`) with one new frontier bullet
  (`corpus/README.md:139`); the new entry is lane-internal instrument ground, said so in the lesson's
  domain share (1 new entry, 0 new tools, 1 desktop-facing runbook row).
- **Sourced claim:** C1 rests on S491 (duplicate member names are a MUST NOT in I-JSON, not the RFC
  8259 SHOULD already held as S486); C2 rests on S492 (`fullmatch` is whole-string, `search` is not).
- **Assimilation: none** — no `merge/mado/` package entry was adopted this round (no package entry
  passed the province/QUALITY bar against this round's claims). `considerthese/2026-11-04.md`
  proposal 2 is mined as QUALITY 145 in the same round, which is not package adoption.

## Trend verdicts

- **expansion — improved.** Two admitted source rows (425→427) and one indexed knowledge entry
  (106→107) on ground the corpus did not hold: what makes a refusal a *record* and what makes a
  matched row's *clauses* observed, both with the held rule's false green measured beside them
  (flood 75/75 → 48/75; 33/37 → 37/37 kills). The one desktop-facing row added is a read
  (`hyprctl getoption general:border_size`), not a new desktop claim.
- **quality — improved.** Both instrument judgements are now falsifiable in ways they were not, and
  the increment is demonstrated against the held instruments rather than asserted: the flood gap and
  the four survivors are re-measured at the round tip (`control-c1/c2`, `control-held-rule`). Three
  failing instrument runs are retained (`instrument-repair-r86.md`), the quote was corrected to the
  pinned bytes, and the freeze-revision receipt's provenance limit is recorded instead of repeated.
- **discernment — improved.** The wave's dissent is recorded, not absorbed: the critic's axis-label
  dissent, the identity-not-position exemption hole, the kill-rule under-enumeration, the
  separability dissent and the two-convention refusal judgement are all in the lesson's routed table
  with executable repairs; the mutation tester's 12 surviving counter mutants are named with inputs.
  The lane corrected its own evidence claim (provenance) in the round that could have let it stand.

## SHONEN

One line per box of `SHONEN.md` (4 boxes; `grep -c '^- \[' SHONEN.md` → 4). No `[x]` this round: no
named non-author verifier has been recorded yet (outside-lane closure pending).

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer:
  `SKILL.md:231` (round-85 runbook table) and `SKILL.md:301` (round-86 section, one row bound to
  `S492`'s whole-line rule); the standing gate's selftest is `receipts/final-gate-r86.txt`, 460/460.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md:4273–4280`
  (the wave's seats re-executed both counters end to end; the critic reproduced C2 from an extracted
  freeze fixture) and `receipts/final-c{1,2}-r86.txt`.
- [~] Instructions executable by an agent without oral context — pointer: the declaration's counting
  commands plus `corpus/knowledge/refusal-records-clause-observations-r86.md` §3–§4; four seats ran
  them from the declaration alone, one of them on a clean extracted tree.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `w1/R86ConnSiblings.md` (connector
  overlap scan: no kumitate/tameshi tool or method acquired; the two-convention judgement is named as
  a lane-internal debt, not a sibling claim) and `PROVINCE.md` unchanged this round.

## Round shape and seats

- ONE v1 wave under `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy.json` (band 8–16):
  **14 seats** — executor 3 (`R86ExecC1`, `R86ExecC2`, `R86ExecControl`), scribe 3
  (`R86ScribeEntry`, `R86ScribeLesson`, `R86ScribeSources`), scout 2 (`R86ScoutRunbook`,
  `R86ScoutSources`), reviewer 2 (`R86ReviewerC1`, `R86ReviewerC2`), critic 1 (`R86CriticClaims`),
  mutation-tester 1 (`R86MutationTester`), sentinel 1 (`R86Sentinel`), connector 1
  (`R86ConnSiblings`). The L1 held the canonical planner seat (the validator refuses `planner`).
- Attack share: reviewer×2 + critic + mutation-tester + sentinel = **5/14 (35.7 %)** ≥ 25 %.
  Connector seats: 1 ≤ 2.
- Dead seats: **none** — `w1-results.json` carries 14 result rows, every `output` non-empty, and 14
  substantive reports under `w1/` (r85's null-telemetry defect does not repeat). Residual call: none.
  Round total **14**.
- Dispatch: `w1.ready` (l1 `MadoR86`) taken at 2026-11-05T00:16:54; wave receipt
  `receipts/final-wave-r86.txt` → `seats=14 dispatched=14 settled=14 verdict=OK`.
- Seat-report path defect (mine): one item's text still named `R86LabRunbook.md` after the item was
  renamed for the scout role; the file was renamed to `R86ScoutRunbook.md` at integration with content
  untouched (M86-9).

## Inherited state (attempt 1)

Attempt 1's L1 died on a provider failure; its in-flight bytes are preserved at `f72bba01` and are
**not** a landed round. Reused after re-verification: the declaration (kept unchanged), both
counters (re-run before the freeze — three C2 repairs, receipts retained), the control sets, the
wave spec/dispatch/ready handoff. Discarded: nothing from the counters' *verdicts* — every number
cited here was produced by a run of the frozen bytes. Named: the C2 instrument's first three runs
(anchor drift, self-contradicting observation, two mutations drifted onto the held control) are
receipts, not hidden history.

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` → `.scratch/run15-state.json` (orchestrator),
`.ufo/reports/round-90/kotodama.md`, `mo.tip` (other lanes/orchestrator). **No mado seat file at the
fleet root**, so nothing to relocate. `.scratch/` untouched.

## Open L0 questions

None raised or appended this round (`grep 'mado | round-86' .ufo/l0-questions.md` → empty). Carried
open questions (r57–r60, the L2 floor, the host-recovery pacman pause, the r37/r38 session-material
history) remain operator-owned and are not treated as answered.

## Stale-lane

Respawn-per-round driver; this process worked round 86 only and no other mado mission is open.

## Tool installs

None this round — no install, upgrade or provider probe; `pacman` stayed paused.

## Seat-authored material referenced

`w1/R86ExecC1.md`, `w1/R86ExecC2.md`, `w1/R86ExecControl.md`, `w1/R86ScoutRunbook.md`,
`w1/R86ScoutSources.md`, `w1/R86ScribeEntry.md`, `w1/R86ScribeLesson.md`, `w1/R86ScribeSources.md`,
`w1/R86ReviewerC1.md`, `w1/R86ReviewerC2.md`, `w1/R86CriticClaims.md`, `w1/R86MutationTester.md`,
`w1/R86Sentinel.md`, `w1/R86ConnSiblings.md` — all committed at `e6b72872`; the two seats' own
scratch helpers (`w1/ctrl-held-rule.py`, `w1/ctrl-r86-controls.py`) are kept as evidence, not as
instruments.
