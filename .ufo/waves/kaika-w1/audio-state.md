# STATE dossier — lane `audio` (game audio production)

Wave: kaika W1 research (read-only). Date: 2026-10-19. Repo: `/home/vgpnk/Projects/shokunin/audio-shokunin`.
Method: local reads + counting commands only; no web research is required by the STATE shape, so this
dossier holds no source rows. Nothing was executed from the lane's fixtures (read-only wave; the fixture
suite writes append-only receipts). No repo file was modified; the only write is this artifact.

All numbers below carry the command that produced them, run in this session against `defbe128`.

---

## 1. Identity

| field | observed | command |
|---|---|---|
| domain | game audio production — SFX + soundtrack, headless-verified | `../MANIFEST.json` roster `audio` |
| rank | `shonen` (fleet roster) | `python3 -c "import json;print([r['rank'] for r in json.load(open('../MANIFEST.json'))['roster'] if r['id']=='audio'])"` → `['shonen']` |
| branch | `main` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `defbe128` — `cleanup: drop regenerable round scratch/baseline snapshot trees`, 2026-10-18, author `ci <ci@local>` | `git log -1 --format='%H %an <%ae> %ad %s'` |
| commits | 262 on `main`; 284 across all refs | `git rev-list --count HEAD`; `git rev-list --all --count` |
| worktree | clean (0 entries) | `git status --porcelain \| wc -l` |
| remotes | `main` is **2 ahead / 0 behind** `origin/main` (`57e5577f`) — unpushed | `git rev-list --left-right --count main...origin/main` → `2	0` |
| worktrees | 2, both at `defbe128`: main tree + `.tower/worktrees/kaika/audio-shokunin` on `kaika/round` | `git worktree list` |

**Author identity (verified, matches the fleet hint).** Commit-author mix over `main`:

```
183 audio-shokunin <audio@shokunin.local>
 73 ci <ci@local>
  4 audio-shokunin <audio-shokunin@local>
  1 shokunin-orchestrator <shokunin-orchestrator@shokunin.local>
  1 Devin <devin@cognition.ai>
```
— `git log --format='%an <%ae>' | sort | uniq -c | sort -rn`

The `ci <ci@local>` identity is therefore not a one-off: 73/262 commits. The lane already admits it:
"several prior author-integration and early safety commits carry ci@local rather than the required lane
identity" (`LOG.md:1533-1535`, entry `ATTRIBUTION CORRECTION (2026-10-16)`). New folds use per-command
identity, but the last two commits (`57e5577f`, `defbe128`) are again `ci <ci@local>`.

### Round ledger — five disagreeing records

| ledger | max round | shape | command |
|---|---|---|---|
| `reports/round-*` | **100** | 100 directories, rounds 1–100, no gaps; round 1 named `reports/round-1-calibration/` (non-conforming name) | `ls -d reports/round-* \| wc -l` → 100; per-round parse shows min 1, max 100, none missing |
| `LOG.md` | **100** | 284 `##` sections; 279 begin `## Round <n>`; rounds **82–100 are bullets inside the section starting line 1357** (`## round 81 — gst↔pipewire binding lattice (ADMIT-corr)`); **rounds 87 and 88 have zero mentions** | `grep -cE '^## ' LOG.md` → 284; `grep -cE '^## Round [0-9]+' LOG.md` → 279; `grep -cE 'r87\|r88\|ROUND 87\|ROUND 88' LOG.md` → **0** |
| `SCORECARD.md` | **86** | 86 `## Round <n> verdict` sections; nothing for 87–100 | `grep -c '^## Round [0-9]' SCORECARD.md` → 86; `grep -nE 'r8[7-9]\|Round 87\|Round 88\|r9[0-9]\|r100' SCORECARD.md` → no hits |
| fleet `MANIFEST.json` | **65** | 4 audio rows: rounds 62, 63, 64, 65 | `python3 -c "import json;m=json.load(open('../MANIFEST.json'));print([r['round'] for r in m['rounds'] if r.get('lane')=='audio'])"` → `[62, 63, 64, 65]` |
| fleet `.ufo/reports/*/audio.md` | **76** | 13 files: 62–71, 73, 75, 76 | `ls ../.ufo/reports/*/audio.md \| wc -l` → 13 |

The fleet hint "max recorded round 65" is **confirmed for `MANIFEST.json` only**. The lane's own record
is 35 rounds ahead of it; the UFO report trail is 11 rounds ahead of it.

**Last round with evidence, precisely:**

- Last **adjudicated** round: **97** (`reports/round-97/r97-adjudicator.md`; LOG line 1479 carries
  "required safety fold").
- Rounds **98, 99, 100** have reports and LOG bullets but **no adjudicator**; LOG says so itself:
  "Remaining adjudication is still open" (`LOG.md:1541`).
- Rounds **87 and 88** have full seat reports and a landed fold (`1977cf42 r87+r88 fold: land
  pwbind/btwit defect fixes (+310/-112)`, ancestor of `main`) but **no LOG entry, no SCORECARD verdict,
  no adjudicator**. Both verifiers returned GATE FAIL pre-fold: "GATE FAIL — NOT VERIFIED as a
  reproducible green landing" (`reports/round-87/r87-verifier.md` §0) and "GATE FAIL as a reproducible
  green landing" (`reports/round-88/r88-verifier.md` §0).
- Adjudicator files exist for 93 of 100 round dirs; inside 62–100 the missing set is
  **{87, 88, 93, 98, 99, 100}** — `python3` scan of `reports/round-*/ *adjudicator*`.

**Next round number: 101.**

---

## 2. Axes

Owned axes, declared at `SCORECARD.md:3`: "Owned axes: depth, coverage, calibration."

### 2.1 The score column is frozen at mint

`SCORECARD.md:8-10` still reads:

```
| depth | unmeasured | mint: no rounds yet | mint |
| coverage | unmeasured | mint: no rounds yet | mint |
| calibration | unmeasured | mint: no rounds yet | mint |
```

Command: `grep -nE '^\| (depth|coverage|calibration) \| unmeasured' SCORECARD.md | wc -l` → **3**.
The lane's stated rationale is `SCORECARD.md:3-4`: "Scores remain unassigned without a quality rubric; a
row count is a measurement, not a score or verdict." That is a declared deviation from `PROTOCOL.md:420`
("owned axes → score 0–10 → evidence pointer → last-change round") and from `AXES.md` §"SCORECARD.md
contract". It is honest, but it makes the protocol's score-based obligation — "at least one claim works
the lane's lowest-scoring non-retired axis" (`AXES.md`) — **not mechanically evaluable for 86 rounds**.

### 2.2 What the verdict rows actually say

267 axis rows across 86 round sections — `awk '/^## [Rr]ound [0-9]+/{r=$0} /^\| (depth|coverage|calibration) \|/{n++} END{print n}' SCORECARD.md` → **267**.

Aggregate verdict-word counts (grep over `| <axis> | <verdict> |`):

| axis | improved family | unchanged | ADMIT-corr (no per-axis call) |
|---|---|---|---|
| depth | 15 + 23 "improved locally" + 15 "narrowly" + 2 = ~55 | 31 | 2 |
| coverage | 15 + 23 + 6 + 3 + 2 = ~49 | 37 | 2 |
| calibration | 12 + 27 + 7 + 1 + 1 + 1 = ~49 | 25 + 11 bold = 36 | 2 |

Command: `grep -oE '\| (depth|coverage|calibration) \| [^|]+ \|' SCORECARD.md | sed -E 's/.*\| (depth|coverage|calibration) \| ([^|]+) \|/\1 \2/' | sort | uniq -c`.
Rounds 80–86 record all three axes **improved** (`SCORECARD.md:827-896`; r79 at `:817` is the
ADMIT-corr exception), i.e. the late rounds claim
triple improvement every time — a pattern worth a critic's attention, not a score.

**Lowest non-retired axis:** **undefined by the record**, because no axis carries a score.
[INFERENCE] By defect density, **calibration** is the weakest: 6 unadjudicated rounds in 62–100, two
rounds (87/88) whose GATE FAIL never reached LOG or SCORECARD, a post-hoc disclosure erratum
("preserved author receipts show two additional LAN-control runs beyond the disclosed integration pass",
`LOG.md:1542-1544`), an attribution correction, future-dated verdict headers, and a score table that has
said "mint" for 86 rounds. Depth/coverage look strong by comparison: `measure_audio.py` has 56,096 lines
and the rounds carry measured laws with receipts.

### 2.3 Saturation and capabilities

- **Saturation line: undeclared.** `SCORECARD.md:905-907` — "The lane's saturation line and stagnation
  window N are to be declared by the lane on its next round … not asserted by this conformance change."
- **Capabilities: 0 rows.** `SCORECARD.md:899-901` — "— none yet —" with the header row only.
  Command: `awk '/^## Capabilities/{f=1;next}/^## /{f=0}f&&/^\| [^|]+ \|/' SCORECARD.md | wc -l` → **0**
  (header separator excluded).
- Consequence: the stagnation nudge (`AXES.md`) can never fire — it requires "no capability has entered
  the table within the lane's stagnation window", and both inputs (window, table) are empty.

### 2.4 Planned claims

Two stale/empty surfaces:

- `SCORECARD.md:12` still opens `planned: r64 (devin, ADMIT) …` — 37 rounds stale.
  Command: `grep -n '^planned:' SCORECARD.md` → lines 12, 13.
- `SCORECARD.md:909-911` (`## Planned`) is a stub: "no entries declared by this rollout".

---

## 3. Corpus

| quantity | value | command |
|---|---|---|
| `corpus/knowledge/` entries | **14** | `ls corpus/knowledge/*.md \| wc -l` |
| entries with no `- Source:` line | **5** (`audio-checklist`, `fixture-battery`, `threshold-calibration`, `ffmpeg-cross-decoder-transport`, `seed`) | `grep -L '^- Source:' corpus/knowledge/*.md \| wc -l` |
| entries with no `- Verified at:` | same 5 | `grep -L '^- Verified at:' corpus/knowledge/*.md \| wc -l` |
| entries with no `- Recheck when:` | same 5 | `grep -L '^- Recheck when:' corpus/knowledge/*.md \| wc -l` |
| `corpus/lessons/` | **absent (0)** | `ls corpus/lessons 2>/dev/null \| wc -l` |
| `corpus/QUALITY.md` | **absent — 0 criteria** | `test -f corpus/QUALITY.md; echo $?` → 1 |
| `corpus/README.md` (coverage map) | **absent — 0 rows** | `test -f corpus/README.md; echo $?` → 1 |
| `## Frontier` rows | **1 doc**, `ports/frontier/fb-pipewire.md` | `find ports -type f \| wc -l` → 1 |
| fixture WAVs | **17** (PROVINCE still says 13) | `ls corpus/artifacts/*.wav \| wc -l` |
| fixture scripts | **19** | `ls corpus/fixtures \| wc -l` |
| tracked files under `corpus/live/` | **49,158** (97.9% of all tracked files) | `git ls-files corpus/live \| wc -l`; `git ls-files \| wc -l` → 50,213 |

**Freshness of knowledge.** Newest entry is `2026-10-14-ffmpeg-cross-decoder-transport.md` (mtime
2026-10-14 11:12); all `round-*` references inside `corpus/knowledge/` are rounds 65–70
(`grep -hoE 'round[- ]?(6[5-9]|7[0-9]|8[0-9]|9[0-9]|100)' corpus/knowledge/*.md | sort | uniq -c`).
**Rounds 71–100 (30 rounds, including the whole pw-profiler/wp-state/pactl/SoX_ng-DSP/JACK/Pulse/RTP
surface) produced zero knowledge entries.** The knowledge corpus stops where the SoX_ng decoder line
stops; everything after r70 lives only in `LOG.md`, `reports/`, and 1.4 GB of `corpus/live/` receipts.

**Overdue `recheck:`.** No entry carries a date or cadence form; 9 carry a conditional clause
("Recheck when: SoX or ffmpeg version/build changes …"). So the count of *overdue* rechecks is not
computable from the record — 0 date-form rechecks out of 14 entries.
Host versions still match the pinned ones, so the conditions have not fired:
`sox --version` → `SoX_ng v14.8.0.1`; `ffmpeg -version | head -1` → `n9.0.1`; `python3 -c "import
numpy;print(numpy.__version__)"` → `2.5.3`.

**Metadata style is non-canonical.** Fleet `CORPUS.md` requires each entry to open with `source:`,
`verified-at:`, `recheck:`. The lane uses prose bullets `- Source:`, `- Verified at:`, `- Recheck when:`.
A strict `^source:` sweep returns 0 hits in all 14 files. Either the contract or the lane should move;
today neither side acknowledges the other.

**PROVINCE coverage map: 0/3 rows.** `PROVINCE.md` has no Core / Frontier / Adjacent classification —
only "Owns", "Sources", "Refuses", "Only writes" (31 lines total: `wc -l PROVINCE.md`). The one frontier
document is the port note `ports/frontier/fb-pipewire.md`, dated **2026-11-01** (`:4`), i.e. a future
date relative to today's 2026-10-19.

---

## 4. Mistakes (mined, with class and proposed criterion)

Sweep showing that **no existing rule captures any of these**: `test -f corpus/QUALITY.md -o -f
SKILL.md; echo $?` → **1** (`corpus/QUALITY.md` absent, `SKILL.md` absent). There is no quality bar and
no craft rulebook in the repo, so every mistake below is un-caught by construction.

| # | class | evidence pointer | captured by QUALITY/SKILL? | proposed criterion |
|---|---|---|---|---|
| M1 | **Unlogged failing round** — two rounds whose verifier returned GATE FAIL never reached `LOG.md`/`SCORECARD.md` | `reports/round-87/r87-verifier.md` §0; `reports/round-88/r88-verifier.md` §0; `grep -cE 'r87\|r88' LOG.md` → 0 | no | "A round with a report but no LOG entry is `unlogged`, not `admitted`; the next round cannot open until it is logged." |
| M2 | **Adjudication skipped** — 6 rounds in 62–100 have no adjudicator while LOG records them as ADMIT-with-findings | adjudicator scan; `LOG.md:1541` "Remaining adjudication is still open" | no | "ADMIT requires an adjudicator file; a fold commit is not a verdict." |
| M3 | **Post-hoc disclosure** — two LAN-control runs beyond the disclosed one, found later in receipts | `LOG.md:1542-1546` (`ROUND 99 DISCLOSURE ERRATUM`) | no | "Every executed arm is disclosed in the round's own record at run time; a later erratum is a calibration harm." |
| M4 | **Side effect on a live network** — a 6-second multicast RTP emission from a default control | `LOG.md:1485-1490` ("ROUND 99 SAFETY … explicit-opt-in, not a default side effect") | no | "No test may emit on a physical interface unless the invocation names the interface; default-off is the only default." |
| M5 | **Commit identity drift** — 73/262 commits by `ci <ci@local>` | author mix above; `LOG.md:1533-1535` | no | "Every lane commit is authored `audio-shokunin <audio@shokunin.local>`; CI identity is a defect, not a convenience." |
| M6 | **Citation lineage drift** — reports cite commits that are not on `main` | 41 of 122 resolved commit citations in `reports/round-8*/`,`round-9*/`,`round-100/` are not ancestors of `main` (python scan; e.g. the r89 adjudicator closes at `5755be5b`/`0cbbb3bb`, neither an ancestor of `main`, while `main` carries the same subjects as `e30bcc4c`/`7506c655`) | no | "A cited commit must be reachable from the published branch, or the row says `branch-scoped`." |
| M7 | **Receipt-vs-harness falsification** — a zero-audio capture passed the TERM gate | `.ufo/reports/round-76/audio.md` §Wave-B, "critic D1 — the round's real defect" | no | "A gate that a zero-energy signal can satisfy is vacuous; every gate carries a positive control." |
| M8 | **Co-tenancy false red/green** — family locks scoped to `TMPDIR`; arms racing siblings | `SCORECARD.md` r84/r86 rows; `reports/round-88/r88-verifier.md` §0 "co-tenancy lotteries" | no | "A family that shares host resources records `co-tenancy` as a named confound; a single red run is not a verdict." |
| M9 | **Ignore-pattern escape** — regenerable snapshot trees committed; 42M `head-tree/`, 51M `big.wav` | `corpus/.gitignore:1-20` comments (`xsentinel w7-F1`, `w8-F4`, `w9`, `w12`) | no | "Snapshot/scratch classes are ignored by class pattern, then proven by a `git status --ignored` census." |
| M10 | **Future-dated verdict headers** — rounds 73/74 dated 2026-11-01 while the round landed 2026-10-14/15 | `SCORECARD.md:738`, `:748`; also `ports/frontier/fb-pipewire.md:4` | no | "A header date is the observation date; wave labels do not substitute for it." |
| M11 | **Vacuous/uncited claim inside a round** — "uncited RED run", "report's own loadavg/leg-count claims falsified by scribe" | `SCORECARD.md` r85/r84 calibration rows | no | "Every number in an admissible round is either re-derivable by the verifier or marked attestation-only." |
| M12 | **Stray byproducts promoted to repo root** — PipeWire profiler output tracked as lane files | `generate_timings.sh` at root, sha256 `ca84a047f3d50c08…`, byte-identical to `corpus/live/r89-boundary/runs/adhoc/eager/wd/generate_timings.sh` (`sha256sum` both) | no | "Test work-products live under `corpus/live/<round>/`; repo root holds only contract files." |

Honest-stop / rejected claims exist and are a strength, not a mistake: r66 "universal hard-refusal …
rejected" (`LOG.md:1473-1475`, r91 bullet), r96 "Post-subcommand -s interpretation is false and
rejected", r92 "Negative-Q reading is clipped". These are the "rejection is evidence of taste" pattern
working as intended — but they are recorded only in LOG bullets, never as lessons.

---

## 5. Contract defects

Severity: **H** = blocks a protocol obligation or falsifies an attestation; **M** = divergence/dead
pointer; **L** = hygiene.

| # | sev | defect | evidence / command |
|---|---|---|---|
| D1 | H | **`SKILL.md` absent** — the file contract's first row and SHONEN box 1's subject | `test -f SKILL.md` → 1; `git log --all -- SKILL.md` → empty, i.e. it never existed |
| D2 | H | **`corpus/README.md`, `corpus/QUALITY.md`, `corpus/lessons/` absent** — the whole corpus index/bar/lesson loop | `ls corpus/README.md corpus/QUALITY.md corpus/lessons` → all missing |
| D3 | H | **SHONEN box 1 is `[x]` while `SKILL.md` does not exist**, and its evidence pointer is dead | `SHONEN.md:3`; `test -e .shokunin/reports/audio-r1-verifier.md` → 1 |
| D4 | H | **SHONEN is not the canonical template** — prose rewritten, not "byte-identical modulo `<name>`", plus an extra closing rule | `PROTOCOL.md:429-434` template vs `SHONEN.md:3-6`, `:9-10` |
| D5 | H | **205 dead `.shokunin/…` path references** across 4 files; `.shokunin/` does not exist at lane or fleet root | `grep -rc '\.shokunin' PROVINCE.md SHONEN.md LOG.md SCORECARD.md` → 3/4/150/48; `ls -d .shokunin ../.shokunin` → both "No such file" |
| D6 | H | **PROVINCE write scope is a dead path** — "Only writes `.shokunin/audio/**`" | `PROVINCE.md:17`; actual outputs are `reports/`, `corpus/` |
| D7 | H | **51 of 216 cited report paths do not resolve** | python scan over `SCORECARD.md`+`LOG.md` (`reports/….(md\|json)`) |
| D8 | H | **41 of 122 cited commits in rounds 80–100 are not ancestors of `main`**; a parallel `wt-r9x` lineage exists (main 54 ahead / branch 21 ahead) | python scan; `git rev-list --left-right --count main...wt-r100` → `54	21` |
| D9 | H | **Round ledger divergence 100 / 86 / 76 / 65** across lane reports, SCORECARD, UFO reports, MANIFEST | §1 table |
| D10 | H | **MANIFEST axis vocabulary mismatch** — audio rows carry `{expansion, quality, discernment}` while the lane owns `{depth, coverage, calibration}` | `python3` dump of manifest audio row; `SCORECARD.md:3` |
| D11 | M | **Axes table frozen at mint** for 86 rounds (no score, no evidence pointer, "last change: mint") | `SCORECARD.md:6-10`; `grep -c 'unmeasured' SCORECARD.md` |
| D12 | M | **Capabilities table empty** and **saturation line/window undeclared** | `SCORECARD.md:899-907` |
| D13 | M | **`planned:` stale by 37 rounds** and `## Planned` empty | `SCORECARD.md:12`, `:909-911` |
| D14 | M | **Round 87/88 absent from LOG and SCORECARD** (§4 M1) | grep counts |
| D15 | M | **Rounds 82–100 have no `## Round` headers**, only bullets under the r81 section | `LOG.md:1357-1580`; next `##` at `1581` |
| D16 | M | **Future-dated records** (2026-11-01) in SCORECARD and the frontier port | `SCORECARD.md:738,748`; `ports/frontier/fb-pipewire.md:4` |
| D17 | M | **Bloat**: 49,158 tracked files (97.9%) under `corpus/live/`; worktree 1.7 G, `.git` 301 M, `corpus/live` 1.4 G; largest tracked file 24 M (`corpus/live/r89-reverify/runs/cot-r1-t3.receipt.json`); `measure_audio.py` is 56,096 lines / 2,773,759 B | `git ls-files corpus/live \| wc -l`; `du -sh . .git corpus/live`; `git ls-files -z \| xargs -0 du -h \| sort -rh \| head -1`; `wc -l corpus/fixtures/measure_audio.py` |
| D18 | L | **Non-conforming report dir** `reports/round-1-calibration/` (contains `proposed-SHONEN.patch`, a stale proposal) | `ls reports/round-1*` |
| D19 | L | **Stray root artifacts**: tracked `generate_timings.sh`; ignored-untracked `Timing1-5.plot`, `Timings.html` (18 ignored entries total) | `git ls-files \| grep generate_timings`; `git status --ignored --porcelain \| grep -c '^!!'` → 18 |
| D20 | L | **Unpushed `main`** (2 commits) while LOG claims push is "blocked" | §1 |
| D21 | L | **No `AGENTS.md`** (listed in the file contract) | `test -f AGENTS.md` → 1 |
| D22 | L | **Empty dir** `corpus/reports/round-83/` (unreferenced) | `find corpus/reports -type f \| wc -l` → 0 |

Not defects (checked and clean): no merge-conflict markers in md/py
(`grep -rlE '^(<<<<<<<|=======|>>>>>>>)' --include='*.md' --include='*.py'` → none); no credential
material observed in the lane record (matches for `api_key|password|token` are variable names, prose
"token(s)", or a scan-pattern mention — nothing quoted); `PROVINCE.md`'s testbed source
`~/Projects/gamez/research/AIAudio.md` still resolves (48,875 B).

Provenance for D5/D6 (why the pointers are dead): the pre-extraction layout is still visible in an old
verifier report — "python3 .shokunin/audio/corpus/fixtures/measure_audio.py …: No such file or directory"
(`reports/round-8/r8-verifier.md:3`, an exit-127 setup failure). The lane moved from `.shokunin/audio/`
to the repo root, but `PROVINCE.md` and `SHONEN.md` were never re-pointed; `PROTOCOL.md:415` requires a
lane to "correct `PROVINCE.md` to the real path and log the correction" when a declared surface moves.

---

## 6. Proposed round 101 (1–3 falsifiable claims, distinct axes, ≥1 on the lowest axis)

Lowest non-retired axis is recorded as **undefined** by the ledger and [INFERENCE] **calibration** by
defect density; claim C1 works calibration, so the lowest-axis obligation is satisfied under either
reading. Each claim is independently verifiable and none requires another to land.

**C1 — calibration: make the ledger tell the truth about rounds 87–100.**
Land `SCORECARD.md` rows for 87–100 (`unadjudicated` for 87, 88, 93, 98, 99, 100; `ADMIT-with-findings`
plus adjudicator pointer for the rest) and a `LOG.md` entry each for 87 and 88, carrying the pre-fold
GATE FAIL verbatim.
- Before: `grep -c 'unadjudicated' SCORECARD.md` → **0**; `grep -cE 'r87|r88' LOG.md` → **0**.
- After: `grep -c 'unadjudicated' SCORECARD.md` ≥ **6**; `grep -cE '^## Round (87|88)' LOG.md` → **2**.
- Falsified if any row asserts ADMIT without an adjudicator file, or if 87/88 are logged without the
  GATE FAIL text.

**C2 — coverage: create the three missing corpus contract files, counted.**
`corpus/README.md` (index + coverage map with one row per knowledge entry and one per frontier port,
counts carrying their commands), `corpus/QUALITY.md` (admission bar derived from the existing round
pattern: falsifiable claim, before→after command, non-author verification, no axis harmed), and
`corpus/lessons/round-101.md` with a `## Gate` section that admits/rejects this round's candidates.
- Before: `ls corpus/README.md corpus/QUALITY.md corpus/lessons 2>/dev/null | wc -l` → **0**.
- After: **3**; `grep -c 'corpus/knowledge/' corpus/README.md` → **14** (one index row per entry) and
  `grep -c 'ports/frontier/fb-pipewire.md' corpus/README.md` → **1**.
- Falsified if the index names a file that does not exist (`AXES.md` "an index row is a claim").

**C3 — depth: make every cited commit resolvable from the published branch.**
Re-cite rounds 80–100 reports to the `main`-lineage hashes where an equivalent commit exists, and mark
the remainder `branch-scoped: wt-rNN`.
- Before: 41 of 122 resolved commit citations are not ancestors of `main`
  (python: `git merge-base --is-ancestor <sha> main` over `reports/round-8*,round-9*,round-100/*.md`).
- After: **0 of 122**, with branch-scoped rows counted separately.
- Falsified if any replacement hash does not exist on `main` or the report's claim text changes.

Which sources/new entries serve these: C2 seeds the wave-2 `corpus/SOURCES.md` layout and the lesson gate;
C1/C3 need no external source (ledger work). No new knowledge entry is claimed by this dossier, so
nothing here should enter `corpus/knowledge/` without its own source line.

---

## 7. Notes for adjacent owners (reported, not absorbed)

- **Manifest shape** (peer `W1ManifestShape`): audio's 4 manifest rows use fleet axes
  `expansion/quality/discernment`; the lane's own axes are `depth/coverage/calibration`
  (`SCORECARD.md:3`). Its 4 cited commits (`cbe763e`, `1a97b0e`, `4c12342`, `1b0d276`) **are** on `main`.
- **Driver/freshness** (peers `W1Driver`, `W1Freshness`): lane rounds stopped at 100 on 2026-10-16/18;
  fleet `.ufo/reports` reaches round 104; audio's last UFO report is round 76, so fleet-level reporting
  has been silent for 24 lane rounds.
- **Protocol lane** (`W1ProtocolLane`): the `SKILL.md`-absent / SHONEN-template defect (D1–D4) is a file
  contract defect, not only a lane defect — two other lanes also lack `SKILL.md`
  (`game-dev-2d-shokunin`, `revenger-shokunin`; `for d in *-shokunin; do [ -f "$d/SKILL.md" ] …`).

---

## 8. Limits of this dossier

- Read-only: no fixture was executed, no receipt regenerated, no `git` write. Therefore "the lane's
  tests pass/fail today" is **not** observed here; only the historical verdicts in the record are.
- `LOG.md` and `SCORECARD.md` were read by targeted ranges + greps, not line-by-line; the round tallies
  are regex-derived and may under-count prose variants (e.g. "improved narrowly (disclosure only)").
- The parallel `wt-r9x` lineage was characterised by hash/ancestry checks only; I did not diff its trees.
- No web sources; STATE shape needs none.
