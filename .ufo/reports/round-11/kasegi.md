# kasegi-shokunin — round 11 report

**Gap closed:** the intake surface — `bounty-map/programs/` (largest unread
dataset, 1088 records) + `.ufo-ingestion/` (unwalked intake lane) +
`fleets/registry.json` (last open known-gap, resolved in-domain).

**Deliverables:** `corpus/knowledge/intake-surface.md` (new),
`SKILL.md` + Intake surface section + 3 cited paths, `corpus/README.md`
coverage row + registry gap CLOSED, `corpus/lessons/round-11.md`, LOG.md
entry. Commit `fb9ac8e` (`round-11`).

## Headline findings (all live-verified 2026-09-28)

- **The map is decorative state.** `mission_state` = DISCOVERED×1087 /
  PLANNED×1, never advanced; `fleet-dispatch.mjs::programState()` reads it
  only for a `--dry` log line. `lane` = executor×1088. `ev_inputs`
  non-empty×1 → `ev-report` is UNKNOWN for 1087 programs, `rank.mjs`'s
  curated gate passes on a population of one. Dispatch scores only
  `priority(9e12) > continue(2e12) > curated(1e12) > reward.min×1000` —
  ~1040 records score 0/1. Real state: `ledger/missions.jsonl` +
  `fleets/run/`; real termination: TERMINAL status + telemetry attempts≥2.
- **A second intake path bypasses the map entirely.** The 2026-09-14
  `.ufo-ingestion/` cycle (16 scouts, grok 403 spending-limit →
  `devin/swe-2:max` reroute) EV-ranked 32 programs and seeded 13 directly
  into `claims/*/ingestion-20260914/` — 22 claims dirs have no map record,
  including 7 of the 12 queue rows and all Cantina/immunefi archive dirs.
  Map↔claims name drift (bugcrowd-spacex vs -starlink, github-bug-bounty vs
  github-bounty) breaks id joins.
- **All records share one `refresh_run_id`** (`refresh-20260829…`, 30 days
  stale); `check-freshness.mjs` exits 1 (358 h vs 26 h) — the AR4 alarm is
  standing state. `validate.mjs` OK. 352 map programs never touched.
- **`.ufo-ingestion/claim-tracker.py` is a dead third watcher** —
  READY.md/no-BLOCKED.md standard (weaker than claim-check), also scans the
  origin-work `claim-packages` receipt tree; last cycle 2026-09-14T20:40Z.
- **`fleets/registry.json` is the decree ledger**, not just routing:
  `operator_decrees` carries claim-queue order (mozilla→spotify→airtable→
  intel), the **3cx never-filed decree** (free disclosure pending rep —
  explains the DONE-but-never-submitted anomaly), intel hold (no Intigriti
  KYC), freebie-class ATTRIBUTED superseding anonymous, paid-track accounts
  `vgpnk1337`/`veigapunk`, severity-evidence-trail. File accretes with
  in-place `superseded` markers (astra simultaneously doctrine-banned and
  LIVE-routed).

## Cross-domain (reported, not fixed — bounties owner)

Standing stale-board alarm, ingestion claims lacking map records, dead
claim-tracker, map↔claims id drift, and the never-run ingestion cycle 2
(~80-program deferred frontier enumerated in `cycle-20260914T171257Z.md`).

**Residual gaps:** `george/` stays parked; `.ufo/bh*/`, `sessions/`,
`.ufo/bounty-fleet/`, `grok-bounty-assessment-20260911` un-censused.
