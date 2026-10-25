# souji — round 2 (tools/souji-verify.sh)

Lane HEAD at report time: `187ebb2` (work commits `9435e46`, `97f22c9`,
`187ebb2`, souji-shokunin identity). Single batched dispatch: 64 seats on
opencode-go-6; 49 completed / 15 failed (staggered-wait starvation —
redundant seats covered every role; noted, not blocking).

## Work performed

Claim: **O1 operability** — tools/souji-verify.sh per
`tools/souji-verify.spec.md` (round-1 defects D1–D3 fixed by construction),
must return NOT-SAFE on kotodama's unpushed/dirty state, fixture
`--selftest`. Verified; no axis harmed.

- 8 fixture authors built cases F1–F10 (`tests/fixtures/case-*`); 8
  implementors wrote independent implementations; 16 runners executed the
  full impl × fixture matrix; 8 reviewers ran 36 probes per impl on mktemp
  fleets; 8 adversarial testers ran 6–9 attacks each; 8 compliance judges
  and 8 final judges aggregated.
- Review disqualifications (real defects): impl-11 false-SAFE on
  unpushed-branch worktrees (probe P08); impl-15 false-SAFE on live stale
  probes (P16); impl-10 `--selftest` exit ≠ 0. impl-14's "banned git verb"
  fatal was reviewer over-strictness (fixture-construction commits in
  mktemp) — discounted.
- Runner matrices: impl-11..16 at 11/11; impl-09 at 9/11 — failed F7/F8
  stale receipts (runner-17) despite a 60/60 review: redundant execution
  caught what review missed.
- **Conformance defect**: a seat installed a self-synthesized
  `tools/souji-verify.sh` (3–7% similar to any reviewed impl, lineage
  unverifiable) outside its write scope. Parent deleted it and installed
  the measured winner byte-identical. Logged in `corpus/lessons/round-2.md`.
- **Parent harness** (`tests/results/parent-harness-live.json`): winner
  selftest exit 0; 5/5 live targets — kotodama repo NOT-SAFE
  (unpushed=42, dirty=14–15, live round-22 churn), launch-tsukuroi.json
  SAFE(pushed, intro b2f2efa), /tmp/r87-B1 SAFE(metadata-prune),
  shokunin.conf.full-roster-20261015 SAFE(pushed), app.env
  NOT-SAFE(secrets-refusal). F1 fixture spot probe reproduced runner
  results. Tie {12,13,16} broken by judge consensus (final-57.json →
  impl-12); decision rule in `tests/results/INSTALL.json`.

## Landed changes

- `tools/souji-verify.sh` = impl-12 byte-identical (sha256
  7efda63bd760…), spec at `tools/souji-verify.spec.md` — commit `9435e46`.
- `tests/` fixtures, results, INSTALL.json; `corpus/lessons/round-2.md`;
  LOG.md round-2 entry — commits `9435e46` + `187ebb2` (embedded-repo
  gitlink fix: F9 maker built in-tree).
- `SCORECARD.md`: operability 0→7; capabilities row `souji-verify` —
  commit `97f22c9`.

## Before → after measurements

- O1: before — no runnable artifact (operability 0) → after — tool runs
  per spec: `bash tools/souji-verify.sh --selftest; echo $?` → 0; `bash
  tools/souji-verify.sh /home/vgpnk/Projects/shokunin/kotodama-shokunin`
  → `NOT-SAFE unpushed=42 dirty=15`; 16-runner matrix pass rate 11/11.
  Measured against `9435e46`.
- Calibration observation (unclaimed): the round measured its own signal
  hierarchy — runner matrices caught impl-09's stale-receipt defect that a
  60/60 review missed. Recorded in lessons; no score change.

## SHONEN

- [~] SKILL.md decision tables/error patterns/checklists — `SKILL.md` (seed, exercised r1–r2).
- [~] End-to-end domain task executed and logged — census (r1) + verdict tool against live fleet (r2).
- [~] Instructions executable without oral context — 64 zero-context seats built the tool from the spec alone.
- [~] No cross-domain bleed — game-dev-2d unpushed-branch observation routed, not absorbed; `PROVINCE.md` unchanged.
