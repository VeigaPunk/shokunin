# kengaku — round 61 report (hyaku run 14, 2026-11-02)

author: kengaku L1 (round 61, Windows host; instruments in WSL Ubuntu-24.04 — the canonical
counter environment). Base `f97e5b7b` (the round-60 non-author closure tip, admitted with
two status-neutral routed defects). Lane tip at report time: see CLOSURE-PREP.

## Work performed

- **R61-C1 / coverage (the lowest owned axis, L0-capped) — the seventeenth grader read and
  executed as a NEW grader class: signal-propagated cancellation semantics.** The grader:
  TB2 `cancel-async-tasks` at pin `2fd12b88` — its decisive legs spawn the candidate as a
  child process, deliver SIGINT mid-flight (capture :93/:126/:162) and price the cleanup
  discipline by counting started/cleanup markers in captured stdout (:102-103/:135-136/:171-172);
  the only `send_signal` grader in the 184-capture round-52 population (evidence:
  `corpus/knowledge/tb2-cancel-async-tasks-grader.md`, the measured negatives paragraph).
  Instrument: `plans/round61_c1_cancel_probe.py` (the r58/r59 sandbox shape; 12 declared
  candidate cases × 6 legs = 72 zero-U predictions DERIVED at run time). The class line
  and the two docstring-named traps are grounded in **S224** (opened live at the pin,
  byte-compared to the committed population capture). The round ran the battery TWICE and
  both receipts are of record: the first scored run FAILED on four author defects (receipt
  `.ufo/waves/round-61/recon/c1-first-run-FAIL.txt`, committed AS-IS, never re-scored —
  Q25); the corrected re-freeze (`plans/round-61-claims.md` Amendment 1, both instrument
  digests named) is the green of record `corpus/evidence/round61/cancel-async-probe.txt`.
  The claim is sourced (S224) and carries three class observations in the knowledge entry
  (the ThreadPoolExecutor warning is only visible at above-max; SIG_IGN is
  indistinguishable from success while the work fits the communicate window;
  threads-vs-asyncio show different no-handler signatures).
- **R61-C2 / calibration (held at ceiling 10, exercised) — the round-60 closure's routed
  defect D1 discharged with byte-true evidence.** The round-60 mirror's "byte-for-byte"
  claim was false at the byte level: measured against the authoritative append (26 lines /
  2141 bytes / sha `2a2f952c…af2a21`, still uncommitted in the fleet working tree at
  measurement — the orchestrator owns the landing; the append re-verified intact), the
  round-60 block carried 9 cp1252-double-encoded characters (5 em-dash-class + 4
  arrow-class; grounded in **S225**, the WHATWG windows-1252 index opened live this round)
  and one surplus trailing blank line; cmp differs at byte 39, line 2. The landing: the
  headerless byte-true mirror `.ufo/waves/round-61/r58-report-corrections-append-byte-true.md`
  (cmp-identical; the file IS the append, so byte verification needs no marker-stripping
  step), the dated ERRATUM appended to the round-60 mirror (defect named, status downgraded
  to the content-mirror of record; the defective bytes above the erratum untouched — they
  ARE the history the erratum describes), and the fidelity receipt
  `.ufo/waves/round-61/mirror-fidelity-receipt.txt` (runner-captured exits).
- **Carry-in and standing opens.** D1 (this round's claim C2) — discharged as above; D2
  (the round-60 report's mistake-row undercount): precision nit on a fleet-root file the
  lane does not own — named here, no lane artifact edited. r50-c1 root cause and the
  R56-F1 checker repair: CLOSED at round 58 (the SCORECARD round-58 rows: R58-C2 freshness
  9→10 with `PREDICATE R50-C1 pass`; R58-C1 operability held 10 with the falsifier
  selftests) and re-verified green in the round-60 final receipts — evidence cited,
  nothing re-opened. The three L0 questions `kengaku | round-25/33/51` (coverage cap;
  decision packet; absent surfaces) and the `kengaku | round-56` pair (L2 surface; ledger
  host column): STILL OPEN — routed around, nothing assumed answered (the cap is why C1's
  score is HELD, not raised). The `kengaku | round-52` push-protection question is already
  disposed by operator decision recorded in
  `corpus/evidence/round52/graders/EXCLUDED.md` (2026-10-28).
- **The round's own failures, mined.** Six defect classes landed in
  `corpus/lessons/round-61.md` — the freeze's own SOURCES write flipped line endings
  (repaired same-round by blob restoration + pure byte append); the simulator never read
  its declared `handler` property; `premature_start` double-printed; one hand-transcribed
  freeze-table row (the r59 class again — the fix is now mechanical: the amendment embeds
  the tool's own `--render-table` output, verified byte-identical by
  `.ufo/waves/round-61/recon/table-identity.txt`); the model's else-branch asserted
  "asyncio + handler" without checking handler; a wrong (asserted, not measured)
  before-anchor in the freeze, caught by the measured controls and dated-corrected in
  Amendment 1 addendum 2. The final-tip takes handed the lane's own gates three more live
  catches (a runner invocation defect on the entry-truth leg; two vacuous-pass clips in my
  own receipts — the r59 W2 class; a stale r35 evidence fragment — the corpus grew), all
  closed with dated errata/refreshes before the receipts of record landed.

## Landed changes

| change | commit |
|---|---|
| Freeze: claims + capture + probe + S224/S225 adoption + the C2 mirror landing + pre-freeze recon receipts | `215a7029` |
| SOURCES EOL repair (the freeze's own write defect; blob restored, pure byte append) — LOG wave F | `b9920576` |
| Amendment wave: the first run's fail of record AS-IS + Amendment 1 (four defects named, probe superseded `7d448487…f9f59` → `92facdc7…fe7f87`, table embedded byte-identically from the tool) — LOG wave A | `0e62b479` |
| Measurements: the second scored run's receipt of record + measured controls (which caught the wrong before-anchor) + claims addendum 2 — LOG wave M | `ddbb93ec` |
| Landing: PROVINCE round-61 section (17 of 89), knowledge entry + README index row, SKILL registry row, entrytruth ledger row, capability row, SCORECARD round-61 section (registration same-commit, the r58 lesson-3 rule), LOG close, lesson round-61 | `ee656c8b` |
| Receipts errata (the gate's two live vacuous-pass catches on my own receipts) | `899a1f72` |
| Cascade: block-form errata (the prose form did not convert) + the r35 fragment refresh (dated) | `52b87f5f` |
| Final-tip receipts (take 3, measured at `52b87f5f`) + the take-1 record | `9812b313` |
| Pushed-head verification (measured at `9812b313`) | see CLOSURE-PREP |

## Before → after measurements

- **R61-C1** — before (base `f97e5b7b`, measured controls in
  `.ufo/waves/round-61/measurements.txt`): the probe, capture, evidence dir and knowledge
  entry all absent (`git cat-file -e` rc=128 ×4); the frontier anchor counts 0 at base;
  SOURCES 216. After: `python3 plans/round61_c1_cancel_probe.py --lane .` →
  `cases=12 legs=72 mismatches=0 setup=0 predicted_u=0`, `PREDICATE R61-C1 pass`, exit 0
  (receipt of record sha `3a69fddb…6922a`, measured at `0e62b479`; the bare form re-executes
  the battery — it is the ledger row's entry argv and re-ran green inside the entry-truth
  legs of takes 2–4); `grep -c '17 of 89' PROVINCE.md` → 1 at the landing tip (0 at base);
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 218 (216→218).
  Measured commit: `0e62b479` (the scored run), landing `ee656c8b`.
- **R61-C2** — before (base): the byte-true mirror absent (rc=128); the round-60 block
  carries 5 em-dash-class + 4 arrow-class cp1252-double-encoded sequences, cmp differs at
  byte 39 line 2, one surplus trailing blank line (27 marker-to-marker lines vs 26).
  After: `cmp <authoritative extract> <byte-true mirror>` → exit 0 (byte-identical,
  26 lines, 2141 bytes, sha `2a2f952c…af2a21`); the erratum is the dated correction of
  record. Receipt: `.ufo/waves/round-61/mirror-fidelity-receipt.txt` (runner-captured
  exits; the before-census re-priced at the amendment tip in
  `.ufo/waves/round-61/measurements.txt`). Measured commit: `215a7029` (the landing),
  re-priced at `ddbb93ec`.

## Sources & frontier

SOURCES.md rows 216 → 218 (counting command
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; both rows opened
this round and adopted through `plans/sources_adopt.py` exit 0 — quote validation 7/7
located+bound, collisions=0, malformed=0, duplicates=0):

- **S224** — TB2 `cancel-async-tasks` scoring predicate (tier A code) at the pin, fetched
  live via curl in WSL, byte-identical to the committed r52 population capture; located
  quotes :75 and :144 (12 words each, gate-checked). Grounds R61-C1.
- **S225** — WHATWG Encoding Standard windows-1252 index (tier A docs), fetched live;
  located quotes :7/:13/:25/:27/:105 (the cp1252 byte-to-codepoint mappings that name the
  mirror's encoding defect). Grounds R61-C2.

No rejections this round; no flips of existing rows. Census (fleet tree,
`scripts/sources-census.sh validate --root <fleet root> kengaku`): round start → verdict
ok, 21×W04 (all pre-existing duplicate-url warnings), **CENSUS-START-EXIT=0** (216 rows);
round end → verdict ok, the same 21 pre-existing W04s, **CENSUS-END-EXIT=0** (218 rows).

## Trend verdicts

- **expansion: improved** — the corpus's graded-class map gained real ground: a new grader
  class read and executed (16→17 of 89, the frontier sentence 0→1), a new capability row
  (`signal-cancellation-grader-probe`, first working round 61), two new sources opened
  live (216→218). The coverage SCORE stays 7 by its standing L0 cap — the capped number is
  the operator's open question, not a trend judgment; the ground moved and is evidenced.
- **quality: unchanged** — depth 9 (the knowledge entry is additive; no entry weakened),
  operability 10 held (a probe registration, no gate moved), freshness 10 held (LOG
  re-verification lines for every touched claim; all citations resolve at the tip — the
  final batteries re-ran the whole surface green).
- **discernment: improved** — the round's own instruments caught the author at every
  stage: the first scored run failed its own frozen predicate and the fail is the receipt
  of record (committed AS-IS, re-frozen per Q25, both digests named); the freeze's own
  wrong before-anchor was caught by measuring and dated-corrected; the final takes handed
  the gates three more live catches, each closed by dated erratum/refresh before the
  receipts of record landed; the r60 closure's false byte-fidelity claim was downgraded
  where the evidence demanded it, not papered over. Six mined classes in
  `corpus/lessons/round-61.md`, each with class · evidence · captured-by · fix.

## SHONEN

SHONEN: boxes unchanged — all four `[~]` (asserted-by-author with resolvable pointers);
`SHONEN.md` untouched this round; no non-author verifier ran in-session (the L2-surface
L0 `kengaku | round-56` remains open — routed around again, nothing assumed answered).

## Assimilation, L0, routing

considerthese/ reviewed (operator-authored; not edited): the window's assimilable
proposals were already adopted (2(a) ledger_tip r37, 2(b) order_check+Q30 r39, 2(c)
tip_receipts r38) and their weaknesses were mutation-tested and wired in r40–r44; nothing
new in the queue clears this round's bar. Assimilation: none — shokuknow unreachable.
L0: the coverage-cap trio `kengaku | round-25/33/51` and the `kengaku | round-56` pair
remain open and routed around; nothing assumed answered. Routing: the fleet-root landing
of the round-58-report erratum append remains the orchestrator's (the append re-verified
intact in the fleet working tree at this round's measurement — fidelity receipt); D2 named
above. §9 sizing: both claims are do-nothing-unreachable (all C1 before-artifacts rc=128
at base; C2's before state is the false standing claim plus the absent byte-true file).

## CLOSURE-PREP

CLOSURE-PREP: kengaku round=61 base=f97e5b7b freeze=215a7029 repair=b9920576
amendment=0e62b479 measurements=ddbb93ec landing=ee656c8b receipts-errata=899a1f72
cascade=52b87f5f final-receipts=9812b313 pushed-head-verification=a6cd337d
head=a6cd337de2a1310ced222316e566e53e641e3239 pushed=yes claims=2 admitted_self=true; final receipts
`.ufo/waves/round-61/final-tip-receipts.txt` (measured at 52b87f5f: registry ADVERTISED 90
/ REGISTERED 90, LANDCHECK PASS n=4, entry-truth executed=91 mismatched=0
evidence_missing=0 laundered=0 TIPSTATE 62g/29r declared==observed, state_check PASS,
R59-C2 defects=0 errata=6 pass, probe PREDICATE R61-C1 pass exit 0, R60-C2 gate defects=0
errata=5 pass, anchor live=0, round46-c2/r51/r50 pass, r35 red-as-declared exit 1); the
pushed-head re-verification is landed at `.ufo/waves/round-61/pushed-head-verification.txt`
(measured at 9812b313: every leg green with the known self-inclusion drift named — the
landed receipts join the census: files=6878 and anchored-exit-pairs=18 at the pushed head
vs take 3's 6876/16, verdicts unchanged — the r59/r60 precedent).

Host note for the closure: the lane's Windows worktree cannot carry ~110 historical wave
files (NTFS-uncheckoutable names committed before this round) — the documented reason this
lane commits only through the plumbing helper with explicit paths and never runs
`git status`/full-tree ops; the worktree-vs-HEAD gap for those paths is pre-existing at
the round base, not round-owned. Every committed byte this round was measured on complete
WSL-native-fs clones (all scored runs and all final takes ran from fresh clones, receipts
kept outside the measured clones, exits captured inside the runners). The frozen
instruments run in WSL Ubuntu-24.04 (python 3.12.3, bwrap 0.9.0, git 2.56.0; uv/pytest
absent — the canonical counter environment).
