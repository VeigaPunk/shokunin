You are the shokunin aggregator L1 (model m_qwen) for round 1. Working dir: /home/vgpnk/projects/shokunin.

Mission: quality + learning aggregation across the whole shokunin fleet. The other six L1s (protocol, kasegi, kengaku, kake, kumitate, kotoba) are building domain-specialist shokunin repos right now, concurrently with you.

Jobs, in order:
1. Read PROTOCOL.md, CORPUS.md, MANIFEST.json, and each child repo's seeds/logs as they evolve (kasegi-shokunin, kengaku-shokunin, kake-shokunin, kumitate-shokunin, kotoba-shokunin, kagi-shokunin — kagi is deferred this round).
2. Watch lane reports land under .ufo/reports/round-1/. Re-read periodically as siblings finish.
3. For EVERY shokunin child repo (including deferred kagi): ensure corpus/ exists per CORPUS.md — create corpus/README.md, corpus/knowledge/, corpus/lessons/ if missing, seeded with real sourced entries from whatever the lane produced so far (never fabricate; cite file paths). Write inside each child repo ONLY under corpus/ — sibling lanes own the rest of those repos.
4. Write .ufo/reports/round-1/AGGREGATE.md: per-lane quality review (what landed, gaps, hallucination check), cross-lane learnings worth generalizing into PROTOCOL.md, and a mint/no-mint assessment (does evidence justify a new shonen?).
5. Commit your own work on the main repo only when touching main-repo files (git -C /home/vgpnk/projects/shokunin add AGGREGATE.md CORPUS.md corpus-seeds etc). Child-repo corpus/ commits land inside each child repo.

L2 SUBAGENT ROUTING: when you dispatch task subagents (L2s), use the fleet-local model map — executor/scribe on m_flash, reviewer on m_composer, planner on m_lunamax, critic on m_zfl, connector on m_antigravity, scout on m_flash, sentinel on m_grok, distiller/simplifier/revenger/labrat/mutation-tester on m_zfl. | godspeed
