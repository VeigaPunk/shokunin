# kaidoku-shokunin — STATE dossier (kaika W1)

Lane: `kaidoku` — reverse engineering of shipped artifacts with REA on this host.
Repo (read-only this wave): `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`.
Measured: 2026-10-19 at `de77d754523afb673b4421d363fe89311644af4f` (clean tree, `main`,
`origin/main` == HEAD). All numbers below were re-derived in this session from the worktree or
Git objects; record-only facts are labeled as records. No repo edit, git mutation, install, or
push was made. The only write is this artifact. `web_search` was not needed and not used (STATE
lane, no external-art claim).

---

## 1. Identity

| Field | Value | Evidence |
|---|---|---|
| Domain | RE of shipped artifacts with REA on this Linux host (native ELF/PE, Electron/ASAR/JS, archives, managed, firmware, crashes, EVM) | `PROVINCE.md:1-6`; `corpus/README.md:1-9` |
| Rank | shonen (4/4 `[~]`, none `[x]`) | `SHONEN.md:1-12`; fleet `MANIFEST.json` roster row `kaidoku` |
| Branch / HEAD | `main` / `de77d754…`; working tree clean; `HEAD` == `origin/main` | `git rev-parse --abbrev-ref HEAD`; `git status --porcelain` (empty); `git rev-parse HEAD origin/main` (both `de77d754…`) |
| Last admitted round | **arc3-loop1-round11** (work `5ee13b3` + records `0436f49`), admitted in fleet `MANIFEST.json` index 292, `closed_at 2026-10-19T19:39:42Z` | `LOG.md:1664-1683`; `SCORECARD.md:1977-2027`; `MANIFEST.json` rounds[292] |
| Last landed evidence | **arc3-loop1-round12 wave, halted**: 48-seat freeze + 47/48 seat reports committed at `de77d75`; **no** work/records commit, **no** `LOG.md`/`SCORECARD.md` section, **no** report | `git show --stat de77d75`; `LOG.md` has no r12 entry (`grep -n 'round 12' LOG.md` → 2 historical hits only, lines 338 and 349); `SCORECARD.md` last section is r11 |
| Next round number | **arc3-loop1-round12** (completion/adjudication), else `arc3-loop1-round13` | `claims-frozen.md`; arc schedule declared in `LOG.md:1398-1399` ("goal-scheduled, 14 rounds per loop") |
| Fleet ledger hint vs reality | Fleet *per-lane* rows stop at **round 14** (2026-10-16, luna-round-10); fleet *closure* rows reuse **rounds 1–11** (2026-10-19) for arc3 and map them through `lane_rounds.kaidoku = 1..11` | `MANIFEST.json` indices 75-78, 166-175, 252-292 |

**Ledger hint answer.** "Max recorded round 14" is **confirmed for the fleet per-lane ledger**
(and for the lane's luna arc: `luna-round-10` is that layer's last); it is **not** the current
round: the latest admitted round is **arc3-loop1-round11**, and **arc3-loop1-round12 is frozen
and in flight** with wave artifacts landed at `de77d75`.

**Numbering conflict (verbatim material for the canonical judge).** `PROTOCOL.md:86` says
"Round numbers are monotonic; a lane must not claim a round other than the steered one". The lane
uses four numbering systems: historical `round 1–14` (2026-10-13/14), `luna-round-1–10`
(2026-10-16), `arc2-loop1-round1–10` (2026-10-18), `arc3-loop1-round1–12` (2026-10-19). The
per-lane ledger maps luna rounds to rounds 5–14; the 2026-10-19 closure rows then reuse rounds
1–11 with `lane_rounds.kaidoku` 1–11. Consequence under `PROTOCOL.md:301` (last row for a lane
wins): the row for `(kaidoku, 11)` at index 292 (arc3 r11, 2026-10-19) shadows index 172
(luna-round-7, 2026-10-16). This is a ledger-identity defect, not a lane claim; reported, not
repaired.

**Round-12 halt state (measured).** Freeze names 48 seats (`claims-frozen.md:66-70`, 12+12+12+12);
seat reports on disk are 47: `c1` 12, `c2` 12, `c3` 12, `verdicts` 11 — `verdicts/CN-1` is
absent. `claims-frozen.md` records the provider substitution (`antigravity/gemini-3.8-flash`
down → `openai-codex/gpt-6-luna-max`). The halt *cause* is not recorded in the lane repo
(`[INFERENCE]` operator/harness stop, per the commit message "as landed at arc halt"); the
commit is by the lane identity, dated `2026-10-19 17:05:32 -0300`.

The round-12 seat drafts are integration-ready but **not landed**:
`c1/CR-1.md` (fourth `ev_` family: `inspect_go_binary`, path-sensitive), `c1/CR-2.md`
(`analyze_function` path-stable path-free projection), `c2/EX-9.md`/`SC-1.md` (rule #17,
projection-local sensitivity), `c3/PL-1.md`/`RV-1.md` (citation-drift covers `recheck:` fields:
57→60 table entries, seeded `callx.txt` → `citation_dead` exit 1). `verdicts/VZ-1.md` recommends
one candidate per claim; `verdicts/CN-2.md` inventories 34 top-level reports at 16:53 and marks
every after-state `UNVERIFIABLE` until integration.

---

## 2. Axes

Owned axes per the lane's own contract: coverage, depth, calibration. Freshness/operability/
adjacency are recorded as fleet-axis moves with an unowned proxy (`SCORECARD.md:19-25`;
`SCORECARD.md:636-702`).

| Axis | Score at HEAD (0–10) | Evidence / proxy limit | Last change |
|---|---|---|---|
| coverage | **10.0** | command A: `mapped 90 / knowledge_files 90`, `missing []`, `dangling []` — index integrity only, not fraction of the REA domain | arc3-r11 (89→90) |
| depth | **10.0** | command A: `citation_resolved_rules 16 / rule_blocks 16` — citation resolvability, not semantic correctness | arc3-r10 (rule #16) |
| calibration | **10.0** | finite 9-obligation rubric (2026-10-15) + per-client surface reconciliation; failure-selected, not unbiased | luna-round-2 + later audits |
| freshness (fleet) | unowned proxy | receipts re-derived per round (r11: Ghidra 34/39, pacman 1350, ASAR 12) | arc3-r11 |
| operability (fleet) | unowned proxy | census PASS + G21 + ptr `current-ok`; probe 0 findings; custody 28/28 | arc3-r10/r11 |
| adjacency | unchanged | `PROVINCE.md` boundary untouched | — |

**Lowest non-retired axis.** All three owned proxies sit at **10.0** (a three-way tie), so the
"lowest axis" is selected by a declared tie-break (`SCORECARD.md:1340-1344`, "most-falsifiable-
next-claim"). No axis is retired.

**Saturation line / window.** Line = **10.0** on the three finite proxies; stagnation window
**N = 10 lane-rounds** (`SCORECARD.md:626-635`). The arc3 window opened at r1
(`SCORECARD.md:1340-1342`, "Round 1 of a new stagnation window (1/10)") and stands at **11/10 or
12/10** at HEAD. No capability row entered during arc3; the last capability entered at arc2-r7/r8
(`SCORECARD.md:615-624`; 4 rows at HEAD).

**Nudge status.** `AXES.md:66-73`: when every owned axis is at/above saturation and no capability
entered inside the window, "the lowest-axis obligation is waived: the round should be a
frontier/capability move". The condition is met from **r10 (10/10)**, yet r10, r11 and the frozen
r12 all ran non-capability claims (coverage/depth/operability or coverage/freshness/calibration).
Recorded as a SHOULD-level contract defect (D3), not as a claim failure.

**Capabilities (4 rows).** `SCORECARD.md:615-624`: (1) pre-registered two-lane live battery on
REA 6.5.0 (luna-round-6); (2) version-symmetry battery on REA 6.4.0 (luna-round-8);
(3) config custody pre/post-pair, 5 paths, 28-case selftest (arc2-r2/r3); (4) contained
user-service analyze of oversized PEs with analyzer-disable recipe (arc2-r7/r8).
Counting: `awk '/^## Capabilities/,/^## Saturation/' SCORECARD.md | grep -cE '^\| [a-z]'` → 4.

**Planned claims.** The `SCORECARD.md` contract field `planned` is **absent at HEAD**: the
current (r11) section has no `Planned:` line and nothing follows it
(`awk 'NR>1977' SCORECARD.md | grep -c 'Planned'` → 0). The de facto plan is
`.ufo/waves/arc3-loop1-round12/claims-frozen.md` (defect D2).

---

## 3. Corpus

| Measure | Count at HEAD |
|---|---|
| Knowledge entries | **90** |
| Lessons | **10** |
| `QUALITY.md` admission criteria | **15** |
| `QUALITY.md` weak signals | **6** |
| Coverage-map rows | **55** |
| `corpus/README.md` `## Frontier` bullets | **10** |
| `PROVINCE.md` `## Frontier` / `### Round-4 frontier` bullets | **5 / 8** |
| PROVINCE frontier rows registered by G21 | **14** (asserted; `frontier_errors []`) |
| PROVINCE Core surface rows | **20** |
| Capabilities | **4** |
| Historical evidence files | **4** (round-1 recovery only; later evidence is committed under `.ufo/waves/`) |

```bash
ls corpus/knowledge/*.md | wc -l
ls corpus/lessons/*.md | wc -l
awk '/^## Admission criteria/,/^## Signals/' corpus/QUALITY.md | grep -cE '^\| [0-9]+ \|'
awk '/^## Signals/,0' corpus/QUALITY.md | grep -cE '^\| [0-9]+ \|'
awk '/^## Coverage map/,/^## Knowledge/' corpus/README.md | grep -cE '^\| [^-]'
awk '/^## Frontier/,/^## Known gaps/' corpus/README.md | grep -cE '^- '
awk '/^## Capabilities/,/^## Saturation/' SCORECARD.md | grep -cE '^\| [a-z]'
find evidence -type f | wc -l
```

**Entries by date:** 62 × 2026-10-13, 10 × 2026-10-14, 7 × 2026-10-16, 2 × 2026-10-18,
9 × 2026-10-19 (`ls corpus/knowledge | cut -d- -f1-3 | sort | uniq -c`).

**Metadata (`source:` / `verified-at:` / `recheck:`).**

| Field | Present | Missing |
|---|---|---|
| `source:` | 82/90 | **8** |
| `verified-at:` | 81/90 | **9** |
| `recheck:` | 18/90 | **72** |
| all three | **17/90** | — |

Missing `source:` and `verified-at:` (same 8, except `verified-at` also misses
`2026-10-19-arc3-r10-rust-evidence-id-domain.md`):
`2026-10-13-r2-doctor-reverify-r2`, `2026-10-13-r3-apk-inventory`,
`2026-10-13-r3-evm-interface`, `2026-10-13-r3-jq-provenance`, `2026-10-13-r3-pe-arm64`,
`2026-10-13-r4-06-1password-asar`, `2026-10-13-r4-12-godot-arm64-scale`,
`2026-10-14-r14-02-final-sweep` (all `.md`). Command:
`for f in corpus/knowledge/*.md; do for k in source verified-at recheck; do grep -q "^$k:" "$f" || echo "MISSING $k: $f"; done; done`.

**Overdue `recheck:`.** **0 measurable.** No `recheck:` value carries a date or cadence; the 18
present values are reproducing commands (3 contain a date token inside a command, which is not a
cadence). Command: `grep -h '^recheck:' corpus/knowledge/*.md | grep -cE '2026-[0-9]{2}-[0-9]{2}|[0-9]+d\b|on-release'` → 3, all incidental. `corpus/SOURCES.md` does not exist yet
(`ls corpus/SOURCES.md` → absent); wave 2 D1 creates it, so no `used-by` rows exist.

**Stale draft headers in landed entries (defect D7).** Three published entries still carry the
seat-draft HTML comment: `2026-10-19-arc3-r8-vyper-optimizer-dispatch-shapes.md:5`,
`2026-10-19-arc3-r9-viair-fallback-miss.md:5`, and
`2026-10-19-arc3-r10-rust-evidence-id-domain.md:1`; the last reads "**DRAFT for parent
integration only** … No corpus or map edit was made by this seat" while the file is landed and
its map token exists (command A 90/90). Command: `grep -l 'DRAFT for parent integration'
corpus/knowledge/*.md | wc -l` → 3.

**Quality bar shape.** 15 criteria with a `supersedes` chain (#15 supersedes #14) and 6 weak
signals (`corpus/QUALITY.md:7-36`); admission requires a resolvable source, falsifiability,
absolute path + stable identity, observation/inference/unknown labels, verb-specific evidence-id
domain, and named non-examination (`QUALITY.md:9-25`).

---

## 4. Mistakes mined (rejected / harmed / honest-stop / errata / gate disagreements)

Sweep results are from this session: `grep -ciE '<pattern>' corpus/QUALITY.md SKILL.md`.

| id | Class | Evidence pointer | Already captured? (sweep) | Proposed action |
|---|---|---|---|---|
| M1 | Parent dispatch short-count: declared seats ≠ items array (luna 5×; arc2 r2-r4 reported "60/64, 4 non-completions" for three rounds when each dispatch held exactly 60 and completed 60) | `corpus/lessons/2026-10-18-wave-dispatch-counting.md:5-16`; `LOG.md:916-917` (five parent short-counts, round 6 at 127/128); `LOG.md:660,723,760,791` (luna occurrences) | Lesson only; sweep `items array / roster`: QUALITY 0, SKILL 0 | QUALITY #16: "a seat count is the items-array length, frozen pre-dispatch; a deficit is a named slot, never an inference from another round's roster" |
| M2 | Honest stop: unverifiable-as-observed claim refused rather than shrunk (91.6MB Godot ARM64 leg died at its own 1800s outer cap; no Evidence sealed; "re-run-dressed-as-a-move" refused) | `SCORECARD.md:798-808`; verdict row `SCORECARD.md:833` | sweep `honest`: QUALITY 0, SKILL 1 (unrelated line 115) | QUALITY #16: "a claim that cannot verify as declared is recorded as an honest stop naming the missing observation; it is never rewritten into a smaller passing claim" |
| M3 | Gate form refuted on evidence (unpinnable operator-owned line numbers, false-positive surface, frozen clause defect) — implementations worked, landing withheld | `SCORECARD.md:812-821`; `SCORECARD.md:834` | PROTOCOL §Gate standard; no lane criterion (sweep `locus`, `declared bound`, `re-key`: 0/0) | Register the gate-standard check in QUALITY (see D5) and keep the probe-vs-gate distinction |
| M4 | Receipt pointer cited as a live line: frozen claim named `config.toml:3298` while the live `PROVINCE.md:18` pointer was `:3546` and `ptr_check` read `stale`; claim adjudicated **partial**, landing withheld | `SCORECARD.md:1766-1776`; `.ufo/waves/arc3-loop1-round7/claims/c1/C1-ADJUDICATION.md` | SKILL rule at `SKILL.md:116`; sweep `receipt`: SKILL 22, QUALITY 0 | Amend the rule: name the **live line re-read at dispatch** and the receipt separately; a stale receipt pointer is a new claim |
| M5 | Records-commit scope drift: text past the declared instrument bound flipped the census to FAIL (r8 and r9 each caught a pre-existing gate FAIL from the previous round's records section) | `LOG.md:1595-1619`, `LOG.md:1621-1641`; `SCORECARD.md:1872-1924` | standing rule only in the census header (`.ufo/gates/c1-census-v10.py:41-46`); sweep `locus`, `declared bound`: QUALITY 0, SKILL 0 | Promote the standing rule into `QUALITY.md` and a SKILL rule: "records text appended past a declared bound is locus-free or the bound is re-keyed in the same commit" |
| M6 | Overstatement in a sweep: "all nine literals cleared" corrected to **8/9 + adjudicated NO-CHANGE** | `SCORECARD.md:1649-1651`; `LOG.md:1525` | sweep `sweep / enumerate`: QUALITY 1, SKILL 0 | QUALITY: "a sweep claim enumerates every item with its own verdict; a count of clean items is not a sweep" |
| M7 | Append-only violation: four SCORECARD living-row rewrites in records commits (rounds 2/3/4/7), numstat-confirmed, disclosed, not retro-fixed | `LOG.md:912-914` (r14 closeout); `LOG.md:902-930` (round section) | PROTOCOL append-only; sweep `append-only`: QUALITY 0, SKILL 2 (unrelated) | QUALITY: "records append; a correction is a new dated row, never an in-place rewrite" |
| M8 | Hygiene: one committed `.pyc` caught by the pre-commit name check and removed; `__pycache__/` now ignored | `LOG.md:1484-1485` (r3 hygiene) | repo hygiene, no criterion needed; sweep `git ls-files '*.pyc'` → 0 | keep |
| M9 | Instrument limits adjudicated, not PASS (round-5 SIZES comma-token, round-4 F18 replacement-encoding, round-5 opener-detector) | `SCORECARD.md:576-588` | census header + SCORECARD prose; QUALITY 0 | QUALITY: "an instrument limit is ADJUDICATED with a retest trigger, never recorded as PASS" |
| M10 | Promotion-checklist drift (current, not historical): `SHONEN.md` still asserts "14/14 rule blocks" and "rules #11-14" while command A reads 16/16 | `SHONEN.md:6`; command A at HEAD | co-land rule #16 (`SKILL.md:279-294`); sweep `SHONEN`: SKILL 1, QUALITY 0 | Re-derive the counts in the same commit that lands a rule (D1) |

Rejected rounds retained as taste: arc2-r3 (1/3 verified; two honest stops), arc3-r7 (C1
adjudicated-partial), and the r5 audit's five corrected discrepancies. No round in the lane's
history is recorded as **harmed** on any axis (grep `harmed`: LOG 1, SCORECARD 1, both the
honest-stop clause "not harmed").

---

## 5. Contract defects (lane-owned unless marked fleet)

| id | Defect | Evidence | Owner |
|---|---|---|---|
| D1 | `SHONEN.md` stale: "SKILL.md:81-255 … 14/14 rule blocks" vs 16 blocks at HEAD; "rules #11-14" omits #15/#16 | `SHONEN.md:6`; command A reads `rule_blocks 16, citation_resolved_rules 16` | lane |
| D2 | `SCORECARD.md` contract field `planned` missing at HEAD; the next round's claims exist only in the round-12 freeze | `SCORECARD.md:1977-2027` contains no `Planned:` line (count 0 after line 1977) | lane |
| D3 | Stagnation nudge unrecorded/unmet: arc3 window reaches 10/10 at r10, no capability row since arc2-r7/r8, yet r10, r11 and the frozen r12 all ran non-capability claims; `## Saturation` still reads "window resets from here" without the arc3 count | `SCORECARD.md:626-635`; `SCORECARD.md:1340-1342`; `SCORECARD.md:1926-2027`; `claims-frozen.md:11-16`; `AXES.md:66-73` | lane |
| D4 | Round 12 in flight: 47/48 seat reports (CN-1 absent), no work commit, no records section, no lane report, no admission; wave artifacts committed as "arc halt" | seat counts 12/12/12/11 (see command block); `LOG.md` has no r12 entry; `SCORECARD.md` ends at r11 | lane |
| D5 | Census verdict script is unregistered and non-self-testing: the `SKILL.md` registry has 3 rows and no `c1-census-v10.py`; the script's argparse exposes only `--root/--json/--quiet` (no `--selftest` or fixtures), while `PROTOCOL.md:360-407` requires a registry row and a self-invocation mode for a gate; the lane itself calls its FAIL a "gate FAIL" (`LOG.md:1599`, `SCORECARD.md:1819`) | registry row count and `grep -n add_argument` in the command block (3 flags) | lane |
| D6 | Entry metadata gaps: 72/90 lack `recheck:`, 8 lack `source:`, 9 lack `verified-at:`; only 17/90 carry all three; the 18 `recheck:` values are commands with no date/cadence, so `SOURCES.md`'s overdue rule cannot be computed | Section 3 sweeps; `2026-10-19-arc3-r10-rust-evidence-id-domain.md:1-9` (source + recheck, no `verified-at`) | lane |
| D7 | Three landed entries keep "DRAFT for parent integration only" headers; one says "No corpus or map edit was made by this seat" | r8 entry line 5, r9 entry line 5, r10 entry line 1 (files in `corpus/knowledge/`) | lane |
| D8 | Lessons lack the wave-2 gate form: 7/10 have no `## Gate`, and all are date-named (`2026-10-18-…`) rather than `round-<N>.md`; the 3 process lessons (dispatch counting, caller-independent services, mechanism-matched walls) have no Gate | lesson sweep in the command block | lane |
| D9 | Ledger identity and omission: per-lane rows stop at round 14 (2026-10-16) while 2026-10-19 closure rows reuse rounds 1-11 with `lane_rounds.kaidoku`; `(kaidoku,11)` has two rows (index 172 and 292) and last-wins shadows luna-round-7; the whole arc2-loop1-round1–10 (2026-10-18) has **no** ledger row (`grep` for `arc2` in `MANIFEST.json` → 0); arc-scoped counters restart while `PROTOCOL.md:86` demands monotonic rounds | `MANIFEST.json` indices 75-78, 166-175, 252-292; `python3 -c` sweep for `arc2` | fleet (integrator) |
| D10 | Bloat: `SCORECARD.md` 137,290 B / 2,027 L; `LOG.md` 111,338 B / 1,683 L; `corpus/README.md` 45,863 B / 190 L (55 rows with very long cells); `SKILL.md` 35,022 B / 427 L | `wc -c` / `wc -l` sizes in the command block | lane |
| D11 | Fleet-root contamination (out of scope, reported verbatim): fleet `SCORECARD.md` line 1 is `# kotoba-shokunin — Scorecard`, fleet `LOG.md` line 1 is `# kotoba-shokunin — Iteration Log` and its tail is kotoba rounds 31-36 — while `MANIFEST.json`/`PROTOCOL.md` are the fleet's; and `.ufo/reports/round-5..11/kaidoku.md` are absent although `MANIFEST.json` marks kaidoku `ok` for those rounds (the protocol says an `ok` row is falsified by the missing derivable report path) | `head -3 LOG.md`; `head -1 SCORECARD.md`; report-path listing in the command block (present 1-4, missing 5-11) | fleet |
| D12 | Push-rule conflict (out of scope): `MANIFEST.json` notes say "No push (standing rule)" (9 occurrences) while the lane `HEAD` equals `origin/main` (`de77d754…` both) | `grep -c 'No push (standing rule)' MANIFEST.json` → 9; `git rev-parse HEAD origin/main` | fleet / operator |
| D13 | Records gap (minor, historical): `SCORECARD.md` has no `luna-round-10` section (round 14 in the fleet ledger), although `SCORECARD.md:610-612` planned it and its verdicts live only in `LOG.md:902-930` and `.ufo/reports/luna-round-10/kaidoku.md` | `grep -n '^## .*luna-round-10' SCORECARD.md` → none | lane |
| D14 | Cache inventory incomplete (found by peer `W1ArtKaidoku`, verified here): four `rea-agents` npx caches exist for three versions. `~/.npm/_npx/9b9809298fe40d2c/node_modules/rea-agents` is a **byte-identical 6.7.0 duplicate** (1775 files, 28,575,703 B; package.json sha256 `3f6c47fb…`; cache-root dir mtime **2026-10-19 15:19:40 -0300**, package dir and both `package.json` mtimes **10:06:03 -0300** — different objects) created by the **unpinned** npx spec (`cache-root package.json` `_npx.packages: ["rea-agents"]`, dependency `^6.7.0`), not listed in `PROVINCE.md:19-23`. Hazard: an unpinned spec can re-resolve to a future version; the pinned 6.7.0 path `a1722018…` (Kimi config `npx -y rea-agents@6.7.0`) is unaffected, so no probe/gate resolves through `9b980…` today. | enumeration in the command block; `stat -c '%y %n'` on the four objects; `sha256sum` of both `package.json` files → `3f6c47fb12c8388f291a21e7f99a876495d03aee671b3b6a0708dd12d6ebb570` | lane |

```bash
# D2
awk 'NR>1977' SCORECARD.md | grep -c 'Planned'
# D4 seat reports (depth-1 seat reports only)
for c in c1 c2 c3 verdicts; do ls .ufo/waves/arc3-loop1-round12/claims/$c/*.md | wc -l; done
# D5 registry rows and census flags
awk '/^## Local round-evidence gate registry/,0' SKILL.md | grep -cE '^\| [a-z]'
grep -n 'add_argument' .ufo/gates/c1-census-v10.py
# D8 lessons without a Gate
for f in corpus/lessons/*.md; do grep -q '^## Gate' "$f" || echo "$f"; done
# D10 sizes
wc -c LOG.md SCORECARD.md SKILL.md PROVINCE.md corpus/README.md corpus/QUALITY.md
# D11 fleet report paths (run from the fleet root)
ls .ufo/reports/round-{1..11}/kaidoku.md
# D14 cache inventory (four dirs, three versions)
for d in ~/.npm/_npx/*/node_modules/rea-agents; do grep -m1 '"version"' "$d/package.json"; done
cat ~/.npm/_npx/9b9809298fe40d2c/package.json   # _npx.packages: ["rea-agents"] (unpinned)
```

Not defects: no `corpus/SOURCES.md` (wave 2 D1 creates it); `__pycache__/` under `.ufo/gates/`
is git-ignored and untracked; `/tmp` quota is recorded in every recheck as a host constraint
(use `/var/tmp`).

---

## 6. Proposed round

Two moves, nested: **finish the halted r12** (the claims are frozen, measured on scratch, and
have a per-claim recommendation), then **r13 must be a capability/frontier move** (D3).

### 6a. arc3-loop1-round12 integration (immediate; 3 claims, distinct axes)

| Claim | Axis | Falsifiable before → after | Counting command |
|---|---|---|---|
| C1: land `inspect_go_binary` as the fourth `ev_` family (CR-1) + one map token; hold CR-2's path-free `analyze_function` as a separate Unknown | coverage (owned) | `knowledge_files 90 → 91`, `mapped 90 → 91`, `missing []`, `dangling []` | command A (`SCORECARD.md:88-124`), run at the landing commit |
| C2: land queue-drain rule #17 "evidence-id sensitivity is projection-local" with the r7/r10/r11 citations (SC-1/EX-9, VZ-1 form) | depth (owned) | `rule_blocks 16 → 17`, `citation_resolved_rules 16 → 17` | command A |
| C3: extend the citation-drift pointer table to grade `recheck:` fields of the three `ev_` entries (PL-4/RV-1 rows), re-pin table digest in the same commit | operability (fleet) | `entries 57 → 60`; strict probe clean; seeded r11 `callx.txt` → `citation_dead` exit 1 | `python3 -c "import json;print(len(json.load(open('.ufo/gates/citation-drift/pointer-table.json'))['entries']))"` + strict probe |

Rule #16 applies to all three: entry ↔ map token ↔ table digest ↔ `expected.json` land in one
commit, then command A is re-run at that commit and the revision recorded. The after-states in
`c1/CR-1.md`, `c2/SC-1.md`, `c3/PL-1.md` are the seats' scratch projections — `UNVERIFIABLE`
until integration (CN-2, VZ-1).

### 6b. arc3-loop1-round13 (nudge-satisfying: capability/frontier, 1-2 claims)

| Candidate | Why it satisfies the nudge | Falsifiable before → after |
|---|---|---|
| ARM64X hybrid PE analysis via Ghidra (self-provisionable, no install) | `PROVINCE.md:83` reserve; moves frontier ground to Core | capability row 4 → 5: one real host carrier analyzed, `evidence_id` + subject sha256 + procedure count > 0 + chosen language id recorded |
| Named-function recovery from typora's `.jsc` using the already-installed electron 42.2.0 run-as-node path (no install) | `.jsc` → source mapping frontier (`corpus/README.md:170-181`; r4-07 holds only Ignition disassembly) | a named-function count from the 530KB Ignition disasm, before 0 named → after N named, with the exact command |
| Organic crash core >32MiB | **blocked** — no cap-raising knob; do not propose without a new mechanism (`corpus/lessons/2026-10-18-mechanism-matched-walls.md` stop rule) | — |

Which sources/entries serve it: C1's entry is self-sourced from the r12 evidence bundle (REA
6.7.0 package source `dist/domain/evidence.js:159-183`, `canonicalDigest.js:8-25,60-76`), so
wave 2's `SOURCES.md` should register the REA package-source path and the CLI self-docs as the
learning rows; C3's entry needs the citation-drift tool docs (`SKILL.md` registry row) as its
source row. No `SOURCES.md` rows are listed here because none were opened and none exist yet
(wave-2 D1 owns that table).

---

## Measurement log (this session, read-only)

| Command | Result |
|---|---|
| `git rev-parse --abbrev-ref HEAD; git rev-parse HEAD; git status --porcelain` | `main`, `de77d754…`, clean |
| `git rev-parse HEAD origin/main` | both `de77d754523afb673b4421d363fe89311644af4f` |
| command A at `HEAD` and `5ee13b3` (recipe `SCORECARD.md:88-124`) | both: `knowledge_files 90, mapped 90, missing [], dangling [], rule_blocks 16, citation_resolved_rules 16, coverage 10.0, depth 10.0` |
| `python3 .ufo/gates/c1-census-v10.py --json --quiet` | `VERDICT PASS` (stale/ambiguous/undeclared/unresolved 0/0/0/0), `frontier_rows 14`, errors `[]`, `g2_ok true`, `g11 []`, `g7 []`, `declared_fail_classes []`; live pins devin 6.5.0 / omp 6.5.0 / kimi 6.7.0; counts 162/2027/427 lines |
| `python3 .ufo/gates/citation-drift/citation-drift-probe.py --root . --rev HEAD --table … --expected …` | `CITATION_DRIFT_VERDICT: reported findings=0 exit=0` |
| Counts (knowledge/lessons/quality/map/frontier/capabilities) | 90 / 10 / 15+6 / 55 / 10 / 4 |
| Metadata sweep (`source`/`verified-at`/`recheck`) | 82 / 81 / 18 present; 8 / 9 / 72 missing; 17 all three |
| Round-12 seat inventory | 12 + 12 + 12 + 11 = **47** of 48 (`CN-1` absent) |
| `wc -c` sizes | LOG 111,338; SCORECARD 137,290; SKILL 35,022; PROVINCE 20,188; README 45,863; QUALITY 6,531 |
| tracked `.pyc` files | 0 |

```bash
git ls-files '*.pyc' | wc -l
```

Record-only (not re-run this session): custody-pair selftest 28/28 and pair MATCH 5/5 (R11
records; `RV-1` re-ran the selftest at `/var/tmp`); round-12 seats' scratch measurements; all
provider substitutions and quota failures.

## Limits of this dossier

- Axis scores are the lane's declared finite proxies; they are not a calibrated expertise
  ranking (the lane says so at `SCORECARD.md:3-17`).
- `[INFERENCE]`: the r12 halt cause; whether the fleet's 2026-10-19 closure rows were intended to
  reuse rounds 1-11 rather than continue the per-lane counter.
- No external-art claim: this is a STATE dossier; `SOURCES.md` rows and candidate knowledge
  entries belong to the ART lanes and wave 2.
- The fleet-root anomalies (D11, D12) are reported for the integrator/judge and were not touched.
