# kasegi — round 52 report (2026-11-01)

Lane: `fleet/kasegi-shokunin` (branch `master`). Base `6c0a08e2b99344ff3e82f8a52771af34fccc0155` (the round-51
closure tip). Freeze commit `29c4bd9dd0aa05a9276be6e3d6b35da7d9ecaa31` (claims + base evidence, landed before
implementation). Final tip **`87dfb88f21e09fd533185e20668b3408c0da3d8a`**, pushed to origin master (commits this round, in order: freeze `29c4bd9`, implementation `227d3ed`, catch-(f) fix `2df91cd`, rev-pointer finalization `87dfb88`). Host unchanged
(Windows workspace, `python` 3.13.15; `python3` = Store stub; /home and /fast absent). Post-freeze erratum:
`.ufo/waves/round-52/claims-erratum-1.md` (C1's instrument was strengthened twice while landing its receipts — the
frozen selftest/audit figures are superseded there; the kill rule only got stronger; instrument sha superseded in
`freeze.txt` rev 1b).

## Work performed

- **Carry-in first (routed by the round-51 non-author closure).** Both figure defects re-measured first-hand before
  anything was written: `printf '%s\n' "<S081 quote>" | wc -w` → **17** (lesson says 24) and `grep -c 4809
  corpus/lessons/round-50.md LOG.md SCORECARD.md` → **2/3/5** (move-log row says 2/3/2). Evidence: this report's
  measurements section; `corpus/lessons/round-51.md` Erratum 1; the SCORECARD correction-of-record paragraph.
- **C1 (depth:verifiability 4, the lowest non-retired axis — capability acquisition).** Landed
  `corpus/instruments/gate-quote-audit.py` + `corpus/instruments/gate-quote-errata.txt`: the fail-closed auditor for
  the QUALITY.md R56 word-count class (the round-48 M48-3 rule that failed twice: 16-vs-14, then 24-vs-17). Finds
  every "<N> words by wc -w" annotation in `corpus/lessons/round-*.md` (spotchecks excluded), locates the associated
  quoted string (nearest straight/curly span in a 600-char window; wrapped quotes and both filed shapes handled;
  self-referential spans — an erratum quoting the stale figure — skipped), re-measures with `wc -w` semantics, exits
  0 only when every annotation is OK (claimed == measured ≤ 25) or ERRATUM-ON-RECORD (mismatch acknowledged by BOTH
  a ledger row `file|claimed|measured` AND the lesson's own erratum text — a separate "<measured> words" occurrence
  within ±1000 chars of an erratum mention). Fails closed on unacknowledged mismatch, >25-word quote, completeness
  floor (<4 annotations), stale ledger rows (LEDGER-ORPHAN). Evidence: `.ufo/waves/round-52/controls/quote-audit-selftest-r52.txt`
  (`selftest cases=9 failures=0`), `quote-audit-before-r52.txt` + `quote-audit-before-recheck-r52.txt` (BEFORE, exit 1),
  `quote-audit-after-r52.txt` (AFTER, exit 0). Three receipt-run-caught strengthenings (self-referential-span rule; tightened
  erratum-acknowledgment; and catch (f) — the round's own lesson prose stated figures 17/24/24 in the audited
  annotation shape and the auditor flagged it over the final committed tree; prose rephrased, audit re-run green)
  are mined in `corpus/lessons/round-52.md` Mistakes and `claims-erratum-1.md`.
- **C2 (calibration — verdict row, not a number).** Both routed corrections landed append-only: (a) the SCORECARD
  round-52 section's correction-of-record paragraph names the re-measured **2/3/5** and supersedes the round-51
  move-log's "2/3/2" (filed line byte-identical); (b) `corpus/lessons/round-51.md` gains Erratum 1 naming **17
  words** with the command (filed "24 words" line byte-identical); (c) PROVINCE gains the r52 adjacency annotation
  recording the closure's S013.txt:65/F05 downstream-consumer observation (S013 stays OUT of scope) and makes the
  downstream-consumer sweep part of the standing pre-freeze screen. `git diff 6c0a08e..227d3ed --numstat` on
  SCORECARD/LOG/PROVINCE/round-51 lesson: insertions only (64/72/4/14 added, 0 deleted). The C1 receipts
  cross-verify: BEFORE exit 1 on the uncorrected tree → AFTER exit 0 once the erratum + ledger row landed.
- **C3 (coverage 8 — frontier admission, the S066 flip spent).** Admitted frontier row **F33 — the NVD API 2.0
  retrieval interface** (NIST's read-side service over the NVD-enriched CVE record: 2.0 paging envelope; NVD-Primary
  CVSS served beside CNA-Secondary with per-item provenance; CPE applicability configurations; CWE weaknesses;
  tagged references; multilingual descriptions; published/lastModified/vulnStatus change tracking; the ingested CISA
  ADP SSVC block) on registry row **S083** — a live API response for CVE-2024-3094 captured from NIST's services
  host (`corpus/source-snapshots/round-52/S083.txt`, sha256 `5c35a51b…`, 13077 bytes, 1 line, 12 assertions Q1-Q12
  each exactly-once, `source-recheck.py --source S083` exit 0). Entry
  `corpus/knowledge/nvd-api-2.0-retrieval-interface.md` with the pre-freeze neighbor screen named against
  F05/F18/F19/F25/F30/F32 AND the downstream-consumer sweep over `corpus/source-snapshots/` (receipt
  `controls/neighbor-screen-r52.txt`, run BEFORE the freeze commit). **S066's round-42 flip is spent** — its own
  flip text invited exactly this ground ("re-open if a frontier targets NVD-specific enrichments … or the API
  interface contract (resultsPerPage/startIndex pagination)"); the row stays byte-identical. Registry also gains
  **S084** (rejected with reason and flip: the developer-hub docs page serves a JS application shell — 2629 raw
  bytes → an 11-byte snapshot, `controls/s084-hub-shell.txt`, the same wall round-42 recorded — so rate limits,
  authentication and the wider parameter surface are unasserted anywhere). README F33 row + round-52 admission block
  appended at EOF (R6); PROVINCE r52 amendment appended; `knowledge-expected.txt` updated (69 entries).
- **Wave disposition — no AgentSwarm surface on this host; no seats ran.** As in rounds 49-51, the MISSION.md L2
  floor stays unsatisfiable here and is recorded as such, not simulated.
- **L0 routed-around:** the 67 host-bound recheck lines stay operator-owned disclosed debt (L0 kasegi round-50
  unanswered); no portability rewrite was attempted. considerthese 2026-10-26: proposal 1 was already implemented
  (round-39 distance-to-next-score section); proposal 2 (end-to-end domain task round) noted-not-adopted this round.
  Assimilation: none — shokuknow unreachable.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Freeze: claims.json + capture S083 + manifest + instrument rev-1 + ledger + base receipts (selftest, BEFORE, do-nothing C1, do-nothing C3, neighbor screen, S083 recheck, S084 hub shell) | round-52 entry (below) | `29c4bd9dd0aa05a9276be6e3d6b35da7d9ecaa31` |
| `corpus/lessons/round-51.md` +14 (Erratum 1: 24→17 words, command in the erratum) | round-52 entry, C2 bullet | `227d3ede15e93191f737e4973e3274509bf4599f` |
| `corpus/instruments/gate-quote-audit.py` (final, sha `396d720e…`) + `gate-quote-errata.txt` (1 row) | C1 bullet | `227d3ed` |
| `corpus/knowledge/nvd-api-2.0-retrieval-interface.md` (new F33 entry) + `corpus/SOURCES.md` +2 rows (S083 mined, S084 rejected) + `corpus/README.md` +25 (F33 row + admission block) + `knowledge-expected.txt` (69) | C3 bullet | `227d3ed` |
| `PROVINCE.md` +4 (r52 F33 amendment; r52 adjacency annotation: S013/F05 scope note) | C2/C3 bullets | `227d3ed` |
| `LOG.md` +72 (round-52 entry); `SCORECARD.md` +64 (round-52 section: correction-of-record, result table, move log, capabilities row, planned-for-53) | round-52 entry | `227d3ed` |
| `corpus/instruments/citation-survival.md/.tsv` (census of record regenerated over the final tree) + gate receipts (`c1-gate-final-r52.txt` rev 4 `CENSUS-FRESH=ok` — the receipt of record; revs 1-3 are the recorded history: rev 1 caught the SCORECARD line-count staleness, rev 3 preceded the last LOG edit, rev 4 measured over the truly final tree) + `c1-gate-selftest-r52.txt` (`cases=3 failures=0`) + counter/audit receipts (`c2-counter-final-r52.txt`, `quote-audit-after-r52.txt` rev 2, `quote-audit-before-recheck-r52.txt`) + `claims-erratum-1.md` + `freeze.txt` rev 1b/2/3/4 | census bullet | `227d3ed` + `2df91cd` + `87dfb88` |

## Before → after measurements

- **C1 (depth:verifiability):** gate-checked Gate word-count figures at base **0** (no instrument exists;
  `controls/quote-audit-donothing-r52.txt`: `git ls-tree 6c0a08e -- corpus/instruments/gate-quote-audit.py
  corpus/instruments/gate-quote-errata.txt` → both empty) → **1 fail-closed auditor + 1-row ledger** at
  `227d3ed`. Counting commands: `python corpus/instruments/gate-quote-audit.py --selftest` → `selftest cases=9
  failures=0` exit 0; `python corpus/instruments/gate-quote-audit.py` → BEFORE `annotated=4 … failures=1` exit 1
  (uncorrected r51 24-vs-17; rev-1 receipt + final-instrument re-derivation on pre-erratum bytes: MISMATCH +
  LEDGER-ORPHAN, exit 1) → AFTER `annotated=5 ok=5 erratum-on-record=2 failures=0` exit 0. Score held 4 (evidence
  capability only; the citation-resolution proxy is the score's measure and it is reported below, not gamed).
- **C2 (calibration):** corrections of record standing at base **0** → **2 + 1 scope note** at `227d3ed`.
  Counting commands: `grep -c 4809 corpus/lessons/round-50.md LOG.md SCORECARD.md` → 2/3/5 (the correction names
  these; filed "2/3/2" line byte-identical); `grep -c "Erratum 1" corpus/lessons/round-51.md` 0 → 1;
  `wc -w` on the S081 quote → 17; numstat insertions-only (append-only R9 held). Verdict row `improved`.
- **C3 (coverage):** `python corpus/instruments/frontier-recheck-count.py` — do-nothing at the 6c0a08e base export
  (per-file git show, 506/506 files; `controls/do-nothing-c3-r52.txt`): `FRONTIER-CENSUS rows=32 admitted=32
  closed=2 problem-rows=30 registry=82`, `entries=35 pass=2`, zero F33 lines → at `227d3ed`
  (`controls/c2-counter-final-r52.txt`): `FRONTIER-CENSUS rows=33 admitted=33 closed=3 problem-rows=30 registry=84`,
  `entries=36 pass=3`, `PASS F33 ids=S083 exit=0`, 33 inherited entry fails exactly `recheck-exit-1` + 30 row fails
  exactly `missing-pass-line`, both classes unchanged; `source-recheck.py --manifest
  corpus/source-snapshots/round-52/manifest.json --source S083` exit 0 (`controls/s083-recheck-r52.txt`). Registry
  rows `grep -cE '^\| S[0-9]{3} \|' corpus/SOURCES.md` 82 → 84. Score held 8 (the denominator is the lost domain
  root's 18-surface set, operator-owned; F33 moves the frontier measure 32→33).
- **Census of record at the tip** (regenerated AFTER the last corpus/SCORECARD/LOG edit; gate receipt
  `controls/c1-gate-final-r52.txt` rev 4, `CENSUS-FRESH=ok files=2` exit 0; SCORECARD 2108 lines, LOG 2333 lines at
  measurement): r51 tip read 206 files / 4868 distinct → **r52 tip reads 209 files / 4912 distinct** (RESOLVES 12,
  INTERNAL 1092, GONE 3808; total occurrences 10471; lane total 1104/4912 = 22.48%). Internal consistency:
  12+1092+3808 = 4912. The gate caught the round on the way, three times, all recorded: rev-1 stale (SCORECARD line-count class),
  rev-3 measured before the last LOG edit moved a LOG.md anchor target line (the same class), and catch (f) below.
  Figures were unchanged through all regenerations (209 files / 4912 distinct).

## Sources & frontier

SOURCES rows before→after: `grep -cE '^\| S[0-9]{3} \|' corpus/SOURCES.md` **82 → 84** (S083 mined, tier A code,
opened 2026-11-01, used-by the F33 entry; S084 rejected with reason and flip). No pre-existing row's
status/recheck/used-by cell changed (S066 byte-identical; its flip spent by record in the entry's §Distinctness).
Frontier rows: 32 → 33 admitted (F33). Sources-census validate: round start exit 0 (the 5 known W04 duplicate-url
warnings: S028, S029, S072, S076, S080) → round end **exit 0**, same 5 warnings, no new warning from S083/S084.
Gate located quote (S083): "resultsPerPage":1,"startIndex":0,"totalResults":1,"format":"NVD_CVE","version":"2.0"
(S083.txt:1, Q1) — 1 "word" by `wc -w` (85 chars; single-line JSON, no interior whitespace), ≤25 bound read against
that measurement; the lesson writes the annotation in auditable form and the round's own auditor checks it OK.

## Trend verdicts

- **expansion: improved.** Frontier 32 → 33 admitted (F33 on a fresh first-party capture); registry 82 → 84; the
  S066 flip spent; PROVINCE +1 frontier amendment; the pre-freeze screen's scope grew (downstream-consumer sweep)
  per the closure's observation. Evidence: `controls/do-nothing-c3-r52.txt` → `controls/c2-counter-final-r52.txt`.
- **quality: improved.** The R56 word-count class moved from prose-rule to instrument-enforced (fail-closed, 9-case
  selftest, errata ledger), both routed figure corrections landed append-only with byte-identical filed lines, and
  the census of record was regenerated over the truly final tree with the gate's own catch recorded (rev 1 stale →
  rev 2 ok). No admitted entry failed a recheck (F33 pass; 33 inherited host-bound fails unchanged, operator-owned).
- **discernment: improved.** Two instrument holes were caught by the round's own receipts BEFORE any commit (the
  self-referential span; the too-weak acknowledgment check that passed the pre-erratum lesson) and are mined with
  fixtures (case-h, case-i); S084 was refused on the JS-wall evidence instead of forcing a docs capture; the F33
  entry asserts nothing the capture does not show (rate limits/parameters explicitly unasserted); scores honestly
  held (4 / 8 / 9) with calibration a verdict row, not a number.

## SHONEN

SHONEN: lane still has SHONEN.md — one line per box:
- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md untouched this
      round (density guard held); verifier: none this round (non-author verification outstanding; the round-51
      closure is the most recent outside check).
- [ ] At least one end-to-end domain task executed and logged in LOG.md — untouched; the considerthese 2026-10-26
      proposal 2 (build a six-file claim package from a public disclosure) stays noted-not-adopted (round-scale;
      the round's three claims were frozen first).
- [~] Instructions executable by an agent without oral context — this round's instruments are selftest-backed with
      reproduce commands in every receipt header (`gate-quote-audit.py --selftest`, census gate `--selftest`,
      embedded rebuild commands); verifier: none this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the S013/F05 note is a scope note, S013 kept out of
      scope; F33's entry names neighbor ground without absorbing it; live-target testing still refused.

## Closure notes for the non-author judge

- Re-derivation entry points: `.ufo/waves/round-52/claims.json` (frozen predicates), `claims-erratum-1.md`
  (superseded figures), `freeze.txt` (rev 1 + 1b + 2 pins), `corpus/lessons/round-52.md` (mistakes + gate), the
  controls receipts named above. Known self-catches recorded, not smoothed over: gate rev-1 stale catch; the two C1
  receipt-run catches; the F33 counter's first-run `selection-not-cited-by-entry` catch.
- Round-start census validate exit 0; round-end census validate exit 0 (at the final tip); committed-state gate
  `CENSUS-FRESH=ok` (rev 4), audit exit 0, S083 recheck exit 0, all re-run at `87dfb88`.
- Scratch `scratch/kasegi-r52` deleted at round end (contains only the base export and receipt-run outputs; every
  committed receipt is in `.ufo/waves/round-52/controls/`).
