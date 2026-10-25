# Final SOURCES census and structural checks — refreshed named lane snapshots

**Cutoff:** 2026-10-20. **Input set:** all 21 physical child repositories at the refreshed full HEADs after the parent-confirmed documentation-only merges. Every input path resolved to its own Git root, each original `HEAD` matched the full OID below before and after archiving, and every original `corpus/` status was empty. All four modes read extracted full-tree `git archive` snapshots, not moving branches, dirty user files, or `repo=.` fleet-root lanes. The temporary snapshot was deleted after all modes. No child repository was modified.

- Fleet worktree: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate`, `HEAD=54a20d39c533dcfd41473582e12ed380cf3d932b`.
- Script: `scripts/sources-census.sh`, blob `3f314620b2395eeb70d8405410132027dfe608e4`; corrected to parse 0–3 leading Markdown spaces and exclude the main-repo `repo=.` lanes from default discovery. Parent's child-only-root / 96-check evidence is `.ufo/waves/kaika-w3/census-indent-final-smoke.txt` and `.ufo/waves/kaika-w3/fleet-source-integration-smoke.txt`. This run passes explicit archived child directories to keep its population unambiguous.
- Snapshot root was `/tmp/kaika-r12-census-final-refresh-k6nha043`, removed on completion. Aggregate tar bytes: **3,286,661,120**. Per-lane archive hashes and exact full-OID / `corpus/SOURCES.md` blob pins are below.

| Lane | Full HEAD | SOURCES blob | Archive bytes | Archive SHA-256 |
|---|---|---|---:|---|
| audio-shokunin | `0462a5440f23f45707ba681e2a011940e3c923dd` | `48d5b87b07cab290672f71195bb70687a8665776` | 1,391,738,880 | `11692152b88b1e721ffc72dedfca578e5ce82959969b5cedefc8969704a889ac` |
| chousa-shokunin | `d730ae4c33989ad9c8535764d4cae77b4db869f6` | `8429343f1b750a9fd4bc7a470373d99ae57d1ad3` | 2,846,720 | `f9c3f99fb9d2109ae94f601deedd86704fbf721e27a7c7d0331ac6f9d4db5707` |
| game-dev-2d-shokunin | `bce53b83a21ea43ddc2bf050bfe78cb4f2b68550` | `6eb0f26c5e3f61567527a45d4b7c95ae52815dd6` | 957,132,800 | `d9fc0dc3c012d18a3bb56328d10e449cd2f7b978b0953f9fd396dfd78b2c3b63` |
| game-dev-3d-shokunin | `3118be0b18dd7351b1faf6ce99d26a34370793ec` | `07a5816947c98a6c39b4ace520aa15654c74c795` | 442,808,320 | `a3257e29818f7c272a7b6c6664f7900e90970b30db3651746268d85c6cb9452d` |
| kagi-shokunin | `c2cab35bc92e57e39e5489bac3386db078345b3f` | `36e166f08fefd6053c1effde41ec6174cb0f5820` | 1,392,640 | `84c18d83f867572c3a0843b981ced80b3fca3de502920500d31dacdab2186b86` |
| kaidoku-shokunin | `767adafb97e2eef6980e2ad873d357e16721c467` | `a411c18c74c0690c1073e08f241c53779750263d` | 146,513,920 | `5fb1f1a85579e35bb775b67904d3d0ac86a6bc46663fe7fcb98667b5bb9b4d13` |
| kake-shokunin | `5009ecaa1cce10b895617a585ddd3f7c7c923a84` | `bb7ed1649256a0ccfd5f8bdc71f1b9c003b9ee09` | 1,484,800 | `b7469e657db5b645c50bd0553cf1016254e2a29cbf832878c7733868b67b9008` |
| kama-shokunin | `2f7303c242319c1dc96c6bcf7702ac18b3ca1aad` | `7de1360655eadada356fe110813c6e1338142551` | 808,960 | `0f8ce554141f557c3e849e6168a54e118c41f543842dabdd63dbde71d94bfe02` |
| kasegi-shokunin | `922a4dde90b60b465e2b8b241d1fe363f1f27e98` | `01fcdbb6b833482ac15e8211624832f52b8abb9e` | 1,259,520 | `999476e7d4283d18b1c09ceb7e5b0051ba746e74d284b4e612e45d08bc1a949e` |
| kengaku-shokunin | `6180e4fb92e90c0b172e9788e2c765d097f2e142` | `74070565c0932a39737fc7d24250c5a716802e40` | 7,055,360 | `40fce2d05b124fac450b824e77a2fa00b4d34350aee379c1bd3a0e14aa93b2a6` |
| kotoba-shokunin | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` | `a048aef0997e68881c9740e878d2fe01402bb04b` | 108,236,800 | `bc1783cc55f76c1547cc23724e79800196c86495f988e6056daacf1d218c582a` |
| kotodama-shokunin | `4ad26836552462d28a946ca3b067cab0b5ce3532` | `34e27f6a1878b0de2bf69785ef2c4b391a1fdb01` | 80,066,560 | `f623f789e8879c9378f41a8062090ec4c916fa08899a2c7a990b0d9a4a8e1703` |
| kumitate-shokunin | `1770305fae20826b39905a8251ddeca6b4957ac4` | `6e92b79bdfe022648574c271c4a9a9768238912b` | 2,304,000 | `99bebc407adebbf0fdba0682812bb4398e4a4d42af799523962a8fba064702ca` |
| lore-shokunin | `01306d51252f837909af5252c398ee4e31259f9b` | `a547b1b60314cb7aacdebad9fb7852509c8e59d3` | 44,195,840 | `0850184a603aa3ef067a82ebe63d601995e1bd002569adefc7f8e416441c2c3c` |
| mado-shokunin | `7dcb785b7b943d03703181b218d7860a7b43007b` | `56f8f49c9913455e89bdf91434130f0d4637b887` | 1,986,560 | `b1eae00493063a41ae9816f9c73f908247b731ac14142ad9f8253afb1b7cb00d` |
| mori-shokunin | `6531ac6029e200a6392bb76673b6a17d3c895c96` | `9065f76f35d7185b4fc5b2ba10c9a05a5cd1186f` | 2,242,560 | `9da3b8a367e7dc4e801f941d527e37c43078f711cb718a645548a82082994a90` |
| revenger-shokunin | `cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97` | `2fcf0d901c71116ea951eb012be67125c2980948` | 5,048,320 | `3005bc8d9b2adb210ceb004fcdb665bed053e105d7c6efae975bdf69154c0711` |
| souji-shokunin | `31984f473ce4bdab61a99b16cca194b28108cb81` | `a67b6f573f1fbb52198c028f0d7e77f5fa3b7f35` | 69,744,640 | `7bdf6ad7eedcd9cdd7e2918fea00c89176b92588f7daf8fba9e0fe8e134bfc4c` |
| tabi-shokunin | `f032f2dccc8a99632eea52edafa8220284b5c919` | `89a69384adeff8ccda3b41e4938abc40425492b9` | 16,220,160 | `9f2b88c5661706a302bf152b5892f4db9d0372f62a040930be7a7a558e3f6a30` |
| tameshi-shokunin | `18ad5d050ef4bcd830fe513825baed878f025024` | `b1cff984384860ad7b3d301aef493ba0386c3a68` | 1,822,720 | `2718649eab4a05a53c263b54eee99a19433945c103e8362e07189c65bded4611` |
| tsukuroi-shokunin | `b76b5c377eaee3e3d8d47fdddde977828d05dbd5` | `194059c471e25702edb6b39c58abd91a79f3d8b5` | 1,751,040 | `65e16273869dc84b759f15a66f043fc3c651f27a89566437f62d63495357f117` |

All commands used the 21 explicit snapshot paths under `/tmp/kaika-r12-census-final-refresh-k6nha043`, in physical basename sort order. Command shape (substitute each mode in `{census,validate,shared,overdue}`):

```sh
bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/scripts/sources-census.sh \
  <census|validate|shared|overdue> --root /tmp/kaika-r12-census-final-refresh-k6nha043 \
  --today 2026-10-20 \
  /tmp/kaika-r12-census-final-refresh-k6nha043/audio-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/chousa-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/game-dev-2d-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/game-dev-3d-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/kagi-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/kaidoku-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/kake-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/kama-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/kasegi-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/kengaku-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/kotoba-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/kotodama-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/kumitate-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/lore-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/mado-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/mori-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/revenger-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/souji-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/tabi-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/tameshi-shokunin \
  /tmp/kaika-r12-census-final-refresh-k6nha043/tsukuroi-shokunin
```

## `census` — exit 0

| Population | Rows | Tier A | Tier B | Tier C | Tier invalid | Mined | Queued | Rejected | Status invalid | Missing |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **FLEET (21 archived child lanes)** | **576** | **500** | **33** | **43** | **0** | **307** | **220** | **49** | **0** | **0** |

| lane | rows | A | B | C | mined | queued | rejected |
|---|---:|---:|---:|---:|---:|---:|---:|
| audio-shokunin | 15 | 11 | 2 | 2 | 14 | 0 | 1 |
| chousa-shokunin | 18 | 14 | 1 | 3 | 8 | 7 | 3 |
| game-dev-2d-shokunin | 31 | 30 | 1 | 0 | 10 | 19 | 2 |
| game-dev-3d-shokunin | 36 | 33 | 2 | 1 | 6 | 28 | 2 |
| kagi-shokunin | 16 | 14 | 0 | 2 | 14 | 1 | 1 |
| kaidoku-shokunin | 22 | 20 | 1 | 1 | 21 | 0 | 1 |
| kake-shokunin | 18 | 16 | 0 | 2 | 14 | 2 | 2 |
| kama-shokunin | 30 | 27 | 0 | 3 | 17 | 8 | 5 |
| kasegi-shokunin | 27 | 25 | 0 | 2 | 15 | 10 | 2 |
| kengaku-shokunin | 26 | 24 | 0 | 2 | 18 | 5 | 3 |
| kotoba-shokunin | 11 | 10 | 0 | 1 | 4 | 6 | 1 |
| kotodama-shokunin | 47 | 34 | 6 | 7 | 20 | 22 | 5 |
| kumitate-shokunin | 20 | 19 | 1 | 0 | 9 | 9 | 2 |
| lore-shokunin | 32 | 24 | 3 | 5 | 12 | 17 | 3 |
| mado-shokunin | 39 | 35 | 1 | 3 | 27 | 9 | 3 |
| mori-shokunin | 34 | 31 | 2 | 1 | 12 | 21 | 1 |
| revenger-shokunin | 15 | 14 | 0 | 1 | 12 | 1 | 2 |
| souji-shokunin | 33 | 29 | 3 | 1 | 16 | 15 | 2 |
| tabi-shokunin | 28 | 22 | 4 | 2 | 20 | 6 | 2 |
| tameshi-shokunin | 44 | 37 | 5 | 2 | 12 | 29 | 3 |
| tsukuroi-shokunin | 34 | 31 | 1 | 2 | 26 | 5 | 3 |

Rows = A+B+C = 576 and mined+queued+rejected = 576; invalid tier/status histograms are zero.

## `validate` — exit 0; seven warnings, zero errors

Observed: 21 `ok`, **0 E-code errors**, **7 W-code warnings**, 0 missing. Warnings are preserved as warnings, not disguised as invalid rows:

```text
audio-shokunin W01 S007 tierC mined used-by=corpus/knowledge/2026-10-19-game-loudness-whole-mix-protocol.md, corpus/lessons/round-101.md
audio-shokunin W04 S014 duplicate url raw.githubusercontent.com/FFmpeg/FFmpeg/n9.0.1/libavfilter/af_loudnorm.c across scopes
audio-shokunin W04 S015 duplicate url www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1770-5-202311-I!!PDF-E.pdf across scopes
lore-shokunin W04 S017 duplicate url arxiv.org/html/2603.05890 across scopes
lore-shokunin W01 S027 tierC mined used-by=corpus/knowledge/r103-canon-status-and-supersession.md
lore-shokunin W04 S032 duplicate url www.iso.org/standard/70908.html across scopes
mado-shokunin W04 S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
```

Warnings are non-failing by the script contract. They do not certify that a row supports its cited claim.

## `shared` — exit 0

```text
godot-gdunit-labs.github.io/gdUnit4/latest/advanced_testing/cmd shared game-dev-2d-shokunin,game-dev-3d-shokunin
kubernetes.io/docs/concepts/workloads/pods/probes shared kama-shokunin,mori-shokunin
```

## `overdue --today 2026-10-20` — exit 0

Overdue findings: **0**. The command emitted 557 cadence rows; histogram:

```text
180d=88; 30d=2; 365d=72; 730d=10; 90d=100; every round=1; frozen=2;
on-change=5; on-commit=2; on-gate-change=1; on-release=274
```

`overdue` judges ISO dates and `NNd` cadences. Symbolic cadences are reported, not declared fresh or overdue; `overdue=0` is not a claim that all sources are fresh.

## Limits

- This is commit-bound structural inventory. `validate` checks row shape, IDs, enums/date/recheck syntax, duplicate URL+scope, community tier, `used-by` path existence, and row placement. It did **not** reopen URLs or prove `teaches`/anchors, that a `used-by` target cites the `S###`, that `supersedes` targets are valid, or that a path is semantically ordered.
- The input set is 21 physical child repositories, not `shokunin.conf` lanes and not the fleet root's `repo=.` entries; MANIFEST remains a distinct 13-entry operator-controlled roster.
- Structural SOURCES cleanliness is not whole-corpus semantic conformance. The existing gate separately leaves r1/r3/r5/r6/r9, verifier independence, and SHONEN truth unevaluated.
