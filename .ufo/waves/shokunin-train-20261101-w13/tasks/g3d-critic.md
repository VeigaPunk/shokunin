# r82 CRITIC (g3d) — adversarial falsification of the r82 claim + diff

Read SHARED.md + the r82 author brief + scout report when it lands.

Attack the claim's weakest joints: over-generalized wording, wrong variable attribution, missing controls, parser artifacts posing as behavior, timing-vs-semantics confusion. Build counterexample probes in your scratch (corpus/live/r82-critic/). When the author diff lands (watch the worktree), replay it, run mutants (collapse controls, forged inputs), and report per-finding severity + repro commands. Your corrections have repeatedly changed the landed claim — be specific, cite file:line.
Report -> reports/round-82/r82-critic.md.
