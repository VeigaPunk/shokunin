# STATE dossier — lane `tsukuroi` (host operability & system repair)

kaika W1 · 2026-10-19 · author W1StateTsukuroi · read-only wave: the only writes were `/tmp`
scratch and this artifact. The census re-run (§2) is the lane's own read-only instrument; its
zero-mutation contract was re-asserted (`git status` byte-identical before/after, `db.lck` absent).

## 1. Identity

- **Domain:** host operability & system repair (繕, mending) — "the OS substrate itself: package
  state, systemd, drivers/firmware, boot health" (`PROVINCE.md:3-4`). Boundary: read-only
  detection and report; never installs/upgrades/removes/restarts (`PROVINCE.md:16-17`, `MINT.md:18-19`).
- **Rank:** shonen, probation; **roster row withheld** — `grep -c '"id": "tsukuroi"' MANIFEST.json`
  → **0**; fleet mint entry (round 0, 2026-10-14): "Probation >=3 verified rounds; roster row
  withheld." (`MANIFEST.json` tsukuroi mint notes). `MINT.md` records the rejected-fit scan
  (kama/kagi/kaidoku/revenger refuse; OS substrate unowned).
- **Git:** branch `master` == `origin/master`; HEAD `9b70381c54a040e8775b43a61245b088acefb65f`
  (2026-10-17 00:28:34 -0300) "tsukuroi: fleet-r1 adjacency handoffs knowledge + lessons +
  PROVINCE/SHONEN/SKILL/README sync"; tree clean (`git status --porcelain=v1 -b` → branch line
  only). Lane identity held: last 6 commits all `tsukuroi-shokunin <tsukuroi@shokunin.local>`.
- **Last round: 11 — fleet hint verified.** Lane `LOG.md` records rounds 0–11 (362 `wc -l`);
  `SCORECARD.md` move log rows 1–11 + final axes table "landed round 11" (`SCORECARD.md:21-52`);
  fleet `MANIFEST.json` `rounds[]` carries tsukuroi entries **2–11** (10 `train`, all 2026-10-14;
  lane round N = training r(N−1)) + the round-0 mint. **Lane round 1 (scribe entry) has no
  MANIFEST row** — integrator-owned ledger gap, reported not repairable here.
- **Next round: fleet round 1 (interactive continuation), not historical 12.** `SCORECARD.md:59-63`:
  "Continue pending **fleet round 1**; do not relabel it historical round 12 or reuse historical
  training round 1." Driver counter `.ufo/state/tsukuroi.round` = **1**. The handoff knowledge
  landed 2026-10-17 (9b70381); the round is still **unadmitted** — 0 newly verified rounds,
  blocked on ROUTE-BINDING (operator routing) + non-author verification (`.ufo/l0-questions.md`,
  2 rows: ROUTE-BINDING, RECEIPT-BINDING).
- **Promotion state:** `SHONEN.md` 4 boxes all `[~]` (asserted with evidence pointers; `[x]` owed
  to a named non-author reviewer). Template-conformant: box text byte-matches the canonical seed
  (`PROTOCOL.md:429-432`), marks confined to the box character + one indented evidence line per box
  (`PROTOCOL.md:417`).

## 2. Axes

Final self-assessment landed round 11 (`SCORECARD.md:39-52`); each score carries its counting
command there; none retired (`SCORECARD.md` §Planned / retired: "retired: none — no axis
saturated").

| Axis | Score | Evidence pointer (as landed) | Last change |
|---|---|---|---|
| depth | 8 | 24 notes + census 2402 `wc -l` / 80 executed cases; ceiling: r8's 9 un-exercised clause sites; lessons never written | r4 |
| coverage | 8 | 6 `PLANE` emitters == 6 rollup keys (`tools/tsukuroi-census.sh:2377-2392`); ceiling: PROVINCE Core/Frontier/Adjacent not landed (since landed, 9b70381) | r9 |
| operability | 9 | selftest rc=0 80/80; live rc=1 six-plane rollup; zero-mutation held; ceiling: D12 `--identity` not landed | r11 |
| freshness | 8 | every round re-ran predecessor pins; 3 receipts; ceiling: live captures drift; r10 receipt pins superseded in-commit (recorded) | r6 |
| calibration | 9 | `calibration-synthesis.md` (463 `wc -l`) claim→re-measure→append→supersede loop; ceiling: D13 verification debts open | r10 |
| **adjacency** | **7** | reported-not-absorbed rows across the arc (`closeout-r11.md` §3.2; PROVINCE ADJ-01..07); ceiling: "no formal overlap table" | r5 |

- **Lowest non-retired axis: adjacency (7)** — the AXES.md obligation ("At least one claim works
  the lane's **lowest-scoring non-retired axis**", `AXES.md:33-34`) points here.
- **Saturation line: undeclared.** `SCORECARD.md:166-170` §Saturation is the 2026-10-16 rollout
  placeholder ("to be declared by the lane on its next round"); the stagnation nudge
  (`AXES.md:66-72`) is therefore idle. Stagnation window N: undeclared.
- **Capabilities count: 0** — `SCORECARD.md:157-163` table reads "— none yet —"; per `AXES.md:57-64`
  rows enter only through a round that demonstrates the capability (no retro-fill).
- **Planned claims:** historical "planned: none" (ladder ended) superseded by the appendix:
  "continue the pending adjacency move in a fresh authorized L1 session after ROUTE-BINDING is
  cleared" (`SCORECARD.md` appendix, planned-current).
- **Live gate state today** (re-run by this dossier, 2026-10-19T21:02:27Z, non-root):
  `bash tools/tsukuroi-census.sh --selftest` → rc=0, `TSUKUROI_CENSUS_SELFTEST: PASS (80 cases,
  80 passed, 0 failed)`; `bash tools/tsukuroi-census.sh` → rc=1, `TSUKUROI_CENSUS: DEGRADED
  (packages=DEGRADED systemd=HEALTHY drivers=DEGRADED journal=DEGRADED update-safety=DEGRADED
  oom=DEGRADED)`. Census md5 `945c76fc6cc548e47b91c23a9637df75` == the round-10/11 pin (identity
  stable). **Two arms fired in production:** oom watch `new=7` kill clusters (2026-10-18 14:46 →
  2026-10-19 00:33, C1_kernel=1, C2_events=16, C3_events=5) and update-safety `REQUIRES-PREP`
  (candidates=430, join_behind=414, `-Sy` refresh 2026-10-18). Zero mutation confirmed.

## 3. Corpus

- **knowledge: 25 md + 1 json** — `ls corpus/knowledge/*.md | wc -l` → 25;
  `ls corpus/knowledge/*.json | wc -l` → 1 (`adjacency-handoffs-fleet-r1.json`, the 7-route
  handoff ledger with source pins + lifecycle vocabulary).
- **lessons: 1** — `ls corpus/lessons/*.md | wc -l` → 1 (`round-1.md`, the *fleet-round-1* lesson,
  2026-10-15, with `## Gate` + 3 rejected candidates). Historical rounds 1–11 have no lessons —
  the closeout's own rule: "no retro-fabrication — a Gate for closed rounds would invent
  decisions" (`closeout-r11.md` §3.2).
- **QUALITY.md criteria: 5** — `grep -cE '^[0-9]+\.' corpus/QUALITY.md` → 5 (falsifiable;
  source-cited; obs/inf/unk separate; errata append-only; rejection kept). Probation draft.
- **Coverage map: 10 rows** — `grep -c '^| `' corpus/README.md → 10; `## Frontier` present
  (3 bullets). `PROVINCE.md`: Core 5 owned surfaces (+ oom/memory prose), Adjacent 7 rows
  (ADJ-01..07 with minimum-evidence + ownership-source columns), Frontier 2 bullets. All 8 cited
  sibling `PROVINCE.md` files exist and every cited line-range resolves (checked per file).
- **Frontmatter health (contract keys):** 6/25 notes missing all three literal keys —
  `grep -L '^source:' corpus/knowledge/*.md | wc -l` → 6 (`package-state-plane`,
  `systemd-user-plane`, `driver-firmware-plane`, `update-safety-note`, `executor-test-sufficiency`,
  `memory-arm-mutants-s8`); 5 more lack `verified-at:`+`recheck:` (`aur-risk-plane-ver-s6/s7`,
  `memory-arm-ver-s8`, `update-safety-v2/v3`). Open since round 1 ("literal
  `source:`/`verified-at:`/`recheck:` keys", LOG round-1 Open list); the 2026-10-17 sync did not
  close it.
- **recheck: shape deviation:** every populated `recheck:` is a section pointer or command, never
  a date/cadence — `grep -h '^recheck:' corpus/knowledge/*.md | grep -cE '[0-9]{4}-[0-9]{2}-[0-9]{2}'`
  → 0. The overdue-recheck check (before 2026-10-19) is **uncomputable**; wave 2's SOURCES.md
  contract expects date-or-cadence.
- **Stale refuted claim still standing:** `corpus/README.md:13` (journal-boot row) still reads
  "failed-service history **0 unit failures in 13 retained boots**" — r4 corrected this to 4
  capitalized-pattern records (`LOG.md:176`). The 2026-10-17 commit touched `corpus/README.md`
  without sweeping the superseded claim — `PROTOCOL.md:348-350` ("Corrections sweep every
  mention") violated.

## 4. Mistakes (mined)

| # | Class | Evidence | Captured? |
|---|---|---|---|
| M1 | Measurement-method errata ×4 (sync-db mtime→birth; journal lines→entries; unit-file count 136→133; rollback-net inference retracted) | LOG round-1 entry; SKILL errata blocks | Yes — QUALITY #2/#3; SKILL journal field map + printed traps (D10) |
| M2 | md5-prefix transcription candidate (`7a3d3b94ed…` vs `7a3d3b94ec…`) | LOG round-2 Open list | Yes — QUALITY #4 append-only; recorded-not-rewritten |
| M3 | Overbroad negative claim without sweep ("0 unit failures in 13 boots" → r4 found 4 records) | `LOG.md:96` vs `LOG.md:176` | **Partial** — D2 empty-proof + `calibration-synthesis.md` §1 cover the shape, but SKILL.md has **no literal negative-claim-sweep rule** (`grep -c negative SKILL.md` → 0). Propose: "a negative claim carries its sweep" as a standing rule |
| M4 | Unresolvable recorded item ("20-min cap" recorded-not-invented; owner integrator) | `executor-test-sufficiency.md` §7 U1; carried in every errata since | Yes — carried-debt discipline; still open |
| M5 | Hardening gap honestly recorded (own sweep 13/23 killed; hardening closed 1/4 of tameshi's survivors) | LOG round-5; `SKILL.md:578-609` | Yes — two-author two-pins rule (`SKILL.md:706-709`) |
| M6 | Admitted arm without non-author verification (r7 memory arm → AUD-X7, closed r8 VER-S8) | `LOG.md:178-179`; `memory-arm-ver-s8.md` | Yes — D13 "attested ≠ verified" (`SKILL.md:1473-1476`) |
| M7 | Count/credit restatement drift ("5-plane" vs realized 3→4→5(uncommitted)→6; AUD-X7 credit misattributed to r9) | `LOG.md:172-173`; appended precision `LOG.md:226-231` | Yes — D3 counts-move-together; append-only precision. Wording repair still owed as a new LOG entry |
| M8 | Markdown table malformation persisting r4→r11 (SCORECARD rows 16/21/22 unmatched `(`) | `closeout-r11.md:249-254`; AUD-S11 O3 | Yes — repaired r11; the escape-the-pipe reading adjudicated and **rejected** (gate disagreement) |
| M9 | Sweep attestation-only (r10's 6/10 kill figure lives in a code comment; no landed sweep note; independent replay owed) | `SKILL.md:1498-1504` | Yes — D13; replay still open |
| M10 | 18-vs-19 `-Qkk` summary split (`cups-browsed` `\r` interleave) unresolved | `SKILL.md:232-235` "Resolve by root re-run; do not reconcile by hand" | Yes — carried debt (elevation-gated register row 1) |
| M11 | **NEW (this dossier):** 2026-10-17 sync commit `9b70381` landed 8 files with **no LOG.md entry** — `git show --stat 9b70381` lists no LOG.md; `AGENTS.md:3`: "Every change appends a `LOG.md` entry with motivating evidence." | Not captured anywhere. Propose QUALITY criterion: a landing commit and its LOG entry land together (or the entry names the commit hash before push) |
| M12 | **NEW (this dossier):** corrections-sweep miss on the same commit (§3 stale row above) — fleet rule exists (`PROTOCOL.md:348-350`) but no lane-side QUALITY criterion mirrors it. Propose adding it |

**Gate disagreements / rejections kept (evidence of taste):** the r11 paren-repair adjudication
(plan's reading rejected with reasons, `LOG.md:223-226`); the L4 no-retro-fabrication refusal;
the 2026-10-15 receipt-mint refusal (no synthetic taskKey — `LOG.md` 2026-10-15 addendum);
`lessons/round-1.md` Gate's three rejected candidates (GPU≠endpoint readiness; "background-noise"
wording ≠ measured threshold; inherited edits ≠ this session's authorship) plus its honest
"no independent non-author admit/reject spot-check obtained".

## 5. Contract defects

1. **SKILL.md frontmatter non-conformant** — `SKILL.md:1-4` description is
   "Domain specialist — host operability & system repair. Rank: shonen (probation)." —
   capability-and-scope-only. `PROTOCOL.md:414` requires "quoted trigger strings, an anti-trigger,
   and a sibling-arbitration note — capability-and-scope-only descriptions misroute."
2. **Sync commit without LOG entry** (M11 above) — `9b70381`, 8 files, no `LOG.md`.
3. **Stale refuted row in README** (`corpus/README.md:13`, M12 above).
4. **11 notes with missing/partial frontmatter keys** (§3): 6 all-three missing, 5 missing
   `verified-at:`/`recheck:` — `grep -L '^source:' corpus/knowledge/*.md | wc -l` → 6.
5. **recheck: never a date/cadence** — 0 date-form values; overdue-recheck uncomputable (§3).
6. **Saturation line + stagnation window N undeclared** (`SCORECARD.md:166-170` placeholder) —
   owed "on its next round" per the 2026-10-16 rollout; still open two commits later.
7. **Capabilities table empty** (`SCORECARD.md:157-163`) — despite demonstrable repertoire
   (census gate operation r2+; mutation-hardening r5/r10; e2e host-health report r3; AUR/OOM
   watch arms firing in production — today's capture).
8. **Round-11 contract debts still open:** L1 runbook (`HANDOFF.md` never landed;
   `closeout-r11.md` is the realized reader artifact), L4 `corpus/lessons/round-11.md` absent
   (lessons = 1 file, fleet-r1 only), L9 non-author runbook test unrun, D13 verification debts
   (r9 planes' non-author verification; six `(S10-2)` covering claims; tameshi B7/B8/B9;
   post-append no-oral-context re-test) — `plans/completion-evidence.md` §3/§5.
9. **Scratch-only verification evidence:** LOG round-11 cites VER-S11's verdict at
   `/tmp/w11-ver-s11/VERDICT.md` — unresolvable for a fresh session; `PROTOCOL.md:341-342`:
   "An evidence pointer must resolve at *closure* time, not only at write time." Substance
   partially preserved in LOG prose (H4/H4-S2 mutant cells, poll timeout); the pointer itself is dead.
10. **Dead l0 evidence pointer:** `.ufo/l0-questions.md` RECEIPT-BINDING row cites
    `/home/vgpnk/Projects/shokunin/.ufo/interactive-l1-20261015T050057Z/launch-tsukuroi.json` —
    absent today (the dir holds only empty `prompts/` and `surface/`; removal plausibly souji's
    2026-10-18 receipt-gated cleanup [INFERENCE]). Routing substance survives committed at
    `.ufo/evidence/fleet-r1-interactive/routing.json`.
11. **Fleet-ledger gaps (integrator-owned, report-only):** MANIFEST tsukuroi rounds 2–11 carry no
    `commit`/`report` fields (other lanes' entries do); no fleet-root `.ufo/reports/round-N/tsukuroi.md`
    for N=1..12 — the fleet-round-1 report is lane-local by the DELIVERY-SCOPE debt, awaiting
    integrator forwarding; lane round 1 has no MANIFEST row.
12. **Bloat (sizes with commands):** `wc -c SKILL.md` → **144 943 B** — largest in fleet
    (`wc -c */SKILL.md | sort -rn` in fleet root: next tabi 125 194 B); append-only per-round
    appends keep every superseded pin in place (design tension, not corruption — D3/D5 keep it
    navigable). `wc -l tools/tsukuroi-census.sh` → 2402 (126 075 B) — a 2.4k-line bash gate.
    `du -b corpus/knowledge` → 602 641 B; `du -b plans` → 325 563 B (18 files incl. ten 20–44 KB
    record drafts); tracked total 1 443 490 B across 86 files; `.ufo/interactive-sessions/`
    2.7 M on disk, gitignored (`.gitignore:1`).
13. **Required files:** all present (`SKILL/PROVINCE/LOG/SHONEN/AGENTS/corpus{README,QUALITY,
    knowledge,lessons}/SCORECARD` + `MINT.md`); `SHONEN.md` seed block template-conformant;
    **uncommitted changes: none** (clean, synced); lane identity held on all commits.

## 6. Proposed round (next dispatch = fleet-round-1 continuation)

Three claims; claim A sits on the lowest non-retired axis (adjacency 7) per `AXES.md:33-34`.

- **Claim A — adjacency 7 → 8: one ADJ route reaches `acknowledged` (or beyond) with a durable
  recipient receipt.** Before (measured): the 7-route ledger defines the lifecycle
  (`adjacency-handoffs-fleet-r1.json:88-94`) but instantiates no state —
  `grep -c '"state"' corpus/knowledge/adjacency-handoffs-fleet-r1.json` → **0**. After: ≥1 route
  carries `"state": "acknowledged"` + receipt path —
  `jq '[.routes[] | select(.state=="acknowledged" or .state=="accepted" or .state=="resolved")] | length' corpus/knowledge/adjacency-handoffs-fleet-r1.json` ≥ 1.
  Serves: SOURCES.md rows for the 8 pinned sibling provinces (own-work kind); a new
  handoff-closure knowledge entry; the lane's own planned move (SCORECARD appendix).
- **Claim B — calibration/operability: the post-append no-oral-context re-test lands** (owed since
  r3; SHONEN box 3 keeps the pre-fix tally). Before: the only tally is against the round-2
  revision — 7 SUFFICIENT / 3 PARTIAL / 3 MISSING (`executor-test-sufficiency.md`; README row:
  "post-fix re-test not yet run"). After: a new note tallies the 1636-line SKILL with **0 MISSING**
  on the six-plane gate steps — `grep -c 'MISSING' <new-note>` → 0. Serves: D13 partial closure,
  SHONEN box 3, a SOURCES.md study path (SKILL → census → notes).
- **Claim C — freshness 8: corpus hygiene + contract fields.** (i) Append literal
  `source:`/`verified-at:`/`recheck:` key blocks (with re-verified dates) to the 11 deficient
  notes — `grep -L '^source:' corpus/knowledge/*.md | wc -l` 6 → 0. (ii) Append a correction entry
  to `corpus/README.md` naming the r4 refutation of its `:13` row (text stays; append-only) —
  `grep -c 'r4-refuted' corpus/README.md` 0 → 1. (iii) Declare the saturation line + stagnation
  window N in `SCORECARD.md` §Saturation and add the first capability row (the oom watch firing
  in production, today's `new=7`) — `grep -c 'none yet' SCORECARD.md` 1 → 0. Serves: wave-2's
  SOURCES.md `used-by` integrity; the stagnation-nudge machinery; QUALITY.md criteria from M11/M12.

Round record discipline: the round's own lesson lands with it (`ls corpus/lessons/*.md | wc -l`
1 → 2) — organic, no retro-fabrication.

## 7. Counts (wave rollup)

- SOURCES rows: **0** (STATE scope — no web research in this dossier; ART scouts own that).
- Corpus held: knowledge **25 md + 1 json**; lessons **1**; QUALITY criteria **5**; coverage rows
  **10**; ADJ handoff rows **7**; capabilities **0**; axes scored **6/6** (none retired).
- Mistakes mined: **12 classes** (M1–M10 historical, M11–M12 new) + 4 kept rejections/gate
  disagreements.
- Defects found: **13** (§5), of which 3 are new findings this session (M11, M12, defects 1/9/10).
- Gate re-run today: selftest **80/80 rc=0**; live **rc=1 DEGRADED** (oom newly DEGRADED,
  update-safety REQUIRES-PREP); zero mutation confirmed; census identity pin stable.
