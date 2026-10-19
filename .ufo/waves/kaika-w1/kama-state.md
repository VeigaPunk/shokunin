# kama-shokunin — STATE dossier (kaika W1)

Lane: `kama` — local model serving & endpoint health
Repo: `/home/vgpnk/Projects/shokunin/kama-shokunin` (read-only in this wave)
Fleet root: `/home/vgpnk/Projects/shokunin`
Date: 2026-10-19
Shape: STATE (campaign §Dossier shapes). No web research; `web_search` available but unused — STATE needs none, so there are **0 source rows** and no `SOURCES.md` claims here.

What I executed: file reads plus read-only commands in the lane repo, the fleet root, and `$HOME` existence checks. What I did **not** execute: any `kama-probe.sh` subcommand, `snapshot`, `test-snapshot.sh`, installs, git mutations, or writes outside this artifact. Every count below carries its command; nothing was rerun from an older round and reported as fresh.

---

## 1. Identity

| Field | Value | Evidence / command |
|---|---|---|
| Domain | local model serving & endpoint health | `PROVINCE.md:3`; `MINT.md` §Domain boundary |
| Fleet rank | `shonen` (probation), roster id `kama`, minted 2026-09-29 | `MANIFEST.json` roster; `PROVINCE.md` |
| Branch / HEAD | `master` / `35e9175` | `git branch --show-current; git rev-parse --short HEAD` |
| Tracked files | 66 | `git ls-files \| wc -l` |
| Fleet ledger max kama round | **4** | `grep -n '"kama": 4' MANIFEST.json` → line 2332 (the only `lane_rounds` entry naming kama, 2026-10-14) |
| Fleet reports for kama | **7** files: rounds 1, 2, 4, 6, 7, 8, 9 | `ls ../.ufo/reports/round-*/kama.md 2>/dev/null \| wc -l` → 7; round 3 absent (`ls ../.ufo/reports/round-3/kama.md` → No such file) |
| Lane LOG round headings | **11** `##` headings | `grep -cE '^## ' LOG.md` → 11 |
| Recorded craft rounds | 1, 2, 3, 4 | `LOG.md` lines 7, 100, 203, 266 |
| Report-backed craft rounds | 3 (rounds 1, 2, 4; round 3 report gap) | SCORECARD §Current authority; `ls` above |
| Last admitted craft round | **4** (`0505b71` per fleet wave; report 3,074 B) | `MANIFEST.json` 2026-10-14 `lane_rounds`; `ls -l ../.ufo/reports/round-4/kama.md` |
| Later attempts | round 5 blocked attempt; rounds 6–9 blocked dispatch; round 10 plan-only | `SCORECARD.md` §Actual round 5, §Round 6–9; LOG §Actual round 5, §round 6–9 |
| Last round with telemetry | **9**, 2026-10-18, BLOCKED-WITH-DATA | `.ufo/round-9/telemetry.json`; `../.ufo/reports/round-9/kama.md` (3,078 B) |
| Next round number | **10** (plan exists, unexecuted: `dispatch_utc: null`, no telemetry); **11** only if the plan counts as an attempt | `.ufo/round-10/plan.json`; `find .ufo/round-10 -type f` → `plan.json`, `SEAT-PROTOCOL.md` |
| Working tree | **1 uncommitted change = `.ufo/round-10/`** — exactly 2 untracked files: `.ufo/round-10/plan.json`, `.ufo/round-10/SEAT-PROTOCOL.md` | `git status --porcelain=v1 -uall` → 2 `??` lines |

Lane-own admissions are explicit that blocked attempts do not increment the counter:

> "This attempt adds **zero** verified completed rounds." — `SCORECARD.md` §Current authority

> "This is a **blocked round attempt**, not an admitted or verified completed round." — `corpus/lessons/round-5.md` §Gate

> "the cumulative verified-round total remains unestablished" — `LOG.md` §Actual round 5

**Identity defects recorded, not resolved:** the lane's local attempt namespace reaches 9 while the fleet ledger records 4; `LOG.md` contains two different `round-1` headings (`:7` craft, `:273` relaunch) and an unnumbered-style `## 4 —` (`:266`). The relaunch collision is already named in the lane's L0 question (`../.ufo/l0-questions.md`, `kama | round-1 | Reconcile the relaunched counter…`), not silently repaired.

---

## 2. Axes

Scores are the lane's self-assessed, evidence-bound rows in `SCORECARD.md` §Axes; I did not re-score them. The SCORECARD banner says the numeric rows are historical assessments, not remeasured file lengths — so the counts below are the *present* measurements of the evidence artifacts, not new axis scores.

| Axis | Score | Evidence pointer | Present measurement / limit |
|---|---:|---|---|
| **operability** (LIVE) | 8 | `tools/kama-probe.sh` md5 `1f81e859c2d7f43f87d1f7e01327b2cf`, 1,092 lines; `registry/endpoint-consumers.tsv` 3 rows; probe `check` last executed 2026-10-15 exit 2 | `md5sum tools/kama-probe.sh` (hash matches SCORECARD); `wc -l tools/kama-probe.sh` → 1,092; registry data rows → 3 (`awk -F'\t' '!/^#/ && NF>1 && $1!="id"' registry/endpoint-consumers.tsv \| wc -l`) |
| **freshness** (LIVE) | 7 | `registry/history/latest.tsv` baseline `20261014T124232Z`; `DELTA.md` 16 transitions; round-5 local delta `fields_checked=4 mismatches=0` | `head -1 registry/history/latest.tsv`; `grep -c '^- ' registry/history/DELTA.md` → 17 entries (baseline + 16 transitions); tracked baseline is **5 days old** today (`date -d 2026-10-19` − `date -d 2026-10-14` → 5 days) |
| depth | 7 | `SKILL.md`; `corpus/knowledge/endpoint-identity.md`; `snapshot-history.md` | `wc -l SKILL.md` → **342**; decision-table data rows **12** (`sed -n '127,141p' SKILL.md \| grep -c '^\|'` → 14 incl. header+sep); error-signature rows **12** (14 − 2); anti-patterns **11**; checklist steps **8** |
| coverage | 8 | 9 knowledge entries, 9 lessons, 5 QUALITY criteria, 19 coverage-map rows, 4 frontier rows | `ls corpus/knowledge/*.md \| wc -l` → 9; `ls corpus/lessons/*.md \| wc -l` → 9; `grep -cE '^\| KQ[0-9]+ ' corpus/QUALITY.md` → 5; coverage/frontier counts in §3 |
| calibration | 7 | round-1 critic falsification; round-4 independent audit; round-5 blocked admission; missing non-author spot-check | `corpus/lessons/round-1-critic.md`; `round-4-recensus.md`; `round-5.md` §Spot-check ("Not performed") |
| adjacency | 7 | `corpus/knowledge/cross-lane-scope.md` ownership + arbitration + handoffs | 6 stale `PROVINCE.md:22-26` anchors in that file (§5); ownership table otherwise intact |

- **Lowest non-retired axis:** 7 — freshness, depth, calibration, adjacency are tied. None is retired (`SCORECARD.md` §Retired: "None").
- **Lowest LIVE assigned axis:** **freshness (7)** vs operability (8). Assignment: `MISSION.md:29` — `axes: "operability + freshness"`.
- **Saturation line / window N:** not declared. `SCORECARD.md` §Saturation: "to be declared by the lane on its next round per `AXES.md` §The stagnation nudge". No stagnation claim is evidence-backed.
- **Capabilities:** **0** rows. `awk` count of data rows in §Capabilities → 0 (only header+separator); table body is `— none yet —`.
- **SCORECARD §Planned claims (author):** re-anchor still-live probe citations via explicit correction entries; declared-vs-served context size is blocked (no serving runtime); service restoration, scheduling, and global route config are operator-owned.

Author scorecard row for depth is **stale by three counts** (claims 323 lines / 11 signatures / 14-step checklist; measures 342 / 12 / 8). The header banner qualifies numeric rows as historical, but the row is an index-row claim; see §5 D3.

---

## 3. Corpus

Counts (all run in the lane repo):

| Quantity | Value | Command |
|---|---:|---|
| Knowledge entries | 9 | `ls corpus/knowledge/*.md \| wc -l` |
| Lessons | 9 | `ls corpus/lessons/*.md \| wc -l` |
| All corpus entries | 18 | `find corpus/knowledge corpus/lessons -name '*.md' \| wc -l` |
| QUALITY criteria | 5 (`KQ1`–`KQ5`) | `grep -cE '^\| KQ[0-9]+ ' corpus/QUALITY.md` |
| Coverage-map rows | 19 | `awk '/^## Coverage map/{f=1;next}/^## /{f=0} f&&/^\| `/{c++} END{print c}' corpus/README.md` |
| `## Frontier` rows | 4 | `awk '/^## Frontier/{f=1;next}/^## /{f=0} f&&/^- /{c++} END{print c}' corpus/README.md` |
| Entries with `source:` | **0 / 18** | `grep -lE '^source:' corpus/knowledge/*.md corpus/lessons/*.md \| wc -l` |
| Entries with `verified-at:` | **0 / 18** | same with `^verified-at:` |
| Entries with `recheck:` | **0 / 18** | same with `^recheck:` |
| Lessons with `## Gate` | **2 / 9** | `grep -l '^## Gate' corpus/lessons/*.md \| wc -l` |

Present structure instead of frontmatter: each entry opens with a dated prose line (e.g. `round-5.md:3` "2026-10-15") and carries a `## Cited sources` section or inline `path:line` citations. **No `recheck:` cadence exists**, so no "overdue before 2026-10-19" set is computable; all 18 entries are missing the field by construction. This is a contract-level gap against the wave's `corpus/` contract, not a lane calibration finding (see §5 D1).

Coverage by round (from coverage map + filenames): round 1 — 7 knowledge + 6 lessons; round 2 — 1 knowledge + 1 lesson; round 3 — none (recorded in `LOG.md`, report missing); round 4 — 1 lesson; round 5 (blocked attempt) — `QUALITY.md`, `lessons/round-5.md`; rounds 6–9 — `knowledge/free-tier-provider-limits.md`. Command: `sed -n '/^## Coverage map/,/^## Known gaps/p' corpus/README.md`.

Corpus-vs-index claims that do not hold:

- `corpus/README.md` indexes `free-tier-provider-limits.md` as rounds **6–17** ("in progress; loop 1 final"), but the entry records **4** rounds (6–9) and explicitly leaves loops 2–3 pending. Command: `grep -c '^| [0-9] ' corpus/knowledge/free-tier-provider-limits.md` → 4 status rows; `sed -n '/^## Status board/,/^n\/m =/p'` shows rows 6–9.
- The same entry's header says "rounds 6–17"; index row repeats it.

QUALITY bar (quoted criteria are paraphrased from `corpus/QUALITY.md` §table, rows KQ1–KQ5): current probe command + exit (KQ1), pin provenance vs effective runtime separated (KQ2), dated/supersession + preserved bytes (KQ3), invocation-history scope vs scheduling (KQ4), operator handoff and nonsecret evidence (KQ5). Review boundary: author/parent-advisor agreement is not an outside spot-check; promotion remains `[~]` in `SHONEN.md` (4/4 rows author-asserted).

Corpus claim that is outright false in present tense:

> "The repository currently has no `tools/kama-probe.sh` or `registry/endpoint-consumers.tsv`" — `corpus/lessons/probe-mutation-matrix.md:3`

Both artifacts have existed since round 1. The lesson is dated at the end of the same line, but the sentence is present tense with no historical marker (KQ3 class).

---

## 4. Mistakes mined

Classes: implementation (I), method (M), calibration/overclaim (C), safety (S), admission/process (P). "Covered?" names the existing rule and the sweep used; where none applies I propose one.

| # | Mistake | Class | Evidence pointer | Covered? (sweep) | Proposed if uncovered |
|---:|---|---|---|---|---|
| 1 | Port resolver synthesized port `30` from model name `Qwen3-Coder-30B` | I | `LOG.md` §round 1 ("the port resolver synthesised `30`"); `SKILL.md` §Anti-patterns #11 | Yes — SKILL anti-pattern #11; regression fixtures `test-snapshot.sh` (24 pass) | — |
| 2 | `--json` path died on trailing comma produced by `$(…)` stripping newline | I | `LOG.md` §round 1 | Harness-covered (exit/JSON fixtures), no QUALITY rule | Keep as fixture class |
| 3 | Lowercase `~/projects` vs `~/Projects` sweep missed the whole checkout | M | `LOG.md` §round 1; `consumer-registry.md` errata | No criterion; no sweep in QUALITY/SKILL | Method rule: canonicalize path case before any repo sweep |
| 4 | Bare `ss -tnp` cannot see listeners; `-l` is required | M | `LOG.md` §round 1 | SKILL §Checklist step 4 uses `ss -ltn` (`grep -n 'ss -ltn' SKILL.md` → hit) | — |
| 5 | `git remote -v \| head -2` "invented" a remote difference | M | `LOG.md` §round 1 | None | Method rule: count-then-read, never head-truncate evidence |
| 6 | Frozen route fact `m_flash` attributed to wrong provider (`alibaba-token-plan` vs `charm-hyper`) | C | `LOG.md` §round 1 peer ledger; `round-1-citations.md` F11 MISMATCH | No QUALITY rule; caught only by reviewer role | Method rule: frozen host facts carry re-derivation commands |
| 7 | "Dead" endpoint wording where service was alive-but-foreign | C | `round-1-critic.md` §Final verdict ("alive but returns Jitsi/Jetty-style HTML 404") | KQ1 (verdict+reason) and KQ2 (pin vs runtime) | — |
| 8 | NAT question asserted/decided without root; correct verdict was UNDECIDABLE | C | `round-1-critic.md` Route 2 ("undecidable without root") | None | **KQ6 (new):** privilege/tool-bounded claims record `UNDECIDABLE` + exact blocked command |
| 9 | Whole-file config read returned a credential line | S | `LOG.md` §round 1 hygiene; `round-2.md` read-overrun note | KQ5 (nonsecret shape only) | — |
| 10 | Redaction regex matched the word "token" inside a route alias (false positive) | S | `LOG.md` §round 1 | None | Method rule: key-side scans for secret values, not substring scanners |
| 11 | Draft claimed "periodic" monitoring when only invocation history existed | C | `round-2.md` §Freshness claim boundary ("A stateful probe is not a scheduler.") | KQ4 | — |
| 12 | `set -e` turned legitimate drift exit 2 into premature script exit | I | `round-2.md` §Implementation traps | Fixtures; no QUALITY rule | Keep as fixture class |
| 13 | `index.jsonl` duplicated derivable dated-file metadata (dead weight) | I/P | `round-2.md` §Implementation traps (simplifier removed it) | None | **KQ7 (new):** no persisted state derivable from an authoritative artifact |
| 14 | 46 stale "current" lines survived round-1 review; 11 lines still survive today | C | `round-4-recensus.md` §Independent audit erratum; §3/§5 here | KQ3 states the rule, but enforcement failed | **KQ8 (new):** every correction round runs a mechanical dead-anchor sweep with a pasteable count |
| 15 | Round-3 fleet report absent; counter/report gap recorded only in round 4 | P | `round-4-recensus.md` §Counter-vs-log audit ("round 3 has no report file") | No QUALITY rule (fleet-level) | Fleet rule: a completed round without a report is `incomplete`, not `ok` |
| 16 | Relaunch reused `round-1` while history was at round 4 | P | `LOG.md:273`; `round-5.md` correction | No QUALITY rule | Fleet rule: relaunch appends `round-(max+1)` with a start-revision line |
| 17 | Documentation delta treated as progress under blocked dispatch | P | `round-5.md` §Gate; `SCORECARD.md` "Admission: BLOCKED, not saturated." | KQ5 + explicit BLOCKED admission | — |
| 18 | Generated prompt said `calibration`; `MISSION.md:29` says `freshness` | P | `LOG.md:273`–`:280` (mission precedence recorded) | No QUALITY rule | Fleet contract: mission file is the only axis authority |
| 19 | Index row claims rounds 6–17 for a 6–9 entry | C | `corpus/README.md` row; `free-tier-provider-limits.md` header/status board | KQ3 partially (dated, but range overclaims) | **KQ8** (index rows name only measured ranges) |
| 20 | SCORECARD depth row counts (323/11/14) contradict the file (342/12/8) | C | `SCORECARD.md:21`; measurements in §2 | KQ3 + §Current authority banner (mitigation, not fix) | KQ8 |

**Counts:** 20 mistakes mined — 17 lane-internal, 3 process/fleet (15, 16, 18). Already covered by KQ1–KQ5 or SKILL/checklist: 8 (rows 1, 4, 7, 9, 11, 14 (rule exists), 17, 20 (rule exists)). Uncovered → proposals: 2 QUALITY criteria (KQ6 UNDECIDABLE, KQ7 derivable-state), 1 enforcement criterion (KQ8 anchor/index sweep), 4 method rules (path case, no head-truncated evidence, frozen-fact re-derivation, key-side secret scans), 3 fleet rules (15, 16, 18).

### Gate disagreements (verbatim, for the canonical Rust judge)

| # | Conflict | Side A | Side B |
|---:|---|---|---|
| G1 | round-2 status | Fleet ledger (2026-09-29): kama round 2 `in-flight`, "no report (`.ufo/reports/round-2/kama.md` → No such file)" | Report now exists: `../.ufo/reports/round-2/kama.md`, 9,909 B — `ls -l` |
| G2 | round ceiling | Fleet: max kama round **4** (`grep -n '"kama": 4' MANIFEST.json`) | Lane: attempts recorded through 9, plan at 10 (LOG/SCORECARD) |
| G3 | report inventory | `SCORECARD.md` §Current authority: "Historical reports exist for rounds 1, 2 and 4" | Fleet: 7 reports (1, 2, 4, 6, 7, 8, 9) — blocked reports omitted from that sentence |
| G4 | round 3 | `LOG.md` records a completed round-3 re-census | No `../.ufo/reports/round-3/kama.md`; SCORECARD calls it unresolved debt |
| G5 | axis authority | Generated prompt: `operability + calibration` (per `LOG.md:273`) | `MISSION.md:29`: `operability + freshness (local model serving/endpoints)` |
| G6 | depth counts | `SCORECARD.md:21`: 323 lines / 11 signatures / 14-step checklist | Measured: 342 / 12 / 8 (§2 commands) |
| G7 | corpus range | `corpus/README.md`: free-tier entry covers rounds 6–17 | Entry records 6–9 only; loops 2–3 marked pending |

No side was edited. G4 and G2 match the lane's own named debt; G1 and G3 are fleet-file staleness; G5 is resolved by mission precedence in the lane's record but the generated prompt remains a contradicting artifact.

---

## 5. Contract defects

| # | Defect | Evidence / command | Owner / note |
|---:|---|---|---|
| D1 | All 18 corpus entries lack `source:` / `verified-at:` / `recheck:` frontmatter | `grep -lE '^source:' … \| wc -l` → 0; same for the other two (§3) | Wave-2 contract sync; no lane edit this wave |
| D2 | `PROVINCE.md` has **no** `##` sections — no Core/Frontier/Adjacent structure | `grep -cE '^## ' PROVINCE.md` → 0; labels are bold (`**Domain:**`, `**Owns…**`, `**Refuses:**`, bold write boundary) | Structure mismatch vs campaign ground; content itself is strong |
| D3 | SCORECARD depth row stale: 323 lines vs 342, 11 signatures vs 12, 14-step checklist vs 8 | `wc -l SKILL.md`; §2 counts | Mitigated by banner; still an index-row claim |
| D4 | 11 corpus lines cite dead `PROVINCE.md:22-26/22-30` or wrong probe anchors | `grep -rnE 'PROVINCE\.md:(22-26\|22-30)' corpus/ \| wc -l` → 8 (6 in `cross-lane-scope.md`, 2 in `round-1-safety.md`); `grep -nE 'kama-probe\.sh:(47-48\|386\|338-350)' corpus/knowledge/endpoint-identity.md \| wc -l` → 3 | Write boundary is at `PROVINCE.md:45-49`; timeouts at probe `:62,:107-108`; `/v1/models` send at `:418`; `normalize_id()` at `:371` |
| D5 | `cross-lane-scope.md` ownership rows still assert deleted consumers as current (opencode provider block, `agents/janitor.md`, `agents/distiller.md`, `~/.local/bin/the-janitor`, `qwen-coder.service`) with no errata marker | `wc -l ~/.config/opencode/opencode.json` → 5; `ls ~/.local/bin/the-janitor ~/.config/opencode/agents/janitor.md` → both absent; rows at `cross-lane-scope.md:12,13,14,15,17,47` | KQ3 class; round-5 fixed SKILL only |
| D6 | `drift-timeline.md:24` says "the current `~/.config/opencode/opencode.json:158`" — file is 5 lines and has no provider block | `wc -l ~/.config/opencode/opencode.json` → 5; `grep -n 'current.*opencode.json:158' corpus/knowledge/drift-timeline.md` | KQ3 class; dated section, present tense |
| D7 | `probe-mutation-matrix.md:3` present-tense false claim (repo "currently has no" probe/registry) | `grep -rn 'currently has no \`tools/kama-probe.sh\`' corpus/` → 1 hit | KQ3 class |
| D8 | `lessons/*.md` gate sections missing in 7/9 lessons | `grep -LE '^## Gate' corpus/lessons/*.md` → 7 paths | Includes `round-1.md`, `round-2.md`, `round-4-recensus.md` |
| D9 | Round-3 fleet report absent; fleet ledger round-2 row stale (G1/G4) | `ls ../.ufo/reports/round-3/kama.md` → No such file; `ls -l ../.ufo/reports/round-2/kama.md` → 9,909 B | Fleet integrator; lane names the debt |
| D10 | Free-tier index row claims rounds 6–17; entry measures 6–9 | `sed -n '/^## Coverage map/,$p' corpus/README.md \| grep free-tier`; status board §3 | KQ8 class |
| D11 | One uncommitted change: `.ufo/round-10/` (2 files) — a pre-registered, unexecuted plan (`dispatch_utc: null`, no telemetry, empty `audit/`, `gates/`, `tps-probes/`) | `git status --porcelain=v1 -uall` → 2 `??`; `find .ufo/round-10 -type f` → 2 | Report only; never touched |
| D12 | Bloat skew: `.ufo` 2,723,079 B vs `corpus` 190,961 B; largest items are ignored interactive-session logs (1,593,314 B + 882,353 B); round-5 wave artifacts 160,282 B combined | `du -sb .ufo corpus`; `find .ufo -type f -printf '%s %p\n' \| sort -rn \| head`; `ls -l .ufo/round-5/wave-*.json` | `.ufo/interactive-sessions/` is gitignored (`.gitignore` 1 line), disk-only |
| D13 | LOG heading namespace inconsistent: duplicate `round-1` (`:7`, `:273`), `## 4 —` unnumbered style, conformance entry between rounds 5 and 6 | `grep -nE '^## ' LOG.md` | Process defect; G2/G4 class |
| D14 | `SHONEN.md` 4/4 rows `[~]` — no independent promotion verifier | `grep -c '\[~\]' SHONEN.md` → 4 | Intentional honesty, not a defect; promotion remains unverified |

Size inventory for the record: `SKILL.md` 342 lines / 25 KB, `LOG.md` 514 lines / 31 KB, `SCORECARD.md` 188 lines, `PROVINCE.md` 52 lines, `corpus/README.md` 77 lines, `QUALITY.md` 20 lines, probe 1,092 lines, harness 171 lines, registry 36 lines, `DELTA.md` 22 lines, `latest.tsv` 4 lines — `wc -l` over the named files.

---

## 6. Proposed round

Round number: **10** (reuse/supersede the untracked, unexecuted plan) or **11** if the integrator counts plan files as an attempt. Start revision: `35e9175` + the untracked round-10 plan. The proposal deliberately drops the plan's seat-counted claims (its counting inputs, `.ufo/round-10/audit/*.json`, never materialized) and replaces them with self-contained commands.

### Claim A — freshness (lowest LIVE axis, score 7)

**Claim.** The active runbook sample and the tracked invocation baseline are refreshed from dated evidence, not inherited prose: the active sample date advances from 2026-10-15 to the round date, the documented summary matches the run's own summary on all four fields, and the tracked baseline advances from `20261014T124232Z` to a same-day snapshot id with a byte-stable re-run.

- **Before:** `head -1 registry/history/latest.tsv` → `#@snapshot_id 20261014T124232Z` (5 days old on 2026-10-19); `SKILL.md` §Current sampled state dated 2026-10-15; last executed `check` is the 2026-10-15 sample (4 fields, 0 mismatches).
- **After:** `bash tools/kama-probe.sh check --json` (real exit captured separately) + `bash tools/kama-probe.sh snapshot`; `head -1 registry/history/latest.tsv` shows the new dated id; a second `snapshot` run reports `transitions=0` and leaves `latest.tsv`/`DELTA.md` byte-identical.
- **Counting command:**
  ```sh
  before=$(head -1 registry/history/latest.tsv)
  bash tools/kama-probe.sh check --json > /tmp/kama-check.json; rc=$?
  bash tools/kama-probe.sh snapshot > /tmp/kama-snap1.txt; snap_rc=$?
  after=$(head -1 registry/history/latest.tsv)
  bash tools/kama-probe.sh snapshot > /tmp/kama-snap2.txt; snap2_rc=$?
  bash tools/test-snapshot.sh | tail -1
  tail -1 /tmp/kama-snap2.txt
  printf 'baseline_before=%s\ncheck_exit=%s\nsnapshot_exit=%s\nbaseline_after=%s\nsnapshot2_exit=%s\n' \
    "$before" "$rc" "$snap_rc" "$after" "$snap2_rc"
  ```
- **Verifies if:** `rc` equals the expected gate status for the sampled state (2 for drift, 0 for clean), the summary comparison is `fields_checked=4 mismatches=0`, `baseline_after` is a new same-day id, and the second snapshot's final line reports `transitions=0`.
- **Does not claim:** endpoint restoration, continuous monitoring, or a new positive control. If all rows remain `DEAD`, the claim is still true and the round says so.

### Claim B — coverage (score 8; distinct axis)

**Claim.** Corpus provenance becomes machine-checkable under the wave contract: every knowledge/lesson entry carries `source:`, `verified-at:`, and `recheck:` lines with real locations and cadences.

- **Before:** `0 / 18` entries carry each field (`grep -lE '^source:' corpus/knowledge/*.md corpus/lessons/*.md | wc -l` → 0; same for `^verified-at:`, `^recheck:`).
- **After:** `18 / 18` for all three fields; an entry with no live source states `source: none — historical record` rather than inventing one; `recheck:` is a date or cadence (`90d`, `on-release`) matching `SOURCES.md` practice.
- **Counting command:**
  ```sh
  for f in source verified-at recheck; do
    printf '%s %s/%s\n' "$f" \
      "$(grep -lE "^$f:" corpus/knowledge/*.md corpus/lessons/*.md | wc -l)" \
      "$(find corpus/knowledge corpus/lessons -name '*.md' | wc -l)"
  done
  ```
- **Verifies if:** all three lines print `18/18` and a reviewer sample confirms the cited location resolves for every entry admitted after the change (historical entries may cite their own dated evidence).

### What serves the claims

- **Claim A** is served by queued `SOURCES.md` rows for (i) the llama.cpp server HTTP API (`/v1/models` shape and id semantics) and (ii) systemd user timer semantics for the operator-owned cadence question; no lane file may install a unit.
- **Claim B** is served by an own-work contract row: `QUALITY.md` + the wave `SOURCES.md` contract; this is a contract-conformance move, not new domain art.
- Candidate knowledge-entry slots created by the round: `citation-anchor-recheck.md` (the mechanical sweep and its count), `provenance-contract.md` (field values, cadence choices, and no-invention rule). Neither exists today.

### Acceptance and non-goals

Every claim must verify with its own pasteable command; no axis may be harmed; rejected candidates are recorded with reasons. Non-goals: service restoration or unit creation, registry expected-value changes, timer installation, route/credential work (kumitate/kagi/operator), sibling-repo writes, `.ufo/round-10` cleanup (report only), push. Round 10's plan files stay untouched unless the round owner explicitly adopts them.

---

## 7. Limits of this dossier

- [INFERENCE] Axis scores are inherited self-assessments; I measured their evidence artifacts, not their truth.
- No live endpoint sample was taken. Current endpoint state is **not** asserted; the last recorded sample (2026-10-15, all three rows `DEAD`, exit 2) is cited as history.
- No fleet ledger edit, lane file edit, commit, or push was performed. The one uncommitted change (`.ufo/round-10/`, 2 files) is reported, not modified.
- Web research was not needed for STATE; there are no source rows and no tier counts.
