# exec-compact.md — round-13 `protocol` lane: PROTOCOL.md compaction (body + appendix artifact + record)

Seat: ExecCompact (L2, `protocol` lane, round 13). Write scope: `.ufo/waves/round-13/` only.
`PROTOCOL.md` was never written (read-only); no commit, no `git add`, no path outside the wave dir.

**Base = the live file at `2d19a64`** (`sibling-mint allowance + kama probation entry`): `PROTOCOL.md`
541 lines / 50603 B, md5 `444667c4a69f5998f9abb957a68a4343`. An earlier pass ran on `e275d4a`
(526 lines, md5 `63de15a37a42ce57decb951a7e8aa2f0`); §12 records the rebase and its cost.

**Toolchain rebased under this pass too** (by siblings, mid-flight): `obligation-census-r13.tsv`
156 → **169 rows** (the seven `2d19a64` sibling-mint rows L8–L20) and `anchor-phrases.txt`
51 → **61 anchors** (10 appendix-region anchors, which that file's own header documents as “present in
the appendix region and absent from the body”). All numbers below are from the rebased toolchain; the
census is treated as the integrator's committed expected value, and no predicate or row was edited by
me.

## 0. Deliverables (measured)

```
$ wc -l -c PROTOCOL.md .ufo/waves/round-13/PROTOCOL.compact.md \
      .ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md \
      .ufo/waves/round-13/PROTOCOL.compact.singlefile.md
   541  50603 PROTOCOL.md
   459  38858 .ufo/waves/round-13/PROTOCOL.compact.md
    40   9570 .ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md
   493  48020 .ufo/waves/round-13/PROTOCOL.compact.singlefile.md
  1533 147051 total
```

| Artifact | Lines | Bytes | Role |
|---|---|---|---|
| `PROTOCOL.compact.md` | **459** | 38858 | normative body: header + `## Lifecycle` … `## Fleet-2 conventions (adopted)` + the 4-line `## Appendix` pointer block. Target ≤460 → 459. |
| `PROTOCOL-APPENDIX.compact.md` | 40 | 9570 | appendix artifact: title + 3-line preamble + the incident table (header, separator, **32 dated rows**) byte-identical to the live `PROTOCOL.md` lines 508–541. |
| `PROTOCOL.compact.singlefile.md` | 493 | 48020 | same content in single-file form (appendix in-file), for the record; §11. |
| `PROTOCOL.md` | 541 | 50603 | untouched live source. |

## 1. Per-section before → after (body)

| Section | before (live 541-line `PROTOCOL.md`) | after (body) | Δ |
|---|---|---|---|
| header (title → before `## Lifecycle`) | 7 | 6 | −1 |
| `## Lifecycle` (incl. the `2d19a64` Sibling-mint bullet) | 36 | 34 | −2 |
| `## Promotion gates` | 26 | 17 | −9 |
| `## Round-robin rounds` | 251 | 224 | −27 |
| `## Evidence standard` | 40 | 31 | −9 |
| `## Gate standard` | 40 | 45 | **+5** (round-13 obligations) |
| `## File contract per shokunin repo` | 26 | 26 | 0 |
| `## Invariants` | 53 | 48 | −5 |
| `## Fleet-2 conventions (adopted)` | 22 | 23 | **+1** (round-12 L0 axis mapping) |
| `## Appendix — incident digest (why these rules exist)` | 40 | 5 (pointer block: heading + 3 lines + trailing newline) | −35 |

Body spans (measured): header 1–6, Lifecycle 7–40, Promotion 41–57, Round-robin 58–281, Evidence
282–312, Gate 313–357, File contract 358–383, Invariants 384–431, Fleet-2 432–454, Appendix 455–459.
Arithmetic: `6+34+17+224+31+45+26+48+23+5 = 459` = `wc -l`; `541 − 82 = 459`. Positive deltas are new
obligations (Gate +5 = snapshot integrity + frozen-root resolution + reflow; Fleet-2 +1 = axis
mapping; Lifecycle/Round-robin absorb the history pin and the Sibling mint).

## 2. Census (rebased: 169 rows; legacy 93)

```
$ sh .ufo/waves/round-11/verify-census.sh .ufo/waves/round-13/PROTOCOL.compact.md \
      .ufo/waves/round-13/obligation-census-r13.tsv
169/169 obligations found; 0 MISSING          (exit 0)
$ sh .ufo/waves/round-11/verify-census.sh .ufo/waves/round-13/PROTOCOL.compact.md
93/93 obligations found; 0 MISSING            (exit 0)
$ # same two commands against PROTOCOL.compact.singlefile.md
169/169 obligations found; 0 MISSING   /   93/93 obligations found; 0 MISSING   (exit 0)
```

**MISS classification (L1 procedure): both candidates report zero MISS — classes (a), (b) and (c) are
empty for this seat.** The seven new rows L8–L20 are the `2d19a64` Sibling-mint obligations; they were
satisfied by *wording* (the census's own phrasing restored verbatim inside the compacted bullet, no
markup crossing a predicate, predicates protected from wrap splits) — not by weakening anything. The
TSV was not edited.

**R52 (five → six), per L1 ruling.** The body reads “and **expand by exactly six**: … and
writing/committing the append-only history pin `.ufo/history-pin.json` — the sixth, added in round 13
(the legacy `expand by exactly five` count is superseded); regeneration is a separate committed act
named in the round notes, never a repair inside the same closure pass” (body lines 154–159). Both
strings are present, so R52 passes before and after the retarget; recorded as “R52 retargeted by the
integrator (five→six)”, not as an obligation loss.

## 3. Committed gate `verify-protocol.sh` (rebased) — all eight checks

```
$ sh .ufo/waves/round-13/verify-protocol.sh PROTOCOL.compact.md \
      --census obligation-census-r13.tsv --max-lines 460 --max-body-refs 4
INFO census    obligation-census-r13.tsv rows=169 miss=0 169/169 obligations found; 0 MISSING
INFO anchors   anchor-phrases.txt phrases=61 missing=10 line-exact-missing=17
INFO modals    modal-census.tsv sections=9 floor-sum=120 measured-sum=113
INFO caps      PROTOCOL.compact.md lines=459/460 body-refs=1/4 (appendix heading at line 455)
INFO structure keys=## Lifecycle|## Promotion gates|## Round-robin rounds|## Evidence standard|## Gate standard|## File contract per shokunin repo|## Invariants|## Fleet-2 conventions (adopted)|## Appendix order=contract
INFO seed      shonen-seed.txt header-line=372 extracted-lines=8 byte-identical=yes
INFO appendix  PROTOCOL.compact.md rows=0/32 body-pointers=16 rows-source=PROTOCOL.compact.md
INFO xref      scope=PROTOCOL.compact.md refs=6 headings=9 unresolved=0
verify-protocol: findings checks=8 failed=3
     10 anchors      17 appendix      1 modals
```

All three failing check ids are **appendix-scoped by construction** under the L1 split — the
check-level analogue of class (c), not obligation losses:

- `anchors` (10) — exactly the 10 phrases the anchor file's own header says are “present in the
  appendix region and absent from the body”. They are present verbatim in
  `PROTOCOL-APPENDIX.compact.md` (the artifact that holds the digest) and in the record file, whose run
  reports `anchors missing=0`.
- `appendix` (17) — “appendix data rows 0 < floor 32 (rows read from PROTOCOL.compact.md)” plus one
  finding per pointer occurrence (gate counts `body-pointers=16`; 17 distinct row names, §6). The rows
  live in the sibling artifact per the spec, and the record file passes this check
  (`rows=32/32 body-pointers=16`).
- `modals` (1) — the Appendix floor (15) measured on a 3-line pointer block. All eight other sections
  meet their floors (body `measured-sum=113` vs `floor-sum=120`, whose 15-token Appendix floor is the
  pointer block's; Round-robin ≥57).

**Single-file record** — `sh verify-protocol.sh PROTOCOL.compact.singlefile.md --census obligation-census-r13.tsv`:

```
verify-protocol: findings checks=8 failed=1      (1 × caps: 493 > 470)
$ sh verify-protocol.sh PROTOCOL.compact.singlefile.md --census obligation-census-r13.tsv --max-lines 500
verify-protocol: clean checks=8 failed=0
```

So the record is content-clean on all seven content checks against the rebased toolchain (census
169/169, anchors 0 missing, modals ≥ floors, structure, seed byte-identical, appendix 32/32 +
pointers, xref 0) and fails only the line cap (§11).

Earlier in the pass the gate was briefly un-runnable (`verify-protocol.sh: line 435:
SECTION_KEYS: unbound variable`) while a sibling rebased it; the runs above are from the rebased
script, and every boolean check was additionally re-verified by hand after the `2d19a64` rebase (§4–§7).

**Toolchain churn, for the integrator:** at the moment this file was finalized, `verify-protocol.sh`
was again mid-edit by a sibling and aborted before evaluating anything —

```
$ sh .ufo/waves/round-13/verify-protocol.sh PROTOCOL.compact.singlefile.md --census obligation-census-r13.tsv
verify-protocol.sh: line 559: syntax error near unexpected token `{'
verify-protocol.sh: line 559: `            if (q[2] != "X" && !(q[2] in S)) { n++; PN[n] = q[2] }'
```

— i.e. a `could-not-evaluate` state of the tool, not a finding against the artifacts. Both artifacts
therefore carry the *last successful* gate run recorded above plus the independent hand checks; the
next closure pass should re-run the settled gate (and the census, which is now stable at 169 rows and
green on both files).

## 4. Body refs and headings

```
$ awk '/^## Appendix/{exit} {print}' PROTOCOL.compact.md | grep -o 'round-[0-9][0-9.]*' | wc -l
1                      (the §Evidence bullet `git rev-parse round-4`; gate: body-refs=1/4)
$ grep -c '^## ' PROTOCOL.compact.md
9                      (all nine sections, contract order; gate `structure` clean)
```

## 5. `SHONEN.md` seed byte-identical

```
$ diff <(awk '/^    # <name>/{x=1} x{print} /No cross-domain bleed/{if(x)exit}' PROTOCOL.md) \
       <(awk '/^    # <name>/{x=1} x{print} /No cross-domain bleed/{if(x)exit}' PROTOCOL.compact.md)
(no output) → SEED_OK (body); same for PROTOCOL.compact.singlefile.md → SEED_OK
gate: INFO seed … header-line=372 extracted-lines=8 byte-identical=yes
```

8 seed lines (body 372–379), byte-identical, followed by the original `Marks:` paragraph.

## 6. `(§Appendix, "X")` pointer sweep (cross-file)

17 **distinct** pointer names in the body (the gate counts 16 pointer *occurrences*): Lands last (2
rows), Orphaned report (1), Prompt embeds contract (1), Marker vs report (2), Stale-lane actuator (3),
Lane identity (1), Closure entries (3), Dispatch evidence (1), Liveness probes (1), Unlanded report
(1), No closure channel (1), Row identity (1), Append-only `rounds` (1), Ledger (1), Evidence standard
(1), Canonical form (1), L0 durability (1). Each resolves to ≥1 row of
`PROTOCOL-APPENDIX.compact.md` whose first column names it — `UNRESOLVED: []` (sweep) and the gate's
`appendix` pointer findings are only about their absence from the *body file*. The pointer block (body
455–458) avoids a literal `(§Appendix, "X")` template so the sweep has no phantom name; section refs
`§Appendix`, `§Evidence standard`, `§Gate standard`, `§Invariants` resolve to headings that exist
(gate: `xref … unresolved=0`), and `§L2 concurrency` / `§Push scope` are `MISSION.md` refs.

## 7. Appendix artifact preservation

```
$ grep -c '^| ' PROTOCOL-APPENDIX.compact.md     → 33   (1 header + 32 dated rows)
$ diff <(grep '^|' PROTOCOL-APPENDIX.compact.md) <(sed -n '508,541p' PROTOCOL.md)
(no output)                                      → APPENDIX_TABLE_OK
```

The live `## Appendix` section is lines 502–541; the artifact reproduces the 33 `|` lines verbatim
(no figure rewritten, no row re-ordered) and adds a title line and a 3-line preamble (pinning
convention + first-column-name rule for pointers).

## 8. Obligations deleted, merged, or restored (each with where it survives)

Nothing was deleted because it "looked unused"; `## Gate standard` is intact and grew.

1. **`## Promotion gates` minimum-bar bullets (4 boxes, source 61–69, 9 lines) — deleted.** They
   survive **verbatim box-for-box** in the seed block (`diff` empty); the coupling rule survives in the
   lead-in (line 50): “Minimum bar: the four boxes of the `SHONEN.md` seed below, rendered box-for-box
   and changeable only in the same edit as this gate text.” Census L5 green; gate `seed`
   byte-identical=yes.
2. **“…the driver's template is the contract's delivery mechanism, not a convenience summary.”** —
   rationale; the rule survives: “Round prompts embed the operative contract verbatim.” (line 71).
3. **“the driver's respawn path is unreachable while its daemon is up (step 4)”** — mechanism; R24
   survives (“recording `failed` is a ledger act, not a kill”, line 138) + appendix row
   `Liveness probes`.
4. **“This does not relax step 1 …”** — merged; the rule survives in step 1 (line 192) and in
   `## Gate standard` (“status-neutral unless the round's rules already prescribe `failed`”, line 348).
5. **“Recommended where the surface drifts outside lane control.”** — tail; the drift-pin rule
   survives (census E11).
6. **“the queue grows, so every line number moves.”** — restored (committed anchor, Fleet-2).
7. **“Waiting for all eight counters to reach `N` waits forever; that is what left rounds 2–11
   unclosed.”** — incident re-narration; survives as appendix row `Closure entries` (r10).
8. **Orphan-sweep rationale** (“a sweep freezes the on-disk bytes, placeholders and all, into a
   permanent object”) — incident re-narration; the resolution order survives verbatim (lines 96–99) +
   appendix row `Orphaned report`.
9. **Steer-era re-narration** — restored verbatim (committed anchor); the 8-lane-round figure lives in
   appendix row `Dispatch evidence`.
10. **Liveness re-narration** — probe figures survive in appendix row `Liveness probes`; the body keeps
    the rule (“Liveness probes are not evidence of an open mission …”).
11. **Header framing** — trimmed to “A **shokunin** is a domain specialist, iterated by swarm rounds
    until it can iterate itself.” (line 5); no census row or gate check depends on it.
12. **19 blank-line paragraph merges** (no words changed): adjacent paragraphs of one obligation were
    joined without a blank line (RR P1‖P2, P2‖P3, P3‖P4, P5‖P6, P6‖P7; Ev E1‖E2‖E3‖E5; the Gate
    lead-in‖`Verdict`; `rounds` append-only‖aggregator lane; `## Lifecycle` heading‖fence; Appendix
    heading‖preamble in the record).
13. **Restorations made during verification (recorded for diff honesty):** the six committed anchor
    phrases that had been trimmed; the two modal-bearing clauses (“routing is integrator work and must
    exist in an artifact”; “required template corrections are named in its report”); the only-channel
    clause; the append-only disambiguator rationale; the `"never MANIFEST.json"` example; the P18/P19
    durability-debt sentence; the `Marks:` delimiter — all restored to source wording so
    `anchors`/`modals`/`seed` pass.
14. **`2d19a64` Sibling-mint bullet (source 23–37, 15 lines) — kept complete at 16 lines** (body
    21–36): all five steps (a)–(d) and the write-scope ban, with the census's own wording restored
    inside it (the twelve predicates L8–L20 are satisfied verbatim: “any lane may mint a sibling when
    it finds a domain demand”, “records the roster map it decided against”, “plus a `MINT.md` stating
    the”, “demand instances with evidence pointers”, “self-iterates through at least three verified
    rounds”, “not as a roster row”, “it never edits `MANIFEST.json` roster or a sibling's”, “existing
    province owns”, “mint evidence”, “only after those rounds land does the operator add”, “repo + the
    new sibling's seed files”, “probation state is recorded in”, “`rounds[].notes` meanwhile”).

## 9. New obligations

| # | Where in body | Lines | Obligation |
|---|---|---|---|
| a | `## Round-robin rounds` step 4, “**History is pinned.**” + the sixth integrator write | 262 (bullet), 158 (sixth write) | `.ufo/history-pin.json` pins `sha256(rounds[0:k])` for the closed prefix plus the commit whose `MANIFEST.json` bytes hash to it; the closure gate reports `history_pin_mismatch` (closed history edited in place) and `history_pin_unanchored` (pin regenerated to bless an edit); regenerating a pin is a separate committed act named in the round notes, never a repair inside the same closure pass; appends never invalidate it. The integrator's main-repo writes **expand by exactly six**, the sixth being writing/committing that pin. |
| b | `## Gate standard`, “**Two evidences.**” | 334 | A frozen baseline's `expected.json` MUST pin the digest of every snapshot input file; the gate verifies those digests before comparing verdicts — an edited snapshot is `snapshot_tampered` (could-not-evaluate), not a compared verdict; a baseline without digests is `unpinned (legacy)`. |
| c | `## Gate standard`, “**Registry.**” | 341 | Frozen baseline names resolve under any `.ufo/waves/*/frozen` root; a bare name matching more than one root **fails closed**. |
| d | `## Fleet-2 conventions (adopted)` bullet 1 | 439 | A `SCORECARD.md` axis name not defined in `AXES.md` (`novelty`, `consistency`) is worked only if its row carries its mapping to one of the six axes `AXES.md` defines, in the same row, so a non-author can re-derive it. |
| e | `## Lifecycle`, “**Sibling mint (lane-initiated)**” (`2d19a64`) | 21–36 | Lane-initiated sibling mint: domain demand no province owns; (a) roster-map scan recorded as mint evidence; (b) `{id}-shokunin/` + `VeigaPunk/{id}-shokunin` remote seeded with SKILL.md / PROVINCE.md / SHONEN.md (canonical template) / AGENTS.md / LOG.md + `MINT.md`; (c) driver wiring (`LANE_CWD`/`LANE_MODEL`/`LANE_AXES`, operator-side, surfaced in `.ufo/l0-questions.md`) and ≥3 verified self-iterated rounds before roster rows exist; (d) only then do the operator's roster and `ROADMAP.md` rows land, probation riding `rounds[].notes`; the lane never writes outside its own repo plus the sibling's seed files and never edits the roster or a sibling's post-seed content. |

Grounding: (a)–(d) L1 spec this round; (b)(c) as above; (e) operator commit `2d19a64` plus census rows
L8–L20.

## 10. Required phrases — candidate line each matched (body)

All 29 present: `unplaceable` 12 · `dormant` 37 · `non-author verifier` 49, 382 · `byte-identical` 365 ·
`Landed means committed` 86 · `marker` 144, 145 · `progressing-weak` 132 · `lane_rounds` 239, 241 ·
`never re-keys` 241 · `unadjudicable` 244 · `supersedes` 103, 255 · `closure-correction` 230, 232 ·
`retroactive-closure` 249 · `could-not-evaluate` 319, 320 · `registry` 319, 327 · `revision` 331, 351 ·
`append-only` 91, 158 · `pathspec-limited` 75, 271 · `operator-side` 28, 80 · `durability owner` 451 ·
`erratum` 102 · `Partial entries are the norm` 203 · `Dispatch evidence` 208, 211 ·
`Termination evidence` 216 · `Liveness probes` 217, 219 · `two driver ticks` 124, 126 · `contested` 390 ·
`local-first` 289, 344 · `lane identity` 93, 421.

## 11. Limits and floor measurement

- **Single-file floor.** `PROTOCOL.compact.singlefile.md` is content-clean on seven of eight gate
  checks against the rebased toolchain; its single finding is `caps` (493 > 470), and it is
  `clean checks=8 failed=0` at `--max-lines 500`. Measured during this pass on the *pre-rebase* base:
  the same construction without the four round-13 obligations was **470 lines and gate-clean** at
  `--max-lines 470` (census 156/156, anchors 51/51, modals 125≥120, seed byte-identical, appendix
  32/32, xref 0, body-refs 1); with them it was 479 (clean at 480). The `2d19a64` Sibling-mint bullet
  (+15 source lines) and the census/anchor rebase move the single-file form to 493. Net: `≤470` is
  reachable for the pre-round-13 obligation set (19 lines better than ScoutCompaction's 489 estimate)
  and is not reachable for the live content in one file without cutting rule text; the L1 split lands
  at 459/460 for the body.
- **Column width.** Every authored body line is ≤100 columns; the sole >100 line is the `rounds`
  entry-shape line (103), byte-identical to the source. Appendix and File-contract rows are long single
  lines inherited verbatim.
- **Not exercised:** no repo-wide test/format/lint/commit (siblings edit concurrently). Programs run:
  `verify-census.sh`, `verify-protocol.sh`, `wc`, `diff`, `grep`, `awk`, plus the Python build/verify
  harness.

## 12. Rebase record (`e275d4a` 526 → `2d19a64` 541; toolchain 156→169 rows, 51→61 anchors)

- Detected via ScoutCompaction's IRC flag; re-anchored per their rule (insert = `## Lifecycle`
  Sibling-mint bullet at source 23–37; everything at or after line 29 shifts +15).
- Actions: source re-read (`wc -l` 541, md5 `444667c4…`, `git log -1` = `2d19a64`); bullet compacted and
  inserted; both artifacts rebuilt; appendix artifact re-anchored to the live appendix lines (508–541)
  and re-diffed empty; seed re-diffed empty; both censuses re-run (169/169 + 93/93); the hand
  verification set re-run.
- The census grew from 156 to 169 rows (L8–L20 = the sibling-mint obligations) between two of my runs;
  the first rebased run MISSed 7 of them (L9, L10, L12, L14, L17, L18, L19), all class (a)-looking but
  actually wording: the bullet carried the obligations while the predicates wanted the census's own
  phrasing (`it never edits `MANIFEST.json` roster…`, `self-iterates through at least three verified
  rounds`, `only after those rounds land does the operator add`, …). Fixed by restoring that wording
  verbatim and protecting each predicate from wrap splits; a first attempt failed because I had added
  `**bold**` markup *inside* predicate spans (markup breaks the literal match) — no predicate was
  weakened, and the TSV was not touched.
- The anchor file gained 10 appendix-region phrases whose own header says they are absent from the body;
  they are satisfied by `PROTOCOL-APPENDIX.compact.md` and by the record file, and are reported above as
  the appendix-scoped class, not as losses.
- Cost: body 445 → 459 (+14; 1 line under the ≤460 target after one further blank-line merge);
  single-file 479 → 493.
- Unchanged by the rebase: census results, seed bytes, appendix table bytes, the 17 `§Appendix` pointer
  names, the four round-13 obligations (lines shifted +14), the history-pin bullet.