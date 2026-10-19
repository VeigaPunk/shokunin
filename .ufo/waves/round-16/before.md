# Round 16 — BEFORE measurements (protocol lane)

- Arc: kaika fleet round 16, lane `protocol`, branch `kaika/protocol`.
- Pinned revision: `31baf5cb07049637a09e18cc421535e376beecd1` (lane base; subject "fleet backlog commit: rounds 33-42 …").
- Restore target for the two root ledgers: `12f2da5` (fleet ledger round-48; last good fleet bytes).
- Write scope of this file set: this file only. Every fleet-repo read below uses the git object database (`git show <rev>:<path>`, `git ls-tree`, `git cat-file`) and never the working tree, because L1 already restored `SCORECARD.md`/`LOG.md` uncommitted. Observed `git status --porcelain`: ` M LOG.md`, ` M SCORECARD.md`.
- Kotoba provenance read-only via `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin`.
- Commands run with cwd `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-protocol`.

## Measurements

| metric | command | output @31baf5c | @12f2da5 (restore target) |
|---|---|---|---|
| SCORECARD.md line 1 | `git show 31baf5c:SCORECARD.md \| head -1` | `# kotoba-shokunin — Scorecard` · exit 0 | `# shokunin (main repo) — Scorecard` · exit 0 |
| LOG.md line 1 | `git show 31baf5c:LOG.md \| head -1` | `# kotoba-shokunin — Iteration Log` · exit 0 | `# shokunin (main repo) — Iteration log` · exit 0 |
| SCORECARD.md sha256 | `git show 31baf5c:SCORECARD.md \| sha256sum` | `a4ec534857be05a3399e40e492423cf7d32a5a152bd7031fa6b38052dd0401e2  -` · exit 0 | `9483fb8d244bb8032c2df75b3fdc444176d5653bf34d56226b7cc49683883fcf  -` · exit 0 |
| SCORECARD.md blob | `git rev-parse 31baf5c:SCORECARD.md` | `3fc970db77eb7e42a2f1e3ee9236e067b281a0a8` · exit 0 | `37b5ffae9e45356f4b91892c82c781fb713fab7e` · exit 0 |
| LOG.md sha256 | `git show 31baf5c:LOG.md \| sha256sum` | `998274c0205921c7a2babd3b0dbb5284d0452c4de0b4fa2d1cec323c022527bf  -` · exit 0 | `df559cd019034067bec68c1b52d49ed1eeaeb130e74a1a8d5585b00d5cfef17e  -` · exit 0 |
| LOG.md blob | `git rev-parse 31baf5c:LOG.md` | `99de619db3908c82c8ebd77764eff953eb331daa` · exit 0 | `faaf3bb8c157cbf9b4817b0b22b2f4c06dd4a880` · exit 0 |
| `## Aggregator lane` count in SCORECARD.md | `git show 31baf5c:SCORECARD.md \| grep -c '^## Aggregator lane'` | `0` · exit 1 | `1` · exit 0 |
| `## Gate registry — protocol lane registry home` count in SCORECARD.md | `git show 31baf5c:SCORECARD.md \| grep -c '^## Gate registry — protocol lane registry home'` | `0` · exit 1 | `1` · exit 0 (line 147) |
| `\| closure-check \| gate \|` row count in SCORECARD.md | `git show 31baf5c:SCORECARD.md \| grep -cE '^\| closure-check \| gate \|'` | `0` · exit 1 | `1` · exit 0 |
| Same three counts in LOG.md | `git show 31baf5c:LOG.md \| grep -c …` (aggregator / registry / closure row) | `0` / `0` / `0` · exit 1 each | `0` / `0` / `0` · exit 1 each |
| Incident diff | `git diff --numstat 12f2da5 31baf5c -- SCORECARD.md LOG.md` | `1356	845	LOG.md`<br>`165	395	SCORECARD.md` (added / removed) · exit 0 | — (baseline) |
| Kotoba equality, c8e233d SCORECARD | `git -C …/kotoba-shokunin rev-parse c8e233d:SCORECARD.md` | `c2ce6947ce9f273fca23e3f0bb3b661281eb3f34` — **not equal** to `3fc970db`; `cmp` exit 1 (`differ: char 1485, line 28`) | n/a |
| Kotoba equality, c8e233d LOG | `git -C …/kotoba-shokunin rev-parse c8e233d:LOG.md` | `4a990b94ad02189c38571552408aade9b4f7505f` — **not equal** to `99de619d`; `cmp` exit 1 (`EOF on - after byte 131795`) | n/a |
| Kotoba equality, b7470d7 SCORECARD (equality pin) | `git rev-parse b7470d7:SCORECARD.md` + `cmp` | `3fc970db77eb7e42a2f1e3ee9236e067b281a0a8`; `cmp` exit 0; sha256 `a4ec5348…` | n/a |
| Kotoba equality, b7470d7 LOG (equality pin) | `git rev-parse b7470d7:LOG.md` + `cmp` | `99de619db3908c82c8ebd77764eff953eb331daa`; `cmp` exit 0; sha256 `998274c0…` | n/a |
| `round-14/registry-home-rerun` file count | `git ls-tree -r --name-only 31baf5c -- .ufo/waves/round-14/registry-home-rerun \| wc -l` | `0` · exit 0 (path absent at 31baf5c) | at `b2f2efa`: `12` · exit 0 |
| Gate file presence | `git ls-tree 31baf5c -- .ufo/gates/root-ledgers.py` and `git cat-file -e 31baf5c:.ufo/gates/root-ledgers.py` | ls-tree: empty · exit 0; cat-file: `fatal: path '.ufo/gates/root-ledgers.py' does not exist in '31baf5c'` · **exit 128** (absent) | n/a |
| PROTOCOL.md size | `git show 31baf5c:PROTOCOL.md \| wc -l -c` | `513 44449` · exit 0 | identical: `git diff --stat 12f2da5 31baf5c -- PROTOCOL.md PROTOCOL-APPENDIX.md` empty · exit 0 |
| PROTOCOL-APPENDIX.md size | `git show 31baf5c:PROTOCOL-APPENDIX.md \| wc -l -c` | `51 14390` · exit 0 | identical (same empty diff) |
| `SOURCES` occurrences in PROTOCOL.md | `git show 31baf5c:PROTOCOL.md \| grep -c 'SOURCES'` | `0` · exit 1 | — |
| `frontier` occurrences (case-insensitive) | `git show 31baf5c:PROTOCOL.md \| grep -ci 'frontier'` | `0` · exit 1 | — |
| `mistake` occurrences (case-insensitive) | `git show 31baf5c:PROTOCOL.md \| grep -ci 'mistake'` | `0` · exit 1 | — |
| `Sources & frontier` occurrences | `git show 31baf5c:PROTOCOL.md \| grep -c 'Sources & frontier'` | `0` · exit 1 | — |
| `root-ledgers` occurrences in PROTOCOL.md | `git show 31baf5c:PROTOCOL.md \| grep -c 'root-ledgers'` | `0` · exit 1 | — |
| Table rows in PROTOCOL-APPENDIX.md | `git show 31baf5c:PROTOCOL-APPENDIX.md \| grep -c '^\|'` | `44` · exit 0 | — |
| `.ufo/state/protocol.round` | `git show 31baf5c:.ufo/state/protocol.round` | `14\n` (`od -An -c` → `1 4 \n`) · exit 0 | fleet root worktree: `14\n` · exit 0 |
| Round-16 protocol report exists | `git cat-file -e 31baf5c:.ufo/reports/round-16/protocol.md` | `fatal: path '.ufo/reports/round-16/protocol.md' does not exist in '31baf5c'` · **exit 128** (absent). Fleet root `test -e …/round-16/protocol.md` · exit 1 (absent). Lane WT listing: kagi, kake, kasegi, kengaku, kotoba, kotodama, kumitate only. | **no collision** |
| Round-15 protocol report exists | `git cat-file -e 31baf5c:.ufo/reports/round-15/protocol.md` | exit 0 (present); fleet root `test -e …/round-15/protocol.md` · exit 0 (present) | n/a |

## Collision check (lane-addendum 6.2)

Round-16 report path `.ufo/reports/round-16/protocol.md` is **free** at `31baf5c`, in the fleet root worktree, and in the lane worktree. Fail-closed signal: **not raised**. Round-15 `protocol.md` exists in both (control).

## Conflict (verbatim, for the canonical judge)

L1 fact stated: "blobs 3fc970db (SCORECARD) and 99de619d (LOG) at 31baf5c are byte-identical to `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin` commit c8e233d (2026-10-19 10:25) versions."

L1 correction received during round 16: the pinned blobs equal kotoba commit **b7470d7** (2026-10-19 07:36:02, "round 36"), not c8e233d; c8e233d is the commit that later replaced those blobs. Use b7470d7 for the equality pin in scripts, LOG text, and appendix rows.

Measurement recorded before the correction:

- `c8e233d:SCORECARD.md` = `c2ce6947…` (sha256 `4a4cb037…`); `c8e233d:LOG.md` = `4a990b94…` (sha256 `ba9141a3…`); `cmp` exits 1 for both against the `31baf5c` bytes.
- `b7470d7:SCORECARD.md` = `3fc970db…`; `b7470d7:LOG.md` = `99de619d…`; `cmp` exits 0 for both, sha256 identical to `31baf5c`.
- Kotoba lineage: `b7470d7` (round 36, 2026-10-19 07:36:02 -0300) carries the pinned blobs; `c8e233d` (round 37, 2026-10-19 10:25:21 -0300) has `diff-tree --name-status` `M` on both paths, i.e. it replaced those bytes with the round-37 versions.

No claim is upgraded: the incident bytes and blobs stand as measured. After the L1 correction, attribution is settled at `b7470d7`; the pre-correction statement above is retained verbatim for audit. The `31baf5c` ledgers carry the kotoba-branded headers and lack every fleet marker, so the incident itself is unchanged.

## Known limits

- Working-tree state was read only through `git status --porcelain`; no working-tree file content was used for any metric.
- `registry_below_aggregator` ordering was not measured directly; at `12f2da5` line numbers are registry 147, aggregator 199 (registry above aggregator).
- No network access, no execution of `.ufo/gates/root-ledgers.py` (absent at the pinned revision), no commits or adds.
