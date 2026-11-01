# kasegi — round 55 report

Lane: `fleet/kasegi-shokunin`, branch `master`. Base `ed60637394b170a4120fda501b9b9c5387f2df24` (the round-54 non-author
closure tip, verdict admitted=true). Round head: **`133c575394099abf28ddf1b0125c53aefde3e0fa`**, pushed to origin (verified
`git ls-remote`). Commits (all through the plumbing helper, all pushed): freeze `fd7838c` → carry-in `d0237d6` → C1 `00832d2` →
C2 `d9d77ec` → results `133c575`.

## Work performed

- **Carry-in addressed first (routed, status-neutral, not counted as claims) — DF-1 and DF-2 from the round-54 closure**
  (`corpus/lessons/round-54-verifier-spotcheck.md` §2/§4, both verified from committed bytes before any landing): (DF-2)
  `controls/d53-base-greps-r54.txt` was cited by cfdf059's corrections file, the LOG entry, the SCORECARD section and the
  report but never committed — the regenerated receipt landed as `.ufo/waves/round-54/controls/d53-base-greps-r54.txt`
  (commit `d0237d6`) naming the same five sha pins (SOURCES@base `06c92e6a…`, nvd entry@base `15eb2d05…` = tip, receipt
  `be69ece7…`, manifest `eb6ffa60…`, capture `4d1c4e77…`), the four filed literals each exactly once at base and the
  measured 542/7590/33 — every limb re-run live this round before landing, so every citation of the path now resolves.
  (DF-1) the r54 report/freeze prose "0 mentions in base SCORECARD/LOG/knowledge-expected" contradicts the receipt it
  cites: the SCORECARD limb prints **2** (receipt lines 12-14; base bytes re-derive 2 at SCORECARD.md:2102,:2158 — the
  r52-planned/r53-routed "figure-audit sibling" routing text; the LOG/knowledge-expected limbs are 0/0 as filed) — the
  prose figures superseded by 2 in the appended R9-form erratum `.ufo/waves/round-55/controls/df1-mentions-erratum.md`
  (commit `d0237d6`) with a runnable closure check printing `df1-erratum=closed` exit 0; no filed byte edited (the r54
  report is fleet-repo record committed by the orchestrator; the erratum is the lane-side record of the correction).
  Both classes are mined in the round-55 lesson and machine-caught from now on (the C1 ledger entries, below).
- **C1 — depth:verifiability (4, the lane's lowest non-retired axis); capability extension; score HELD, labelled nominal
  per QUALITY R58.** The round-54 move-log figure audit grows 9 → 17 pinned figures (commit `00832d2`): the round-54
  figures fold in rev-pinned to `5108584aab38a1919992c46d0224f6ec1cb59363` (frontier-rows-r54 35, registry-rows-r54 86,
  entries-r54 38 via the F-row entry-cell comma split, knowledge-expected-r54 73, knowledge-files-r54 73) and the DF-1
  do-nothing mention counts are pinned machine-checkably (figure-audit-mentions-base-scorecard 2 — naming the superseded
  filed-prose 0, mentions-base-log 0, mentions-base-knowledge-expected 0 via awk whole-count so a zero prints with exit
  0). Evidence: selftest `cases=5 failures=0` exit 0 (`controls/c1-selftest-r55.txt`); GREEN over the lane root
  `FIGURE-AUDIT figures=17 ok=17 stale=0 exit=0` (`controls/c1-green-lane-r55.txt`, run before any C2 byte — every new
  derive addresses committed revs or the invariant FAIL-record count 33 = 38−5 = 39−6, so the audit stays green across
  C2 and is re-run green over the truly final tree in the gate receipt); RED control over the DF-1 prose figures AS
  FILED plus two wrong fold-figures reads 3 stale exit 1 (`controls/c1-red-df1-r55.txt` +
  `.ufo/waves/round-55/controls/red-df1-ledger.json`); do-nothing at base ed60637 in the freeze commit
  (`controls/c1-donothing-r55.txt`: 9 ids at base, the new entry ids 0, the base ledger 9/9 green).
- **C2 — coverage (8); frontier F35 → F36; score HELD (operator-owned denominator).** F36 = GitHub Docs' own REST API
  reference page for repository security advisories (`https://docs.github.com/en/rest/security-advisories/repository-advisories`),
  first admission of the round-47 lead (then `corpus/SOURCES.md:137`, provenance
  `corpus/source-snapshots/round-47/S076.txt:574` — the lead line's bytes unchanged, flip recorded in the
  registry-changes bullets), on new registry row S087 (tier A, docs, mined, opened 2026-11-01). Capture
  `corpus/source-snapshots/round-55/S087.txt` (3407 lines, 137738 snapshot bytes over 937712 fetched HTML bytes, sha256
  `3eebdf476fbfe5040ad3367edfe3961fbda1bff412bb74ee43bb08ab2f754b93`; three same-sha instrument opens this round plus
  two byte-identical raw-HTML curl opens; normalization strip-cr-tab = no-op at byte level, 0 CR / 0 TAB), manifest with
  14 assertions Q1-Q14 each occurrences=1 at its pinned anchor (`controls/s087-recheck-r55.txt`, exit 0). Entry
  `corpus/knowledge/github-repository-security-advisories-rest-api.md`: attribution, 4 falsifiable claims with rejected
  over-generalizations (the twelve-endpoint family with per-endpoint permission tiers and the list endpoint's
  unauthenticated public-resource carve-out; the POST/PATCH create-update pair with the required-body contract and the
  closed published/closed/draft state vocabulary; the standalone ghsa_id-keyed 202-Accepted CVE request; the
  private-fork route that alone names a second permission set), distinctness vs F28/F29/F30 argued from the neighbor
  screen, honest Limits (rate limits / plan-gated parameters / response examples / error-body schemas unasserted; the
  live docs.github.com page pinned by sha). Extended pre-freeze screen incl. the downstream-consumer sweep run at base
  BEFORE the freeze (`controls/neighbor-screen-r55.txt`: the URL held by no README/PROVINCE/knowledge row; only F29 the
  concepts-lifecycle neighbor; zero snapshot consumers). Committed `d9d77ec`.
- **Round-55 lesson** `corpus/lessons/round-55.md`: six Mistakes rows — the two mined routed defects (DF-2 the
  unresolvable pointer; DF-1 the memory-composed prose count) plus four own-catches, three caught BEFORE their data
  landed (the v1 stand-in's incomplete declared-adds list, caught by the dry-run limb reading F36 `manifest-unreadable`;
  the export-root audit draft caught fail-closed by the derive limb before the of-record receipt; the three non-unique
  manifest quotes caught by the pre-freeze recheck's occurrences counter) and one at the capture's byte-verification
  step (the MSYS grep CR artifact, settled by a byte-level read). Gate: S087 with the 11-word located quote at
  S087.txt:2853 (`wc -w` measured, R56). Limits and the considerthese disposition recorded.
- **SCORECARD round-55 section** (result table, move log, capabilities note, planned-for-56) and the **LOG round-55
  entry** appended; census of record regenerated to its fixed point; gate receipt `.ufo/waves/round-55/controls/gate-final-r55.txt`
  `CENSUS-FRESH=ok`, measured after the last corpus/SCORECARD/LOG edit (commit `133c575`).

## Landed changes (every change ↔ LOG.md round-55 entry ↔ commit)

| Change | Commit |
|---|---|
| `.ufo/waves/round-55/claims.json` + `freeze.txt` + S087 capture + manifest + neighbor screen + do-nothing C2 + stand-in dry-run + capture-binding + S087 recheck + c1-donothing receipts | `fd7838c` |
| `.ufo/waves/round-54/controls/d53-base-greps-r54.txt` (DF-2, regenerated) + `.ufo/waves/round-55/controls/df1-mentions-erratum.md` (DF-1, R9 erratum + closure check) | `d0237d6` |
| `corpus/instruments/figure-audit-ledger.json` (9 → 17 entries) + `controls/red-df1-ledger.json` + 3 C1 receipts | `00832d2` |
| `corpus/knowledge/github-repository-security-advisories-rest-api.md`; `corpus/README.md` +29/−0; `PROVINCE.md` +2/−0; `corpus/SOURCES.md` +3/−0 (row inserted after S086, 2 bullets at EOF, zero deleted lines); `corpus/instruments/knowledge-expected.txt` 73→74; C2 final receipt | `d9d77ec` |
| `corpus/lessons/round-55.md`; `SCORECARD.md` round-55 section (+58/−0); `LOG.md` round-55 entry (+48/−0); census pair regenerated; gate receipt rev 1 | `133c575` |

## Before → after measurements (counting command + measured commit)

- **C1** (capability extension; nominal move, R58 label — the axis counter is the citation census, named non-moving):
  before `git show ed60637…:corpus/instruments/figure-audit-ledger.json | grep -c '"id"'` → 9, the new entry ids 0, and
  the base ledger over the lane root re-runs `FIGURE-AUDIT figures=9 ok=9 stale=0 exit=0`
  (`controls/c1-donothing-r55.txt`, measured in the freeze commit `fd7838c` over base bytes); after
  `python corpus/instruments/figure-audit.py` → `FIGURE-AUDIT figures=17 ok=17 stale=0 exit=0`
  (`controls/c1-green-lane-r55.txt`, run at the `00832d2`-state before any C2 byte, measured commit `00832d2`);
  selftest `cases=5 failures=0` exit 0; red control 3 stale, exit 1. The green re-runs over the truly final tree in
  `controls/gate-final-r55.txt` (17/17, commit `133c575`).
- **C2**: before `python corpus/instruments/frontier-recheck-count.py --root <base export of ed60637>` →
  `FRONTIER-CENSUS rows=35 admitted=35 closed=5 problem-rows=30 registry=86`, `entries=38 pass=5`, zero F36 lines, FAIL
  records 33 (`controls/do-nothing-c2-r55.txt`, measured in `fd7838c`) → after
  `python corpus/instruments/frontier-recheck-count.py` → `FRONTIER-CENSUS rows=36 admitted=36 closed=6 problem-rows=30
  registry=87`, `FRONTIER-PASS F36 ids=S087`, `entries=39 pass=6`, FAIL records 33 (=39−6, invariant) over the landed
  tree (`controls/c2-counter-final-r55.txt`, measured at `d9d77ec`); capture-binding 69 → `records=70 bound=70
  unbound=0` exit 0, `multi_row_url=7` unchanged 7→7 (`controls/capture-binding-r55.txt` before/after + the final
  receipt); expect limb 73 → expected=74 missing=0 unexpected=0; knowledge files 73 → 74; `LC_ALL=C sort -c` clean;
  capture 3407 lines / 137738 bytes / sha `3eebdf47…`; every C2 after-literal was dry-run green on the stand-in tree
  BEFORE the freeze (`controls/c2-standin-dryrun-r55.txt` v2; v1's capture-pair omission is recorded in the same
  receipt and mined).

## Sources & frontier

Registry rows before→after with the counting command:
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → **86 → 87** (+S087, opened this round; the
sourced claim C2 rests on it). Knowledge entries 73 → 74; frontier rows 35 → 36 (F36 admitted). Search-log bullet and
registry-changes bullets appended; no existing row's cells changed (R8; the round-47 lead line's bytes are unchanged —
its sha at base `de3270d5…` and the same line text prints exactly once at the tip; the flip is recorded in the bullets).
Round-start census validate: exit 0 (6 informational W04 rows, unchanged). Round-end census validate: **exit 0** (same
6 informational W04s). Census of record (gate receipt `controls/gate-final-r55.txt`, `CENSUS-FRESH=ok`, fixed point
confirmed over two identical runs): 215 files / 4978 distinct → **218 files / 5013 distinct** (RESOLVES 12, INTERNAL
1118, GONE 3883; total occurrences 10684; lane total 1130/5013 = 22.54%) — a bookkeeping move from the new corpus files
(the F36 entry + the round-55 lesson and their citations); no citation-resolution move claimed (R58 nominal labeling on
C1).

## Trend verdicts

- **expansion: improved** — frontier 35 → 36 (F36 admitted on a live first-party source opened this round — the
  round-47 lead's own pointer), registry 86 → 87, knowledge 73 → 74; the coverage SCORE held at 8 (operator-owned
  denominator) is recorded, not gamed.
- **quality: improved** — the figure-audit capability's ledger grew 9 → 17 with selftest (5/0), a red control that
  catches the DF-1 prose-figure class AND wrong fold-figures, and a do-nothing absence proof; no admitted entry failed
  a re-check (S087 recheck exit 0 14/14 occurrences=1; F31–F36 all PASS in the final counter run; the 33 host-bound
  FAIL records are the standing disclosed operator-owned class, unchanged); the round's own biggest mistake (the v1
  stand-in) was caught by the round's own dry-run limb before any data landed and mined the same round.
- **discernment: improved** — the carry-in landed append-only with byte pins and runnable closure checks
  (`df1-erratum=closed` exit 0; the DF-2 receipt's every limb re-run live before landing); six Mistakes rows with
  class/captured-by/fix, three own-catches before their data; the DF-1 erratum corrects this lane's OWN filed prose
  against its OWN receipt — the honest form of the same lesson the lane taught r53.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — Evidence: SKILL.md unchanged
  this round (non-target guard held at density 9); existing assertion stands, outside promotion verification still
  required.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — Evidence: LOG.md round-55 entry is source and
  diagnostic work only (the routed carry-in + instrument growth + one frontier admission); the considerthese
  end-to-end proposal remains open (named in the lesson disposition).
- [~] Instructions executable by an agent without oral context — Evidence: `corpus/instruments/figure-audit.py
  --selftest` runs green from the lane root with no oral context (`controls/c1-selftest-r55.txt`); extension of the
  round-54/47 declared-root observations, not promotion.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — Evidence: PROVINCE.md r55 amendment appended at EOF only
  (+2/−0); F36 scoped inside the domain (the repository-advisories machine interface of the disclosure platform);
  live-target testing still refused.

Assimilation: considerthese checked (newest file still 2026-10-26.md; idle stretch 2026-10-27 → 2026-11-01; all seven
proposals carry recorded dispositions in `corpus/knowledge/considerthese-proposals-ledger.md` and rounds 36-39; the
one-per-round adoption slot goes unspent) — Assimilation: none — shokuknow unreachable
