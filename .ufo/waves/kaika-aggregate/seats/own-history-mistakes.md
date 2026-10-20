# own-history-mistakes — aggregator self-defect ledger, rounds 6–11 → Round 12

**Seat.** `KaikaAggregateR12.OwnHistoryMistakes` (reviewer). Read-only review; no child repo,
gate, script, score, or ledger byte was modified.

**Revision bound.** Fleet-aggregate worktree HEAD `ee8ba85736ee`
(`git rev-parse --short=12 HEAD`), commit `2026-10-19T20:15:19-03:00
"rounds ledger: mori r12 closure (admitted) — kaika, non-author verified"`;
`git status --porcelain | wc -l` → `0`. Fleet root `/home/vgpnk/Projects/shokunin`
has **21** physical `*-shokunin` lanes (`find … -maxdepth 1 -type d -name '*-shokunin' | wc -l` → `21`).

**Limits (read first).**

1. Every score quoted is the record's, not a re-grade. The restored card's last values are
   corpus review **9**, cross-lane quality **9**, mint/dormancy **9** (`SCORECARD.md:395-408`).
   This note offers **no new numeric score** and changes none.
2. **No census total is published or frozen here.** The parent states a parser fix for indented
   Markdown source rows is in flight; any census baseline is therefore provisional. §3.3 records
   the exact selector defect, not a row count.
3. Historical `AGGREGATE.md` sections are append-only; corrections live where they were filed,
   not in a rewritten past.
4. This seat file is untracked (`git ls-files .ufo/waves/kaika-aggregate/` → 0 files). Under
   existing proposal **C-B** (`.ufo/waves/kaika-w1/aggregator-state.md:369`) and self-defect **21**,
   an uncommitted seat is **not evidence** until the parent commits it.

## 1. Where the record is (exact anchors)

Restored `SCORECARD.md` (473 lines; restore provenance §1.1):

| Block | Lines |
|---|---|
| Aggregator lane header + round-6 move + C1–C8 / Q1–Q6 / M1–M3 | 234–285 |
| Round 7 (refresh 5) — M3–M6 | 286–303 |
| Round 8 (refresh 6) — X1–X8, D-129 repairs at 320–326, repair note 328–334 | 304–371 |
| Round 9 (refresh 7) — V1–V12 | 336–371 |
| Round 11 (refresh 8) — M7–M11 | 372–394 |
| Round 11 final training re-run | 395–408 |
| Planned / Retired / Move log | 409 / 427 / 441 |
| Round 10 (2026-10-15 relaunch) | 452–473 |

`.ufo/reports/AGGREGATE.md` (2,132 lines): §11.7 self-defects 1–8 (line 794); §11.9 (826);
§12.4 9–11 (957); §13.4 (1294); §13.5 12–18 (1324); §13.7 (1428); §13.8 item 19 (1461);
§14.4 item 20 (1573); §14.7 (1643); §14.11 items 21–24 + wrong resolver (1751);
§14.12 table 20–26 (1777); §15.5 (2068); §15.7 items 27–29 (2099); §15.8 D-151–D-155 (2111).

Round-9 **verifier** passages: `.ufo/waves/round-9/seats/reviewer-citations.md`
(cell grades 9–16; `§13.6` execution notes 24; historical three-FAIL recheck 38),
`.ufo/waves/round-9/seats/standing-tables.md:170-206` (findings F1/F2),
`.ufo/waves/round-9/seats/critic.md` (attempts A1–A7),
`.ufo/waves/aggregator-r11/seats/reviewer-verify.md` (checks 1–12 and dissents D1–D5).
Round-9 gate declarations: `.ufo/waves/round-9/corpus-gate.mjs:88-115` (“RULES NOT EVALUATED”).

Current-era dossier: `.ufo/waves/kaika-w1/aggregator-state.md` — §1.1 round-number collision
(line 41), §3.3 verdict practice, §7 mistakes M1–M10 (358), §8 contract defects A1–A18 (395),
§10 census design. It is stamped at HEAD `31baf5c`, **before** the restore.

### 1.1 Restore state

`31baf5c` replaced root `SCORECARD.md`/`LOG.md` with kotoba-lane bytes; `7c5b34f` restored both
to the `12f2da5` blobs (`LOG.md:847-877`; `git log --oneline -3 -- SCORECARD.md` →
`7c5b34f`, `31baf5c`, `0b1ac3b`). At my HEAD, `grep -c '^## Aggregator lane' SCORECARD.md` → `1`
(it was `0` at `31baf5c`). The clobber class now has a committed detector:
`.ufo/gates/root-ledgers.py` (`7c5b34f`) checks `aggregator_section_lost` among other losses
(`LOG.md:879-905`). This is the **A1/A2** repair, and it is why this review could read the
aggregator record at all.

## 2. Recurring defect classes — directly evidenced

Each row cites the record that filed it. “Status” is the record's status, not my re-test.

### 2.1 Evidence not committed (uncommitted wave / session-scoped transcripts)

| # | Instance | Reference |
|---|---|---|
| 1 | Aggregator lessons left uncommitted in live child trees; one swept into a lane commit | §11.7 item 1 |
| 8 | Staged ledger rename consumed by another lane's bare commit (`ade32e4`) | §11.7 item 8 |
| 12 | Round-7 ledger/SCORECARD/LOG/report written but never committed; landed next round as `6d27283` | §13.4; §13.5 item 12 |
| 21 | Round-8 committed ledger + report but **not the wave**; `.ufo/waves/round-8/` absent ⇒ X2/X3/X4/X8 unreproducible | §14.11; §14.12 item 21 |

Corrections on record: commit-before-report ordering rule **P-r** (§13.4), and round 9's
committed wave **15/15** (SCORECARD V6). The class recurred after being “fixed” once
(12 → 21), so a past fix is not proof of current durability.

### 2.2 Unreproducible aggregate counts

| Cell | Published | Re-derived | Reference |
|---|---|---|---|
| X2 commands | 115 (105 ok / 10 fail) | 99 strictly indexed rows; ok/fail split encoded nowhere | `SCORECARD.md:320`; `reviewer-citations.md:10` |
| X3 break points | 28 | 17 (5+0+3+4+0+5) | `SCORECARD.md:321`; `reviewer-citations.md:11` |
| X4 gated rows | 30 (12/18) | not mechanically countable (naive pipe count 37 incl. headers) | `SCORECARD.md:322`; `reviewer-citations.md:12` |
| X8 re-executions | 41 = 30/8/3 | no committed cell ledger exists | `SCORECARD.md:326`; `reviewer-citations.md:16` |
| §13.3 kessho cell | 6 lanes / 9 artifacts | 5 lanes / 15 tracked harnesses | §14.12 item 23; `standing-tables.md:188-202` |
| Report headline | 17 child commits | own enumerations say 16 and 15 | §14.12 item 24; §14.11 |

Root cause, one line from the record: *“round 8 committed the ledger and the report but not the
wave. So its numbers were author-asserted aggregates over payloads a non-author cannot reach.”*
(§14.11). Repair: D-129 in-place cell repair (`SCORECARD.md:320-334`) with the unpublished
evidence gap named as permanent. The governing existing rule is `CORPUS.md:33`
(a count is evidence only with its counting command); **P-q** says an audit row's command must
reproduce its own observed cell (`AGGREGATE.md:1422`). `kaika-w1` M2 records the same class.

**Round-12 direct relevance:** this is the class that makes a provisional census baseline
dangerous. Publish only (count, unit, command, revision, dirty count), never a total whose
payload was session-scoped or produced by a selector under repair.

### 2.3 Selector / row misread (wrong rows, wrong file, wrong window)

| # | Defect | Exact reference |
|---|---|---|
| 9 | Dormancy scan: case-sensitive token, `sort -V` filename ranking, shared-LOG attribution; under-reported kotoba (`round-9` vs `## Round 10`) | §12.1 corrections 1–3; §12.4 item 9 |
| 14 | Published “copy-paste runnable” block that emits empty on this host (`pi-uu-grep 0.2.0`, zero-length `-oE '[0-9]+$'`); unanchored variant admits noise | §13.5 item 14; §13.6-R replacement |
| 15 | Mixed windows: “7 L0 entries at cutoff” where the cutoff blob had 6; pointer to `~/.config/opencode:158` (a directory) | §13.5 item 15 |
| 22 | §13.6-B “last bold mark” resolver returns kumitate's **withdrawn** `[ ]`, not the operative `[x]` ⇒ any consumer mis-grades | §14.11; §14.12 item 22; D-130; `reviewer-citations.md:24`; `standing-tables.md:170-187` |
| 25 | 138 unqualified cross-repo citations in mirrored lessons; 6 counted `UNRESOLVED` by kagi's own gate | §14.12 item 25; fixed in-round 9→0 in the six drafts (P-t) |

**Live instance for Round 12 (the in-flight fix).** The census selector is indentation-blind:

- `scripts/sources-census.sh:464` — gawk `if ($0 !~ /^\|/) next` (a row must start with `|`
  at column 0).
- `scripts/sources-census.sh:404` — bash used-by scanner `[[ "$line" == '|'* ]] || continue`
  (same assumption, second parser).
- `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:68-80` — every published census command anchors
  `^\|`, so the contract's own manual commands skip indented rows.
- `scripts/fixtures/sources-census/` contains **no** indented-row fixture:
  `grep -rln '^[ \t]\+| S' scripts/fixtures/sources-census` → no output, exit `1`.

Consequence: an indented `| S### | … |` row is invisible to census **and** to validation
(E12 included), so totals under-count silently while the run looks clean. This is the same
defect shape as 9/14/22 — a selector that answers a narrower question than the one claimed.
No total from this instrument should be frozen until both parsers and the fixtures are fixed
and the parent signals `FINAL LANES READY`. (I did not run the census; no totals are claimed.)

### 2.4 Duplicate / colliding queue IDs

| Evidence | Reference |
|---|---|
| Key collision refused (`D-50…D-58` reused by protocol) | SCORECARD X7; §13.2 |
| Duplicate groups folded (`D-39⊇D-85`, `D-51⊇D-84`) | SCORECARD X7; §13.2 |
| 84 distinct keys / max D-86 at r8; 118 distinct / 116 definition rows / max D-120 at r9 | V9, §14.14-R6 |
| r11: 160 rows / 146 distinct / max D-150; **14 repeated keys are status updates/folds, not divergent-text collisions**; new keys begin D-151 | §15.5 |
| Current at my HEAD | `grep -cE '^\| D-[0-9]+'` → **165 rows**; `sort -u` → **151 distinct**; max **D-155** (14 repeats) |

Existing practice (not new): next free key, then classify each repeat as status-update vs
divergent-text collision (V9's one-liner); never reuse a key for a different claim.

### 2.5 Omitted / stale verdicts

- **Round 8 owed rule-10 verdicts** and said so rather than silently reusing them:
  *“an unrefreshed verdict is a stale claim, not a neutral one”* (§13.7).
- **Round 9** re-emitted 6/6 at named revisions (V1; §14.2), and the gate's `r10` findings
  cleared 6→0 only after the obligation was discharged (V7, §14.17).
- **Round-7 report omitted the `SHONEN` heading**; D-120 was first filed against protocol,
  then narrowed to this lane and closed by re-filing (§13.8 item 19).
- **Markers:** round 5 (254 B) and round 10 (187 B) are failed reports, not rounds
  (`stat -c '%s'` → 254 / 187; `reviewer-verify.md` check 5). Round 11's marker-overwrite gate
  found 5 live instances (D-153; SCORECARD round-11 final re-run).

**Round-12 direct relevance:** `kaika-w1` §3.3 recorded **21/21 failed** at **live worktrees**
(1,374 findings, 3 dirty/provisional) — that is the dossier's measurement, not mine. A verdict
must name revision **and** `dirty=N`; a dirty worktree result may not be frozen (A17), and a
gate/SOURCES structural clean is not semantic conformance (§4).

### 2.6 Falsified status / claims over a moving tree

| # | Falsified claim | Evidence |
|---|---|---|
| 11 | Wave seed baseline served as truth; counters/reports/LOG/commits moved within 10 minutes | §12.4 item 11 |
| 13 | Kotoba “self-healed inside the refresh” — entry landed `633859f` at 23:27:55Z, **after** the 22:55:03Z cutoff | §13.5 item 13 |
| 15 | Post-cutoff L0 line published as a cutoff measurement | §13.5 item 15 |
| 24 | Three different child-commit totals (17/16/15) in one committed report | §14.11; §14.12 item 24 |
| 27–28 | Mint census measured `minted` (always-empty array), not `type=="mint"`; seed then over-corrected to “no ledger record” while `rounds[36]` existed | §15.7 items 27–28 |
| 29 | One dormancy LOG grammar prescribed; 6 of 7 child repos use another | §15.7 item 29 |
| D-153 | kotoba r15 report overwritten 14,715 B → 273 B marker at the canonical path | §15.8; SCORECARD round-11 final re-run |
| r11 dissents | Mint was ledgered 13 s after launch; `17c1fad` did stage the kama gitlink (reverted 13 s later); “7 pre-kama lanes” has no seventh repo; kama r1 fleet-wrapped three times before real completion | `reviewer-verify.md` D1–D4 |
| r11 volatility | kagi HEAD moved mid-verification; commit-age cells require an aggregator-author filter | `reviewer-verify.md` check 10, “VOLATILE” |

**Live Round-12 round-number collision (uncorrected; `kaika-w1` §1.1):**
`.ufo/state/aggregator.round` → `10`; `.ufo/reports/round-10/aggregator.md` → 187 B marker;
`.ufo/reports/round-11/aggregator.md` → 14,359 B real; `MANIFEST.json` last aggregator lane row
→ round **12 `in-flight`**; prompt file `aggregator-round-12.md` exists; the working namespace
is `kaika-aggregate`. Advancing a counter blindly to 11 would target the path holding the real
r11 report — exactly the D-153 marker-overwrite class. The namespace/round reconciliation is
the parent's to record; this note only pins the state.

### 2.7 False charge against a sibling

- Round-5 charge against kotoba **withdrawn** (D-80; §11.7 item 3).
- D-120 first filed against protocol for a ruling protocol had already published, and which
  this lane itself had reopened; closed by re-filing (§13.8 item 19).
- Named cost: *“a false auditor claim costs the audited lane a repair cycle it does not owe”*
  (§11.7 item 3). Existing guard: read the sibling's own artifacts before filing.

### 2.8 Scope / identity / self-audit bias

| # | Defect | Reference |
|---|---|---|
| 7 | Round-3 write-scope violation adjudicated, no rewrite | §11.7 item 7 |
| 18 | Round 6 pushed into six child remotes with no push scope; lessons committed locally thereafter | §13.5 item 18 |
| 20 | Rule 8 published “clean everywhere” while the literal `op://` hits sat mostly in **this lane's own** mirrored lessons; D-125 routed, forward-only fix | §14.4; §14.12 item 20 |
| 25 | Self-authored cross-repo citation debt measurably reddened a sibling's gate | §14.12 item 25 |
| M10 / A13 | Later aggregator work authored `ci`, not `aggregator-shokunin`; last lane-authored commit `b159992` (2026-09-29); `79752af` (which carries the round-10 discovery patch) is a `ci` WIP checkpoint | `kaika-w1` §7 M10, §8 A13, E19; my `git show -s 79752af` → `ci`, “checkpoint WIP” |

**Round-12 direct relevance:** the kaika campaign's standing rule is **no push**
(`.ufo/waves/kaika/PLAN.md`); all 21 lanes are read-only. Any citation to a main-repo commit
should distinguish lane-authored evidence from `ci` integration commits.

### 2.9 Plan / axis / registry bookkeeping

- **26:** axis switched away from committed `### Planned` without amending it first; merit was
  right, reader expectation was not. Reason now recorded in the round-9 header/§Planned.
- **A5:** aggregator had 0 capability rows, no saturation line, and no current planned claim;
  the only planned round-12 item was already superseded by the round-11 final re-run
  (`kaika-w1` §2).
- **A2/D-120:** registry home absent (no aggregator `SKILL.md`); restored section is now the
  registry home (`PROTOCOL.md:360` per w1 §3.4/§10).
- **A11:** fleet ledger's last aggregator row sat `in-flight` since 2026-09-29.

## 3. Classification for Round 12

### 3.1 Live hazards — guard before publishing anything this round

| Hazard | Why it is live now | Existing guard to apply (no new rule) |
|---|---|---|
| Uncommitted wave / seats | `.ufo/waves/kaika-aggregate/` has **0 tracked files** at my HEAD; seats are being written untracked | P-r ordering (§13.4); C-B (only committed evidence is evidence); self-defect 21 |
| Census totals | Parent says indented-row parser fix in flight; selector lines §2.3 | No frozen totals; name unit+command+revision+dirty; wait for `FINAL LANES READY`; C-A (predicate needs a positive fixture) |
| Selector/row misread | two parsers (`:404`, `:464`) + contract commands (`SOURCES-CONTRACT-v1.md:68-80`) all assume `^\|`; no indented fixture | Re-run after fix; verify both parsers; do not present a `^\|`-only scan as coverage |
| Queue key integrity | 165 rows / 151 distinct / max D-155 (14 repeats) | Start at D-156; classify repeats; D-87 refusal precedent; V9/§15.5 |
| Verdict staleness | 0/21 conformant baseline is live-worktree, `kaika-w1`-stamped, 3 lanes dirty | §13.7 stale-claim rule; revision + `dirty=N`; never freeze a dirty result (A17) |
| Round/namespace status | counter 10 / report 11 / MANIFEST 12 in-flight / prompt 12 / `kaika-aggregate` | Record the namespace; do not advance into the r11 path (D-153; w1 §1.1) |
| False sibling charge | D-80 / D-120 class | Read the sibling's own artifact first; cost is a wasted repair cycle |
| Scope / identity | read-only children; no push; `ci` vs lane identity | kaika PLAN no-push rule; PROTOCOL lane-identity expectation (M10/C-H) |
| Marker as report | r5 = 254 B, r10 = 187 B exist | Marker clause; `reviewer-verify.md` check 5; do not count as rounds |
| Self-mirror rule 8 / citations | any aggregator lesson written this round inherits the class | Forward-only zero unqualified credential-shaped refs; path-convention line (P-t) |

### 3.2 Already corrected / mitigated — cite the correction, do not re-litigate

| Items | Correction |
|---|---|
| 9, 10 | §12.1 + R4 (host-independent entry scan); §12.2 quotes the bar verbatim |
| 11 | Cutoff-only evidence practiced; every later refresh stamps its cutoff |
| 12 → 21 | P-r ordering + round-9 committed wave (V6 15/15) — **discipline still required**, not structural immunity |
| 13, 15 | Corrected in §13.3/§13.5; append-only history left intact |
| 14 | §13.6-R ships only the entry-scan form |
| 16 | P-n proposal + pre-flight read of mutating verbs |
| 17 | Corrected commit form (`git add -- <path> && git commit -- <path>`) |
| 18 | Recorded; round-8 lessons committed locally, not pushed |
| 19 | D-120 closed by re-filing the round-7 assessment |
| 20 | D-125 routed; forward-only fix in the six drafts |
| 22 | Tail-anchored operative-block rule (P-o); D-130; corrected in §14.11 |
| 23, 24 | D-129 in-place repair + §14.11; the missing round-8 evidence is named unrepairable |
| 25 | In-round fix 9→0; path-convention line; P-t proposed as CORPUS rule-6 clarification |
| 26 | Switch reason recorded in the round-9 block |
| 27–29 | §15.1–§15.3: `type=="mint"` census; `rounds[36]` probation recognized; per-repo LOG matcher reproduced all 8 verdicts |
| D-129 cells | `SCORECARD.md:320-334` repaired where they stand, published figure kept visible |
| A1/A2 | `7c5b34f` restored `SCORECARD.md`/`LOG.md` to `12f2da5` blobs; `.ufo/gates/root-ledgers.py` detects `aggregator_section_lost` |

“Corrected” means the record was annotated or the practice changed; it does **not** mean the
class cannot recur (12 → 21 is the proof).

### 3.3 Not this round

- **Mint/dormancy axis calls:** not the selected scope; `kaika-w1` §5 says the candidate table
  is stale after nine mints and roster changes — do not copy old calls as current.
- **Scores:** all three axes are 9; this round is an assessment, not an axis move. No score may
  be raised by this note.
- **Corpus-gate semantic claims:** a gate pass is not whole-corpus conformance. The gate itself
  declares `r1`, `r3`, `r5`, `r6`, `r9`, box-3 independence, and SHONEN truth **not evaluated**
  (`.ufo/waves/round-9/corpus-gate.mjs:88-115`). A SOURCES structural clean is likewise not
  evidence of truthful rows.

## 4. Residual risk and verification gaps

1. **Round-8 evidence is permanently unreproducible** (wave never committed); X2/X3/X4/X8's
   corrected figures are committed lesson rows, not a re-run (D-129 note, `SCORECARD.md:328-334`).
2. **Historical defects 1–29 cannot be rewritten**; the ledger's corrections are the record.
   Cumulative count was 26 at r9 (V12) and 29 at r11 (§15.7); treat the series, not a clean state.
3. **Census dual parsers** may diverge even if one is fixed; the fixture set has no indented-row
   case, so a green selftest would not prove the fix without a new fixture.
4. **Gate tallies are record-quoted, not re-run by me:** r9 V2 (selftest 12/12, 8/8 frozen),
   r11 `reviewer-verify`/`kaika-w1` E8/E20. Assignment forbids builds/tests; I executed none.
5. **Dossier measurements are at `31baf5c`;** my HEAD is `ee8ba85` and the restore changed
   SCORECARD/LOG bytes. Re-run before quoting any dossier count.
6. **This note's own durability:** untracked until the parent commits the wave. If it stays
   untracked, C-B says it is not evidence — the same rule the ledger applied to round 8.

## 5. Exact commands and observed outputs (this review)

All run read-only from
`/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate` unless a path is absolute.

| # | Command | Observed |
|---|---|---|
| 1 | `git rev-parse --short=12 HEAD` | `ee8ba85736ee` |
| 2 | `git log -1 --format='%aI %s'` | `2026-10-19T20:15:19-03:00 rounds ledger: mori r12 closure (admitted) — kaika, non-author verified` |
| 3 | `git status --porcelain \| wc -l` | `0` |
| 4 | `grep -c '^## Aggregator lane' SCORECARD.md` | `1` (exit 0) |
| 5 | `wc -l SCORECARD.md` / `wc -l .ufo/reports/AGGREGATE.md` | `473` / `2132` |
| 6 | `git ls-files .ufo/waves/kaika-aggregate/ \| wc -l` | `0` |
| 7 | `ls -A .ufo/waves/kaika-aggregate/seats/ \| wc -l` | `9` at check time (sibling seats; this file is an additional untracked artifact) |
| 8 | `find /home/vgpnk/Projects/shokunin -maxdepth 1 -type d -name '*-shokunin' \| wc -l` | `21` |
| 9 | `find .ufo/reports -path '*/round-*/aggregator.md' -printf '%p %s\n' \| sort -V` | r3 8000 · r4 12837 · r5 **254** · r6 15931 · r7 10695 · r8 24058 · r9 18604 · r10 **187** · r11 14359 bytes |
| 10 | `cat .ufo/state/aggregator.round` | `10` |
| 11 | `jq -r '.rounds[]\|select((.lanes//{})\|has("aggregator"))\|[.round,.type,.lanes.aggregator]\|@tsv' MANIFEST.json \| tail -3` | `9 closure-correction ok`; `11 closure-correction ok`; `12 closure-correction in-flight` |
| 12 | `grep -cE '^\| D-[0-9]+' .ufo/reports/AGGREGATE.md`; distinct; max | `165` rows; `151` distinct; max `D-155` (⇒ 14 repeated keys) |
| 13 | `sha256sum .ufo/waves/round-9/corpus-gate.mjs` | `e7d49942017a8c522e2b16f3de78e60d16a23ffad6838396a8c44897c12299c3` |
| 14 | `git log --oneline -3 -- .ufo/waves/round-9/corpus-gate.mjs` | `79752af` (ci WIP checkpoint), `6415a9b` (round-9 lane commit) |
| 15 | `grep -nF '$0 !~ /^\|/) next' scripts/sources-census.sh` | `464` |
| 16 | `grep -nF "[[ \"\$line\" == '\|'* ]] \|\| continue" scripts/sources-census.sh` | `404` |
| 17 | `grep -rln '^[ \t]\+| S' scripts/fixtures/sources-census` | no output, exit **1** (no indented-row fixture) |
| 18 | `git log -1 -- scripts/sources-census.sh` | `ae7bf19 2026-10-19T19:52:48-03:00 ci scripts: sources-census.sh …` |
| 19 | `git log -1 -- .ufo/gates/root-ledgers.py`; `git log --oneline -3 -- SCORECARD.md` | `7c5b34f`; `7c5b34f`, `31baf5c`, `0b1ac3b` |
| 20 | `grep -n 'D-129' SCORECARD.md` | lines `320`, `321`, `322`, `326`, `328` |
| 21 | `stat -c '%s %n'` on r5/r10/r11 reports | `254`, `187`, `14359` bytes |

**No tests, builds, gates, or censuses were run.** Every gate/census figure above is quoted
from the cited record with its own revision and remains provisional where the record says so.
