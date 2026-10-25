# kake-shokunin — round 4 report

Commit: `kake-shokunin@6b1cd07` ("round-4"). Scope: `kake-shokunin/` only.
No fires, no deploys, no publishes, no live-site edits.

## Gap closed

**Undecoded fire journals.** Rounds 1+3 taught the kimi-surface verbs
(update/recreate/rebuild) and probe semantics, but nothing taught how to
read a finished run. `~/Projects/webzites/state/` holds 15+ run journals
whose `error.code` had no decoder — and the exit code alone does not reveal
whether the metered fire was consumed. An agent misreading code 6/7 could
refire (double meter spend, orphaned version cards) or abandon a succeeded
run.

## What landed

1. `corpus/knowledge/fire-journal-codes.md` (new, 67 lines):
   - Full exit-code table extracted from every `code:` throw site in
     `scripts/kimi-surface.mjs` (codes 1–8, 64 — verified complete by
     `grep -o "code: [0-9]*" | sort -u`).
   - Journal anatomy: what `liveBefore/slugCheck/zip/canonCheck/fired/
     versionWait/preview/liveAfter/operatorNext` each prove.
   - The decisive rule: **meter consumption is a journal fact** (`fire:true`
     + a `fired` step), not an exit-code fact. Code 5 = clean pre-send abort;
     4/6/7 post-`fired` = ANOMALY (operator inspects, never blind refire).
   - Success signature: `liveAfter.stillDead:true` + claimed version card +
     working `p-*.kimi.page` preview = agent-done; live URL flips only on the
     human publish click.
   - Observed-outcome table from real journals (rebuild charter-ufo-fsd
     `efc1830` success; plazir15 code-6 post-fire orphan risk; ds4cc mirror
     code-7 post-fire anomaly; lucario 3× preflight-only).
2. `SKILL.md`: journal-reading step in the publish checklist; new
   "fired-but-orphaned runs" pitfall with recovery path (kimi-map + match by
   fire-description timestamp).
3. `corpus/lessons/round-4.md` + `LOG.md` entry + README coverage-map row.

## Audit fixes (in-round)

An aggregator audit (`corpus/lessons/round-1-aggregator-audit.md`, arrived
mid-round from the orchestrator) filed defects against round-1 claims.
Verified each against ground truth and fixed:

- **"20-row registry" → 21 rows.** Confirmed `len(sites)` = 21 (12 live /
  3 pruned / 3 broken / 3 queued; 14 kimi-surface updatePath). Corrected in
  `fleet-registry.md`, `SKILL.md`, `corpus/README.md`. Audit's secondary
  suggestion (add `app.ds4cc.com` to inventory) rejected: that row is not in
  `fleet.config.json` — it's a SKILL property-map entry; documented as such
  instead.
- **Clone count ~40 → 50** (`ls ~/Projects/webzites/repos | wc -l`).
- **`status:"pruned"` semantics**: probe.mjs has NO pruned branch — every
  url+expect row is probed equally; pruning is a registry-only label.
  Corrected in `fleet-registry.md` + `SKILL.md`.
- `drift-detection.md` gained a top-level Source: line (minor conformance).

## Fresh verification

- Probe state re-read from `state/probe-latest.json` (2026-09-28T18:51Z):
  6 violations — plazir15, charter-ufo-fsd-kimi, lucario (404 dead slots),
  plazir27-kimi-pro (preview-404), xsnapshot-app (fetch failed), charter-ghp
  (beat-marker churn, PQ-12). Matches round-3 corrections; no new deltas.
- Exit-code completeness: every `code:` literal in kimi-surface.mjs mapped.

## Open items for round 5+

- Orphaned-card recovery sweep: `kimi-map` + timestamp-match for the plazir15
  code-6 and ds4cc code-7 fired-but-unclaimed runs (needs browser lane).
- PQ-12 marker re-pin for charter-ghp (webzites keeper owns; beat churn <48h).
- 50-repo `sourceDir` map still absent (only registry-bound dirs documented).
- Cross-domain flag (from audit, not absorbed): the shared burner-chrome CDP
  lease is also claimed by kagi-shokunin corpus — integrator decision needed.
