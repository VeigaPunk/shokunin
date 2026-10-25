# g3d-r100-authorfinish — finish the r100 CAPSTONE author round (probe fixtures already in tree)

Lane: /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin
Original contract: `.ufo/waves/shokunin-train-20261015-w22/tasks/g3d-r100-author.md`
(scout `reports/round-100/r100-scout.md`, boundary `reports/round-100/r100-boundary.md`,
scout probes under `corpus/live/r100-scout/`).

State found at resume — the author seat wrote SIX r100b probe fixtures, uncommitted:
`corpus/fixtures/r100_probe_r100b_{area,cls,life,modes,rt,sched}.gd`, but never wired them
into `corpus/fixtures/run_battery.py` (insertion-only rule) and filed no report.

Your job:
1. Read the six probes + scout/boundary reports; decide which probe arms become battery rows
   (encode only boundary-surviving claims; bimodal cells arm as envelopes, never single-value pins).
2. Insertion-only edit of `run_battery.py`: add the r100/r100b case rows with pinned signatures
   (re-derive each signature live — never pin an unobserved string; follow the existing CASES
   comment-block convention documenting provenance, folds, and expected-error classes).
3. Battery green twice on the final bytes; documented flake classes only. `--headless`,
   timeout-bounded. If a law fails, fix in the author's spirit and document; never weaken pins.
4. Write `reports/round-100/r100-author.md`: rows added, fixture provenance, green-run receipts,
   blockers. Zero commits. Return: report path, row count, green-run dirs, blockers.
