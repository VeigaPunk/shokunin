# Plan — protocol round 14
**Spec:** `.ufo/prompts/protocol-round-14.md` + `PROTOCOL.md` **Author:** protocol L1, 2026-09-28

## Data walk

See `.ufo/waves/round-14/data-walk.md`. Both owned axes tie at 8; choose the queued protocol-soundness compaction because the current candidate has a measured pass against its expanded preservation gate. The closure checker separately reports live fleet debt and remains explicitly unclean.
## L2 dispatch

- The planner seat was dispatched first for a read-only plan check.
- One subsequent batched task call launched 10 L2 seats: two scouts, two executors drafting only to unique scratch paths, plus critic, connector, reviewer, sentinel, revenger, and scribe. The MISSION route buckets were included in the assignments.
- The task API exposes role selection but no model parameter; the requested `@m_lunamax` / `@m_flash` provider routing cannot be independently attested from this surface.
- All reviewers were told not to edit source files or run tests/builds/formatters. Their findings remain advisory; L1 integrates only evidence-backed changes.


## Milestone

### M1 — Preserve one canonical protocol across the compact body and incident appendix
**Does:** independently review the inherited 464-line `PROTOCOL.md` + 47-line `PROTOCOL-APPENDIX.md` candidate; retain it only if the cited meanings, anchors, modal floor, cross-references, and required appendix rows remain sound. Record the already measured baseline 526 lines / 49,269 bytes and candidate 464 lines / 40,079 bytes. Do not rewrite the uncommitted round-13 marker or aggregator-owned scorecard section.
**Gate:** `sh .ufo/waves/round-13/verify-protocol.sh PROTOCOL.md --appendix PROTOCOL-APPENDIX.md` → clean; `--selftest` → 18/18; census → 169/169. Rerun after final integration. A falsified obligation, unresolved required pointer, weakened normative meaning, or gate failure blocks raising the score.
**Touches:** `PROTOCOL.md`, `PROTOCOL-APPENDIX.md`, protocol-owned rows in `SCORECARD.md`, append-only `LOG.md`, `.ufo/waves/round-13/` evidence needed to rerun the gate, `.ufo/waves/round-14/`, and `.ufo/reports/round-14/protocol.md`.
**Out of scope:** watchdog/script/manifest semantics, unrelated closure debt, aggregator scorecard hunks, sibling repos and domain sources. Preserve the live closure-gate result (debt 15) without calling it clean or silently folding it into this one-axis move.
