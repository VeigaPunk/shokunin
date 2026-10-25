# mado — round 36 report

Lane: `mado-shokunin` (desktop & compositor craft). Round **36**, attempt 1.
Prompt: `.ufo/prompts/mado-round-36.md`. Base: `4243d031e3441f5063f92c33aa58377c6f9ff120`
(the round-35 verifier spot-check commit). Freeze: `dbf8b579aeac0f023aaf595770f1cb0049e4baa2`.
Lane tip when this report was written: `64979efb7f95acc67e753c642294c41a4d102bfa`.

## Work performed

**Declared claims — 2, frozen before any round-36 data**
(`mado-shokunin/.ufo/waves/round-36/registration.md`).

- **C1 — calibration** (one of the two axes tied at the lowest published score). The two
  round-35 admission counters are repaired as standing tools and **shown to discriminate**
  over a frozen 25-control manifest: 3 accept controls (the lane, a registry-shaped copy of
  it, the live clause ledger) and 22 reject controls (14 `c1` cribs, 8 `c2` mutation
  fixtures). Target `correct == controls`; before **14/25**, after **25/25**. Closes
  spot-check D3 (a receipt digest computed and discarded) and D4 (a self-authored, fail-open
  evidence ledger).
- **C2 — operability** (the other tied-lowest axis). The lane's own records pass an
  evidence-pointer durability gate (`PRED-PTR-r36-v1`): every pointer a round's records cite
  resolves at the committed revision, every round-35 dangling pointer is closed by a
  correction pair whose replacement resolves, the inherited uncommitted set is empty, the
  round-35 scratch tree carries a counted disposition, and a tip-revision axis transcript is
  committed. Before `TARGET_MISSED`, after `TARGET_MET`. Closes D2, D5, D8 and D10.

**Work items, each with its evidence pointer.**

- Freeze commit `dbf8b57`: registration with both predicate texts, both frozen specs
  (`.ufo/waves/round-36/c1/frozen.json`, `.ufo/waves/round-36/c2/frozen.json`), the control
  manifest, two new crib trees, the two gates, the fixture generator, and the two before
  receipts (`receipts/before-discrimination.txt` → `correct=14/25`,
  `receipts/before-pointers.txt` → `TARGET_MISSED`).
- Data commit `a3094c9`: `quality/counters/c1-idle-lock.py` (`PRED-C1-r36-v1`) and
  `quality/counters/c2-ledger.py` (`PRED-C2-r36-v1`); the round-36 clause ledger and blob
  ledger; 25 discrimination receipts under `.ufo/waves/round-36/controls/receipts/`; the
  clause-attribution receipt; the S211 fetch receipt; `corpus/lessons/round-36.md`;
  `corpus/QUALITY.md` criteria 57–61; the S211 registry row; the PROVINCE instrument
  paragraph; the wave spec, the validator's task-call payload and 64 seat prompts.
- Records commits `520c631`, `ebc5437`, `c5d7773`, `cf175c7`, `2d90524`: the LOG entry and its
  corrections, the scorecard rows, the D9 boundary ruling in `PROVINCE.md`, the red and green
  axis transcripts, and the wave-1 reports.
- **C1 evidence, measured.** The before run's eleven wrong controls are exactly the classes
  the spot-check routed: `c1-shape-only` and `c1-fabricated-payload` (a computed-but-unused
  digest), `c1-no-registry-heading` and `c1-row-moved-out` (a whole-file row scan), and seven
  of the eight `c2` mutants (a self-authored clause list, token-grep receipts, a prose
  tip test, and a document table the old counter never parsed). The after run classifies all
  25 correctly and still accepts the live bytes and the registry-shaped copy.
- **C1 attacked by the wave.** An always-rejecting instrument scores **23/25** and is killed
  by the two `c1` accept controls; the accept-all twin scores 11/25, killed by all fourteen
  rejects, and the two degenerates' correct sets are disjoint — no subset they share reaches
  the target (`w1/reports/MutC1RejectAll.md`, `w1/reports/MutC1AcceptAll.md`: 23/25 and 11/25,
  each killed on its own accept/reject side). A line-faithful port of the round-35 tip logic
  **survives 4/4** of the `c2` mutation fixtures that the round-36 rule kills
  (`w1/reports/MutC2HardcodedTip.md`). The tip rule was then audited independently: the computed
  tip is the same hash, the ledger carries four tip lines, all seven rows re-derive, and a
  document that launders the exemption on every tip line forfeits the three-line minimum and is
  rejected before its table is read (`w1/reports/RevTipRule.md`). Clause attribution was proved separately: the ten
  inherited cribs are fence-first under the new counter, so each was re-scored from a copy
  with only the fence restored and still dies on its own clause
  (`receipts/clause-attribution.txt`).
- **C2 evidence, measured.** `receipts/after-pointers.txt` at `cf175c7`:
  `dangling_r35_closed=1 dangling_r36=0 inherited_dirty=0 scratch_tracked=124
  scratch_disposition_ok=1 tip_axis_transcript=1 setup=ok verdict=TARGET_MET`, exit 0.
- **D2** resolved: the eight modified round-35 seat reports and
  `.ufo/waves/round-35/scratch-evidence/RevEntryR12/evidence.txt` were rewritten from the
  branch (the bytes the spot-check examined) and the two untracked probe directories under
  `.ufo/waves/round-35/scratch/` were removed — their receipts are the evidence.
- **D5** closed by a correction pair, not a record edit (`record_intact` refuses the edit);
  the pair is in `LOG.md`'s round-36 section in the gate's machine form.
- **D8** closed by a counted disposition in the lesson (`tracked paths=124`).
- **D9** closed twice over: the refusal boundary is now **stated** in `PROVINCE.md`
  (round-36 refinement: the localized documentation channel out, the English config-plane
  channels in, the omarchy skill's own files read-only) — `w1/reports/CritD9Boundary.md`
  showed it was practised in four rounds of lessons and stated nowhere — and the provenance
  convention is counted (29 of 50 knowledge notes carry the trio in their first 15 lines; 20
  carry none anywhere) with an append-only normalization ruling
  (`w1/reports/ScoutD9Provenance.md`).
- **D10** closed by `quality/receipts/axis-520c631…txt` (green, `MADO_AXIS: checked=3
  mismatched=0`) with its red half `quality/receipts/red-axis-publication-stale-at-data-commit.txt`
  (`mismatched=1` at the data commit before the publication landed).
- **Frontier step**: one row, S211, opened 2026-10-25 and independently re-opened by a second
  seat with a stronger anchor (`w1/reports/ScoutPriorArt.md`); its anchor cell was corrected
  in place and the correction logged in the lesson's Gate.
- **A defect a seat found in my own freeze**: the registration's harm-watch command
  `quality/check-index.py --repo .` exits 2 as written (`SETUP_ERROR: --rev or --root is
  required`) — `w1/reports/RevIndexGate.md`. Recorded as M36-6 with criterion 61.
- **Host harm watch**: fifteen declared config files hashed read-only with zero new drift;
  every sha-pinned plane matches its latest lane pin, and two stale *citations* (the
  pre-gkeep `hyprland.conf` hash still quoted in `SKILL.md`, and walker 2.17.2 installed
  against the 2.17.0 pin already ledgered in round 19) are reported as findings that were
  already recorded, not new drift (`w1/reports/ScoutHostProbe.md`).
- **Harm watch**: `MADO_SELFTEST: 460/460 assertions passed` with the gate blob
  byte-identical to the round-35 tip (`w1/reports/RevSelftest.md`); index `50/50`
  (`w1/reports/RevIndexGate.md`), `MADO_AXIS: checked=3 mismatched=0`
  (`w1/reports/RevAxisNow.md`), registry rows untouched since the round-35 tip
  (`w1/reports/RevRowsUnchanged.md`), census exit 0 with the same seven pre-existing `W04`
  warnings (`w1/reports/RevCensusNow.md`).

### Adjacency and inherited defects (reported, not absorbed)

- **Adjacency, from `w1/reports/ConnOverlap.md`.** No sibling disputes either claim, but two
  ownership lines bind them: the mutation *method* is `tameshi-shokunin`'s, so the fixture
  generator and the discrimination gate stay lane-internal and are never offered as a reusable
  harness; and the pointer-audit *instrument class* already exists at `kaidoku`, `kagi` and
  `chousa`, so C2's claim is "mado's own records pass this gate", not new ground. Both
  boundaries are now written into the scorecard's capability rows.
- **An inherited gate defect, routed not patched.** `quality/check-index-rows.py`'s rev-mode
  `exists_glob` passes `--name-only` with `--format` to `git ls-tree`, which host git 2.56.0
  rejects; the error is swallowed and every glob citation in rev mode warns spuriously
  (`w1/reports/RevIndexGate.md`, three false positives named and checked against the tree).
  Warnings do not fail the gate, so nothing this round claimed rests on it; the repair is a
  declared item for round 37 (criterion 52: a sweep that finds an inherited defect records and
  routes it, it does not patch it inside the discovering round).

- **The frozen manifest does not exercise the digest clause's anchor half.** A wave mutant that
  deletes the anchor-cell test survives at 25/25, because every `c1` reject crib dies at the
  `row-in-registry` fence before the digest clauses are reached; with the fence restored, the
  bytes binding alone kills the fabricated-payload tree, and the anchor test is the sole guard
  for a tree whose receipts are genuine but whose anchor cell is prose
  (`w1/reports/MutC1CheckAnchor.md`). So `digest-match`'s two halves are proven by
  fence-restored probes, not by a frozen control — stated here rather than left in the table.
- **Three seats attacked the gates' own verdict logic and all three are load-bearing**: the
  `setup_ok` conjunct (a mutant that drops it exits 0 on a tree with no round-36 sections —
  `w1/reports/MutPtrNoSetup.md`), the `tracked paths=N` equality (a wrong count passes without
  it — `w1/reports/MutPtrDisposition.md`), the ancestor plus `rev=` checks on the transcript
  (`w1/reports/MutPtrTipAncestor.md`), and the clause/control receipt binding (a token grep
  lets 2 of 8 frozen rejects pass — `w1/reports/MutC2NoReceiptBind.md`); dropping the document
  table parse lets `c2-blob-corrupt` and `c2-blob-row-deleted` pass
  (`w1/reports/MutC2NoTable.md`).
- **The gate trusts its inputs.** A trimmed manifest, or a manifest whose expectations are
  echoed by a stub, reaches the target: the gate binds no identity between the manifest it
  scores and the frozen one it was registered with (`w1/reports/LabratGateOracle.md`, B2/A3).
  The receipts now carry the manifest's sha256, so a substituted manifest is visible to a
  reader; binding it inside the gate is routed to round 37.
- **Nine of the fourteen `c1` rejects exercise the fence, not their clause.** A seat showed
  that deleting any one repaired `c1` clause except the fence leaves the manifest at 16/16, and
  that the unmodified round-35 counter plus only the section rule also scores 16/16
  (`w1/reports/RevAfterC1.md` F1). The digest repair is therefore proven by the fence-restored
  probes (a one-byte-flipped receipt: round-35 `MET`, round-36 `MISSED`; the anchor test's own
  kill flips under the mutant), not by the frozen manifest — the scorecard's C1 row says so.
- **A security review found the gates' own hygiene gaps** — ambient `GIT_*` inherited into
  every child git call (a spoofed `GIT_DIR` could fake C2), a receipt filename taken from a
  manifest id without validation, and a generator join without containment
  (`w1/reports/SentGateExec.md`). The `GIT_*` scrub, the id validation and the pair-target
  validation landed in `ea89bde`; the remaining traversal and `/tmp`-race items are routed.
- **Causality, corrected after review.** A critic found the scorecard's original sentence
  ("neither reads the other's output") false at the *record* level: the round-36 records cite
  C1's artifacts, so C2 needs them to exist, though not to be correct. The scorecard now says
  exactly that; a second critic confirmed the two *verdicts* are independent in both
  directions (`w1/reports/CritSeparability.md` under the wave scratch tree).

### Findings that limit the claims (stated, not hidden)

- The tip-transcript observable is a three-substring test over a committed file, so a
  hand-authored transcript would conform (`w1/reports/RevAxisTranscriptAsk.md`, F1). The
  other four C2 observables do not read that file. Routed to round 37 as a hardening.
- The discrimination gate does not enforce exit-code/verdict coherence: an instrument that
  printed `TARGET_MET` and exited 1 would be scored `MET` (`w1/reports/ConnGateReuse.md`).
  Routed, not silently changed — the predicate was frozen before data.
- The manifest's control order is load-bearing (the `c2` fixtures embed the gate's own `c1`
  receipts) and that dependency is undocumented in the gate. Named here and routed.
- The pointer gate gained its supersede exemption (pointers written as the `old` side of a
  correction pair are named, not cited) after the freeze and before any after-state
  measurement; **both** receipts were produced with that revision, and it is behaviour-neutral
  for the before state, which short-circuits at `setup=missing-r36-sections`. The gate bytes
  are committed (`a5f76c9`) so the receipt's revision and the bytes agree.
- The axis publication's own anchor commit is never checked — the gate compares numbers, not
  the sha the prose names — and the gate reads the *committed* card, so a dirty tree is
  invisible to it (`w1/reports/MutPublication.md` F-1/F-2). Both are routed, not hidden.
- Two scorecard defects this wave found are fixed, not papered over: the publication named the
  data commit as its anchor while `48/48` first derives at the records commit (now anchored at
  `520c631`, with the red receipt showing the `47/47` state), and `## Retired` still read "none"
  while the round-36 section retired `sourced-art` (now a dated `## Retired` bullet).
- The S211 receipt's `fetched_sha256` is not a stable identity: the page carries two rotating
  tokens, so three consecutive fetches give three HTML hashes at an invariant 150,283 bytes
  while the text is byte-identical. Both quotes were re-checked contiguous in a fresh
  extraction, and the receipt now records the extraction digest as its identity
  (`w1/reports/RevSourceS211.md`).
- The clause-attribution probe shows a crib dies with exactly one cite open, not *which*
  conjunct closed it; the attribution therefore rests on the probe plus the wave's per-clause
  drop mutants, not on the probe alone (lesson M36-3).

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Round-36 freeze: registration, both specs, the manifest, two crib trees, the two gates, the generator, the before receipts | round-36 | `dbf8b57` |
| The repaired counters, both round-36 ledgers, 25 discrimination receipts, the clause-attribution receipt, the S211 fetch receipt, the lesson, four criteria, the S211 row, the PROVINCE instrument paragraph, the wave spec/prompts | round-36 | `a3094c9` |
| The records: LOG entry, scorecard rows, the D9 boundary ruling, the sixth mistake, nine wave-1 reports, the red axis receipt | round-36 | `520c631` |
| The green tip-revision axis transcript; two LOG corrections | round-36 (corrections) | `ebc5437` |
| The superseded transcript pointer in machine form; further wave-1 reports | round-36 | `c5d7773` |
| The D9 census in the lesson, decoupled from a pending seat report | round-36 | `cf175c7` |
| The after receipts, the measured-at block, the round-37 plan, the S211 corroboration | round-36 | `2d90524` |
| The wave's hardening — census-parity fence, exit/verdict coherence, `GIT_*` scrub, pair-target validation, supersession owed at zero dangling, negated dispositions rejected — and 40+ wave reports | round-36 | `ea89bde` |
| The after receipts re-pinned to the hardened tip with the gate, manifest and spec digests bound | round-36 | `64979ef` |

## Before → after measurements

**C1 — counter discrimination.**

```sh
cd /home/vgpnk/Projects/shokunin/mado-shokunin
python3 -I quality/check-counter-discrimination.py --profile r35 \
  --manifest .ufo/waves/round-36/controls/manifest.json \
  --receipts .ufo/waves/round-36/controls/receipts-r35      # before
python3 -I quality/check-counter-discrimination.py --profile r36 \
  --manifest .ufo/waves/round-36/controls/manifest.json \
  --receipts .ufo/waves/round-36/controls/receipts          # after
```

- before, at `4243d03` (`receipts/before-discrimination.txt`):
  `MADO_DISCRIMINATION: profile=r35 instruments=c1,c2 controls=25 correct=14/25 verdict=TARGET_MISSED`,
  exit 1.
- after, at `64979efb7f95acc67e753c642294c41a4d102bfa` (`receipts/after-discrimination.txt`, which binds the gate, manifest and both frozen specs by sha256):
  `MADO_DISCRIMINATION: profile=r36 instruments=c1,c2 controls=25 correct=25/25 verdict=TARGET_MET`,
  exit 0.

**C2 — evidence-pointer durability.**

```sh
cd /home/vgpnk/Projects/shokunin/mado-shokunin
python3 -I quality/check-evidence-pointers.py --rev <rev>
```

- before, at `4243d03` (`receipts/before-pointers.txt`): `dangling_r35=2
  dangling_r35_closed=0 scratch_disposition_ok=0 tip_axis_transcript=0
  setup=missing-r36-sections verdict=TARGET_MISSED`, exit 1. The receipt's header records
  `inherited_dirty=10` from the live work tree at 04:31 — a work-tree reading the re-run
  cannot reproduce once the ten paths are resolved, and it says so instead of dropping it.
- after, at `64979efb7f95acc67e753c642294c41a4d102bfa` (`receipts/after-pointers.txt`, which binds the gate blob by sha256):
  `dangling_r35=2 dangling_r35_closed=1 dangling_r36=0 inherited_dirty=0 scratch_tracked=124
  scratch_disposition_ok=1 tip_axis_transcript=1 setup=ok verdict=TARGET_MET`, exit 0.

## Sources & frontier

`SOURCES.md` rows **200 → 201**; one row added, tier **A**; rows touched old→new: **one
cell** — S211's `anchor` was corrected in place from "Introduction, the Jackson example" to
`#S2 … paragraph #P15`, logged old→new in the lesson's `## Gate`. No `status`, `recheck` or
`used-by` change. Counting command, exit **0** before and after:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado
```

- **S211** — negative controls in observational studies
  (`https://pmc.ncbi.nlm.nih.gov/articles/PMC3053408/`, opened 2026-10-25, receipt
  `mado-shokunin/.ufo/waves/round-36/fetch/S211.receipt.txt`): 17-word located quote in the
  lesson's `## Gate`, plus a 22-word definitional quote located and independently verified by
  a second seat at `#S1`/`#P8`. It grounds C1's reject half: an apparent effect where the
  claimed cause is impossible is instrument failure.
- Frontier rows advanced: **none on the domain plane** — this round advances the lane's
  instrument plane (two counters, two gates) and says so. Domain-versus-meta ratio for the
  last 30 commits: **3 / 27**, independently re-derived by a scribe seat as 3 of 30 with the
  longest record-only streak at 20 commits (criterion 60's forcing function already has a
  reading).
- **Assimilation: none this round** (registered before data; round 35 adopted the package's
  core theme and its evidence chain is what this round repairs).
- **considerthese**: `considerthese/2026-10-24.md` proposal 1 (domain-versus-meta ratio)
  landed as `QUALITY.md` criterion 60 plus this report's ratio line, grounded in counts
  re-derived from the lane's own commits (lesson M36-5).

## Trend verdicts

- **expansion: unchanged.** No domain knowledge admitted, no coverage ground claimed. One
  grounding row for a method the round uses is curation, not expansion; calling it expansion
  would be the "re-scoring on new inputs is coverage" error the fleet lesson names.
- **quality: improved.** Two instruments that could not tell work from shape now can
  (14/25 → 25/25 on 25 frozen controls, live bytes still accepted); the records pass a
  pointer gate for the first time; six mistakes are mined with fixes shown able to fail; six
  criteria (57–61) and M36-6 came out of them. Harm watch green (suite 460/460, gate blob
  unchanged, index 50/50, census exit 0).
- **discernment: improved, with named limits.** The lane's own instruments are now attacked by
  committed controls rather than asserted, a wave seat's finding against my freeze became a
  criterion in the same round, and the round refuses to dress meta work as expansion. The
  limits are listed above (three-substring transcript, no exit/verdict coherence, undocumented
  control ordering).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer `SHONEN.md:3`; unchanged this round, and no non-author promotion review exists, so the lane's own assertion stands as `[~]`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — historical pointer `corpus/knowledge/config-health-report-r3.md` and `LOG.md` round 3; this round ran no desktop task, and says so rather than counting a seat's probe as one.
- [~] Instructions executable by an agent without oral context — pointer `SHONEN.md:7`; this round's 70 seats were executed from 64 committed prompt files with no oral context, which is evidence *inside* the lane, not outside-lane independence.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer `PROVINCE.md` round-36 refinements (two tool-plane paragraphs, one refusal-boundary sentence); no sibling lane's ground is absorbed and no desktop write surface is added.

## Round shape, waves and seats

- **Wave 1: 64 seats, one batched `task` call** built from the validator's payload
  (`mado-shokunin/.ufo/waves/round-36/w1-taskcall.json`, `counts {spawn: 64, resume: 0,
  total: 64}`, policy v1 band 32–64). Role mix: reviewer 17, mutation-tester 13, scout 12,
  executor 5, scribe 5, critic 5, sentinel 2, connector 2, simplifier 2, revenger 1. Seat
  prompts committed under `.ufo/waves/round-36/w1/prompts/`; reports under
  `.ufo/waves/round-36/w1/reports/`.
- **Residual attack pass: 6 seats in one ordinary `task` call** (reviewer 4, critic 1,
  mutation-tester 1) against the landed measurements, because wave 1 could not attack numbers
  that did not exist when it was dispatched.
- Planner seat: held by the L1 (the validator rejects `planner`); the planning data-walk rode
  the `connector` and `scout` items.
- Round total: **70 seats**. Reports committed: **46 seat reports** (wave 1 plus the residual
  pass), committed under `.ufo/waves/round-36/w1/reports/`. Dead seats: **none reported** — every
  dispatched seat either filed a report or was still running when the round closed, and no seat
  was replaced (the last few in flight are named here rather than quietly dropped: the round
  closed on `64979ef`, and any report not in that commit is not claimed).

## Routed defects from the round-35 closure (D1–D10)

| Defect | Disposition | Artifact |
|---|---|---|
| D1 report-lands-last and tip citation | erratum below; this report lands after the last lane commit and cites it | this report |
| D2 uncommitted round work at closure | resolved — eight files rewritten from the branch, two untracked probe dirs removed | `LOG.md` round-36; `inherited_dirty=0` |
| D3 C1 counter shape-scored | **claim C1** — digest bound to the bytes read; the content cribs are committed controls | `quality/counters/c1-idle-lock.py` |
| D4 C2 observables fail-open | **claim C1** — clause set pinned, receipts bound to clause and control, tip computed by one rule, the document's table parsed | `quality/counters/c2-ledger.py` |
| D5 dangling evidence pointers in LOG | correction pair, record untouched | `LOG.md` round-36 |
| D6 wrong correction count | erratum below, re-derived | this report |
| D7 stale seat-report count | erratum below, re-derived per revision | this report |
| D8 cleanup claim vs committed bytes | counted disposition | lesson § Scratch disposition |
| D9 provenance trio and refusal boundary | boundary now stated in PROVINCE.md; convention counted with an append-only ruling | `PROVINCE.md`, lesson |
| D10 tip-revision axis transcript | green transcript + red half | `quality/receipts/` |

### Errata owed to the round-35 report (append-only; its filed bytes are not rewritten)

- **D1.** The round-35 lane tip is `7a068cbee3b0983230b8fb8467c02e12772832dd`; the round-35
  report's last fleet commit preceded three further lane commits and its text declined to name
  a hash. This round names the tip and lands last.
- **D6.** The round-35 report's Sources & frontier says "four of the new rows'
  `scope`/`teaches` cells were corrected"; the committed bytes show **three** rows (S203,
  S204, S205) and **six** cells — `teaches` ×3, `recheck` ×2, `scope` ×1
  (`git diff --numstat 02088b4 7a068cb -- corpus/SOURCES.md` → `3 3`; re-derived in
  `w1/reports/ScoutD6Rows.md`). `SCORECARD.md` already carried "three".
- **D7.** The round-35 report's Work-performed bullet says "(38 reports)"; re-derived counts
  are **37** at `4f35c80`, **37** at `7b745a1`, **40** at `7a068cb`. 38 was never a committed
  state — the stale figure was a pre-commit tally carried through all nine report versions
  (`w1/reports/ScoutD7Counts.md`).

## Post-report lane commit (correction line; append-only)

One lane commit follows the tip this report cites: `4bac2163ac0fc3dd55e806947597a11596885139`
carries the last two seat artifacts produced before closure (a critic's manuscript-balance report
and a scratch tree). `64979efb7f95acc67e753c642294c41a4d102bfa`, the tip named above, remains an
ancestor, and no file this report cites changed in it. `CritManifestBalance` confirms the
manifest-substitution hole named in the limits: a trimmed or rewritten manifest reaches 25/25
with the unmodified round-35 counters, which is why both receipts now carry the manifest's
sha256.

## Second post-report lane commit (append-only)

Two further lane commits followed, each carrying only wave output or a gate hardening, never a
file this report cites by content:

- `4bac216` — the last two straggler seat artifacts.
- `4d28b19` — two fail-opens a critic closed at the end of the wave: the discrimination gate now
  binds the manifest's id, its control-id set and every control's expectation to the frozen
  manifest (a trimmed or rewritten manifest dies `manifest-control-set-drift`, proven), and the
  pointer gate fails closed (`error=git-status-unusable`, exit 1) when `git status` cannot
  answer, instead of reading an unmeasurable tree as clean (proven on a bare clone).
- `fe55a90` — the after receipts re-pinned to `4d28b19` with the gate digests bound.

Lane tip at closure: `fe55a90ca4d16c1929bb3832c73396fd0170f2f1`, working tree clean. The tip
this report cites (`64979ef`) and the round's data commit (`a3094c9`) are ancestors.

## Stale-lane

Respawn-per-round driver; this lane-round ran well inside two driver ticks and no other
mission of this lane is open.

## Tool installs

None. No seat reported an install; the source work used `curl` against the publisher's own
page. Pacman stayed paused for the whole round; no package transaction of any kind was run.
