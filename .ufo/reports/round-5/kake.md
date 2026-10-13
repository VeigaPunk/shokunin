# kake-shokunin — round 5

Domain: web properties & publishing (ds4cc.com, kimi.page/pro mirrors, Pages deploys).
Commit: `18537e9 round-5` in `kake-shokunin/`. Evidence-only round — zero probes fired, zero deploys, zero metered ops.

## Gap closed

The corpus covered the *static* playbook (registry, verbs, drift commands, journal codes) but had zero coverage of the **ops layer already running** and the **repo-evidence lane that had already answered the corpus's own "known gaps"**. Three new knowledge files:

- `corpus/knowledge/ops-automation.md` — `webzites-probe.timer` (systemd user, `OnUnitActiveSec=6h`, `SuccessExitStatus=1`) + `webzites-keeper.timer` (daily `grokbot tick`); `probe-history.jsonl` (76 rows) semantics and observed transitions; full `webzites.mjs --help` verb table including the previously-undocumented `bots`/`grokbots`/`speedrun`/`install`/`auth`/`map` surface.
- `corpus/knowledge/origin-repos.md` — the 50-clone `~/Projects/webzites/repos/` canonical-source map from wz-repos r1–r8 (terminal 2026-09-21): byte-verified writers, name-trap receipts, 5 sourceless artifacts, fleet.config `sourceDir` drift.
- `corpus/knowledge/speedrun-pipeline.md` — the second publish surface (record→report→prep→operator-push→X-draft) with its fail-closed schema, redaction denylist, and no-upload-API rule.

Also updated: `SKILL.md` (check `probe-latest.json` age before re-probing; speedrun gated lane; cited paths for units/repos/state), `corpus/README.md` (coverage map + rewritten gaps), `corpus/lessons/round-5.md`, `LOG.md`.

## Key evidence

- `probe-history.jsonl` transitions: `veigapunk-page` left `violated[]` between 09-21T04:14 and 09-22T22:58 (human publish click); `charter-ghp` entered `violated[]` 09-27T00:22→06:22 (marker churn, not outage); `lucario` appeared already-violated at total 17→18 (registration event); `xsnapshot-app` constant `errors[]` = armed NXDOMAIN baseline.
- `repos-r5` byte-verdicts: `ds4cc-website` is NOT the ds4cc.com source (sha `70b2241e…` ≠ live `b6f65899…`); `burnerchrome.kimi.page` canonical = `repos/burnerchrome`, not the vendored `ds4cc-marketplace/burnerchrome/`.
- README's prior "known gaps" were stale: probe cadence answered by `probe-history.jsonl`, the 50 repos answered by `repos-r8.md`.

## Residual gaps (next rounds)

- 5 sourceless kimi artifacts → extraction is operator-gated.
- GHP subpath rot beyond `index.html` — no spotcheck tool exists.
- kimi `apiv2` authenticated ops — recorded, intentionally unwired.
- Alerting on `violated[]` deltas vs silent log — undecided operator preference.
