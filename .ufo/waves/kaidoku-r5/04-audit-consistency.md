# kaidoku-r5 · 04-audit-consistency — internal coherence audit of kaidoku-shokunin @ f507327

Lane: round-5 consistency audit (Devin host). Scope: the lane repo
`/home/vgpnk/Projects/shokunin/kaidoku-shokunin` plus its upstream references
(parent `MANIFEST.json`, `.ufo/reports/round-4/kaidoku.md`, `~/.bashrc`).
Method: mechanical cross-reference (programmatic set-diff of filenames vs table
refs), `find` recount, errata spot-checks against surviving original text,
git status/log. All commands re-run this round.

## Check 1 — r4*/r4u* knowledge files ↔ README knowledge table ↔ PROVINCE

**DRIFT** (README table complete; PROVINCE has stale/uncited surfaces).

- README `## Knowledge` table ↔ filesystem: **56/56 both directions**. Every one
  of the 18 round-4 files (`r4-05`…`r4-16`, `r4u-01`…`r4u-06`) has a table row
  (`corpus/README.md:76-93`) and every backticked `2026-10-13-*` ref in the
  table resolves to an existing file. Zero orphans, zero dangling refs.
  (The only dangling-looking tokens, `2026-10-13-round-1..4` in the Lessons
  table at `corpus/README.md:99-102`, resolve to `corpus/lessons/*.md` — all
  four exist.)
- PROVINCE: no dangling `2026-10-13-*` refs; shorthand `rN(-u)-NN` citations all
  resolve. **But five held r4 surfaces are uncited where PROVINCE describes
  them:**
  - `PROVINCE.md:159-160` — "**Signal/1Password-scale asar analysis** …
    signal's 38.5MB asar lane **in flight**" — STALE: the lane landed and is
    held (`corpus/knowledge/2026-10-13-r4-05-signal-asar.md`; README:86;
    LOG.md:85-96). Contradicts the file's own Core row.
  - `PROVINCE.md:144-152` — ">90 MB PE scale wall" frontier bullet restates
    r4-12's measurement (~900s, GhidraClient.js:607) without citing `r4-12`.
  - `PROVINCE.md:46` — Cross-version compare row cites r4-09 but never mentions
    r4-10's real-version pair / Go-symbol-hazard finding (README:87).
  - `r4-14-libsignal` and `r4-16-frontier-rescan` are cited nowhere in
    PROVINCE (r4-16 is cited at README:114).
- **PROVINCE "## Frontier" is internally self-contradicting** — six bullets at
  `PROVINCE.md:70-97` still describe pre-round-4 "not yet held" state while the
  same file's "### Round-4 additions to Core" (`:128-140`) holds each one:
  - `:70-73` managed AnyCPU "rejected… no SDK/ilspycmd/Mono" vs `:135` held
    (r4-11, r4u-04).
  - `:74-78` firmware "requires REA_BINWALK_COMMAND… no fallback path" vs `:132`
    held (r4u-01/03).
  - `:82-84` `inspect-binary-layout` "still gated… not persisted" vs `:54` and
    `:138` held (r4-13, persistent `~/.local/share/kaidoku-pwnenv`).
  - `:87-89` Android "need REA_JADX_MCP_JAR + REA_APKTOOL_COMMAND — both absent"
    vs `:134` held (r4u-02).
  - `:90-93` runtime-obs "unexercised: observe-web-session…" vs `:137` held
    (r4-08; only `capture-electron-scenario` still refused).
  - `:94-97` cross-version "unexercised: compare_javascript_export_shapes" vs
    `:46` held (r4-09).
- Minor: `corpus/knowledge/2026-10-13-asar-surface.md:78` Summary still states
  "Six ASARs" as the host population (typora×3 missed by the r1 sweep). The
  under-count correction exists only inside `r3-typora-signal.md`'s errata —
  no erratum ever landed on asar-surface.md itself, and `README.md:48`'s row
  still advertises "6 asar archives".

## Check 2 — coverage-map table vs `ls corpus/knowledge/`

**DRIFT.** Coverage map (`README.md:13-32`) references 44 unique files; the
directory holds 56. All 44 cited files exist (no dangling). The 12 files absent
from every coverage-map row are all round-4-era:
`r4-07, r4-08, r4-09, r4-10, r4-12, r4-13, r4-14, r4-15, r4-16, r4u-02,
r4u-05, r4u-06`. Six r4/r4u files did make the map (`r4-05`, `r4-06` at :21;
`r4-11`, `r4u-04` at :23; `r4u-01`, `r4u-03` at :32), so the map was partially
updated then abandoned mid-integration. The `## Knowledge` table itself is
complete (see Check 1) — the drift is confined to the coverage map.

## Check 3 — PROVINCE asar-archive count vs `find /usr /opt -name '*.asar'`

**CONFIRMED.** `find` yields exactly 9 archives, matching `PROVINCE.md:43`'s
enumeration one-for-one:

```
/usr/lib/obsidian/app.asar          } obsidian ×2 ✓
/usr/lib/obsidian/obsidian.asar     }
/usr/lib/signal-desktop/resources/app.asar        signal ✓
/opt/1Password/resources/app.asar                 1Password ✓
/usr/lib/electron39/resources/default_app.asar    } electron stubs ×2 ✓
/usr/lib/electron43/resources/default_app.asar    }
/usr/share/typora/resources/{app,lib,node_modules}.asar   typora ×3 ✓
```

## Check 4 — r4 + r5 errata blocks exist and cite the right original claims

**CONFIRMED** (all blocks present; 4 spot-checked against surviving text; one
erratum's premise is imprecise — noted, not a break).

Blocks present: `## Errata (round 4)` on 10 files — managed-assemblies:53,
r2-crash-inspect-probe:68, r2-evidence-bundle-schema:242, r3-evm-interface:149,
r3-renderer-asar:109, r3-appimage:91, r3-keyed-archive-carriers:150,
r3-mcp-session:150, r3-verb-coverage:226, r3-typora-signal:81 — matching
LOG.md:50-56's "ten errata" list one-for-one. `## Errata (round 5 audit)` on
r4-06:325, r4-07:212, r4-08:285 (4 bullets total).

Spot-checks:
1. `r3-typora-signal.md:84` (99.38% correction) — original claim at `:17`
   literally reads "388,080 B — **99.42%** of archive bytes". Correct cite. ✓
2. `r3-appimage.md:91-95` (envelope precision) — original verify row `:31`
   records "FAIL `invalid_format`" for bad read-bytes grammar; erratum refines
   to `invalid_request`/`invalid_input` code + `invalid_format` field reason.
   Correct cite. ✓
3. `r2-crash-inspect-probe.md:74-77` (`zstd -d` unnecessary) — original `:29`
   documents "`zstd -d`/`coredumpctl dump` is therefore the caller's job";
   erratum correctly clarifies dump output is already raw ELF. Correct cite. ✓
   (Its sibling bullet at `:70-73` claims "the entry's error-code wording
   conflated the two envelopes" — the file already records
   `invalid_request`/`out_of_range` correctly at `:22-23`; the premise is
   imprecise, likely targeting the same top-level-vs-field shorthand as the
   appimage fix. Substance still lands.)
4. `r4-07-jsc-bytecode.md:212-216` (nondeterminism) — original pins
   "530,020 B / 116 function blocks" at `:128-129`,`:191`; erratum records the
   re-run 531,851/115. Correct cite. ✓

## Check 5 — LOG.md, SHONEN.md, QUALITY.md, SKILL.md

**DRIFT** (minor): two stale surfaces in SKILL, two count slips in LOG/report.

- LOG.md: round-4 entry `:46-83` and follow-up entry `:85-105` both present and
  consistent with the commits (`999ce12` integration, `f507327` follow-up).
  Minor: `:104` says "**five** minor errata appended" but the parenthetical
  lists four items and exactly four r5 errata bullets exist
  (r4-06×1, r4-07×2, r4-08×1).
- SHONEN.md: checklist body (`:7-14`) is byte-identical to the canonical seed
  in `PROTOCOL.md` ("The canonical `SHONEN.md` seed" — confirmed at
  `~/Projects/kimi-shokunin/skills/shokunin/protocol/PROTOCOL.md:419-428` and
  `~/Projects/myskills/shokunin/protocol/PROTOCOL.md:415-424`, both identical)
  modulo `kaidoku` = repo name and the four allowed `[ ]→[x]` marks. Caveats:
  the header comment's "lines 386-393" citation is stale (seed now sits at
  ~419+ upstream), and `[x]` boxes carry no indented verifier-id/evidence line
  the canonical mark spec describes.
- QUALITY.md (`corpus/QUALITY.md`): admission criteria numbered 1-14
  sequentially, no dupes; #10 declares "sharpens 8" in its supersedes column;
  weak signals 1-6 sequential. ✓
- SKILL.md decision table (`:40-62`): every row claims a surface that is held
  or explicitly measured — verified against the knowledge entries. One stale
  recipe: `:48` still prescribes `coredumpctl dump` + `zstd -d`, contradicting
  the landed r4 erratum (dump emits decompressed ELF; PROVINCE.md:54 has the
  correction). All `held` statuses are backed by entries; only IDA/Hopper/JEB
  marked `frontier` — correct.
- `SKILL.md:69` uses `REA_APKTOOL_COMMAND` — the *correct* key name (see
  Check 8); PROVINCE is the side that drifted.

## Check 6 — MANIFEST.json round-4 entry vs `.ufo/reports/round-4/kaidoku.md`

**CONFIRMED** (verdict fields match; two cosmetic count slips inside the
report itself).

- Verdicts: MANIFEST `expansion:"improved"`, `quality:"improved"`,
  `discernment:"verified (r3 audit: all upheld, 10 errata applied)"` — matches
  the report's "Expansion — improved", "Quality — improved", "Discernment —
  verified by audit … 10 errata". Commit `kaidoku-shokunin@999ce12` correct for
  integration; `f507327` follow-up is consistent with MANIFEST's "2 lanes
  pending follow-up" note.
- Numeric slips (report-internal, inherited by MANIFEST): report claims
  "11 r4 + 6 r4u knowledge entries" / MANIFEST "17 new entries" — commit
  `999ce12` added exactly 10 r4-* + 6 r4u-* knowledge files (16; r4-05/r4-10
  landed in `f507327`). Off by one, or counting `corpus/lessons/round-4`.
  Report also says "All **six** operator-gated surfaces unlocked" then lists
  seven names (binwalk, unblob, jadx-mcp, apktool, pwntools, adb, wakaru);
  MANIFEST repeats the 6-with-7-list pattern.

## Check 7 — git state

**CONFIRMED** for the lane repo: `git status --porcelain` empty, HEAD
`f507327`, seven commits, no uncommitted drift, no stray untracked files.
Parent repo `/home/vgpnk/Projects/shokunin` carries expected wave-staging
state only: `M .ufo/waves/kaidoku-r4/14-libsignal.md` (lane's own staging file
updated with the third timed run — content is staging evidence), untracked
`.ufo/waves/kaidoku-r4/{05-signal-asar,10-real-version-pair}.md` and
`.ufo/waves/kaidoku-r5/`. Nothing outside wave staging.

## Check 8 — `.bashrc` provider env keys vs PROVINCE claims

**DRIFT** — one documented key name is wrong (documentation bug; the host
config itself is correct).

| PROVINCE claim | .bashrc | resolves? |
|---|---|---|
| `REA_BINWALK_COMMAND` (:19) | `:59` → `/usr/bin/binwalk` | ✓ regular file |
| `REA_UNBLOB_COMMAND` | `:60` → `~/.local/bin/unblob` | ✓ symlink→uv tool |
| `REA_JADX_MCP_JAR` | `:64` → `~/.local/opt/jadx-headless-mcp/jadx-headless-mcp-0.7.1-all.jar` | ✓ 42.6 MB jar |
| `REA_ADB_PATH` | `:62` → `/usr/bin/adb` | ✓ executable |
| `REA_PWNTOOLS_PYTHON` | `:58` → `~/.local/share/kaidoku-pwnenv/bin/python` | ✓ symlink→cpython-3.11 |
| `REA_WAKARU_COMMAND` | `:63` dynamic `find` under `$(npm root -g)/wakaru/…@wakaru/cli-linux-x64` | ✓ resolves to the ELF (matches PROVINCE's "fix applied .bashrc:63" exactly) |
| `REA_APKTOOL_JAR` (:20, :134) | **absent** — no export in `.bashrc`/`.profile` | ✗ |

Ground truth: REA 6.4.0 consumes `REA_APKTOOL_COMMAND`
(`~/.npm/_npx/9b9809298fe40d2c/node_modules/rea-agents/dist/apktool/ApktoolConfiguration.js:5`
`APKTOOL_COMMAND_ENV = "REA_APKTOOL_COMMAND"`), and `.bashrc:61` +
`.profile:10` do export `REA_APKTOOL_COMMAND=/usr/bin/apktool` (file exists).
So the working config is right; `PROVINCE.md:20` and `:134` document a
nonexistent variable name. (`PROVINCE.md:89` and `SKILL.md:69` spell it
correctly — PROVINCE is self-inconsistent.) Supporting claims verified:
`JAVA_HOME` at `.bashrc:24`/`.profile:4` as `:41` states;
`REA_IDA_MCP_CONFIG`/`HOPPER_LAUNCHER_PATH` unset as `:22-23` states.

## Verdict summary

| # | check | verdict |
|---|---|---|
| 1 | r4* files ↔ README ↔ PROVINCE | DRIFT — stale PROVINCE frontier (6 bullets), "in flight" signal claim, 4 uncited entries |
| 2 | coverage-map counts | DRIFT — 44/56 files mapped; 12 r4/r4u files unrepresented |
| 3 | asar count | CONFIRMED — 9/9 exact |
| 4 | errata blocks | CONFIRMED — all present; 4/4 spot-checks cite real original text (1 premise imprecise) |
| 5 | LOG/SHONEN/QUALITY/SKILL | DRIFT — SKILL:48 stale `zstd -d`; LOG "five" vs 4 bullets; SHONEN stale line-cite + bare `[x]` marks |
| 6 | MANIFEST ↔ report | CONFIRMED — verdicts match; cosmetic 16-vs-17 / six-vs-seven count slips |
| 7 | git cleanliness | CONFIRMED — lane clean; parent shows wave-staging only |
| 8 | env keys | DRIFT — `REA_APKTOOL_JAR` documented but never exported; actual `REA_APKTOOL_COMMAND` exported and works |

Highest-value repairs: prune/merge the six stale `PROVINCE.md` Frontier bullets
against the Round-4 Core table; fix `REA_APKTOOL_JAR`→`REA_APKTOOL_COMMAND` at
`PROVINCE.md:20` and `:134`; correct the signal "in flight" line at
`PROVINCE.md:160`; drop `zstd -d` from `SKILL.md:48`; fold the 12 unmapped
r4/r4u entries into the coverage map.
