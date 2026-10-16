# audio-r90-foldfix

Lane repo: /home/vgpnk/Projects/shokunin/audio-shokunin | Round: 90 | Landed f50cf66a | adjudication a2c6e3b7
Critic fold-required + reviewer/scribe findings. Fix the wpstate/pw-link/wpformat family in corpus/fixtures/measure_audio.py (r95 fold template applies — _jack_r95_* in same file is the reference implementation).

Required: (FF1) entry["legs"] preserved + receipt written AFTER teardown on every block/exit path, never failures:[] with 0 legs; (FF2) family lock -> host-global $XDG_RUNTIME_DIR bounded LOCK_NB + stale handling; (FF3) phantom-tunnel + k_w_late race legs -> retry-once-record-both (w_settings pattern), name unknown refusal class; (FF4) receipts carry seat + fixture_sha256; stop citing untracked corpus/live paths; (FF5) store-residue census leg (r90a_ rows persist structurally); (FF6) doc fixes in r90-author.md (k_w_late run attribution, stderr shape).

Contract: work on lane HEAD; do NOT commit. Before/after archive-tree runs on the responsive daemon (bounded pactl info first); green must show legs+census populated, negative probes named. File reports/round-90/r90-foldfix.md.
