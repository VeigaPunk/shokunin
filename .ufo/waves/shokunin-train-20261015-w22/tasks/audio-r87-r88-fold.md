# audio-r87-r88-fold — COMBINED fold: repair r87+r88 arms after two GATE FAILs

Custody is yours NOW (r89 landed 0d732989; r90 author waits for you). Read both fold specs:
tasks/audio-r87-fold.md and tasks/audio-r88-fold.md — apply both queues to
corpus/fixtures/measure_audio.py.

Core theme (shared defect class): co-tenancy-sensitive arms that snapshot shared-daemon state
or read bounded windows of buffered logs. Fixes are all the same shape:
- match over the FULL log / full census, not the last-500-chars or a single snapshot bracket
- membership not equality for census comparisons (transient clients drift +-1)
- take the LAST error_class line or scope to own request id
- missing legs -> coverage_blocked, never silent skip
Then the per-queue items (r87: m_sysex/skeleton/midi-census/no-link-peer/cold_nowarm; r88:
pt flush lottery, bz_tree truncation, bz_device negative-only) + both simplifier patches
(-7 each, proven) + citation fixes.

After applying: two green runs of BOTH families (--probe-pwbind-r87 AND --probe-btwit-r88)
on the folded bytes. Commit nothing. Report reports/round-87/r87-fold.md +
reports/round-88/r88-fold.md + receipts corpus/live/r87-fold/ + corpus/live/r88-fold/.
TMPDIR=~/Projects/shokunin/tmp. Return: both report paths, green-run shas, blockers.
