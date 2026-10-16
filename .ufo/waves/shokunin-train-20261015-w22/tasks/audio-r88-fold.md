# audio-r88-fold — repair the r88 arms after GATE FAIL (committed dossier)

WAIT until the r89+ author commits (measure_audio.py custody; can run inside the r89 fold
window — r87 and r88 folds share the same file). Apply queue:

1. wd_dump_empty bracket race (verifier F1 + reviewer F1, 2-seat): arm requires pw-dump ''
   id-set == census exactly; transient clients drift +-1. Fix: arm on set MEMBERSHIP
   (dump ids subset of census or vice versa) not equality — or retry-on-drift with
   coverage_blocked, not hard fail.
2. Foreign stderr pollution (verifier F2): one-shot `pw-cli info <id>` prints
   `remote 0: error ... no global` when a foreign object dies mid-call, flipping the
   empty-channel arms (wd_silent_cli_meta, wd_cli_meta_extra, wd_enum_num2). Fix: filter
   foreign remote-0 lines or arm only on own-node errors.
3. error_class precedence (verifier F3, r87-F4 realized): preceding foreign res:-2 masks
   real res:-22 (bz_create_midi/a2dp.source). Fix: take the LAST error_class line, or
   scope to own request id.
4. pt_nneg/pt_nabc flush-timing lottery (F4): frame arm is timing-dependent; bound it.
5. bz_tree truncated enumeration (F8): false-PASS direction; bound or declare.
6. bz_device negative-only (reviewer F2): fault-injected absence still green — needs a
   positive-side witness or declared scope.
7. Missing-leg silent skips -> coverage_blocked (critic F1-3, reviewer F3).
8. Simplifier patch net -7 (T1-T6) proven — apply.
9. Citation fixes: uncited RED dev run (scribe ADJ-1 + critic F7, 2-seat).

After applying: two green runs on folded bytes -> verifier-r2 -> adjudication.
Report reports/round-88/r88-fold.md + receipts corpus/live/r88-fold/.
