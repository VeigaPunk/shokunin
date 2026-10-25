# kasegi — round 24 report

Lane: kasegi-shokunin (bounty & security research; axes **depth + coverage**).
Round 24, base `d0a3f6a4643fc5f668e95d94fcdbe22830bb8f9a`, lane tip at attempt
start `c2480b1`. Frozen claims: `kasegi-shokunin/.ufo/waves/round-24/claims.json`
(written before any data was collected; one false timestamp and one mis-specified
counter are corrected by erratum — see §Landed changes).

**Declared claims.** Two, on distinct axes:

- **C1 — `depth:verifiability` (4, the lowest non-retired axis):** the two
  verifiability instruments the round-23 verifier routed back. (A) no capture
  existed for S001–S015, so five Frontier entries' `recheck:` lines could only
  fail closed; (B) `resolve.py`'s brace/glob dispatch dropped an empty brace
  alternative, credited a dangling symlink as the first glob match, and never
  globbed a brace alternative that carries a `<...>` placeholder. Predicate: every
  Frontier entry's own `recheck:` exits 0 **and** the dispatch matrix is 8/8.
- **C2 — `coverage` (7):** one new Frontier topic (F09, authorisation outside a
  platform's safe-harbour text) admitted with two entries re-grounded from the
  shokuknow package, under the assimilation contract (§10). Predicate: frontier
  8 → 9 and two entries each citing a row first registered this round.

## Work performed

**C1 (depth:verifiability).**

- Captured S001–S015 with a new committed instrument `corpus/instruments/capture-source.py`
  (HTML/PDF/text → UTF-8 text, deterministic, `--selftest` exit 0) —
  `kasegi-shokunin/corpus/source-snapshots/round-24/` + `capture-log.txt`
  (15 fetches, status 200 each, sha256 per snapshot).
- Built `corpus/source-snapshots/round-24/manifest.json`: 19 records, 76
  assertions (S001–S015 plus S032–S035), every assertion measured exactly-once
  before being written; `source-recheck.py --manifest …` exit 0
  (`c1-counterA-manifest-receipt.txt`, 95 OK lines).
- Re-pointed the five F01–F05 `recheck:` lines from `source-snapshots/round-23/`
  to `round-24/` on the same physical line (length-neutral, so no line anchor
  moves; F06–F08 stay on the round-23 manifest, which still passes).
- Patched `corpus/instruments/resolve.py`: empty brace alternative kept inside a
  real alternative set (`{,sub}`), bare `{}` still a placeholder; a brace
  alternative carrying `<...>` is globbed (`brace-glob`); the glob branch returns
  the first match that **exists**; CLI refuses a non-directory root and an empty
  census run (`--help` no longer overwrites `citation-survival.*`).
- Built `corpus/instruments/resolve-dispatch-check.py` +
  `resolve-dispatch-fixtures.json`: 8 cases (4 liveness / 4 control) run on real
  copied CLI bytes, asserting class **and** resolved path.
- Built `corpus/instruments/frontier-recheck-count.py`: the entry-bound counter-A
  harness (header `source:` ids must be covered by the line's `--source` set, the
  set must be cited by the entry, the manifest must list it, the line must be a
  `source-recheck.py` invocation) — after four wave-1 seats demonstrated that the
  bare shell loop reaches 8/8 by pointing every entry at one capture, writing
  `recheck: true`, dropping `--source`, or using `--selftest`.
- Hardened `corpus/instruments/source-recheck.py`: rejects a quote shorter than
  12 normalized characters, prints `occurrences=N` on every pass, verifies an
  optional `anchor` line (round-23's one non-unique assertion now reads
  `S029:art14-2a-early-warning OK occurrences=2 anchor=10-ok`).

**C2 (coverage / assimilation).**

- Collision check + guard proof + renumber map:
  `kasegi-shokunin/.ufo/waves/round-24/assimilation/{reg-ids,staged-ids,collisions,renumber-map.tsv,guard-proof.txt,quarantine-slice,quarantine-handcheck.txt,census-before.txt}`.
- Two entries admitted, re-opened by this lane on 2026-10-25:
  `corpus/knowledge/authorised-testing-rules-of-engagement.md` (S032) and
  `corpus/knowledge/statutory-authorization-and-unauthorized-access.md`
  (S033/S034/S035), with four new registry rows in `corpus/SOURCES.md`.
- Refused `chinese-criminal-thresholds-and-authorisation.md` (Q2/Q4: its own
  cited 第二百八十五条 lacks the 情节严重 element it asserts; prose `recheck:`;
  `ground: F12` names no lane topic) and three standards-body entries (PROVINCE
  scope) — reasons and flip conditions in `corpus/lessons/round-24.md` § Gate.
- `corpus/README.md` F09 row + coverage-map rows + provenance count (33 → 35);
  `PROVINCE.md` Frontier F01–F09; the frontier denominator line 8/8 → 9/9.

**Bookkeeping / contract.**

- QUALITY gains **Q9** (assertion binding: id↔path, exactly-once-or-anchor,
  occurrence count printed), **R11** (a counter publishes its discrimination
  against degenerate/mutated instruments), **R12** (a recheck line is measured
  against the entry that owns it). `corpus/instruments/README.md` gains the
  round-24 section including the published blind spot.
- `corpus/lessons/round-24.md`: Gate (admission/rejection/quarantine/census),
  four mined mistakes, routed-defect disposition, considerthese landing.
- Routed defects from `corpus/lessons/round-23-verifier-spotcheck.md`: **1 and 2
  fixed and measured**; **3** closed by recording the two counters (host counts
  launches, lane counts landings); **4** recorded as reachable-only-via
  `git show 953c278:` (receipt paths were overwritten at `bf9ce02`), cells left
  verbatim per R9.

**considerthese.** `considerthese/2026-10-24.md` proposal 1's unlanded conjunct
(exactly-once-or-anchor) landed as QUALITY Q9 + code; proposals 2–3 were already
landed in round 23 (`QuarterConsiderthese` re-derived this), 4–5 are
operator-owned.

## Landed changes

Lane commit **`d3614a2c5489e6379bdd0e56440496310b8b5e00`** (jj-lane helper,
`landed d3614a2c…`, remote-verified), message
`round-24: verifiability instruments (counter A 3/8->8/8, dispatch 4/8->8/8) + F09 assimilation (S032-S035)`.
Every change below is inside that commit and tied to the LOG entry
`kasegi-shokunin/LOG.md` § *2026-10-25 — round 24*:

| Change | Path(s) | LOG line |
|---|---|---|
| resolver dispatch fixes + CLI guards | `corpus/instruments/resolve.py` | C1 paragraph |
| dispatch matrix + checker | `corpus/instruments/resolve-dispatch-check.py`, `resolve-dispatch-fixtures.json` | C1 paragraph |
| counter-A harness (R12) | `corpus/instruments/frontier-recheck-count.py` | C1 paragraph |
| capture instrument + manifest | `corpus/instruments/capture-source.py`, `corpus/source-snapshots/round-24/` | C1 captures |
| rechecker hardening (Q9) | `corpus/instruments/source-recheck.py`, `corpus/source-snapshots/round-23/manifest.json` | C1 captures |
| F01–F05 recheck re-point | `corpus/knowledge/{cvss-v4-severity-and-vector,coordinated-disclosure-timelines,authorization-safe-harbor-and-scope,ai-assisted-finding-validation,cwe-top25-2025-methodology}.md` (line 4 only) | C1 paragraph |
| two admitted entries | `corpus/knowledge/authorised-testing-rules-of-engagement.md`, `statutory-authorization-and-unauthorized-access.md` | C2 paragraph |
| four registry rows | `corpus/SOURCES.md` (S032–S035 after S031) | C2 + Assimilation |
| frontier/coverage docs | `corpus/README.md`, `PROVINCE.md` | C2 + Docs |
| quality criteria + instrument docs | `corpus/QUALITY.md`, `corpus/instruments/README.md` | Docs/contracts |
| scorecard + lesson + wave evidence | `SCORECARD.md`, `corpus/lessons/round-24.md`, `.ufo/waves/round-24/` | whole entry |

**Errata filed in `SCORECARD.md` § Round 24 (before the after-measurement):**
(1) `frozen_at_utc` was written `2026-10-25T00:00:00Z` while the file's real
creation time is `07:09:47Z`; (2) counter B's frozen `grep '^source: S1[0-9][0-9] '`
cannot match a registry that continues at S032 — the predicate stands and the
command is corrected to `S03[2-5]` (ids follow the document, never arithmetic);
(3) the wave-1 matrix item's L4 could not fail the baseline (a dangling brace
alternative was already skipped), so the landed L4's fail-before is driven by its
second citation, printed per case.

## Before → after measurements

Measured against lane commit `d3614a2c` (after) and `c2480b1` (before).

**C1 counter A — every Frontier entry's own `recheck:` exits 0.** Counting command
(frozen shell form, cwd-pinned; `c1-counterA-shell-{before,after}.txt`):

```sh
cd /home/vgpnk/Projects/shokunin/kasegi-shokunin || exit 99
for f in cvss-v4-severity-and-vector coordinated-disclosure-timelines \
         authorization-safe-harbor-and-scope ai-assisted-finding-validation \
         cwe-top25-2025-methodology multiparty-vulnerability-coordination \
         cna-assignment-and-vulnerability-rules cra-manufacturer-reporting-duties; do
  p="corpus/knowledge/$f.md"; [ -r "$p" ] || { echo "$f NORESULT"; continue; }
  r=$(grep -m1 '^recheck: ' "$p" | sed 's/^recheck: //'); [ -n "$r" ] || { echo "$f NORESULT"; continue; }
  bash -c "$r" >/dev/null 2>&1; echo "$f $?"
done
```

before `3/8` (F01–F05 exit 2 `not-listed`) → after **`8/8`**. Entry-bound harness
(`frontier-recheck-count.py`, `c1-counterA-{before,after}.json`): before
`entries=8 pass=3 exit=1` → after `entries=10 pass=10 exit=0` (F09's two entries
included, because C2 adds them to the admitted set).

**C1 counter B — dispatch matrix pass count.**

```sh
python3 corpus/instruments/resolve-dispatch-check.py            # landed bytes
python3 corpus/instruments/resolve-dispatch-check.py --resolver \
  .ufo/waves/round-24/c1-baseline-resolver.py                  # do-nothing control
```

before (round-23 resolver `690153ad…`) **`cases=8 pass=4 exit=1`** → after
(`db5e0767…`) **`cases=8 pass=8 exit=0`**; round-23 containment matrix regression
**24/24 exit 0** both sides (`c1-containment-regression.txt`). Degenerate
instruments: always-GONE `1/8`, always-INTERNAL `0/8`. Published blind spot: a
bound-64→8 brace mutant scores 8/8 and 24/24 (R11).

**C2 — frontier topics and package entries.**

```sh
awk -F'|' '$2 ~ /^ *F[0-9]+ / && $4 ~ /^ *admitted *$/ {n++} END{print n+0}' corpus/README.md
grep -lE '^source: S03[2-5] ' corpus/knowledge/*.md | wc -l
```

before `8` and `0` → after **`9`** and **`2`**. Frozen command for the second
counter (`S1[0-9][0-9]`) reads `0 → 0`; the erratum above explains why and the
corrected command is what measures the frozen predicate.

**No-harm guard.** `density.py SKILL.md` mean **154.0** before and after (SKILL.md
bytes untouched; 652 path-citation instances, 19 blocks, exit 0);
`anchorcheck.py SKILL.md` 0 bad / `LOST-RECORDED=306` / exit 0 both sides.

## Sources & frontier

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi
```

before (`assimilation/census-before.txt`): **exit 0**, rows **31**, malformed 0,
tier A=29 C=2, status mined=19 queued=9 rejected=3, W04 ×2 (S028, S029).
after (`census-after.txt`): **exit 0**, rows **35**, malformed 0, tier **A=32 B=1
C=2**, status mined=23 queued=9 rejected=3, same two W04s (both declared:
S028 is the rejected duplicate-row proposal; S029 opens `supersedes S024 —`).
Rows added by tier: A **+3** (S032, S033, S035), B **+1** (S034), C ±0.

Rows touched old → new (all four are new rows, not edits):
`S032 — → mined, opened — → 2026-10-25, recheck — → 730d, used-by — → authorised-testing-rules-of-engagement.md`;
`S033 — → mined, 2026-10-25, 730d, → statutory-authorization-and-unauthorized-access.md`;
`S034 — → mined, 2026-10-25, 180d, → same`;
`S035 — → mined, 2026-10-25, 730d, → same`.
One same-round field correction: S034's title `防止 → 禁止` (the page's own
`<title>` and 平成11年法律第128号 read 禁止), logged in the lesson Gate.

Frontier rows advanced: **F09 admitted** (new topic) → 8/8 → **9/9**;
`corpus/README.md` provenance count 33 → 35 entries; `PROVINCE.md` Frontier line
now F01–F09.

**Assimilation (§10).** Package `/home/vgpnk/Projects/shokuknow/merge/kasegi`
read-only, tools not run. One theme, two entries, four rows. Package staged ids
S031–S124 vs lane max S031 → **1 collision (S031)**; guard proven on an indented
scratch fixture (`guard-proof.txt`: 0-3-space pattern finds it, column-zero-only
does not). Renumber map (by document, append order):
`S123→S032`, `S039→S033`, `S040→S034`, `S041→S035`; the other 90 staged rows get
no id. Quarantine: the lane's register slice is **7 rows** (S037, S048, S054,
S065, S068, S069, S070) — none adopted; hand-check verdicts
(`quarantine-handcheck.txt`): S048 **404** dead as cited, S069/S070 **302/0 B**
unreachable as cited, S037 payload absent behind the preview tool, S054/S065/S068
reachable today but no quote located, so none is appendable.

## Trend verdicts

- **expansion — improved.** One new frontier topic admitted (8/8 → 9/9) with two
  entries on ground the lane provably did not hold (repo-wide grep 0 hits at base
  for "rules of engagement"/"engagement document"/"statutory authorization"), four
  registry rows opened and pinned this lane, and two capabilities entered
  (`frontier-recheck-harness`, `source-capture`). Counter-argument a hostile
  verifier would make: F09 is one topic and the entries are public-method
  documents, not new domain technique — the expansion is breadth, not depth.
- **quality — improved.** Both routed verifier defects are fixed with a
  do-nothing control that cannot meet the counter; four wave-1 seats proved the
  old counter A gameable four ways and the harness now closes those routes
  (R12); the rechecker gained Q9 binding and an anchor; the resolver ate three
  dispatch defects plus two CLI guards that a wave-1 seat's accident motivated.
  Honest limits published, not hidden: the bound-64→8 mutant survives both
  matrices, and the dispatch matrix's L4 fail-before rides on its second citation.
- **discernment — improved.** A package entry was **refused against its own cited
  source** (its 285 text carries no 情节严重 element for the paragraph it
  characterises), three standards-body entries were refused on PROVINCE scope,
  and two of the round's own frozen artefacts were corrected by erratum rather
  than silently edited (`frozen_at_utc`, counter B's id band). The weakest
  remaining sentence is C1's "from committed captures": a recheck can be re-pointed
  at another manifest, and only R12's harness — not the claim text — forbids it.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited
  sources — verified this round by `QuarterSHONEN` (`SKILL.md:134`, `:1014`,
  `:680`, `:565`, `:60-87`, 10 `S###` cites all present in `corpus/SOURCES.md`);
  no promotion claim.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — still
  false: 27 LOG entries, none records executing a domain work item, and all three
  domain roots remain absent (`root-loss-2026-10-12.md`); L0 round-15 re-scope
  still open at `.ufo/l0-questions.md:10`.
- [~] Instructions executable by an agent without oral context — the lane's own
  documented invocations run cold from a `git archive` export (5/5 exit 0), but
  the pipeline they describe names 14 `ops/*` executables that no longer exist.
- [~] No cross-domain bleed (PROVINCE.md accurate) — `ConnSibling` confirmed no
  sibling lane claims this ground (chousa refuses bounty scope and routes it to
  kasegi; tabi/kotodama disclaim), and PROVINCE.md is updated for F09; the
  residual adjacency (chousa owns external-target approval, tabi interaction
  approval) is reported, not absorbed.

## Round shape, waves, capacity

- Wave 1 `kasegi-r24-build`: **43 seats** (scout 22, reviewer 7, executor 5,
  scribe 3, critic 3, mutation-tester 1, connector 1, sentinel 1), all 43 reports
  landed under `.ufo/waves/round-24/wave1/`. §3 L2 floor met inside wave 1; L1
  holds the canonical planner seat and `PlannerWalk` supplied the data-walk.
- Wave 2 `kasegi-r24-falsify`: **35 seats**, attack roles **24/35** (reviewer 12,
  critic 6, revenger 3, mutation-tester 2, sentinel 1), validated under
  `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy.json` (band 32–64).
  **Refused four times at dispatch** with `Background job limit reached (100)`,
  0 seats spawned, payload never split or shrunk — `wave2-refusal-{1,2,3,4}.json`.
- **Round total: 78 seats** (inside the 128 cap). **Dead seats: none** in wave 1;
  wave 2 never spawned. **No residual call** was needed (wave 1 produced 43
  reports including 11 attack seats).
- **Tool installs: none** (no pacman, no uv, no npm; `pdftotext` and `curl` were
  already present). Pacman pause respected.
- **Attempt numbering:** the host launched this round three times as
  `attempt=1` (inline driver); the lane counts landings, and this report is
  landing 1 of round 24. Both conventions stated per the lesson (routed defect 3).
- **Stale-lane:** respawn-per-round driver; this is the lane's only open mission —
  round 24 launched in-session by the hyaku orchestrator and is complete with this
  report. No other kasegi mission is open.
- **L0 questions:** none added this round. Pre-existing open item unchanged:
  kasegi round-15 re-scope (`~/Projects/bounties` lost, PROVINCE root), which is
  unreachable work rather than a blocker for this round.
