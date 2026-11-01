# kasegi — round 50 report

Lane: kasegi-shokunin (fleet/kasegi-shokunin, branch master). Host: Windows workspace (Git Bash; `python`
3.13.15; `python3` is the Microsoft Store stub; `/home/vgpnk` and `/fast` absent). Round base
`c5e36360f5226c97d28f1937961b15c90e58827f`. Lane tip at filing: `021989bf4f5699fa55c6d90abd37ce6ad1caa50a`,
pushed to origin (VeigaPunk/kasegi-shokunin). All commits cite shas the plumbing helper printed.

**Freeze supersession of record (read first).** The inherited round-50 freeze (`.ufo/waves/round-50/claims.json`,
commits `a2de23b`/`28c65eb`, made earlier in this round on this host) is superseded by
`.ufo/waves/round-50/claims-erratum-1.md` + `claims.v2.json` (`freeze-v2.txt`): D1 — the frozen C2 surface
(EPSS as "F31") is already admitted as F19 (`PROVINCE.md` r36 amendment; entry
`corpus/knowledge/epss-exploit-prediction-scoring.md`, source S053); D2 — every frozen counter command names
`python3` + `/home/vgpnk/...`, both absent here, a binding shared by all 67 committed entry recheck lines, so
the frozen `entries=34 pass=34` is unreachable on this host regardless of lane work; D3 — the committed
`controls/do-nothing-c2.txt` prints an output no run on this host can produce (the real base-export run reads
`entries=33 pass=0`), retained byte-identical as mistake evidence beside the working
`controls/do-nothing-c2-winhost.txt`. All five mistakes are mined in `corpus/lessons/round-50.md` § Mistakes.
No claim is asserted on the superseded freeze; nothing was silently rewritten.

## Work performed

Declared claims (claims.v2.json): **C1** — capability acquisition on **depth:verifiability** (the lane's
lowest non-retired axis, 4): a committed census-freshness gate. **C2'** — frontier admission on **coverage**:
F31, OSV affected-range events, grounded on a first-party capture opened this round. One exploratory claim:
none.

- Superseded the inherited freeze on three mined defects and re-froze both claims with host-portable
  predicates (`.ufo/waves/round-50/claims-erratum-1.md`; `claims.v2.json`; `freeze-v2.txt`; commit
  `7918178`).
- C1: shipped `corpus/instruments/census-freshness-check.py` — exit 0 with `CENSUS-FRESH=ok` only when the
  committed `citation-survival.md`/`.tsv` are byte-identical to what `resolve.py` generates over the current
  tree; exit 1 stale/tampered; exit 2 unmeasurable (fail-closed); always restores the bytes it found.
  Selftest `cases=3 failures=0` (fresh/stale-tree/tampered fixtures; `controls/c1-gate-selftest.txt`);
  pre-freeze mutant battery `mutants=6 closed=5 survivors=1` with the survivor named
  (`controls/c1-mutbat.txt`, builder committed beside it). Motivating state: the inherited committed census
  at base read 201 files / 4758 distinct against a live 202 / 4771 (`.ufo/waves/round-50/r50-live-resolve.txt`,
  commit `28c65eb`) — the round-49 stale-census mistake class is now an exit 1. The gate demonstrated itself
  twice in-round by catching real drift (the controls rename; the lesson erratum) before each final
  regeneration (lesson erratum, commit `e27d080`/`021989b`).
- C2': captured the OpenSSF OSV format specification page first-party with the lane's own instrument
  (`capture-source.py --kind html` → `corpus/source-snapshots/round-50/S080.txt`, sha256 `97b850a4…`, 70913
  bytes, 1462 lines, fetched 2026-11-01T01:17:14Z, HTTP 200, 228890 raw bytes — the same raw byte count the
  round-42 S065 screen recorded, so the page was unchanged across both opens); manifest with 16 assertions
  Q1–Q16 (`source-recheck.py --source S080` exit 0, `BROKEN=0`; `controls/s080-recheck.txt`); knowledge entry
  `corpus/knowledge/osv-affected-range-events.md` (interpreter-portable recheck line, distinctness stated
  against F25/F21/F23, the S065 flip condition fired in both row and entry); SOURCES row S080; README F31
  row + round-50 admission block appended at EOF (R6); PROVINCE r50 amendment line appended (commit
  `e1c3ef5`).
- Frontier bookkeeping: the re-open is the S065 flip, spent by F31; the inherited EPSS C2 was refused as a
  duplicate (lesson § Gate); no new rejected SOURCES row this round because the refused surface already has
  an admitted row.
- Mistake-mining: `corpus/lessons/round-50.md` — five rows (duplicate-surface freeze; host-unportable freeze
  predicates; unproducible control evidence; manifest anchor from a displayed range; probe defects faking a
  battery verdict), each with class, evidence pointer, captured-by, fix. An in-round erratum records the
  203/4784 → 204/4807 census-figure correction (commit `e27d080`).
- Records: SCORECARD round-50 result (scores held; capability row enters the table), LOG round-50 entry
  (commit `7918178`), instruments README gate section (commit `33946a3`).
- L0 side channel (append-only, not committed by the lane): kasegi round-50 row asking the operator to
  authorize a portability repair of the 67 host-bound recheck lines (or confirm them operator-owned debt),
  and noting the census's host-path binding.
- Wave disposition: the inherited wave-1 spec (32 seats, commit `28c65eb`) is stale against claims.v2.json
  (its seats attack the superseded EPSS freeze; its CONTEXT names Linux-only roots); no AgentSwarm surface
  exists on this host; no seat ran, no results exist, **no falsification credit is claimed**.

## Landed changes

All tied to the LOG.md round-50 entry; every sha below is one the helper printed; all pushed to origin.

| Commit | Change |
|---|---|
| `e1c3ef5b00362fb02b47e822bb47abe114c0b7c0` | C2' content: SOURCES S080 row; README F31 row + round-50 admission block; PROVINCE r50 amendment; `corpus/knowledge/osv-affected-range-events.md`; `corpus/source-snapshots/round-50/{S080.txt,manifest.json}` |
| `33946a3a7189f6a8f6d2f1e55fed23eca4bc8d1d` | C1 instrument: `corpus/instruments/census-freshness-check.py`; census of record regenerated; instruments README gate section |
| `7918178b1b09801b2de7c4c310cfbc4fcb9d0119` | Freeze supersession (`claims-erratum-1.md`, `claims.v2.json`, `freeze-v2.txt`), host-produced controls (9 receipt files), round-50 lesson (5 mistakes), SCORECARD result, LOG entry |
| `e27d0809a56edd5f3243eb0cf058dc68c54e324c` | Corrections named: census figures 203/4784 → 204/4807 with the lesson erratum; gate receipt re-measured after the gate caught the controls rename |
| `021989bf4f5699fa55c6d90abd37ce6ad1caa50a` | Final census of record over the post-erratum tree; gate receipt `CENSUS-FRESH=ok`; no corpus/** edit follows |

## Before → after measurements

Counting commands run on THIS host against committed bytes; measured commit = lane tip `021989b…` unless
stated.

- **C1 (depth:verifiability 4 → 4 held, capability acquired).**
  `python corpus/instruments/census-freshness-check.py <lane-root>` → `CENSUS-FRESH=ok files=2`, exit 0 at
  the tip (receipt `controls/c1-gate-final.txt`). Selftest: `python corpus/instruments/census-freshness-check.py --selftest`
  → `selftest cases=3 failures=0` (stale-tree and tampered-census fixtures read exit 1). Do-nothing control:
  at the base export the instrument does not exist → exit 2 (`controls/do-nothing-c1.txt`, produced on this
  host). Before-state the gate inherits: committed census 201 files / 4758 distinct vs live 202 / 4771
  (`r50-live-resolve.txt`). Score HELD at 4: `score-gap.py`'s 22 gated lines stay operator-owned and the
  67 host-bound recheck lines are filed as L0 debt, not repaired.
- **C2' (coverage 8 → 8 held, frontier 30 → 31).**
  `python corpus/instruments/frontier-recheck-count.py` (from the lane root):
  before (base export, this host, `controls/do-nothing-c2-winhost.txt`): `FRONTIER-CENSUS rows=30
  admitted=30 closed=0 problem-rows=30 registry=79`, `entries=33 pass=0 exit=1`, zero `F31` lines →
  after (tip, `controls/c2-counter-final.txt`): `FRONTIER-CENSUS rows=31 admitted=31 closed=1
  problem-rows=30 registry=80`, `entries=34 pass=1 exit=1` with the single pass `PASS F31 ids=S080 exit=0`;
  all 33 inherited entry fails carry exactly `problems=recheck-exit-1` (no missing-entry, no manifest
  problem). `python corpus/instruments/source-recheck.py --manifest corpus/source-snapshots/round-50/manifest.json --source S080`
  → exit 0, 16/16 assertions, `BROKEN=0`. Score HELD at 8: the denominator is the lost domain root's
  18-surface set (0 present, operator-owned re-scope); F31 moves the frontier measure, not the score.
- **Census of record:** base `201 files / 4758 distinct` → tip `204 files / 4807 distinct`
  (`grep "Scope:" corpus/instruments/citation-survival.md`; `grep "distinct path-like citations" ...`).

## Sources & frontier

SOURCES.md rows before → after: **79 → 80** (`grep -c "^| S" corpus/SOURCES.md` → 79 at base commit
`c5e3636`, 80 at the tip). Row added this round, opened this round: **S080** (OpenSSF OSV format
specification page, kind `spec`, tier A, status `mined`, opened 2026-11-01, recheck `90d`, used-by
`corpus/knowledge/osv-affected-range-events.md`), which re-opens the round-42 S065 screen under its own
recorded flip condition (OSV-specific range semantics the CVE format cannot express); S065 itself stays
`rejected`, byte-identical (R8). Sourced claim: C2' rests on S080. Frontier census: `FRONTIER-CENSUS
rows=30 → 31 admitted` (counter receipts above); PROVINCE F01–F31 with the r50 amendment line. Round-start
census (`sources-census.sh validate --root <fleet> kasegi`, exit 0, four pre-existing W04 warnings) and
round-end census (exit 0, the same four plus the expected `W04 S080 duplicate url ossf.github.io/osv-schema
across scopes` — the S065/S080 re-open pair; overall `kasegi ok`):

```
# round start (exit 0)
kasegi  W04 S028 duplicate url docs.hackerone.com/... ; W04 S029 ; W04 S072 ; W04 S076
kasegi  ok C:/Users/jpvei/.../shokunin/kasegi-shokunin/corpus/SOURCES.md
# round end (exit 0)
kasegi  W04 S028 ; W04 S029 ; W04 S072 ; W04 S076 ; W04 S080 duplicate url ossf.github.io/osv-schema across scopes
kasegi  ok C:/Users/jpvei/.../shokunin/kasegi-shokunin/corpus/SOURCES.md
```

## Trend verdicts

- **expansion: improved.** Frontier 30 → 31 admitted on a genuinely new, first-party capture (counter
  receipts; README F31 row; PROVINCE F31 line), reached by firing a recorded flip rather than by re-admitting
  a held surface. The coverage score itself is held (denominator is the lost domain root), so the improvement
  is the frontier measure, stated as such.
- **quality: improved.** A new instrument turns the round-49 stale-census mistake into an exit 1
  (selftest `cases=3 failures=0`; battery `mutants=6 closed=5 survivors=1` named), and it proved itself
  in-round by catching two real drifts (controls rename; lesson erratum) before each final regeneration. The
  freeze-correction work (erratum + host-portable claims + honest controls) repairs the round's own evidence
  chain. depth:verifiability score held at 4 with the residue named, not gamed.
- **discernment: improved.** The round refused its own inherited freeze: a duplicate-surface claim (EPSS =
  F19), host-unportable predicates and an unproducible control were mined as named mistakes, superseded
  through an erratum, and re-frozen only at the bar the evidence supports — with the honest taxonomy
  (`entries=34 pass=1`, 33 × `recheck-exit-1`) reported instead of a greener number. Scores asserted:
  none; held: all.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — Evidence:
  `SKILL.md` (untouched this round; author assertion; outside promotion verification remains required).
- [ ] At least one end-to-end domain task executed and logged in LOG.md — Evidence: LOG.md round-50 entry —
  no new end-to-end domain task claimed; source capture, instrument and record work only.
- [~] Instructions executable by an agent without oral context — Evidence: `corpus/lessons/round-47-verifier-spotcheck.md`
  (declared-root recheck observations; not promotion); this round adds a host-portability limit now filed as
  L0 kasegi round-50.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — Evidence: `PROVINCE.md` r50 amendment appended
  (F31, bounty/security-research-relevant format knowledge); scope unchanged; live-target testing refused.

## Assimilation

`considerthese/` exists (8 operator files, latest 2026-10-26). Proposals reviewed this round: none adopted —
the round's only adoption candidate would have been a wave/frontier proposal, and the round's frontier move
came from the S065 flip instead; no still-unimplemented proposal was grounded through this round's bar.
Assimilation: none — shokuknow unreachable.

## Honest stops

- No independent non-author verification this round: no seat ran (no AgentSwarm surface on this host; the
  inherited wave spec targets the superseded freeze). The claims verify on re-derivable commands only; the
  outside spot-check duty is stated as outstanding in SCORECARD and the lesson.
- `python3` is not executable on this host; every counting command above uses `python` (3.13.15). The one
  new recheck line (F31's entry) is interpreter-portable (`python3 || python`); the other 67 remain
  Linux-bound by inherited bytes, disclosed here, in SCORECARD, in the lesson, and in the L0 question.
- Scratch dir `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/scratch/kasegi-r50` is
  deleted after this report; every receipt it carried is committed under `.ufo/waves/round-50/controls/`.
