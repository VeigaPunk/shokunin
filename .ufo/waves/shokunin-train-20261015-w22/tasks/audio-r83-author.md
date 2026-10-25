# Seat: audio r83 author — pw-cat/pw-record props surface
Lane: /home/vgpnk/Projects/shokunin/audio-shokunin
Head: aa03c347 (r82 landed; measure_audio.py is yours).
Scout: reports/round-83/r83-scout.md. Boundary: reports/round-83/r83-boundary.md (58e45e9).
## MANDATORY boundary folds
- Malformed props are NOT universally silent-drop: `}{ garbage` drops but `a=b }{ c=d`, `{ bad`, `media.name=` -> rc=255 'syntax error in --capture-props' zero nodes. Encode both classes.
- `-d 1.0` DOES add ~1.0s onset delay (falsified 'no delay'); pin the delay or qualify.
- `-i ''`/`-o ''` SIGSEGV family extended: also `-i ' '`, `pw-cat -P ''`, `pw-record -P ''`.
- peaks is FULL-WAVE |x| not half-wave (zero-fraction 8.3%, octave shift amp@2k).
- `-l -5` -> 4294967056/48000 uint32 wrap.
- A3 cell: `-m '[ MONO ]'` alone is time-varying; only `-c 1 -m '[ MONO ]'` gives stable 0.5*(L+R)=4095.6/freq.
## Conventions
- r82 family shape in measure_audio.py (--probe-pwcat-r83 or similar); namespace r83a_*; >=3 fresh reps/pin; envelopes for real modes; explicit teardown (sinks_gone + own_nodes_after + name-verified unloads); record realized/unrealized arms honestly.
- reports/round-83/r83-author.md + corpus/live/r83-author/. No commits.
