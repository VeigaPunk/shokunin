# r81 BASELINE (audio) — frozen-tree regression replay

Repo: `/home/vgpnk/Projects/shokunin/audio-shokunin`, HEAD at dispatch =
the reconcile commit (work commits land later — pin the sha you froze).

Copy the tracked tree into `corpus/live/r81-baseline/tree/` (cp -a or git
archive; do not mutate the worktree). Run the lane's existing fixture
battery there **twice** (`corpus/fixtures/measure_audio.py` battery leg
per its own README/help — use the same invocation prior baselines used;
see `reports/round-80/r80-baseline.md` for the established procedure).

Report: total legs/cells replayed, how many byte-identical vs committed
receipts, any drift row named individually (do not re-run indefinitely to
explain drift — report what you saw). Write
`reports/round-81/r81-baseline.md`. Scratch only under
`corpus/live/r81-baseline/`. Do NOT write tracked files, do NOT commit.

Contention: this is a shared PipeWire host — if the battery exercises
routing, use only the seat-owned names/objects the harness already
creates; never `pactl set-default-sink`.
