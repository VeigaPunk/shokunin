# kagi round-8 — transcript-hygiene gate

## What landed (kagi-shokunin/, commit `148ae5c` `round-8`)

- `corpus/transcript-scan.sh` — repeatable secret-leak gate over the durable
  transcript DB (`$STATE_DIR/xdg-data/opencode/opencode.db`). 270 cells × 30
  patterns over every text-bearing column + row-count tripwires on the 5
  credential-bearing tables (`account`, `account_state`, `control_account`,
  `credential`, `session_share` — schema confirmed to carry NOT NULL
  `access_token`/`refresh_token`/`value`/`secret` columns; all empty).
  Counts-only output (never matched text), `file:…?immutable=1` open (no
  `-wal`/`-shm` side effect — re-verified: `-readonly` mutated them,
  immutable did not), `--selftest` seeded-hit check, exit 0/1/2.
- `corpus/knowledge/transcript-hygiene.md` — schema census, two-tier
  semantics (HIT = material shapes exit 1; WARN = credential-language
  field names, exit stays 0), triage/purge procedure, bounds.
- `corpus/lessons/round-8.md` — false-positive taxonomy lesson: first single-
  tier pattern list fired 5 hits on the real DB, all request text *discussing*
  credentials; tier split preserves gate credibility.
- SKILL.md: decision-table row, gate paragraph in on-disk section, checklist
  item, 3 anti-patterns, falsification bullet.
- Corpus rot fixed: README `Model endpoint drift` bullet was truncated
  mid-sentence since the round-7 commit (completed); `MODEL_ENDPOINT`
  stale line ref corrected L17→L19 in SKILL.md, README,
  `janitor-env-contract.md`, `lessons/round-4.md`.

## Baseline / verification

- `transcript-scan.sh` real run: `TRANSCRIPT_SCAN: CLEAN (cells=270
  patterns=25+5 warns=4 schema-absent=0)`, exit 0; all 5 credential-table
  tripwires empty. WARN cells = 4 (`api_key`×3, `refresh_token`×1) across 5
  distinct sessions — requests naming credential concepts, no material.
- `--selftest`: seeded fake `op://` + populated `credential` detected
  (exit 1); clean scratch db exit 0; missing db / bad args exit 2.
- `drift-pins.sh`: 13/13 pinned host files unchanged.
- L2 reviewer (17 claims): 15 VERIFIED, 2 corrections applied (WARN spans
  5 distinct sessions not 4; truncation introduced round-7 not round-4;
  also caught my lesson quoting WARN-row text → redacted to categories).

## Open operator items (unchanged, all documented)

- Endpoint drift: `opencode.json` `baseURL` → 127.0.0.1:34113.
- Control-plane auth: `OPENCODE_SERVER_PASSWORD` + `client.py` header
  (recipe: `control-plane-hardening.md`).
- Successful `request` still needs operator `op signin`.
- New this round: no purge verb — transcript hygiene is now monitorable but
  deletion remains manual (stop + `rm -rf xdg-data`).

No vault access; no secret values, ref paths, or row contents in any
artifact. In-flight at report time: sentinel coverage lane (advisory only).
