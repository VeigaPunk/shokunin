# kagi — round 66

Lane: kagi (secrets & vault ops — the-janitor flows, credential-hygiene
evidence). Round 66, attempt 1. Claim BASE
`d549ee6eb8770a49938b78f49cf79e36d9c1c2e8` (round-65 verifier spot-check tip).
Frozen predeclaration `plans/round-66.md` at `ddcd46bb`, with Amendments A1–A4
at `dcd78c2e` (each appended before the reading it governs). Lane commits:
`cfafdb11` (instruments, carrier row, census repair, lesson, criteria),
`f2d58687` (integration: scorecard, claims rows, LOG, lesson addendum,
provenance/quote repairs, receipts), `567f50c3` (sentinel V-2 closure),
`967afd49` (carrier-binding entry wiring, class-matrix `Reverify`, final gate
receipts). Final lane tip: `git ls-remote origin refs/heads/master`.

**Declared claims (3, distinct axes, causally separable):**

1. **C1 freshness** — the S148 carrier binds by path equality + digest on a
   registry row that names the capture path. `C1_CARRIER` drift 0 → 1.
2. **C2 operability** — the pre-file falsification ledger reads `pass` with the
   wave's attack seats reconciled and `claims-declared` CLEAN with the round's
   rows. `C2_PREFILE` gate 0 → 1. **Verdict: honest stop** — the driver had not
   written `w1-results.json` at filing (one seat handle open), so the gate read
   `SETUP findings=1`. Measured, not narrowed (§C2 below).
3. **C3 calibration** — the LANE's own census gate goes
   `SOURCES_CENSUS: FAILED (findings=4)` → `CLEAN (findings=0)`, and the round
   names which census it means. `C3_CENSUS` findings 4 → 0.

## Work performed

- **C1 instrument.** `plans/round-66-c1.sh` (sha256 `d72f9712…`) resolves three
  anchors — the registry row's anchor cell, that row's `source-fetches.tsv`
  column 16, and `corpus/volatile-shape.py`'s `DEFAULT_CAPTURE` — to ONE path
  whose sha256 equals the pin the row carries; the verdict fields are computed
  by `verdict_of(...)`, never printed as literals. Evidence:
  `.ufo/waves/round-66/final/c1-candidate.txt`, `…/c1-base.txt`,
  `…/c1-selftest.txt`.
- **C1 repair.** Registry row **S164** (`supersedes S148 —`) names the carrier
  capture `.ufo/waves/round-64/capture/S143.body` (264946 B, sha256
  `3b8d4e15…cba40`); its `source-fetches.tsv` row carries the same path with
  columns 10/11 equal to the pin and byte count. Evidence: `corpus/SOURCES.md`
  S164; `corpus/source-fetches.tsv` S164.
- **C1 attack surface.** Three wrong bodies (the 39 750 B arXiv body at the
  `S148` handle, plus `S156`/`S157`) are each refused with
  `digest-mismatch:`; guard (d) repoints the row to the wrong file and reads
  `drift=0`.
- **C2 instrument.** `plans/round-66-c2.sh` (sha256 `1c1a7935…`) runs the
  pre-file gate with an explicit `--fleet` on every invocation (a gate run
  without it measures the default fleet — M66-10), folds `claims-declared` into
  `gate` so the verdict line and the exit code agree (M66-11), and carries four
  guard legs; on a conforming fixture fleet it reads
  `C2_PREFILE: gate=1 claims=3 rows=9 attack_seats=3 guard=1` rc 0
  (`R66MutC2` receipt `.ufo/waves/round-66/w1/R66MutC2/receipts/`, ten gate-side
  mutants killed).
- **C2 ledger.** `.ufo/waves/round-66/claim-falsification.tsv` (9 rows) covers
  C1–C3 and names the filing attack seats' artifacts (reviewer, critic,
  mutation-tester ×2, connector, scout pre-state).
- **C3 instrument + repair.** `plans/round-66-c3.sh` (sha256 `a6c36b87…`) reads
  the LANE gate's own verdict line; the four findings it printed at BASE are
  repaired by three provenance rows (S155, S156, S164), the class-matrix entry's
  `cites:` line and the S148/S156 `used-by` cells. Evidence:
  `.ufo/waves/round-66/final/c3-base.txt`, `…/c3-candidate.txt`,
  `…/c3-selftest.txt`.
- **C3 second repair, adopted from a seat.** `R66ScoutSources` measured that
  round 65's 429 capture pair only *describes* the 899-byte body; the body itself
  was never committed. It is now at
  `.ufo/waves/round-66/capture/S156-429.body` (sha `037c2dbe…`, 899 B) and
  S156's provenance row binds to it.
- **Record-binding repairs (scribe seat's findings, all measured).** S155's
  normalized digest was the BioC body's (`4d966ff9…`) instead of its own
  (`5f509414…`); S156's declared quote joined two JSON fields and did not locate
  (`locate ⇒ count=0`) — both repaired and re-located. Sweep of the class: of 36
  fetch rows whose column 16 names an existing file, 34 locate and 2 did not
  (S115 pre-existing, S156 landed this round).
- **Carrier-binding entry.** `corpus/knowledge/claim-instrument-carrier-binding.md`
  (from `R66ScribeEntry`) states the path+digest binding rule, the borrowed-id
  class and the checks that see it; wired with `cites:`, `used-by` cells,
  `Reverify: R21-03` and a stamp row. `DOC_AUDIT: CLEAN (entries=47
  row_linked=44 by_hand=3 undeclared=0 missing_ids=0 unpinned=0)`
  (`.ufo/waves/round-66/final/doc-audit-candidate.txt`).
- **Inherited defect found by running a gate round 65 skipped.** The class-matrix
  entry had no `Reverify:` line and no stamp row; `docs` read `BROKEN …
  undeclared=1 unpinned=1` naming it. Declared, stamped, and mined as M66-14.
- **Sentinel dispositions.** V-1 (HIGH, write scope) closed in-round; V-2
  (MEDIUM) closed on the landed bytes — `resolve_volatile` now refuses a
  non-repo-relative `DEFAULT_CAPTURE` (`DEFAULT_CAPTURE-not-repo-relative:`) with
  two selftest cases (absolute `/etc/passwd`, traversal `../../outside.body`).
  A stray `scripts/hyaku/__pycache__/` under the FLEET root was created inside
  this round's window; `scripts/` is a never-edit path for a lane, so its
  deletion is routed operator-side (D-66-2), not performed.
- **Frontier.** S164 admitted (live re-open 2026-11-08, HTTP 200, 264946 B,
  sha equal to the pin); one duplicate-URL second row refused; two leads opened
  and refused with reasons; the arXiv:2404.09241 equivalent-mutant paper
  recorded as a **lead** for round 67. Evidence: `corpus/lessons/round-66.md`
  §Gate and §Gate addendum.
- **Mistakes mined (14).** M66-1 an undefined predicate term frozen; M66-2 a
  kill rule defining the candidate's own act as failure; M66-3 a do-nothing
  target (M65-1 recurrence); M66-4 a hard-coded sample as a census; M66-5 the
  round named the wrong census gate; M66-6 the dispatch handoff had the wrong
  top-level shape; M66-7 the counter's verdict held a literal; M66-8 mutation
  legs ran on a tree where the claim already failed; M66-9 a guard leg measured
  the lane instead of the candidate; M66-10 a new provenance row borrowed
  another body's normalized digest; M66-11 a declared quote that does not
  locate; M66-12 a Gate cell stated a byte-diff `cmp` does not produce; M66-13
  a gate blind to the class the round closes; M66-14 an entry landed undeclared
  and unpinned. Evidence: `corpus/lessons/round-66.md` §Mistakes.
- **Quality bar.** `corpus/QUALITY.md` gains QM89–QM94 (computed verdict fields;
  legs scoped to their state and their tree; handoff shape verified; digests and
  quotes bound to the body the row names; a capture-citing gate reads the bytes).

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| `plans/round-66.md` (frozen plan) + base census receipts | Round 66, bullet 1 | `ddcd46bb` |
| `plans/round-66.md` Amendments A1–A4 | Round 66, bullet 2 | `dcd78c2e` |
| `plans/round-66-c1.sh`, `-c2.sh`, `-c3.sh`, `-controls.sh` | Round 66, bullets 3–5 | `cfafdb11` |
| `corpus/SOURCES.md` S164, `source-fetches.tsv` +3, class-matrix `cites:`/`used-by` | Round 66, bullets 6–7 | `cfafdb11` |
| `corpus/lessons/round-66.md`, `corpus/QUALITY.md` QM89–QM94, `SKILL.md` gate rows | Round 66, bullets 8–10 | `cfafdb11` |
| `SCORECARD.md` pre/post, `claims-declared.tsv` 66/C1–C3, `LOG.md`, provenance/quote repairs | Round 66, bullets 11–13 | `f2d58687` |
| `plans/round-66-c1.sh` V-2 guard + 2 cases; lesson sentinel dispositions | Round 66, bullet 14 | `567f50c3` |
| `corpus/knowledge/claim-instrument-carrier-binding.md`, class-matrix `Reverify`, `stamps.tsv`, final gate receipts | Round 66, bullets 15–16 | `967afd49` |
| `.ufo/waves/round-66/**` (spec, dispatch, handoff, base, capture, w1 reports, final receipts) | Round 66, wave bullet | across the four commits |

## Before → after measurements

### C1 — freshness (`C1_CARRIER`, drift 0 → 1)

Counting command (frozen):

```
bash plans/round-66-c1.sh --tree <TREE> [--base-tree <d549ee6 extraction>] [--selftest]
```

- **BASE** `d549ee6` (`--tree` on a `git archive` extraction):
  `C1_CARRIER: drift=0 paths=0 hex=0 match=0 guard=0` rc 1 — receipt
  `.ufo/waves/round-66/final/c1-base.txt`. No row carries the pin *and* names a
  capture path (`registry:no-row-carries-pin-with-path`, `fetches:no-row`).
- **candidate**: `C1_CARRIER: drift=1 paths=3 hex=3 match=1 guard=1` rc 0 —
  receipt `.ufo/waves/round-66/final/c1-candidate.txt`, guard `a=1 b=1 c=1 d=1`:
  `row=S164 path=.ufo/waves/round-64/capture/S143.body`, three wrong bodies
  refused (`hex=3 refused=3`), BASE tree reads drift 0 (a), the round-65
  volatile gate still `VOLATILE_SHAPE: match=1` (c), and the row repointed to the
  wrong file reads `digest-mismatch:` (d).
- `--selftest` ⇒ `c1-carrier: selftest cases=45 failed=0`
  (`.ufo/waves/round-66/final/c1-selftest.txt`).

Axis: **freshness**, 9 → 9 (increment recorded; the score was at the saturation
line). Ceilings: one row's path (a second row carrying the same pin resolves to
the newest — measured by the battery); the counter proves path↔digest agreement,
not that the endpoint still serves the bytes; the borrowed-identity class is
**not** covered for the other 11 round-64 handles — routed (D-66-1).

### C2 — operability (`C2_PREFILE`, gate 0 → 1) — **honest stop**

Counting command (frozen):

```
bash plans/round-66-c2.sh [--tree DIR] [--fleet DIR] [--selftest]
```

- **pre-integration tree**: `C2_PREFILE: gate=0 claims=0 rows=0 attack_seats=0
  guard=0` with the gate's own `PREFILE-FALSIFICATION: SETUP findings=2`
  (`wave-missing`, `report-missing`).
- **as filed**: `C2_PREFILE: gate=0 claims=0 rows=0 attack_seats=0 guard=0`,
  `claims-declared=1` (`CLAIMS_DECLARED: CLEAN (claims=59)`), guards `a=1 b=0
  c=0 d=1`, and the gate's own line
  `PREFILE-FALSIFICATION: SETUP findings=1`
  (`FINDING wave-missing …/.ufo/waves/round-66/w1-results.json`).
- **why**: `w1-results.json` is written by the inline dispatcher when the last
  seat handle closes. 13 of 14 seats filed; `R66ScribeEntry` was still live at
  filing and the file never appeared. The missing artifact is a **driver
  artifact**, not a lane defect; writing it myself would be fabrication.
- **what is measured**: on a conforming fixture fleet the same instrument reads
  `C2_PREFILE: gate=1 claims=3 rows=9 attack_seats=3 guard=1` rc 0 with ten
  gate-side mutants killed (`R66MutC2`). The predicate is reachable; this
  round's tree did not carry the file it reads.

Axis: **operability** — **did not verify**. Reported, not prettified.

### C3 — calibration (`C3_CENSUS`, findings 4 → 0)

Counting command (frozen):

```
bash plans/round-66-c3.sh [--tree DIR] [--fleet DIR] [--selftest]
```

- **BASE** (`--tree` on a `git archive d549ee6` extraction):
  `C3_CENSUS: findings=4 rows=155 guard=1` rc 1 — receipt
  `.ufo/waves/round-66/final/c3-base.txt`; the four findings are
  `SC_FETCH id=S155 missing-provenance`, `SC_FETCH id=S156 missing-provenance`,
  `SC_BODY_CITE … claim-instrument-class-matrix.md id=S148 unrecorded` and the
  same for `S156`.
- **candidate**: `C3_CENSUS: findings=0 rows=156 guard=1` rc 0 — receipt
  `.ufo/waves/round-66/final/c3-candidate.txt`; guard `a=1 b=1 c=1 d=1`
  (removing the entry's `cites:` line returns `findings=4`; a shim gate printing
  `rows=999` makes the counter print 999; the fleet wrapper reads `kagi ok`).
- `--selftest` ⇒ `c3-census: selftest cases=4 failed=0`.

Axis: **calibration**, 9 → 9 (increment recorded). Ceiling: the counter reads one
gate's verdict line; it does not judge whether each row's `teaches` is the best
citation of its anchor.

## Sources & frontier

Census, round start (2026-11-08, before any edit):

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi
kagi ok …/kagi-shokunin/corpus/SOURCES.md   rc=0   (155 data rows; W04 warnings only)
$ bash corpus/sources-census.sh            # the LANE gate
SOURCES_CENSUS: FAILED (findings=4 rows=155)
```

Census, round end:

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi
kagi ok …/kagi-shokunin/corpus/SOURCES.md   rc=0   (156 data rows; W04 only)
$ bash corpus/sources-census.sh            # the LANE gate
SOURCES_CENSUS: CLEAN (rows=156 A=139 B=2 C=15 queued=3 mined=136 rejected=17 entries_sourced=26 …)
```

Rows: 155 → 156 (`awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {n++} END{print n+0}'
corpus/SOURCES.md`). Rows added by tier: 1 tier A (`S164`, `mined`), 0 tier B,
0 tier C. Rows touched old→new: `used-by` cells only — S148, S156, S143, S145,
S152, S164 each gained one entry path (old→new logged in the lesson's Gate
addendum). Frontier rows advanced: S164 names the carrier capture the S148 pin
is read from (C1's sourced basis); S156's provenance row binds the 899-byte 429
body that grounds its rejection.

Both gates are printed because M66-5 is exactly the defect of naming one and
meaning the other.

`Assimilation: none` — no `merge/kagi/` package was adopted this round (its
collision check has not been re-run; the claim cap is spent on C1–C3).

`considerthese/`: the latest file is `considerthese/2026-10-26.md`; its proposal
3 was mined in round 63 (QM83/QM84), so no still-unimplemented proposal is mined
this round.

## Ceilings and routed defects

- **Borrowed identity is a class, not one file.** Over all 20 round-64 captures,
  only `S149.body` carries its own row's bytes; 11 carry another row's pin; both
  census gates are blind to it (`R66ScoutSources` M4: a fetch row repointed at
  another row's body still reads CLEAN, and deleting the cited file still reads
  CLEAN — the gate checks the location string's length, never the bytes), while
  `plans/round-66-c1.sh` catches it. **Routed to round 67** (D-66-1).
- **`CITATION_GATE` / `CLAIM_LEDGER verify`** — `docs` was run and is CLEAN;
  `verify` (full) exceeded a 280 s bound under fleet load and was not completed
  (round-64 readings stand). Named debt.
- **Stray fleet artifact.** `scripts/hyaku/__pycache__/` — operator-side
  deletion (D-66-2).
- **Wave.** 13 of 14 seats filed; `R66ScribeEntry` was live at filing and its
  report is absent, though its three receipts and the knowledge entry it wrote
  are landed and cited. The falsification ledger reconciles the seats that filed.

## Trend verdicts

- **expansion: `unchanged`** — one registry row admitted (S164), one knowledge
  entry landed on ground the coverage map did not hold (the carrier-binding
  rule), no coverage-map frontier area moved into core and no capability entered
  the SCORECARD table; nothing admitted failed its bar. Not `improved` on the
  SCORECARD's definition, not `harmed`.
- **quality: `improved`** — three instruments moved from claimed to measured
  properties (carrier binding, pre-file ledger reachability, lane census), each
  with a falsifier that fires, and six criteria (QM89–QM94) entered the bar from
  measured mistakes. A round-65 landing defect (an undeclared, unstamped entry)
  was found and repaired by running the gate round 65 skipped.
- **discernment: `improved`** — fourteen mistakes mined; six were caught by the
  round's own attack seats **before** any candidate reading, three by the L1's
  own instruments, three by the records seat's re-reading of rows this round
  landed, one by a sentinel and one by a gate the previous round had skipped.
  Named caveat: one seat had not filed, and C2's honest stop means the ledger's
  attack-seat population is 13/14.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited
  sources — author-asserted; pointers `SKILL.md` §Vault-ops decision table,
  §Failure table, §Gate registry round-66 rows; no non-author verifier this round.
- [~] At least one end-to-end domain task executed and logged — pointer: three
  counters run end-to-end on the candidate and on a `git archive` BASE
  extraction, receipts under `.ufo/waves/round-66/final/`.
- [~] Instructions executable by an agent without oral context — pointer: three
  counters and the controls battery run from a clean tree with `--selftest`
  (`45`, `4` and `29` cases).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer:
  `bash corpus/scope-gate.sh` unchanged; the carried `ADJACENCY_SCOPE: DEFECT`
  breadth debt named, not absorbed.

## Round shape, wave and dead seats

- Shape: **one v1 wave**, band 8–16. Spec `.ufo/waves/round-66/w1-spec.json`
  validated under `scripts/hyaku/ufo-wave-policy.json`; dispatch
  `.ufo/waves/round-66/w1-dispatch.json`; handoff `kagi-r66-w1.ready`
  (`l1: KagiR66`), taken 06:14 (`kagi-r66-w1.ready.dispatched`).
- Seats declared: **14** — 2 scout, 4 executor, 2 scribe, 1 reviewer, 1 critic,
  2 mutation-tester, 1 connector, 1 sentinel. Attack share 4/14 = 28.57 % on the
  addendum's literal list, 5/14 = 35.71 % counting the sentinel.
- **Dispatch defect.** The handoff's dispatch file was written as
  `{context, tasks}`; the driver reads `d['taskCall']['tasks']` and raised
  `KeyError('taskCall')` every 30 s from 05:47 until the orchestrator repaired
  the file at 06:13 (`w1-dispatch.json.pre-taskcall-wrap-20261108T061324`).
  Zero seats spawned in that window; mined as M66-6/QM91.
- Seats filed: **13 of 14**. `R66ScribeEntry` did not file a `.md` report (its
  receipts and the knowledge entry it drafted are landed); `R66ExecControls`
  filed `SEAT-STATUS: partial mismatch=1` before the ledger existed and the L1
  re-ran the battery after integration.
- `Stale-lane`: this round's mission is the lane's only open mission and it is
  **progressing** — four lane-authored commits, with the report to follow.
- Tool installs: none. No `pacman` transaction was attempted (host-wide pause
  respected); nothing installed via `uv`/`npx`/binary.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows
  no file one of this round's seats wrote into the fleet root.

## Honest shortfalls

1. **C2 did not verify.** The pre-file gate needs the driver's
   `w1-results.json`; the last seat handle had not closed. Honest stop, with the
   SETUP line quoted; the predicate itself is proven reachable on a fixture fleet
   with ten mutants killed.
2. **The wave started 26 minutes late** because of the handoff shape (M66-6).
3. **One seat did not file** (`R66ScribeEntry`), so the ledger's attack-seat
   population is 13/14.
4. **The borrowed-identity class is measured, not closed** — routed with the
   instrument that sees it named.
5. **`claim-ledger.sh verify` (full) was not completed** under fleet load;
   `docs` was and is CLEAN.

## Erratum (appended after the filed bytes)

This erratum supersedes the sentence in §Landed changes that ends "Final lane
tip: `git ls-remote origin refs/heads/master`" and adds the close correction:

- Final lane tip after the close correction: **`d1e127ac5b363522ee5a2804ad57c72af7a32953`**
  (`round-66: close correction — one seat unfiled, w1-results.json absent, C2
  honest stop (C1/C3 verified)`), pushed — `git ls-remote origin
  refs/heads/master` prints that hash.
- The correction landed in `LOG.md` (append-only, pointing at the round-66
  entry it corrects): 13 of 14 seats filed, `w1-results.json` absent at close,
  C2 an honest stop; C1 and C3 verified.
