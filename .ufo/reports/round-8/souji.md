# souji — round 8 (quarantine tooling + gate runbook)

Lane HEAD at report time: `6d749f17` (souji-shokunin identity). Single
batched dispatch: 24 seats on **zai-coding-plan/glm-5.3-flash**; 22/24
(two failures traced to **host /tmp disk quota** corrupting fixture
runs — escalated to operator/tsukuroi; workaround TMPDIR=/var/tmp).

## Work performed

Claims: **O1 operability** — the receipt-gated quarantine flow as a
tested tool; **C1 calibration** — evidence-pointer integrity sweep;
**K1 coverage** — the gate-opening runbook. All three verified.

**O1 — tools/souji-quarantine.sh (verified).** Eight implementors, six
runner scenarios; final judges converged on **impl-01** (sha
5780ad75…): 63-check selftest green; fail-closed by design — stage-1
authorization via the receipt engine with receipt pinning (list rows
whose engine verdict doesn't exactly match the pinned receipt are
NOT-AUTHORIZED), `git mv` for tracked / `mv` for untracked staging into
`.ufo-quarantine/<utc-date>/`, hold window, class-aware second check
(stale binding on the quarantined copy; pushed/obsidian re-derived
against original context), delete only on PASS else ABORTED with the
copy kept. **Live-fleet mutations are refused (exit 4) without an
explicit env override.** The full flow is now exercised end-to-end on
fixtures — every stage the r6/r7 audits flagged UNEXERCISED.

Parent verification: selftest 63/63; untracked-stale fixture flows
DRY-RUN-PASS; **96-row approval dry-run: 96/96 DRY-RUN-PASS, zero
mutations** (`git status` clean before/after). A parent awk bug (empty
receipt pins) was caught by the tool's own fail-closed refusal — fixed
and re-run.

**C1 — pointer integrity (verified).** 111 tokens extracted from
reports r1–r7 + SCORECARD/LOG: 95 alive, 1 dead pointer (confirms the
r7 correction), 1 drift recorded.

**K1 — gate runbook (verified).** `census/round-8/gate-runbook.md`:
exact command sequences for every blocked class — the one-line
quarantine command for the operator-signed 96, the gd2d-pin
regeneration after that lane pushes (verified via a simulated
post-push fixture: registrations become SAFE(metadata-prune)), the
lane-remote creation sequence, kotodama's disposition, and the now
host-critical /tmp cleanup escalation.

## Landed changes

- `tools/souji-quarantine.sh` + 3 rival impls + `census/round-8/`
  (fragments, qrun results, pinned approval list, runbooks) +
  `corpus/lessons/round-8.md` + LOG — commit `6d749f17`.

## Before → after measurements

- O1: before — quarantine flow UNEXERCISED (r6/r7) → after — tool
  installed, 63/63 selftest, all five flow outcomes demonstrated on
  fixtures, 96/96 real-list dry-run with zero mutations.
- C1: 111 pointers checked, dead-pointer rate 1/111 (the r7 correction
  itself).
- K1: every blocked class has an executable, verified-open gate path.

## SHONEN

- [~] SKILL.md decision tables — the quarantine flow now exists as code; the UNEXERCISED notes flip next content edit.
- [~] End-to-end domain task — first full removal-flow execution (fixtures) in the lane's history.
- [~] Executable without oral context — 22 zero-context seats.
- [~] No cross-domain bleed — /tmp quota escalated to tsukuroi/operator, not absorbed.
