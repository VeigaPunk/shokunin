# kake — round 51 (attempt 2)

Lane: `kake-shokunin` (axes: operability + freshness). Base for every before-measurement:
`007d66e4e8360a5f88d29a93eeedd8066dad4434`. Measured lane commit: `842c1b44a590104cff4c06ef84726cac19475d0a`.
Author: in-session L1 (hyaku run 6). Report shape: default — one v1 wave of 48 seats, then a residual
wave-2 call of 6 reviewer/critic/scout seats dispatched only after the wave evidence was committed.

**Earlier attempts.** The watchdog logged `lane-dead-no-report kake round=51` for attempt 1, which had
committed three lane commits (`19a99bd`, `5591557`, `9d13768`) and left everything else uncommitted.
Inherited and re-verified: the frozen contract, both counters, the two registry rows, both entries, the
lesson. Inherited and **discarded**: the "pre-append" mirror snapshot (it was post-append bytes — see
`## Landed changes` and the lesson's Mistakes) and attempt 1's four census receipt files (kept verbatim
under `assimilation/pre-append/superseded/`). Attempt 1 committed no wave evidence, so nothing of it is
reused for C1.

## Work performed

Two claims, frozen in `.ufo/waves/round-51/contract.json` before any score:

- **C1 — operability, capability acquisition.** A committed wave-evidence ledger that re-derives a
  round's own seat accounting, route receipts and time accounting from committed bytes.
  Predicate `met: ledger_checks_passed == 3 of 3`;
  `python3 -B .ufo/waves/round-51/c51_wave_ledger.py --root . --revision <commit>`.
- **C2 — freshness, sourced learning claim.** Google's canonical *selection* and its crawler
  *identity* enter held ground as two source-backed entries on rows S262 and S263, re-grounded this
  round. Predicate `met: conditions_passed == 8 of 8`;
  `python3 -B .ufo/waves/round-51/c51_quote_truth.py --root . --revision <commit>`.

Separable: C1's counter reads only the wave evidence (settlement, payload, route map, probe receipts,
timing pair, time accounting, LOG.md); C2's reads only the registry, the two entries, the lesson, the
retained bodies and the pre-append mirror. Neither reads the other's inputs.

Work items (one bullet per item; every claim below rests on a committed byte at `842c1b4`):

- **C1 evidence built and committed.** `settlement.json` (48 seats, 48 reports, 0 dead),
  `wave-timing.json` (06:32:17Z → 06:47:14Z = 897 s), `round-time-accounting.json` (wall 897, aggregate
  23 554 seat-seconds, dead 0), `route-map.json`, `route-probes/*.json`, `wave-grant.txt`
  (`granted lane=kake wave=r51-w1 seats=48 …`), `w51-taskcall.json` (validator payload, `counts.spawn 48`).
- **Wave dispatched as exactly one `task` call** from the validator's `ufo-swarm-wave-dispatch-v1`
  payload (`w51-taskcall.json`, validator exit 0, `w51-validator.err` empty). First dispatch attempt was
  refused at the harness job cap ("Background job limit reached (100)"); the same payload was resent once
  after capacity freed and spawned all 48 seats — no seat was dropped, shrunk or replaced.
- **Route receipts.** One route used: `@m_flash` → `commandcode/deepseek/deepseek-v4.1-flash`
  (`route-probes/commandcode_deepseek-v4.1-flash.json`, HTTP 200 at the provider edge, completion leg
  answered `PONG` via `omp -p --mode json`). One recorded deviation:
  `route-probes/xai-oauth_grok-4.7-fast.json`, HTTP 403 with a body excerpt, bound to no role.
- **Seat accounting re-derived independently** by `ResidualC1Rerun`: 49 committed files under `w1/`
  (48 `.md` + `swarm-registry.json`), name-set equality both ways against the settlement, aggregate
  re-summed to 23 554, wall re-derived to 897 (`residual/ResidualC1Rerun.md`).
- **C2 rows and entries** (inherited, re-verified): 143 → 145 rows, both tier A, `mined`, `opened
  2026-10-24`, `recheck 180d`, `used-by` exactly the citing entry; append-only proof is
  `sed '152,153d'` on the tip reproducing the base byte-for-byte (`w1/ReviewAppendOnly.md`).
- **QUOTE-CLASS DEFECT FOUND AND CORRECTED.** 15 body quotations in the two entries are 3 raw,
  2 whitespace-collapsed-only and 10 that need inline-markup removal; 10 of 13 source-relation labels
  were wrong (`w1/ExecQuoteRawScan.md`, `w1/ScribeEntryAudit.md`). Both entries now carry a
  `## Quote classes (round-51 correction)` block and the two false in-line labels were replaced. The
  16 over-assertions the audit named are **not** repaired; they are routed (same report).
- **SPECIAL: the mirror was rebuilt.** Attempt 1's pre-append mirror was byte-identical to the
  post-append registry (145 rows, both ids). Found by `w1/ExecRegistryDiff.md`, confirmed by five other
  seats. Rebuilt from `git show 19a99bd:corpus/SOURCES.md` (143 rows, sha256 `cd9ee4cf…`), census
  re-run (`--file`, exit 0, W04 only), a discriminating `census` receipt added (`rows 143`), attempt 1's
  receipts archived under `superseded/`; all recorded in
  `.ufo/waves/round-51/assimilation/pre-append/census-correction.txt`.
- **Quarantine.** The lane's 12-row slice of the campaign register was re-derived read-only, its
  verbatim output committed as `assimilation/quarantine-slice.raw` (the committed `quarantine-slice`
  had normalised backticks away), and nothing adopted; the residual critic ruled unadopted acceptable
  under the clause's conditional grammar (`residual/…`, `w1/CriticQuarantine.md`).
- **Frontier step.** Census before → after below; two rows added, both tier A; one frontier line
  narrowed (`PROVINCE.md` § Round-51); lesson carries admit/reject pairs, the wave accounting, four
  attempt-2 mistakes and the corrections to two false attempt-1 mistake rows.
- **Residual wave 2** (6 seats, dispatched after `907790c`): C1 re-run and independently re-derived;
  C2 re-run at base and tip plus a hand-verified C6; the rebuilt mirror checked under both readings;
  the real settlement attacked; the LOG figure audited; the round-end census run.
- **No tool installed or upgraded** this round (no pacman transaction attempted; the host-wide pause
  was respected).

## Landed changes

| Commit | What it carries |
|---|---|
| `19a99bd8c30d36a4d664871236ba2015d893b5b9` | attempt 1: claim declaration, frozen contract, both counters, junk/base controls, pre-append mirror (later found contaminated) |
| `55915579563a781adcebc2e269cff57470ce2a8e` | attempt 1: S262/S263 appended, the two entries and the lesson landed |
| `9d13768c4fdd0e9a2688d2ecf1616b539cf57658` | attempt 1: C2 counter receipt lookup fixed (post-data, pre-scoring; disclosed in LOG) |
| `907790c78008819fc95c988431188f90b81f0d5f` | attempt 2: wave evidence (settlement, timing, accounting, route map, probes, grant, payload, 48 seat reports), rebuilt mirror + receipts, entry quote-class corrections, lesson wave/mistakes/corrections, SCORECARD results + capability row, LOG wall-clock entry, PROVINCE § Round-51 |
| `842c1b44a590104cff4c06ef84726cac19475d0a` | attempt 2: the 6 residual wave-2 verdicts, the restated C8 repair, the mirror receipt limits, post-commit seat report updates |

Every change is tied to a LOG.md entry (§ Round 51 — four attempt-1 bullets, three attempt-2 bullets)
and to the commit above that carries it.

## Before → after measurements

| Claim | Before (base `007d66e`) | After (`842c1b4`) | Counting command |
|---|---|---|---|
| C1 | `C1 ledger 0/3 met=False`, exit 1 — no ledger instrument, no route receipts, no timing | `C1 ledger 3/3 met=True`, exit 0 — L1/L2/L3 pass, no notes; facts 48/48/48/48/48/48, roles 10, receipts 2, wall 897, aggregate 23 554, dead 0 | `python3 -B .ufo/waves/round-51/c51_wave_ledger.py --root . --revision <commit>` |
| C2 | `C2 quote-truth 0/8 met=False`, exit 1 — all eight conditions fail | `C2 quote-truth 8/8 met=True`, exit 0 — all eight pass | `python3 -B .ufo/waves/round-51/c51_quote_truth.py --root . --revision <commit>` |

Both pairs were re-run at the measured commit by a residual seat from committed bytes
(`residual/ResidualC1Rerun.md`, `residual/ResidualC2Rerun.md`). The do-nothing controls are the base
revision itself (0 of 3 and 0 of 8), which no do-nothing round can pass because every input is read
with `git show <rev>:<path>`; the junk controls committed by attempt 1 cite revisions that do not
exist in the lane and are **not** replayable, and a residual seat's three one-change mutants replace
them for C2 (8/8 → 7/8 → 6/8 → 5/8, exit 1 each, `w1/ReviewQualityBar.md`).

**Verdicts, with their limits stated rather than smoothed:**

- **C1: MET as declared** — with the measured caveat that the frozen L1 sentence asks for agreement
  between artifacts one author types, not for independence. Four seats scored `3/3, exit 0` on
  synthetic evidence (empty wave, phantom seat, 48 zero-byte reports, an unreported seat dropped from
  both lists, a used route whose receipt says `httpStatus 500, ok true`). The claim's honest reading is
  "the wave evidence is internally re-derivable and internally consistent", which is what the
  capability row says. The concrete hardening is routed, not applied — a rule changed after items have
  scored is not the claim's rule.
- **C2: MET at the counter's reading, contested under a third reading.** C8's sentence names "the
  registry at that mirror": the live registry at the mirror's add-commit (143 rows, neither id — the
  counter's reading) and the mirror file at the measured revision (143 rows, neither id — after this
  round's rebuild) both pass. A literal reading as "the bytes committed at the mirror's add-commit"
  fails permanently (that blob is the contaminated `4ea81a5a…`) and cannot be repaired without
  rewriting history. The mirror itself was reconstructed after the append, so no committed receipt
  evidences a census of the 143-row bytes taken *before* the append; C7's receipt is shape-level, and
  only the `census` receipt binds the count. Fully recorded in
  `assimilation/pre-append/census-correction.txt` and `w1/ReviewC2Conditions.md`. Admission of this
  residual is the non-author closure's call; the author-side verdict is met-with-limits, not a
  clean met.

## Sources & frontier

Census, both runs with the frozen command (exit 0 required at round end):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake
```

| When | Exit | Rows | Output |
|---|---|---|---|
| round open, at base `007d66e` (before) | 0 (measured from a `/tmp` copy of the base registry: `validate --file`, `census` → `rows 143`, tier.A 120/B 6/C 17, mined 113) | 143 | 12 × W04, `ok` |
| round end, at `842c1b4` (after) | **0** | **145** | 12 × W04 (same ids), `kake ok` |

`census --root … kake` at round end: `rows 145`, `tier.A 122 / tier.B 6 / tier.C 17`,
`status.mined 115 / status.queued 8 / status.rejected 22`, exit 0 (`residual/ResidualCensus.md`).

- **Rows added, by tier:** 2 rows, both tier A, both `kind docs`, both `status mined` — S262
  (`developers.google.com/…/canonicalization`) and S263 (`developers.google.com/…/googlebot`), each
  `used-by` exactly the one entry that cites it.
- **Rows touched old→new:** none. No pre-existing row's cell changed (byte reconstruction:
  `sed '152,153d'` on the tip equals the base; base id order is an ordered subsequence of the tip's).
- **Frontier rows advanced:** 1 — `PROVINCE.md` Frontier line 23's "canonical/JS rendering open" is
  now partly held by `corpus/knowledge/canonical-selection.md` (selection half) and
  `corpus/knowledge/crawler-identity.md` (identity half); JS rendering stays open and stays tabi's for
  anything that executes a browser. The § Round-51 PROVINCE block records both and the subtype
  ambiguity the held entries inherit.
- **Sourced claim:** C2 rests on S262 and S263, both **opened by this lane this round** (2026-10-24,
  23:16:49 -03:00), bodies retained under `.ufo/waves/round-51/sources/` with sha256 in
  `receipts.json`; each lesson `## Gate` line carries the URL, the access date and a ≤25-word located
  quote that is a raw substring of its own retained body (`a hint, not a rule`, 10 words;
  `Googlebot is the generic name for two types of`, 9 words).
- **Assimilation:** one theme adopted from the `shokuknow` package (`merge/kake/`), three staged
  entries judged — 1 theme, 2 entries admitted (S262, S263 re-grounded in-round), 2 entries refused
  with reason and flip inside the lesson's `## Gate` (`engine-crawl-contracts.md`: within-scope
  duplicate URL (E04) plus two unopened Baidu sources; `crux-eligibility-route.md`: covered ground).
  The id-collision guard was re-derived read-only; the staged ids overlapping the lane registry are
  S273/S274/S286 and none is adopted (`assimilation/{reg-ids,staged-ids,collisions,guard/}`). A residual
  critic measured that the committed `staged-ids` list matches no package revision and that a
  shape-repaired append under a live id would be silently accepted — routed.
- **Quarantine:** 12-row slice, all carrying an S-id, none adopted, verbatim output committed
  (`quarantine-slice.raw`); the register itself untouched.
- **considerthese/**: present (six files, newest `2026-10-24.md`); **no proposal mined this round** —
  the round's 1–3 claim cap was spent on C1 and C2 and the frontier step, and the operator input was
  not edited.

## Trend verdicts

- **expansion — improved.** Two knowledge entries on ground the lane's coverage map did not hold: the
  selection half of the canonical signal (explicitly disclaimed by `static-canonical-preflight.md`) and
  the identity half of the crawl signal (the lane held robots semantics and crawl-budget consequences,
  never crawler identity). One frontier line narrowed, one PROVINCE block added, two tier-A rows.
- **quality — improved, with a named regression repaired in-round.** The round found and corrected 10
  false quote-class labels in its own new entries and rebuilt a mirror that misrepresented its own
  state; it added a discriminating census receipt where validate alone cannot tell 143 rows from 145.
  It also landed two entries that still carry 16 over-assertions and two registry anchors that are not
  body headings — routed, not repaired.
- **discernment — improved.** Six residual seats were dispatched *after* the evidence landed and each
  attacked a committed artifact: the ledger was re-derived independently, the settlement was attacked
  with 47-of-48 and phantom-seat counterexamples, C8 was tested under three referents, and one seat
  corrected the round's own prescribed round-52 fix as unsatisfiable. The round's headline defect (the
  contaminated mirror) was found by a wave-1 seat, not by the author.

## SHONEN

- `[~]` **SKILL.md contains real decision tables, error patterns, checklists, cited sources** — bytes
  measurable (tables, S-id cites, `file:line` pins); unchanged this round; no non-author grades the
  predicate (`w1/ReviewShonen.md`).
- `[~]` **At least one end-to-end domain task executed and logged** — the GET-only live snapshot at
  `LOG.md:784/787`; unchanged this round, no non-author re-verified it.
- `[~]` **Instructions executable by an agent without oral context** — the only non-author `[x]`
  (`labrat`/`Box3Kake`, r8) is explicitly "provisional" and graded against a 313-line SKILL.md.
- `[~]` **No cross-domain bleed, PROVINCE.md still accurate** — `PROVINCE.md` § Round-51 was added this
  round and both entries were scope-checked against PROVINCE by `w1/ReviewEntryScope.md` (Frontier, not
  Core; not tabi/chousa/kagi); no verifier rules the whole file.

**Stale-lane:** this is a respawn-per-round lane; no other mission of this lane is open.

**Wave shape and seat accounting for the report record:** round total **54** seats — wave 1 **48**
(one v1 wave under `ufo-wave-policy.json`, band 32–64, validator exit 0) + residual wave-2 **6**
(4 reviewer, 1 critic, 1 scout), dispatched as a separate `task` call only after `907790c` landed.
Wave-1 role mix: reviewer 10, critic 10, executor 9, scout 6, mutation-tester 5, scribe 4, connector 1,
sentinel 1, revenger 1, simplifier 1. Dead seats: **0** (48/48 reports committed; one seat wrote its
report at 895 s and kept working, so its charge is its report mtime). The L1 holds the canonical
planner seat; the bounded planning data-walk rode the scout/connector items. Per-seat seconds are
elapsed time from dispatch to each seat's own report mtime — a re-run of the builder would print a
larger aggregate today; the committed blob is the measurement.

**Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` (no pathspec) shows no
untracked file naming kake or round-51 outside the fleet report itself; the lane's `*-shokunin/`
directories are gitignored at the fleet root, so the fleet census cannot prove anything about the lane
(`w1/ScoutMisroot.md`). No misrooted seat output was found, so nothing was copied or deleted.

**L0 questions:** none opened this round. The one decision the round could not make for itself — 
whether C1's frozen L1 sentence should gain an independence floor in round 52 — is routed as a named
defect with a measured list, not as a blocker.

**Routed defects for round 52** (each with a seat report as the pointer): C1 vacuity floor and
seat-identity binding, grant-parse binding and a labelled LOG token (`residual/ResidualSettlement.md`,
`w1/ReviewL1Accounting.md`, `w1/CriticZeroControl.md`); C2's C8 referent and `show(root, rev, MIRROR)`
form, C6 URL equality plus `httpStatus`/`bytes`/`fetchedAt`, and an entry-level quote-class condition
(`residual/ResidualC2Rerun.md`, `w1/ReviewC2Conditions.md`); C7's content-blind receipt
(`residual/ResidualMirror.md`); the entries' 16 over-assertions and the two non-heading § anchors
(`w1/ScribeEntryAudit.md`, `w1/ScribeSourcesCells.md`); the unreplayable junk controls
(`w1/ScoutCounterC1Base.md`, `w1/CriticGateCriterion.md`); concurrent writers on one lane worktree
(`w1/SentinelWriteScope.md`); the staged-id pin (`w1/CriticIds.md`).
