# r87 CRITIC (g3d) — adversarial gate review of the landed arm

Review commit c57fa40 (body-tier direct-state lattice: body_handle,
acq_use, step_stamp, write_loss, body_tier, freed_space). Reproduce
every gate from the receipts; try to forge PASSes (self-printed lines,
missing conjuncts, identity pins that a different object could satisfy).
Check: the write-loss row's precondition+tally pins are real (scout's
loss did not replicate — is the row honest about measuring
non-loss?); the freed_space two-mode Jolt crash disjunction
(rc 134/137 + witness); held-handle identity pins can they be
satisfied by a stale object. Report -> reports/round-87/r87-critic.md.
Read-only on tracked files; scratch corpus/live/r87-critic/.
