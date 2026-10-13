# kasegi-shokunin — round-1 findings

Lane: bounty & security research. Commits `5a0188f` + `49f5945` in
`~/projects/shokunin/kasegi-shokunin` (files: `SKILL.md`, `LOG.md`, `corpus/`).

## What was done

Walked `/home/vgpnk/Projects/bounties` and rewrote the seed SKILL.md into
grounded craft; appended a LOG.md round-1 entry with the evidence list.

Corpus added per `~/projects/shokunin/CORPUS.md`: `corpus/README.md` (index +
coverage map + gaps), five sourced `corpus/knowledge/` entries
(claim-package-contract, policy-access-playbook, ev-model, terminal-classes,
program-quirks), and `corpus/lessons/round-1.md`.
No files outside the shonen were mutated; report written here per protocol.

## Surfaces verified (bytes read, not inferred)

| Surface | What it yielded |
|---|---|
| `claims/` — 275 packages | Real package taxonomy: positive (`ingestion-*`, vuln-slugs), `honest-zero*`, `program-paused`; `submit/BLOCKED.md` residual-gate markers |
| `claims/cantina-pendle/ingestion-20260915/` | Complete positive-blocked exemplar: `claim.json`, `status.json` (BLOCKED, `resume_condition`), `evidence/manifest.json` (v1, polarity + redaction receipts), `custodian` chain, `provenance.json` (pin `f242659`, `policy_sha256`), `claim_checklist.md` ($100 fee gate, SEAL safe-harbor caveat), `submit-payload.json`, `poc/` (5/5 forge) |
| `claims/bugcrowd-seek/honest-zero/` | Complete honest-zero exemplar: `scope-snapshot.json` (coverage.missing semantics), `authorization-envelope.json` (grants/not_granted/stop_reason), `custodian-receipts.json` (HARD_STOP signals), `submit/BLOCKED.md` (hard-gate falsification table) |
| `fleets/mission-template.md` | L1 contract: AR14 = one bounded passive policy read; six-file deliverable spec; reviewer-distinctness; `DONE` vs `BLOCKED` semantics |
| `docs/claim-runbook.md` | `claim-check.mjs` complete gate; `claim-index.mjs`/`prepare-claims.mjs`; submission 100% operator-executed (decree 2026-09-05); H1/Intigriti operator-only actions |
| `docs/claim-ready-index.md` | 12-package operator queue; per-package gate-failure strings for blocked DONEs and stale tags |
| `docs/continuation-notes.md` | 486-mission partition: 438 LEARNED honest-zero, 19 RETIRED auth-walled, 3 RETRY-method, 26 FAILED-infra; precedence rule |
| `docs/wrap-report.md` | 7 canonical packages: 0 GO, 5 GO-WITH-FIX-NEEDED, 2 NO-GO — all blockers were disclosure defects (severity strings, hedging, internal artifacts, stale tags, absolute statements contradicted by provenance) |
| `docs/review-verdicts.jsonl` | 486 verdicts: 430 leave / 50 continue / 6 drop; continue always names an exact next step |
| `docs/autopsies/` (30 files) | Dominant structural failure: auth-walled scope (H1 `/policy` 403, Bugcrowd SPA shell) and terms-gated policy (SIX Group) → hard stop, not work-around |
| `ops/ev-report.mjs` | `adjusted_ev = p_in_scope·p_reproducible·p_unique·p_accepted·expected_reward − (effort_hours·opportunity_rate + direct + delay + risk)`; missing inputs → UNKNOWN, never 0/1 |
| `bounty-map/schema.json` | Draft-07 fail-closed program record (`additionalProperties:false`, required id/name/source_kind/official_url/freshness/lane/mission_state) |

## Skill content shipped

Pipeline map, scope-snapshot checklist with field semantics, per-platform
policy-access playbook, finding-triage decision table (6 terminal classes),
evidence-package anatomy incl. `status.json`/`claim_review` gate semantics,
10 observed disclosure anti-patterns, adjusted-EV model, cited-paths index.

## Open risks / next-round candidates

- Cantina `submit_fee` ($100) + live-balance precondition pattern likely
  generalizes across Cantina programs — worth a per-platform quirks table next
  round.
- `honest-zero` evidence is richer than positive-package evidence (envelope,
  custodian retry files); a minimal honest-zero authoring checklist could be
  extracted.
- No `ops/` validator semantics were re-derived beyond headers/docstrings —
  deep-dive `claim-check.mjs` if a future round needs the full gate list.

## Routing note

Operator interjection applied: scout lanes → `@m_flash` (not `@m_zfl`). No L2s
were dispatched this round; all recon was direct reads.
