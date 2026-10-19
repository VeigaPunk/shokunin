# Kaidoku r13 source-curation critic review

**Comparison:** `kaidoku-shokunin` r13 `5ac7860730e7be7156b1a71f590d50261fb14e63` vs r12 `1170f71`.

## Strongest actionable counterexample

**The new curation capability is evidenced, but the Scorecard mislabels it as an expansion-trend improvement.** Fleet Contract v1 defines expansion as admitted `corpus/knowledge/` entries that cite a mined source row on uncovered coverage-map ground (`fleet-ledger/CORPUS.md:123-125`). The r13 lesson explicitly says there was no new knowledge entry (`corpus/lessons/round-13.md:18,56`), and the scorecard says its uncovered-ground knowledge-entry submeasure is unchanged, yet declares “expansion **improved** by entry of the separately recorded capability” (`SCORECARD.md:2151-55`). A new source registry/capability is valuable curation, but it is not the contract's expansion unit.

**Smallest safe correction:** keep the separately recorded “curated source registry” capability and all numeric axis values unchanged; append a correction recording expansion as **unchanged** for this round. Do not recast the 22-row count as knowledge growth. Parent adjudication remains open.

**Impacted axis/trend:** learning trend **expansion only**. The scorecard's owned coverage, depth, and calibration axes are explicitly unchanged (`SCORECARD.md:2144-46`); no numeric axis increase was found.

## Evidence and bounded sweeps

- The curation record is more than a bare count: `corpus/SOURCES.md` has scoped tiers/anchors, four ordered study paths, a bounded search log, distinct unopened leads, and a rejection with a flip condition. All 22 `used-by` links point to `corpus/lessons/round-13.md`; the lesson contains the corresponding row IDs, source locations, and excerpts. This use-by is a lesson, not an admitted knowledge entry, consistent with the contract's allowed `knowledge entries or lessons` paths. The SOURCES validator found no missing used-by paths.
- **Independent source/taste sample:** reopened S003's installed Ghidra Base source archive. Its SHA-256 equals the row's pinned digest (`f00d29c20119562eca7efd2740e8c67257ebd63ea24a3dfbc4dbbb9187a8d804`); `GoRttiMapper.java:79` exactly says `SUPPORTED_VERSIONS = GoVerRange.parse("1.15-1.25");`, matching the Gate quote and its scoped A tier. `GoApiSnapshot.java:get` returns `EMPTY` when its snapshot provider is absent, supporting the row's additional anchor. Reopened S008's arXiv v1 page: title/authors and the quoted abstract clause match. Reopened rejected S022's page: it explicitly requires browser upload and states Electron 17–38 coverage; the row's rejection against this lane's Electron 42/V8 14.8 `.jsc` work and local-custody preference is source-grounded and has a concrete, sensible flip condition. This is a small sample, not re-verification of every row.
- Frontier honesty: the unopened-leads section distinguishes unopened later GoReSym releases, later Ghidra release notes, and a version-matched Electron 42/V8 14.8 route from the pinned sources actually opened (`SOURCES.md:44-50`). The selected rows do not claim those gaps are closed.
- Preservation: `git diff --unified=0 1170f71 5ac7860730e7be7156b1a71f590d50261fb14e63 -- corpus/lessons/round-12.md corpus/README.md corpus/knowledge` returned no changes. The whole revision diff adds `SOURCES.md` and `round-13.md`, and appends to LOG/SCORECARD plus the stated SKILL/QUALITY pointers; it does not alter prior knowledge entries or the README coverage map.
- Privacy/provenance: a credential-indicator scan over `SOURCES.md` and `round-13.md` matched only the product name `1Password`; no `op://`, URL userinfo, or credential assignment was observed. Local documentation paths and canonical public URLs are recorded; the row's opened date and anchors are present.

## Actual checks / limits

Commands run (all with explicit absolute paths):

```sh
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kaidoku-shokunin /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kaidoku-shokunin
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --today 2026-10-19 --root /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kaidoku-shokunin /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kaidoku-shokunin
git -C /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kaidoku-shokunin diff --stat 1170f71 5ac7860730e7be7156b1a71f590d50261fb14e63
git -C /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kaidoku-shokunin diff --name-status 1170f71 5ac7860730e7be7156b1a71f590d50261fb14e63 -- corpus/knowledge corpus/SOURCES.md corpus/lessons/round-12.md corpus/lessons/round-13.md corpus/README.md SKILL.md corpus/QUALITY.md SCORECARD.md
sha256sum /home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC/Ghidra/Features/Base/lib/Base-src.zip
```

Observed census: 22 rows; A/B/C = 20/1/1; mined/rejected = 21/1; invalid and missing = 0. Validator: `ok`. Archive digest matched. No build/lint/test, target binary analysis, live REA session, repo edit, or commit was performed. Not all 22 external/local sources were independently reopened; the source-quality assessment is bounded to the named sample and static registry/lesson inspection.
