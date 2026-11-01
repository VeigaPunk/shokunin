# kaidoku round 54 — the routed-record repair round: ten routed round-53 defects close with receipts

## Work performed

Fresh-start round, L1-inline on the Windows host (no wave surface; the kaidoku
round-53 L0 question on the L2 floor stays open and unanswered — routed around, never
treated as answered). Round base `45c6878634c16caa8e3e63472b30e439581b3a0d` (the r53
spot-check commit). Commit chain: declaration `9dc73005…` → freeze `5f768669…`
(LOG entry only; ordering defect M54-4) → freeze contents `85843f2e…` (the operative
freeze: first commit adding `.ufo/waves/round-54/claims.json` + every wave receipt) →
landing `c753b24f…` → record `8f1c3fa7…` → close `90f3a9b9…` (pushed; local main ==
origin/main at filing). The only executed instrument is the frozen
`tools/round-53/r53-record.py` (bytes unchanged since round 53, pin `c9fd8c68…`
re-derived by the gate at the landing and at the tip); every other measurement is a
plain counting command over committed bytes.

- **Fresh-start compliance:** r50/r51/r52 (all `rejected-honest-stop`, digests in the
  rendered prompt §7), the r53 spot-check, and the r53 plans' fresh-start section were
  read before declaring. **Ruled out, with reasons:** (1) the AVM LE-SquashFS
  Frontier→Core C1 — REA 6.5.0, sasquatch/sasquatch-v4be, unblob and vendor fetches are
  absent on this host (PROVINCE `## Host migration — 2026-10-31`); three rounds died
  re-attempting it; routed findings stay routed. (2) The `census3` outside-13
  registry-drift census (r53's planned second item) — sized out: this is the
  repair-first round; declaring it would repeat the r51/r52 shape (a second declared
  claim that does not land). (3) A frozen-instrument portability pass (r53's planned
  third item) — the frozen bytes are pinned; a port is a new instrument needing its own
  freeze and battery; stays planned, never a silent patch. (4) Any wave dispatch — no
  surface on this host.
- **R54-C1 (calibration — a lowest-axis claim; all three owned axes tied at 10.0)** —
  the nine routed-record closures D1,D2,D4,D5,D6,D7,D8,D9,D10
  (`corpus/lessons/round-53-verifier-spotcheck.md` §6 items 1,2,4,5,6,7,8,9,10), each
  with a committed, content-checked artifact. Evidence:
  `.ufo/waves/round-54/l1/scores/c1-before.txt` (0/9 at the base, committed at the
  freeze), `.../scores/c1-after.txt` (21/21 checks pass at the landing `c753b24f…`).
- **R54-C2 (depth)** — SKILL rule-block 27 prose/table agreement: the drifted clause
  ("the `clean` row itself narrows its census cell to `partial,readable`") removed; the
  prose now attributes `partial,readable` to `legacy-body-failure` and states the clean
  row's `*` under the two census-conditioned guard rows. Evidence:
  `.../scores/c2-before.txt`, `.../scores/c2-after.txt`, `.../c1-v6-at-landing.json`.
- **Frontier/protocol work:** SOURCES **S254** opened this round (RFC 6962, rfc-editor
  plain text, fetched read-only 2026-11-01; snapshot bytes + sha256
  `.ufo/waves/round-54/l1/s254/`, `08fdf31c…`); C1's D5 (the freeze-ledger
  correction-entry convention, `corpus/QUALITY.md` row 100 + the new
  `corpus/claim-freezes-corrections.tsv`) is grounded in its append-only log model
  (§7.3: a log misbehaves by "violating its append-only property by presenting two
  different, conflicting views"). The r53 INSTRUMENT_NONE container shape was avoided,
  not shaped away: the round-54 container names the instrument path in a frozen-atom
  value, so the R29 gate audited it and returned **CLEAN**.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| Declaration (plans/round-54-claims.md + fresh-start ruled-out set) | "round 54 — declared" | `9dc73005d5b961f5b2b953c63e17d6f06ab24f39` |
| Freeze: claims container (pins the frozen r53 oracle), census-start, before-arms, record receipts (selftest/battery/tip-repro/E11), misroot artifacts, S254 snapshot | "round 54 — freeze recorded" | `5f768669…` (LOG only; M54-4) + `85843f2ec7feef3f44c285df455233cb865202f9` (files) |
| Landing: QUALITY row 100; corrections ledger + `round-53/correction-1`; knowledge-entry `## Corrections (round 54)` (provenance trio, pointer fix, 35-vs-31 erratum); SKILL block-27 prose alignment; r53 lesson Gate correction (3 reject rows + spot-check); round-54 lesson (Gate with rejects, Mistakes M54-1..M54-4); SOURCES S254; ledger row round-54 | "round 54 — landing" | `c753b24f96db335eeeca0003d2906457d6e71849` |
| Record: SCORECARD round-54 section (atoms T1-T12, receipts, record-corrections sub-block); after-receipts; gate receipt; M54-5 | "round 54 — record landing" | `8f1c3fa7ed7c988e81ed4e2da73c6df239e3c8df` |
| Close: census-end receipt (exit 0, 19 standing W04) | "round 54 — close" | `90f3a9b9d3970ae87173787521a821132c10c66c` |

Per-defect closure map (all ten routed items):

1. **D1 provenance trio** — appended correction block carries
   `verified-at:`/`recheck:`; the original 100 header lines are byte-identical
   (sha-checked in `c1-after.txt`).
2. **D2 dangling pointer** — correction names `s253/digests.txt` with the full control
   digest `89ff4a11fa260bcd…4c4`; the absent `control-sha256.txt` path was never
   created (`git cat-file -e` still fails).
3. **D3 block-27 prose** — R54-C2 above; the v6 marker-block table bytes are
   byte-identical base→landing (sha256 `b340ed2b…` both) and the frozen
   `tools/round-53/sqfs-triage-v6.py` re-scores 0/0/0/0 at the landing.
4. **D4 receipts** — `records/c2-selftest-receipt.json` (the frozen oracle's
   `--selftest`: 32 cases, pass 32, fail 0) and `records/c2-control-battery.txt`
   (junk-record / forged-receipt / falsified-wave arms over the frozen oracle in a
   scratch fixture; 3/3 red on exactly their atom; the ≥10-mutation arm is the
   selftest).
5. **D5 correction convention** — `corpus/QUALITY.md` row 100 + companion ledger
   `corpus/claim-freezes-corrections.tsv` with `round-53/correction-1` recording the r53
   in-place verdict-correction event; append-only, S254-grounded; the gate-governed TSV
   stays gate-owned (a correction row there would be a stray — measured reasoning in
   the lesson's Gate reject 2).
6. **D6 390-hit retention** — `misroot/r53-broad-sweep-retained.txt` (regenerated
   2026-11-01: fleet root 0 hits, lane-checkout root 272 vs the original 390; drift
   disclosed inside, not reconciled) + pointer corrections in LOG and the SCORECARD
   record-corrections block (the filed report is fleet-owned and stays as filed).
7. **D7 35-vs-31** — erratum in the knowledge-entry correction block and the SCORECARD
   record-corrections block, with both counts and their counting targets: pinned JSON =
   31 fixture rows + 1 lineage + 4 family totals (counted in `c1-after.txt`); 35 is the
   round-50 receipt table.
8. **D8 lesson Gate** — r53 lesson gains an appended Gate correction with three explicit
   reject rows and the spot-check result; the round-54 lesson's own Gate carries
   candidates/admitted/rejected/spot-check.
9. **D9 tip reproduction** — `records/c2-after-tip-7c0630ce.json`: the frozen oracle at
   rev `7c0630ce…`, freeze `6ead6f1b…` → exit 0, `mismatches []`, verdict `met` (the r53
   report's unreceipted claim, now receipted).
10. **D10 E11 revision** — `records/census-e11-repro.txt`: the M53-4 failure reproduced
    from committed bytes (SOURCES@`94efae0d…` + the S253 row verbatim inside the
    Registry table + the entry present + the lesson absent on disk) → exit 1 with the
    exact `E11 S253 missing used-by corpus/lessons/round-53.md` line.

## Before → after measurements

- **R54-C1:** before — at the base `45c68786…`, 0 of 9 closures present
  (`scores/c1-before.txt`; per-check commands and outputs transcribed). After — at the
  landing `c753b24f…`, 21 checks pass / 0 fail; 9/9 closures content-checked
  (`scores/c1-after.txt`). Representative counting command (D5):
  `git show c753b24f…:corpus/claim-freezes-corrections.tsv | grep -c '^round-53/correction-1\t'`
  → 1 (base: `git cat-file -e 45c68786…:corpus/claim-freezes-corrections.tsv` → exit 1,
  absent). Measured at `c753b24f…`.
- **R54-C2:** before — `git show 45c68786…:SKILL.md | grep -c 'row itself narrows its
  census cell to'` → 1. After — `git show c753b24f…:SKILL.md | grep -c 'row itself
  narrows its census cell to'` → 0; v6 marker-block table sha256 `b340ed2b…` identical
  at base and landing; `python -X utf8 -I -B tools/round-53/sqfs-triage-v6.py --root .
  --rev c753b24f… --freeze 764e6ed8… --envelopes
  .ufo/waves/round-42/w1/artifacts/R42C2ReconLegacy/envelopes --json-out <OUT>` →
  exit 0, `pair_mismatches 0`, `evaluator_missing 0`, `executability_violations 0`,
  `clean_residue 0`; command A at the landing → mapped 142/142,
  `citation_resolved_rules 27`. Measured at `c753b24f…`.
- **No axis harmed:** `git diff 45c68786..90f3a9b9 --numstat -- SKILL.md` = 1/1 (the
  one prose line); PROVINCE.md = no diff; LOG.md = 37 insertions / 0 deletions
  (append-only); the SCORECARD Owned-axes depth/calibration/coverage rows are
  byte-equal base→landing (the record section is an appended section); frozen
  instrument bytes unchanged (`r53-record.py` sha `c9fd8c68…` re-derived by the gate at
  the landing and at the tip `90f3a9b9…`); freeze gate at the tip: exit 0, disclosures
  29/29 exact, no stray, no missing.

## Sources & frontier

`corpus/SOURCES.md` rows 160 → 161 (S254 only). Counting command:
`git show 90f3a9b9…:corpus/SOURCES.md | grep -c '^| S'` → 161 (base `45c68786…` → 160).
S254 (RFC 6962, tier A spec) was opened this round by curl (datatracker first returned
the HTML rendering; replaced with the rfc-editor origin — both recorded in the lesson's
Gate row) and grounds C1's D5; snapshot bytes + sha256 committed at
`.ufo/waves/round-54/l1/s254/`. Census: start exit 0 / end exit 0, 19 standing W04
warnings both ends (receipts `.ufo/waves/round-54/l1/census-{start,end}.txt`); W04
stays named debt. Mistakes mined: M54-1 (registry reconstruction order — E12 masked the
target E11), M54-2 (fixture-root confusion — stale lane hashes passed to fixture runs),
M54-3 (stale docstring on the frozen oracle — erratum, bytes untouched), M54-4
(helper directory arguments are not expanded — the split freeze, disclosed), M54-5
(receipt authoring — the E11 receipt carries exit+line but no verdict line; checker
derives it; landed receipt not rewritten).

## Trend verdicts

- **expansion: unchanged** — no Frontier→Core move; PROVINCE.md untouched (no diff
  base→tip); S254 grounds a record-keeping form, not a surface; SOURCES 160→161 is the
  only registry growth.
- **quality: improved** — all ten routed round-53 defects closed with committed,
  content-checked artifacts (the spot-check's §6 list is fully discharged); the
  block-27 surface is made self-consistent with its scored table with the frozen
  instrument re-scored green; the freeze-ledger gains the correction convention the
  spot-check asked for, and the asserted-but-unreceipted r53 artifacts are receipted.
- **discernment: unchanged** (pending the outside spot-check, not self-certified) —
  the round executed the previous closure's routed repairs verbatim and self-routed
  five new mistakes (M54-1..M54-5) plus one ordering defect (M54-4) into the lesson;
  every verdict above rests on re-runnable commands over committed bytes.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited
  sources — pointer: SKILL.md craft section (27 rule blocks; command A at
  `c753b24f…`: `citation_resolved_rules 27`, map 142/142, receipt
  `.ufo/waves/round-54/l1/scores/c2-after.txt`); this round made block 27's prose
  agree with its scored table.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer:
  the round's end-to-end task is the receipted repair of the round-53 record (LOG
  entries "declared" → "close"; the frozen oracle executed for three receipts; the
  freeze gate run green at the landing and tip).
- [~] Instructions executable by an agent without oral context — pointer: every
  after-check is a pasteable command over committed bytes, transcribed with outputs in
  `.ufo/waves/round-54/l1/scores/c1-after.txt` / `c2-after.txt`; a non-author can
  re-run them at `c753b24f…`/`90f3a9b9…`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: PROVINCE.md has no
  diff base→tip (`git diff 45c68786..90f3a9b9 -- PROVINCE.md` empty); S254 is recorded
  as grounding a record-keeping form, not an REA surface.

No SHONEN box is self-issued `[x]`; all four remain `[~]` with resolvable pointers
pending non-author verification.

Assimilation: none — shokuknow unreachable; `considerthese/` does not exist in this
lane (measured at round start).
