# Role-Specific Work

## critic

Read the pinned family, its dispatch, supporting instrument and claimed
laws. Attack missing-witness acceptance, green-on-blocked summaries,
fail-open exceptions, process ownership and cleanup, lock scope, inherited
environment, unsupported mechanism claims and copied-but-unmeasured bytes.
Use source-linked counterexamples; do not mutate or execute the fixture.
Name a fixable defect separately from a declared loss of coverage. No
new numerical claim, live family, benchmark or generated grader.

## reviewer

Trace affected callers, error paths and return/accumulator propagation in
the actual pinned artifact. Check self-containment, configuration precedence,
missing-key behavior, and whether source matches each claimed safeguard.
For r99 specifically verify the physical-LAN control cannot run by default.
For r100 specifically follow failures from helper through entry and main.
Read-only audit; no live families or source changes.

## simplifier

Inventory unreachable branches, unused symbols/arguments, duplicate
observations and redundant authority. Propose only source-supported
deletions; distinguish a proven reference absence from behavioral proof.
Do not edit or run before/after experiments, invent a grader or declare
a fold proven without existing execution evidence. Preserve provenance
and classify any withdrawal of an extension point as a tradeoff.

## scribe

Audit report -> receipt -> author bytes -> integrated bytes -> pinned
revision links. Use the recorded source snapshots and byte comparisons;
do not recompute original measurements. Check timestamp and hash scope,
uncommitted dependencies, stale counts, citation locations and coverage
labels. Keep the original vs corrected artifact distinction. Do not
edit a report other than your assigned scribe report or create new gates.

## verifier

You alone may run the assigned round's existing full family, ONCE, on a
minimal frozen tracked-source export. No other live family, new grader,
law set, mutation, fallback or retries beyond existing source behavior.

From the lead-supplied PIN and N/FLAG, use this exact recipe:

```
set -o pipefail
REPO=/home/vgpnk/Projects/shokunin/audio-shokunin
SCRATCH=/home/vgpnk/Projects/shokunin/audio-waveb-resume/rN-verifier
# Verify SCRATCH's parent before mkdir; use unique, never reused scratch.
mkdir -p "$SCRATCH/tree"
git -C "$REPO" archive PIN corpus/fixtures corpus/artifacts |
  tar -x -C "$SCRATCH/tree"
```

The minimal export intentionally omits ignored author evidence: generated
stimuli must regenerate, not be silently borrowed. Record export errors,
do not substitute a working-tree copy or full repository archive.

For r93 only, first run `timeout 15 pactl info`; a nonzero result is a
blocked prerequisite, not permission to restart services.

In the exported tree, execute exactly:

```
env -u RTP_R99_ALLOW_LAN_CONTROL UFO_SEAT=rN-verifier-resume \
  PYTHONDONTWRITEBYTECODE=1 timeout 1500 \
  python3 corpus/fixtures/measure_audio.py --probe-FLAG
```

Save the literal command, stdout, stderr, return code and resulting
measurements.json path under your scratch directory. Do not interpret rc0
as complete coverage or compose any new numeric checker. Cite the receipt
for the lead to inspect. Missing outputs, blocks, red results or timeout
remain visible; never tune/retry to make the report green.

Afterward leave evidence and services intact. Write the advisory report
only; it is not a shipping or gate-admission decision.
