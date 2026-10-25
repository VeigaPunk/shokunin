# r75 AUTHOR (audio) — consumer-class breadth: paplay + aplay + ffplay

Read SHARED.md + r74 author/adjudicator first.

ARM — three NEW consumer runtimes on the canonical member x transport
matrix (the r73 consumers-r73 shape, new ledger family
`--probe-consumers2-r75`):
- `paplay` (PulseAudio client over pipewire-pulse): daemon-gated like
  pw-cat; the compat layer is the interesting axis — does paplay's
  libsndfile path inherit the same name axis (.snd fork)? Measure
  per-member transport matrix + a name-axis control on identical bytes
  via {named-fifo, rfd}.
- `aplay` (ALSA direct): NO daemon — kernel device coupling. Viability
  is conditional on an ALSA device existing; on this host check
  `aplay -l` first — absence is an honest `blocked` verdict (record
  the exact device enumeration), never fabricate.
- `ffplay` (SDL+lavf): a second lavf consumer — does it share mpv's
  inverted-seek fork on dec_hcom, or does SDL's pull-model avoid the
  refresh seek? `--autoexit --nodisp` + `-an`/`vn` flags as needed for
  headless; parse its own log surface (stderr) for detect+seek+decode
  fields; never bare rc.
Per-consumer ops rows: daemon/device gates (paplay->pulse, aplay->ALSA
card, ffplay->SDL audio driver — SDL_AUDIODRIVER=dummy for determinism),
hang classes under the writerless-fifo cell, kill semantics.
All fifo arms `timeout -s KILL`. Prior rows byte-identical.
Report -> reports/round-75/r75-author.md.
