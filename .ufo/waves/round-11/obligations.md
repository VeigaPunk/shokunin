# PROTOCOL.md — Complete obligation inventory (round-11, lane `protocol`)

Artifact: `/home/vgpnk/projects/shokunin/PROTOCOL.md`
- Line count: `awk 'END{print NR}' PROTOCOL.md` → **583**
- Identity: `md5sum PROTOCOL.md` → `a89395757757044f2923c41a3a4ab74c`
- Sections: `grep -n '^## ' PROTOCOL.md` → Lifecycle:9, Promotion gates:34, Round-robin rounds:66,
  Evidence standard:410, File contract per shokunin repo:463, Invariants:489, Fleet-2 conventions (adopted):565
- Modal census (`grep -oi <w> PROTOCOL.md | wc -l`): must 16, never 33, required 6, only 34, may 7,
  recommended 1, allowed 3, **should 0**, forbidden 0, mandatory 0.
  → The file carries **no SHOULD-level obligations**; its softest normative forms are "may carry" /
  "Recommended" (O-65) and "allowed" (O-11). All 91 rows below are MUST/NEVER/ONLY/REQUIRED-level
  or definitional-constitutive.

Method. Every numbered row is an obligation range `[O-nn] L<start>-L<end> | text | section`.
Ranges are contiguous, non-overlapping, and jointly exhaustive with the non-normative sweep (§B).
Sentences that state a rule were kept in an O row even when they carry an embedded incident
parenthetical; pure narrative/measurement/example spans were split out into §B. Coverage is
machine-checked: O-lines 452 + N-lines 131 = **583**, gaps 0, overlaps 0.

---

## §A Obligation inventory (91 rows)

### Lifecycle (L9-32) — 4

```
[O-01] L15-19  | Shonen mints only on two unplaceable demands or operator directive; ships scoped SKILL.md, PROVINCE.md, empty LOG.md, MANIFEST record | Lifecycle
[O-02] L20-23  | Shokunin promotion requires real decision tables, cited sources, completed LOG rounds, executable without oral hand-holding | Lifecycle
[O-03] L24-26  | Jin'i-ryu promotion requires one landed falsifiable self-improvement delta logged in LOG.md | Lifecycle
[O-04] L28-32  | Shonen dormant after two dispatched rounds with no LOG.md activity; dormancy never auto-retires | Lifecycle
```

### Promotion gates (L34-64) — 5

```
[O-05] L36-37  | Every promotion gate must name its verifier and its evidence | Promotion gates
[O-06] L39-47  | Only a non-author may mark [x]; each checked box names verifier; unattributed [x] counts as [~] | Promotion gates
[O-07] L48-57  | Minimum bar: decision table, error patterns, checklist with sources; one end-to-end logged task; oral-context-free instructions; accurate PROVINCE.md | Promotion gates
[O-08] L58-59  | On promotion delete SHONEN.md, update MANIFEST rank, record review in lane report and LOG.md | Promotion gates
[O-09] L60-64  | shokunin->jin'i-ryu gate: one logged round with falsifiable improvement and its falsification condition in LOG.md | Promotion gates
```

### Round-robin rounds (L66-408) — 46

```
[O-10] L68-70   | Dispatch at most one lane per shokunin per round; undispatched shokunin is scope, never implicit no-op | Round-robin rounds
[O-11] L72-77   | Lane must not claim a round other than the steered one; skipped rounds yield no entry; duplicates allowed | Round-robin rounds
[O-12] L79-82   | Repo files win over prompts; lane re-reads protocol each steered round; superseded rules not grandfathered | Round-robin rounds
[O-13] L84-96   | Prompts must embed the operative contract verbatim; child-lane, aggregator and protocol item sets enumerated | Round-robin rounds
[O-14] L104-107 | Integrator report must carry exact corrected lane_prompt() text; scripts/ stays operator-side, never lane-edited | Round-robin rounds
[O-15] L109-114 | Rounds are per-lane counters; integrator closes round N per lane, not per fleet | Round-robin rounds
[O-16] L116-127 | Report lands after commit; must cite HEAD hash; non-ancestor hash is defect; corrections are new commits, never amend | Round-robin rounds
[O-17] L128-131 | The commit adding a lane report must carry the lane identity | Round-robin rounds
[O-18] L136-138 | Swept reports stay landed; integrator records attribution defect; uncommitted report fails the clause | Round-robin rounds
[O-19] L140-146 | Every dispatched lane writes .ufo/reports/round-<N>/<id>.md; other names fail; absence keeps round open | Round-robin rounds
[O-20] L148-152 | Report minimum content: work, evidence pointers, landed changes tied to LOG.md, cross-domain evidence, SHONEN assessment | Round-robin rounds
[O-21] L153-159 | Missing SHONEN heading voids the report as evidence; assessment must be re-filed next round | Round-robin rounds
[O-22] L161-167 | A lane terminated or respawned without filing its report is recorded failed | Round-robin rounds
[O-23] L170-176 | Mission open over two driver ticks is a stale-lane trigger; reports must list age and progressing/silent status | Round-robin rounds
[O-24] L179-182 | Progressing means lane-scope activity since launch; silent means neither a commit nor modified files | Round-robin rounds
[O-25] L185-188 | No commit is not silence; integrator records failed only for silent missions; failed is ledger act, not kill | Round-robin rounds
[O-26] L189-193 | A respawned mission resolves inherited uncommitted lane-authored changes before filing its report | Round-robin rounds
[O-27] L194-196 | No lane commits aggregator-owned files; it records them and leaves them to the aggregator | Round-robin rounds
[O-28] L200-202 | A file at the report path is not automatically a report; a contentless marker proves nothing | Round-robin rounds
[O-29] L206-209 | Report with no checkable work is a marker: recorded failed, kept as defect, counter advancement named | Round-robin rounds
[O-30] L210-212 | A short report naming a real committed hash is defective status ok, not a marker | Round-robin rounds
[O-31] L213-216 | A marker naming nothing checkable is failed whatever the lane actually did | Round-robin rounds
[O-32] L217-218 | Contract violations inside a real report stay status-neutral defects | Round-robin rounds
[O-33] L220-223 | The round's protocol lane is integrator-of-record; on prompt conflict this file wins | Round-robin rounds
[O-34] L233-239 | Integrator writes exactly three things; never edits prompts or scripts; scripts/ and .ufo/state/ stay operator-side | Round-robin rounds
[O-35] L240-243 | A protocol-lane report carrying no closure record is incomplete | Round-robin rounds
[O-36] L251-252 | Round completed when every dispatched lane reported or was recorded failed; failed counts | Round-robin rounds
[O-37] L257-260 | Closure is per lane-round: close terminated lane-rounds plus older unresolved rows | Round-robin rounds
[O-38] L263-276 | Step 1: verify commit ancestry, no uncommitted round work, SHONEN heading, prompt fidelity; record defects | Round-robin rounds
[O-39] L277-292 | Step 2: land protocol improvements, route defects including self-defects, keep durable aggregated ledger row | Round-robin rounds
[O-40] L293-296 | Step 3: mint a shonen only with two unplaceable demands or operator directive; this file beats ROADMAP drift | Round-robin rounds
[O-41] L297-303 | Step 4: append one rounds entry; statuses are ok|failed|not-dispatched|in-flight | Round-robin rounds
[O-42] L304-310 | Write partial round entries on first termination; closed_at required on any not-dispatched row | Round-robin rounds
[O-43] L311-323 | Dispatch evidence is the watchdog.log launch/steer line; committed prompt must be committed; prompt without dispatch line records failed | Round-robin rounds
[O-44] L331-333 | in-flight is decided by absence of complete line and report, never by a status probe | Round-robin rounds
[O-45] L334-338 | Round notes carry a committed digest of every dispatch/complete line a status rests on | Round-robin rounds
[O-46] L339-346 | Every in-flight row is resolved by an appended closure-correction; last row for a lane wins | Round-robin rounds
[O-47] L347-349 | No not-dispatched row against dispatch evidence; no in-flight row unless mission live at closed_at | Round-robin rounds
[O-48] L358-366 | Rows name their lane-round; lane_rounds required on not-dispatched rows; other non-ok rows cite notes | Round-robin rounds
[O-49] L367-374 | Retroactive closure entries must be typed and never read as contemporaneous passes | Round-robin rounds
[O-50] L375-379 | rounds is append-only after closure: corrections use type closure-correction and supersedes, never in-place or prepends | Round-robin rounds
[O-51] L382     | Consumers read the rounds array in order; the last row for a lane wins | Round-robin rounds
[O-52] L384-394 | Aggregator reviews every child corpus each round; corpus is its only child-repo write; commits its own files at creation | Round-robin rounds
[O-53] L395-398 | Aggregator maintains one rolling ledger, canonically .ufo/reports/AGGREGATE.md; no third path counts | Round-robin rounds
[O-54] L399-402 | While the canonical ledger is absent the integrator's round notes are the queue of record | Round-robin rounds
[O-55] L403-408 | Ledger is append-only; an aggregator report is incomplete unless the ledger was refreshed or reason named | Round-robin rounds
```

### Evidence standard (L410-461) — 10

```
[O-56] L412-415 | Evidence means a resolvable pointer; a pointerless LOG entry or unreachable claim is not evidence | Evidence standard
[O-57] L417-423 | End-to-end domain task is trigger->action->outcome->pointer; operator-owned gates accept prepared+verified+handed-off | Evidence standard
[O-58] L425-429 | Numeric claims carry their counting command; absence claims their sweep; quotes their location; capability needs a probe | Evidence standard
[O-59] L431-436 | Pointers must resolve at closure time: tmpfs paths and session-scoped artifacts are not evidence | Evidence standard
[O-60] L437-439 | Evidence timestamps must be at or before the shipping commit; future dating is a defect | Evidence standard
[O-61] L443-445 | Offered commands must be re-executed with observed output, never quoted from memory | Evidence standard
[O-62] L446-449 | Before the round's commit, grep every touched file for the superseded claim | Evidence standard
[O-63] L450-452 | Falsified claims in append-only files get a named correction entry next round, staying queued | Evidence standard
[O-64] L453-454 | Commits are cited by hash, never by subject or tag | Evidence standard
[O-65] L455-461 | Drift pins count only with expected values persisted in-repo; fingerprint printers cannot detect drift | Evidence standard
```

### File contract per shokunin repo (L463-487) — 7

```
[O-66] L467     | SKILL.md frontmatter description carries quoted triggers, an anti-trigger, and a sibling-arbitration note | File contract per shokunin repo
[O-67] L468     | PROVINCE.md declared surfaces must resolve; a moved surface is corrected and logged | File contract per shokunin repo
[O-68] L469     | LOG.md is append-only: round entries, accepted changes, falsifiable next-iterations | File contract per shokunin repo
[O-69] L470     | SHONEN.md regenerated verbatim from the template; seed must diff byte-identical; marks confined to one evidence line | File contract per shokunin repo
[O-70] L472     | corpus/ structure per CORPUS.md; aggregator reviews every child corpus each round | File contract per shokunin repo
[O-71] L473     | SCORECARD.md rows carry the counting command and measured commit so readers can re-derive | File contract per shokunin repo
[O-72] L486-487 | [~] requires an evidence pointer; [x] only with a named non-author verifier | File contract per shokunin repo
```

### Invariants (L489-562) — 15

```
[O-73] L491-492 | SKILL.md knowledge must be cited and verifiable, never generic agent advice | Invariants
[O-74] L493-499 | Contested scope is reported; integrator arbitrates in PROVINCE.md; silence never defaults scope to first writer | Invariants
[O-75] L500-501 | Every LOG.md entry cites the work that motivated it | Invariants
[O-76] L502-503 | LOG.md entries are never rewritten or deleted; corrections land as new entries | Invariants
[O-77] L504-507 | MANIFEST.json is canonical for rank and roster; only integrator roles write main-repo files | Invariants
[O-78] L508-509 | MISSION.md, AXES.md and scripts/ are operator-side; the protocol lane names but does not edit corrections | Invariants
[O-79] L510-512 | Protocol lane owns protocol/roadmap/report writes plus MANIFEST rounds appends; other MANIFEST edits stay operator-side | Invariants
[O-80] L513-517 | Lanes write only their child repo and report; main-repo lanes keep SCORECARD.md and LOG.md at root | Invariants
[O-81] L518-522 | .ufo/reports/, .ufo/waves/ and generated prompts are committed with the round; untracked prompt is non-durable | Invariants
[O-82] L523-527 | No lane commit may include .ufo/state/ or .ufo/watchdog.log; pathspec-limited commits enforce this | Invariants
[O-83] L528-529 | A meta-domain shokunin documents patterns and owns no protocol files or promotions | Invariants
[O-84] L530-541 | Domain-facing actions are operator-owned; operator-gated artifacts are not pushed; commits are pathspec-limited to own report | Invariants
[O-85] L542-549 | Round commits carry lane identity; unconfigured repos set git config once; operator-identity commits are defects | Invariants
[O-86] L550-553 | Main-repo lanes commit with explicit -c user.name/user.email, never relying on shared git config | Invariants
[O-87] L557-562 | corpus/ inherits the evidence standard; corrections are new entries; no lane edits another's corpus files | Invariants
```

### Fleet-2 conventions (adopted) (L565-583) — 4

```
[O-88] L567-574 | Each lane works one axis-move per round measured in SCORECARD.md with counting commands | Fleet-2 conventions (adopted)
[O-89] L575-576 | MISSION.md is the mission SSOT; watchdog prompts bind to it | Fleet-2 conventions (adopted)
[O-90] L577-582 | PROTOCOL.md owns process, evidence and gates, wins process conflicts with MISSION.md; neither is lane-edited | Fleet-2 conventions (adopted)
[O-91] L583     | Lanes append L0 questions to .ufo/l0-questions.md; aggregator surfaces them | Fleet-2 conventions (adopted)
```

---

## §B Non-normative sweep (54 ranges, 131 lines)

Classes: **definition** (states what a thing is), **prose** (framing/heading/blank), **measurement**
(a count/audit number), **incident-narrative** (round-<n> history/example), **example** (verbatim seed block).

```
[N-01] L1-8     | title, blockquote tagline, definition of "shokunin"                        | definition/prose
[N-02] L9-14    | "## Lifecycle" heading + mint->shonen->shokunin->jin'i-ryu diagram            | definition
[N-03] L27      | blank separator                                                               | prose
[N-04] L33      | blank separator                                                               | prose
[N-05] L34-35   | "## Promotion gates" heading + blank                                          | prose
[N-06] L38      | blank                                                                         | prose
[N-07] L65      | blank                                                                         | prose
[N-08] L66-67   | "## Round-robin rounds" heading + blank                                       | prose
[N-09] L71      | blank                                                                         | prose
[N-10] L78      | blank                                                                         | prose
[N-11] L83      | blank                                                                         | prose
[N-12] L97-103  | prompt-gap narrative: 41/45 reports missing SHONEN heading, 0/58 prompts named it (round 9: 36/40, 0/46) | incident-narrative/measurement
[N-13] L108     | blank                                                                         | prose
[N-14] L115     | blank                                                                         | prose
[N-15] L132-135 | round-10 sweep measurement: 21/21/4 reports added by 6565e89/609ecb6/0a30b44; kasegi 17:38:25 vs lane-round 17:32:47 | measurement
[N-16] L139     | blank                                                                         | prose
[N-17] L147     | blank                                                                         | prose
[N-18] L160     | blank                                                                         | prose
[N-19] L168-169 | launch-fail orphan-prompt count (0 observed as of round 10; structural)       | measurement
[N-20] L177-178 | round-10 tick counter reset (tick=13 17:32:48 -> tick=1 17:50:21; watchdog.log:117,126) | measurement
[N-21] L183-184 | commit-sparsity measurement (kumitate 39 min, kake 34 min, this lane 47 min)  | measurement
[N-22] L197-198 | round-9 aggregator mirrors uncommitted; kasegi swept c80c2a1 misattributed    | incident-narrative
[N-23] L199     | blank                                                                         | prose
[N-24] L203-205 | round-8 kengaku 101 B completion marker advanced 8->9 with HEAD f147a27      | incident-narrative
[N-25] L219     | blank                                                                         | prose
[N-26] L224-232 | rounds 2-11 produced no closure artifact; MANIFEST rounds [0,1,1.5,9]; round-9 entry rows contradicted evidence | incident-narrative
[N-27] L244-249 | protocol prompts name none of steps 1-4 (grep -c MANIFEST -> 0); rounds 2-8 produced no artifact | prose/measurement
[N-28] L250     | blank                                                                         | prose
[N-29] L253-256 | same-instant counter divergence; round 9 dispatched 17:57 vs closed 16:47     | incident-narrative/measurement
[N-30] L261-262 | blanks                                                                        | prose
[N-31] L324-330 | liveness-probe misinformation (kasegi r12, kagi r9, kake r10 still listed); lane-dead-no-report unreachable, 0/135 | incident-narrative/measurement
[N-32] L350-357 | round-9 row contradictions (kake in-flight vs 4c81066; kumitate ok; kengaku/kotoba/kagi) + round-1 kagi not-dispatched vs watchdog.log:3 | incident-narrative
[N-33] L380-381 | rounds[1] citation count: grep -rn 'rounds\[' *-shokunin | wc -l -> 13        | measurement
[N-34] L383     | blank                                                                         | prose
[N-35] L409     | blank                                                                         | prose
[N-36] L410-411 | "## Evidence standard" heading + blank                                        | prose
[N-37] L416     | blank                                                                         | prose
[N-38] L424     | blank                                                                         | prose
[N-39] L430     | blank                                                                         | prose
[N-40] L440     | blank                                                                         | prose
[N-41] L441     | "Sharpened by the round-4 audit (111 re-executed citations):"                  | prose
[N-42] L442     | blank                                                                         | prose
[N-43] L462     | blank                                                                         | prose
[N-44] L463-464 | "## File contract per shokunin repo" heading + blank                          | prose
[N-45] L465-466 | table header "| File | Purpose |" + separator                                 | prose (structure)
[N-46] L471     | AGENTS.md table row: "Operating rules when working inside this repo" (states no rule) | definition
[N-47] L474     | blank                                                                         | prose
[N-48] L475-476 | canonical SHONEN.md seed intro line ("<name> is the only substitution") + blank | prose
[N-49] L477-484 | verbatim SHONEN.md seed block (4 unchecked boxes + preamble)                  | example
[N-50] L485     | blank                                                                         | prose
[N-51] L488-490 | blank + "## Invariants" heading + blank                                       | prose
[N-52] L554-556 | round-10 lane-identity measurement: 0/60 lane-identity; 33 operator, 26 shokunin@local | measurement
[N-53] L563-564 | blanks                                                                        | prose
[N-54] L565-566 | "## Fleet-2 conventions (adopted)" heading + blank                            | prose
```

---

## §C Totals and arithmetic

| Bucket | Rows | Lines |
|---|---|---|
| Obligations (O-nn) | 91 | 452 |
| Non-normative (N-nn) | 54 | 131 |
| **Total** | **145** | **583** |

Machine check over the two range lists: `gaps: []`, `overlaps: []`, `sum == 583`.

Per-section obligation counts (by range-start line):

| Section | Line span | Obligations |
|---|---|---|
| Lifecycle | 9-32 | 4 |
| Promotion gates | 34-64 | 5 |
| Round-robin rounds | 66-408 | 46 |
| Evidence standard | 410-461 | 10 |
| File contract per shokunin repo | 463-487 | 7 |
| Invariants | 489-562 | 15 |
| Fleet-2 conventions (adopted) | 565-583 | 4 |
| **Total** | 1-583 | **91** |

Density note (counted): the `Round-robin rounds` band L66-408 is 343 of 583 lines (58.8%) —
269 normative lines across 46 obligations plus 74 non-normative lines (58 incident/measurement,
14 blank, 2 heading). File-wide the 131 non-normative lines classify as: definition 15,
blank 29, heading/blank 13, structure 2, prose 3, prose+measurement 6, incident-narrative 22,
incident+measurement 18, measurement 15, example 8 (= 131). The section is therefore a rule corpus
layered over an audit chronicle — the main structural risk for a compactor.

---

## §D Top 10 most droppable obligations

Ranked by the probability that a compactor keyed on modal verbs (MUST/never/required) deletes or
flattens them. Each entry names the phrasing defect that makes it invisible.

1. **[O-65] L455-461 — Drift pins.** Only soft modals in the whole file: "may carry", "only counts
   if", "Recommended where the surface drifts". No MUST/never. A compactor that keeps modal
   sentences drops the entire rule; the operative half ("expected values persisted inside the
   repo") is a mid-sentence condition, not a matrix row.
2. **[O-28] L200-202 — "A file at the report path is not automatically a report."** Stated as a
   definition; its only normative word is "not". Its force is fully delegated to O-29/O-31, so a
   deduplicating compactor can delete it as redundant and lose the marker/report distinction's
   statement of record.
3. **[O-04] L28-32 — Dormancy.** "is flagged dormant", "a review trigger" — no modal except "never
   an automatic retirement". Reads as a description of an integrator action rather than a duty to
   perform one; droppable without tripping a MUST scan.
4. **[O-30] L210-212 — Short-report vs marker classification.** Sentence is bracketed by incident
   prose (`round-10: kotoba 8c300ad, kumitate 7a4c9a0`) and phrased as a status verdict, not a
   rule. High risk of being folded into the neighbouring narrative.
5. **[O-36] L251-252 — Round-completed definition.** A lone definitional sentence inside a
   paragraph whose remaining lines (253-256) are narrative that a sweep will classify as
   incident/measurement; the boundary is one sentence and easily dropped with it.
6. **[O-05] L36-37 — "Every gate names its verifier and its evidence."** Two-line prose preamble
   with no modal at all; it is the meta-rule that makes O-06/O-08 enforceable, so losing it is
   silent.
7. **[O-89] L575-576 — MISSION.md SSOT.** First sentence is definition ("is the mission SSOT"),
   only the trailing six words ("Watchdog prompts bind to it") carry force; a compactor trimming
   by modal density keeps neither.
8. **[O-91] L583 — L0 side channel.** File-final single line, no modal, no section of its own;
   sits after the last blank line region and is the most likely single-line loss in a truncating
   summarizer.
9. **[O-70] L472 — corpus/ table row rule.** "reviewed by the aggregator lane every round" is a
   duty inside a descriptive table cell whose siblings (O-66/O-67/O-71 aside, `AGENTS.md` at
   N-46) are pure definitions — a compactor that treats the table as a file listing drops it.
10. **[O-45] L334-338 — Watchdog digest rule.** Buried inside a bullet whose headline subject is
    "`.ufo/watchdog.log` is mutable … line numbers drift" (narrative about drift). The actual duty
    ("the round notes carry a committed digest … that digest … is the pointer that resolves") reads
    as an explanation of the drift.

Runner-up (11th, close call): **[O-11] L72-77**, whose permissive tail "several entries for one
steered round are allowed" a compactor may treat as commentary; and **[O-83] L528-529** ("does not
own … promotions"), a negation-only rule.

---

## §E Ambiguity notes (compactor hazards beyond the top 10)

- **Definition-as-rule.** O-01/O-02/O-03, O-36, O-28 state gates/statuses as definitions. They are
  normative (they bind mint/promotion/closure) but contain no modal verb; 3 of the first 4
  obligations in the file are in this class.
- **Rule embedded in incident parenthetical.** O-02's bar is restated by O-07; O-16 (L131) and
  O-17 (L131) carry the round-10 sweep measurement inside the normative sentence, so a
  sentence-level splitter that defers to the parenthetical loses the rule.
- **Duplication across sections (dedupe bait).** "LOG.md is append-only" appears at L502-503
  (O-76), L469 (O-68), L124-127 (O-16) and L450-452 (O-63), each with a different scope: file
  contract, commit discipline, corrections, and queue retention. A compactor that dedupes to the
  shortest form loses the queue-retention nuance.
- **Bundled obligations in one bullet.** O-38 packs five distinct verification duties (ancestry,
  uncommitted work, SHONEN heading, prompt fidelity, L2 route map) into step 1; O-84 packs four
  (operator-owned actions, push gate, local-commit exception, pathspec limit) into one Invariant
  bullet. Splitting or trimming either silently removes duties.
- **Permissive/soft forms.** O-65 ("may carry", "Recommended"), O-11 ("allowed"), O-23 ("may
  record it failed") — the file uses "may" 7x and "recommended" 1x; none is MUST-level, so a
  modal-only extractor under-collects by design. Conversely "never" is used 33x, mostly as
  rhetoric inside narrative (e.g. N-26, N-31), which inflates any naive never-scan and can mask
  the real obligations.
- **Cross-file delegation.** O-13/O-14 defer to `MISSION.md` (L2 minimum, currently 8) and
  `CORPUS.md`; O-70/O-87 defer to `CORPUS.md`; O-71/O-88 defer to `AXES.md`. These numbers/rules
  are unquotable from this file alone — a compactor that keeps only PROTOCOL.md text loses the
  referenced minimum values.
- **Section membership vs scope.** O-33..O-55 are filed under `Round-robin rounds` but govern the
  integrator/aggregator lanes; a section-scoped compactor that keeps "round-robin mechanics" may
  drop the entire closure-ledger sub-machine (23 obligations, 121 lines).

---

## §F Verification of this artifact

```
awk 'END{print NR}' PROTOCOL.md                     -> 583
md5sum PROTOCOL.md                                  -> a89395757757044f2923c41a3a4ab74c
grep -n '^## ' PROTOCOL.md                          -> 9,34,66,410,463,489,565
grep -oi <modal> PROTOCOL.md | wc -l                -> must 16, never 33, required 6, only 34,
                                                       may 7, recommended 1, allowed 3, should 0
range-tiling check (O 452 + N 131)                  -> 583, gaps [], overlaps []
```
