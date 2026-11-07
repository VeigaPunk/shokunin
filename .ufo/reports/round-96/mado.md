# mado — round 96 report (hyaku run 15, attempt 1)

Lane: mado. Round: 96. Agent: MadoR96. Base revision: `9f029f46f01f6cd3a1d29ac39bb548498a1d0c3d`. Lane tip when this
report was written: **`c20f060d83f7dc595be58f15c5144dc805f1cd70`** (branch `master`, pushed; `git ls-remote origin
refs/heads/master` prints it). Lane repo `mado-shokunin`; this report lands through `fleet-commit.sh --as mado`.

**Round shape.** One v1 wave (`w1`) of 14 seats — 4 executors, 2 mutation-testers, 2 reviewers, 1 critic, 1 scout,
1 connector, 1 scribe (attack share 5/14 = 36 %); the L1 holds the planner seat; no residual call. Round total 14.
All 14 seats settled (`.ufo/waves/round-96/w1-results.json`, one entry per seat, every report present); **dead
seats: none**. Wave spec/dispatch/registry: `.ufo/waves/round-96/w1-spec.json`, `w1-dispatch.json`, `w1/swarm-registry.json`.

## Work performed

The round declares two claims (declaration `.ufo/waves/round-96/claims-declaration-r96.md`, freeze `b056290d`,
w1 findings folded in before the freeze and listed in its `## Freeze` block):

- **C1 — coverage (new surface, capability):** what GLib 2.90.1 `g_content_type_guess` answers when the reachable
  MIME directories hold the **text** database (`mime/magic`, no loadable `mime.cache`) — delivered as
  `tools/mado-mimetext.py`, the one named frontier of the round-95 entry.
- **C2 — operability:** the last gate-compatible tool (`quality/check-receipt-presence.py`) becomes guardable (six
  distinct selftest labels, the selftest block after `main()`) and is guarded by a kill-set under the unchanged
  round-93 selftest-strength gate — the round-95 spot-check's routed defect 3.

Work items with evidence:

- **C1 candidate** `tools/mado-mimetext.py` (frozen `d5f174fc…b857cbd`): the `MIME-Magic\0\n` gate, `[priority:type]`
  sections, length-prefixed matchlets with `&mask`/`~word` (0/1/2/4)/`+range`, the state machine's whole-section drop
  (and the extra-line eat of the word-length error), chapter-and-verse of the indent tree, priority order with
  file-order ties, the text fallback and the guess combination with round 94's name step — `--selftest` 50 checks,
  measured at 284/284 frozen cases (16/16 classes), 268–283 fresh inputs per seed, 9822/9822 host pairs over the
  round-95 4911-file list against the host's own cache-free text database, 84/84 counted mutants with class_kills
  16/16 (`.ufo/waves/round-96/receipts/c1-measured-r96.txt`).
- **Cases and oracle labelling** (`.ufo/waves/round-96/controls/magictext-cases-r96-frozen.json`, 284 cases / 423
  inputs / 16 classes; probe `magictext-probe-r96.py`): every label from the compiled GLib oracle; five declared
  cache-refusal cases hold **loadable** caches; the `mode-06` junk cache is text mode and oracle-labelled.
- **Mutants** (`.ufo/waves/round-96/controls/magictext-mutants-r96-frozen.json`, 84 counted + 13 not-observable with
  arguments + 13 equivalents): anchored one-by-one to the frozen candidate bytes (R96MMutC1), every kill a parsed
  wrong answer, no kill a crash.
- **Counter** `quality/counters/c1-r96-magictext.py` (`9d3e1e76…a7f7`): empty `PATH`, an audit-hook launcher, the
  structural allowlist, a sha-pinned tool and sibling, the host-DB manifest verified file by file, and the controls
  (`c1-measured-r96.txt`).
- **C2 tool and kill-set** (`quality/check-receipt-presence.py` `be716a63…c962`;
  `quality/selftest-kills/check-receipt-presence.json` `305d735f…a495`): six labels with label-only FAIL lines, the
  selftest block after `main()` (production text byte-identical after removal of the block), seven kills with exact
  list-form `must_fail` sets, six singleton labels.
- **C2 counter** `quality/counters/c2-r96-selftest-kills.py` (`2bd9e562…eb895`): the gate and kill-set pins, the six
  neutralisations, the 31 hand weakenings + 6 neutral edits, the do-nothing/always-OK/always-WEAK controls, the
  first-draft kill-set control and the round-90 main-path leg (`receipts/c2-measured-r96.txt`).
- **Entry** `corpus/knowledge/mime-textdb-magic-r96.md` (indexed, `corpus/README.md` row + frontier line), the two
  SOURCES rows, the SKILL registry row and the PROVINCE refinement (`SKILL.md`, `PROVINCE.md`).
- **Frontier step:** `corpus/lessons/round-96.md` (M96-1 the 63-hex oracle pin, M96-2 the `mime.cache` proxy read as
  cache mode), `corpus/QUALITY.md` 166–167, `receipts/sources-open-r96.txt` + `sources-verify-r96.txt`, census
  `receipts/census-start-r96.txt` / end (in LOG).
- **Assimilation:** `Assimilation: none` — the id-collision check (`.ufo/waves/round-96/assimilation/`: reg-ids 458,
  staged-ids 147, collisions 94) found no staged entry on the MIME plane; considerthese 2026-11-07 proposal 3 (an
  exhaustive small-domain sweep) is the mined proposal, implemented as the oracle-labelled case set.
- **Cross-domain evidence:** GLib `xdgmime`/`gcontenttype-fdo`/`gio` (GNOME), the shared-mime-info format
  (freedesktop.org), and `file(1)`/libmagic (revenger owns its rule grammar; this tool never reads it). R96MConnector
  swept every sibling `PROVINCE.md`: no sibling claims the text MIME database; `update-mime-database` and
  `~/.local/share/mime` stay operator-owned (tsukuroi's hook ground).
- **Mistakes owned:** M96-1 (a 63-character oracle digest in the declaration, caught by the scribe and the host seat)
  and M96-2 (five refusal labels fabricated from a coarser proxy, caught by the critic, the tools seat and my own
  scorer) — both fixed before the freeze, both with a QUALITY criterion.

## Landed changes

Every change below is inside `mado-shokunin` and lands through `jj-lane.sh` (lane identity `mado-shokunin
<mado@shokunin.local>`); the LOG entry is `LOG.md` round 96.

| commit | what it carries |
|---|---|
| `09db97c3` | w1 spec, dispatch and the declaration draft (wave evidence) |
| `b056290d` | **claims freeze**: the pinned declaration, the w1 seat reports, the frozen inputs (cases, mutants, panel, host-DB manifest, r90 argv, forgery), the build drafts, the harm harness |
| `5dd921b3` | **C1 landing** (`tools/mado-mimetext.py`, `quality/counters/c1-r96-magictext.py`, the entry, SOURCES S524/S525 + used-by, the README index/frontier rows, SKILL and PROVINCE rows, ledger rows) |
| `f54def27` | **C2 landing** (`quality/check-receipt-presence.py`, `quality/selftest-kills/check-receipt-presence.json`, `quality/counters/c2-r96-selftest-kills.py`, ledger row) |
| `8a0aadb0` | measured receipts, the lesson, QUALITY 166–167, `LOG.md` and `SCORECARD.md` records, the harm-harness fix |

## Before → after measurements

**C1 — coverage.** Counting command (frozen declaration, every argument named; the `--expect-*` values are the freeze
block's pins):

```sh
python3 -I quality/counters/c1-r96-magictext.py --repo . --rev 5dd921b3d659585b1ca30611445098d8debced84 \
  --base-rev 9f029f46f01f6cd3a1d29ac39bb548498a1d0c3d \
  --cases .ufo/waves/round-96/controls/magictext-cases-r96-frozen.json --expect-cases-sha256 4b3645ae83f6bb1822ebdacd4e42c2dc0fdd152bdca8fc4ff558985052f1d565 \
  --mutants .ufo/waves/round-96/controls/magictext-mutants-r96-frozen.json --expect-mutants-sha256 448150e2be7650309d126670413ea0a2d8c11c8c257807014418cf28ac1bc440 \
  --oracle-src .ufo/waves/round-95/controls/mimesniff-oracle-r95.c --expect-oracle-sha256 99df35f8b3fd7005f30789f8866984a1bbceaff8dc6c1d326f0132eb7b4d124a \
  --fresh-gen .ufo/waves/round-96/controls/magictext-fresh-r96.py --expect-fresh-gen-sha256 32d38edfb2cff57de3d89297ffaf1bd781d730b7be502fbfa62efa38de0815da \
  --host-list .ufo/waves/round-95/controls/mimesniff-host-files-r95.txt --expect-host-list-sha256 9d5947a70d112796f39c3e309c5a25e5ff333b5ebeb51867ebe748af1135ba87 \
  --host-db .ufo/waves/round-96/controls/host-text-db-r96.json --expect-host-db-sha256 9c411d2af41ac283fb7d229152f0b7b28b7854eabd057135a225762389d1ddd7 \
  --expect-tool-sha256 d5f174fc33d0b1f1847897a8e63724c7112137c1bf58a89508d1c1c13b857cbd --expect-mimeglob-sha256 65f80a6cb1551bb722ae7608df04fb17deba1b5cd05bef6f7fdd79bed76e2453 \
  --forgery .ufo/waves/round-96/controls/forgery-ctypes-r96.py --expect-forgery-sha256 06800cd141a18548c63701a44f9cab70e2c90f0f316fb6f24d0c06fca079fd97 \
  --scratch-root DIR
```

**Before:** at `9f029f46` no lane tool answers the text database (`git cat-file -e 9f029f46:tools/mado-mimetext.py`
absent; the round-95 tool refuses text mode: 0 scored inputs). **After:** `TARGET_MET` at `5dd921b3` — cases 284/284,
classes 16/16, fresh 268/268 (seed printed; 273–319 across seeds), host 9822/9822 (4911 paths × 2 legs), mutants
84 killed / 84 with class_kills 16/16, `checks=50 failed=0`, static ok, audit_denials 0; controls do-nothing 0/259
text-mode (20/20 none-mode answered), name-only 32/284, naive 101/284, memoriser fresh 0/40, ctypes-libgio forgery
rejected. Receipt: `.ufo/waves/round-96/receipts/c1-measured-r96.txt`. Separability: the same counter
`TARGET_MET` at the C2 revision `f54def27` (`receipts/c1-at-c2-r96.txt`).

**C2 — operability.** Counting command:

```sh
python3 -I quality/counters/c2-r96-selftest-kills.py --repo . --rev f54def272d0f9426820a17f226babbd655455f2e \
  --panel .ufo/waves/round-96/controls/selftest-panel-r96-frozen.json --expect-panel-sha256 4332b488309309b81eccccabaff9322c5b7a54fcedd74079b58f50926f773982 \
  --expect-gate-sha256 2d6f1219fae19a85cc92f7d4103db396e1306fea74c2226bb068b335598da61b \
  --expect-kills-sha256 305d735fd665ad87566c7983f4e9163eaf323ad1ddb7a99a907e507c8a617495 \
  --control-kills .ufo/waves/round-96/build/check-receipt-presence-draft.kills.json --expect-control-sha256 0c233a47b9d0b855ed92991079399c1e6cf32848d4016081057c569ea3aed0c7 \
  --r90-argv .ufo/waves/round-96/controls/r90-c2-argv-r96.json --expect-r90-argv-sha256 386a5a18f77bf6fa564f2a11498ef21f5c1e7ef461028a2956050d3af52ecda0 \
  --scratch-root DIR
```

**Before:** no kill-set exists at base and no instrument sees a weakened assertion for this tool (0/31, 0/6, 0/6).
**After:** `TARGET_MET` at `f54def27` — labels 6/6, `labels_covered 6/6`, `singleton_labels 6/6`,
`neutralised_flagged 6/6`, `hand_flagged 31/31`, `neutral_ok 6/6`, `do_nothing_flagged 0`, `always_ok_flagged 0`,
`always_weak_positive WEAK:1`, `gate_selftest ok`, `control_hand_flagged 19/31`, round-90 leg `TARGET_MET 83/83`
(killed 28/28) with `tool_pin=ok` at the changed bytes. Receipt: `.ufo/waves/round-96/receipts/c2-measured-r96.txt`.
Separability: the same counter at the C1 revision `5dd921b3` is `SETUP_ERROR … kill-set path … absent`
(`receipts/c2-at-c1-r96.txt`).

**Harm watch** at the final tip: `.ufo/waves/round-96/receipts/harm-final-r96.txt` — 22 legs: 21 rc 0 (gate selftest 460/460, file plane CLEAN 29, index 117/117, ledger 188/188, every tool selftest green, the four gate kill-set legs OK, r90 C2 83/83, r92 C2 45/45, r94 C1/C2 and r93 C2 TARGET_MET) and `r90c1_portal_routing` rc 2, its declared expectation since round 93; harness exit rc 0; the round-96 legs are the separate c1/c2/c1-at-c2 receipts. No axis harmed..

## Sources & frontier

- **Census before → after.** `sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado` at round start:
  `mado ok`, rc 0, 458 rows (`receipts/census-start-r96.txt`). At round end (receipt in the LOG/D commit):
  `mado ok`, rc 0, 460 rows (S524 and S525 added tier A; the W04 for S525's duplicate URL is the expected warning), receipt `.ufo/waves/round-96/receipts/census-end-r96.txt`..
- **Rows added by tier:** 2 tier-A rows — **S524** (GLib 2.90.1 `xdgmimemagic.c`, the text magic parser and matcher,
  `fcb1eafe…ce742`, HTTP 200 twice) and **S525** (shared-mime-info spec §2.5 "The magic files", the locator S523
  holds, `e00fa00e…c61e`, HTTP 200 twice; the expected W04 duplicate-url warning). Both opened by the L1 on
  2026-11-07; located quotes in the lesson's Gate table and in `receipts/sources-open-r96.txt`.
- **Rows touched (old → new):** `used-by` only, appended with `corpus/knowledge/mime-textdb-magic-r96.md` on S505,
  S519, S520, S521, S522, S523; no anchor, digest or scope cell of a held row moved (registry draft §2). The held
  S505 and S523 digests were re-fetched and re-derived byte-identically this round (`sources-open-r96.txt`).
- **Frontier rows advanced:** `corpus/README.md` gains the r96 frontier line (text-database half of the
  content-type plane) and the index row for the entry; the round-95 entry's "text `magic` files" limit is closed.
- **Frontier-step duties:** the census before/after, one mined mistake (M96-1; M96-2 is a second, from the wave's
  own attack) and a sourced claim (C1 cites S524/S525/S505/S520/S521/S522/S523). `Assimilation: none` (94
  staged-id collisions, none on this plane; `.ufo/waves/round-96/assimilation/`).

## Trend verdicts

- **expansion — improved.** A surface the coverage map did not hold (the text MIME database's magic step) moves into
  core with an admitted entry (index 117/117), two tier-A rows and a capability row demonstrated at 284/284, 268/268
  fresh and 9822/9822 host pairs.
- **quality — improved.** C1: 284/284 + 84/84 mutants (class_kills 16/16) + 9822/9822 host pairs + the four controls
  (do-nothing, naive, memoriser, forgery) all behind the target; C2: 31/31 hand weakenings, 6/6 neutralisations, 6/6
  singletons under the unchanged gate, with the round-90 leg green; a green harm watch over every prior round's
  counters.
- **discernment — improved.** The wave's attackers reversed two of the L1's own sentences (the `mime.cache` proxy →
  five mislabelled cases; the word-size set and the indent rule) *before* the freeze, and the round mines both as
  criteria; the mutant population's 13 unobservable entries are named with the fixture that kills each rather than
  silently dropped.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — asserted: the tool registry
  row (verdict map + self-test + pin path) and the PROVINCE refinement landed this round; no non-author `[x]` verifier
  this round (the freeze draft was checked by the wave's critic/reviewer seats, which are the lane).
- [~] At least one end-to-end domain task executed and logged in LOG.md — asserted: the r96 entry's §5/§7 run the tool
  end-to-end and the C1 receipt is the executed measurement (`receipts/c1-measured-r96.txt`); no outside-lane
  verification this round.
- [~] Instructions executable by an agent without oral context — asserted: the entry §5 carries the exact commands, the
  tool row the verdict map; the outside-lane executor test remains the historical round-3 record.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — asserted: R96MConnector's sibling sweep found no conflicting
  claim (revenger owns `file(1)`/libmagic; this tool reads the GLib text database only) and PROVINCE carries the r96
  refinement; not a fresh outside-lane approval.

## Extras

- **Stale-lane:** no — this round ran under the respawn-per-round driver, terminated with a landed report, and no
  other mission of this lane is open.
- **Tool installs:** none (no `uv`/`npx`/binary install; pacman stayed paused). `cc`/`pkg-config` from the host were
  used to compile the frozen oracle.
- **Open L0 questions:** none added this round; no operator decision was needed.
- **Named defects routed to round 97:** the tool docstring's three line citations (fixing them changes the frozen tool
  bytes and re-anchors every mutant), ten case gaps named in the declaration's `not_observable_not_counted`, and the
  three structurally unguardable tools (mako/mimesniff/mado-verify.sh) that need a gate predicate change carrying the
  rounds 93/94/95 counters re-anchored (QUALITY 153/155).
