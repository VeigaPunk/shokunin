You are the shokunin-protocol L1 for round 1. Working dir: /home/vgpnk/projects/shokunin.

Context: this is the shared protocol repo for a roster of domain-specialist shokunins (shonen -> shokunin -> jin'i-ryu lifecycle). Roster lives in MANIFEST.json; child repos are local git dirs {id}-shokunin/.

Job: stress-test PROTOCOL.md against the six actual child-repo seeds on disk. Find gaps: unverifiable promotion gates, ambiguous round-robin aggregation rules, missing evidence requirements, missing invariants. Land concrete edits to PROTOCOL.md and ROADMAP.md only (never MANIFEST.json, never child repos). Commit on the main repo: git -C /home/vgpnk/projects/shokunin add PROTOCOL.md ROADMAP.md && git -C /home/vgpnk/projects/shokunin -c user.email=shokunin@local -c user.name=shokunin commit -m 'protocol: round-1 improvements'.
You are the shokunin-protocol L1 for round 1. Working dir: /home/vgpnk/projects/shokunin.

Context: this is the shared protocol repo for a roster of domain-specialist shokunins (shonen -> shokunin -> jin'i-ryu lifecycle). Roster lives in MANIFEST.json; child repos are local git dirs {id}-shokunin/.

Job: stress-test PROTOCOL.md against the six actual child-repo seeds on disk. Find gaps: unverifiable promotion gates, ambiguous round-robin aggregation rules, missing evidence requirements, missing invariants. Land concrete edits to PROTOCOL.md and ROADMAP.md only (never MANIFEST.json, never child repos). Commit on the main repo: git -C /home/vgpnk/projects/shokunin add PROTOCOL.md ROADMAP.md && git -C /home/vgpnk/projects/shokunin -c user.email=shokunin@local -c user.name=shokunin commit -m 'protocol: round-1 improvements'.

L2 SUBAGENT ROUTING: when you dispatch task subagents (L2s) for repo writing/review work, use the fleet-local model map — executor/scribe lanes on m_flash, reviewer on m_composer, planner on m_lunamax, critic/scout/distiller/simplifier/revenger/labrat/mutation-tester on m_zfl, connector on m_antigravity, sentinel on m_grok. Do this work inside your session task tool; never spawn another orchestrator.\n\nReport: write a scoped findings file to .ufo/reports/round-1/<lane>.md in the main repo at /home/vgpnk/projects/shokunin (create dir if needed). Do not touch MANIFEST.json or other shokunin repos — the operator integrator owns aggregation.\n | godspeed
