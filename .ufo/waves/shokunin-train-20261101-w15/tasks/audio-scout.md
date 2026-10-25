# r76 SCOUT (audio) — pre-measure the capture surface
Read SHARED.md + r76 author brief. Measure FIRST in
corpus/live/r76-scout/: capture-source inventory on this host
(`pactl list sources short`, `pw-link -o`, `arecord -l`, ffmpeg mux
presence for -f pulse/-f alsa), whether each consumer can produce bytes
at all, SIGTERM partial-write behavior per consumer, and which cells are
viable vs blocked. Falsify the brief's frame early. Report ->
reports/round-76/r76-scout.md.
