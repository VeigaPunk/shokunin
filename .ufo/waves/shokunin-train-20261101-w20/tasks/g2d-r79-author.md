# r79 AUTHOR (g2d) — PhysicsServer2D interior-window lattice (23 cells)

Arm the r79 scout's verbatim cell table: reports/round-79/r79-scout.md
§1.4 (23 rows) + §4 author directives + receipts corpus/live/r79-scout/.
Repo: /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin. Existing Godot
harness: corpus/fixtures/run_battery.py + .gd fixtures (88 cells green).
Extend it: new fixture script(s) (e.g. phys2d_events.gd) + appended CASES
insertion-only; keep love_battery.py untouched this round.

Classes to pin (from §1.1/1.2): the two interior windows
(contact_monitor RigidBody2D vs monitoring Area2D) on the same scene —
write lattice identical, writes refused (rigid_body_2d.cpp:605 /
area_2d.cpp:429), set_deferred deferred, max_contacts_reported applied
in-cb, direct_space_state available inside both windows (cb_dss_null=false,
cb_q_hits=1), per-tier handle behavior, threading-invariance rows,
fail-closed pins (§2 evidence must hold: muted/absent channels fail).
Also note the errorhandler/windowed-surface guard from r78's ledger:
any new love-side run must keep the strict conf; if you add a headless
love.errorhandler print-and-quit override to make windowed error screens
impossible on stray invocations, keep it in a NEW file (never modify
love_phys_probe/main.lua — its receipts are committed pins).
Run the full Godot battery at least twice post-landing; prior 88 rows
byte-identical. Report -> reports/round-79/r79-author.md. Do NOT commit.
