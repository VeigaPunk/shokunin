# Round-14 registry-home rerun — contract handoff (contract executor → registry executor / parent)

Authority: `context.md` in this directory. This file records the landed `PROTOCOL.md` clauses,
the registry-home design they encode, and the row requirements for the registry executor. No
scores, no gate implementation, no execution claims; parent integrates and verifies.

## Landed clauses (current `PROTOCOL.md` text, §Gate standard)

`## Gate standard` → **Registry** bullet:

> The schema is this section's; the rows live at the lane's *registry home*: for a
> child lane, its own repo's `SKILL.md`; for a main-repo lane (`protocol`, `aggregator`), that
> lane's explicitly lane-owned registry section in the root `SCORECARD.md` — the `protocol` lane's
> section sits in protocol territory, above the `## Aggregator lane` heading, the `aggregator`
> lane's inside its own section below it. The main repo carries no root `SKILL.md`: none is
> required and none is invented; the lane-owned `SCORECARD.md` section is the main-repo home
> (§Appendix, "Registry home"). Row fields: name, `gate|probe`, entry command, verdict map
> (code → class), self-test command and spelling, pinned-value path, write scope, owner. The
> aggregator ledger stays the routed-defect queue, not a second inventory; a fleet index is
> pointers to lane rows at their registry home, never copied expected values. Frozen
> baseline names resolve under any `.ufo/waves/*/frozen` root; a bare name matching more than one
> root fails closed.

`## Gate standard` → **Delivery** bullet (its history-pin sentence is unchanged):

> This section reaches a lane through the re-read duty, not the driver's prompt
> template (one of five child-lane items): the integrator names the exact `lane_prompt()` addition
> in its round report, and closure grades no gate conformant until its registry row exists at the
> lane's *registry home* — the same homes **Registry** above names: the lane's own `SKILL.md` for a
> child lane, the lane's explicitly lane-owned root `SCORECARD.md` registry section for a
> main-repo lane; the root has no `SKILL.md` and demands none.

Both clauses enumerate the identical homes for every lane kind; Delivery adds no home Registry
lacks. Nothing else in §Gate standard changed: **Verdict**, **Self-test**, **Two evidences**,
**Scope** (runtime boundaries: read-only, operator-owned external surfaces, `loop_stop`/`mission_goal`
and native-judge bars intact) and the remaining bullets are untouched; all other sections are
untouched.

## Registry home by lane kind

| Lane kind | Home | Notes |
|---|---|---|
| child lanes (`kasegi`, `kengaku`, `kake`, `kumitate`, `kotoba`, `kagi`, `kama`, future) | own repo `SKILL.md` | unchanged from the prior clause; children retain their rows |
| `protocol` (main-repo) | root `SCORECARD.md`, explicitly lane-owned registry section, protocol territory — **inserted above the `## Aggregator lane` heading** (before `SCORECARD.md:132` in the baseline) | registry executor's sole SCORECARD edit this wave |
| `aggregator` (main-repo) | root `SCORECARD.md`, its own lane-owned section inside the existing `## Aggregator lane` territory | landing an aggregator row there is the aggregator lane's own future work; this wave preserves that section byte-for-byte |
| root `SKILL.md` | does not exist; never required, never invented | the contradiction the appendix row pins: `root_SKILL_exists=False` at `99efc52` |

## Appendix pointer pairing (resolves)

- Body: `(§Appendix, "Registry home")` in the Registry bullet.
- `PROTOCOL-APPENDIX.md` line 49 (appended; prior rows unmodified, old bytes a strict prefix):
  first column `Registry home`, round 14, figures verbatim from
  `.ufo/waves/round-14/registry-home-rerun/before.json` (`protocol_registered_closure_gates=0`,
  `root_SKILL_exists=False`, command + stdout).

## Row the registry executor inserts (protocol section, root SCORECARD.md)

- Section must name itself as the `protocol` lane's registry home in its own heading, sit above
  `## Aggregator lane`, and not alter a single aggregator byte. `before.json` protects the
  aggregator section at sha256 `7abc0478efcb16d0d2e4bbe57271d52c00da08a8eb33bc76edc272ae5b5cfccf`;
  it must still hash identically after the insertion.
- One row, the eight fields exactly as §Gate standard lists them, for the existing gate
  `.ufo/waves/round-15/closure-check.py` (protected sha256 `0ac440f7a3b3a7500568fa469b7efba451ee0eabb9683b827630dcc0869a778c` — unchanged, not edited):
  - name: `closure-check` — rows are counted by the baseline as lines starting
    `| closure-check | gate |`, keep that prefix;
  - `gate|probe`: `gate`;
  - entry command: `python3 .ufo/waves/round-15/closure-check.py --repo . --json --no-citations`
    (live mode, the invocation the inherited record captured);
  - verdict map (code → class): `0` clean; `1` failed; `2` could-not-evaluate; `3` no-baseline
    (declare the reserved codes per §Gate standard Verdict; the round-12 exit map is the
    precedent at `SCORECARD.md` M14);
  - self-test command + spelling: `python3 .ufo/waves/round-15/closure-check.py --selftest`
    (spelling `--selftest`; recorded tally 27/27 at M25 — quote it as recorded, do not re-run);
  - pinned-value path: `.ufo/waves/round-15/frozen/r15-pre-003400/expected.json` and
    `.ufo/waves/round-15/frozen/r15-post-012710/expected.json` — always use the **qualified**
    frozen names `round-15/r15-pre-003400` and `round-15/r15-post-012710`; a bare name that
    matches more than one `.ufo/waves/*/frozen` root fails closed;
  - write scope: read-only over the main repo (stdlib-only checker; no external surface, no
    driver/runtime mutation);
  - owner: `protocol` lane.
- Row status text must say **registration at the declared home only** — NOT blanket conformance,
  NOT a live clean verdict. The inherited live run
  (`.ufo/waves/round-14/registry-home/live-closure.json`, at `e163d15`) crashed with
  `TypeError: '<' not supported between instances of 'NoneType' and 'int'` inside
  `analyze()`'s row sort (`closure-check.py:1143`, historical `round:null`) and emitted no
  verdict. Treat as the known failure: do NOT rerun to confirm, do NOT change the gate; the
  parent routes the defect.
- No duplicate inventory: the aggregator ledger (`.ufo/reports/AGGREGATE.md`) is not written by
  this wave and stays the routed-defect queue; a fleet index, if ever built, is pointers to lane
  rows at their registry homes, never copied expected values.

## Files changed by this seat

1. `PROTOCOL.md` — §Gate standard **Registry** and **Delivery** bullets only (amended above).
2. `PROTOCOL-APPENDIX.md` — one appended row `Registry home` (line 49); no prior byte rewritten.
3. This file.

No SCORECARD.md, LOG.md, `MANIFEST.json`, report, script, routing, or inherited-artifact
edit by this seat; nothing committed.

## Parent verification handles (do not run before all wave artifacts land)

- `grep -n 'registry home' PROTOCOL.md` — Registry defines the homes, Delivery names them
  "the same homes **Registry** above names"; no clause requires a row in a root `SKILL.md`
  (`grep -n 'SKILL.md' PROTOCOL.md` around §Gate standard shows child-repo homes + the explicit
  "no root SKILL.md" statement only).
- `(§Appendix, "Registry home")` in the body resolves to `PROTOCOL-APPENDIX.md` first column
  `Registry home` (line 49); verify the appendix's lines 1–48 are an exact byte prefix of the
  pre-edit file.
- Eight registry fields present verbatim in the Registry bullet; no-duplicate-inventory sentence
  and frozen-baseline fail-closed sentence retained.
- SCORECARD.md aggregator section still hashes to `7abc0478…5cfccf`; `closure-check.py`,
  `expected.json` pair, `.ufo/history-pin.json`, `MANIFEST.json`, and the filed
  `.ufo/reports/round-14/protocol.md` (prefix `d2567df3…`) match `before.json` digests, with the
  report byte-preserved until the parent appends the erratum after commit.
- Re-run of every registry citation belongs to the parent's integrated pass, not to any seat.
