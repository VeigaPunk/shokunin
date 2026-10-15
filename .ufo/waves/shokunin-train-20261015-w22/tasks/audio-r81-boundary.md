# r81 BOUNDARY (audio) — honest edges of the gst↔pipewire claims

Repo: `/home/vgpnk/Projects/shokunin/audio-shokunin`. Read
`reports/round-81/r81-scout.md` — work its §11 "remaining unknowns" and
the edges of each pinned claim. You are a bounded empirical probe: run
real `gst-launch-1.0`/`pactl`/`pw-dump`/`pw-link` legs, each triple-bounded
(num-buffers where it exists + wall cap + byte cap, same loop that owns
the process group).

Probe candidates (pick the sharpest, measure, don't enumerate all):
- `on-disconnect` vs a *peer stream that closes itself* (producer exits
  while sink node lives) — the scout only tested target-node destruction.
- `PIPEWIRE_REMOTE` / `PIPEWIRE_NODE` interplay on capture vs playback.
- gst element prop vs `stream-properties` precedence on the *capture*
  side (scout pinned it on playback; same law or split?).
- `pulsesink device=` bogus-name silent fallback — does the record side's
  rc=1 refusal hold for `pulsesrc device=` variants the scout didn't try?
- The r81 scout's frozen-file claim at buffer granularity: exact freeze
  size vs `num-buffers` boundary.

Isolation: seat-owned objects only (`gst_r81_bnd_*` names, own null sink
`gst_r81_bndns`), module index verified before unload, NEVER
`pactl set-default-sink`/`set-default-source` (shared host, other lanes
live).

Report → `reports/round-81/r81-boundary.md` with receipts under
`corpus/live/r81-boundary/` (per-leg cmd/stdout/stderr sidecars). Mark
[O]/[I]/[?]. No tracked-file writes, no commits.
