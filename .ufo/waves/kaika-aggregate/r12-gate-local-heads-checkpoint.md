# R12 corpus-gate outputs at original local HEADs — pre-refresh checkpoint

**Non-final provenance record.** Captured after the parent's `FINAL LANES READY` announcement but before the parent fetched/preserved 14 newer live-branch commits that were absent from local object databases. The gate outcomes below are valid only at these exact local OIDs; do not label them the refreshed or published lane heads. At closure, compare with `local://kaika-final-lane-heads.json`; rerun each changed OID. No child path was written.

Cwd for snapshot commands: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate`. Gate: `.ufo/waves/round-9/corpus-gate.mjs` (`corpus-gate-v1`, sha256 `e7d49942017a8c522e2b16f3de78e60d16a23ffad6838396a8c44897c12299c3`). Every R12 gate selected the **aggregator review round** uniformly: `--round 12`, so r10 asks for `corpus/lessons/round-12-aggregator-*.md`. All 21 original lane roots passed `git rev-parse --show-toplevel` identity and their full local `HEAD` was pinned before the gate.

For 20 lanes the exact command shape was:

```sh
node .ufo/waves/round-9/corpus-gate.mjs --snapshot \
  /home/vgpnk/Projects/shokunin/<lane>-shokunin <full-40-hex-HEAD> --round 12
```

Audio's 1,391,728,640-byte tar stream exceeds the gate's 1 GiB in-memory snapshot buffer. It was graded using the same existing gate's `--repo` interface over a fully streamed `git archive <HEAD> | tar -x` tree, with a temporary index built from that exact OID and `GIT_DIR`/`GIT_WORK_TREE`/`GIT_INDEX_FILE` set to the original object store plus temporary snapshot. Temporary status was empty, full HEAD matched, original HEAD was unchanged after, and the temp tree was removed. This is **streamed-archive/live-interface**, not `--snapshot`; it was not a grade of the original live checkout.

| Physical lane | Exact original local HEAD | Original status porcelain lines | Gate mode | Exact `# verdict` summary | Gate exit |
|---|---|---:|---|---|---:|
| audio-shokunin | `63593ded480a2f9b0cf59dc39f7efb72250fe8b7` | 0 | streamed archive / `--repo`, `dirty=0` | `failed findings=6 rules=r4,r8,r10` | 1 |
| chousa-shokunin | `d730ae4c33989ad9c8535764d4cae77b4db869f6` | 0 | `--snapshot`, `dirty=0` | `failed findings=69 rules=r4,r7,r10,shonen` | 1 |
| game-dev-2d-shokunin | `7461a0868798c5fb7a08d119fa71e472172726c5` | 0 | `--snapshot`, `dirty=0` | `failed findings=19 rules=r4,r8,r10` | 1 |
| game-dev-3d-shokunin | `3118be0b18dd7351b1faf6ce99d26a34370793ec` | 1 (`reports/round-107/`, parent identifies 79 user-owned files) | `--snapshot`, `dirty=0` | `failed findings=42 rules=r4,r8,r10,shonen` | 1 |
| kagi-shokunin | `1e9e67ff3f8f9e7118f8a7026c0e79aab9ce42b2` | 0 | `--snapshot`, `dirty=0` | `failed findings=64 rules=r2,r4,r8,r10` | 1 |
| kaidoku-shokunin | `767adafb97e2eef6980e2ad873d357e16721c467` | 0 | `--snapshot`, `dirty=0` | `failed findings=92 rules=r2,r4,r8,r10,shonen` | 1 |
| kake-shokunin | `7e17c663b8713daac27774d49d87c4d44ea30747` | 0 | `--snapshot`, `dirty=0` | `failed findings=54 rules=r4,r8,r10` | 1 |
| kama-shokunin | `03b5f0e8b9ec421c0b819b31e1bbc452b61dd0f9` | 2 (`.ufo/round-10/SEAT-PROTOCOL.md`, `plan.json`) | `--snapshot`, `dirty=0` | `failed findings=18 rules=r2,r4,r8,r10,shonen` | 1 |
| kasegi-shokunin | `13a51920068c48c0c5b3c8c81d5af0df6d4ea337` | 0 | `--snapshot`, `dirty=0` | `failed findings=63 rules=r2,r4,r8,r10` | 1 |
| kengaku-shokunin | `a42bb40c1767e1ac24394fadda7301ae5409e7ae` | 0 | `--snapshot`, `dirty=0` | `failed findings=73 rules=r4,r8,r10` | 1 |
| kotoba-shokunin | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` | 0 | `--snapshot`, `dirty=0` | `failed findings=85 rules=r4,r8,r10` | 1 |
| kotodama-shokunin | `4ad26836552462d28a946ca3b067cab0b5ce3532` | 0 | `--snapshot`, `dirty=0` | `failed findings=208 rules=r2,r4,r8,r10,shonen` | 1 |
| kumitate-shokunin | `a5683a96cae2fcdcf313e4a3b47dea340d6451a9` | 0 | `--snapshot`, `dirty=0` | `failed findings=108 rules=r2,r4,r8,r10` | 1 |
| lore-shokunin | `6e804e2e5bff0edcc260c995a058dd724b0c98c0` | 1 (`.scratch/`, parent identifies 26 user-owned files) | `--snapshot`, `dirty=0` | `failed findings=17 rules=r4,r10` | 1 |
| mado-shokunin | `e3e6a8e6ca493e250fb357343816a88e844c4c63` | 0 | `--snapshot`, `dirty=0` | `failed findings=82 rules=r4,r8,r10` | 1 |
| mori-shokunin | `bf7cdc4783d0748d525fbfe3ba8fb3d285eb929a` | 0 | `--snapshot`, `dirty=0` | `failed findings=41 rules=r4,r8,r10` | 1 |
| revenger-shokunin | `cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97` | 0 | `--snapshot`, `dirty=0` | `failed findings=3 rules=r4,r10` | 1 |
| souji-shokunin | `31984f473ce4bdab61a99b16cca194b28108cb81` | 0 | `--snapshot`, `dirty=0` | `failed findings=18 rules=r2,r4,r10,shonen` | 1 |
| tabi-shokunin | `9bc89bfe78b1c455501b2c7a0d9bd061ea539c21` | 0 | `--snapshot`, `dirty=0` | `failed findings=158 rules=r4,r8,r10` | 1 |
| tameshi-shokunin | `a21e9104723e7a46b794b03b8fdcdd1455696f7e` | 0 | `--snapshot`, `dirty=0` | `failed findings=83 rules=r4,r8,r10` | 1 |
| tsukuroi-shokunin | `d8ec15d5e6c1d93370f5a85b929745e26577f4d8` | 0 | `--snapshot`, `dirty=0` | `failed findings=98 rules=r4,r10` | 1 |

At these local OIDs, all 21 produce `not conformant` under the R12 gate selector. Every `r10` finding is the aggregator-owned absence of a round-12 aggregator lesson; no child-corpus write is authorized, so do not attribute it to lane authors. The other failed-rule IDs and finding counts are the exact gate output. `# expect … ABSENT` means a fresh recomputation with no frozen expected result, not an expected-drift check.

## Limits

- This is a local-HEAD checkpoint before the parent's fetch/preserve/integration of 14 remote-only commits. The user's final report must use the refreshed OID map; do not copy an old row forward unless its full OID still matches.
- `dirty=0` is the gate's archived tree status or the isolated streamed archive's status, not proof the original checkout is clean. Preserve the three user-owned untracked paths above; they were not modified or committed.
- Implemented gate checks: r2/r4/r7/r8-literal/r10/SHONEN form. Declared not-evaluated: r1/r3/r5/r6/r9, verifier independence, SHONEN truth; r8 classification is `could-not-evaluate`, and r7 under-coverage is a note. A pass/fail is not whole-corpus semantic conformance.
- All original HEADs matched their pre-gate pins after the reads. No lane, MANIFEST, report, or original checkout was modified.
