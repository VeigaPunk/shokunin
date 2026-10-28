# kasegi — round 43 (attempt 1)

Lane `kasegi-shokunin`; base `ab98fac9dce87130bc4f66de89e30650d63943dc`; lane tip `dbd2e106e35ac5ad14ea80f4c634d3fbf11853fb`
(remote `master` matches). Round shape: **one v2 wave** (`ufo-wave-policy-v2.json`, band 64–128) — 73 seats, all 73
settled with non-empty output, **0 dead seats** (`.ufo/waves/round-43/kasegi-r43-hyaku-results.json`). Role mix:
executor 23, reviewer 11, scribe 10, scout 9, critic 7, mutation-tester 5, connector 2, sentinel 2, revenger 2,
simplifier 2; attack share 23/73 = 31.5 %.

## Work performed

Declared claims (frozen before data in `.ufo/waves/round-43/claims.json`, digest `a4c03e1e…`, freeze record
`.ufo/waves/round-43/freeze.txt`, controls committed first): **C1 on `depth:verifiability` (score 4)** — a new
closure suite whose six new checks make the round-42 verifier's narrative defects machine-gradable; **C2 on
`coverage` (score 8, capability acquisition)** — an executable gate for the six-file claim-package contract with a
worked exemplar on one public disclosure captured this round.

- C1: `corpus/instruments/r43-closure.sh` — export mode only (plain run exit 2; unresolvable ref prints
  `ref-not-found`, exit 1), nineteen checks emitted in numeric order: K1–K7 and K9–K13 carry the r42 J-checks
  verbatim from the export's own `r42-closure.sh` (payload grammar and replay limbs unchanged), K8 is the round-43
  receipt check, K14–K19 are six limbs under `corpus/instruments/r43-limbs/`. Evidence: the suite plus
  `.ufo/waves/round-43/final-gates/all-gates.txt` (J-run receipt) and the two ref-bytes transcripts
  `r42-at-de09313-{run,selftest}.txt`.
- C1 routed defects: RD42-1 (`SCORECARD.md` correction literal), RD42-2/3/4 (`LOG.md`, `corpus/lessons/round-42.md`),
  RD42-5 (`de09313` ref-bytes transcripts), RD42-6 (`.ufo/waves/round-43/claims-erratum-1.md`), RD42-8
  (`.ufo/waves/round-42/claims-erratum-5.md`) — each closed by an appended `Correction (round 43)` line and graded
  by K14–K18.
- C2: `corpus/instruments/claim-package-check.py` (eight rules, one `RULE <id> verdict=` line each, then
  `package=… rules=8 pass=… fail=… verdict=WELL-FORMED|DEFECT`), companion `claim-package-selftest.py`, exemplar
  `corpus/instruments/fixtures/claim-package/exemplar/`, nine `defect-<k>-<class>` fixtures, entry
  `corpus/knowledge/claim-package-gate.md`, capture `corpus/source-snapshots/round-43/S067.txt` +
  `manifest.json`, registry rows S067 (mined) and S068 (rejected, reason + flip), coverage-map note.
- Connector seat (`ConnCrossClaims`) supplied the landing order (E0–E10) and four measured requirements, all
  followed (round-42 erratum for K17, no `closed=` literals in lane records, entry-before-rows for the census).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| claims freeze, controls, freeze record, v2 spec + dispatch (73 seats) | `## Round 43` | `4cb6d4ae` |
| C2 gate, selftest, exemplar, nine fixtures, S067 capture + manifest, registry rows, entry, coverage note | `## Round 43` | `5b4a8503` |
| `Correction (round 43)` lines (RD42-1/2/3/4), claims-erratum-5 (RD42-8), claims-erratum-1 (RD42-6) | `## Round 43` | `a6c1d462` |
| C1 suite + six limbs | `## Round 43` | `ffe197d1` |
| round records (lesson, LOG, SCORECARD, SHONEN, QUALITY R43–R46, considerthese ledger), suite patch, wave evidence | `## Round 43` | `9e6800ea` |
| K15/K18-clean lesson wording; 19-case selftest on hard-linked mutant trees | `## Round 43` | `6c360f4c` |
| restore SCORECARD/SHONEN/QUALITY/ledger after an L1 truncation defect and re-append the blocks | `## Round 43` | `0a24364d` |
| run summary counted from payload lines; K18 mutant removes both transcripts | `## Round 43` | `f2dee6c0` |
| wave settlement (73/73, 0 dead), late seat deliverables, results file, LOG correction, J-run receipt | `## Round 43` | `2448a7d2` |
| K8 accepts the J-run receipt at Y | `## Round 43` | `2fccc781` |
| K8 runs after every other check; payload lines emitted in numeric order | `## Round 43` | `3634ec94` |
| **receipt Y** (J-run tee) | `## Round 43` | `fdc20ad6` |

## Before → after measurements

| claim | axis | before (base `ab98fac9`) | after (Y) | counting command |
|---|---|---|---|---|
| C1 | depth:verifiability | suite absent (run exit 127); the r42 stand-in over the base export prints `closed=12/13 exit=1` while all six routed defects sit in committed bytes (`c1-controls/do-nothing.txt`) | **19 of 19 closed at Y** — `closed=19/19 exit=0`, `selftest cases=19 failures=0`, nineteen graded case lines all `verdict=pass`; K8 grades the committed J-run receipt (`payload-match=18/18`, `forged=3/3`). The committed receipt is the J-run tee (18 of 19, K8 alone open) and the at-Y transcript `.ufo/waves/round-43/final-gates/all-gates.at-Y.txt` carries the 19/19 run | `bash corpus/instruments/r43-closure.sh --export-ref <Y> --receipt-out <path>`; `--selftest --export-ref <Y>` |
| C2 | coverage | gate absent; registry 66; knowledge 61; binding 56/56; audit expected=61 (`c2-controls/before.txt`) | **verified**: exemplar `rules=8 pass=8 fail=0 verdict=WELL-FORMED exit=0`; nine fixtures `verdict=DEFECT exit=1` on their own rule; `selftest cases=10 failures=0` with the degenerate always-pass control rejected; registry 68 (S067 mined, S068 rejected); knowledge 62; binding 57/57; audit expected=62; frontier harness `entries=28 pass=28`; census exit 0 | `python3 corpus/instruments/claim-package-check.py corpus/instruments/fixtures/claim-package/exemplar`; `--selftest`; the nine C2 counters in `claims.json` |

## Sources & frontier

SOURCES: registry **66 → 68** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Rows added:
one tier-A `mined` (S067 — curl project advisory CVE-2025-9086, opened 2026-10-28, capture
`corpus/source-snapshots/round-43/S067.txt`, 109 lines, sha256 `7e35413a…`, six anchored quotes) and one tier-B
`rejected` (S068 — GitHub Advisory Database GHSA-v676-f8gm-92r9 republishing NVD's record, reason + flip in the
row and in the lesson Gate block). Rows touched old→new: none of the 66 pre-existing rows changed a status,
recheck or used-by cell. Census before: `.ufo/waves/round-43/census-before.txt` — `W04 S028`, `W04 S029`, `ok`,
exit 0. Census after (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`): the same
two `W04` warnings and `ok`, exit 0. Capture binding 56 → 57 bound, 0 unbound; `recheck-audit` 61 → 62 entries;
frontier harness `entries=28 pass=28`; frontier rows **unchanged** (F01–F25, 25/25 admitted; the round moves
documentation ground to an instrumented surface instead, recorded in the `corpus/README.md` round-43 note).
**Assimilation: none** — the §10 collision check was re-run read-only (66 lane ids vs 94 staged, 36 collisions,
all source-distinct apart from S042), nothing adopted, no renumber map filed; the round's C2 source is a §2b row
minted this round, never a staged-package adoption.

## Trend verdicts

- **expansion — improved.** Registry 66 → 68 (one mined row opened this round, one recorded reject with its flip),
  knowledge 61 → 62, and a new executable capability (`claim-package-gate`) enters the SCORECARD repertoire table
  with its demonstration command and output.
- **quality — improved.** The r42 suite was green while six routed narrative defects sat in committed bytes; K14–K19
  now grade exactly those classes, each red at base and each rejecting a mutant built from the committed defeat
  bytes, and the missing `de09313` transcript is committed so the one unbacked quote is bound. The C1 suite's own
  selftest is green on nineteen cases.
- **discernment — improved.** The gate is exercised against one real public disclosure with `claimable: false` and
  its operator gates named, nine deliberate defects are rejected by their own rule, and a degenerate always-pass
  gate is rejected; the round reports the C1 receipt as 18 of 19 with K8 open rather than dressing the
  self-reference as a pass.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` byte-unchanged this round; the two new instruments are registered in `corpus/instruments/README.md` and the lesson, not yet as `SKILL.md` Gates & probes rows (`.ufo/waves/round-43/w1/ScribeShonenLines.append.md`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — the claim-package exemplar is package-shaped and gate-checked but `claimable:false` with operator gates open; no submission performed (`corpus/instruments/fixtures/claim-package/exemplar/claim_checklist.md`).
- [~] Instructions executable by an agent without oral context — `corpus/instruments/r43-closure.sh` and `claim-package-check.py` run from a cold checkout with documented CLIs (`.ufo/waves/round-43/final-gates/all-gates.txt`, `corpus/knowledge/claim-package-gate.md` recheck line, exit 0).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` byte-unchanged; the gate is ruled disjoint by `.ufo/waves/round-43/w1/ScoutSiblingOverlap.md` and within province by `.ufo/waves/round-43/w1/CritProvinceScope.md`.

## Mistakes (mined this round, in `corpus/lessons/round-43.md` § Mistakes)

- **M43-1 (stale premise, mine).** The first C1 predicate froze a base figure its own control contradicted
  (`closed=13/19` vs the measured `closed=12/13`); caught by R22/R25 through the control receipt before dispatch.
- **M43-2 (landing, mine — new this filing).** Four append scripts truncated `SCORECARD.md`, `SHONEN.md`,
  `corpus/QUALITY.md` and `corpus/knowledge/considerthese-proposals-ledger.md` (`open(p,'w').write(read(p)…)` opens
  the target for writing before reading it); detected by the suite's K1/K11 payloads collapsing to 9 corrections,
  repaired by restoring the four files from base `ab98fac9` and re-appending the blocks (`0a24364d`). Captured by
  K1/K11; the fix is shown able to fail (the truncated tree printed `K1 records=0` and `K11 corrections=9`).
- Routed by the round-42 verifier and closed this round: RD42-1, -2, -3, -4, -5, -6, -8.

## Open / routed forward

- **C1 K8 self-reference (closed by the at-Y transcript).** The committed receipt is the J-run tee and cannot contain
  its own closure; the 19/19 measurement is the at-Y run committed at `dbd2e106`
  (`.ufo/waves/round-43/final-gates/all-gates.at-Y.txt`). Round 44 should keep that two-file shape explicit.
- `ExecSuiteSkeleton` delivered a 2339-line suite after the L1's composed suite was landed; the seat's bytes are
  kept as wave evidence (`w1/ExecSuiteSkeleton.r43-closure.sh`) and reconciling the two is routed to round 44.
- L0 questions carried: round-41 F24/RFC 9116 shared ground with kake (unanswered; F24 stays parked).

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Tooling

None installed or upgraded: no pacman transaction (host-wide pause honoured), no `uv tool`, no `npx`, no PATH write.
