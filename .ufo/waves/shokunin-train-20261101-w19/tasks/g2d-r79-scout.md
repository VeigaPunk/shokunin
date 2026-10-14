# r79 SCOUT (g2d) — refine the Godot-2D PhysicsServer2D arm into cell-ready pins

reports/round-77/r77-scout-godot.md already MAPPED the surface (88
cells zero server-side; write/read two-tier rule reproduces g3d r85
cell-for-cell; threaded fetch gate at godot_physics_server_2d.cpp:281;
script-size accident band (308,508]). Your job: turn that map into a
CONCRETE r79 arm — run each proposed cell on the real Godot 4.7.2
harness and pin the expected receipt fields (exit codes, error text,
per-tier handle behavior, contact_monitor on/off partition, RigidBody2D
interior partition inside body_entered). Deliver a cell table the
author can arm verbatim. Scratch under corpus/live/r79-scout/;
report -> reports/round-79/r79-scout.md. Do NOT touch love_battery.py
or main.lua (r78 wave-B in flight).
