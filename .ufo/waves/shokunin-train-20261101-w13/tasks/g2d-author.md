# r73 AUTHOR (g2d) — reorder topology depth + non-Python owner census

Read SHARED.md + r72 author/adjudicator/boundary reports first.

ARM A — topology depth (xconnector X4). The measured-unpinned set is
{prefix, infix, midline, append, fd2-inversion}; r72 pinned prefix +
midline + append. Now pin:
- INFIX: paced-flush owner (pre-buffered HEAD, timed mid-chunk child
  write between flushes — r72-boundary `paced2` measured INJ@126005 3x).
  Pin bounded ranges (topology class + offset bounds +/-1 chunk), never
  exact offsets.
- DETACH EOF-hold: detached descendant (double-fork/nohup) holds the
  capture pipe open past parent exit — battery EOF arrives late. Pin as
  a harness-integrity cell: parent exits clean, capture EOF delayed;
  bounded timeout so a stuck detach = measured FAIL not hang.
- FD2-INVERSION: descendant writes fd2 while fd2 merges into the same
  capture (2>&1) — r72-boundary fd2mrg measured `ERR\nHEAD  TAIL\n`.
  Pin the merge topology cell.
All cells through the RAW_CASES raw-wire machinery + owner-mode sweep
convention from r72. PYTHONUNBUFFERED stripped from controlled envs.

ARM B — non-Python owner census (xconnector X1, NEW-RUNTIME contact).
Node.js v24.21.0 is on this host (`node --version` to confirm).
Source-derived UNMEASURED predictions:
- node small-write owner -> SPLICE family (libuv uv_write try-write
  fast path = synchronous small writes).
- node >64KB single write -> INFIX (partial fill + event-loop queue
  remainder = third withholding layer beyond libc/Python).
- Control: `fs.writeSync(1,...)` = write-through; C owner cell
  (r72-critic c_reorder.c precedent — buffered C stdio reorders).
Implement a `node_census` arm in pygame_probe.py — spawn `node -e ...`
as the fd1-OWNER (not descendant): node writes HEAD, spawns printf
child via execSync, writes TAIL; capture the wire. Sweep {small,
>64KB, writeSync} cells. Viability-conditional: node absent ->
bounded blocked verdict, never fabricated.

Prior rows byte-identical; PYTHONUNBUFFERED hygiene carries; LOVE
sibling battery untouched = control. Report ->
reports/round-73/r73-author.md.
