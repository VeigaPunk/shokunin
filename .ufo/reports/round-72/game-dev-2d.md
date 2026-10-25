# game-dev-2d round 72 — depth: reorder fabrication (xconnector X1, fd1-inheritance × stdio-withholding)

**Stamp.** 2D lane, round 72 (wave `shokunin-train-20261101-w12`; full 9-seat landing). Lane commits `fee5563` (arm) + `2dd108b` (report-last).

## Work performed

`reorder_*` arm family on `pygame_probe.py` — 5 spawned-child cells sweeping the fd1-OWNER's stdio mode (`buf`/`unbuf`/`flush`/`env`/`late`) + `reorder_self` raw markers on the probe's own wire. Battery: +18 CASES + `RAW_CASES` raw-wire topology predicate (new case class); `PYTHONUNBUFFERED` popped probe-side; `env=CHILD_ENV` folded onto `popen_arm` (r71 verifier defect).

## Measured (55/55, verifier AGREE 5/5, 4-seat independent repro)

- Buffered owner → `prefix_reorder` (`INJECTEDHEAD  TAIL`); -u/flush/env → `midline_splice` (Godot/LOVE topology); late descendant → `append`. Same 19 bytes, only order moves.
- Critic F1 referent correction: variable = **fd1-owner's** mode, not descendant's (13-cell matrices, both regimes).
- Mechanism libc/CPython-general — byte-equal on bare python3 vs in-pygame; C repro confirms writer-side stdio.
- Window = buffer lifetime (byte bound, not wall-ms; +300ms descendant still reorders unflushed). Topology family 4-valued {prefix,infix,midline,append}; SIGKILL → distinct loss class.
- Parser hazard pinned live: `REORDER-CHILD` precedes `REORDER-HEAD` at captured lines 15<16 — what a streaming ARM parser would see.

## Remaining

`reorder_late` ~300ms timing margin (flake surface under load); per-build bufsize=131072 pins; hybrid infix cell un-pinned (nondeterministic); fd2 unprobed. Baseline zero-drift on freeze `44127af` across all 5 families.
