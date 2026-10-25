# R12 corpus-gate checkpoint — 19 stable originals

**Status: provisional, not the final 21-lane ledger.** Captured after the critic correction that `--round` selects the aggregator lesson round. These commands therefore use `--round 12` uniformly. Audio and game-dev-2d were omitted because their lane rounds remain open. After the parent's `FINAL LANES READY` signal, pin all 21 original HEADs again, rerun any changed revisions, and add those two lanes; do not freeze this checkpoint as the round report.

## Method

Cwd: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate`.
For each original lane path `/home/vgpnk/Projects/shokunin/<lane>-shokunin`, before the gate I ran `git -C <path> rev-parse --show-toplevel`, `git -C <path> rev-parse HEAD`, and `git -C <path> status --porcelain`. Every reported top-level equaled its lane path; every command exited 0. The exact full SHA below was passed to the existing `.ufo/waves/round-9/corpus-gate.mjs --snapshot <path> <full-SHA> --round 12`. The gate's own tree lines say `mode=snapshot dirty=0`; that describes the archived commit tree, not physical-worktree cleanliness. `# expect … ABSENT` means no frozen expected verdict exists for these new revisions; exit 1 is a fresh recomputation, not an expected-drift result.

The observed command shape for every row:

```sh
node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/Projects/shokunin/<lane>-shokunin <full-40-hex-HEAD> --round 12
```

## Revision-bound verdicts

| Lane | Full HEAD | Original status porcelain entries | R12 gate output | Exit |
|---|---|---:|---|---:|
| chousa | `d730ae4c33989ad9c8535764d4cae77b4db869f6` | 0 | `# verdict chousa-shokunin failed findings=69 rules=r4,r7,r10,shonen` | 1 |
| game-dev-3d | `3118be0b18dd7351b1faf6ce99d26a34370793ec` | 1 (`reports/round-107/`, parent identifies 79 user-owned untracked files; untouched) | `# verdict game-dev-3d-shokunin failed findings=42 rules=r4,r8,r10,shonen` | 1 |
| kagi | `1e9e67ff3f8f9e7118f8a7026c0e79aab9ce42b2` | 0 | `# verdict kagi-shokunin failed findings=64 rules=r2,r4,r8,r10` | 1 |
| kaidoku | `767adafb97e2eef6980e2ad873d357e16721c467` | 0 | `# verdict kaidoku-shokunin failed findings=92 rules=r2,r4,r8,r10,shonen` | 1 |
| kake | `7e17c663b8713daac27774d49d87c4d44ea30747` | 0 | `# verdict kake-shokunin failed findings=54 rules=r4,r8,r10` | 1 |
| kama | `03b5f0e8b9ec421c0b819b31e1bbc452b61dd0f9` | 2 (`.ufo/round-10/SEAT-PROTOCOL.md`, `plan.json`; user-owned untracked, untouched) | `# verdict kama-shokunin failed findings=18 rules=r2,r4,r8,r10,shonen` | 1 |
| kasegi | `13a51920068c48c0c5b3c8c81d5af0df6d4ea337` | 0 | `# verdict kasegi-shokunin failed findings=63 rules=r2,r4,r8,r10` | 1 |
| kengaku | `a42bb40c1767e1ac24394fadda7301ae5409e7ae` | 0 | `# verdict kengaku-shokunin failed findings=73 rules=r4,r8,r10` | 1 |
| kotoba | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` | 0 | `# verdict kotoba-shokunin failed findings=85 rules=r4,r8,r10` | 1 |
| kotodama | `4ad26836552462d28a946ca3b067cab0b5ce3532` | 0 | `# verdict kotodama-shokunin failed findings=208 rules=r2,r4,r8,r10,shonen` | 1 |
| kumitate | `a5683a96cae2fcdcf313e4a3b47dea340d6451a9` | 0 | `# verdict kumitate-shokunin failed findings=108 rules=r2,r4,r8,r10` | 1 |
| lore | `6e804e2e5bff0edcc260c995a058dd724b0c98c0` | 1 (`.scratch/`, parent identifies 26 user-owned untracked files; untouched) | `# verdict lore-shokunin failed findings=17 rules=r4,r10` | 1 |
| mado | `e3e6a8e6ca493e250fb357343816a88e844c4c63` | 0 | `# verdict mado-shokunin failed findings=82 rules=r4,r8,r10` | 1 |
| mori | `bf7cdc4783d0748d525fbfe3ba8fb3d285eb929a` | 0 | `# verdict mori-shokunin failed findings=41 rules=r4,r8,r10` | 1 |
| revenger | `cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97` | 0 | `# verdict revenger-shokunin failed findings=3 rules=r4,r10` | 1 |
| souji | `31984f473ce4bdab61a99b16cca194b28108cb81` | 0 | `# verdict souji-shokunin failed findings=18 rules=r2,r4,r10,shonen` | 1 |
| tabi | `9bc89bfe78b1c455501b2c7a0d9bd061ea539c21` | 0 | `# verdict tabi-shokunin failed findings=158 rules=r4,r8,r10` | 1 |
| tameshi | `a21e9104723e7a46b794b03b8fdcdd1455696f7e` | 0 | `# verdict tameshi-shokunin failed findings=83 rules=r4,r8,r10` | 1 |
| tsukuroi | `d8ec15d5e6c1d93370f5a85b929745e26577f4d8` | 0 | `# verdict tsukuroi-shokunin failed findings=98 rules=r4,r10` | 1 |

**R12 gate result at this checkpoint:** all 19 archived commits return `failed`/exit 1. `r10` is present for all 19 because no `corpus/lessons/round-12-aggregator-*.md` exists at the corresponding commit. This is the aggregator-owned round-12 lesson-presence debt, not a child-authored defect; child-corpus writes are prohibited for this round. Additional failed rule IDs above are the gate's literal mechanical findings.

## Limits and debt

The gate implements r2/r4/r7/r8-literal/r10/SHONEN-form only. r1 source semantics, r3 falsifiability, r5 negative sweeps, r6 quote-location truth, r9 append-only/history, verifier independence, and SHONEN truth are declared not evaluated. `r7` under-coverage is a note, not a finding; `r8` schematic-vs-real classification is `could-not-evaluate`. A `not conformant` gate result does not mean every finding is semantic or that sources are untrue. No child file was written; the three nonempty original status observations above are retained and were not called whole-tree clean.
