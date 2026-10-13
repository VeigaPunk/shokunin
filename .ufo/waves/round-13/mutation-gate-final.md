# Final checker battery (lane-universe revision)

Checker SHA-256: `bf8d34fbaafa17cb0d1f343b1f526c936bc687c56e04a1fd24ecd3c3e67d5c83`. All runs use synthetic copies under `/tmp/r13-final`, never the live ledger. Kill criterion is finding-set difference that names the mutation; exit code alone is insufficient.

The committed replay harness is `mutants/rerun.sh`; it was run once and printed:
```
closure-check: ok selftest passed=19/19 failed=0
baseline: match  expected exit=1  analyzed exit=1
baseline: match  expected exit=1  analyzed exit=1
baseline: match  expected exit=0  analyzed exit=0
synthetic-pristine closure-check: debt debt=5 contradictions=0 unrowed_terminated=0 pending_round=6
```

m1–m9 were replayed against the final checker with the prior finding-set criterion: all nine remain killed (m1/m4/m5 by history-pin mismatch, m8 unavailable, m9 unanchored; m2/m3/m6/m7 structural findings). Finding-set score: **9/9 (100%)**. Exit-only score: **8/9 (88.9%)**, with m5 the non-separable exit-1 case.

m10 deleted `.ufo/state/kama.round` while retaining `launch kama round=1`. Result: `closure-check: debt debt=9 contradictions=0 unrowed_terminated=3 pending_round=7`, exit 1, but no `kama` finding or pending row was emitted. **The gate is blind to this mutation** when the driver-written counter is removed; this is a residual universe-source gap.

m11 copied frozen `round-12/frozen/post` to `round-13/frozen/post`. `--frozen post` exited 3 with: `frozen name post is ambiguous across 2 roots (round-13, round-12): pass --frozen <wave>/post or --frozen-root DIR`. `--frozen round-12/post` still printed `baseline: match expected exit=0 analyzed exit=0`, exit 0. m11 is killed by the ambiguity finding.
