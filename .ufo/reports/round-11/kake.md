# kake-shokunin — round 11 report

**Axis-move: operability (8→9).** Closed the r10 residual "3 of ~20 free-read
verbs never live-run": `probe <id>`, `kimi-surface sync-check`, `grokbot
reconcile` — plus `status` variants — all executed live on the real repo,
backup-guarded where the verb writes state. Freshness held at 8 (probe-latest
2.6h fresh at round open; operability picked per the SCORECARD plan; no
double-count). Commit `round-11` in `kake-shokunin/`. 13 read-only L2 probes in
ONE batch (planner/scout/revenger/labrat×3/executor×2/critic/reviewer/
connector/sentinel/scribe → `/tmp/kake-r11/`); zero fires, zero pushes, zero
browser ops; sentinel proved the only webzites state delta = one sanctioned
`total:1` history append + a clobber→byte-identical restore.

## The round's central finding: `probe <id>` clobbers the fleet snapshot

Live proof (LabratProbe, backup-guarded, 21:31:26Z): `probe ds4cc-com --json`
→ exit 0, `state/probe-latest.json` **18 rows → 1 row**; `webzites status`
while clobbered printed **1 OK row, exit 0** — 5 violated + 1 error fleet rows
invisible; post-restore, 18 rows, exit 1. `--quiet` does not prevent it
(`cli.mjs:78` saves before the `:79` gate). This is an **unintended defect,
not spot-probe semantics** (RevengerMerge archaeology): the
`mergeProbeResults` intent comment (`fleet.mjs:27-29`) says site-specific
verbs "must not erase every other site's verdict"; the r2-era fix covered
`grokbot tick` (`cli.mjs:289`) and `bots task` (`:647`) but left `cmdProbe:78`
raw. History carries 11 `total:1` spot rows (10 pre-state + this round's).
SKILL.md step 1 now carries the trap + the backup/restore recipe; the
one-line webzites fix proposal is recorded for the owner lane (kake never
edits webzites source).

## Live exit contracts landed (7 previously-undocumented behaviors)

- `probe`: exit 1 is **subset-scoped**; unknown id → **exit 2 + HELP on
  stderr, no state write** (`cli.mjs:1097-1101`).
- `status --json` **always exits 0** (`:94-97`); plain `status` exit 1 is
  **snapshot-relative** (`:99`) — critic REFUTED our r10 unconditional
  wording ("whenever the last probe had any violation/error"); SKILL.md
  sharpened accordingly.
- `reconcile`: read-only (empirically zero writes, isolated marker re-test);
  exit 1 only on drift/fetch-error/source-missing — **`no-source-file`/`NOSRC`
  silently exit 0** (`:269-272`); unknown id → **crash exit 1 + raw stack**
  (un-awaited dispatch `:1086`) colliding with the legitimate drift exit 1;
  live runs: ds4cc-com SYNC exit 0 (79 453B live vs 79 422B source), plazir15-ghp
  match exit 0 (reconcile compares live vs **local** sourceDir — the r6
  "5 commits ahead of origin" is invisible to it), fleet 21-row sweep exit 1
  with 7 attention ids.
- `sync-check`: stricter bad-set (`kimi-surface.mjs:206`), `--all`/`--dead`
  undocumented selectors (`:184-190`), unknown id exit 1 via `die` (`:34`),
  unknown verb exit 64; the ~Aug-29 stale ds4cc mirror (75/93 canonical locs
  missing) verdicts **in-sync, exit 0** — vintage lag invisible; `liveSha256`
  **nondeterministic per fetch** (abf822c7→440e3cba→5a80ee93 — never alert on
  sha deltas).

## Landed (kake-shokunin)

- `corpus/knowledge/free-read-verbs.md` — 4 verb cards, three-universe model
  (probe 18 / reconcile 21 / sync-check 15-9-6 rows, counted live), the
  state-persistence model (clobber, merge asymmetry table, `total:1` spot-row
  semantics, reader contract), live-run provenance table.
- SKILL.md — step-1 spot-probe trap + recipe, status-exit sharpening,
  write-path citation fix (`cli.mjs:998-1002` was the install unit template →
  real write path `:78` + `fleet.mjs:39-52`), 3 drift-table rows with live
  exit contracts, cited-paths entry.
- SCORECARD.md 8→9 + move-log row; LOG.md r11 entry.

## Verification

- Sentinel: exactly two sanctioned writes (history +1 line, clobber→restore
  byte-identical, sha `8c5bb8ca…` before==after); `git -C webzites` clean
  check NOT_EVALUABLE — **webzites is not a git repo** (receipts pin by sha
  instead). Sentinel also found the `-newermt` local-time trap (UTC-3 host →
  naive threshold parses as future → vacuous check) — recorded in playbook
  scratch.
- Reviewer: every file:line citation in the drafts verified; 7 off-by-N pins
  corrected before landing (loadLastProbe `fleet.mjs:14-18`, writeJson
  `:20-25`, `at: report.at` `:45`, `total` `:46`, "no probe results yet"
  `:92`, bin import `:5`, reconcile verdict fork `reconcile.mjs:171-173`).
- L1 re-verified all disputed pins against source before landing; smoke run
  `scripts/probe-delta.mjs` on the 77-line history: exit 0, 6 events,
  0 phantom, 11 spot probes suppressed (the new `total:1` row included).

## Honest limits

- The `cmdProbe` merge fix belongs to the webzites owner lane; kake recorded
  the one-line patch proposal (`/tmp/kake-r11/scout-verbs.md` F1) as a
  handoff, never applied it.
- Corrupt-`probe-latest.json` crash path and `--quiet` variant are
  replica-verified (isolated byte-identical copy), not yet real-repo runs.
- Revenger's draft had 2 incoherent cells (sync-check exit family, untested
  `--log` path) — scribe flagged them; only corroborated items were folded.
- Connector: no sibling overlap (kumitate has zero webzites-verb vocabulary;
  kagi CDP-lease boundary respected — reported, not absorbed).

## Round-end actions

kake-shokunin: commit `round-11` + push. Main repo: this report committed +
pushed.
