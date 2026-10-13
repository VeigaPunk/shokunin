# kasegi — round 6

**Gap chosen:** the retirement half of the mission pipeline —
`ops/park-disposition.mjs` + `docs/autopsies/` (31 files) — cited in
SKILL.md since round 1 but never distilled: who writes autopsies, how
parked missions get classified, and what the artifact contract is.

**Landed (all inside `kasegi-shokunin/`, commit `d31f4ca` on master):**

- `corpus/knowledge/retirement-autopsies.md` (new, ~6.5 KB):
  - `ops/park-disposition.mjs` full read (80 lines): dry-run default,
    first-match regex chain over `status.json.detail` —
    `honest.zero`→LEARNED no-op, H1-SPA wording→RETRY_METHOD (GraphQL
    workaround exists), AUTH keyword→RETIRE_AUTH, transient→RETRY,
    else REVIEW. `--apply` un-parks retries (status `rm` +
    `mission_unparked` telemetry) and produces autopsy + RETIRED status
    rewrite + `mission_retired` telemetry.
  - Autopsy schema: fixed five-part generated artifact; requeue =
    operator session token or public policy page, then delete BOTH
    `docs/autopsies/<id>.md` AND `fleets/run/<id>.status.json`.
  - 31-autopsy sub-cause census: auth-walled SPA ×27, terms-gate ×1
    (hackerone-six-group), privacy hard stop ×1 (hackerone-airtable),
    paused/non-enumerable ×2 (blockopensource, sky-plc-mbb-og2).
    Generated "Why" boilerplate mis-describes non-login sub-causes —
    `Reason (verbatim)` is authoritative.
- `SKILL.md`: new "Retirement lane — autopsies & the detail regex"
  section; corrected `docs/autopsies/` count 30→31; added
  `ops/park-disposition.mjs` to cited paths.
- `corpus/README.md`: coverage-map row + lessons list updated.
- `LOG.md`: round-6 entry with evidence.
- `corpus/lessons/round-6.md`: closed items, friction, parked gaps.

**Cross-domain evidence (belongs to `~/Projects/bounties` ops, reported
not absorbed — per PROVINCE.md):**

- **Disposition regex drift.** Re-running the exact classifier live over
  `fleets/run/` (703 statuses, `ls fleets/run/*.status.json | wc -l`)
  gives: LEARNED 529 / REVIEW 85 / RETIRE_AUTH 30 / RETRY_METHOD 1 /
  RETRY_TRANSIENT 1. The 85 REVIEW are almost all the same auth-wall
  failure in newer wording — "no exact in-scope assets",
  "active-testing grant", "custodian HARD_STOP", "SCOPE_UNVERIFIABLE" —
  that the AUTH regex doesn't match, so they park invisibly: never
  autopsied, never retried. Evidence: classifier replay script in
  `retirement-autopsies.md` §regex-drift. Fix candidates: extend the
  AUTH regex to the newer phrases, or standardize `detail` emission to
  include a literal keyword (`in_scope_assets empty`, `no testing
  grant`, `auth-walled`).

**Commit:** `d31f4ca` `round-6` on `kasegi-shokunin` master
(`git -C kasegi-shokunin log --oneline -1` → `d31f4ca round-6`;
5 files, +217/−2).

## SHONEN

- [x] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — six grounded sections now incl. retirement-lane
  classifier semantics; every claim cites a repo path or command output.
- [x] At least one end-to-end domain task executed and logged — six
  rounds of sourced corpus work; LOG.md rounds 0–6.
- [x] Instructions executable without oral context — corpus knowledge
  files are self-contained with verbatim schemas, regexes, commands.
- [x] No cross-domain bleed — PROVINCE.md still accurate; the regex-drift
  defect found inside `~/Projects/bounties` was reported to the
  orchestrator, not fixed from this lane.
