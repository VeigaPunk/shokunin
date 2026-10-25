# kotodama — round 47 (regimen 2, loop 2 position 1)

**Verdict: NOT ADMITTED on C; O+Ca improved+landed — honest stop.**
opencode-go/deepseek-v4.1-flash 64 seats (key-1 batch 50/64 + key-6 refire 14/14).

## Work performed
- 64-seat AgentSwarm on opencode-go (key-1 50/64, key-6 refire 14/14).
- Claim O landed: `tools/harness/claims-freshness.py` durable freshness gate.
- Claim Ca landed: `calib/queue-successor-r47.json` (corrected).
- Rejection receipt via isolated git-archive replay (`validation.json`).

## Landed changes
- `tools/harness/claims-freshness.py` — pre-dispatch gate; closes R01-43-12.
  Selftest 62/62; r43 regression (O/C stale, Ca fresh, exit 1 + REFUSE);
  negative control green; could-not-evaluate != green.
- `calib/queue-successor-r47.json` + `calib/r43-checks.json` + `calib/r47-checks.json`.
- No corpus delta (C blocked); r42/r44 tools untouched.

## Before → after
- **O (improved):** no durable freshness gate → durable green gate (62/62).
- **C (unchanged/blocked):** fresh cartography gap but 790-line entry (3.6x
  partition max) + 9 blocking defects; not landing-ready; 223 holds.
- **Ca (improved):** loop-1 defects undispositioned → 5 rows classed + corrections.

## SHONEN
- [~] decision tables/checklists cited — the gate's probe registry + the queue successor.
- [~] end-to-end task logged — `validation.json`.
- [~] executable without oral context — seat fragments carry missions+evidence.
- [~] no cross-domain bleed — A03 write-surface audit; only intended writes.

Named non-author reviewers: R01, R02, R03, R04, R05; critics X01-X05; gate Q01.
