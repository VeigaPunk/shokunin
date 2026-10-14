# r85 SCRIBE (g3d) — evidence audit + receipt provenance

Read SHARED.md. Audit r83->r85 evidence integrity:
- verify the landed r84 receipts: every verdict-map key in the jolt
  child.log re-derivable; the phase_delta markers consistent; confirm
  the child.log's jolt_dss_class line is a real CHILD_RESULT (pinned)
  not a NOTE.
- verify the r84 fold deltas: threaded child.log identical modulo the
  --arm=threaded_edge addition (invisible in output); jolt child.log
  gains exactly one jolt_dss_class line; all 188 verdict rows
  identical.
- child.log provenance hazard: confirm remove_absolute is present in
  both arms (prevents stale-map forge); confirm no receipt cites a
  log path that can hold stale content.
- check the BLOCKED arm path exists and is reachable-but-unexercised
  (Jolt present on this build) — record as known-unexercised branch.
- enumerate fixture-sha citations in landed reports vs current tree —
  flag any citation that no longer resolves (post-fold drift).
Report -> reports/round-85/r85-scribe.md.
