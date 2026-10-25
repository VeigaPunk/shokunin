# chousa round 39 — capture bash pin + verifier/subject receipt binding

Lane: chousa (deep-research method). Round 39, attempt 1. Landed lane tip
`6ac1007e6a5d699d0742801026554fac1d900b5d` (jj-lane `landed` line; work
commit `6d914e95…`). Host mapping: this seat holds no live L2 dispatch tool
(accepted across seats 2026-10-24) — the round's swarm is PREPARED and
validated under `.ufo/waves/round-39/` for the orchestrator to dispatch
between rounds; the L1's own construction runs supply the committed
measurement evidence, disclosed as such in the frozen claims.

## Work performed

Declared claims (2, distinct axes, both from the round-38 closure's routed
list — Errata 5/6/11 cells and defect D7):

1. **C1 — operability (lowest scored axis, 3/10):** the canonical pin
   capture's grandchild AND the verify-all section children run through ONE
   pinned absolute `bash` (`RESEARCH_GATE_BASH` override, GNU-reporting,
   refused exit 2 `BASH_PROVENANCE` before any mode runs), so a caller PATH
   `bash` shim cannot interpose (echo re-add / suppress / hostile drift).
2. **C2 — calibration:** round-39 receipts bind `verifier_sha256` and
   `subject_counter_sha256`; the verifier re-derives both with named
   refusals (the r38 Erratum 2/11 debt, demonstrated live twice).

- **C1 gate work** — `bash_pin_init` + capture/section call-site pins in
  `tools/research-gate.sh` (`git diff 8c7c867 6d914e95 -- tools/research-gate.sh`);
  selftest cases 273–275. Evidence: `RESEARCH_GATE_SELFTEST: PASS (275 cases,
  0 skipped)` (re-run at report time on the landed bytes).
- **C1 counter** — `corpus/evidence/round39/c1-count.py`: the round-38 seven
  scenarios + eighth family `capture-bash-path-pin` (five cells: PATH bash
  shim echo/suppress, PATH env shim hold, override honoured, relative
  override refused). Evidence: receipts `c1-after-s39011.json`,
  `c1-after-s39111.json` (8/8, `VERIFY: ok`), base `7/8`
  (`c1-base-s39001.json`), mutant `4/8` (`c1-mutenv-s39013.json`).
- **C2 counters + verifier** — `corpus/evidence/round39/{c2-count.py,
  verify-receipts.py}`: family-specific required bindings, named refusal
  labels, census/expect/ok re-derivation kept from r38. Evidence: receipts
  `c2-after-s39101.json`, `c2-after-s39121.json` (8/8, `VERIFY: ok`;
  `verifier_sha256 1b6e0de6…` and `subject_counter_sha256 91618e91…` equal
  the committed file digests, re-checked at report time).
- **Frozen claims** — `corpus/evidence/round39/claims.md` (P1/P2, kill
  rules, before-states measured pre-freeze and disclosed; no errata needed).
- **Routed defect repairs (round-38 closure D1–D6)** — D1/D2: r38 claims
  Errata 14–15 (hash supersession `37e2b996…→0447ad14…` named; harness
  changes disclosed). D3: stale erratum counts corrected (LOG 1419/1422,
  SCORECARD r38 section, r38 lesson header/notes; claims carries 15 errata).
  D4: SCORECARD r38 attribution note (wave-2 seeds ran at `8e93bc91…`; tip
  evidence = regenerated receipts + one-hunk diff). D5: SKILL.md round-37
  counters row restored to 9 pipes with `| chousa |`. D6: r38 lesson
  correction block (URLs per contract rule 1; rejected-candidate wording).
  D7: closed by C2 itself.
- **Frontier step** — S071 (env(1)) re-opened this round (fresh located
  quote, sha match), used-by extended old→new; knowledge entries ×2; lesson
  `round-39.md` with 4 mined mistakes; QUALITY criterion 56.
- **Wave preparation** — `.ufo/waves/round-39/{w1-spec.json, w1-plan.json,
  gen-w1-spec.py, DISPATCH-README.md}`: v1 wave, 32 seats, validated under
  policy v1 (`counts {spawn:32,total:32}`, `dispatch {calls:1, kind:task}`,
  plan rc 0).

## Landed changes

- `6d914e95…` "round-39: capture bash pin … + verifier/subject receipt
  binding …" — `tools/research-gate.sh`; `corpus/evidence/round39/`
  (c1-count.py, c2-count.py, verify-receipts.py, expectations.jsonl,
  claims.md, receipts ×6); `.ufo/waves/round-39/` (controls base+mutant,
  spec, plan, handoff). LOG.md round-39 entry names this commit.
- `6ac1007e…` "round-39: knowledge x2 …" — SCORECARD.md (r39 verdicts + r38
  D4 note), LOG.md (r39 entry + count fixes), SKILL.md (r39 gates row, r37
  row repair, 275-case bumps), corpus/QUALITY.md (criterion 56),
  corpus/README.md (coverage rows ×2 + count fix), corpus/SOURCES.md (S071
  used-by old→new), corpus/lessons/round-39.md (new),
  corpus/lessons/round-38.md (correction block),
  corpus/evidence/round38/claims.md (Errata 14–15),
  corpus/knowledge/{capture-bash-pin-r39.md, receipt-verifier-subject-r39.md}.

## Before → after measurements

- **C1:** `ENV_PIN_CAPTURE_MATCH` **7/8 → 8/8**.
  Command (lane root): `python3 corpus/evidence/round39/c1-count.py --gate
  tools/research-gate.sh --seed N --receipt F`.
  Before: seed 39001 against `.ufo/waves/round-39/controls/base-gate-r39.sh`
  (pre-round bytes `0447ad14…`, committed) → 7/8, `predicate_holds=false`
  (`receipts/c1-base-s39001.json`; the eighth family fails live:
  `GATE_DRIFT: -GATE_GREP`, suppress kills the capture, relative override
  ignored). After: seeds 39011/39111 against the landed gate → 8/8,
  `predicate_holds=true`, both `VERIFY: ok`
  (`receipts/c1-after-s39011.json`, `receipts/c1-after-s39111.json`);
  report-time re-run seed 39301 → 8/8. Discrimination: PATH-`env` mutant
  (`e1251030…`) → 4/8 (seed 39013). Measured at `6d914e95…`.
- **C2:** `RECEIPT_BINDING_MATCH` **before = the r38 pipeline refuses →
  after 8/8**.
  Command (lane root): `python3 corpus/evidence/round39/c2-count.py --gate
  tools/research-gate.sh --seed N --receipt F`.
  Before: every committed r38 receipt lacks both bindings — the r38 verifier
  also accepted five of six weakened-verifier mutants (r38 Erratum 11);
  under the r39 verifier the committed r38 receipt refuses
  `predicate-mismatch` and a stripped r39 receipt refuses `missing-field
  verifier_sha256` (both re-run live in the counter's legacy cell).
  After: seeds 39101/39121 → 8/8, `predicate_holds=true`, both `VERIFY: ok`
  (`receipts/c2-after-s39101.json`, `receipts/c2-after-s39121.json`; the
  39121 receipt re-verified at report time). Measured at `6d914e95…`.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
validate --root /home/vgpnk/Projects/shokunin chousa`.

- Rows before → after: **73 → 73** (A 67/B 1/C 5; mined 50/queued 19/
  rejected 4, unchanged histograms). Exit **0 at round start and 0 at round
  end** (both outputs recorded in `corpus/lessons/round-39.md` §Gate;
  standing W04 ×3: S051/S053 duplicate URLs + the expected S073-shared
  coreutils manual URL).
- Rows added by tier: none new. Rows touched old→new: **S071 used-by**
  `corpus/knowledge/pin-capture-env-r37.md` →
  `corpus/knowledge/pin-capture-env-r37.md,
  corpus/knowledge/capture-bash-pin-r39.md` (S071 re-opened this round:
  quote "remove variable from the environment", 8 words at decompressed
  line 28; file sha `4ae797e6…` matches the row).
- Frontier rows advanced: none (no queued row changed status). Rejected
  candidates recorded in the lesson: a second `bash(1)` row (S068 holds the
  file; the r38 rejected-candidate row stands), a third `sha256sum(1)` row
  (S070/S073 cover both scopes).
- Sourced claim: **C1 rests on S071**, opened/re-opened this round and cited
  by `corpus/knowledge/capture-bash-pin-r39.md` (with S072 for the
  BASH_FUNC channel).

## Trend verdicts

- **expansion: improved** — two knowledge entries admitted on new round
  ground (`capture-bash-pin-r39.md`, `receipt-verifier-subject-r39.md`),
  each with provenance trio and receipt pointers; S071 re-cited by new work.
  Evidence: README coverage rows; `ls corpus/knowledge/*.md | wc -l` 29 → 31
  (2026-10-24).
- **quality: improved** — the r38 closure's two disagreements became fixes
  (D3/D6 corrections with the spot-check's reasons honored); QUALITY 56
  lands from three vacuous-fixture self-catches whose fixes are shown able
  to fail on the controls (mutant 4/8, base 7/8, named refusals); no older
  entry failed its re-check (census exit 0 both ends; r1 observables held).
- **discernment: improved** — the lane's first in-round counter run caught
  its own author's three drafting defects (identical-bytes doctored subject;
  stderr-only crash as "weakening"; benign PATH-`env` shim), mined as
  lesson mistakes with class/evidence/captured-by/fix; the routed-defect
  repairs D1–D6 landed as named artifacts. No non-author spot-check exists
  yet this round (pending the hyaku closure, as every round).

## SHONEN

- [~] SKILL.md decision tables/error patterns/checklists cite sources —
  `SKILL.md` Gates table (round-39 row; r37 row repaired D5); knowledge
  entries cite S071/S072 (`corpus/knowledge/capture-bash-pin-r39.md`).
  Lane assertion; no non-author verifier.
- [~] End-to-end domain task executed and logged — this round's claims are
  an end-to-end measurement of the research-gate against its frozen
  predicates (`LOG.md` round-39 entry; receipts). Lane assertion.
- [~] Instructions executable without oral context — the counters'
  self-test, kill rules and re-run recipes are in the frozen claims and the
  gates-table row; report-time re-runs succeeded from the recorded commands
  alone. Lane assertion.
- [~] No cross-domain bleed, PROVINCE.md accurate — zero network; sibling
  material (loader-env → tsukuroi, dispatch mapping → kumitate) named as
  debt/routed, not absorbed; `PROVINCE.md` unchanged and accurate. Lane
  assertion.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs this round: none (all work used installed coreutils/man pages;
no pacman transaction, per the host-wide pause).

Round shape: **v1 two-wave shape**; wave 1 PREPARED+validated (32 seats,
policy v1, role mix executor 6 / reviewer 6 / critic 5 / scout 3 / scribe 3 /
mutation-tester 3 / sentinel 2 / revenger 2 / connector 1 / simplifier 1),
**0 dispatched / 0 dead this seat** (host mapping: orchestrator dispatches
prepared waves between rounds; itemized under `.ufo/waves/round-39/`).
Planner seat held by the L1 (validator rejects `planner`; data-walk rides
ScoutSurfaces/ConnectorSiblings). Wave 2 (falsify, 32) to follow under the
same policy when wave 1 returns ≥32 attack items. Round total this seat: 32
prepared + 1 L1 = 33 seats accounted; 0 dead. Open L0 questions: none new
(the loader-env pause and rea MCP state remain the operator's, already on the
L0 file from prior rounds).
