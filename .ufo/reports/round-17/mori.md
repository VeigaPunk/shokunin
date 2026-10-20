# mori — round 17 (attempt 1)

## Work performed

Declared claims: **C1 coverage** — acquire bounded terminal-at-scan transcript observation;
**C2 operability** — branch-authoritative jj census and identity diagnostics;
**C3 calibration** — repair the known blind fleet-root misroot sweep. Calibration **5** is a
lowest non-retired score; all scores are held. C3 was explicitly added after build reconnaissance
and before L1 measurement to correct the initial “lowest owned axis” reading, not silently waived.

**L1 verdict: all three claims verified at their finite exercised scopes; no observed axis harm.
Independent non-author admission remains pending. Execution is not fully conformant.**

- C1 delivers `tools/mori-seat-terminal.py`: schema-3, descriptor-relative/no-follow reads,
  strict selective JSON projection, settle/unknown-age handling, relative identities and exact
  prefix filters. Unknown vendor causes remain unknown; numeric code metadata honors the original
  contract. Evidence: `corpus/knowledge/seat-terminal-status-r17.md`,
  `.ufo/waves/round-17/evidence/final/seat-after-fixed/run-manifest.json` (**66/66**).
- C2 fixes `tools/mori-census.sh`: jj lanes require the helper's `lane.branch` mirror; missing
  authority is unavailable, never HEAD progress. `HEAD_BRANCH_MISMATCH` and
  `LANE_AUTHOR_MISMATCH` are warn diagnostics, including young rounds; legitimate sibling authors
  are controls. Git trace/config child overrides are scrubbed. Evidence: the **17 real git/jj
  scenarios / 204 assertions** in `evidence/final/jj-after/run-manifest.json` under the round root.
- C3 delivers `tools/mori-misroot-sweep.py`: no-pathspec filename-or-content detection, never
  relocation/remediation. A precommitted exact 847-byte `MoriR16.Lesson`, token-bearing tracked
  control and sibling control are hashed before/after. Evidence: `frozen/c3-final-expected.json`,
  `evidence/final/c3-fixture-setup.json` and `c3-assertions.json` under the round root.
- Frontier/teaching: two sourced knowledge entries, eight new source rows, QUALITY Q43–Q50,
  append-only r16 M7/misroot precision, closure/version supersessions in PROVINCE, corpus index
  and r16 window note. Evidence: `corpus/lessons/round-17.md`, `corpus/lessons/round-16.md`
  appended correction, `corpus/knowledge/journal-cursor-window-r16.md` appended correction.
- Fresh falsification caused real corrections, not a clean first pass. Retained failures include
  the background-clause survivor, census trace-simulator false positive (**131/132**) and C1
  independent long-code metadata failure (**65/66**). Final census **134/134**, terminal **49**
  arms, other named selftests, oracle **28/28**, r13 **24/24**, r14 **44/44**, r15 **63/63** with
  frozen red **34/34** pass. Evidence: `evidence/final/` and lesson M15–M20. Seven historical
  instrument/pin bytes are unchanged; r10 remains red debt without a live drift re-run or re-pin.
- Detection-only handoffs: `/var/log/pacman.log:2462` records 09:15:30 `-Syu` (448 actions),
  `:3161` records 13:23:08 `-U zcode`. `build/PacmanActorTrace.md` correlates the former's command
  stream/invocation UUID to another OMP session; human actors/authorization remain unknown or
  inferred. OS diagnosis/recovery stays tsukuroi/operator-owned. The fresh live transcript receipt
  sees **469** scoped observations, **94** aged rate-limit errors (**93 zai/glm-5.3-flash,
  1 anthropic/claude-opus-5-5**) and **90** retry-exhausted records. Per-prefix aged errors are
  TabiR17 **22**, TsukuroiR17 **44**, SoujiR17-3 **28**. These are last-observed states, not
  permanent deaths, incidents, endpoint health or a routing decision. Evidence:
  `.ufo/waves/round-17/evidence/final/seat-live-final.json` (explicit canonical path redaction).

### Swarm and conduct

Both policy-v2 waves were validated and dispatched as exactly one unchanged `taskCall` each:

| Wave | Seats | Role mix | Reports | Reported dead |
|---|---:|---|---:|---:|
| Build | 70 | scout23, executor7, scribe13, reviewer12, connector6, critic4, revenger3, sentinel2 | 70/70 | 0 |
| Fresh falsify | 64 | scout17, executor3, scribe3, reviewer27, connector4, critic4, mutation-tester4, sentinel2 | 64/64 | 0 |

**134 unique seats**, no replacements. L1 MoriR17 holds the canonical planner seat (validator
excludes planner). Four all-70 and three all-64 job-cap refusals spawned nothing; the same payloads
were retried at the required backoff, never split/shrunk. Original writer identities resumed in
separate observed-base clones; L1 alone integrated. Specs, receipts, assignments, registries and
role counts are in `.ufo/waves/round-17/`, especially `wave-settlement.json`.

Initial unauthorized/unscoped seat actions remain disclosed: unflagged lane jj reads and one
snapshot, pre-guard ad hoc sandbox writes, `/tmp` residue/reads, overbroad transcript/config/actor
reads, one forbidden record-class display, and L1's initial overbroad seat-selftest authorization.
No values from that forbidden display were admitted. See lesson M8–M20 and
`falsify/ConformanceAudit.md` V1–V15, including inferred and non-violation dispositions. Final
correction writers were explicitly forbidden test execution; L1 ran committed tools in isolated
verification clones. Static context checks are not runtime prevention. All owned clones and
transient copied sessions are removed after retaining artifacts (394 byte-exact mutation files,
132 delivered streams, revision attestations and replay inputs).

Migration disposition: census HEAD grading is fixed. Historical r13–r16 gate HEAD fields remain
commit-context metadata, **not landed-branch identity**; old env/output-guard residuals are
explicitly retained rather than changing historical instruments. They were exercised only in
clean isolated clones/safe outputs; new branch/hash wrappers pin the measured inputs. Helper
metaedit remains the only live commit path; only final `landed` hashes are cited. Details:
`corpus/knowledge/jj-branch-anchor-r17.md` and lesson migration dispositions (JjAuditMori F3/F4,
F10/F12; JjTrialMori H1–H5).

Stale-lane: age **10166 s** from the 15:26:16 launch, beyond two 450-second ticks but **progressing**
through landed work/evidence; respawn-per-round, no other mori mission open and no next round
initiated. Tool installs/updates: **none** by L1 or seats. New L0 questions: **0**. No package
transaction, service action, routing change, MANIFEST edit or promotion by this lane.

## Landed changes

All child work is committed and pushed. Each row is tied to a LOG.md entry:

| Citable landed hash | Changes | LOG.md entry |
|---|---|---|
| `273aa74ab73701f41fea38ec7bd1c47b4b2bfbc7` | initial tools, source/corpus corrections and build evidence | Round 17 — declared observation/provenance/calibration moves |
| `5c1dfb8d0530c74eb0e1630c2b522b735b486274` | first measurements and fresh falsification preparation | Round-17 first landing and executed measurements |
| `2be82940828424ef4a2d623173d7e603b8a18f93` | A2 source/fixture/guard corrections, fresh reports, precommitted C3 controls | Round-17 fresh falsification and A2 correction landing |
| `fe9fa9083db998ead1554459d656568c4173f288` | realistic Git-only trace simulator and positive/negative controls | Corrected-input landing and actual final-check failure |
| `91940fa339e38006f8db5bd7d78bb6f037f4d016` | complete numeric metadata, unchanged independent expectation | Final C2 pass and independent C1 metadata failure |
| `dcb2eea26d8dff0485b1cd0a9402fa63af82cb99` | final successful measurements, criteria/scorecard, exact evidence and cleanup | Round-17 final verified measurements and cleanup |

Final authoritative state (helper `state`, not bare HEAD):

```text
state branch=master local=dcb2eea26d8dff0485b1cd0a9402fa63af82cb99 remote=dcb2eea26d8dff0485b1cd0a9402fa63af82cb99 ahead=0 behind=0 head=detached tracked=0 untracked=0
```

SHONEN.md and non-author verifier files are intentionally unchanged. No inherited lane dirt was
present at dispatch; operator-authored prior closures/considerthese were left intact.

## Before → after measurements

Counting commands below were executed (all **exit 0**). They read committed retained receipts;
raw before/after gate/probe argv, rc, source hashes and timestamps remain in the wrappers.

### C1 — coverage, score 6→6, improved

Before capability absent at entering `24526ea9617cd020fee16c28fe4d4a2789dc28cb` (cat-file rc128).
Same 66-case / 96-pin table: **66→0** unmet, after **66/66**, gate exits **1→0**. Absence is not
66 historical production defects. After code/input pin: `91940fa339e38006f8db5bd7d78bb6f037f4d016`; before retained gate run `fe9fa9083db998ead1554459d656568c4173f288`.

```sh
jq -s '[.[] | (.summary.capability_absent + .summary.mismatched)]' /home/vgpnk/Projects/shokunin/mori-shokunin/.ufo/waves/round-17/evidence/final/seat-before/run-manifest.json /home/vgpnk/Projects/shokunin/mori-shokunin/.ufo/waves/round-17/evidence/final/seat-after-fixed/run-manifest.json
```

Observed: `[66,0]`. Delivered streams **132/132** match SHA/size (`stream-integrity.json`).

### C2 — operability, score 7→7, improved

Same **204** assertions: **60→0** failed; **7/17→17/17** scenarios match, gate exits **1→0**.
Measured `fe9fa9083db998ead1554459d656568c4173f288`; census/gate/frozen hashes unchanged at final input `91940fa339e38006f8db5bd7d78bb6f037f4d016`. Earlier 21/0 counts
used a weaker conditional denominator and are historical, not the final comparison.

```sh
jq -s '[.[].totals.failed_assertions]' /home/vgpnk/Projects/shokunin/mori-shokunin/.ufo/waves/round-17/evidence/final/jj-before/run-manifest.json /home/vgpnk/Projects/shokunin/mori-shokunin/.ufo/waves/round-17/evidence/final/jj-after/run-manifest.json
```

Observed: `[60,0]`.

### C3 — calibration, score 5→5, improved

Same pinned exact witness/probe: missed known artifact **1→0**, unexpected candidates **0→0**;
tracked token-bearing and sibling controls stay unclaimed. Legacy probe rc0 is a known false
clean; corrected probe rc1 is the required candidate alert. Measured `91940fa339e38006f8db5bd7d78bb6f037f4d016`, with expected/tree/
recipe already committed before the run. All witness/tool/control digests are bound before/after.

```sh
jq -c .missed_unexpected /home/vgpnk/Projects/shokunin/mori-shokunin/.ufo/waves/round-17/evidence/final/c3-assertions.json
```

Observed: `[{"missed":1,"unexpected":0},{"missed":0,"unexpected":0}]`.
Depth/freshness/adjacency are unchanged (5/5/6 held); no observed axis harm at the exercised scope.

## Sources & frontier

SOURCES **40→48**: eight new tier-A rows S041–S048; A **37→45**, B2/C1 held;
mined **19→25**, queued **20→22**, rejected1 held. Six rows are mined by the two new knowledge
entries; Retry-After and LogFile remain queued. No existing status/recheck/used-by or immutable
cell changed, so no existing-row mutable transitions are omitted. Gate quotes, located dates,
search-stop rationale and corrected verbatim text are in `corpus/lessons/round-17.md`.
S043 materially drives vendor-cause precedence; S046 materially drives status1-vs-error handling.

Required census command (executed at start and final close):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori
```

Start output / exit:

```text
mori	W04	S035 duplicate url raw.githubusercontent.com/systemd/systemd/cf8ebfc6159cf0b3b99aa9a0164ccb07c4c9c5af/catalog/systemd.catalog.in across scopes
mori	W04	S037 duplicate url www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html across scopes
mori	ok	/home/vgpnk/Projects/shokunin/mori-shokunin/corpus/SOURCES.md
exit=0
```

Final output / exit:

```text
mori	W04	S035 duplicate url raw.githubusercontent.com/systemd/systemd/cf8ebfc6159cf0b3b99aa9a0164ccb07c4c9c5af/catalog/systemd.catalog.in across scopes
mori	W04	S037 duplicate url www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html across scopes
mori	ok	/home/vgpnk/Projects/shokunin/mori-shokunin/corpus/SOURCES.md
exit=0
```

Executed committed-row/histogram counting command (exit 0):

```sh
python3 -c 'import subprocess,json,collections; r='"'"'/home/vgpnk/Projects/shokunin/mori-shokunin'"'"'; out=[]
for rev in ['"'"'24526ea'"'"','"'"'dcb2eea26d8dff0485b1cd0a9402fa63af82cb99'"'"']:
 text=subprocess.check_output(['"'"'git'"'"','"'"'--no-optional-locks'"'"','"'"'-C'"'"',r,'"'"'show'"'"',rev+'"'"':corpus/SOURCES.md'"'"'],text=True); rows=[[x.strip() for x in l.split('"'"'|'"'"')[1:-1]] for l in text.splitlines() if __import__('"'"'re'"'"').match(r'"'"'^\|\s*S[0-9]{3,}\s*\|'"'"',l)]; out.append({'"'"'revision'"'"':rev,'"'"'rows'"'"':len(rows),'"'"'tiers'"'"':dict(collections.Counter(x[3] for x in rows)),'"'"'statuses'"'"':dict(collections.Counter(x[7] for x in rows))})
print(json.dumps(out,sort_keys=True))'
```

Observed:

```json
[{"revision": "24526ea", "rows": 40, "statuses": {"mined": 19, "queued": 20, "rejected": 1}, "tiers": {"A": 37, "B": 2, "C": 1}}, {"revision": "dcb2eea26d8dff0485b1cd0a9402fa63af82cb99", "rows": 48, "statuses": {"mined": 25, "queued": 22, "rejected": 1}, "tiers": {"A": 45, "B": 2, "C": 1}}]
```

FR14 advances only to passive supported transcript observation; emission/authoritative
orchestration remains kumitate-owned. jj history provenance and blind-root calibration are bounded
mori observation work. FR1 kernel attribution, FR11 aliases/vacuum/cross-boot/completeness and r10
redness remain open qualifications, not new ownership. Final full fleet status had **no pathspec**;
misroot scan found **0 candidates**, no confirmed own-seat artifact to relocate. Driver baselines
were left unmodified; unattributed transient `stdout.toon` was already absent when read, not
claimed or deleted. Evidence: `evidence/final/fleet-status-full.json`, `fleet-misroot-final.json`.

## Trend verdicts

- **expansion: improved** — sourced `seat-terminal-status-r17.md` advances bounded FR14 ground;
  `jj-branch-anchor-r17.md` and the demonstrated repertoire add independently verifiable capability.
- **quality: improved** — stronger finite contracts/metadata, real guard/oracle repairs and stale
  closure/version corrections; both actual failed runs stay retained, old pins/instruments survive.
- **discernment: improved** — prior non-author `ClosureMoriR16` disagreements became precise
  appended lessons and Q43–Q46. Author-wave findings generated Q47–Q50 but do **not** count as
  outside agreement. Current non-author admit/reject closure is still required; no prevention or
  procedural-compliance credit is inferred from these trends.

## SHONEN

Author assessments only; no non-author promotion certification is claimed.

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` Gates/decision rules; `corpus/SOURCES.md`; both new knowledge entries.
- [~] At least one end-to-end domain task executed and logged in LOG.md — final live terminal-at-scan trigger→read→bounded output→handoff in `LOG.md` final entry and `evidence/final/seat-live-final.json`.
- [~] Instructions executable by an agent without oral context — registered CLIs/selftests, pinned fixture tables and `c3-capture-recipe.json`; actual committed L1 receipts in `evidence/final/`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — detection/report boundaries in PROVINCE; package/routing/cleanup owners retained. Scope/privacy deviations remain disclosed, so this is **not** a clean non-author promotion pass.

Path-basis clarification for the pointers above: lane-relative code/corpus paths are under
`/home/vgpnk/Projects/shokunin/mori-shokunin/`; the round evidence root is
`.ufo/waves/round-17/` there. Unprefixed receipt names in measurement paragraphs use
`.ufo/waves/round-17/evidence/final/`; named specs, ledgers and replay recipes are at the round root.
