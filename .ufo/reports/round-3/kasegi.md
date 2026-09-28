# kasegi-shokunin — round-3 findings

Lane: bounty & security research. Commit `e73b2b5` (`round-3`) in
`~/projects/shokunin/kasegi-shokunin`. Repo-only changes: `SKILL.md`,
`corpus/{README,knowledge/*,lessons/*}.md`, `LOG.md`.

## Gap selected and closed

Two gaps from `corpus/README.md` addressed:

### 1. `ops/claim-check.mjs` gate list (was: "only known via error strings")

Read all three ops scripts in full. Authored `corpus/knowledge/claim-gates.md`
with the complete extracted inventory. Findings that change how a package is
built:

- **Duplicate-submission guard is global** — claim-check scans *every*
  `claims/*/*/status.json`; same slug OR same title (≥16 chars) with any prior
  submission record fails. Title reuse across programs is a real footgun.
- **`claim_review.reviewer.role` must be literally `kx-reviewer`** — a reviewer
  on another role string fails the gate even if everything else passes.
- **`head_sha256` three-way binding**: custodian chain's last decision ==
  `head_sha256` == `manifest.expected_head_sha256`.
- **`prepare-claims.mjs` immutability rule**: if `submit-payload.json` is a
  manifest-bound artifact and bytes differ, skip — changed bytes need
  re-review. Post-write recheck failure restores original bytes.
- **claim-index error ranking**: prior-submission/duplicate/state errors
  display first, custodian/manifest second, others last; only 5 shown.

### 2. `vdp-disclosures/` unwalked (was a listed gap)

Read all 4 files of `vdp-disclosures/anthropic-plugin-dev-cmd-injection/` plus
the `claims/*/honest-zero-vdp-no-payout/` statuses. New corpus entry
`knowledge/vdp-disclosure-packages.md`: distinct four-file package shape
(`ROUTE.md`/`cover-note.md`/`report.md`/`SUBMITTED.md`), free + fully
attributed per operator decree 2026-09-06, channel = vendor security.txt
Contact (H1 `embedded_submissions`), operator sends personally.

## Bonus evidence

Sampled 5 Cantina sibling ingestions to test whether the $100-fee /
live-precondition pattern generalizes: only `cantina-dydx` repeats
`positive-blocked-live-precondition`; `morpho/euler/uniswap/reserve` are
honest-zero parks. Recorded in `program-quirks.md` — fee gate is
Pendle-specific so far.

## SKILL.md changes

- "Enforced gate" paragraph after the triage table (claim-check +
  prepare-claims semantics summarized; pointer to corpus entry).
- New "VDP disclosure packages (sibling format)" section.

## Carried gaps

`vgn-bounty-lab/` unwalked; `fleets/registry.json` lane routing possibly
cross-domain; `evidence/` (per-program) vs `claims/*/evidence/` (per-package)
conventions unexamined.
