# r78 CRITIC (audio) — adversarial review of the landed playback lattice

Review commit d9aa6f9 (--probe-capture-r78: 8 entries, 60+ legs).
Reproduce each gate from the final receipt
(corpus/live/runs/20261014T221945369366Z-capture-r78/measurements.json);
forge PASSes where possible (self-printed markers, conjuncts a wrong
outcome satisfies, legs that pass vacuously). The r78 boundary found
exploits the arm does NOT cover (pcm_stolen_silent_success,
default_metadata_triple_divergence, dup_name_lowest_serial_wins,
late_bind_retarget, move_revives_unlinked, suspend_advisory_wakeup,
class_segv_consumer_partition, aplay_file_fmt_refusal) — check whether
any landed cell's pins could be satisfied by those mechanisms.
Also probe: does every leg fail closed (missing file/absent key ->
anomaly not pass); are the named-class leaves asserted or just
recorded (r77's repeat wound). Report -> reports/round-78/r78-critic.md.
Scratch corpus/live/r78-critic/. Read-only on tracked files.
