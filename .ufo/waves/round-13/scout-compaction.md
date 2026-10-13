# scout-compaction — round-13 line-budget map for `PROTOCOL.md`

Read-only survey. **This file writes nothing into `PROTOCOL.md`**; it maps a budget, ranks cuts, names the
census ids each cut must keep alive, and states what is not cuttable. Companion draft text is carried inside
fenced `DRAFT` blocks so the compactor seat can lift it verbatim and so every proposed line count in this file
is reproducible from this file (see §8).

Baseline at survey time: `wc -l PROTOCOL.md` → **526**; `wc -c` → **49269**; body (`NR<487`) → **39401 B / 439
nonblank lines / 89.8 chars per nonblank line**. Census baseline: `sh .ufo/waves/round-11/verify-census.sh
PROTOCOL.md` → **93/93 obligations found; 0 MISSING**.

## 0. Headline findings

1. **The file is already at maximum density.** An automatic re-wrap to 100 columns over every section recovers
   **4 lines total** (Rounds −3, Fleet-2 −1, everything else ±0). Cross-paragraph *literal* duplication is
   **zero**: 0 duplicate 10-grams across the 46 body paragraphs, 8 duplicate 6-grams. So neither re-wrapping
   nor mechanical de-duplication can supply the −56.
2. **The obligation-preserving ceiling I could measure is −40 → 486 lines** (Track A, §2) on the revision it
   was measured against (`e275d4a`, 526 lines) — **501 on the live `2d19a64`** (541 lines), 500 once the new
   sibling-mint bullet is re-wrapped (§1a). 156/156 on the extended r13 census either way, from 25 candidate
   spans (23 re-drafted, 2 deletions), 3 refused at ±0. **Track A does not reach ≤470** — 16 short on the
   surveyed revision, 30 short on the live one.
3. **≤470 is reachable only by Track B**: Track A + offloading the 40-line `## Appendix` to a committed sibling
   artifact → **450 lines** surveyed / **464 live**, 156/156 (§2, §1a, §7.3) — but see §7.3a: the committed preservation gate
   (`verify-protocol.sh`) **fails such a file by construction** (appendix floors + unresolved `§Appendix`
   pointers), so Track B now needs a Main decision to extend the gate. Nothing else I could measure reaches 470
   without deleting rules.
4. **The committed census is not a sufficient acceptance test.** 392 of 526 lines (343 nonblank) match no
   census predicate at all. Deleting `## Gate standard` entirely, or the entire `## Appendix`, each leaves the
   census at **93/93**; deleting **both** yields **446 lines and 93/93** (§7.2). All seven round-12 pins' rules
   are census-blind (§7.1). A compactor graded only by "≤470 ∧ census green" has a 80-line cheat available.
5. **Wrap position is load-bearing for the census.** Predicates are line-oriented `grep -E`. My first assembly
   (plain re-wrap at 100 cols) scored **143/156** on the r13 census with no rule removed: 13 pinned phrases had
   split across a line break — 12 pure wrap artifacts and 1 genuine reword (§6 R8, §7.4). Wrapping the same text
   with the census's matched phrases held unbreakable scores **156/156 and is 5 lines shorter** (486 vs 491).
   Cheaper remedy, reproduced: verify the **unwrapped view** of the file instead — plain re-wrap then scores
   `156/156`/`93/93` on the flattened text and lands at **484 lines** (§6 R8b, §8 V8). Any compaction must
   re-run the census *after* the final wrap, on a view that tolerates wrapping.

## 1. Baseline measurements (each with its command)

| # | Measurement | Command | Observed |
|---|---|---|---|
| B1 | total lines | `wc -l < PROTOCOL.md` | `526` |
| B2 | total bytes | `wc -c < PROTOCOL.md` | `49269` |
| B3 | body bytes (`NR<487`) | `awk 'NR<487' PROTOCOL.md \| wc -c` | `39401` |
| B4 | body nonblank lines | `awk 'NR<487 && length($0)>0' PROTOCOL.md \| wc -l` | `439` |
| B5 | section map | `awk '/^## /{print NR": "$0}' PROTOCOL.md` | Lifecycle 8, Promotion 29, Round-robin 55, Evidence 306, Gate 346, File contract 386, Invariants 412, Fleet-2 465, Appendix 487 |
| B6 | body inline round-incident refs | `awk 'NR<487' PROTOCOL.md \| grep -o 'round-[0-9][0-9.]*' \| wc -l` | `4` (lines 86 `round-3`, 298 `round-2`, 329 + 338 `round-4`) |
| B7 | appendix rows | `awk 'NR>=487' PROTOCOL.md \| grep -c '^\| '` | `33` |
| B8 | census baseline | `sh .ufo/waves/round-11/verify-census.sh PROTOCOL.md \| tail -1` | `93/93 obligations found; 0 MISSING` |
| B9 | census coverage of the file | `grep -nE -f <(tail -n +2 .ufo/waves/round-11/obligation-census.tsv \| cut -f4) PROTOCOL.md \| cut -d: -f1 \| sort -un \| wc -l` | `134` lines matched by ≥1 predicate |
| B10 | census-blind mass | `526 − 134` (B1 − B9) | **392 lines blind** (343 nonblank) |
| B11 | re-wrap ceiling | auto-wrap every section's prose to 100 cols, keep tables/code/blocks | Header 0, Lifecycle 0, Promotion 0, Rounds **−3**, Evidence 0, Gate 0, FileContract 0, Invariants 0, Fleet-2 **−1**, Appendix 0 → **−4** |
| B12 | literal duplication | 10-gram shingles across the 46 body paragraphs | **0 duplicate 10-grams**; 8 duplicate 6-grams (top pair lines 289–304 ↔ 467–485, 4 shingles) |
| B13 | longest line | `awk '{print length}' PROTOCOL.md \| sort -n \| tail -1` | `691` (appendix table row 521; table rows legitimately exceed 100) |

## 1a. Revision pin and live re-base — read this before applying anything

The file moved while this map was being written (the pool commits concurrently; this seat wrote no PROTOCOL.md
byte and ran no mutating git command).

| | commit | lines | bytes | md5 | role |
|---|---|---|---|---|---|
| surveyed | `e275d4a` | **526** | 49269 | `63de15a37a42ce57decb951a7e8aa2f0` | every span number in §3/§9, every census match line in §8 V4, and Track A/B 486/450 are keyed to **this** revision |
| live | `2d19a64` | **541** | 50603 | `444667c4a69f5998f9abb957a68a4343` | current HEAD: surveyed revision **+15 lines**, inserted at 23–37 inside `## Lifecycle` — the lane-initiated **Sibling mint** bullet (`git diff --stat e275d4a..HEAD -- PROTOCOL.md` → `15 insertions(+)`) |

**Re-anchor rule: add 15 to any span whose start is ≥ 29** (the insert sits entirely after line 22 and before
`## Promotion gates`). Verified for all 25 mapped spans by first/last-6-word anchors: every shift is exactly
`+15`, with two trailing-blank edge cases (`C9a` 329–330 → content 344–344; `C2` 408–410 → content 424–425).
Lifecycle itself grew 21 → 36 lines; every other section is unchanged in length and merely shifted.

**Live arithmetic** (required saving is now 541 − 470 = **71**, not 56):

| | surveyed `e275d4a` | live `2d19a64` |
|---|---|---|
| Track A (map's 25 cuts) | **486** (−40) | **501** (−40) |
| Track A + new C26 (sibling-mint bullet, live 23–37 → 14) | n/a | **500** (−41) |
| Track B (= A + appendix offload, −36) | **450** | **464** (−77, margin 6) |
| target | 470 (−56 needed) | 470 (**−71** needed) |

**Executed on the live revision** (`541`-line file, spans re-anchored +15, C26 applied, against the **rebased
169-row** census `ce6d0ef44ab5ed66391e708b7d8aa5a0…`, 170 lines): **500 lines**, legacy census `93/93`, extended
r13 census `169/169`, on **both** the line-bounded and the unwrapped view, body round-incident refs `0`. (At
draft time the r13 census had 156 rows; it has since gained 13 rows `L8–L20` that pin the sibling-mint bullet,
so C26's draft now keeps the census's own phrasing.) Both censuses pass on the live file itself, so the 15 new
lines introduced no predicate drift — only row growth.
**Live-revision re-run after the census rebase:** `500 lines / 169/169 + 93/93` (line-bounded and unwrapped),
`0` body round-refs; before C26's phrasing was aligned the same assembly scored `163/169` with six misses
(`L10 L12 L14 L17 L18 L19`) — four wrap splits and two rewords, all in the new bullet. Verify with §8 V6/V8.

**New candidate C26 — the sibling-mint bullet (live 23–37, `## Lifecycle`).** 15 lines / 1325 B, already at
92 B/line, and **census-blind in both censuses** (deletion flips nothing) — i.e. the newest rule in the file is
also one no predicate guards. A conservative re-wrap (no rule dropped, every element (a)–(d) intact) measures
**14 lines (−1)**; its draft is in §9. Anything beyond −1 here is a rule deletion and belongs in §5's spirit:
the bullet's four steps and its two prohibitions are all load-bearing. Note it also *helps* the modal ledger:
ExecVerifier measures the live Lifecycle section at 5 normative tokens against a floor of 2 (the bullet added
+3), so cutting it would spend modal headroom as well as lines.

## 2. Proposed budget, two tracks, with arithmetic

**Coordinates and totals in this section are the surveyed revision `e275d4a` (526 lines); §1a rebases them onto
the live `2d19a64` (541 lines, Track A 501 → 500 with C26, Track B 464, required saving 71).**

Wrapping rule behind every number below: **predicate-aware wrapping** — the literal matched phrases of the
census (156 rows) are held unbreakable while wrapping, then restored, so the result is green on *both* the
line-bounded and the unwrapped census views. Plain re-wrapping runs 2 lines shorter (484 vs 486 for the same
cuts) but splits 11 pinned phrases on the line-bounded view; it is equally acceptable if the gate verifies the
unwrapped view instead (§6 R8, §8 V7/V8). Either way the reachability conclusion is unchanged: Track A stays
over 470 (486 masked / 484 plain) and Track B stays under it (450 masked / 448 plain).

### 2.1 Per-section table

| Section | Lines | Track A proposed | mechanism | Track B proposed | mechanism added |
|---|---|---|---|---|---|
| Header | 7 | **7** | untouched | 7 | — |
| Lifecycle | 21 | **21** | untouched (no cut measured) | 21 | — |
| Promotion | 26 | **22** | class-(b) merge: minimum bar folded to one gloss (C1) | 22 | — |
| Rounds | 251 | **228** | class (a)+(c): 16 candidates, §3 | 228 | — |
| Evidence | 40 | **36** | class-(a) lead-in deletion (C9a) + bullet re-wrap (C9b) | 36 | — |
| Gate | 40 | **40** | untouched (C10 re-wraps to the same 6 lines) | 40 | — |
| FileContract | 26 | **23** | class-(b) delete: second "Marks:" restatement (C2) | 23 | — |
| Invariants | 53 | **49** | class-(c): restatement deletions (C3, C11) | 49 | — |
| Fleet2 | 22 | **20** | re-wrap (C13) | 20 | — |
| Appendix | 40 | **40** | untouched in Track A / moved to a committed sibling in Track B | 4 | move-to-sibling: 2-line pointer paragraph (§7.3) |
| **Total** | **526** | **486** | | **450** | |

Arithmetic, Track A: `7+21+22+228+36+40+23+49+20+40 = 486` → **saved 40**; executed as:
apply §9’s 21 draft blocks (−35), delete 408–410 (`C2`, −3) and 329–330 (`C9a`, −2), run the census →
**486 lines, 156/156, exit 0**.

Arithmetic, Track B: `7+21+22+228+36+40+23+49+20+4 = 450` → **saved 76**, i.e. **≤470 with 20 lines of margin**.
Appendix line recovery in Track B: `40 − 4 = 36`.

### 2.2 Read this before using the table

* **Track A is the measured floor for an in-file compaction that keeps every rule and every rationale
  pointer.** 486 > 470 by 16 lines. A compactor who hits 470 in Track A has deleted rules, not prose —
  §5 lists the 16 census-invisible spans where that happens silently.
* **Track B is the only ≤470 route I could measure that keeps every rule** (offload the appendix, §7.3); it is not
  free: 20 in-body `§Appendix` pointers must be rewritten in the same edit.
* Span counts are `awk`-reproducible (§8 V1); proposed counts are the §9 blocks’ own line counts (§8 V3).

## 3. Ranked cut list

Ordered by measured lines saved. `first 6` / `last 6` quote each span so it stays findable after renumbering.
"legacy flips" = ids of the round-11 census (93 rows) that go MISS if the span is deleted verbatim today, with the
line where the predicate currently matches (§8 V4). "blind" = none — the argument for that cut is semantic only.
The extended r13 census adds rows on many of these spans; §6 R8 and §7.4 say what that means for a cut. Which
spans the new rows sit on (computed by matching every r13 `G*`/`P*`/`V6–V11`/`R52` predicate inside each span):
`C4` → P15–P21, P29; `C7` → P22, P23; `C16` → P24, P25; `C22` → P11–P14; `C10` → G21–G24, G35, G36; `C13` →
V6–V11; `C5` → R52 (its `expand by exactly five`). The other 17 spans carry **no** new row, so on those the
extended census is exactly as blind as the legacy one and §5 is the only guard.

| # | id | Span | first 6 words | last 6 words | what it is | cur → new | Δ | class | legacy flips |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **C1** | 41–48 | `- `SKILL.md` contains at least one` | `matches reality: no absorbed cross-domain work.` | promotion minimum bar | 8 → 4 | **-4** | b | blind |
| 2 | **C14** | 113–129 | `Every dispatched lane writes a report` | `heading in the next round's report.` | report path + minimum content | 17 → 14 | **-3** | re-wrap | R15@115, R16@119, R17@127, R18@118 |
| 3 | **C16** | 233–252 | `- **Dispatch evidence** is the `.ufo/watchdog.log`` | `the pointer that resolves at closure.` | dispatch/completion/termination evidence | 20 → 17 | **-3** | a | R41@250 |
| 4 | **C2** | 408–410 | `Marks: `[~]` asserted by the lane` | `named non-author verifier per **Promotion gates**.` | File-contract "Marks:" restatement | 3 → 0 | **-3** | b | blind |
| 5 | **C3** | 424–439 | `- `MANIFEST.json` is canonical for rank` | `work named in the round notes.` | Invariants write-scope bullet | 16 → 13 | **-3** | c | I4@424, I5@427, I5@430, I7@439 |
| 6 | **C4** | 89–111 | `A lane report **lands last** —` | `the filed bytes, labelled or silent.` | "lands last" paragraph | 23 → 21 | **-2** | a+dedupe | R10@89, R11@93, R12@94, R13@95, R14@96 |
| 7 | **C7** | 131–151 | `A lane whose mission has terminated` | `in this section terminates live work.` | stale-lane / failed / actuator | 21 → 19 | **-2** | a | R19@132, R20@134, R20@138, R22@142, R23@147, R24@149 |
| 8 | **C5** | 170–186 | `**Integrator of record.** The integrator this` | `reader can re-execute is an opinion.` | **Integrator of record.** | 17 → 15 | **-2** | c | R30@170, R31@173, R32@181 |
| 9 | **C12** | 220–226 | `4. Appends one entry to `MANIFEST.json`'s` | `optional. Semantics under a per-lane-counter driver:` | step-4 entry shape | 7 → 5 | **-2** | re-wrap | blind |
| 10 | **C9a** | 329–330 | `Sharpened by the round-4 audit (§Appendix,` | `the round-4 audit (§Appendix, "Evidence standard"):` | "Sharpened by the round-4 audit" lead-in | 2 → 0 | **-2** | a | blind |
| 11 | **C9b** | 331–344 | `- **Claimed ≠ re-executed.** A command` | `the surface drifts outside lane control.` | evidence bullets | 14 → 12 | **-2** | re-wrap | E8@333, E9@336, E10@338, E11@341 |
| 12 | **C13** | 467–485 | `- Expertise axes live in `AXES.md`;` | `owns the path (§Appendix, "L0 durability").` | Fleet-2 bullets | 19 → 17 | **-2** | re-wrap | V1@470, V2@470, V3@473 |
| 13 | **C23** | 61–69 | `Rounds are driven externally (a scheduler/steer` | `mission does not grandfather superseded rules.` | driven-externally + snapshot | 9 → 8 | **-1** | re-wrap | R2@62, R3@64, R4@67, R5@68 |
| 14 | **C24** | 84–87 | `Rounds are per-lane counters, not a` | ``<N>` per lane, not per fleet.` | per-lane counters | 4 → 3 | **-1** | a | R9@84 |
| 15 | **C17** | 159–168 | `A file at the report path` | `a real report stay status-neutral defects.` | marker vs report | 10 → 9 | **-1** | dedupe | R27@159, R28@165, R29@166 |
| 16 | **C8** | 188–194 | `A round is **completed** when every` | `(step 4). After closing, the integrator:` | round completion | 7 → 6 | **-1** | a | R33@188 |
| 17 | **C19** | 205–216 | `2. Lands warranted protocol improvements in` | `outlive the round that routed them.` | step 2 routing | 12 → 11 | **-1** | a | blind |
| 18 | **C20** | 227–232 | `- **Partial entries are the norm.**` | `is what left rounds 2–11 unclosed.` | partial entries | 6 → 5 | **-1** | a | blind |
| 19 | **C21** | 253–260 | `- **`in-flight` is debt, not a` | `stays debt until the mission terminates.` | in-flight debt | 8 → 7 | **-1** | re-wrap | blind |
| 20 | **C22** | 264–273 | `- **A row names the lane-round` | `rows carry their pointer in `notes`.` | row identity | 10 → 9 | **-1** | re-wrap | blind |
| 21 | **C6** | 289–304 | `The **aggregator** lane is a main-repo` | `the routed-defect queue empty by construction.` | aggregator lane | 16 → 15 | **-1** | a+dedupe | R47@294, R48@296, R49@298, R50@300, R51@303 |
| 22 | **C11** | 442–452 | `- Local-first: repos live locally; **domain-facing` | `in-flight edits and integrator working-tree changes.` | local-first bullet | 11 → 10 | **-1** | a | I9@449, I10@451 |
| 23 | **C15** | 153–157 | `A respawned mission inherits its predecessor's` | `them for the aggregator to resolve.` | respawn inheritance (refused) | 5 → 5 | **+0** | — | R25@153 |
| 24 | **C18** | 196–204 | `1. Reads every lane report and` | `the round's rules already prescribe `failed`.` | step 1 (refused) | 9 → 9 | **+0** | — | R6@200 |
| 25 | **C10** | 375–380 | `- **Closure consequence.** A red gate` | `and write scope are the lane's.` | gate closure consequence | 6 → 6 | **+0** | re-wrap | blind |

Sum of Δ: `4+3+3+3+3+2+2+2+2+2+2+2+1+1+1+1+1+1+1+1+1+1 = 40`.
**Refused (measured ±0 — the prose is already at its rule minimum): `C15` 153–157, `C18` 196–204, `C10` 375–380.**

### 3.1 What each cut carries, and where the obligation survives

Draft text for every row is the canonical marked block **`§9 DRAFT <id>`** — this section keeps no duplicate copy.

| id | obligation carried | survives where | census risk (§6) |
|---|---|---|---|
| **C1** | promotion minimum bar | same gate, compressed; canonical wording stays in the `SHONEN.md` seed (400–407); the dropped example list and `no absorbed cross-domain work` gloss are illustrations, not rules | low (legacy-blind; r13 rows may still sit on it) |
| **C14** | R15–R18 (report path, minimum content, SHONEN heading) | same paragraph + bullets; SHONEN-heading consequence tightened | high — `R15`@115, `R16`@119, `R17`@127, `R18`@118 |
| **C16** | R39–R41 | same bullet; the steer-era narrated figure deleted (appendix row carries it) | high — `R41`@250 |
| **C2** | L4 marks rule | Promotion gates 36–39 + File-contract row 393 | low (legacy-blind; r13 rows may still sit on it) |
| **C3** | I4/I5/I6/I7 | same bullet; C5/C7 carry report-path and evidence text; appendix carries the `609ecb6` figure (I7 must stay one line) | high — `I4`@424, `I5`@427, `I5`@430, `I7`@439 |
| **C4** | R10–R14 + orphan order + errata | same paragraph; three rationale clauses deleted, each carried by an appendix row (Lands last r9/r10, Orphaned report r12) | high — `R10`@89, `R11`@93, `R12`@94, `R13`@95, `R14`@96 |
| **C7** | R19–R24 | same paragraph; the "context predates landed changes" rationale deleted (§Appendix pointer kept) | high — `R19`@132, `R20`@134, `R20`@138, `R22`@142, `R23`@147, `R24`@149 |
| **C5** | R30–R32 | same paragraph; "only guaranteed delivery channel" rationale + trailing opinion clause deleted | high — `R30`@170, `R31`@173, `R32`@181 |
| **C12** | R37 | same text, re-wrapped (three lines were wrapped short) | low (legacy-blind; r13 rows may still sit on it) |
| **C9a** | none of its own (incident citation) | the bullets after it keep E7–E11; appendix row "Evidence standard" carries the audit | low (legacy-blind; r13 rows may still sit on it) |
| **C9b** | E7–E11 | unchanged text, re-wrapped | high — `E8`@333, `E9`@336, `E10`@338, `E11`@341 |
| **C13** | V1–V3 | same bullets, re-wrapped | high — `V1`@470, `V2`@470, `V3`@473 |
| **C23** | R2/R3/R4/R5 | same two paragraphs, one blank line removed | high — `R2`@62, `R3`@64, `R4`@67, `R5`@68 |
| **C24** | R9 per-lane counters | same sentence, minus the `round-3` illustration | high — `R9`@84 |
| **C17** | R27–R29 | same paragraph; the sentence restated immediately after it deleted | high — `R27`@159, `R28`@165, `R29`@166 |
| **C8** | R33 | same paragraph; the `rounds 2–11` incident clause deleted, `§Appendix` pointer kept | high — `R33`@188 |
| **C19** | R35 | same paragraph; `since defects outlive the round that routed them` deleted | low (legacy-blind; r13 rows may still sit on it) |
| **C20** | R38 | same bullet; `that is what left rounds 2–11 unclosed` deleted | low (legacy-blind; r13 rows may still sit on it) |
| **C21** | R42 | same bullet, re-wrapped | low (legacy-blind; r13 rows may still sit on it) |
| **C22** | R44 | same bullet, re-wrapped | low (legacy-blind; r13 rows may still sit on it) |
| **C6** | R47–R51 | same paragraph; the `round-2/AGGREGATE.md` example + trailing construction clause deleted | high — `R47`@294, `R48`@296, `R49`@298, `R50`@300, `R51`@303 |
| **C11** | I9/I10 + push scope | same bullet; the `235b414` provenance tag and one example trimmed | high — `I9`@449, `I10`@451 |
| **C15** | R25/R26 | unchanged text | high — `R25`@153 |
| **C18** | R6/R34 | unchanged text | high — `R6`@200 |
| **C10** | Gate closure consequence | same bullet, re-wrapped (same 6 lines) | low (legacy-blind; r13 rows may still sit on it) |

## 4. The three duplication classes, quantified

### 4.1 (a) Body prose narrating an incident the `## Appendix` already carries

Sweep: `grep -n` each appendix-carried figure in the body and in the appendix (`NR<487` vs `NR>=487`).
Ten spans were found: **eight** are recoverable (rows 1, 2, 3, 5, 6, 7, 8, 10 below; ~5–7 lines, most of them
shared with the candidates in §3, not additive to them) and **two** are kept on purpose (rows 4 and 9). This
class is real but is *not* the source of the −56:

| Body span | Narrated figure | Appendix row carrying it | Recovered in |
|---|---|---|---|
| 191 | `waiting for it is what left rounds 2–11 without a closure entry` | Closure entries (r10) | C8 (−1) |
| 231–232 | `that is what left rounds 2–11 unclosed.` | Closure entries (r10) | C20 (−1) |
| 236 | `the earliest rounds had no prompt files at all, so a prompt-only test misreads real lane-rounds as undispatched` | Dispatch evidence (r1–3) | C16 (−1) |
| 277 | `for rounds before fleet-2 (`609ecb6`)` | Retroactive typing (r10) | kept (C22) — the fleet-2 tag is a rule's boundary |
| 329 | `Sharpened by the round-4 audit` | Evidence standard (r9, r4) | C9a (−2) |
| 338 | `git rev-parse round-4` fails wherever the tag doesn't exist` | Evidence standard (r9, r4) | C9b (cut inside its −0) |
| 437 | `tracked since `609ecb6` although this clause once said they stay untracked` | Tracked runtime (r10) | C3 (−1 of its −3) |
| 444 | `(operator rule, landed in `235b414` 2026-09-28)` | not in the appendix (r13 provenance) | C11 (−1 of its −1) |
| 243 | `ufo-sighting status --lite` still lists a mission after the driver `complete`d it` | Liveness probes (r10) | kept — the probe is named in the rule, not narrated |
| 298 | `(e.g. `round-2/AGGREGATE.md`)` | Ledger (r10) | C6 (−1 of its −1) |

### 4.2 (b) Promotion-gate minimum bar vs the canonical `SHONEN.md` seed

Measured: bar = lines 41–48, **8 lines / 531 B, 72 words**; seed = lines 400–407, **8 lines, 58 words**;
"Marks:" restatement = lines 409–410, **2 lines / 139 B, 20 words**. Token-set Jaccard: bar↔seed **0.222**,
bar↔Marks **0.015**, Promotion 34–40 ↔ Marks **0.167**. The bar and the seed are the same four claims in
different words, and the file *says so*: "Minimum bar (rendered box-for-box by the `SHONEN.md` seed below; the
two change only in the same edit)".

| Seed box (400–407) | Bar sub-bullet (41–48) | What only the bar adds |
|---|---|---|
| `SKILL.md` contains real decision tables, error patterns, checklists, cited sources | 41–43 "at least one decision table, one error-pattern list, and one checklist, each citing a resolvable source" | cardinality (≥1 each), resolvability of the source |
| At least one end-to-end domain task executed and logged in LOG.md | 44–45 "at least one end-to-end domain task: trigger → action → outcome → evidence pointer" | the log shape + pointer |
| Instructions executable by an agent without oral context | 46–47 "an agent with no oral context can execute … self-contained, pointers resolvable" | self-containment test |
| No cross-domain bleed (PROVINCE.md still accurate) | 48 "`PROVINCE.md` still matches reality: no absorbed cross-domain work" | nothing material |

Achievable merge: **C1 −4 + C2 −3 = −7** (fold the bar into one 4-line gloss that keeps the three added
specifics, and delete the second "Marks:" restatement, which duplicates both line 393 and lines 36–39).
Neither cut flips a census id — **both are blind**, so the census cannot police how the compactor does this.
The bar's *content* is on the do-not-cut list (§5 item 1): the census-invisible rule "SKILL.md must contain at
least one decision table, one error-pattern list, and one checklist, each with a resolvable source" is the
`shonen → shokunin` gate.

### 4.3 (c) Invariants write-scope bullet vs `**Integrator of record.**`

Measured: `**Integrator of record.**` = lines 170–186, **17 lines / 1566 B / 115 words**; Invariants write-scope
bullet = lines 424–439, **16 lines / 1567 B / 84 words**; token-set Jaccard **0.16** with 16 shared content
tokens (`manifest.json rounds scripts/ corrections edits inside integrator lane main-repo notes operator-side own
protocol remain round writes`). Both enumerate the main-repo write set and both state the integrator's
`rounds`-append licence; the bullet additionally repeats "the protocol lane holds the protocol/roadmap/report
writes and, as integrator-of-record, `MANIFEST.json` `rounds` appends", which line 173 already says as
`expand by exactly five`. Achievable: **C3 −3 + C5 −2 = −5**. Keep the enumeration in `## Invariants` (I4/I5
predicates live there and it is the invariant's home) and let `**Integrator of record.**` keep the five
expansions (R31 lives there). Neither deletion silently changes scope *if and only if* both are edited as a pair
— see §6 R3.

## 5. Do-not-cut list (census is necessary, not sufficient)

Each span below was deleted in memory and the census re-run: every one stays **93/93**, i.e. the census cannot
see the loss. Ordered by how much a compactor would be tempted. (Spans 3 show a MISS and are listed as *covered*
counter-examples, to show which of my candidates the census does police.)

1. **Lines 41–48 + 398 + 400–407 — the minimum bar and the canonical seed.** Deleting 400–407 (the seed block
   itself) leaves 93/93 (observed: `518 lines; 93/93`), yet F4's predicate `seed .verbatim` lives at 398 while
   the artifact it mandates is the block. Deleting 41–48 leaves 93/93 too (observed). Losing either destroys the
   promotion gate's only executable definition.
2. **Line 393 — the `SHONEN.md` row's mechanical-verification tail** (`the seed block (indented lines below) must
   diff byte-identical modulo `<name>` … marks are confined to the box character plus one indented evidence line
   per box … no other prose, added boxes, or removed boxes`). Deleted alone: 93/93 (observed). This is the only
   place the seed's *diff* verification and the marks-confinement rule are stated.
3. **Line 36 — `a subagent the lane dispatched is still the lane.`** Deleted alone: 93/93 (observed). Without it,
   a lane can route its self-attestation through a subagent and still call it non-author review: the gate's
   R4/L4 protection is defeated while `non-author verifier` (line 39) still matches.
4. **Line 316 — `a documented negative result at that gate still counts.`** Deleted alone: 93/93 (observed). It
   is what keeps an operator-owned handoff's *refusal* a valid end-to-end outcome (E2).
5. **Lines 143–145 — `progressing-weak` third grade** (`sibling-authored activity alone is a third grade,
   progressing-weak: named as such in the row, never called progressing, and never silent or failed on its own`).
   Deleted: 93/93 (observed). Round-12 pin (appendix row "Stale-lane actuator" r12) — the r12 kotoba-r13 defect;
   R21's `progressing` still matches line 140, so the census cannot tell the grade was removed.
6. **Lines 246–248 — `uncommitted file at the report path does not end `in-flight``.** Deleted: 93/93 (observed).
   Round-12 pin ("Unlanded report" r12, the kagi-r12 13620 B draft); R40 matches elsewhere.
7. **Lines 99–101 and 101–106 — `A swept report is still landed` / orphan-resolution order + the aggregator
   `corpus/` carve-out.** Deleted: 93/93 (both, observed). Round-12 pin ("Orphaned report" r12, the `LANE_HASH`
   placeholder freeze). Losing it turns a two-step resolution order into an unbounded integrator sweep.
8. **Lines 268–271 — `reading the map as the key erases in-flight debt and manufactures rows …`.** Deleted:
   93/93 (observed). Round-12 pin ("Row identity" r12); R44's `lane_rounds` matches 265/267/270.
9. **Lines 481–485 — L0 durability tail** (`Cite a question by lane + round + its opening words, never by line
   number: the queue grows, so every line number moves.`). Deleted: 93/93 (observed). Round-12 pin ("L0
   durability" r12, the uncommitted l0 questions and the kake-r14 in-place rewrite).
10. **Lines 352–366 — Gate §Verdict `could-not-evaluate` map, §Self-test's `a helper-only or model-only
    self-check does not satisfy this clause`, §Two evidences' frozen-run and revision-naming.** Deleted
    separately: 93/93 each (observed). **The span inside this blind region that I drafted (C10, `gate redness is never the marker predicate` sentence) measured ±0 and is on the
    refused list** — do not buy lines here; nothing in §3 deletes a Gate-standard rule.
11. **Lines 381–384 — Gate §Delivery** (`This section reaches a lane through the re-read duty, not the driver's
    prompt template … closure grades no gate conformant until its registry row exists in the lane's own
    `SKILL.md``). Deleted: 93/93 (observed). It is the only statement of how the Gate standard reaches lanes.
12. **Lines 424–433 — `the two main-repo lanes (`protocol`, `aggregator`) additionally keep `SCORECARD.md` and
    `LOG.md` at the main-repo root`** (and the `AXES.md` per-repo justification). Deleted: 93/93 (observed).
    Deletes the main-repo lanes' licence to keep root-level SCORECARD/LOG.
13. **Lines 444–445 — `domain source trees are read-only and upstream-bound work is carried in the round
    report`.** Deleted: 93/93 (observed). The only statement that domain source trees are read-only.
14. **Lines 25–26 — `rounds the lane was not dispatched do not count against it`.** *Covered:* deleting it flips
    **L2** (observed `92/93 MISS=['L2']`) — a worked example of a predicate that does police a semantic clause.
15. **Lines 145–148 — `commit sparsity is not silence`.** *Covered:* deleting flips **R23** (observed
    `92/93 MISS=['R23']`).
16. **Lines 298–299 — `a superseded snapshot elsewhere is relocated there by its next refresh — superseded, not
    voided`.** *Covered:* deleting flips **R49** (observed `92/93 MISS=['R49']`).

## 6. Residual risk — what a compactor following this map could still break

* **R1 — wrap position decides predicate hits (observed 13 times).** Plain re-wrap at 100 cols made **I7** MISS
  on the legacy census (`pathspec-limited` / `commits` split) and **13 rows** MISS on the r13 census (§7.4).
  Any follow-on must wrap with the matched phrases unbreakable (or merge the split pair afterwards) and re-run
  the census *after* the final wrap.
* **R2 — Track A arithmetic does not reach the target, and it is a cut list, not a floor.** 486 > 470 by 16 on
  the surveyed revision (501/500 live). See §7.6: a broader rule-preserving search reached 459 body + 40
  appendix artifact on the live base, so treat §3 as one worked cut set, not as the minimum. If the work is
  graded on line count alone, the compactor will start eating §5 spans; the *legacy* census will not object
  (B10: 392 blind lines), and the extended census only objects where a new row happens to sit.
* **R3 — editing one side of a class-(b)/(c) pair.** The bar↔seed pair and the Invariants↔Integrator pair are
  each "keep both or edit both". Cutting §4.3's Invariants enumeration while leaving line 173's "expand by
  exactly five" makes the five expansions unverifiable; cutting line 173 while keeping the enumeration makes the
  closure gate's own write scope unstated. My map pairs them (C3+C5); an unpaired edit is silent scope loss.
* **R4 — `lane_rounds` / `rounds` / `closed_at` inside code spans.** The step-4 block quotes JSON
  (`{"round": N, "type": "closure-correction", …}`) and `lane_rounds: {<id>: <n>}`. Re-wrapping inside a backtick
  span changes the JSON's rendering; the census matches on the *words*, so it will not notice.
* **R5 — appendix-row deletion vs pointer rewriting.** If Track B is chosen, all 20 in-body `§Appendix, "X"`
  pointers must be rewritten to name the new artifact in the same edit, and the new path must be committed in the
  same round commit (I6: "an untracked prompt is non-durable dispatch evidence" — same principle). A dangling
  `§Appendix, "X"` is worse than a long file: the rule keeps its text and loses its rationale.
* **R6 — the census id I4/I5/I7 trio must not be split across the bullet's two halves.** C3's replacement moved
  the `609ecb6` figure out; the tracked-runtime *rule* must stay attached to a `§Appendix, "Tracked runtime"`
  pointer, otherwise I7's enforcement sentence reads as an assertion with no rationale.
* **R7 — date/figures.** I deliberately did **not** propose touching any figure inside the appendix rows (B13:
  rows run to 691 chars; the appendix's own rule is "figures verbatim … never live values"). A compactor who
  "shortens" rows to buy lines breaks the digest's contract and the 20 pointers that rely on it.
* **R8 — the extended census keys on wording, so rewording a pinned clause is a MISS even when the obligation
  survives.** My first assembly (plain re-wrap) scored **143/156**: `G22 G23 G24 G35 P16 P19 P20 P22 P23 P29 V6
  V9 V10` — 12 pure wrap artifacts (`the integrator sweeps it`; `re-grades it failed for want of a landed report
  if the successor never lands it`; `sibling-authored activity alone is a third grade, progressing-weak: named as
  such`; `appends a new line naming the superseded one`; `never by line number`; `integrator, which commits it
  with the round's integration commit`; `The integrator verifies a gate's committed evidence`; `it does not
  execute a sibling's gate`; `never the marker predicate`; …) and 1 genuine reword (`gate redness is`, which my
  C10 draft had paraphrased away). Fix: hold the census's matched phrases unbreakable while wrapping — same
  text, **486 instead of 491 lines, 156/156**. A cut that must *reword* a pinned clause is gate-integration work
  (new or amended row), reported, never a silent downgrade.
* **R8b — the cheaper remedy for the same hazard: verify the unwrapped view.** `ScoutCensus` showed (and I
  reproduced on my own variants) that flattening each paragraph before grepping removes the hazard without
  touching the wrapper: `awk 'BEGIN{RS=""; ORS="\n\n"} {gsub(/\n[ \t]*/," "); gsub(/[ \t]+/," "); print}'`
  then point `verify-census.sh` at the flattened file. Observed on my plain-re-wrapped Track A assembly
  (**484 lines**): line-bounded **145/156** (`G23 G24 P16 P19 P20 P22 P23 P29 V6 V9 V10` MISS), unwrapped
  **156/156** and legacy **93/93** — i.e. every line-bounded MISS was an artifact and no obligation moved. The
  legacy 93 rows are line-fragile too (ScoutCensus measured 10 legacy MISSes on their plain re-wrap). The
  false-MISS *count* is implementation-dependent — they measure 41 extended + 10 legacy at 72 columns over the
  whole file, I measure 11 extended + 0 legacy at 100 columns over my cut set — which is exactly why the
  criterion is "the unwrapped view agrees", never "the MISS count is low". Reading
  rule: a MISS on the unwrapped view is real; a MISS only on the line-bounded view of a file that passes
  unwrapped is a wrap artifact. Caveat from that seat, re-run on their witnesses: unwrapping can join
  non-adjacent clauses, so keep a handful of line-bounded witnesses rather than retiring the line-bounded
  view entirely. **The unwrapped view is the re-wrap-invariant check; masking is only an extra guarantee.**
  Two masking caveats, both observed by ScoutCensus and worth having: (i) a masker must protect the *union* of
  every predicate-match span in a paragraph — taking only the longest of overlapping matches scored `155/156`
  because it split `G37` (`second inventory; a fleet index is pointers`, which overlaps `G17`); (ii) masked
  text pins where lines may break, so a later one-line edit can re-break a phrase and flip the line-bounded
  view red again — re-run V7/V8 after any such edit. My §9 blocks satisfy both views, which is why they are the
  canonical drafts.

## 7. Gate integrity: what this survey says about the census itself

### 7.1 All seven round-12 pins are census-blind

Round column command: `awk 'NR>=487' PROTOCOL.md | grep -cE '^\| .*\$$| [0-9, ]*12[0-9, ]*\|'` → **7 rows whose
Round column contains 12** (Gate standard ×2, Row identity, Orphaned report, L0 durability, Stale-lane actuator,
Unlanded report). Each pin's rule text was deleted in memory and the census re-run:

| Pin (appendix row) | Rule text tested | Census after deletion |
|---|---|---|
| Gate standard (r10, r12) | 357–361 registry + self-test depth | **93/93 — blind** |
| Gate standard (r12) | 362–366 two evidences / revision naming | **93/93 — blind** |
| Row identity (r12) | 268–271 `lane_rounds`-as-key erasure | **93/93 — blind** |
| Orphaned report (r12) | 101–106 resolution order | **93/93 — blind** |
| L0 durability (r12) | 481–485 queue grows, cite by words | **93/93 — blind** |
| Stale-lane actuator (r12) | 143–145 `progressing-weak` | **93/93 — blind** |
| Unlanded report (r12) | 246–248 uncommitted ≠ `in-flight` end | **93/93 — blind** |

So the round-13 mandate to extend the census to "the seven round-12 pins plus `## Gate standard`" is not
belt-and-braces: **at survey time the census had zero coverage of every one of them**, and zero rows whose
`section` column names the Gate standard.

**Status update (cross-seat, observed): the extension landed while I was writing.** `ScoutCensus` reports
`.ufo/waves/round-13/obligation-census-r13.tsv` (157 lines = the 93 legacy rows byte-identical + 63 new: G1–G37
`## Gate standard`, P11–P29 the seven pins, V6–V11 Fleet-2/L0, R52 the write-scope numeral), green at
**156/156** via `sh .ufo/waves/round-11/verify-census.sh PROTOCOL.md .ufo/waves/round-13/obligation-census-r13.tsv`
(legacy default still 93/93), and every span in the table above now carries ≥1 row, so those deletions MISS.
Consequence for this map: **§7.2's cheat is closed against the extended census** (the 80-line deletion now fails),
and §3's "blind" column describes the *legacy* predicate set only — a cut marked blind may still be caught by a
new G*/P*/R52 row. Caveat from that seat, which I endorse: its predicates key on pre-existing wording, so a cut
that legitimately rewords a pinned clause MISSes even though the obligation survives.

### 7.2 The cheat, demonstrated

* delete `## Gate standard` (346–385): `486 lines`, census **93/93**, MISS `[]`.
* delete `## Appendix` (487–526): `486 lines`, census **93/93**, MISS `[]`.
* delete **both**: `446 lines`, census **93/93**, MISS `[]` — i.e. **≤470 with 24 lines to spare**, bought by
  deleting the exact two sections round 13 exists to protect.

### 7.3a The committed gate's verdict on a digest-less target (measured)

`sh .ufo/waves/round-13/verify-protocol.sh .ufo/waves/round-13/PROTOCOL.compact.md --max-lines 470` (the live
compactor's draft, md5 `6ac3aae59a5edfc3e5bf9e3bf4bfc9fd`, 445 lines), observed:

```
INFO caps .ufo/waves/round-13/PROTOCOL.compact.md lines=445/470 body-refs=1/4 (appendix heading at line 441)
INFO appendix .ufo/waves/round-13/PROTOCOL.compact.md rows=0/32 body-pointers=17
FAIL modals section '## Appendix' normative tokens 0 < floor 15
FAIL appendix appendix data rows 0 < floor 32
FAIL appendix body pointer (§Appendix, "…") resolves to no row      ×17
verify-protocol: findings checks=8 failed=2
```

So the gate enforces, on the **target file**, that `## Appendix` carries ≥15 normative tokens and ≥32 data
rows, and that every body `§Appendix, "X"` pointer resolves to a row. Track B removes exactly that, so as
committed the gate fails a digest-less file by construction — Track B is not free, it was *blocked* pending a
gate change. `PROTOCOL.md` itself has 20 `§Appendix, "` pointers; the draft carries 19, and the gate reports 17
unresolved body pointers — pointer survival is itself a gradeable quantity, and a compactor should keep the
count monotone.

**Status update (ExecVerifier, observed): the gate change is happening — and the gate was never line-pinned.**
`sh .ufo/waves/round-13/verify-protocol.sh PROTOCOL.md --max-lines 541` on live HEAD → `clean checks=8
failed=0`, exit 0; the gate resolves the `## Appendix` heading, the seed-block header and every section slice
dynamically and `caps` counts whatever revision it is handed, so **no rebase is needed for the checks** (only
for prose citations, which that seat pins per revision). Two consequences for Track B: (i) `--appendix FILE`
two-file mode is being added per Main's adaptation, which is the mechanism that lets the digest live outside
the target; (ii) in that mode the digest artifact must carry an **H2** `## Appendix … incident digest …`
heading — today's `PROTOCOL-APPENDIX.compact.md` carries an H1 (`# PROTOCOL-APPENDIX.md — incident digest …`)
and trips the `structure` check. Keep the modal floors in mind: measured per-section counts on live are
5,3,57,10,10,8,11,4,15 against committed floors 2,3,57,10,10,8,11,4,15 (measured-sum 123 ≥ floor-sum 120) —
adding text cannot trip a floor, only losing it can.

### 7.5 QA of the live draft against this map's do-not-cut list

Against `.ufo/waves/round-13/PROTOCOL.compact.md` (md5 `6ac3aae59a5edfc3e5bf9e3bf4bfc9fd`, 445 lines), all
**16** §5 spans are retained — verified on the **unwrapped view** (the line-bounded view produced 2 false
negatives of its own: `erases in-flight debt` @227–229 and `superseded, not voided` @261, the latter reworded
to `superseded and not voided`, same rule). The draft is therefore not (yet) paying for its 41-line head start
with a §5 rule; its two gate FAILs are the Appendix-class failures of §7.3a, nothing else. Reading rule from
§6 R8b applies to *this* check too: line-bounded substring tests on a re-wrapped file lie in both directions.
The census has since been rebased (169 rows / 170 lines, `ce6d0ef4…`): the sibling-mint bullet is now pinned
by `L8–L20` (deleting live 23–37 → `156/169`), and that seat's one standing hole `P17` moved to live lines
120–121 (was 105–106). Re-pin the census digest before grading; a census file mid-edit, or a row set built from
a different revision, is a could-not-evaluate state, not a verdict.

### 7.3 Track B's design and cost

Move the appendix's 33 rows verbatim into a committed sibling artifact (candidate path:
`.ufo/waves/round-13/incident-digest.md`, or a stable `CORPUS.md`-adjacent path — the lane should pick one and
commit it in the same round commit), leave a 4-line section in `PROTOCOL.md` (`## Appendix — incident digest` +
2-line pointer paragraph), and rewrite the body's `§Appendix, "X"` pointers to name that path. Cost: the file
stops being self-contained for rationale (it says "why these rules exist" in place); benefit: −36 lines with no
rule touched, and the digest becomes its own artifact with its own evidence chain. Prerequisite: the census
extension should pin the digest's path so the pointer target is itself checked.

### 7.4 The extended census against this map (re-executed)

* legacy census (93 rows) on the assembled Track A text: **93/93**, exit 0.
* extended census (156 rows): **156/156**, exit 0 — but only after the unbreakable-phrase wrap (§6 R8). With
  plain re-wrapping the same cuts score **143/156**; the 13 MISSes are `G22 G23 G24 G35 P16 P19 P20 P22 P23 P29
  V6 V9 V10`, and 12 of them are pure line-break artifacts.
* consequence for reading §3: the "legacy flips" column is the *legacy* predicate set. The r13 rows sit on many
  of the same spans, so a cut marked "blind" there is still checked by the extended census — verify with V6, not
  with the table.
* both views, executed: masked assembly (486 lines) **line-bounded 156/156 + 93/93** and **unwrapped 156/156 +
  93/93**; plain re-wrap (484 lines) **unwrapped 156/156 + 93/93**, line-bounded 145/156. After the census
  rebase to 169 rows, the live-revision assembly (500 lines, §1a) re-runs at **169/169 + 93/93** on both views. `PROTOCOL.md` itself
  is green on both views (sanity: unwrapped 93/93 and 156/156), so the unwrapped view is not a relaxation
  invented for a broken file.

## 8. How to re-verify every number in this file

* **V1 — span sizes.** For any candidate span `A–B`: `awk -v a=A -v b=B 'NR>=a&&NR<=b' PROTOCOL.md | wc -l`
  (e.g. `awk -v a=41 -v b=48 …` → `8`, matching the table). Totals: `wc -l < PROTOCOL.md` → 526.
* **V2 — census flip per candidate.** Delete the span in memory, re-run all predicates; the "flips" column is
  exactly the set of ids that go MISS. Equivalent one-liner per candidate:
  `awk -v a=A -v b=B 'NR<a||NR>b' PROTOCOL.md > /tmp/x.md && sh .ufo/waves/round-11/verify-census.sh /tmp/x.md | grep MISS`.
* **V3 — the whole map, executed.** §9 carries the replacement text for all 23 non-delete candidates as marked
  blocks (`<!-- DRAFT <id> <A> <B> -->`). Apply each block to its span, bottom-up, then delete 408–410 (`C2`) and
  329–330 (`C9a`), then run:
  `sh .ufo/waves/round-11/verify-census.sh <assembled> .ufo/waves/round-13/obligation-census-r13.tsv` → expect
  `156/156`, exit 0; `sh .ufo/waves/round-11/verify-census.sh <assembled>` → `93/93`, exit 0; `wc -l < <assembled>`
  → **486**; `awk 'NR<APPENDIX_LINE' <assembled> | grep -o 'round-[0-9][0-9.]*' | wc -l` → **0** (baseline 4,
  must not rise). I ran exactly this assembly from §9's blocks: **491 lines after the 23 blocks, 486 after the
  two deletions, 156/156 `MISS=[]`, 0 body round-refs**. Adding §7.3's appendix move: **450 lines, 156/156**.
  **On the live revision** (§1a): re-anchor every span +15, apply the 23 blocks, the two deletions and `C26` →
  **500 lines, legacy 93/93, r13 156/156, line-bounded and unwrapped, 0 body round-refs** (executed). Track B on
  the live revision: **464 lines**.
* **V4 — census id → today's match lines** (used throughout §3): `grep -nE '<predicate>' PROTOCOL.md`
  with `<predicate>` from `.ufo/waves/round-11/obligation-census.tsv`. Spot values used above: L1@14, L2@25,
  L4@39,410, L5@40,393, R10@89, R11@93, R12@94, R13@95, R14@96, R15@115, R16@119, R17@127, R18@118, R19@132,
  R20@134,138, R22@142, R23@147, R24@149, R25@153, R27@159, R28@165, R29@166, R30@170, R31@173, R32@181,
  R33@188, R41@250, R42@255, R44@265, R47@294, R48@296, R49@298, R50@300, R51@303, E7@331, E8@333, E9@336,
  E10@338, E11@341, F4@398, I4@424, I5@427,430, I6@436,485, I7@439, I9@449, I10@451, V1@470, V2@470, V3@473.
* **V5 — blind mass.** `grep -nE -f <(tail -n +2 .ufo/waves/round-11/obligation-census.tsv | cut -f4)
  PROTOCOL.md | cut -d: -f1 | sort -un | wc -l` → `134`; `526 − 134 = 392` blind lines (343 nonblank).
* **V6 — the extended census runner** (the round-13 acceptance, re-executed by me):
  `sh .ufo/waves/round-11/verify-census.sh PROTOCOL.md .ufo/waves/round-13/obligation-census-r13.tsv` →
  `156/156 obligations found; 0 MISSING`, exit 0 (legacy default unchanged at `93/93`). The file has 157 lines
  (93 legacy rows + 63 new: G1–G37, P11–P29, V6–V11, R52).
* **V7 — the unbreakable-phrase wrap.** Build the phrase set from the census itself: for each row, every literal
  match in PROTOCOL.md of length ≥ 8 chars containing a space. Mask those phrases' spaces (a sentinel byte)
  before `textwrap.wrap(..., width=100)`, restore afterwards. Symptom of skipping this step: `143/156` (§6 R8).
* **V9 — the committed preservation gate** (ExecVerifier's, the round-13 acceptance shape):
  `sh .ufo/waves/round-13/verify-protocol.sh .ufo/waves/round-13/PROTOCOL.compact.md --max-lines 470` →
  `findings checks=8 failed=2` on the live draft (`INFO caps lines=445/470`), the two failures being the
  `## Appendix` modal floor and the appendix data-row/pointer floors (§7.3a). Grading `<target>` only, so a
  digest relocated out of the file reads as an appendix failure by construction.
* **V8 — the unwrapped view (alternative to V7, cheaper).**
  `awk 'BEGIN{RS=""; ORS="\n\n"} {gsub(/\n[ \t]*/," "); gsub(/[ \t]+/," "); print}' <file> > /tmp/unwrapped.md`
  then `sh .ufo/waves/round-11/verify-census.sh /tmp/unwrapped.md [<census>]`. Observed: `PROTOCOL.md` `93/93` +
  `156/156`; masked assembly `93/93` + `156/156`; plain re-wrap (484 lines) `93/93` + `156/156`.
  Usage trap, observed: the verifier runs one `grep` per row, so it **cannot read a pipe** —
  `... | sh verify-census.sh /dev/stdin` gave `150/156` on the same text because every `grep` after the first
  found stdin already drained. Always write the view to a real file first.

## 9. Draft appendix — replacement text for every candidate (canonical, machine-extractable)

Pre-wrapped with the unbreakable-phrase rule, in the exact bytes that assemble to §2’s totals. Markers:
`<!-- DRAFT <id> <A> <B> -->` … `<!-- /DRAFT <id> -->`. `C2` (408–410) and `C9a` (329–330) are deletions and
carry no block; `C15`, `C18`, `C10` are measured ±0 and are kept as the drafts that prove it.

Per-block count: `awk '/^<!-- DRAFT C4 /{f=1;next} /^<!-- \/DRAFT C4 /{f=0} f' .ufo/waves/round-13/scout-compaction.md | wc -l` → 21.
All-block count: `awk '/^<!-- DRAFT /{f=1;next} /^<!-- \/DRAFT /{f=0;next} f' .ufo/waves/round-13/scout-compaction.md | wc -l` → **254** (24 blocks).
Marker spans are **surveyed-revision coordinates** (`e275d4a`): add 15 to any span starting at or after line 29
when applying to the live `2d19a64` file (§1a). `C26`'s marker is already in live coordinates (23–37).

**C1 — 41–48 → 4 lines (saved 4).**
```
<!-- DRAFT C1 41 48 -->
  Minimum bar: the seed's four boxes read strictly — `SKILL.md` holds at least one decision table,
  one error-pattern list and one checklist, each citing a resolvable source; `LOG.md` holds at least
  one end-to-end task (trigger → action → outcome → evidence pointer); instructions are
  self-contained for an agent with no oral context; `PROVINCE.md` still matches reality.
<!-- /DRAFT C1 -->
```

**C23 — 61–69 → 8 lines (saved 1).**
```
<!-- DRAFT C23 61 69 -->
Rounds are driven externally (a scheduler/steer names the round number); the steer advances the
round, the lane owns the work content. Round numbers are monotonic; a lane must not claim a round
other than the steered one — in commits, `LOG.md` entries, corpus lessons, and reports alike. A
round the driver skipped produces no entry rather than a mislabeled one; several entries for one
steered round are allowed. Round prompts are snapshots: where a prompt — or any earlier round's
instructions — conflicts with the current `PROTOCOL.md` or `CORPUS.md`, the repo files win. A lane
re-reads the protocol at the start of every steered round; a long-lived mission does not grandfather
superseded rules.
<!-- /DRAFT C23 -->
```

**C24 — 84–87 → 3 lines (saved 1).**
```
<!-- DRAFT C24 84 87 -->
Rounds are per-lane counters, not a fleet-global clock: the driver keeps `.ufo/state/<lane>.round`
and lanes can sit on different round numbers at the same moment. `reports/round-<N>/` collects
whichever lanes ran their Nth round; the integrator closes round `<N>` per lane, not per fleet.
<!-- /DRAFT C24 -->
```

**C4 — 89–111 → 21 lines (saved 2).**
```
<!-- DRAFT C4 89 111 -->
A lane report **lands last** — written only after the lane's child-repo work is committed, and it
must cite that commit's hash; landed means committed, so changes that exist only in a working tree
do not count. The cited hash is the lane repo's `HEAD` when the report is written — a report naming
a hash the repo does not contain fails verification, and a cited hash that is not an ancestor of
`HEAD` at closure is a conformance defect (`git merge-base --is-ancestor <hash> HEAD` is the check).
Corrections land as new commits, never by amending a cited one — amending or rewriting orphans the
record — and append-only files (`LOG.md`) take an appended correction entry pointing at the
superseded text, never an in-place rewrite. Landed also means landed *by the lane*: the commit that
adds `.ufo/reports/round-<N>/<id>.md` carries the lane identity, because the driver completes the
mission the instant the file reaches disk and any later fleet-level commit can sweep it (§Appendix,
"Lands last"). A swept report is still landed, but the integrator records the attribution defect,
and a lane whose report is still uncommitted when its mission completes has not satisfied this
clause. An orphaned report is resolved in order: the lane's own respawn inherits and lands it;
the integrator sweeps it for durability only if that successor mission also terminates without
landing it, and records the attribution defect — the order never reaches aggregator-owned `corpus/`
files (§Appendix, "Orphaned report"). A terminated lane-round whose report exists on disk but is
unlanded is recorded on its termination evidence with the durability debt named, and the next pass
re-grades it `failed` for want of a landed report if the successor never lands it. A filed report is
a record: a correction to it lands in the correcting round's own report, or as an erratum
appended after the filed bytes in a new commit and naming the text it supersedes — never a rewrite
of the filed bytes, labelled or silent.
<!-- /DRAFT C4 -->
```

**C14 — 113–129 → 14 lines (saved 3).**
```
<!-- DRAFT C14 113 129 -->
Every dispatched lane writes a report at `.ufo/reports/round-<N>/<id>.md` in the main repo, where
`<id>` is the roster id (`protocol` and `aggregator` for the two main-repo lanes); a report under
any other name does not satisfy the contract. For the current respawn driver the report file's
existence is also the round-completion signal: a lane that finishes all other work but files no
report keeps the *driver's* mission open until the stale-lane rule below fires, while a missing
report never holds a round open in the *integrator's ledger* — there the lane-round is recorded
`failed` at closure. Minimum content: - work performed and evidence pointers (paths, commands,
diffs); - changes landed in the child repo, each tied to a `LOG.md` entry; - cross-domain evidence
encountered, with the domain it belongs to; - a `SHONEN.md` checklist assessment for that lane's
shokunin, under a `SHONEN` heading with one line per box (`[x]` / `[ ]` / `[~]` + pointer); `[~]`
means asserted-by-author, not skipped. A report without this heading does not satisfy the contract
even if the same facts appear elsewhere in it, is a conformance defect AND is
disqualified as evidence in that lane's promotion review — the assessment (reports are filed once;
the assessment is not) must be re-filed under the heading in the next round's report.
<!-- /DRAFT C14 -->
```

**C7 — 131–151 → 19 lines (saved 2).**
```
<!-- DRAFT C7 131 151 -->
A lane whose mission has terminated or been respawned without filing its round report is recorded
`failed` by the integrator. `failed` covers every lane-round that was prompted or dispatched and has
no report by closure, including a prompt left behind by a failed launch (dispatch evidence and
orphan prompts: step 4). A mission still open more than two driver ticks after its steer is a
stale-lane review trigger, and the integrator may record it `failed` so the driver respawns it on a
fresh prompt. The trigger needs an actuator: every dispatched lane's report must list any mission
open longer than two driver ticks — age computed from the launch timestamp, not the tick counter,
which resets when the driver restarts — and must say whether it is *progressing* or *silent*.
Progressing means observable activity in the lane's write scope since its launch — a commit authored
by the lane, or files modified under its repo (`find <repo> -newermt <launch-ts> -type f -not -path
'*/.git/*'`); silent means neither. A commit authored by *another* lane is not the subject lane's
activity — the aggregator writes into every child repo — so
sibling-authored activity alone is a third grade, `progressing-weak`: named as such in the row,
never called progressing, and never silent or `failed` on its own. Commit sparsity is normal in this
fleet (§Appendix, "Stale-lane actuator"): the absence of a commit is not silence and must not
trigger `failed`. The integrator-of-record records `failed` only for silent missions and flags
progressing ones in the round notes — and recording `failed` is a ledger act, not a kill: the
driver's respawn path is unreachable while its daemon is up (step 4), so nothing in this section
terminates live work.
<!-- /DRAFT C7 -->
```

**C15 — 153–157 → 5 lines (saved 0 (refused, ±0)).**
```
<!-- DRAFT C15 153 157 -->
A respawned mission inherits its predecessor's working tree: uncommitted *lane-authored* changes it
finds are uncommitted round work under the landed-means-committed rule — the new lane resolves them
(commit-under-its-entry or revert) before it files its own report. Uncommitted **aggregator-owned**
files (`corpus/lessons/round-*-aggregator-*`) are not the lane's to commit: the lane records them in
its report and leaves them for the aggregator.
<!-- /DRAFT C15 -->
```

**C17 — 159–168 → 9 lines (saved 1).**
```
<!-- DRAFT C17 159 168 -->
A file at the report path is not automatically a report. The driver's completion signal is that
path's existence (`report_of()` in `scripts/shokunin-watchdog.sh`), so a contentless **completion
marker** can close a lane-round with no work behind it (§Appendix, "Marker vs report"). A filed
report that records no lane work — no changes, no evidence pointer, no resolvable commit — is a
marker, not a report: the integrator records that lane-round `failed`, keeps the marker file as a
conformance defect, and names the counter advancement in the round notes. A short report that names
a real committed round-work hash is a *defective* report, not a marker: status `ok`, minimum-content
defect recorded. A marker that names nothing checkable is `failed` whatever the lane actually did.
This does not relax step 1: contract violations inside a real report stay status-neutral defects.
<!-- /DRAFT C17 -->
```

**C5 — 170–186 → 15 lines (saved 2).**
```
<!-- DRAFT C5 170 186 -->
**Integrator of record.** The integrator this protocol assigns work to is the round's `protocol`
lane — a role, not a separate rostered lane; where a generated driver prompt conflicts (e.g. "never
MANIFEST.json"), this file wins per the snapshot clause. Its main-repo writes are
`PROTOCOL.md`/`ROADMAP.md`/`SCORECARD.md`/`LOG.md`/its own report, and expand by exactly five:
appending `MANIFEST.json` `rounds` entries, the conformance/routing record inside its own report
(the round notes), committing already-generated `.ufo/prompts/*.md` so dispatch evidence is durable,
committing `.ufo/l0-questions.md` so the operator queue is durable, and committing the round's
closure-gate artifacts under `.ufo/waves/round-<N>/` — it never edits a prompt or the script, and
`scripts/` plus `.ufo/state/` remain operator-side (§Invariants); required template corrections are
named in its report. Its closure artifact is its own round report: a protocol-lane report carrying
no closure record — the statuses it wrote, or a statement of why none was writable — is an
incomplete report whatever else it contains. Generated protocol prompts name none of steps 1–4
(§Appendix, "No closure channel"), so the duty reaches the lane solely through this file's re-read.
The closure record is a gate, not prose: steps 1 and 4 run through a committed checker whose frozen
re-run reproduces every status the entry carries (§Gate standard, "Two evidences").
<!-- /DRAFT C5 -->
```

**C8 — 188–194 → 6 lines (saved 1).**
```
<!-- DRAFT C8 188 194 -->
A round is **completed** when every dispatched lane has either reported or been recorded failed by
the integrator — a failed lane counts; a missing report does not. Under the respawn driver lanes
hold different counters at the same instant, so fleet-wide completion is never observable
(§Appendix, "Closure entries"). Closure is therefore per lane-round: each protocol round the
integrator closes every lane-round that terminated since its last pass plus any older one still
carrying an unresolved row (step 4). After closing, the integrator:
<!-- /DRAFT C8 -->
```

**C18 — 196–204 → 9 lines (saved 0 (refused, ±0)).**
```
<!-- DRAFT C18 196 204 -->
1. Reads every lane report and verifies each cited child-repo commit exists *and is an ancestor of
the lane repo's `HEAD`*; verifies no participating repo is left with uncommitted round work
(uncommitted aggregator-owned files are reported, not lane debt); checks each report for the
contract-required `SHONEN` heading; checks the round's dispatched `.ufo/prompts/*.md` carried the
five contract items verbatim per the embed clause above **and that any L2 route map quoted in the
prompt matches the current `MISSION.md` bucket**. A report that violates the report contract
(missing heading, dead or orphaned hash, report filed before its commit) or a prompt missing
embedded items is recorded as a conformance defect in the round notes — this does not change the
lane's status unless the round's rules already prescribe `failed`.
<!-- /DRAFT C18 -->
```

**C19 — 205–216 → 11 lines (saved 1).**
```
<!-- DRAFT C19 205 216 -->
2. Lands warranted protocol improvements in this file (a highly valuable feature discovered by any
domain generalizes to the protocol); routes cross-domain defects a lane report filed against a
sibling's files to the owning lane — and the integrator's report carries one routing line per defect
**including defects a lane owes its own repo** (self-defects ride the same durable queue; routing is
integrator work and must exist in an artifact). The aggregator mirrors each routed defect into the
owning repo's `corpus/lessons/` (aggregator-owned naming) and keeps an **open routed-defects row**
in its ledger (canonical path and fallback queue: the aggregator-lane paragraph below) until the
owning lane's `corpus/lessons/` or `SKILL.md` correction lands; unresolved rows are re-flagged each
audited round, and on its first audited round after any absence the aggregator sweeps intervening
lane reports and round notes and reconciles ledger rows before new audits. The ledger row — not
round notes alone — is the durable queue.
<!-- /DRAFT C19 -->
```

**C12 — 220–226 → 5 lines (saved 2).**
```
<!-- DRAFT C12 220 226 -->
4. Appends one entry to `MANIFEST.json`'s `rounds` array (integrator-of-record scope; each lane's
own `LOG.md` entry remains lane work, not integrator work). Round-entry shape: `{round, date, type,
lanes: {<id>: <status>}, promotions: [{id, from, to}], minted: [id...], notes}` where `<status>` is
`ok | failed | not-dispatched | in-flight`; `type`, `closed_at`, `protocol_updates`, and other
annotation keys are optional. Semantics under a per-lane-counter driver:
<!-- /DRAFT C12 -->
```

**C20 — 227–232 → 5 lines (saved 1).**
```
<!-- DRAFT C20 227 232 -->
- **Partial entries are the norm.** Write the entry for round `N` as soon as one lane's Nth
lane-round terminates: a terminal status for every `N` lane-round that has terminated, `in-flight`
for lanes dispatched and still open, `not-dispatched` for lanes with no dispatch evidence **as of
`closed_at`** — so `closed_at` is required on any entry carrying a `not-dispatched` row. Waiting for
all eight counters to reach `N` waits forever.
<!-- /DRAFT C20 -->
```

**C16 — 233–252 → 17 lines (saved 3).**
```
<!-- DRAFT C16 233 252 -->
- **Dispatch evidence** is the `.ufo/watchdog.log` dispatch line — `launch <lane> round=N` (respawn
driver, written only after a successful launch) or `steer <lane> -> round N` (steer-era driver —
§Appendix, "Dispatch evidence"). The committed `.ufo/prompts/<lane>-round-N.md` corroborates mission
*content* and must be committed to be durable, but `lane_prompt()` writes it before the launch is
attempted — a prompt with no dispatch line is an attempted dispatch and records `failed`.
**Completion evidence** is a `.ufo/reports/round-N/<lane>.md` that satisfies the report contract; a
completion marker is not a report (see above) and makes the lane-round `failed`. **Termination
evidence** is a `complete <lane> round=N` line or the lane's counter passing `N`. Liveness probes
are not evidence of an open mission: `ufo-sighting status --lite` still lists a mission after the
driver `complete`d it (§Appendix, "Liveness probes"), so the driver's `live` test can never fail
while its daemon is up and its `lane-dead-no-report` retry path is unreachable. `in-flight` is
therefore decided from the absence of both a `complete <lane> round=N` line and a *landed* report —
an uncommitted file at the report path does not end `in-flight`, however it fires the driver's
existence signal (§Appendix, "Unlanded report") — and never from a status probe. `.ufo/watchdog.log`
is mutable and the driver appends to it concurrently, so its line numbers drift: the round notes
carry a committed digest (timestamp + text) of every dispatch/complete line a status rests on, and
that digest — not the live log — is the pointer that resolves at closure.
<!-- /DRAFT C16 -->
```

**C21 — 253–260 → 7 lines (saved 1).**
```
<!-- DRAFT C21 253 260 -->
- **`in-flight` is debt, not a resting status.** Every `in-flight` row is answered by the next
protocol round — resolved to a terminal status or re-confirmed with evidence — which appends
`{"round": N, "type": "closure-correction", "closed_at": …, "lanes": {<id>: <status>}}` — never an
in-place edit. A lane dispatched for its Nth round *after* round `N` closed rides the next
closure-correction for `N` — never dropped, never folded into `N+1`. An `in-flight` row whose
mission is still live at the next pass is re-confirmed by a closure-correction carrying `in-flight`
plus the launch pointer, and stays debt until the mission terminates.
<!-- /DRAFT C21 -->
```

**C22 — 264–273 → 9 lines (saved 1).**
```
<!-- DRAFT C22 264 273 -->
- **A row names the lane-round it describes.** `lanes` values stay status strings; the optional
`lane_rounds: {<id>: <n>}` map records a lane's own counter where it differs from the entry's
`round` and is required on every `not-dispatched` row — the counter the lane actually held is what
makes such a row falsifiable. The row describes lane-round `(<id>, round)`: `lane_rounds` annotates
it and never re-keys it, so last-wins is computed over `(id, entry.round)`; reading the map as the
key erases in-flight debt and manufactures rows out of the pre-fleet-2 fleet-keyed entries, which
carry no `lane_rounds` and are `unadjudicable` as lane-rounds (§Appendix, "Row identity"). An `ok`
row needs no pointer: `.ufo/reports/round-<n>/<id>.md` is derivable, and its absence falsifies the
row. `failed`, `in-flight`, and `not-dispatched` rows carry their pointer in `notes`.
<!-- /DRAFT C22 -->
```

**C6 — 289–304 → 15 lines (saved 1).**
```
<!-- DRAFT C6 289 304 -->
The **aggregator** lane is a main-repo lane that reviews every child repo's `corpus/` each round
(per `CORPUS.md`), files gaps as lessons inside the child repos, and files its own round report at
`.ufo/reports/round-<N>/aggregator.md` covering per-repo corpus verdicts and cross-lane learnings.
It is the sole exception to lane write-scope: it may create or repair `corpus/` inside any child
repo — nothing else: no main-repo files outside its own report and ledger. Every file it creates
inside a child repo is **committed by the aggregator itself at creation time**, pathspec-limited to
its own files, under its own subject (`corpus: round-<N> aggregator …`) — never left uncommitted for
a lane's round commit to sweep, and a lane never commits an aggregator-owned file. Alongside the
per-round report it maintains one rolling audit ledger — canonically `.ufo/reports/AGGREGATE.md`,
and no third path counts; a superseded snapshot elsewhere is relocated there by its next refresh —
superseded, not voided. While the canonical ledger is absent or unrefreshed, the integrator's round
notes are the queue of record (§Appendix, "Ledger"). The ledger is append-only in the same sense as
`LOG.md` — refresh sections supersede earlier rows explicitly rather than rewriting them. An
aggregator round report is incomplete unless the ledger was refreshed or the report names why no row
changed.
<!-- /DRAFT C6 -->
```

**C9a — 329–330 → DELETE (proposed 0, saved 2).**

**C9b — 331–344 → 12 lines (saved 2).**
```
<!-- DRAFT C9b 331 344 -->
- **Claimed ≠ re-executed.** A command offered as evidence is a re-run performed at write time with
its observed output — never an output quoted from memory or a prior session. - **Corrections
sweep every mention.** Before a round's commit, grep every file the lane touches
(`corpus/README.md`, `SKILL.md`, `knowledge/`) for the superseded claim — a corrected fact left in a
sibling file is still a defect. - **A falsified claim in an append-only file gets a
named correction entry in the lane's next round** — appended, never rewritten; it stays on the
routed-defect queue until it lands. - **Commits are cited by hash, never by subject or tag** — a tag
that resolves to nothing is not a citation. - **Drift pins.** A corpus that cites host files by
line/content may carry a pin mechanism — but a pin only counts if its expected values are
**persisted inside the repo** (a recorded sha/mode/lines baseline, or a committed expected-output
file the script diffs against). A fingerprint *printer* with no stored baseline cannot detect drift;
recommended where the surface drifts outside lane control.
<!-- /DRAFT C9b -->
```

**C10 — 375–380 → 6 lines (saved 0 (refused, ±0)).**
```
<!-- DRAFT C10 375 380 -->
- **Closure consequence.** A red gate is a conformance defect recorded in the round notes and routed
to its owner — status-neutral unless the round's rules already prescribe `failed`, gate redness is
never the marker predicate (step 1 grades marker-versus-real-report first).
The integrator verifies a gate's *committed evidence* (self-test tally, frozen-run verdict, the
revision measured); it does not execute a sibling's gate, whose dependencies and write scope are the
lane's.
<!-- /DRAFT C10 -->
```

**C2 — 408–410 → DELETE (proposed 0, saved 3).**

**C3 — 424–439 → 13 lines (saved 3).**
```
<!-- DRAFT C3 424 439 -->
- `MANIFEST.json` is canonical for rank and roster; `ROADMAP.md` mirrors it. Only integrator roles
write main-repo files — `MANIFEST.json`, `PROTOCOL.md`, `ROADMAP.md`, `CORPUS.md`, `MISSION.md`,
`AXES.md`, `scripts/`, `.ufo/` state and prompts. `MISSION.md`, `AXES.md`, and `scripts/` are
operator-side integrator files: the protocol lane names the corrections they need in its round notes
and does not edit them, and `MANIFEST.json` edits *outside* `rounds` (roster, rank, minting) are
operator-side too. Lanes write only inside their own child repo and their lane report at
`.ufo/reports/round-<N>/<id>.md`; the two main-repo lanes (`protocol`, `aggregator`) additionally
keep `SCORECARD.md` and `LOG.md` at the main-repo root, because their axes are fleet-level.
`.ufo/reports/`, `.ufo/waves/`, and the round's generated `.ufo/prompts/*.md` are the round's
written evidence, committed with the round's integration commit — an untracked prompt is non-durable
dispatch evidence. `.ufo/state/` and `.ufo/watchdog.log` are driver runtime that churns every tick
and are tracked (§Appendix, "Tracked runtime"): no lane commit may include them; the enforcement is
pathspec-limited commits. Untracking them is operator-side work named in the round notes.
<!-- /DRAFT C3 -->
```

**C11 — 442–452 → 10 lines (saved 1).**
```
<!-- DRAFT C11 442 452 -->
- Local-first: repos live locally; **domain-facing actions are operator-owned** (publishing, vault
approval, claim submission). Push scope is owned by `MISSION.md` §Push scope — hard rule: lanes push
only to the main repo and their own `<lane>-shokunin` remote; domain source trees are read-only and
upstream-bound work is carried in the round report. Repo bookkeeping — committing and `git push`ing
the round's commits — is ordinary lane work, not publishing, when the driver instructs it.
Exception: operator-gated artifacts (staged payloads, publish candidates, vault material, embargoed
evidence) are committed locally but not pushed until the operator releases the gate — bookkeeping
never front-runs an operator decision. A lane's main-repo commit is pathspec-limited to its own
report file (`git commit -- .ufo/reports/round-<N>/<id>.md`) — never `commit -a` / `add -A`, which
sweeps up sibling in-flight edits and integrator working-tree changes.
<!-- /DRAFT C11 -->
```

**C13 — 467–485 → 17 lines (saved 2).**
```
<!-- DRAFT C13 467 485 -->
- Expertise axes live in `AXES.md`; each lane owns a named subset and works one axis-move per round,
measured in `SCORECARD.md`. An axis-move inherits the evidence standard: before and after numbers
each carry the counting command and the commit they were measured against, and a score no reader can
re-derive is an opinion, not a measurement. Axis work does not displace the file contract — a round
that moves an axis while `corpus/`, `LOG.md`, or `SHONEN.md` drift are a conformance defect like any
other. - `MISSION.md` is the mission SSOT: fleet shape, model map, concurrency floor (the L2
minimum's source), push rule, L0 side channel. Watchdog prompts bind to it. Precedence between the
two SSOTs: `PROTOCOL.md` owns process, evidence, and gates; where they conflict on process —
`MISSION.md`'s unconditional "commit then push" against this file's operator-gated hold, for
instance — `PROTOCOL.md` wins and the conflict is named in the round notes; neither file is edited
by a lane. - L0 side channel: lanes append `.ufo/l0-questions.md`; the aggregator surfaces it. The
file is append-only in the same sense as `LOG.md` — a lane restating or correcting its own question
appends a new line naming the superseded one and never rewrites a filed line, and the operator's
in-place answers are never a lane write. Cite a question by lane + round + its opening words,
never by line number: the queue grows, so every line number moves. Its durability owner is the
integrator, which commits it with the round's integration commit — a lane's appended question is
non-durable until committed and no lane owns the path (§Appendix, "L0 durability").
<!-- /DRAFT C13 -->
```


**C26 — live 23–37 → 14 lines (saved 1), `## Lifecycle`, indent 0.** The lane-initiated sibling-mint bullet
(landed in `2d19a64`). Conservative re-wrap — every step (a)–(d) and both prohibitions intact, the census's own
phrasing restored (`probation state is recorded in`, `it never edits \`MANIFEST.json\` roster`), pinned phrases
held unbreakable. It **was** census-blind when this map was drafted; the rebased census now pins it with
**L8–L20**, so deleting live 23–37 scores `156/169` (13 MISS).
```
<!-- DRAFT C26 23 37 -->
- **Sibling mint (lane-initiated)** — any lane may mint a sibling when it finds a domain demand no
existing province owns. In order: (a) scan `MANIFEST.json` + every `PROVINCE.md` and
records the roster map it decided against — that scan record is part of the mint evidence; (b)
create the sibling's repo dir `{id}-shokunin/` and its GitHub remote `VeigaPunk/{id}-shokunin`,
seeding the canonical files (SKILL.md, PROVINCE.md, SHONEN.md from the canonical template,
AGENTS.md, LOG.md) plus a `MINT.md` stating the reasoning, the cause, the
demand instances with evidence pointers, the rejected roster fit, and the claimed domain boundary;
(c) the sibling is wired into the driver (`LANE_CWD`/`LANE_MODEL`/`LANE_AXES` —
operator-side integrator work, surfaced in `.ufo/l0-questions.md` if the lane lacks the route map)
and self-iterates through at least three verified rounds building `corpus/` + `PROVINCE.md`; (d)
only after those rounds land does the operator add the `MANIFEST.json` roster row and `ROADMAP.md`
table row — probation state is recorded in `rounds[].notes` meanwhile, not as a roster row. The
minting lane never writes outside its own repo + the new sibling's seed files;
it never edits `MANIFEST.json` roster or a sibling's post-seed content.
<!-- /DRAFT C26 -->
```

## 7.6 Errata — this map's floor is *this map's cut set*, not a floor (peer result, re-executed)

ExecCompact, working from its own cut list rather than mine, falsified the stronger reading of §0/§2. My claim
was scoped ("the obligation-preserving ceiling **I** could measure"), and it was stated as if it were a bound;
it is not. Re-executed by me on its artifacts:

| artifact | lines | bytes | md5 | r13 census (169 rows) | legacy |
|---|---|---|---|---|---|
| `PROTOCOL.compact.md` (body + 4-line `## Appendix` pointer block) | **459** | 38858 | `2fe00da4e28902a6eac9d719682c6f54` | `169/169` | `93/93` |
| `PROTOCOL-APPENDIX.compact.md` (digest artifact, 32 dated rows) | 40 | 9570 | `697ba3a0cefd4220ff1e112e0e849b4e` | — | — |
| `PROTOCOL.compact.singlefile.md` (appendix in-file, record) | **493** | 48020 | `e178013e9f717a4d33665a22b6f3682e` | `169/169` | — |

Its own floor finding: a **470-line single file was gate-clean for the pre-round-13 obligation set**, 479 with
the four round-13 obligations, 493 with `2d19a64`'s sibling-mint bullet — i.e. **my 486 (surveyed) / 501 (live)
is 31 lines above what a broader rule-preserving search reached on the same obligation set.** Independent check
of its artifact against §5: **all 16 do-not-cut spans survive in the 459-line body** (unwrapped view; one false
negative on my side — `probation is recorded in` — where the bullet is present and merely reworded, the same
line-bounded-substring trap §6 R8b warns about).

Corrected reading of this map's numbers: §2's Track A is *the sum of the cuts in §3*. Anyone who wants the
real floor should take 459 body + 40 appendix artifact as the compliant shape on the live base (≤470 **only**
in split form, requiring the two-file gate mode of §7.3a), and 479–493 as the single-file range for the live
obligation set. Also adopted from that seat, a third interference class for the census: **`**bold**` markup
inside a predicate span breaks the literal match** (its first attempt MISSed 7 sibling-mint rows that way, all
false) — alongside wrap splits (§6 R8) and rewording (§6 R8b). Measured witnesses for the emphasis class, each
edit applied alone with the full 169-row census re-run: `snapshot` → `**snapshot**` inside G14's span → G14
MISSes; `a **probe**, and is registered as one.` → `a probe, …` → G4 MISSes; `never the marker predicate` →
`never the **marker** predicate` → G22 MISSes; `at least three verified rounds` → `at least **three** …` → L12
MISSes — all four with the obligation intact. Scale: **24 of the 169 matched spans already contain `*` or a
backtick**. Reading rule in three steps, which any grading lane should apply before weakening a row: (1) wrap
split → settle it with the unwrapped view; (2) reword → visible only inside the pinned span, fix the text or
re-derive the row; (3) **emphasis markup → the unwrapped view does *not* settle it** — leave the span's markup
untouched or re-derive the row. One more caveat it reports and I echo: the gate
script itself was mid-edit by siblings twice in that window (`SECTION_KEYS: unbound variable`, then a syntax
error) — a could-not-evaluate state, not findings; re-run the settled gate before grading.

## Unknowns

* Whether the lane accepts Track B's appendix offload; without it the measured floor is **486**, i.e. the ≤470
  acceptance criterion is unmet by 16 lines by any obligation-preserving map I could construct (affects §2,
  §7.3). The alternative — buying the 16 lines from §5 — is a rule deletion the legacy census will not catch.
* Which path the digest would take if offloaded, and whether the round-13 census extension will pin it
  (affects §6 R5).
* The census row **R31**'s intended count ("three" vs the file's "five") — a pre-existing inconsistency I did not
  resolve; the census-extension seat has since pinned the live numeral in a new row **R52** (`expand by exactly
  five`) and recorded the stale description in `.ufo/waves/round-13/scout-census.md §Legacy rows` (affects §3
  C5's note only).
* Whether a compactor's legitimate re-wording of a pinned clause trips the extended census: the r13 rows key on
  pre-existing wording, so **a cut that rewords a pinned clause MISSes even when the obligation survives** — run
  the extended verifier and treat such a MISS as gate-integration work, not as a reason to weaken a row
  (affects §6, §8).