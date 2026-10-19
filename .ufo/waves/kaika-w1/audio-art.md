# kaika W1 — ART dossier · lane `audio` (game audio production)

- Author: W1ArtAudio (scout, leaf; no subagents). Written 2026-10-19.
- Repo: `/home/vgpnk/Projects/shokunin/audio-shokunin`, HEAD `defbe128` (2026-10-18). I read only what the ART shape names, plus targeted greps.
- Tools: `web_search` worked. Every row below was opened in this session. Host checks ran on the fixtures read-only: ffmpeg wrote to `-f null -`, and curl output went straight into grep or pdftotext.
- Prompt injection: none seen. Fetched pages had only marketing calls to action (for example Sonniss "share this page"). I followed no instruction found in fetched content.
- Notation: [OBS] is observed this session. [INF] is inference. [GAP] is unresolved. `n — command` gives a count and the command that produced it. Inside table cells, `\|` stands for a literal `|` when you paste a command. All relative paths are relative to the lane repo root.

---

## 1. Uncovered ground: what the lane already holds

### 1.1 Files the ART shape reads

| ART input | State | Evidence |
|---|---|---|
| `corpus/README.md` (coverage map + `## Frontier`) | **absent** | `0 — ls SKILL.md corpus/QUALITY.md corpus/README.md corpus/SOURCES.md 2>/dev/null \| wc -l` |
| `corpus/QUALITY.md` | **absent** | same command |
| `SKILL.md` headings | **absent**. README says SKILL.md is "absent on lanes still in shonen seed form" (`README.md:10-11`) | same command |
| `corpus/lessons/` | **absent** | `0 — ls -d corpus/lessons 2>/dev/null \| wc -l` |
| `PROVINCE.md` | present. It has no Core/Frontier/Adjacent headings | `0 — grep -cE '^#+ *(Core\|Frontier\|Adjacent)' PROVINCE.md` |
| `corpus/knowledge/` | 14 entries | `14 — ls corpus/knowledge/*.md \| wc -l` |

**PROVINCE ownership.** `PROVINCE.md:3-5`: "Owns: game audio production — SFX ... and soundtrack (motifs, loops, stems, adaptive layers) — verified by headless analysis". PROVINCE also refuses publishing, sample-rights clearance, engine source mutation and mechanics (`PROVINCE.md:13-15`). It asks for a reference ledger that keeps "attribution / rights / training permission kept distinct" (`PROVINCE.md:10-11`).

**Knowledge held.** 10 of the 14 entries are SoX_ng or ffmpeg decoder and transport internals: `10 — ls corpus/knowledge | grep -cE 'sox|ffmpeg'`. The other four are:
- `seed.md`: toolchain census and production map
- `2026-10-12-audio-checklist.md`: 9 mint probe rows
- `2026-10-12-fixture-battery.md`: synthetic fixtures
- `2026-10-12-threshold-calibration.md`: fixture-local gates, with "Loudness: deliberately no acceptance window"

The only frontier artifact is `ports/frontier/fb-pipewire.md`, about realtime transport through pw-cat and mpv.

### 1.2 Gap sweeps (negative claims, each with its sweep)

| Topic | Held? | Sweep |
|---|---|---|
| Engine, middleware, platform loudness target, true peak, loudnorm, QOA, licensing | **0 entries** | `0 — grep -rilE 'godot\|fmod\|wwise\|aswg\|loudnorm\|dualmono\|dBTP\|qoa\|creative commons\|cc0\|licen[cs]e' corpus/knowledge \| wc -l` |
| Platform loudness target values (−23/−24 LUFS, LKFS) | **0**. The only match is "−23.780 dBFS", which is an RMS value | `grep -rcE -- '-23 LUFS\|-24 LUFS\|−23\|−24 LUFS\|LKFS' corpus/knowledge \| grep -v ':0$'` → `threshold-calibration.md:1` (that RMS line) |
| Ship formats (Ogg, Vorbis, Opus) | mentioned in 5 files, but only as roadmap lines or SoX detection-table types; **none measures a round trip** | `5 — grep -rilwE 'ogg\|vorbis\|opus' corpus/knowledge \| wc -l` (checklist, seed, three SoX entries) |
| Adaptive crossfade between states | roadmap only (`seed.md:27`, `audio-checklist.md:12` "unprobed") | `2 — grep -rilE 'crossfade\|cross-fade' corpus/knowledge \| wc -l` |
| EBU R128 | linked twice, with no target or tolerance stated | `2 — grep -rlE 'R ?128' corpus/knowledge \| wc -l` |
| Entry headers (`source:` / `verified-at:` / `recheck:`) | **0 of 14** | `0 — grep -lE '^(source\|verified-at\|recheck):' corpus/knowledge/*.md \| wc -l` |

### 1.3 Harness and pointer findings that bound this ground

ART uses these findings; STATE owns the fixes.

- **[OBS] The harness requests true peak and then discards it.** `corpus/fixtures/measure_audio.py:83` runs `"ebur128=peak=true"`. Lines 84-85 parse only `Integrated loudness`. `0 — grep -cE 'True peak|true_peak|dBTP' corpus/fixtures/measure_audio.py`. The call also never sets `dualmono`. The consequences are in §4 K3.
- **[OBS] Harness size.** `56096 — wc -l < corpus/fixtures/measure_audio.py`. This is bloat, reported to STATE.
- **[OBS] The R128 link fails for automated readers.** `tech.ebu.ch/publications/r128` is cited at `fixture-battery.md:22` and `threshold-calibration.md:20`. My reader got "Failed to fetch URL (HTTP 403)". The normative PDF `https://tech.ebu.ch/docs/r/r128.pdf` fetches cleanly (row S002).
- **[OBS] Stray root files.** `generate_timings.sh` is tracked at the root: `git ls-files | grep -E '^(Timing|generate_timings)'`. `Timing*.plot` and `Timings.html` are gitignored (`.gitignore:4-5`).

---

## 2. Current art (2025–2026) the corpus does not hold

### A. Engine audio (Godot 4.x)

The host runs Godot `4.7.2.stable.arch_linux.ed1daf0bf` (`godot --version`).

- **The WAV import default became lossy QOA in 4.4.** Godot class references give `compress/mode` default `0` in 4.3 (S009) and `2` = "lossy Quite OK Audio" in 4.4 (S010) through stable 4.7 (S008). The 4.4 tutorial still says "Disabled (default)" (S011). Details in K4.
- **Import options that affect measured properties** (S008):
  - `edit/normalize` is a *peak* normalize to 0 dB.
  - `edit/trim` cuts below −50 dB with 500-sample fades.
  - Loop mode "Detect From WAV" reads loop metadata from the WAV.
  - Ogg/MP3 support only a loop *begin* point, forward only (S012).
- **Adaptive music is native since 4.3:**
  - AudioStreamInteractive transition table: NEXT_BEAT/NEXT_BAR, fades measured in beats, filler clips, hold/return (S014).
  - AudioStreamSynchronized layers, up to 32 streams (S016).
  - `TRANSITION_TO_TIME_PREVIOUS_POSITION` existed in C++ and the editor but had no GDScript enum binding until PR #114129 merged on 2026-04-29 (overflow O3).
  - Known failure, fixed in 4.4: a fade into an Auto-Advance clip played "very silent" (S015).
- **Web export (S018, S017).** Since 4.3, Web exports default to Web Audio "Sample" playback, which has no AudioEffects, reverb/doppler or procedural audio. Bus effects need Stream mode. A renamed bus silently routes to Master.

### B. Middleware

- **FMOD:** MIT-licensed `fmod-gdextension`, tested on Godot 4.4 with FMOD 2.03 (S019).
- **Wwise:** the Godot integration is *community-managed* according to Audiokinetic's own page (S020).
- **Licensing is budget-gated:**
  - FMOD Indie: under $600k development budget, free or $2,000 (S021).
  - Wwise Indie: up to $250K production budget, free (S022).
- **Wwise 2025.1** adds Media Pool and Similar Sound Search, built with Sony AI (overflow O6).

### C. Loudness targets and measurement

- **Standards current as of 2023.**
  - BS.1770-5 (11/2023): 400 ms gating blocks; the algorithm is "not ... suitable ... for pure tones" (S001).
  - EBU R128 V5 (11/2023): −23.0 LUFS; ±1.0 LU only where the target is impractical; ±0.2 LU QC tolerance; ≤−1 dBTP; LRA not recommended under 1 minute (S002).
- **Game-specific practice.**
  - ASWG-R001: −24 ±2 LKFS for home, −18 ±2 for portable, ≤−1 dBTP, whole mix, at least 30 minutes of measurement (S003).
  - PlayStation recommendations as of Feb 2024 restate these and add a maximum LRA of 20. They advise capturing the device output (S004).
- **Field reality (lead only):** a 38-game convenience sample averages −20.6 LUFS (S007).

### D. Open tooling: ffmpeg n9.0.1 behaviours measured today

These are not in the corpus. Details in K1–K3.

1. `loudnorm` treats a sub-400 ms SFX as having integrated loudness `-inf` and simply peak-normalizes it to the TP target. The lane's `ui.wav` goes from −8.50 to −1.00 dB.
2. Two-pass `linear=true` silently reverts to `dynamic`, with 192 kHz output, when the measured LRA is 0.00. In linear mode, the reported `output_tp` is a native-rate *sample* peak.
3. `ebur128` reads mono files 3.0 LU lower than when `dualmono=true` is set.
4. The lane fixture `impact.wav` has a −1.8 dBFS sample peak but a −0.7 dBTP true peak.

Host capability: ffmpeg has a QOA *decoder* but no QOA encoder. The libvorbis and libopus encoders are present (`ffmpeg -hide_banner -decoders`, `-encoders`).

### E. Procedural and adaptive music research

- A PMG survey from Dec 2025 gives a taxonomy that bridges research prototypes and shipped systems (S030).
- Gen-AI use in game audio is still rare: 8% of professionals use it and 15% are exploring it, according to the GameSoundCon 2025 survey (overflow O9).

### F. SFX licensing and AI-generated audio terms

- **Human-made libraries:**
  - Freesound added an uploader Gen-AI training-preference panel in July 2026, on top of CC0/BY/BY-NC (S023).
  - The Sonniss GDC 2026 bundle is free for commercial use and prohibits AI/ML training (S024).
- **AI-generated audio:**
  - US Copyright Office: prompts alone do not make output copyrightable (S025).
  - Steam must be told about AI content that ships and that players consume, including sound (S026).
  - ElevenLabs SFX output can be used only combined with other material, updated 2026-10-09 (S027).
  - Stable Audio Open's licence ends above $1M in revenue and bans using outputs to train foundation models (S028).
  - MusicGen weights are CC-BY-NC (S029, rejected).
  - EU AI Act Art. 50 machine-readable marking has applied to providers since 2026-08-02 (overflow O10).

---

## 3. SOURCES.md rows (30)

All 30 follow the draft contract.
- Tier counts: `grep -E '^\| S[0-9]{3} ' local://kaika-w1-audio-art.md | awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c` gives **A 26 · B 3 · C 1**.
- Status counts: `grep -E '^\| S[0-9]{3} ' local://kaika-w1-audio-art.md | awk -F'|' '{gsub(/ /,"",$7); print $7}' | sort | uniq -c` gives **queued 23 · watch 5 · rejected 2 · mined 0**. Nothing is mined yet because no entry cites these rows.

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
| S001 | ITU-R BS.1770-5 (11/2023) Algorithms to measure audio programme loudness and true-peak audio level — https://www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1770-5-202311-I!!PDF-E.pdf | spec | A | what a LUFS/LKFS figure is: K-weighting, 400 ms blocks with incomplete final blocks dropped, −70 LKFS gate, Annex 2 true peak; unsuitable for pure tones | queued | 2026-10-19 | on-release | — |
| S002 | EBU R 128 V5 (Nov 2023) Loudness normalisation and permitted maximum level — https://tech.ebu.ch/docs/r/r128.pdf | spec | A | −23.0 LUFS target; ±1.0 LU only where impractical; ±0.2 LU QC; ≤−1 dBTP (±0.3 dB); measure the whole programme; LRA not for under 1 minute | queued | 2026-10-19 | on-release | — |
| S003 | Sony WWS ASWG-R001 v1.10 (Aug 2013) Average loudness and peak levels on SCE platforms — http://gameaudiopodcast.com/ASWG-R001.pdf (third-party mirror) | spec | A | game adaptation of BS.1770: home −24 ±2 LKFS, portable −18 ±2, ≤−1 dBTP, whole mix over ≥30 min of representative play in stereo and surround | queued | 2026-10-19 | 365d | — |
| S004 | Couthier and Schembri, Mastering a Game with Wwise Part 1 (Audiokinetic blog, 2024-02-15) — https://www.audiokinetic.com/en/community/blog/mastering-a-game-with-wwise-part1/ | docs | B | PlayStation recs as of Feb 2024 incl. max LRA 20; capture device output not the middleware bus; Mastering Suite limiter is not true-peak | queued | 2026-10-19 | 180d | — |
| S005 | FFmpeg libavfilter/af_loudnorm.c (master) — https://raw.githubusercontent.com/FFmpeg/FFmpeg/master/libavfilter/af_loudnorm.c | code | A | loudnorm mode logic: short-input linear path (l.456), linear gate on measured_* sentinels (l.826-828), 192 kHz in dynamic mode (l.746 and 757), stats peaks via sample peak (l.852 and 862) | queued | 2026-10-19 | on-release | — |
| S006 | ffmpeg n9.0.1 on host — `ffmpeg -hide_banner -h filter=loudnorm` and `ffmpeg -hide_banner -h filter=ebur128` | tool | A | installed option surface: loudnorm defaults I −24, LRA 7, TP −2, linear true, stats_file; ebur128 peak none/sample/true (default none), dualmono false, panlaw −3.0103 | queued | 2026-10-19 | on-release | — |
| S007 | Matt J Hart, A Study of Video Game Loudness (Sound Armoury) — https://www.soundarmoury.co.uk/blog/loudness-study | community | C | field-reality lead: 38 games (28 indie, 10 AAA), mean −20.6 and median −20.7 LUFS; author flags preference skew; never sole support | queued | 2026-10-19 | 365d | — |
| S008 | Godot ResourceImporterWAV (stable 4.7) — https://docs.godotengine.org/en/stable/classes/class_resourceimporterwav.html | docs | A | WAV import defaults: compress/mode 2 = lossy QOA; Detect From WAV loop mode; normalize = peak to 0 dB; trim below −50 dB with 500-sample fades | queued | 2026-10-19 | on-release | — |
| S009 | Godot ResourceImporterWAV (4.3) — https://docs.godotengine.org/en/4.3/classes/class_resourceimporterwav.html | docs | A | baseline compress/mode default 0 (Disabled); with S010 pins the QOA-default change to 4.4 | queued | 2026-10-19 | frozen | — |
| S010 | Godot ResourceImporterWAV (4.4) — https://docs.godotengine.org/en/4.4/classes/class_resourceimporterwav.html | docs | A | first class reference stating lossy QOA as the WAV import default (compress/mode 2) | queued | 2026-10-19 | frozen | — |
| S011 | Godot Importing audio samples (4.4 tutorial) — https://docs.godotengine.org/en/4.4/tutorials/assets_pipeline/importing_audio_samples.html | docs | A | rejected as authority for defaults: says Disabled (default) while the same-version class reference says QOA; tutorials lag generated references | rejected | 2026-10-19 | — | — |
| S012 | Godot Importing audio samples (stable tutorial) — https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_audio_samples.html | docs | A | per-second size of each format; Ogg and MP3 loop begin only, forward only; BPM, beat count and bar beats feed interactive music | queued | 2026-10-19 | on-release | — |
| S013 | QOA — The Quite OK Audio Format — https://qoaformat.org/ | spec | A | Godot's default WAV codec: lossy time-domain codec, about 400-line reference coder, one-page CC0 spec; host ffmpeg decodes but cannot encode it | queued | 2026-10-19 | 365d | — |
| S014 | Godot AudioStreamInteractive (stable 4.7) — https://docs.godotengine.org/en/stable/classes/class_audiostreaminteractive.html | docs | A | clip and transition-table adaptive music: from IMMEDIATE/NEXT_BEAT/NEXT_BAR/END, to SAME/START/PREVIOUS_POSITION, fades in beats, filler clips, hold and return | queued | 2026-10-19 | on-release | — |
| S015 | Godot issue #95740 AudioStreamInteractive transition plays clips very silent (closed by #95803, milestone 4.4) — https://github.com/godotengine/godot/issues/95740 | code | B | transition error pattern: fade or cross-fade into an Auto-Advance clip played very silent in 4.3.stable; MRP attached | queued | 2026-10-19 | — | — |
| S016 | Godot AudioStreamSynchronized (stable) — https://docs.godotengine.org/en/stable/classes/class_audiostreamsynchronized.html | docs | A | vertical layering: sub-streams start together, per-stream volume_db, MAX_STREAMS 32, a looping sub-stream keeps playback alive | queued | 2026-10-19 | on-release | — |
| S017 | Godot Audio buses (stable) — https://docs.godotengine.org/en/stable/tutorials/audio/audio_buses.html | docs | A | buses route right to left into Master; a renamed bus silently outputs to Master; silent buses auto-disable; layout in default_bus_layout.tres; its dB primer is unreliable | queued | 2026-10-19 | on-release | — |
| S018 | Godot Exporting for the Web, Audio playback (stable) — https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_web.html | docs | A | since 4.3 Web defaults to Sample playback: no AudioEffects, reverb, doppler or procedural audio; Stream mode restores them at a latency cost | queued | 2026-10-19 | on-release | — |
| S019 | utopia-rise/fmod-gdextension — https://github.com/utopia-rise/fmod-gdextension | code | A | MIT GDExtension exposing the FMOD Studio API to Godot 4 (event emitters and listeners, bank auto-load, live update); README tested on Godot 4.4 and FMOD 2.03 | queued | 2026-10-19 | 90d | — |
| S020 | Audiokinetic, Wwise Integrations — https://www.audiokinetic.com/en/wwise/integrations/ | docs | A | vendor lists the Godot integration as Community Managed (Alessandro Fama GDExtension), unlike the Unity and Unreal integrations it maintains | queued | 2026-10-19 | 180d | — |
| S021 | FMOD, Licensing — https://www.fmod.com/licensing | docs | A | per-game fee by development budget: Indie under $600k free or $2,000 (note did not render), Basic $6,000, Premium $18,000; logo required | watch | 2026-10-19 | 90d | — |
| S022 | Audiokinetic, Wwise for Games pricing — https://www.audiokinetic.com/en/wwise/pricing/for-games/ | docs | A | per title and platform by production budget: Indie up to $250K free; Pro up to $2M at $8,000 first platform | watch | 2026-10-19 | 90d | — |
| S023 | Freesound, FAQ: Licenses and Gen-AI preferences — https://freesound.org/help/faq/ | docs | A | CC0, BY and BY-NC duties, remix-licence matrix, attribution format; uploader Gen-AI training preference panel since July 2026 | queued | 2026-10-19 | 180d | — |
| S024 | Sonniss, GDC 2026 Game Audio Bundle — https://gdc.sonniss.com/ | docs | A | 347+ royalty-free files, no attribution, commercial use; AI/ML training strictly prohibited; full licence at sonniss.com/gdc-bundle-license (unopened) | queued | 2026-10-19 | 365d | — |
| S025 | U.S. Copyright Office, NewsNet 1060 (AI report Part 2, 2025-01-29) — https://www.copyright.gov/newsnet/2025/1060.html | docs | A | AI output is protectable only where a human determined enough expressive elements; prompts alone are not enough; Part 3 on training forthcoming | queued | 2026-10-19 | 180d | — |
| S026 | Steamworks, Content Survey: Generative AI section — https://partner.steamgames.com/doc/gettingstarted/contentsurvey | docs | A | disclose AI content that ships and is consumed by players (sound included); live-generated content must also describe guardrails | watch | 2026-10-19 | 90d | — |
| S027 | ElevenLabs, ElevenCreative Terms Exhibit 4 Sound Effects (updated 2026-10-09) — https://elevenlabs.io/creative-terms | docs | A | SFX output may ship in games only combined with other material; no standalone or library redistribution; commercial use only where the plan permits | watch | 2026-10-19 | 30d | — |
| S028 | Stability AI Community License, stable-audio-open-1.0 LICENSE.md (2024-07-05) — https://huggingface.co/stabilityai/stable-audio-open-1.0/blob/main/LICENSE.md | docs | A | commercial use needs registration and ends above US$1M annual revenue; outputs may not train foundation models; outputs owned as far as the law permits | watch | 2026-10-19 | 180d | — |
| S029 | facebook/musicgen-small model card — https://huggingface.co/facebook/musicgen-small | docs | A | rejected for shipping assets: weights are CC-BY-NC 4.0 and intended for research | rejected | 2026-10-19 | — | — |
| S030 | Luo and Reiss, Procedural Music Generation Systems in Games (arXiv 2512.12834, 2025-12-14) — https://arxiv.org/abs/2512.12834 | paper | B | two-aspect PMG taxonomy contrasting research prototypes with shipped systems; only the abstract has been read so far | queued | 2026-10-19 | 180d | — |

### Overflow: opened this session but not rowed (30-row cap)

Promote these if the cap is raised. Each line is grounded in what I read.

- O1 libebur128 — https://github.com/jiixyj/libebur128 (code, A): MIT reference implementation of R128 (M/S/I, LRA per Tech 3342, true peak). The changelog fixes a true-peak null dereference on 192 kHz input.
- O2 ffmpeg-normalize — https://github.com/slhck/ffmpeg-normalize (tool, A): batch two-pass EBU R128, RMS or peak normalization. `--batch` preserves relative loudness. `--print-stats` reports per-file status.
- O3 Godot PR #114129 — https://github.com/godotengine/godot/pull/114129 (code, A): binds `TRANSITION_TO_TIME_PREVIOUS_POSITION`. Merged 2026-04-29. The value already worked from the editor.
- O4 alessandrofama/wwise-godot-integration — https://github.com/alessandrofama/wwise-godot-integration (code, A): GDExtension with Ak* nodes and auto-defined SoundBanks; Web support is experimental.
- O5 ValveSoftware/steam-audio — https://github.com/ValveSoftware/steam-audio (code, A): Apache-2.0, version 4.8.1. Official integrations are Unity, Unreal, FMOD and Wwise; there is no official Godot integration.
- O6 Wwise 2025.1 What's New — https://www.audiokinetic.com/en/community/blog/wwise-2025.1-whats-new/ (docs, A): Media Pool, Similar Sound Search, audio-rate sidechaining, Multiband Meter, Event Limiting.
- O7 Stable Audio 3.0 announcement (May 2026) — https://stability.ai/news-updates/meet-stable-audio-3-the-model-family-built-for-artistic-experimentation-with-open-weight-models (docs, A, watch): vendor claims training on fully licensed data, an on-device open-weight "Small SFX" model, and output ownership under the Community License.
- O8 Xbox Accessibility Guideline 105 — https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/105 (docs, A, Adjacent): separate volume per audio category and a stereo-to-mono option.
- O9 GameSoundCon Game Audio Industry Survey 2025 — https://www.gamesoundcon.com/post/gamesoundcon-game-audio-industry-survey-2025 (dataset, B): 654 respondents; 8% use Gen-AI and 15% are exploring it; placeholder dialogue is 43% of uses; the sample is non-random by the survey's own statement.
- O10 EU AI Act Art. 50 (AI Act Explorer reproduction) — https://artificialintelligenceact.eu/article/50/ (spec, B, watch): from 2026-08-02, providers must mark synthetic audio in a machine-readable form. Deepfake disclosure is limited for evidently artistic works.
- O11 Godot ResourceImporterWAV 4.5 — https://docs.godotengine.org/en/4.5/classes/class_resourceimporterwav.html: also shows `compress/mode` = `2`, corroborating S010.
- O12 Godot AudioStreamInteractive 4.3 — https://docs.godotengine.org/en/4.3/classes/class_audiostreaminteractive.html: TransitionToTime lists only SAME_POSITION and START.

### Leads (unopened)

**Loudness and measurement**
- EBU Tech 3341 (EBU Mode metering) and Tech 3342 (LRA) — https://tech.ebu.ch/docs/tech/tech3341.pdf , https://tech.ebu.ch/docs/tech/tech3342.pdf
- EBU R 128 s1, loudness for short-form content. This is the closest broadcast analogue for short assets.
- EBU Tech 3343 and 3344 (production, distribution).
- Report ITU-R BS.2217: meter compliance test signals. The lane could use them to calibrate its ebur128 use.
- PlayStation DevNet loudness recommendations: partner-only, so S004 is the public proxy.
- Audiokinetic "Loudness Processing Best Practices" series, linked from S004.
- Kyle Swanson's loudnorm design notes (2016) — http://k.ylo.ph/2016/04/04/loudnorm.html. Cited at the top of S005.
- phoboslab/qoa reference coder (`qoaconv`) — https://github.com/phoboslab/qoa. It is not on the host and would be needed to make QOA fixtures without Godot.

**Godot**
- PR #64488 (interactive music, reduz).
- PR #91382 (Web sample playback).
- godot-proposals #15584 (Opus import, open).
- stechyo/godot-steam-audio.
- hyprtuna/divisi (adaptive-music clock).

**Rights and AI terms**
- Sonniss bundle licence text — https://sonniss.com/gdc-bundle-license/
- US Copyright Office Part 2 full report — https://www.copyright.gov/ai/
- Freesound blog "Freesound in the era of generative AI" — https://blog.freesound.org/?p=2082
- EU Code of Practice on marking and labelling AI content.
- UMG/WMG–Stability alliances (watch).

**Canonical books**
- Farnell, *Designing Sound* (MIT Press 2010), procedural audio.
- Collins, *Game Sound* (MIT Press 2008).
- Sweet, *Writing Interactive Music for Video Games* (2014).
- Stevens and Raybould, *Game Audio Implementation* (2016).
- Luo and Reiss full text (S030 beyond the abstract).

---

## 4. Candidate knowledge entries (6)

**Admission bar.** `corpus/QUALITY.md` does not exist, so each candidate is checked against the fleet bar:
- `LEARNING.md:12-14` requires gating on the lane's own bar.
- `LEARNING.md:54-56` says what QUALITY.md must hold.
- The lane's established practice (`seed.md:14-20`): "Every audio claim is a measurement, not a listen", with named receipts.

Each entry below has a primary source, a pasteable recheck, an observation/inference/unknown split, and a pinned tool or doc version. All commands run from the lane root.

**Coverage map.** The lane has none, so I propose these rows for the first `corpus/README.md`:
- **Core:** SFX synthesis and measurement (held); loop seams (held); loudness-measurement conventions (gap: K3); per-asset normalization tooling (gap: K1, K2); platform loudness targets (gap: K5); ship formats and engine import (gap: K4).
- **Frontier:** engine-native adaptive music (S014–S016); AI-audio terms ledger (gap: K6); realtime transport (held: `ports/frontier/fb-pipewire.md`).
- **Adjacent:** middleware integration and licensing (S019–S022); accessibility mixes (O8); spatial audio (O5).

### K1 `loudnorm-short-sfx-regimes`

**Claim.** With ffmpeg n9.0.1, `loudnorm=I=-24:TP=-1:LRA=11` behaves in three regimes depending on input length:
1. **Shorter than one 400 ms gating block.** Integrated loudness is `-inf`, and the filter applies one linear gain that puts the sample peak at TP. The lane's 0.12 s `ui.wav` goes from `input_tp` −8.50 to an output peak of −1.000000 dB, labelled `"linear"`.
2. **Under 3 s.** Linear gain to the I target: a 2.5 s tone reaches `output_i` −24.05.
3. **3 s or longer.** `dynamic` mode, with 192 kHz output.

So loudnorm is not a loudness matcher for UI-length SFX: it peak-normalizes them.

**Sources.** S005, S001, S006.
- S005 `af_loudnorm.c:456`: `if (s->frame_type == FIRST_FRAME && in->nb_samples < frame_size(inlink->sample_rate, 3000))`. The gain is capped by sample peak at l.462, and dynamic mode forces `input_srate[] = {192000, -1}` at l.746.
- S001, Annex 1: "Incomplete gating blocks at the end of the measurement interval are not used."

**Recheck.**
```
for d in 0.12 2.5 4; do printf '%ss ' $d; ffmpeg -hide_banner -nostats -f lavfi -i "sine=frequency=1000:sample_rate=48000:duration=$d" -af "volume=-12dB,loudnorm=I=-24:TP=-1:LRA=11:print_format=json,astats=measure_overall=Peak_level:measure_perchannel=none" -f null - 2>&1 | grep -oE '"(input_i|output_i|normalization_type)" : "[^"]+"|Peak level dB: [-0-9.]+' | tr '\n' ' '; echo; done
ffmpeg -hide_banner -nostats -i corpus/artifacts/ui.wav -af "loudnorm=I=-24:TP=-1:LRA=11:print_format=json,astats=measure_overall=Peak_level:measure_perchannel=none" -f null - 2>&1 | grep -oE '"(input_i|input_tp|normalization_type)" : "[^"]+"|Peak level dB: [-0-9.]+'
```

**Observed 2026-10-19.**

| Input | Result |
|---|---|
| 0.12 s tone | `input_i -inf`, peak −1.000000, `linear` |
| 2.5 s tone | `output_i -24.05`, `linear` |
| 4 s tone | `dynamic` |
| `ui.wav` | `-inf`, −8.50 → −1.000000, `linear` |

- **Inference:** the cut-overs are 0.4 s, the first complete BS.1770 gating block (S001), and 3 s (S005 l.456). The 0.4–3 s regime was tested only at 2.5 s.
- **Unknown:** behaviour on other ffmpeg versions.

**Coverage row:** Core, per-asset normalization tooling. It carries `threshold-calibration.md:20` (six short SFX read null LUFS) from measurement into normalization: loudnorm turns undefined loudness into a peak normalize.

### K2 `loudnorm-linear-gate-and-tp-report`

**Claim.** Two-pass `linear=true`, given every `measured_*` value, still runs `dynamic` (192 kHz output) in two cases:
- The measured LRA is 0.00, as for any steady tone or bed, because 0 is also the option's "unset" sentinel.
- The measured LRA exceeds the target LRA.

Only `"normalization_type"` in `print_format=json` reveals the fallback. When linear mode does engage, the JSON `output_tp` is a native-rate *sample* peak. A 12 kHz test signal reported −25.56 while `ebur128` measured a −22.2 dBFS true peak, so the report under-reads by 3.4 dB.

**Source.** S005 `af_loudnorm.c:826`: `if (s->measured_tp != 99 && s->measured_thresh != -70 && s->measured_lra != 0 && s->measured_i != 0)`. Line 827 adds `s->measured_lra <= s->target_lra`. The `measured_LRA` default of 0 is at l.121. Peaks are taken with `ff_ebur128_sample_peak` at l.852 and l.862.

**Recheck.**
```
run(){ src="$1"; set -- $(ffmpeg -hide_banner -nostats -f lavfi -i "$src" -af "loudnorm=I=-24:TP=-1:LRA=11:print_format=json" -f null - 2>&1 | sed -n '/^{/,/^}/p' | python3 -c 'import json,sys;d=json.load(sys.stdin);print(d["input_i"],d["input_tp"],d["input_lra"],d["input_thresh"],d["target_offset"])'); printf 'LRA=%s -> ' "$3"; ffmpeg -hide_banner -nostats -f lavfi -i "$src" -af "loudnorm=I=-24:TP=-1:LRA=11:measured_I=$1:measured_TP=$2:measured_LRA=$3:measured_thresh=$4:offset=$5:linear=true:print_format=json,ebur128=peak=true+sample" -f null - 2>&1 | grep -oE '"(output_tp|normalization_type)" : "[^"]+"|Stream #0:0: Audio: [^,]+, [0-9]+ Hz|^ +Peak: +[-0-9.]+ dBFS' | tail -n5 | tr -s ' ' | tr '\n' ' '; echo; }
run "aevalsrc=0.1*sin(2*PI*440*t)*(1+1*gt(t\,10)):s=48000:d=20"; run "sine=frequency=440:sample_rate=48000:duration=20"; run "aevalsrc=0.25*sin(2*PI*12000*t+PI/4)*(1+1*gt(t\,10)):s=48000:d=20"
```

**Observed 2026-10-19.**

| Input | Measured LRA | Result |
|---|---|---|
| stepped 440 Hz | 6.00 | `linear`, 48000 Hz |
| steady 440 Hz | 0.00 | `dynamic`, 192000 Hz |
| 12 kHz stepped | 6.00 | `linear`; JSON `output_tp` −25.56; ebur128 sample peak −25.6, true peak −22.2 dBFS |

A control with a stepped tone at LRA 12.10 (> target 11) also fell back to `dynamic`.

**Coverage row:** Core, per-asset normalization tooling. It is also a QUALITY.md seed: a normalization receipt must assert the mode it actually got.

### K3 `harness-ebur128-mono-and-truepeak-gaps`

**Claim.** The harness's single `ebur128=peak=true` call (`measure_audio.py:83`) has two gaps.

(a) It measures mono fixtures as one channel. With `dualmono=true` (default false, panlaw −3.0103), the same files read exactly 3.0 LU higher:

| Fixture | dualmono=false | dualmono=true |
|---|---|---|
| `ambience.wav` | −30.7 LUFS | −27.7 LUFS |
| `stem_sections.wav` | −24.7 LUFS | −21.7 LUFS |

Any LUFS figure for a mono asset heard centred on stereo must name this setting.

(b) It computes true peak and then discards it: `0 — grep -cE 'True peak|true_peak|dBTP' corpus/fixtures/measure_audio.py`. On the canonical `impact.wav`, the sample peak is −1.8 dBFS, which passes the lane's `< .95 FS` gate, but the true peak is −0.7 dBTP: 1.1 dB of inter-sample overshoot, above the −1 dBTP ceiling in S002(m) and S003 rec. 7. Per-asset TP is not a mix violation; this only shows that the sample-peak gate does not bound true peak.

**Sources.**
- S006: "treat mono input files as dual-mono (default false)".
- S001, Annex 1: "applied to the left, centre, or right channel input, the indicated loudness will equal −3.01 LKFS".
- S003 rec. 11: measure "in both stereo and surround configurations".
- S002(m): "True Peak Level of a programme shall not exceed −1 dBTP".

**Recheck.**
```
for f in ambience stem_sections; do for dm in false true; do printf '%s dualmono=%s ' $f $dm; ffmpeg -hide_banner -nostats -i corpus/artifacts/$f.wav -af "ebur128=dualmono=$dm:peak=true" -f null - 2>&1 | grep -E '^\s+I:' | tr -s ' '; done; done
for f in ui impact movement ambience stem_sections; do printf '%s ' $f; ffmpeg -hide_banner -nostats -i corpus/artifacts/$f.wav -af "ebur128=peak=true+sample" -f null - 2>&1 | grep -A1 -E '^\s+(Sample|True) peak:' | grep -oE 'Peak: +[-0-9.]+' | tr -s ' ' | tr '\n' ' '; echo; done
```

**Observed 2026-10-19.** Sample / true peak per fixture:

| Fixture | Sample peak | True peak |
|---|---|---|
| `ui` | −8.5 | −8.5 |
| `impact` | −1.8 | −0.7 |
| `movement` | −5.4 | −5.1 |
| `ambience` | −15.2 | −15.2 |
| `stem_sections` | −15.3 | −15.3 |

Meter sanity check: a 0.25-amplitude 12 kHz sine reads −12.0 dBTP with a 0.5 s fade-in (theoretical −12.04) but −11.4 with an abrupt onset. The meter is accurate; the extra +0.6 dB is genuine onset overshoot.

**Coverage row:** Core, loudness-measurement conventions. It deepens `threshold-calibration.md`, whose peak gate is a "local clipping-headroom design choice, not mastering ceiling".

### K4 `godot-wav-import-default-qoa`

**Claim.** Godot's WAV importer default `compress/mode` changed between versions:
- 4.3 class reference: `0`, uncompressed (S009).
- 4.4 class reference (S010), 4.5 (O11) and stable 4.7 (S008): `2`, lossy Quite OK Audio.
- The 4.4 tutorial still says "Disabled (default)" (S011).

So the lane's measurements of PCM16 masters do not describe the bytes a default Godot ≥4.4 import ships. Seam, peak and centroid values could differ after QOA coding.
- **Unknown:** the size of that difference, which is unmeasured.
- **Province:** describing the default is in scope; changing a game's import settings is refused.

**Sources.**
- S008, Description: "By default, Godot imports WAV files using the lossy Quite OK Audio compression."
- S011, section "Compress > Mode": "Three compression modes can be chosen from for WAV files: **Disabled** (default), **RAM (Ima-ADPCM)**, or **QOA (Quite OK Audio)**".

**Recheck.**
```
for v in 4.3 4.4 stable; do printf '%s ' $v; curl -sL https://docs.godotengine.org/en/$v/classes/class_resourceimporterwav.html | grep -c 'By default, Godot imports WAV files using the lossy Quite OK Audio compression'; done
curl -sL https://docs.godotengine.org/en/4.4/tutorials/assets_pipeline/importing_audio_samples.html | grep -c 'Disabled</strong> (default)'
```
Observed 2026-10-19: `4.3 0`, `4.4 1`, `stable 1`; tutorial `1`.

**Next measurable step, in lane scope.** The host has Godot 4.7.2. Import a fixture inside a scratch project under `.shokunin/audio/**` and read `compress/mode` from its `.import` file. Host ffmpeg can decode a raw `.qoa` but cannot encode one, so measuring the codec delta needs Godot or `qoaconv` (lead).

**Coverage row:** Core, ship formats and engine import. This is the "wav (master) → ogg (ship)" step on the `seed.md:28` roadmap.

### K5 `game-loudness-protocol-whole-mix`

**Claim.** Game loudness targets are whole-mix, long-capture measurements, not per-asset ones:
- Home −24 (±2) LKFS and portable −18 (±2) (S003 recs. 4 and 5).
- True peak ≤ −1 dBTP (rec. 7).
- Measure the mix "as a whole" (rec. 9), for at least 30 minutes of representative gameplay (rec. 10), in stereo and surround (rec. 11).

PlayStation's Feb 2024 recommendations restate these and add a maximum LRA of 20 (S004). BS.1770 itself excludes pure tones (S001). Together this gives the lane's existing "no LUFS acceptance window" stance a primary basis: a per-fixture LUFS window on sine fixtures would contradict both specs.

**Sources.**
- S003, rec. 10: "audio content should be measured for as long as is practical and for a minimum of 30 minutes".
- S003, rec. 9: "measured as a whole, and should not focus on dialogue, sound effects or music specifically".
- S001, Annex 1, after Table 3: "not, in general, suitable for use to estimate the subjective loudness of pure tones".

**Recheck.**
```
curl -sL http://gameaudiopodcast.com/ASWG-R001.pdf | pdftotext - - 2>/dev/null | tr '\n' ' ' | grep -oE -- '-24 \(±2\) LKFS|-18 \(±2\) LKFS|minimum of 30 minutes|exceed -1 dBTP' | sort | uniq -c
curl -sL 'https://www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1770-5-202311-I!!PDF-E.pdf' | pdftotext - - 2>/dev/null | grep -c 'loudness of pure tones'
```
Observed 2026-10-19: each ASWG string 1; BS.1770 1.

**Coverage row:** Core, platform loudness targets. It deepens `threshold-calibration.md` §"Loudness: deliberately no acceptance window" on the quality axis.

### K6 `ai-audio-terms-ledger-fields`

This entry is record-only. PROVINCE refuses clearance; the lane documents terms and never certifies rights.

**Claim.** As of 2026-10-19, the primary terms for AI-generated audio vary on four independent axes. A reference-ledger row must therefore hold four separate fields, which extends PROVINCE's "attribution / rights / training permission kept distinct" (`PROVINCE.md:10-11`).

1. **Commercial permission.**
   - S027: "only where your plan permits commercial use".
   - S028: the licence "shall terminate" above US$1,000,000 annual revenue.
   - S029: "model weights are released under CC-BY-NC 4.0".
2. **Standalone redistribution.** S027 Exhibit 4 §2: "You may exercise those rights only in respect of Output combined with other material".
3. **Training use.**
   - S028 §IV(b): outputs may not be used "to create or improve any foundational generative AI model".
   - S024: "Use for AI/ML training is strictly prohibited under our licence terms."
   - S023: uploaders' Gen-AI preferences "as of July 2026".
4. **Disclosure and authorship.**
   - S026: "content that ships with your game, and is consumed by players".
   - S025: authorship "not the mere provision of prompts".

**Recheck.**
```
curl -sL -H 'Accept: text/markdown' https://elevenlabs.io/creative-terms | grep -c 'Output combined with other material'
curl -sL https://huggingface.co/stabilityai/stable-audio-open-1.0/blob/main/LICENSE.md | grep -c 'foundational generative AI model'
curl -sL https://huggingface.co/api/models/facebook/musicgen-small | python3 -c 'import json,sys;print(json.load(sys.stdin)["cardData"]["license"])'
curl -sL https://partner.steamgames.com/doc/gettingstarted/contentsurvey | grep -c 'consumed by players'
curl -sL https://www.copyright.gov/newsnet/2025/1060.html | grep -c 'not the mere provision of prompts'
curl -sL https://freesound.org/help/faq/ | grep -c 'as of July 2026 Freesound has introduced'
```
Observed 2026-10-19: `1`, `1`, `cc-by-nc-4.0`, `1`, `1`, `1`.

Sonniss cannot be checked with curl, which receives a 5,373-byte challenge page (`curl -sL -A 'Mozilla/5.0' https://gdc.sonniss.com/ | wc -c`). Re-open it in a reader.

**Coverage row:** Frontier, AI-audio terms ledger. Watch cadence is 30–90 days (S026, S027 and S028 are rowed `watch`).

---

## 5. Paths (study sequences for the frontier)

1. **Game loudness**, from what a number means to what ships:
   S001 → S002 → S003 → S004 → S006 → S005 → S007.
   Measurement algorithm, then broadcast normalization policy and tolerances, then the game adaptation (whole mix, 30 minutes), then current platform practice (device capture, LRA 20), then the tool the lane actually runs, then that tool's internals, then measured field reality (a lead, never an authority).
2. **The Godot asset path:**
   S009 → S010 → S011 (rejected) → S008 → S012 → S013 → S017 → S018 → S016 → S014 → S015 → S019, S020 → S021, S022.
   Import defaults across versions (and why tutorials lose to class references), then the shipped codec, then routing, then platform limits, then layering, then transitions, then a known transition failure, then when to leave native audio for middleware and what that costs.
3. **Rights and AI-generated audio** (record, never clear):
   S023 → S024 → S025 → S026 → S027 → S028 → S029 (rejected).
   Human CC licences and remix rules, then a commercial bundle with an AI-training ban, then authorship of AI output, then store disclosure, then a generator's use terms, then an open-weights revenue gate, then the non-commercial rejection test.

---

## 6. Rejected candidates (evidence of taste)

1. **"EBU R128: −23 LUFS ±0.5 LU"** (from an AI search summary and secondary pages): **stale.** In the V5 (2023) text, the only "0.5 LU" occurrence is the 2014 V3 row of the document-history table. The normative text, item (h), gives ±1.0 LU where the target is impractical, and item (i) gives ±0.2 LU for QC. Check: `curl -sL https://tech.ebu.ch/docs/r/r128.pdf | pdftotext - - 2>/dev/null | grep -n '0.5 LU'` → `37:± 0.5 LU (except Live-programmes)`.
2. **"ASWG-R001: console −23 LUFS ±2"** (Schappler 2013 and ansoaudio 2016, seen in search results): **superseded** within v1.10 itself. Note (3) says "This update revises the ASWG's Average Loudness Level recommendation from -23 to -24 LKFS" (S003, page 7).
3. **"FMOD is free for indies under $200k revenue / $500k budget"** (a 2023 news item in search results): **stale.** The primary page now says Indie means a development budget "Under $600k" and costs "Free or $2,000" (S021).
4. **"Sony, Nintendo and Microsoft, via G.A.N.G., recommend −24 console / −16 portable"** (community wiki, in search results): **unsourced** tier-C claim that conflicts with ASWG portable −18 (S003, rec. 5). No primary source found.
5. **The Godot 4.4 tutorial as the authority for WAV defaults** (S011): **contradicted** by the same-version class reference (S010). Rowed as `rejected`.
6. **MusicGen for shipped game assets** (S029): CC-BY-NC 4.0 weights, research use only. Rowed as `rejected`.
7. **"Wwise ships an official Godot integration"** (implied by search summaries of "Wwise 2024.1 for Godot"): **rejected.** Audiokinetic's own page lists Godot under "Community Managed" (S020).
8. **The Godot audio-buses dB primer as a loudness or psychoacoustics source** (S017): **internally inconsistent.** It says "For every 6 dB, sound amplitude doubles or halves" but also "Every 6 dB below the 0 dB limit, sound energy is halved". Energy goes with amplitude squared [INF: standard physics]. The row keeps S017 for engine routing behaviour only.
9. **Sound Armoury's "about −20 LUFS typical" as a target authority** (S007): a convenience sample of 38 with skew acknowledged by the author. Kept as a tier-C lead; rejected as sole support.

---

## 7. Receipts: commands run this session (all read-only)

- **Toolchain:**
  - `ffmpeg -hide_banner -version` → `ffmpeg version n9.0.1`.
  - `sox --version` → `SoX_ng v14.8.0.1`.
  - `godot --version` → `4.7.2.stable.arch_linux.ed1daf0bf`.
  - `command -v pdftotext` → present.
  - `ffmpeg -hide_banner -decoders | grep -iE ' (qoa|vorbis|libvorbis|opus|libopus)'` → QOA, Vorbis and Opus decoders present.
  - `ffmpeg -hide_banner -encoders | grep -iE ' (qoa|vorbis|libvorbis|opus|libopus)'` → no QOA encoder; libvorbis and libopus encoders present.
- **Tone dualmono check:** `sine=frequency=1000`, 10 s, `volume=-20dB` → `I: -41.1 LUFS` with dualmono=false and `-38.1 LUFS` with dualmono=true. Peak is −38.1 dBFS in both.
- **Default loudnorm:** a 6 s steady sine comes out at `192000 Hz`, `"normalization_type" : "dynamic"`.
- **Lane fixtures:** the results in K1 and K3. `corpus/artifacts` holds 17 WAVs: `ls corpus/artifacts | grep -cE '\.wav$'`.
- **Doc and PDF quote checks:** the K4, K5 and K6 commands above, outputs as stated. Godot pages, Steam, ElevenLabs, USCO, Freesound and Hugging Face all work with curl; Sonniss needs a reader.

## 8. Unresolved

- The text of FMOD's Indie "see note" (the page is JS-rendered and the note did not render).
- The Sonniss licence text itself.
- The size of the QOA-induced deltas on lane fixtures.
- The 0.4–3 s regime of loudnorm, tested only at 2.5 s.
- Whether PlayStation's post-2024 DevNet recommendations changed (partner-only).
- S030's full text.
- The EU AI Act "Digital Omnibus" deadline shifts (watch).
