# Aggregator R12 corpus-gate results — refreshed final lane heads

**Cutoff:** 2026-10-20. Scope is the 21 physical child repositories, read only from original paths under `/home/vgpnk/Projects/shokunin` or exact streamed archives. Each original lane's `HEAD` was pinned to the full OID below and resolved to that lane's own Git top level; each `corpus/` status was empty before and after the run. Gate: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/.ufo/waves/round-9/corpus-gate.mjs`, `corpus-gate-v1`, SHA-256 `e7d49942017a8c522e2b16f3de78e60d16a23ffad6838396a8c44897c12299c3`.

The gate's `--round` selector names the aggregator lesson round checked by r10, not the child's latest LOG round. Every run therefore used `--round 12`. Twenty lanes used this exact-SHA snapshot command:

```sh
node .ufo/waves/round-9/corpus-gate.mjs --snapshot \
  /home/vgpnk/Projects/shokunin/<lane>-shokunin <full-40-hex-HEAD> --round 12
```

Each of those 20 runs printed `# expect ... ABSENT`: no frozen expected verdict existed at the exact OID. These are fresh recomputations, not expected-drift checks.

For audio, `git archive` was **1,391,738,880 bytes**, above the gate's `spawnSync` `maxBuffer=1<<30`. The archive was streamed with:

```sh
git -C /home/vgpnk/Projects/shokunin/audio-shokunin archive 0462a5440f23f45707ba681e2a011940e3c923dd | tar -x -C /tmp/kaika-r12-audio-final-_djj915j/audio-shokunin
```

The byte stream SHA-256 was `11692152b88b1e721ffc72dedfca578e5ce82959969b5cedefc8969704a889ac`; its tree was `51444bb9f6ddf0d97d16fdfd25bdf191498c22c5`. A temporary Git index was initialized from the exact OID; `GIT_DIR` pointed at the original audio object store and `GIT_WORK_TREE`/`GIT_INDEX_FILE` only at that extracted snapshot. Its temporary `HEAD` matched the full OID and `git status --porcelain` was empty. The existing gate then ran as `node .ufo/waves/round-9/corpus-gate.mjs --repo /tmp/kaika-r12-audio-final-_djj915j/audio-shokunin --round 12` and emitted `mode=live dirty=0`; this is a streamed-archive/live-interface result, **not** a `--snapshot` result or a claim about a whole dirty original checkout. The temporary tree was removed.

## Exact outputs

Every row below is an observed gate verdict line; exit 1 means the gate found the listed rules, not that the command failed to run. Rules are the gate's exact rule IDs. All 21 original HEADs stayed equal to the pinned value.

| Lane | Full HEAD | Mode / original status | Exact verdict | Exit |
|---|---|---|---|---:|
| audio-shokunin | `0462a5440f23f45707ba681e2a011940e3c923dd` | streamed archive, `--repo`; original status empty | `# verdict audio-shokunin failed findings=6 rules=r4,r8,r10` | 1 |
| chousa-shokunin | `d730ae4c33989ad9c8535764d4cae77b4db869f6` | `--snapshot`; status empty | `# verdict chousa-shokunin failed findings=69 rules=r4,r7,r10,shonen` | 1 |
| game-dev-2d-shokunin | `bce53b83a21ea43ddc2bf050bfe78cb4f2b68550` | `--snapshot`; status empty | `# verdict game-dev-2d-shokunin failed findings=19 rules=r4,r8,r10` | 1 |
| game-dev-3d-shokunin | `3118be0b18dd7351b1faf6ce99d26a34370793ec` | `--snapshot`; original has `?? reports/round-107/` (79 parent-identified user files, untouched) | `# verdict game-dev-3d-shokunin failed findings=42 rules=r4,r8,r10,shonen` | 1 |
| kagi-shokunin | `c2cab35bc92e57e39e5489bac3386db078345b3f` | `--snapshot`; status empty | `# verdict kagi-shokunin failed findings=64 rules=r2,r4,r8,r10` | 1 |
| kaidoku-shokunin | `767adafb97e2eef6980e2ad873d357e16721c467` | `--snapshot`; status empty | `# verdict kaidoku-shokunin failed findings=92 rules=r2,r4,r8,r10,shonen` | 1 |
| kake-shokunin | `5009ecaa1cce10b895617a585ddd3f7c7c923a84` | `--snapshot`; status empty | `# verdict kake-shokunin failed findings=54 rules=r4,r8,r10` | 1 |
| kama-shokunin | `2f7303c242319c1dc96c6bcf7702ac18b3ca1aad` | `--snapshot`; original has two untracked `.ufo/round-10` planning files (untouched) | `# verdict kama-shokunin failed findings=18 rules=r2,r4,r8,r10,shonen` | 1 |
| kasegi-shokunin | `922a4dde90b60b465e2b8b241d1fe363f1f27e98` | `--snapshot`; status empty | `# verdict kasegi-shokunin failed findings=63 rules=r2,r4,r8,r10` | 1 |
| kengaku-shokunin | `6180e4fb92e90c0b172e9788e2c765d097f2e142` | `--snapshot`; status empty | `# verdict kengaku-shokunin failed findings=73 rules=r4,r8,r10` | 1 |
| kotoba-shokunin | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` | `--snapshot`; status empty | `# verdict kotoba-shokunin failed findings=85 rules=r4,r8,r10` | 1 |
| kotodama-shokunin | `4ad26836552462d28a946ca3b067cab0b5ce3532` | `--snapshot`; status empty | `# verdict kotodama-shokunin failed findings=208 rules=r2,r4,r8,r10,shonen` | 1 |
| kumitate-shokunin | `1770305fae20826b39905a8251ddeca6b4957ac4` | `--snapshot`; status empty | `# verdict kumitate-shokunin failed findings=108 rules=r2,r4,r8,r10` | 1 |
| lore-shokunin | `01306d51252f837909af5252c398ee4e31259f9b` | `--snapshot`; original has `?? .scratch/` (26 parent-identified user files, untouched) | `# verdict lore-shokunin failed findings=17 rules=r4,r10` | 1 |
| mado-shokunin | `7dcb785b7b943d03703181b218d7860a7b43007b` | `--snapshot`; status empty | `# verdict mado-shokunin failed findings=82 rules=r4,r8,r10` | 1 |
| mori-shokunin | `6531ac6029e200a6392bb76673b6a17d3c895c96` | `--snapshot`; status empty | `# verdict mori-shokunin failed findings=41 rules=r4,r8,r10` | 1 |
| revenger-shokunin | `cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97` | `--snapshot`; status empty | `# verdict revenger-shokunin failed findings=3 rules=r4,r10` | 1 |
| souji-shokunin | `31984f473ce4bdab61a99b16cca194b28108cb81` | `--snapshot`; status empty | `# verdict souji-shokunin failed findings=18 rules=r2,r4,r10,shonen` | 1 |
| tabi-shokunin | `f032f2dccc8a99632eea52edafa8220284b5c919` | `--snapshot`; status empty | `# verdict tabi-shokunin failed findings=158 rules=r4,r8,r10` | 1 |
| tameshi-shokunin | `18ad5d050ef4bcd830fe513825baed878f025024` | `--snapshot`; status empty | `# verdict tameshi-shokunin failed findings=83 rules=r4,r8,r10` | 1 |
| tsukuroi-shokunin | `b76b5c377eaee3e3d8d47fdddde977828d05dbd5` | `--snapshot`; status empty | `# verdict tsukuroi-shokunin failed findings=98 rules=r4,r10` | 1 |

**R12 result:** all 21 physical lanes are **not conformant** under the gate. Every lane reports `r10` because no `corpus/lessons/round-12-aggregator-*.md` exists. This is the aggregator's lesson-presence debt under the explicit no-child-write boundary, not a child-authored defect. The gate's `r4`, `r7`, `r8`, `r2`, and SHONEN findings are literal form checks; they do not independently establish semantic source defects. Audio additionally reported r7 under-coverage as informational and r8 intent classification as `could-not-evaluate`; literal r8 hits remain failures.

## Limits

The gate implements only r2/r4/r7/r8-literal/r10/SHONEN form. It declares r1/r3/r5/r6/r9, box-3 verifier independence, and SHONEN truth not evaluated. A `not conformant` gate verdict is not a claim that every reported finding is semantically wrong. The three non-empty original status paths are preserved and excluded from archived grading; archived/temp `dirty=0` does not mean the full original checkout was clean. The refreshed remote merges changed only README/wiki, append-only LOG, and `considerthese/2026-10-19.md`; parent verified corpus/runtime blobs unchanged. No child repository was edited by this audit.
