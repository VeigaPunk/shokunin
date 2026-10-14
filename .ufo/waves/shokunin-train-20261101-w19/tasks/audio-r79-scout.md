# r79 SCOUT (audio) — the pw-loopback / filter-chain DSP surface

Untested runtime surface: PipeWire's own DSP graph. Measure:
pw-loopback (capture/playback props, -C/-P matrix mixing, its target
resolution behavior — does it obey the same fallback lattice?),
filter-chain conf.d loading (a minimal graph conf, error on parse vs
runtime), pw-cat --playback with -P node latencies, the
stream.capture.sink prop on PLAYBACK-side tools, and
pw-record --target against a pw-loopback-created capture port.
Also: the hot-plug pseudo-surface — module-load/unload of a null sink
while a loopback is routing through it. Bounded probes (timeout 15s),
witness with pw-link + content taps, scratch corpus/live/r79-scout/;
report -> reports/round-79/r79-scout.md. Do NOT touch
measure_audio.py (r78 author in flight).
