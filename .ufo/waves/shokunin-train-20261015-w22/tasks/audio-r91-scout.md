# r91 SCOUT (audio) — forward reconnaissance, next unscouted surface

Repo: `/home/vgpnk/Projects/shokunin/audio-shokunin`. You are the r91
scout — pre-measure the NEXT surface so the r91 author can arm cells
without exploratory cost. Scouts are leaf seats: zero tracked-file
writes; all scratch under `corpus/live/r91-scout/`; report →
`reports/round-91/r91-scout.md`.

Surface choice (in priority order — read `PROVINCE.md` and the r81–r90
scout reports' "remaining unknowns" sections first):
1. **Mechanism / prior-art read**: r81's unexplained laws — why
   `pipewiresrc` freezes on target loss while `pw-record` re-links
   (gstpipewiresrc.c / pw_stream_connect paths); whether the host has
   readable sources (`/usr/include`, pacman source pkgs, or docs) — mark
   every source claim [I] vs [O] accordingly.
2. If mechanism sources are unavailable: **the WirePlumber/session-manager
   policy surface** — metadata writes via `pw-metadata`, default-routing
   policy objects, `wpexec`/scripts if present.
3. Or the native-pulse client surface (`pacat`/`paplay`/`parecord`,
   `PULSE_SERVER`, `PULSE_SINK`/`PULSE_SOURCE` vectors) wherever r87's
   remote-sink scout left gaps.

Method (established scout contract): build your own probes
(`corpus/live/r91-scout/probes/`, `driver.py`, `audit.py`), every leg
triple-bounded (element bound + wall cap + byte cap, same loop owning the
process group), ≥3 reps per measured claim, byte-stability recorded,
`manifest.sha256` + `RECEIPTS.md`. Seat-owned PipeWire names only
(`gst_r91_*`/`r91s_*` style), module index verified before unload, NEVER
`pactl set-default-sink`/`set-default-source`.

Report: headline claims table, per-claim evidence pointers, author
directives (which cells are verbatim-ready vs bimodal), remaining
unknowns. [O]/[I]/[?] labels throughout.
