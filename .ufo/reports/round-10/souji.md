# souji — round 10 (close the r9 defect classes)

Lane HEAD at report time: `e879ba0` (souji-shokunin identity). Dispatch:
16 seats on **devin/deepseek-v4-1-flash-max** — after the operator-requested
**hyper test failed functionally**: `hyper/deepseek-v4.1-flash` served one
trivial probe in **829 seconds** and produced zero completions across two
interrupted batches. Per the session fallback (deepseek → devin), r10
completed on devin. 16/16 seats.

## Round verdict: REJECTED on O1 — 3 residual unsafe outcomes, 1 class

The certifier ran **15 corpora/reproducer suites** (S05–S24, final-21..24,
fresh variants): **unsafe = 3**, all a single class —
`souji-census --compare` accepts empty/near-empty prior censuses instead of
refusing (contract violation; **originals preserved in every case; no data
loss**). **121 conservative refusals** — the r9 fix classes hold.

**Delta vs r9's close:** ≥16 open defect classes → **1**. The composed
merge (7 clusters, A–G: hidden-reference sweeps, full-tree directory
staleness, ledger revocation + input forgery, nested-repo + symlink
containment, index-hidden flags + full-tree pushed receipts, git-failure
refusals + locale pinning + worktree-HEAD skew, ownership-by-gitdir +
gitfile roots + stage-4 revalidation, index-write contract + descendant
pins) is installed over the S17 tools — selftests **40/51/91 green**.
Tools remain **NOT certified** until the census contract closes (r11).

## Landed changes

- `tools/souji-{verify,vault-verify,quarantine}.sh` = cand-merge bytes;
  `tools/cand-*` cluster/merge candidates; `census/round-10/` (16 fragments
  + cert-16 with the full unsafe register); lessons; LOG — commit `e879ba0`.

## Before → after measurements

- O1: open classes ≥16 → 1 (census-empty-compare); certification NOT
  granted (unsafe ≠ 0) — NOT-MET, honest.
- Hyper provider: tested per operator request — functional, ~14 min/agent,
  unfit for batch work (recorded; future use advisory).

## SHONEN

- [~] SKILL.md decision tables — the census-contract gap is the last open class.
- [~] End-to-end domain task — a full defect-class closure campaign.
- [~] Executable without oral context — 16 zero-context seats.
- [~] No cross-domain bleed — census fix routed to r11; no live artifact touched.
