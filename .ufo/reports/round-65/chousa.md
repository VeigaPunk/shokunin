# chousa — round 65 (attempt 2)

Lane repo `/home/vgpnk/Projects/shokunin/chousa-shokunin` (branch `master`) · base `d6ed8155e9b4735639a2cf0a3e479c62f2056195` · claim freeze `f99de3bdfaaf9b4c4fa85cc55dd37b9df2ee90fd` · lane tip at report time `62b0af1538e067f014ed96d6973e9a711b9d2487` (local = remote). Attempt 1 (`ChousaR65`) froze the claims, ran the before measurements and dispatched wave `w1`, then died at 12:08 -03 without committing or filing a report; this attempt inherited its uncommitted bytes, re-verified them, implemented and measured the work, dispatched wave `w2`, and was stopped by the operator wrap-up before the wave settled.

## Work performed

Round 65 declared **two** claims, both frozen at `f99de3b` (`corpus/evidence/round65/claims.md`):

- **C1 — operability (the lane's lowest numeric axis, historical 3/10): acquire a receipt-header consistency capability** at `tools/receipt-pin.py`. Predicate `R65-C1`: `CASES=20/20 C1=PASS` iff all twenty frozen receipt-consistency cases match their exact exit and token. Counting command `python3 corpus/evidence/round65/c1-count.py --work <fresh-dir>`. **Verdict: admitted.**
- **C2 — depth (sourced): land an interpretation entry separating object identity, content digest, reported exit and execution authenticity** at `corpus/knowledge/receipt-identity-r65.md`. Predicate `R65-C2`: `ENTRY_CHECKS=10/10 C2=PASS` iff the ten frozen structural sourced-entry checks hold. Counting command `python3 corpus/evidence/round65/c2-count.py`. **Verdict: unprovable / not admitted on this counter** — wave 2 built a do-nothing control that reaches the same 10/10, so the counter attests shape, not substance.

Work items and their evidence:

- **Inherited attempt-1 state, re-verified rather than trusted** — the inherited corpus bytes (`corpus/lessons/round-65.md`, `corpus/knowledge/receipt-identity-r65.md`, registry rows S154–S157, the SKILL.md gate rows, QUALITY criterion 130, the README section) were re-derived: all four source digests in `corpus/evidence/round65/source-openings.json` re-verified byte-exact against the installed or committed files and every quote re-located (S154's OUTPUT sentence in the Git 2.56.0 man page; S155 line 31 of `/usr/lib/python3.14/hashlib.py`; S156 lines 1 and 44 of the round-64 before receipt; S157's docstring sentence).
- **Implemented `tools/receipt-pin.py`** — validates `REVISION=<40 lowercase hex>`, `EXIT=<decimal 0..255>`, `SHA256=<64 lowercase hex> <canonical repo-relative POSIX path>`, one empty separator line and a nonempty body against `git -C ROOT cat-file blob REVISION:PATH` (committed bytes, never the working tree); exit 0 `RECEIPT_PIN=PASS`, 1 `RECEIPT_PIN=FAIL …`, 2 `RECEIPT_PIN=ERROR` for usage/environment. Landed at `0a85189821322e01db06216b5cb82d2d858c19f0`.
- **Falsify wave w2 (32 seats) attacked the landed bytes and found two real defects** — the validator answered environment faults with a receipt verdict (exit 1) although the frozen contract assigns "2 usage/environment" (`R65R01` finding F1, `R65C01` finding 1), and the C2 counter's after-state is reachable by boilerplate (`R65C03`, `R65M02`). Both are recorded in `corpus/lessons/round-65.md` `## Mistakes` rows 4 and 5.
- **Fixed the exit taxonomy and landed the corrections** — `tools/receipt-pin.py` now separates the taxonomy (an explicit `git -C ROOT rev-parse --git-dir` environment probe plus an OSError branch return exit 2 with `RECEIPT_PIN=ERROR` on stderr, while receipt-content defects keep exit 1); two cosmetic quote-location imprecisions in the knowledge entry were corrected (the git-cat-file quote's `<object>` notation; the hashlib quote's span, line 31 rather than 31–32). Landed at `1df2af73a79d038edf0b62ebc5691cb579ca3445` together with QUALITY criterion 131 and the wave-2 evidence.
- **Measured at the fixed tip** — `corpus/evidence/round65/controls/c1-after.txt` `CASES=20/20 C1=PASS` exit 0; `controls/c2-after.txt` `ENTRY_CHECKS=10/10 C2=PASS` exit 0; `controls/c1-stubs-after.txt` always-pass 3/20 and always-fail 17/20, both exit 1; `controls/c1-c2-separability.txt` proves the claims are causally separable; `controls/l1-boundary-probes.txt` records the environment taxonomy and the disclosed CRLF acceptance; `corpus/evidence/round65/measurement-summary.json` indexes every run.
- **Frontier step** — registry rows 153 → 157 (S154, S155 admitted as A; S156 admitted as B; S157 rejected as C with reason and flip), zero held status/recheck/used-by cells changed; `corpus/lessons/round-65.md` mines five mistakes; the census ran at both ends with exit 0.

## Landed changes

| Change | LOG.md entry | Commit carrying it |
|---|---|---|
| `tools/receipt-pin.py` (new validator; later given the exit-2 environment taxonomy) | Round65 entry, bullets "Implementation" and "C1 after" | `0a85189821322e01db06216b5cb82d2d858c19f0`, fixed at `1df2af73a79d038edf0b62ebc5691cb579ca3445` |
| `corpus/knowledge/receipt-identity-r65.md` (new sourced entry; quote locations corrected) | Round65 entry, bullet "C2 after" | `0a85189821322e01db06216b5cb82d2d858c19f0`, corrected at `1df2af73a79d038edf0b62ebc5691cb579ca3445` |
| `corpus/SOURCES.md` rows S154–S157 | Round65 entry, bullet "Frontier" | `0a85189821322e01db06216b5cb82d2d858c19f0` |
| `corpus/README.md` round-65 coverage row and frontier line | Round65 entry, bullet "Frontier" | `0a85189821322e01db06216b5cb82d2d858c19f0` |
| `corpus/QUALITY.md` criterion 130 and criterion 131 (shape-only counter) | Round65 entry, bullets "Mistakes" and "C2 after" | `0a85189821322e01db06216b5cb82d2d858c19f0`, criterion 131 at `1df2af73a79d038edf0b62ebc5691cb579ca3445` |
| `SKILL.md` gate rows `receipt-pin` (r65), `round65 claim counters`, `round64 honest-stop instruments` | Round65 entry, bullets "Implementation" and "Mistakes" | `0a85189821322e01db06216b5cb82d2d858c19f0`, rows corrected at `1df2af73a79d038edf0b62ebc5691cb579ca3445` |
| `corpus/lessons/round-65.md` (Gate, five Mistakes rows, routed items, attempt-2 continuation, wave-2 findings) | Round65 entry, bullet "Mistakes" | `0a85189821322e01db06216b5cb82d2d858c19f0`, extended at `1df2af73a79d038edf0b62ebc5691cb579ca3445` |
| `corpus/evidence/round65/source-openings.json` (four digest-pinned openings) | Round65 entry, bullet "Frontier" | `0a85189821322e01db06216b5cb82d2d858c19f0` |
| `SCORECARD.md` round-65 verdict section, per-axis verdicts, `## Capabilities` row `receipt-header consistency checking` | Round65 entry, bullets "C1 after" and "Outcome" | `9672a2e998bff2b51d18b0df4d835bd3ae2c453f`, verdicts corrected at `36281d6989275c83bd20628c9df1a25bdd70e951` |
| `corpus/evidence/round65/controls/{c1-after,c2-after,c1-stubs-after,c1-c2-separability,l1-boundary-probes}.txt`, `corpus/evidence/round65/measurement-summary.json`, `.ufo/waves/round-65/census-end.txt` | Round65 entry, bullets "C1 after", "C2 after", "Frontier" | `9672a2e998bff2b51d18b0df4d835bd3ae2c453f`, re-issued at `36281d6989275c83bd20628c9df1a25bdd70e951` |
| Wave evidence `.ufo/waves/round-65/{w1-results.json,w2-spec.json,w2-dispatch.json,w2.ready,w2.ready.dispatched,build-w2-spec.mjs,w2/**}` | Round65 entry, bullet "Wave" | `91717322e4dc7f38d4f84010e48b832032808e0c`, `1df2af73a79d038edf0b62ebc5691cb579ca3445`, partial seat output at `62b0af1538e067f014ed96d6973e9a711b9d2487` |
| `LOG.md` Round65 entry | the entry itself | `36281d6989275c83bd20628c9df1a25bdd70e951` |

## Before → after measurements

| Claim | Before (frozen receipt) | After (measured) | Counting command | Measured against |
|---|---|---|---|---|
| C1 operability (admitted) | `corpus/evidence/round65/controls/c1-before.txt` — `CASES=0/20 C1=FAIL missing-target`, exit 1 | `controls/c1-after.txt` — `CASES=20/20 C1=PASS`, exit 0; do-nothing controls `controls/c1-stubs-after.txt` 3/20 and 17/20, both exit 1; separability `controls/c1-c2-separability.txt` (C2 stays 10/10 without the target; C1 stays 20/20 without the entry) | `python3 corpus/evidence/round65/c1-count.py --work <fresh-dir>` | tool bytes at `1df2af73a79d038edf0b62ebc5691cb579ca3445`; receipts committed at `36281d6989275c83bd20628c9df1a25bdd70e951` |
| C2 depth, sourced (not admitted on its counter) | `controls/c2-before.txt` — `ENTRY_CHECKS=0/10 C2=FAIL`, exit 1 | `controls/c2-after.txt` — `ENTRY_CHECKS=10/10 C2=PASS`, exit 0 — but the wave-2 boilerplate control also scores `ENTRY_CHECKS=10/10 C2=PASS` exit 0 (`.ufo/waves/round-65/w2/R65C03.md`, `R65M02.md`), so the after-state is reachable by a do-nothing control and the counter cannot certify the depth move | `python3 corpus/evidence/round65/c2-count.py` | entry bytes at `1df2af73a79d038edf0b62ebc5691cb579ca3445`; receipts committed at `36281d6989275c83bd20628c9df1a25bdd70e951` |

The frozen counters, the claims file and the four frozen controls are byte-unchanged since the freeze (`git diff f99de3b 1df2af73 -- corpus/evidence/round65/{c1-count.py,c2-count.py,claims.md,controls/always-pass.py,controls/always-fail.py,controls/ref-receipt-pin.py}` is empty). C1's 20/20 target is proven unreachable by a do-nothing control (3/20); C2's 10/10 target is proven reachable by one, which is why C2 is not admitted.

## Sources & frontier

Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`.

- Rows before → after: **153 → 157** (registry `corpus/SOURCES.md`).
- Rows added by tier: **A +2** (S154 `git-cat-file(1)`, S155 `hashlib`), **B +1** (S156 the round-64 before receipt), **C +1** (S157, rejected) — tiers A/B/C 118/27/8 → 120/28/9; statuses mined/queued/rejected 124/19/10 → 127/19/11.
- Rows touched old → new: **none** — zero held rows changed status, recheck or used-by (diff over held rows between the freeze and the tip is empty).
- Frontier rows advanced: **two** — `corpus/README.md` gained the round-65 coverage row and the frontier line ("an authenticated command/result binding and outside re-execution are not supplied by a local header-consistency validator"), and `corpus/knowledge/receipt-identity-r65.md` carries the four numbered claims and the limits section.
- Census before: `.ufo/waves/round-65/census-start.txt` — exit 0, 153 rows, five pre-existing W04 duplicate-URL warnings (S051, S053, S073, S074, S075). Census after: `.ufo/waves/round-65/census-end.txt` — exit 0, 157 rows, the same five warnings, final line `chousa ok /home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md`.
- Sourced claim attempted: **C2** rests on S154–S156, each opened and re-opened this round (2026-10-30) with a located quote and a digest pin in `corpus/evidence/round65/source-openings.json`; the entry landed and its sources were re-opened by an independent seat (`R65R02`: no misquote, no overreach), but the claim is **not admitted** because its counter is shape-only.
- Assimilation: **none** — the round-42 quarantine verdicts keep adoption closed, the staged package under `/home/vgpnk/Projects/shokuknow` stayed read-only and no row was appended from it. Considerthese: CT-20261026-4 (independent CJK quote spot-check) stays carried without implementation credit — a lane-dispatched review cannot supply outside independence.

## Trend verdicts

- **expansion — improved.** The repertoire grew: the `receipt-header consistency checking` capability entered the SCORECARD capabilities table with a passing demonstration (`CASES=20/20 C1=PASS`, `controls/c1-after.txt`) over a target a do-nothing control cannot reach.
- **quality — improved (narrowly).** A sourced interpretation entry landed with three pinned sources, four numbered claims and an explicit limits section, and a new gate row carries the frozen counts plus the evidence-only exemption for the round-64 counters. The improvement is bounded by two disclosed limits: the entry's counter attests shape rather than substance (C2 not admitted on it), and a fabricated body still passes the validator.
- **discernment — unchanged.** The lane's own discrimination worked (the falsify wave caught the exit-taxonomy deviation and the shape-only counter, and the L1 re-opened every source instead of trusting the inherited bytes), but no outside non-author spot-check exists for this round; wave seats are lane-authored evidence, so no discernment upgrade is claimed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `## Gates` rows `receipt-pin` (r65) and `round65 claim counters`; `corpus/knowledge/receipt-identity-r65.md` (lane assertion, no non-author verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md Round65 entry; `corpus/evidence/round65/controls/c1-after.txt`, `c2-after.txt`, `c1-stubs-after.txt` (lane assertion)
- [~] Instructions executable by an agent without oral context — `python3 corpus/evidence/round65/c1-count.py --work <dir>`; `corpus/evidence/round65/measurement-summary.json`; `corpus/evidence/round65/controls/l1-boundary-probes.txt` (lane assertion)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md`; `corpus/knowledge/receipt-identity-r65.md` `## Limits` (generic testing stays adjacent to tameshi, receipt/dispatch lifecycle to kumitate) (lane assertion)

## Round shape, waves and seats

- Shape: **two v1 waves, 96 seats total** (band 64–128; hard ceiling 256). No residual call.
- `w1` (inherited from attempt 1, dispatched 11:47 -03): 64 seats — executor 20, critic 20, scribe 12, scout 8, connector 2, reviewer 2. `w1-results.json` records 64 results: **55 seats returned output, 9 returned empty output** (dead seats: Attack03, Attack06, Attack19, RegistryDraft, ScoreDraft, ReadmeDraft, Considerthese, Assimilation, SourceGit — reported as dead, never replaced); six further seats returned output without leaving a report file in the wave folder (Attack10, EntryDraft, LessonDraft, SourceReject, PriorClosure, SourcesCensus).
- `w2` (falsify, dispatched by this attempt): 32 seats — executor 8, scout 8, reviewer 4, critic 4, scribe 4, mutation-tester 2, connector 2; attack share 10/32 = 31%. Spec `.ufo/waves/round-65/w2-spec.json`, dispatch `.ufo/waves/round-65/w2-dispatch.json`, ready `.ufo/waves/round-65/w2.ready` (+ `.dispatched`).
- **Wave-2 settlement: 29 of 32 seats reported; three seats (R65D01, R65D03, R65S07) were released un-settled when the operator stopped the run.** No WAVE-DONE handoff arrived for w2, so no settlement is claimed for those three seats and none was re-spawned; R65D01's partial draft is committed as partial evidence at `62b0af1538e067f014ed96d6973e9a711b9d2487`. The §3 L2 floor (at least 8 L2 seats in one batched call) was met inside `w1`.
- The L1 holds the canonical planner seat (a planner seat is never a swarm role); a bounded planning data-walk rode the scout and connector seats.

## Known limits, routed items and open questions

- **Fixed-case oracle (C1).** `R65M01` mutated the validator 11 ways: 6 killed, 5 survived. Every survivor is a coverage gap of the frozen 20-case list, not a defect of the shipped validator — the pristine tool rejects all four live probes (whitespace body, `./SKILL.md` path, a receipt for a nonexistent blob carrying the empty-blob digest, and a 2-line receipt). The `..` guard is an equivalent mutant, since git refuses every `..` path in `rev:path` syntax. A successor freeze could pin those cases; this round does not rewrite the frozen counter.
- **Shape-only counter (C2).** The after-state is reachable by boilerplate (`R65C03`, `R65M02`); QUALITY criterion 131 records the rule that a depth claim on a structural counter needs a separate source/claim review and a do-nothing control committed before the freeze.
- **Forged body.** A consistent header can carry a fabricated body; `RECEIPT_PIN=PASS` proves header/blob consistency, never that a command ran (`corpus/knowledge/receipt-identity-r65.md` `## Limits`, lesson Limits).
- **CRLF acceptance.** The validator accepts CRLF receipts (universal-newline read plus `splitlines()`); the frozen cases pin no byte-exact line endings, so this is a disclosed behaviour rather than a measured failure (`corpus/evidence/round65/controls/l1-boundary-probes.txt`).
- **Round-64 routed items** (`corpus/lessons/round-64-verifier-spotcheck.md` section 5): item 1 — the SKILL.md cell now carries the pinned frozen counts; item 2 — the round-64 counters are registered as evidence-only honest-stop instruments; item 3 — receipts self-pin (`REVISION=`/`EXIT=` headers in `controls/c1-before.txt`); item 4 — report pointers name the lane repo explicitly; item 5 — SHONEN remains four author assertions, no promotion review manufactured; item 6 — the carried consideration pointer stays without credit.
- **Open L0 questions** (unchanged, routed around with local reads only): external fetch scope and receipt identity. No new L0 line was needed and none was filed; the fleet's existing lines cover both.
- **Stale-lane:** none — this was the lane's only open mission this round; the respawn-per-round driver holds no other chousa mission.
- **Tool installs:** none — pacman stayed paused (host-wide guard) and nothing was installed or upgraded by this attempt or its seats.
- **Misroot sweep** (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): `.scratch/goal-20261029-hyaku-run12.md` (operator-owned, untouched), `r8-in-tree-pollution.txt` ("written by invalid-args run") and `rerun-daemons.log` ("error: command not found: ./rerun-daemons.sh") — neither names chousa nor round 65, so neither was copied into the lane nor deleted; they belong to another process. No lane-authored file was found misrooted.

## Honest-stop statement

This round landed a real, counter-verified capability (C1 admitted) and a real sourced entry whose frozen counter cannot certify it (C2 not admitted), plus two defects the falsify wave found and this attempt fixed. The round is filed as an honest stop because the operator stopped it before wave 2 settled: three seats are released un-settled, no WAVE-DONE handoff arrived for w2, and C2's admission is withheld on its own counter. No settlement was fabricated and no claim was widened to cover the gap.
