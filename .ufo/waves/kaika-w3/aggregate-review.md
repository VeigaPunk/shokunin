# Kaika round-12 final aggregate — non-author review (bounded)

**Reviewer:** FinalAggregateReview (non-author; no edits, no reruns of archives/gates).
**Targets read:** work commit `1bcf59eab527a9225152e7a912c7beb9301a11e9` (source work,
preserved) plus integrator commits `05bfb56` (schema/receipt provenance) and `ba007d8`
(report bound to work commit; main-repo SOURCES exemption) on `kaika/aggregate`.
All child reads used the original repositories at the pinned OIDs.

## Verified (independent checks, 1bcf59e + corrections)

1. **21-HEAD matrix.** Parsed all lane rows in `.ufo/reports/round-12/aggregator.md`,
   `AGGREGATE.md`, `SOURCES.md` against `local://kaika-final-lane-heads.json`: 21/21
   lanes, 21/21 exact full-OID matches, zero mismatches, no stray lane OIDs.
2. **Census sums.** Per-lane table in `.ufo/waves/kaika-aggregate/sources-census-final.md`:
   21 lanes, rows=576, A/B/C=500/33/43, mined/queued/rejected=307/220/49;
   tier sum == status sum == rows == 576 (declared values reproduce exactly).
3. **Gate table cross-consistency.** The 21 verdict/findings rows in
   `.ufo/reports/round-12/AGGREGATE.md` match the 21 exact verdict lines in
   `r12-gate-final.md` with zero mismatches; all 21 `not conformant`, exit 1.
4. **Structural-clean vs not-conformant distinction.** Gate (form: r2/r4/r7/r8-literal/
   r10/SHONEN) is `not conformant` on all 21; census/validate are exit 0 with E=0,
   W=7; `r10` on all 21 is attributed to the aggregator's own missing round-12 lesson
   under the no-child-write boundary, not to child defects. Both reports state the
   limits (r1/r3/r5/r6/r9, verifier independence, SHONEN truth not evaluated).
5. **Claim shape 7→21, score held.** `SCORECARD.md` V13: before **7** (R11 standing-duty
   record), after **21/21** at refreshed full OIDs, 0/21 conformant; numeric
   corpus-review score stays **9**; expansion/quality/discernment all "unchanged";
   index explicitly "not an axis claim, capability score, or knowledge-expansion
   count"; no knowledge entry created.
6. **Append-only ledgers.** Endpoint diff `54a20d39..ba007d8`: `.ufo/reports/AGGREGATE.md`
   +167/−0, `LOG.md` +26/−0, `SCORECARD.md` +32/−0 (pure insertions; no base line removed).
7. **Roster 13 vs physical 21.** `MANIFEST.json` at HEAD: `roster` len 13, `rounds`
   len **320**; reports keep the 13-entry operator-controlled roster distinct from the
   21 physical local repositories. No MANIFEST/PROTOCOL/ROADMAP/roster/mint change in
   the aggregate commit.
8. **No authority flip.** README wording: canonical protocol is
   `kimi-shokunin@e737d2ea…`, vendored copies "not a second" authority, "configuration
   and historical annotations do not override canonical rules"; fleet root has no
   `corpus/` (verified absent), so the added "main-repo lanes hold no corpus/" marker is
   accurate. SHONEN marks remain report-local; no `[x]`/promotion/verifier claim.

## Spotchecks against pinned registries (agree/disagree)

- **Admitted route — audio §Paths:29, `S009 → S010 → S011 → S008 → S013`.** At
  `0462a544`: line 29 text matches; `S011` row (line 19) is tier **C**, status
  **rejected**, recheck `on-release`, flip = tutorial revision/engine source showing
  `compress/mode 0` as 4.4 default. Index says "4 mined, 1 rejected; S011 explicitly a
  rejected counterexample" → **AGREE** (parent's S011-is-right reading confirmed).
- **Admitted route — kagi §Paths:26, `S001 → S004 → S002 → S003 → S006 → S007`.** At
  `c2cab35`: sequence matches exactly; all six rows tier A, status **mined**, each
  `used-by` the lane's `onepassword-machine-credentials.md` entry. Index "6 mined; rows
  point to the lane's knowledge entry" → **AGREE**.
- **Excluded route — game-dev-3d §Paths:48, `S012 → S011 → S035`.** At `3118be0`:
  line 48 is that exact bullet; `S036` (line 44) declares "supersedes S011" (build-commit
  pin) and the path text never references S036. Index exclusion claim → **AGREE**.
- **Excluded route — mado U2 §Paths:55, `… → S029 → S030`.** At `7dcb785`: line 55 is
  that path ending at `S030`; `S030` row (line 41) status **rejected**, `used-by` `—`;
  search-log line 91 records the in-place mined→rejected flip and the distinct-anchor
  flip condition; the path carries no caution marker. Index exclusion claim → **AGREE**.

## Findings by severity

- **None blocking.** Core evidence (HEAD matrix, census arithmetic, gate matrix, ledger
  append-only, roster separation, spotchecks) reproduces.
- **Low / already corrected:** aggregator.md:76 "96-check receipt is
  census-indent-final-smoke.txt" — that receipt has **93** `killed` checks;
  `canonical-final-checks.txt` has **96**. Corrected at `05bfb56` (now attributes 93 to
  the indent receipt, 96 to canonical-final) and restated in the LOG errata. **Fixed.**
- **Low / already corrected:** aggregator.md:82 cited pre-cutover blob `5eae1063…` as
  "the committed canonical schema" (163/314). Governing canonical is
  `kimi-shokunin@e737d2ea` (schema blob `43b0f37c…`, contains `supersedes`/`entry`,
  i.e. supports `supersedes.entry`); MANIFEST `rounds`=320. Corrected at `05bfb56`,
  with proof file `.ufo/waves/kaika-w3/final-schema-check.json`. **Fixed.**
- **Low / residual (one line, optional):** `sources-census-final.md` still reads
  "Parent's child-only-root / 96-check evidence is `census-indent-final-smoke.txt` and
  `fleet-source-integration-smoke.txt`". Minimal correction if desired: drop "96-check"
  there (or say "93-check indentation receipt"). The LOG errata already states the
  93/96 split, so this is errata-covered, not a claim defect.
- **Note (no fix):** `.ufo/reports/AGGREGATE.md:2277` retains the stale 5eae1063/163/314
  sentence; the appended erratum at line 2289 explicitly supersedes it. Append-only
  pattern, correct as designed, but requires reading to the end.

## Residual risk and verification gaps

- Gate semantics remain form-level (r1/r3/r5/r6/r9, verifier independence, SHONEN truth
  not evaluated); `not conformant` is not a semantic defect verdict.
- Census validates structure, not that URLs were opened, anchors/`teaches` hold, or
  `used-by` targets cite the row; `overdue=0` is not "all fresh" (symbolic cadences).
- Audio lane was graded via streamed archive + `--repo` live interface (1.39 GB >
  1 GiB snapshot buffer); its verdict is explicitly not a `--snapshot` result. Three
  original checkouts carry user-owned untracked paths; no whole-tree clean claim.
- I did not rerun gates/census/archives or re-open external URLs; spotchecks cover four
  routes, not all 21 registries. No child corpus or original repo was written.

## Recommendation

**ADMIT bounded coverage.** The claim (per-repo R12 review surface 7 → 21 at named full
OIDs, with a pointer index) is supported by reproducible structural evidence, the score
stays 9 with no knowledge-expansion inflation, ledgers are append-only, and the roster
13 / physical 21 and authority boundaries are preserved. The two flagged metadata errors
are corrected in the integrator commits; only the one-line `sources-census-final.md`
wording residual remains, and it is already covered by the LOG errata.
