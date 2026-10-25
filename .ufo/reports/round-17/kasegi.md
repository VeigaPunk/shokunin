# Kasegi Shokunin — Round 17

## Axis and move

- Starting scores: `depth:density=9`, `depth:verifiability=4`, `coverage=7`. Selected lowest axis: `depth:verifiability`.
- Move: extend `corpus/instruments/anchorcheck.py` to recognize the one explicit ORIGIN-WORK path prefix already cited at `SKILL.md:683`, confine resolved paths to the exact configured root, and emit `IN-RANGE(ORIGIN)` / `OUTSIDE-BASE` with separate summary counts. Regular-file checks keep directories and missing paths from being read as source files.
- The selected receipt citation now covers lines 5–8, which contain report ID, URL, submitted date, and status. `SKILL.md:683` previously cited only lines 5–6.
- This is checker vocabulary/coverage, not a new resolver range check: `resolve.py` already tested in-range lines for resolvable paths. Therefore the scored verifiability axis remains **4→4**; no resolver-rate gain is claimed.

## Before → after evidence

- Baseline isolated fixture: the checker skipped the ORIGIN citation (`0` in-range, `0` bad, `0` distinct anchors).
- Final fixture command: `python3 corpus/instruments/anchorcheck.py /tmp/kasegi-r17-origin-anchor.md`.
  - Result: `1` in-range anchor, `3` rejected anchors, `1` distinct anchor; `ORIGIN=1`, `OUTSIDE-BASE=1`.
  - The valid line range printed report ID, report URL, submission date, and `status: submitted`. Negative cases returned `PAST-EOF`, `OUTSIDE-BASE`, and `MISSING-FILE`.
- Full-skill smoke: `python3 corpus/instruments/anchorcheck.py SKILL.md`.
  - Before→after: `195→196` in-range cite instances; `46` bad, `5` lost-recorded, `0` pin-broken; final `ORIGIN=1`, `OUTSIDE-BASE=0`.
  - The new citation is the one additional checked instance. Existing missing/lost counts did not improve.
- `SCORECARD.md` records `depth:verifiability 4→4` and the unchanged other axes. Current resolver context recorded there: `480/1506` overall and `222/486` for SKILL.

## Source and authority boundary

- Source: `/home/vgpnk/Projects/origin-work/open-bug-bounties/claim-packages/submission-review/receipts/k8s-nodebound-token-impersonation.json`; 11 lines, observed SHA-256 `daaee21c387ff6b2103043e53db1794bb6b6b4eb0c9444bc615aa48ca476122b`.
- The source file is untracked in its repository; its HEAD was reported as `1307b8b`. This check verifies current bytes only, not an immutable or independently authenticated receipt. `status: submitted` is not evidence of acceptance.
- The source repository was read-only for this round. No network, credentials, targets, or external side effects were used. The checker accepts only the explicit prefix and rejects resolved paths outside its root.
- Other ORIGIN-like forms, sibling path-only references, and the remaining missing citations are not claimed as covered.

## L2 review

Ten L2s were dispatched in one batched task call; all ten reports returned.

- The empirical probe confirmed the pre-change silent skip and the post-change
  valid/invalid distinction. The approach critic found resolver range-checking
  already existed, so the score stayed at 4 and ORIGIN needed its own summary
  counter.
- The anchor reviewer required lines 5–8 rather than 5–6 to substantiate the
  submitted-status claim. Direct receipt inspection confirms those four fields.
- Connector and security reviews accepted only a narrow, read-only exact-root
  extension; no province re-point, network, credential, or target work.
- Scouts and intent review identified broader unsupported reference shapes and
  unrelated stale/missing corpus references; these remain outside this move.
- The executor's frozen 54-markdown lane regression reported only two new
  ORIGIN observations (`SKILL.md` and the historical `citation-survival.md`
  record); no lane/mirror/pin/MISSING-FILE/PAST-EOF/LOST-RECORDED/PIN-BROKEN
  classifications changed elsewhere. Its no-guard ablation showed a traversal
  could misattribute an existing mirror file, confirming that containment is
  load-bearing.
- Documentation recommendations were applied to the checker README and smoke
  evidence. No unrelated reference families were broadened.

## Files and verification

- Changed: `corpus/instruments/anchorcheck.py`, `corpus/instruments/README.md`, `SKILL.md`, `SCORECARD.md`, `LOG.md`.
- `LOG.md` records the evidence, unchanged score, source limitation, and no-external-write boundary.
- Verification consisted of the isolated boundary fixture and full `SKILL.md` checker smoke above. No permanent test was added; the throwaway fixture lives under `/tmp`.
- Deferred: investigate the 46 missing citations and 5 lost-recorded entries in a later verifiability round; do not infer a score increase from this checker-coverage change.
