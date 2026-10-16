# audio-r87-fold — repair the r87 arms after GATE FAIL (commit c8a958e2 dossier)

WAIT until the r89 author commits (measure_audio.py custody), then apply the queue:

1. GATE-BLOCKER (verifier F1 + reviewer F1, 2-seat measured): `create_badfac`/`create_usage`
   verdicts read only the last 500 chars of a BLOCK-BUFFERED pw-cli held-session log. Refusal
   printed 12/12 but in-window 2/12; 4/7 committed-byte replays red. FIX: match the async
   refusal over the full session log (or the recorded `errors` list), not the tail window.
2. m_sysex vacuous arm (reviewer F2 + simplifier F1): "stays running" arm fires only on rc==0
   while harness SIGTERM gives rc=1; window 1.7s < 4.0s fixture. Arm on the node-alive
   observation (law proven true at 9.0s), not the exit code.
3. skeleton rc arm accepts harness SIGKILL (reviewer F3): the 26B file witness is the only
   discriminating term — tighten or declare.
4. midi dead-target census silent-skip + mdump_live empty-attempts -> coverage_blocked
   (critic F1/F2).
5. Hard-no-link switches accept real-link-with-unresolved-peer (critic F3): fix the falsy
   in_node drop in _pwbind_r87_consumers / r85_edges lookup.
6. Cold_nowarm `or "unknown global"` bypass (reviewer F4); p_coll/foreign unarmed (F5).
7. Simplifier patch net -7 (T1-T9) — proven, apply.
8. Citation fixes: 2 undisclosed RED dev runs (scribe ADJ-1); line refs ~90 low; +2083 exact.

After applying: two green runs on folded bytes -> verifier-r2 gate -> adjudication.
Report reports/round-87/r87-fold.md + receipts corpus/live/r87-fold/.
