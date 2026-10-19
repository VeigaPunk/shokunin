# Protocol round 16 — L2 dispatch receipt

Dispatch evidence lives here, not under `.ufo/prompts/`: this round was dispatched by the kaika
orchestrator, not by the driver's `lane_prompt()`, so no driver prompt file exists for it. The L2
seats were spawned by the protocol L1 in ONE batched `task` call (2026-10-19), every prompt
leading with `/skill:godspeed` plus the verbatim bytes of `~/.agents/skills/godspeed/directive.md`;
no model was passed (session route table). Transcripts are session-scoped; their durable outputs
are the files named below.

| seat | role | write set | outcome | durable output |
|---|---|---|---|---|
| R16Planner | planner | none | completed — measurement plan; recommended holds unless non-author review clears a soundness raise | SCORECARD G/P rows |
| R16Connector | connector | none | completed — anchors, operator-side name alignment, incident cross-links, 0 merge-conflict risk across kaika worktrees | appendix row "Root ledger identity" cross-links |
| R16Ledger | executor | `SCORECARD.md`, `LOG.md`, `.ufo/waves/round-16/clobber/**`, `.ufo/waves/round-14/registry-home-rerun/**` | completed | `clobber/classify.{sh,out}`, LOG correction entry, registry row, 12 restored files |
| R16Gate | executor | `.ufo/gates/root-ledgers.py`, `.ufo/gates/root-ledgers/**`, `.ufo/waves/round-16/gate/**` | **failed mid-run — provider rate limit** (`resource_exhausted`); left a duplicated `GATE_DIR` | gate, fixtures, `mutate.sh` (repaired by L1, see `gate/runs.md`) |
| R16ProtocolText | executor | `PROTOCOL.md`, `PROTOCOL-APPENDIX.md` | completed; L1 then kept one pointer on a single line, made appendix pointers repo-resolvable, reworded two external section refs that the round-13 verifier read as xrefs, and added an interim-authority clause | 4 rules + 4 appendix rows |
| R16Scribe | scribe | `.ufo/waves/round-16/before.md` | completed; caught the L1's wrong kotoba commit attribution (`c8e233d` → `b7470d7`) | `before.md` |
| R16Scout | scout | none | completed — carry set = 0 | LOG correction entry "Carry-forward" |
| R16Reviewer | reviewer | none | completed — independent difflib re-derivation (165/165 SCORECARD, 1299/1299 LOG added lines in kotoba `b7470d7`; 0 not-in-kotoba) | SCORECARD G6 |
| R16Critic | critic | none | **failed at start — provider quota (429)**; revived by message, then reviewed the landed state: 15 findings, 0 block | fixes 1, 2, 4, 5, 6, 8, 13, 14 applied; 3 (LOG prefix gate) queued in §Planned |
| R16GateRedo | executor (fresh re-dispatch per orchestrator route note) | same as R16Gate | **failed at start — provider capacity** (`turn_rate_limit_exceeded`); changed nothing | — |

Seats in the batched call: 9 (≥ 8). Seats that ran to a result: 8 (critic after revival).
