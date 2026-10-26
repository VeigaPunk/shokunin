# kasegi round 37 — report

Lane HEAD at filing: `2387dcf6ccfefcfb703783387b9aade8fc82abfa` (pushed; `git ls-remote origin refs/heads/master` = same). Claims frozen in `.ufo/waves/round-37/claims.json` (commit `224df74d`), with claims-erratum-1 (`b3620681`, pre-data) correcting the C2 capture URL to the SSVC overview tutorial page.

## Work performed

Fran claims:
- **C1 — depth:verifiability (score 4, held).** Landed `corpus/instruments/r37-closure.sh` (export-mode suite E1–E14, digest `0da98e37…`, `bash -n` clean, plain-run refusal exit 2) closing the round-36 verifier spot-check's routed defects D1–D6. Measured at the final lane head `2387dcf6`: `closed=14/14 exit=0`; `--selftest` → `cases=14 failures=0`; required reds — r36 base `cc692008` export → `closed=4/14 exit=1`; r36 judged head `a23dc478` export → `closed=7/14 exit=1` (E10–E14 open there). Receipt `.ufo/waves/round-37/final-gates/all-gates.txt` (genuine transcript of the F1 run, `all-gates v1` header, suite digest bound, 14 E-lines, 14 selftest case lines).
- **C2 — coverage (score 7, held).** Admitted frontier F20 (SSVC — Stakeholder-Specific Vulnerability Categorization, CERT/CC) 19→20; registry S054 (tier A, mined, opened 2026-10-26, kind docs); entry `corpus/knowledge/ssvc-stakeholder-specific-vulnerability-categorization.md` (`source: S054`, Q1–Q6-compliant); capture `corpus/source-snapshots/round-37/S054.txt` (518 lines, 32,623 B, sha256 `ff3f3b2c…`) + manifest (3989 B, `fabc3163…`); junk twin `c2-controls/junk-f20.md` rejected by source-recheck (`MISMATCH reason=quote-not-found` ×4, exit 1).

Wave shape: one v2 wave `kasegi-r37-build`, 64 seats (executor 18, scribe 12, reviewer 10, critic 6, scout 6, mutation-tester 5, connector 3, sentinel 2, simplifier 2; attack seats 23/64 = 35.9 %). Planner seat held by the L1 (validator rejects `planner` as a frozen-topology seat). Dead seats: 0 — all 64 receipts filed (the final seat, `MutC1Fixtures`, settled late and was committed as a follow-up; the dispatcher's `wave1-results.json` had not finalised at filing — recorded, not hidden). Residual calls: none. Round total: 64 seats. Stale-lane: no other mission of this lane is open (respawn-per-round driver). Tooling: no installs; no pacman transactions (host-wide pause). L0: kasegi round-32 question remains open (unchanged).

## Landed changes

Every change is tied to the round-37 LOG entry and to commits `224df74d` (freeze), `f3246559` (wave evidence), `b3620681` (erratum), `0acffc82` (F0 integration), `a4b6a8ca` (F0b headings), `2735e93f` (late seat receipt), `9492c776` (F1 bootstrap receipt), `aa88877b` (F2 final head — genuine gates transcript), `2387dcf6` (F3 final head — final-hash bindings)

- `corpus/instruments/r37-closure.sh` (new, E1–E14).
- `corpus/source-snapshots/round-37/S054.txt`, `manifest.json` (new).
- `corpus/SOURCES.md`: S054 registry row (11 cells, NF=13, single `https://` token = erratum URL).
- `corpus/README.md`: F20 frontier row + round-37 admission paragraph + "20/20 admitted" count line.
- `corpus/knowledge/ssvc-stakeholder-specific-vulnerability-categorization.md` (new entry).
- `corpus/instruments/knowledge-expected.txt`: 49th entry (C-locale sorted).
- `SKILL.md`: Gates & probes registry rows — `r37-closure.sh` plus the D5-corrected single-choice `r36-closure.sh` row (type `gate`, verdict map incl. exit 2 → `could-not-evaluate`).
- `corpus/QUALITY.md`: R30 (fail-closed failure paths, grounded M37-2) and R31 (considerthese disposition ledger, grounded proposal 7).
- `corpus/knowledge/considerthese-proposals-ledger.md`: round-37 18-row disposition table + re-pin note (claims.json shorthand `corpus/considerthese-ledger.md` resolved to this tracked ledger — F3 resolution).
- `PROVINCE.md`: F20 frontier amendment (end-of-file).
- `LOG.md`: round-37 entry incl. the **D2 correction** ("Correction (round 37): … `corpus/instruments/r36-fixtures/` … `git ls-tree` shows it absent — never committed").
- `SCORECARD.md`: round-37 result section (anchor-ancestor label for `c20300df`; `Final lane commit: f3246559…` ancestor binding; no stale `e666d902` label in the section).
- `corpus/lessons/round-37.md`: Gate/assimilation/considerthese/census/Mistakes + integration resolutions addendum.
- `SHONEN.md`: round-37 box lines.
- `c2-controls/junk-f20.md` (control).
- `.ufo/waves/round-37/`: claims.json, c1/c2-controls, census-before, erratum, spec/plan/dispatch/ready, 64 seat receipts, assimilation artifacts (reg-ids/staged-ids/collisions/quarantine-slice), final-gates/all-gates.txt.

## Before → after measurements

**C1** (commit measured: before `224df74d`, after `2387dcf6`):
- `bash corpus/instruments/r37-closure.sh --export-ref 2387dcf6…` → `closed=14/14 exit=0`
- `bash corpus/instruments/r37-closure.sh --selftest --export-ref 2387dcf6…` → `selftest cases=14 failures=0` exit 0
- `bash corpus/instruments/r37-closure.sh --export-ref cc692008b0cfd58d18275aa6c4aed79620120799` → `closed=4/14 exit=1`
- `bash corpus/instruments/r37-closure.sh --export-ref a23dc4788aa7c98831eed6db953434034ce5ae8d` → `closed=7/14 exit=1`
- before: suite absent (`suite_missing=1`); D1–D6 open (all-gates absent; LOG false path; stale label `Final lane commit: e666d902`; `gate|probe` type cell; `porcelain:-0`); after: all six routed defects closed (E10–E14 green), quiescent at filing (worktree clean, scratch empty).

**C2** (before `224df74d`, after `2387dcf6`):
- `grep -cE '^\| F[0-9]+ \|' corpus/README.md` → 19 → 20
- `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 53 → 54
- `grep -rlE '^source: S054 ' corpus/knowledge | wc -l` → 0 → 1
- `python3 corpus/instruments/frontier-recheck-count.py` → `entries=23 pass=23 exit=0` incl. `PASS F20 knowledge/ssvc-stakeholder-specific-vulnerability-categorization.md ids=S054 exit=0`
- `python3 corpus/instruments/source-recheck.py --manifest corpus/source-snapshots/round-37/manifest.json --source S054` → `S054:sha256 OK` + Q1–Q4 `occurrences=1` (anchors 259/277/473/68), exit 0
- `python3 corpus/instruments/capture-binding-check.py` → `records=44 bound=44 unbound=0`, exit 0
- `python3 corpus/instruments/recheck-audit.py --quiet` → `strict pass=49/49 … expect=present expected=49 missing=0 unexpected=0 exit=0`
- `ls corpus/knowledge/*.md | wc -l` → 48 → 49
- census → exit 0 (W04 S028/S029 only), before and after
- junk control: `c2-controls/junk-f20.md` rejected (4× `quote-not-found`, exit 1)

## Sources & frontier

`SOURCES.md` rows before→after: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 53 → 54 (1 added this round: S054, tier A / kind docs / status mined / opened 2026-10-26 / recheck 90d / used-by the F20 entry). Census commands (both exit 0, W04 S028/S029 only):

```
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi
```

Rows added by tier: A=1. Rows touched old→new: none (no status/recheck/used-by edits; S054 is a new row — the r24–r35 lessons' staged/quarantine `S054` id refers to a different document, noted in the lesson). Frontier rows advanced: F19 → F20 (20/20 admitted). Assimilation: none adopted — id-collision rerun registry L53 × staged 94 → 23 collisions at freeze (S031–S053), 24 once S054 lands (staged S054 is the IPA request PDF, different document); quarantine slice 7 rows verdicts (0 fabrication-class, 1 unreachable S048, 6 present-and-located with 2 quote-form defects) in the lesson Gate; standing refusals flips unmet. considerthese 2026-10-26: proposal 7 mined → QUALITY R31 + ledger; proposals 1–6 dispositions recorded (proposal 1's §Saturation thresholds plank stays open). Sourced claim: C2 cites S054, opened this round. `Assimilation: none` (no penalty clause).

## Trend verdicts

- **expansion: improved** — F20/SSVC admitted on page-level ground the corpus did not hold (20-lane sweep + kagi `ssvcV203` probe + shokuknow doctrine ruled uncontested; nearest in-lane precedent S004 is the CERT/CC disclosure policy, a different surface); source S054 tier-A mined; entry cites it.
- **quality: improved** — round-36 verifier's routed defects D1–D6 close and are re-verifiable via the committed r37 suite (green at final head, reds at r36 base/judged head, selftest 14/14, fixed-point E10 receipt protocol); S054 recheck + junk twin exercised; no admitted entry failed a re-check; R30/R31 criteria added from mined mistakes.
- **discernment: improved** — Gate admit (F20/S054) and rejects (junk twin; quarantine rows; standing refusals) rest on measured, independently reproduced evidence (capture digest `ff3f3b2c…` reproduced across 4+ seats; manifest pins match RevEntryF20/RevSourceRecheck/ExecC2QuoteOnce); claims-erratum-1 filed before any seat scored and was applied by every affected seat.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence (round 37, final head `2387dcf6`): Gates & probes registry now carries `r37-closure.sh` and the D5-corrected single-choice `r36-closure.sh` row (E13); `anchorcheck.py SKILL.md` exit 0; density/anchor post-append re-measurement per `wave1/RevNoHarm.md`; `density.py SKILL.md` base 225.3/27 blocks/751 cites. Box stays `[~]`; no non-author check.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence (round 37): no new end-to-end domain hunt ran; closest executed measurement is instrument + admission work (C1 suite runs over exports; C2 SSVC capture/harness). Box stays `[~]`.
- [~] Instructions executable by an agent without oral context — evidence (round 37): `recheck-audit.py` strict pass=49/49 expected=49 exit=0; frontier harness entries=23 pass=23 exit=0 incl. PASS F20 ids=S054; source-recheck S054 exit 0; capture-binding records=44 bound=44; census exit 0; r37 suite `--selftest` cases=14 failures=0 and `--export-ref 2387dcf6…` closed=14/14 exit=0 (raw transcript committed at `.ufo/waves/round-37/final-gates/all-gates.txt`). Box stays `[~]`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence (round 37): PROVINCE.md F20 amendment appended; F20/S054 uncontested across 20 sibling lanes (ConnSibling/ScoutF20Sibling ruling); junk twin rejected. Box stays `[~]`.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Tooling

No installs or upgrades; no pacman transactions (host-wide pause). All work used existing host tools (bash 5.3.20, git 2.56.0, python3 3.14.8, GNU coreutils).

## WAVE-DONE addendum (appended after filing)

`WAVE-DONE kasegi-r37-build` arrived after the report was filed: all 64 seats settled, 0 dead. Results archived at `.ufo/waves/round-37/kasegi-r37-build-results.json` (64 entries with seat output) and committed at `83975acc…` — a post-measurement lane commit (claim measurements stand at `2387dcf6…`; the results commit is wave evidence, not a claim byte). The earlier "not finalised" note is superseded by this line.
