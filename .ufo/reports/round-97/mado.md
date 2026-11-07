# mado — round 97 report (hyaku run 15, attempt 1)

Lane: mado. Round: 97. Agent: `MadoR97`. Base revision: `e6152b589c2c6a28426c28263c4bcc3c46398be4` (branch
`master`). Lane tip when this report was written: **`15b6280483fe8fab52acbce689c883c056b34e7d`** (`git ls-remote origin refs/heads/master` prints it).
Lane repo `mado-shokunin`; this report lands through `fleet-commit.sh --as mado`.

**Round shape.** Wave `w1` (one v1 wave, 14 seats: 3 executors, 2 mutation-testers, 2 reviewers, 1 critic, 1 scout,
1 connector, 1 scribe; attack 5/14 = 36 %) and wave `w1b` (one v1 wave, 10 seats: 5 executors, 2 mutation-testers,
2 reviewers, 1 critic; attack 5/10 = 50 %), the second dispatched after four w1 seats died on a provider 401
(`commandcode/stealth/crouton-alpha`, `401 Invalid Authorization`) and the corrected declaration needed fresh
falsifiers. Round total 24 seats; no residual call. Dead seats: w1 `R97MScoutSources`, `R97MExecC2`, `R97MMutC2` (settled
with no report; their items were carried by w1b) and four provider-401 deaths in w1 (`R97MExecCasesC1`,
`R97MExecToolC1`, `R97MExecC2`, `R97MExecCounterC2`; `R97MExecToolC1` landed on its second attempt and
`R97MExecCasesC1` wrote its report before dying, both superseded in w1b), replaced in w1b; w1b: no dead seats. The
401 deaths are provider-failure attempts, not quality rejections. Wave evidence:
`.ufo/waves/round-97/w1-spec.json`, `w1-dispatch.json`, `w1.ready`, `w1-results.json`, `w1b-spec.json`,
`w1b-dispatch.json`, `w1b.ready`, `w1b-results.json`, seat reports under `w1/` and `w1b/`. The L1 holds the
planner seat (a bounded data walk in `.ufo/waves/round-97/planning-data-walk-r97.md`).

## Work performed

The round declares two claims (declaration `.ufo/waves/round-97/claims-declaration-r97.md`, freeze `78e9ccdd`,
corrected before the freeze on the waves' measured findings — the `## Freeze` block lists every correction):

- **C1 — coverage (new surface, capability):** the content type GIO 2.90.1 reports for a **path**
  (`standard::content-type` / `standard::fast-content-type`) — delivered as `tools/mado-filetype.py`.
- **C2 — operability:** the two round-96 counters gain the Gate standard's self-invocation mode, and the registry
  rows for the three instruments close — delivered as `--selftest` on `quality/counters/c1-r96-magictext.py` and
  `quality/counters/c2-r96-selftest-kills.py`, scored by `quality/counters/c2-r97-counter-selftest.py`.

Work items with evidence:

- **C1 candidate** `tools/mado-filetype.py` (frozen `da6af7a0…8a44d2d8`, 606 lines): the two-stage stat (lstat, then
  a guarded follow), the eight-branch order (broken/nofollow symlink, directory, chardev, blockdev, FIFO, zero-size
  regular, socket), the alias rewrite, the basename-only guess with its three uncertain states, the sniff gate
  (`!fast && uncertain && path`), the sniff length from the database's own max extent clamped to 16384, the
  `O_NOATIME` open/read that keeps the name-only answer on failure, the `EACCES`-tolerant `lstat` and the
  loop/broken answer, path normalisation (`//`, `./`, `a/../b`, trailing slash), `--json`, and `--selftest`
  `checks=40 failed=0` (`38` from a lone copy) — `.ufo/waves/round-97/w1b/R97MExecToolC1b.md`.
- **Cases** `.ufo/waves/round-97/controls/filetype-cases-r97-frozen.json` (157 cases, 15 classes, ≥9 each; 196+
  path labels, every label produced by `/usr/bin/gio` on the built root; probe
  `controls/filetype-probe-v2.py` rebuilds the file byte-identically) — `w1b/R97MExecCasesC1b.md`.
- **Host inputs** `controls/filetype-host-r97-frozen.txt` (6,194 stable system paths) and
  `controls/host-labels-r97-frozen.json` (6,194 oracle labels, 0 ERROR, produced with `env -i LC_ALL=C
  /usr/bin/gio info -a standard::content-type`), `controls/host-db-r97.json` (the nine `/usr/share/mime` files),
  `controls/filetype-fresh-r97.py` (seeded generator, labels at measurement time) —
  `w1/R97MExecHostC1.md`, `receipts/host-labels-r97.txt`.
- **Mutants** `controls/filetype-mutants-r97-frozen.json` (101 counted, anchored to the tool pin, every class kills
  at least one) — `w1b/R97MMutC1b.md`.
- **C1 counter** `quality/counters/c1-r97-filetype.py` (`745a341e…195ba9e0`): pinned inputs, an audit-hook launcher
  with an empty `PATH`, the structural allowlist, the frozen host labels with a live-`gio` drift note, the fresh
  leg, the controls and the credential guard — `w1b/R97MExecCounterC1b.md`.
- **C2 counters** `quality/counters/c1-r96-magictext.py` (`4f678384…aaa64d`) and
  `quality/counters/c2-r96-selftest-kills.py` (`54143b8a…002217b`): a `--selftest` block appended after the
  production path (production text byte-identical; the block sits immediately before the `__main__` guard), ten
  `st-*` checks each, fixtures resolved from the counter's own path so the landed `quality/counters/` layout is
  green — `w1b/R97MExecC2b.md`.
- **C2 counter** `quality/counters/c2-r97-counter-selftest.py` (`abb17a01…06b879`) and the panel
  `controls/counter-selftest-panel-r97.json` (`87ba2f41…`, 9 neutralisations per counter, 6 broken rows, the echo
  stub) — `w1b/R97MExecCounterC2b.md`, `w1b/R97MMutC2b.md`.
- **Entry** `corpus/knowledge/gio-content-type-file-r97.md` (indexed; §11 carries the measured receipt cells), the
  two SOURCES rows, the README index/frontier rows, the SKILL registry rows and the PROVINCE refinement —
  `w1/drafts/*`, `w1/R97MScribeEntry.md`.
- **Frontier step:** `corpus/lessons/round-97.md` (M97-1…M97-6), `corpus/QUALITY.md` 168–169,
  `receipts/sources-open-r97.txt` (the two new rows opened with HTTP 200 and digests),
  `receipts/census-start-r97.txt` / `census-end-r97.txt` (rc 0 both ends).
- **Assimilation:** `Assimilation: none` — the round-96 id-collision check stands (`.ufo/waves/round-97/assimilation/`
  is empty this round because no staged entry touches the content-type caller plane; the package's entries were
  checked in round 96: reg-ids 458, staged-ids 147, collisions 94). considerthese: no still-unimplemented proposal
  matched this round's surface (the 2026-11-07 proposal 3 was mined in round 96).
- **Cross-domain evidence:** GLib's GIO local-file layer and its xdgmime port (GNOME/freedesktop); the `gio(1)` CLI
  as the installed surface; `file(1)`/libmagic is revenger's ground and is not this surface. R97MConnector swept all
  20 sibling `PROVINCE.md`s: no sibling claims GIO's `standard::content-type` or `gio info`; `update-mime-database`
  and `~/.local/share/mime` stay operator-owned (tsukuroi's hook ground) (`w1/R97MConnector.md`).
- **Misroot sweep:** two seat files had landed at the fleet root — `dropped-volatile.txt` (the host census's dropped
  paths; copied byte-exact, `cmp` clean) and `host-list-final.txt` (the seat's intermediate census, which is *not*
  byte-identical to the wave copy: `cmp` exits 1, corrected in the lesson). Both are copied into the lane, the fleet
  copies deleted, and mined as M97-7/M97-8.
- **Mistakes owned:** M97-1 (an admitted sentence contradicted by the round's own fixture — the r96 erratum class),
  M97-2 (the contract's refusal condition lacked the library's errno guard; two reachable path shapes were
  misclassified), M97-3 (the host census carried credential-shaped paths into a leg that reads host bytes), M97-4
  (a base count asserted without measuring: registry 0 vs 1), M97-5 (a receipt byte count published as measured),
  M97-6 (a frozen control panel named fixture files that do not exist under the instrument's fixture root) —
  `corpus/lessons/round-97.md`, QUALITY 168–169.

## Landed changes

Every change below is inside `mado-shokunin` and lands through `jj-lane.sh` (lane identity `mado-shokunin
<mado@shokunin.local>`); the LOG entry is `LOG.md` round 97.

| commit | what it carries |
|---|---|
| `78e9ccdd` | **claims freeze**: the declaration with its pins, the frozen C1 controls (157 cases, 101 mutants, 6,194 host labels, the forgery), the w1 spec/dispatch/ready and seat reports |
| `a1408d47` | **C1 landing**: `tools/mado-filetype.py`, `quality/counters/c1-r97-filetype.py`, the entry, SOURCES S526/S527 + used-by, the README index/frontier rows, the SKILL and PROVINCE rows, the ledger rows |
| `dc0daad9` | the C1 ledger pointer names a committed frozen path (the receipt lands with the records) |
| `4541d94b` | the three large C1 case files (w1 draft, v2, frozen), named explicitly because a directory commit skips new files over 1 MiB — **C1 measured here** |
| `65ff5591` | **C2 landing**: the two round-96 counters with `--selftest`, `quality/counters/c2-r97-counter-selftest.py`, the SKILL registry rows (r96 ×3 + the r97 counter) and the strength-row population; ledger row — **C2 measured here** |
| `1b9bad52` | measured receipts (C1, C2, run 1, the C2-at-C1 leg), the lesson, QUALITY 168–169, LOG and SCORECARD records, the corrected panel and the declaration's final pins, the w1/w1b reports and results |
| `e957932d` | the C1-at-C2 separability receipt and the mutant file's post-freeze metadata |
| `d421fd77` | the round-96 spot-check record fixes (D1/D2/D5/D6/D11: the used-by cells, the entry's stale measurement cells, the declaration's command pins and mutant population, the census receipt counts) |
| `4bfe2e43` | the harm watch (25 legs) and the declaration-counter runner fix |
| `992037c6` | the misroot sweep: the host seat's dropped-path list copied into the lane (M97-7) |
| `d7c186bc` | the second misroot sweep: the host census copy copied into the lane (M97-8) |
| `15b62804` | M97-8's correction: the fleet-root census copy is not byte-identical to the wave copy (`cmp` exits 1) |

## Before → after measurements

**C1 — coverage.** Counting command (the declaration's C1 block, every pin named; the full line is
`.ufo/waves/round-97/receipts/c1-measured-r97.txt` line 122):

```sh
python3 -I quality/counters/c1-r97-filetype.py --repo . --rev 4541d94b4797c872b55f3facf3996d54e63326a5 \
  --base-rev e6152b589c2c6a28426c28263c4bcc3c46398be4 \
  --cases .ufo/waves/round-97/controls/filetype-cases-r97-frozen.json --expect-cases-sha256 fc710b94df67391c392d95aeabd6dfa4c016081019d732f5c373fb990844be20 \
  --mutants .ufo/waves/round-97/controls/filetype-mutants-r97-frozen.json --expect-mutants-sha256 c6f156c380b42b9d1bb78e9eb3142f11cdca70cd0c504cdd8bae2edd3f8db120 \
  --genseed .ufo/waves/round-97/controls/filetype-fresh-r97.py --expect-genseed-sha256 c3143775d346921085a4f312eb596bc9b062abb11c3257aed47d9bba50bf7bf2 \
  --host-list .ufo/waves/round-97/controls/filetype-host-r97-frozen.txt --expect-host-list-sha256 943fd957f4fae5ce77ab2aff12ad473072a88055802afa03b634b290728c2a86 \
  --host-labels .ufo/waves/round-97/controls/host-labels-r97-frozen.json --expect-host-labels-sha256 f4ef8738b93a783c5358400f64de95da0ffc5558328772da19a5ac4a9a28ebea \
  --host-db .ufo/waves/round-97/controls/host-db-r97.json --expect-host-db-sha256 0c6c0c0c7f62353777053bb77b33bca4cb01a23d0e5ab81eaa5c8d9d00518562 \
  --expect-tool-sha256 da6af7a0789265187f6b2c2462bf5104a7c0b780baed3235300f89978a44d2d8 \
  --expect-mimeglob-sha256 65f80a6cb1551bb722ae7608df04fb17deba1b5cd05bef6f7fdd79bed76e2453 \
  --expect-mimesniff-sha256 4ef019c69ea8ae4147f83d1558683f012fb4aac0815d36770304717aaca6af24 \
  --expect-mimetext-sha256 d5f174fc33d0b1f1847897a8e63724c7112137c1bf58a89508d1c1c13b857cbd \
  --expect-gio-sha256 d216426080f847bfccdc7c735a4f349dc74f524530a19e8b1c32d04270cfc462 \
  --forgery .ufo/waves/round-97/controls/forgery-ctypes-r97.py --expect-forgery-sha256 7b1f1492445ec891fada7755ef103716d7cf89fc44ae655734c19e496ddf7cf9 \
  --scratch-root DIR
```

**Before:** at `e6152b58` no lane tool answers a path's content type (`git cat-file -e
e6152b58:tools/mado-filetype.py` absent; the r94–r96 tools answer inputs, not paths): 0 scored paths. **After:**
`TARGET_MET` at `4541d94b` — cases 157/157 (15/15 classes), mutants 101/101 (class_kills 15/15), fresh 140/140
(seed `4c1d3a48329c2167`), host 6194/6194 (0 mismatches, 0 errors, 0 drift), selftest `checks=40 failed=0`,
controls name-only 39/157, naive 67/157, memoriser 0/140 fresh, forgery rejected (`audit_denials=0` on the
candidate, 3 on the forgery), `credential_guard=0`. Receipt: `.ufo/waves/round-97/receipts/c1-measured-r97.txt`.
Separability: the same counter `TARGET_MET` at the C2 revision `65ff5591`
(`receipts/c1-at-c2-r97.txt`).

**C2 — operability.** Counting command:

```sh
python3 -I quality/counters/c2-r97-counter-selftest.py --repo . --rev 65ff5591c40c13ae7686b30587d202086353c165 \
  --base-rev e6152b589c2c6a28426c28263c4bcc3c46398be4 --expect-base-registry-sha256 6a8754df2d6d0123b77db384ac85bef17baa378e0be2782a01ba79e069ff028d \
  --panel .ufo/waves/round-97/controls/counter-selftest-panel-r97.json --expect-panel-sha256 87ba2f4149ff5fbcd7dfe7179bc87b1bd50cd083867f736b62f02796cfa9b4ba \
  --expect-c1-sha256 4f6783848ded9c63f934c68a24da856369895987651d0f66fdd6920f07aaa64d \
  --expect-c2-sha256 54143b8a28f2be4b2f1361c443d32156a68fd088c7cdb9c9030ca7415002217b \
  --expect-registry-sha256 fab1ff74944e9ecc3f9f4ef52e31e1af899ee9588a9c0a41ee29545ce3ce944e \
  --expect-ledger-sha256 fb0f2f3c818c81978fe35814697c44764a6b31796ea8baa0290406df7559d624 \
  --scratch-root DIR
```

**Before:** both counters refuse `--selftest` (argparse rc 2, no result line) and `SKILL.md` holds 1 of the 3
instrument rows. **After:** `TARGET_MET` at `65ff5591` — `selftest_green=2/2 checks=10,10`, `negative_ids=18/18`,
`broken_modes=6/6` (`broken_c1=3/3 broken_c2=3/3`), `base_refuse=ok`, `always_ok_flagged=0`,
`stub_uncredited=18/18`, `registry=1->3`, `ledger_members=2/2`, `ledger_uncovered_ok=True`. Receipt:
`.ufo/waves/round-97/receipts/c2-measured-r97.txt` (run 1, whose two `missing-input` rows declared exit 2 where the
mode measures exit 1, is kept as `receipts/c2-run1-r97.txt`; the predicate allows exit 1 or 2 and the panel's
declared exit was corrected before the final run — `receipts/panel-correction-r97.txt`). Separability: the C2
counter at the C1 revision `4541d94b` stops on `SKILL.md sha256 != --expect-registry-sha256` (the C2 landing is not
there; `receipts/c2-at-c1-r97.txt`).

## Sources & frontier

**SOURCES before → after:** 460 → 462 rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`;
start `receipts/census-start-r97.txt`, end `receipts/census-end-r97.txt`; both rc 0). Rows added by tier: A +2 —
S526 (`gcontenttype-fdo.c`'s `_g_unix_content_type_get_sniff_len` and the Unix content-type mapping) and S527 (the
installed `gio(1)` `info` contract), both opened this round with HTTP 200 and digests in
`receipts/sources-open-r97.txt`. Rows touched old → new: ten `used-by` cells (S505, S515, S516, S518, S519, S520,
S521, S522, S524, S525) gain `corpus/knowledge/gio-content-type-file-r97.md`; no anchor, digest, scope or status
cell moves. Frontier rows advanced: the content-type plane's **caller** (path → type) moves from frontier to core
(the README frontier bullet); launch stays frontier. Census conformance: rc 0 at both ends (the expected W04
duplicate-URL warnings are listed in the receipts). **Assimilation: none** (see Work performed).

## Trend verdicts

- **expansion — improved.** A new admitted entry (`corpus/knowledge/gio-content-type-file-r97.md`, index 117 → 118)
  on ground the coverage map did not hold (the path-level caller), citing two new tier-A rows (S526, S527) plus the
  held GLib rows; the capability row is entered with a demonstrated run (157/157, 101/101, 6194/6194). Rows were not
  padded: 460 → 462.
- **quality — improved.** C1's instrument supersedes "no lane tool answers a path" with a measured answer and four
  controls behind it (name-only 39/157, naive 67/157, memoriser 0/140, forgery rejected); C2 replaces "no
  self-invocation" with 10 checks per counter, 18/18 neutralisations flagged with their declared ids, 6/6 broken
  modes named and the base bytes refusing. The harm watch over every prior instrument is
  `receipts/harm-final-r97.txt`: 25 legs, 24 rc 0 and the declared `r90c1_portal_routing` SETUP_ERROR (its nine
  anchors were removed by the round-90 port; the expectation is declared since round 93), including the two
  round-96 counters replayed at the tip after their `--selftest` block was added.
- **discernment — improved.** Six mistakes are mined with a criterion each (M97-1…M97-6, QUALITY 168–169); the wave
  reversed four of the L1's own sentences before the freeze (the sniff extent, the `EACCES`/loop refusal boundary,
  the registry base count, the memoriser control), and the panel's setup error was caught by the counter's own
  SETUP check rather than by a green run.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the registry rows for the
  tool and both counters, the entry's tables and the PROVINCE refinement land this round; outside-lane independence
  is still not established (no `[x]` written).
- [~] At least one end-to-end domain task executed and logged in LOG.md — the C1 measured run (157 cases + host leg)
  is this round's end-to-end task; the LOG entry carries it.
- [~] Instructions executable by an agent without oral context — the entry's §5/§11 commands and the counter's CLI
  are pasteable; the wave's seats executed them without oral context, but a dispatched seat is still the lane.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — R97MConnector's 20-lane sweep found no sibling claim on
  this surface; PROVINCE.md carries the round-97 refinement; outside-lane approval is not in this round.

## Notes

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none this round (no `uv`/`npm`/binary installs; `/usr/bin/gio` and stdlib Python only).
- **L0 questions:** none opened this round. The omarchy-host freshness rubric stays dormant (r57 L0 open); the
  r96 spot-check's D1–D13 are closed by this round's record fixes (D1 used-by cells, D2 stale cells, D3/D4 registry
  and self-test, D5/D6 declaration corrections, D8/D11 receipt addenda, D10 newline, D12 mined as M97-1, D13 tied in
  this report's Landed-changes table).
- **Round-95 routed defects:** items 1, 2, 4 and 5 remain open and are re-flagged (tool docstring citations, the
  gate's own selftest kill-set predicate change, QUALITY 158's HTTP-status gap).
