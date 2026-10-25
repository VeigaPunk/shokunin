# audio-r87r88-foldverify — verify the applied r87+r88 combined fold and file both fold reports

Lane: /home/vgpnk/Projects/shokunin/audio-shokunin
Context: the combined fold seat applied the r87+r88 queues to `corpus/fixtures/measure_audio.py`
(WORKING TREE, uncommitted — do not commit; orchestrator commits) and ran green probes:
pwbind-r87 runs through `corpus/live/runs/20261016T070305393338Z-pwbind-r87` and
btwit-r88 through `corpus/live/runs/20261016T072341162452Z-btwit-r88` (all `failures` empty).
The seat died before filing its reports; `corpus/live/r87-fold/proofs/` and
`corpus/live/r88-fold/proofs/` hold only the pre-fold baseline snapshot.

Original contract (authoritative): `.ufo/waves/shokunin-train-20261015-w22/tasks/audio-r87-r88-fold.md`.

Your job:
1. Sanity-check the working tree compiles (`python3 -m py_compile corpus/fixtures/measure_audio.py`).
2. Run `--probe-pwbind-r87` AND `--probe-btwit-r88` on the folded working-tree bytes, one fresh
   green run each (a second if the first is red — distinguish real fold defects from host
   confounds; never weaken a gate). Seat-namespace any PipeWire objects `r87f_*`/`r88f_*`;
   NEVER `pactl set-default-sink`/`set-default-source`; TMPDIR=~/Projects/shokunin/tmp.
3. Write `reports/round-87/r87-fold.md` and `reports/round-88/r88-fold.md`: what each fold
   changed (read the diff `git diff corpus/fixtures/measure_audio.py`), which defects each
   hunk answers, and the green-run receipt pointers (run dir names + sha256 of measurements.json).
   Drop receipts under `corpus/live/r87-fold/` and `corpus/live/r88-fold/`.
4. Zero commits. Return: both report paths, green-run shas, blockers.
