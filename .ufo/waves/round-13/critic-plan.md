# Round 13 protocol-lane plan — adversarial critique

## Axes and verdict

The owned axes are **protocol soundness** and **gate integrity** (`MISSION.md` fleet
shape; `SCORECARD.md` header). `AXES.md` says a round is one axis-move: land one
verifiable improvement, measure it, and record before→after. The plan is directionally
right, but A is not automatically an axis move and C has a serious trust-boundary gap.
B is a closure obligation, not an axis move by itself.

## Must-fix blockers

### A — compaction and the proposed score

**Blocker 1: compaction may only repay a booked regression.**
`SCORECARD.md` §Planned calls A a “compensating move”; round-12's report §Length cost
says protocol soundness was **held at 8**, because seven holes were closed but
`PROTOCOL.md` grew 446→526 lines. Current commands, re-run here, are:

```text
wc -l -c PROTOCOL.md && awk 'NR<487' PROTOCOL.md | grep -o 'round-[0-9][0-9.]*' | wc -l
526 49269
4
```

The round-12 report §Length cost records the same 446/39718→526/49269 change and
explicitly queues ≤470. Therefore deleting lines to return toward the already-booked
P4 baseline does not prove 8→9. The smallest correction is to state **8 held** unless
A lands a new, independently measurable capability beyond debt repayment (for example,
a compacted text that also makes every new pin and the Gate standard independently
checkable by a new verifier). Do not record a score increase merely for reaching 470.

**Blocker 2: the census is necessary but not a preservation test for modality.**
`verify-census.sh` reads TSV predicates and runs `grep -qE` against the target; the live
run is `93/93 obligations found; 0 MISSING`. Regex presence can pass after a modal is
weakened, split, or made conditional elsewhere. A compaction could retain “MUST” in
an unrelated sentence while changing the obligation's effective scope. Smallest
correction: extend the committed census with exact quoted normative anchors (at minimum
one anchor per changed rule and all seven pins plus `## Gate standard`), and add a
negative/semantic check for modal strength and scope, or explicitly cap the claim to
“predicate preservation,” not “no obligation lost.” The acceptance command must report
both 93/93 predicate hits and the anchor/modal check; a 93/93 result alone cannot
justify a score change.

**Blocker 3: seven pins and Gate standard are not yet proven covered by the census.**
The current verifier's output proves only the existing TSV's 93 rows. The smallest
correction is a committed census diff showing seven named pin predicates and a
`^## Gate standard` predicate, followed by a run that prints the expanded denominator
and 0 missing. Do not accept “the section exists” as proof that each pin remains
operative after compaction.

### B — closure debt versus treadmill

**Blocker 4: closing rows after evidence lands is falsifiable only if the cutoff is
fixed.**
The round-12 report §Closure record says the gate's 21:20 pass missed four rows and the
21:30 pass caught them; its live reading changed again when kotoba r14 landed. The
frozen command demonstrates why a cutoff matters:

```text
python3 .ufo/waves/round-12/closure-check.py --frozen pre --no-citations
closure-check: debt debt=5 contradictions=0 unrowed_terminated=2 pending_round=7
...
python3 .ufo/waves/round-12/closure-check.py --frozen post --no-citations
closure-check: ok debt=0 contradictions=0 unrowed_terminated=0 pending_round=3
```

A later `closed_at` can make a stale row disappear without improving process; that is a
measurement treadmill. Smallest correction: for each of the five debt rows and six
pending rows, commit one round-13 snapshot with `closed_at`, evidence cutoff, status
transition, and the exact checker output. Require that every stale row is either
terminally resolved with evidence at or before that cutoff or explicitly re-confirmed
in-flight with a new launch pointer. “No stale rows in a live run” is insufficient.

**Blocker 5: B is not itself an axis move.**
`AXES.md` requires a verifiable improvement; bookkeeping already required by
`PROTOCOL.md` §Closure (“Every `in-flight` row is answered by the next protocol
round”) cannot raise gate-integrity merely by being performed. Smallest correction:
score B only against a named before→after metric such as stale rows at the same frozen
cutoff, or hold the score and describe B as standing closure duty. Never count
`closed_at` edits as capability absent a durable detector or reduced recurrence.

### C — checker changes and trust

**Blocker 6: a history pin has an unassigned and forgeable writer.**
The proposed pin is a sha256 over canonical JSON of `rounds[0..k-1]`, but the plan does
not say who updates the pin or what authenticates it. If the same lane that edits
`MANIFEST.json` can regenerate the pin after its edit, the pin blesses tampered history.
The existing gate already pins expected verdicts in frozen artifacts; `PROTOCOL.md`
§Append-only `rounds` says corrections append and never edit. Smallest correction:
make the pin an append-only, committed artifact generated by an independent integrator
step **after** the manifest commit, and have the checker reject a pin whose recorded
manifest commit/parent is not the expected prior chain. Better still, have the pin
contain the prior commit id and hash, and require a non-author verification command in
the round report. Otherwise this is self-attestation.

**Blocker 7: history pin may duplicate Git without adding detection.**
Git already proves committed bytes and ancestry, but not that a checker consumed the
intended canonical prefix at runtime. Conversely, a hash of canonical JSON adds little
if an authorized committer can rewrite both files. The smallest defensible scope is
not “history integrity” generally: define it as “the checker refuses a changed prefix
when the pin is independently anchored to the prior commit.” Include a committed
fixture that mutates a historical row while leaving the new pin untouched and requires
the new finding class; include a second fixture showing that regenerating the pin is
not an allowed repair in the same closure pass.

**Blocker 8: discovered frozen roots can shadow round-12 baselines.**
Current code hardcodes:

```python
frozen_dir = os.path.join(repo, ".ufo", "waves", "round-12", "frozen", which)
```

at `.ufo/waves/round-12/closure-check.py:1330`. If generalized lookup searches
`.ufo/waves/*/frozen/<NAME>` and picks the first match, a round-13 `post` can shadow
round-12 `post`, silently weakening the three committed round-12 baselines. Smallest
correction: require an explicit root selector (or require exactly one matching name and
fail closed on duplicates); preserve a compatibility assertion that `pre`,
`post-actual`, and `post` resolve to round-12 paths when invoked in the old mode. Add a
fixture with duplicate `post` names and require exit 3 / an explicit ambiguity finding,
not arbitrary glob order.

**Blocker 9: “7/7 mutation score” is underspecified after C.**
Round-12's mutation artifact itself records m1 survived because legacy rows were
unadjudicable, while its headline elsewhere says 7/7 determinate. The plan's m1 fix
must name the mutation and the expected structured finding, not merely rerun the old
battery. Smallest correction: commit a mutation manifest whose m1 changes
`MANIFEST.json` legacy status, whose history pin remains unchanged, and whose checker
emits the new finding class; rerun all seven with exit codes and classify each as
killed, survived, or inconclusive. Require no traceback (round-12 mutation-gate records
m3's `KeyError` as inconclusive precedent).

## Non-Pareto check

| Move | Axis benefit | Harm / required guard |
|---|---|---|
| A compaction | Potentially restores the protocol-size metric and makes seven pins easier to audit. | Can harm protocol soundness by dropping modal scope or Gate-standard detail; can harm sibling lanes if their quoted anchors/line references break. Hold score at 8 unless a new capability is measured. Preserve quoted anchors and update all affected citations. |
| B closure pass | Can improve gate integrity if the same cutoff proves stale debt is resolved and pending rows are accounted for. | Merely closing rows can hide elapsed time, and editing `MANIFEST` can conflict with concurrent lane entries. It does not improve protocol soundness; freeze cutoff and append only. |
| C checker changes | History detection and root selection can improve gate integrity. | A forgeable pin weakens gate integrity; ambiguous root discovery can invalidate round-12 comparability. It can also harm siblings by changing `--frozen` semantics. Fail closed on duplicate roots and preserve old names/outputs. |

## Accepted falsification conditions

### A
A non-author runs the expanded census against the compacted `PROTOCOL.md`: it must
show ≤470 lines, body refs ≤4, the original predicates plus seven pin predicates and
`## Gate standard` all passing, and the modal/anchor check must fail if a `MUST` is
changed to `SHOULD`, if a prohibition is removed, or if a pin's operative sentence is
absent. Any failed anchor, changed modal, or body count >4 falsifies A.

### B
Against a committed round-13 frozen snapshot and its stated `closed_at`,
`closure-check.py --frozen NAME` must reproduce the expected exit and debt set. Every
five formerly `stale_in_flight` rows must have a terminal evidence-backed status or an
explicit re-confirmation at that cutoff; all six pending rows must be represented with
an explainable status. A later live clean run without this cutoff proof does not count.
Any stale row absent from the append-only correction, or any expected-baseline mismatch,
falsifies B.

### C
A non-author runs the seven-mutant battery plus two new fixtures: (1) mutate a legacy
prefix row without changing the committed history pin and observe the new history-pin
finding; (2) create duplicate frozen roots with the same NAME and observe a structured
no-baseline/ambiguity failure. Then run `--frozen pre`, `post-actual`, and `post` and
prove each still resolves to the round-12 committed snapshots and reproduces their
recorded verdicts. Any m1 survival, traceback, arbitrary root selection, or loss of
round-12 baseline matches falsifies C.

## What round 13 should do instead

The plan is right only with these corrections and with protocol-soundness held at 8.
Treat A as a narrowly bounded compensating compaction, B as standing closure evidence
rather than a score move, and C as a fail-closed checker change with independent pin
anchoring and duplicate-root tests. If the team cannot establish an independent writer
and immutable prior commit for the history pin, reject that part of C and instead add a
checker-only legacy-row consistency finding backed by the existing committed frozen
snapshots; do not ship a self-blessable hash and do not claim m1 is killed.
