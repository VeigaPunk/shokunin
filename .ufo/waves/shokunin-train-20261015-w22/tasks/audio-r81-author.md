# r81 AUTHOR (audio) — GStreamer↔PipeWire lattice

Arm the r81 scout's measured surface: `reports/round-81/r81-scout.md` — the
seven pinned frontier claims (§0 headline table) + receipts
`corpus/live/r81-scout/` (harness `r81_probe.py`, `receipts/s*.json`).
Repo: `/home/vgpnk/Projects/shokunin/audio-shokunin`. Lane harness:
`corpus/fixtures/measure_audio.py` — extend it per repo convention (new
legs/section, insertion-only; prior legs' commands, pins and receipt formats
untouched).

Claims to pin (each = measured values verbatim from the scout receipts):
1. element availability lattice: `pipewiresink`/`pipewiresrc` (v1.6.8),
   `pulsesink`/`pulsesrc` (1.28.6), `autoaudiosink`/`autoaudiosrc` present;
   `openalsink` absent rc=255.
2. naming: `client-name=` renames the *node*; `client-properties=
   props,application.name=` renames the *Client* — the crossover.
3. routing vectors: `target-object=` writes both `node.target` and
   `target.object`; `PIPEWIRE_PROPS` + `PIPEWIRE_NODE` env honored; gst
   element property BEATS `stream-properties` (reverse of r78's `-P` law —
   pin both laws with their authorities).
4. `pulsesink device=`: bogus name → rc=0 silent fallback to default sink;
   record direction refuses same input rc=1 `No such entity`.
5. target-loss split law: playback re-links to default ≤0.2 s and never
   exits; capture does NOT re-link — file freezes at last buffer, no error,
   no EOS, process alive (contrast: pw-record re-links, same session).
6. exit classes: parse refusal rc=1 + no artifact; runtime state-change
   rc=255 + 0-byte artifact; `pulsesrc` outlier rc=1 + 0-byte artifact.
7. `autoaudiosink`→`pulsesink`, `autoaudiosrc`→`pulsesrc` fails rc=1 (r77's
   no-working-default law survives the autodetect wrapper).

Contention rules (r77 flood lesson + scout §10, mandatory): all routing
legs target a seat-owned null sink `gst_r81_auth` or read-only observation;
stream/node names prefixed `gst_r81_*`; verify module index against name
before EVERY unload; never `pactl set-default-sink`/`set-default-source`;
every capture leg triple-bounded (element bound where it exists + wall cap
+ byte cap in the same loop that owns the process group).

Deliverables: new legs armed + green; FULL prior battery replayed ≥2× with
all prior rows byte-identical (counting command + row totals in the
report); `reports/round-81/r81-author.md` with per-claim evidence pointers
and any scout-claim falsification found (correct it and disclose). Do NOT
commit.
