# mado — round 31 report

Lane tip at write: `256222890d935212874a09751ff9b7869943c2d7` (pushed via
`jj-lane.sh`, `landed` printed). Base: `274f7355366d38d6e78f641ad62472e68df4686a`
(round-30 lane tip; r30's 33-seat w1 wave landed post-closure and routed its
findings here). Attempt 2: attempt 1 died pre-prompt on a Kimi 429 with no
lane work. Round 30's admission record untouched; its verdict/ledger not
rewritten.

## Work performed

Re-verified every routed r30 w1 finding against committed bytes, then repaired
them as three causally separable claims on three distinct surfaces:

- **C1 — coverage / index-row fidelity surface** (routed: CritPredicates §a,
  RevC1Rows, ScribeRowAccuracy — the fence counts name-matches over the whole
  README byte stream; a row outside the table, a 2-cell row, or a row whose
  text lies all still satisfy `43/43`). New gate
  `quality/check-index-rows.py`: each row must sit inside the coverage-map
  table, carry ≥3 non-empty cells, name only defined S-ids, cite
  repo-relative artifact paths that exist at REV (globs warn on zero
  matches), and its Holds cell must share ≥5 words with the note it names.
  Found a real defect the fence could not see: `animation-table-r26.md`'s
  row carries 2 cells (Sources folded into Holds) — repaired.
- **C2 — calibration / resolved-citation rubric v2** (lowest active sub-axis
  at base: resolved-active 0.9750 vs 1.0 elsewhere; routed: RevC2Counter S8,
  CritKillRules K2, RevC2Supersede, CritPredicates §b).
  `.ufo/waves/round-31/c2/count.py` replaces existence/word-presence with
  resolution: `file#anchor` must resolve to a GitHub-slugged heading *in the
  named file* (the r30 S8 miss — `M23-7` cited under `#mistakes` while living
  under `### Final C1 disposition` — now fails as UNRESOLVED at base); the
  spell form `lesson round<N> M<M>` must appear in that file's bytes; a bare
  `lessons/round-<num>.md` counts only if the file exists and is non-empty;
  `outside X` corroborates but never grounds alone; `active ≥ ACTIVE_MIN(30)`
  floors the denominator against a `Supersedes criteria 1-40` drain.
- **C3 — operability / gate robustness** (routed: RevC3Gate L1/L4/H1,
  RevC1Fence, MutC3Gate, SentScope F2/F5, CritCausal). `check-index.py`:
  `--rev` resolved once through `git rev-parse --verify --end-of-options`
  (a crafted `--rev=--output=…` can never reach a `git show` write path);
  `--root` refuses symlinked `corpus/` ancestors by realpath containment;
  `--repo` under `--root` is SETUP_ERROR instead of silently ignored;
  selftest 9 → 12 assertions covering the three routed findings.

## Measurements (all re-run at write time; committed bytes only)

| Claim | Before (`274f7355`) | After (`f621e3c0` / tip `25622288`) | Command |
|---|---|---|---|
| C1 | `MADO_INDEX_ROWS: rows=43 errors=1` — `row-cells: knowledge/animation-table-r26.md … 2 cells`, exit 1 | `rows=43 errors=0`, exit 0 (3 glob WARN — ephemeral r12/r24 evidence) | `python3 -I quality/check-index-rows.py --rev REV --repo .`; `--selftest` 10/10 |
| C2 | `literal 40/52 = 0.7692, resolved_active 39/40, UNRESOLVED criterion 35`, TARGET_MISSED | `literal 42/54 = 0.7778, resolved_active 41/41 = 1.0000`, TARGET_MET | `python3 -I .ufo/waves/round-31/c2/count.py REV` |
| C3 | `indexed=43/43`, selftest 9/9 | `indexed=43/43` at base AND tip, selftest `12/12 assertions passed` | `python3 -I quality/check-index.py --rev REV --repo .` / `--selftest` |

Negative controls (committed under `.ufo/waves/round-31/c2/negative/`,
receipts reproducible with `--active-min 2`): n1-empty → UNRESOLVED
(empty file); n2-wrongfile → TARGET_MET — *existence is the rubric, relevance
is out of scope; routed forward as a residual cheat*; n3-section →
UNRESOLVED (wrong-section id); n4-collapse → FLOOR_VIOLATION
(supersede-all drains below 30).

Kill rules (frozen verbatim in `registration.md`): K1 any ERROR nonzero |
errors=0 on an out-of-table/<3-cell control; K2 any UNRESOLVED among active
| literal < 0.70 | supersede-all draining active < 30; K3 any of the 12
assertions failing | a mutated control printing the clean PASS. No kill
rule fired on the reported controls.

## Causal separability

- C1 reads `corpus/README.md` + `corpus/knowledge/` only; reverting the C2
  QUALITY edits or the C3 gate edits leaves C1's receipts byte-identical
  (same base-red, same tip-green). CritCausal's r30 finding (C3 green depended
  on C1's README change) does not recur: C3's `43/43` is green at *both*
  revisions — the README repair under C1 removed the gate's input defect but
  C3's verdict is computed on the note set + index rows, which were complete
  in both states; each claim's predicate holds with the other two reverted.
- C2 reads `corpus/QUALITY.md` + `corpus/lessons/` only — independent of
  README rows and gate bytes.
- C3 reads the gate script and corpus tree; its new assertions exercise
  `/tmp` fixtures only.

## Integrity notes

- The 33 r30 w1 wave reports + `swarm-registry.json` are untracked
  orchestrator-dispatched artifacts; preserved, never committed by this lane
  (worktree diffs against them predate this round — e.g. the r30 sibling's
  RevC1Fence/SentScope/RevRecordsChain edits — and remain).
- `quality/q36-successor-receipts.txt` untouched; peer-reported restored to
  HEAD (`git diff HEAD -- quality/q36-successor-receipts.txt` empty).
- Misroot sweep at fleet root: only `mado-shokunin/`; clean.
- No `corpus/knowledge/`, `tools/`, `SKILL.md`, `PROVINCE.md` byte changes;
  no compositor/config mutation; no installs this round.
- Wave: `.ufo/waves/round-31/w1-spec.json` (15 seats: reruns, scribes,
  critic falsifiers, reviewers, mutants, sentinel, scouts) — PREPARED, not
  dispatched; this seat has no swarm-dispatch tool (expected host surface).

## Residual cheats routed forward

1. `outside`-only grounding: criteria 19/22/23/26/28 resolve via
   `outside` corroboration alone — WARN now; the w1 reviewer seats attack it.
2. Relevance-free resolution (n2): a lesson whose content contradicts its
   criterion still resolves; resolution is syntactic.
3. Holds overlap ≥5 words is a proxy; a row can paraphrase the wrong note.
4. `.ufo/waves/round-24/fetch/S###.bin` convention — glob with `#` digits;
   WARNed on zero match at tip (ephemeral r24 dir).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — asserted: SKILL.md byte-unchanged this round
  (`git diff 274f7355 25622288 -- SKILL.md` empty); no SKILL work claimed.
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  asserted: LOG.md round-31 entry (row-fidelity gate, resolved-citation
  counter v2, gate hardening, with committed receipts at named revisions).
- [~] Instructions executable by an agent without oral context — asserted:
  all three counters/gates ran end-to-end from committed bytes at named
  revisions (`--rev 274f7355` / `25622288`) with the transcripts above.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — asserted:
  `git diff 274f7355 25622288 -- PROVINCE.md SKILL.md` empty; the two
  `quality/` checkers are lane-internal gates (same class as the existing
  `quality/` fleet tools; no new province surface); no sibling/fleet writes
  (misroot sweep clean; only `mado-shokunin/` at fleet root).

No `[x]`: every box lacks a named non-author verifier on record this round;
the prepared w1 wave's reviewer seats are the candidate verifiers.

## Round shape, waves, seats

Shape: **three-claim repair round on the routed r30-w1 defects with a
prepared wave** (default shape). Round total: **15 prepared seats, 0
dispatched, 0 dead** — below the live swarm floor; the orchestrator
validates and records that boundary (this seat has no dispatch tool).

- Wave 1 (prepared): 15 seats — executors 4 (ExecC1Rerun, ExecC2Rerun,
  ExecC3Rerun, ExecCensusRerun), scribes 2 (ScribeCriteria, ScribeRecords),
  critics 2 (CritPredicates, CritKillRules), reviewers 3 (RevC1Rows,
  RevC2Resolution, RevC3Gate), mutation-tester 1 (MutGates), sentinel 1
  (SentScope), scouts 1 (ScoutAxisTable), revenger 1 (RevengerRowGap). Spec
  `.ufo/waves/round-31/w1-spec.json` at `72021ded`.
