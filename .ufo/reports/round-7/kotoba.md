# kotoba-shokunin — round 7 report

Commit: `kotoba-shokunin@3b029b8` — "round-7: compressor mechanism
reverse-engineered (cache-or-truncate, 99-char cliff), 3 new checklists,
self-audit cures, drift recount"

## SHONEN

- `[~]` SKILL.md decision tables/error patterns/checklists/cited sources —
  evidence: SKILL.md now carries 4 checklists (trigger-fidelity 13,
  agent-def 9, dispatch-prompt 12, always-on 8), 22-row anti-pattern table,
  Sources updated (asserted — L1-dispatched lanes).
- `[~]` end-to-end domain task — evidence: round-7 dispatch-prompt audit of
  43 files + self-audit, `corpus/knowledge/dispatch-prompt-audit-round7.md`,
  `corpus/knowledge/alwayson-checklist-round7.md` (asserted).
- `[~]` instructions executable without oral context — a second
  blank-context reviewer lane ran the 13-item checklist verbatim on this
  repo's own SKILL.md: 13 verdicts, 4 fails, 3 wording meta-findings, zero
  clarification requests (asserted; lane is still the lane).
- `[~]` no cross-domain bleed — all defects found outside the repo
  (`~/.config/opencode/*`, `.ufo/prompts/`, `scripts/`, sibling SKILL.md)
  reported below, not fixed; PROVINCE.md unchanged (asserted).

## L2 dispatch (MISSION.md floor: 8 — delivered 9, one batched task call)

| Lane | Role | Bucket | Output |
|---|---|---|---|
| RevSkillAudit | reviewer | m_zfl | 13-item checklist verbatim on own SKILL.md: 7/13 clean, 4 fails, 1 ambiguous |
| CriticDrift | critic | m_zfl | durable-claim recount: CLAUDE.md 16→18, warns 10191→10681, rest stable |
| SentinelSiblings | sentinel | m_zfl | all cross-domain defects still present |
| ExecDispatchChecklist | executor | m_flash | drafted 12-item dispatch checklist; applied: 37/43 fail ≥1 item |
| ExecResolvability | executor | m_flash | 46-file reference sweep + generator audit |
| ScoutRenderSurvival | scout | m_flash | compressor mechanism + trigger survival measurement |
| ScoutCatalogueCensus | scout | m_flash | 3911 session_init records, 14 distinct catalogues |
| ConnRoutes | connector | m_lunamax | cross-domain defect routing map |
| PlanAgentsChecklist | planner | m_lunamax | drafted 8-item AGENTS.md checklist; host file FAIL |

Lane artifacts: `/tmp/kotoba-r7/*.md` (full evidence + counting commands).

## Landed (all tied to the LOG.md round-7 entry)

**The round-5 "model-compressed render" claim was wrong; the real mechanism
is now proven from the binary.** `strings -n 6 ~/.local/bin/omp` recovered
`skill-descriptions.ts`: `previewSkillDescription` = `slice(0,99)` then
first-sentence-wins-if-≥40-chars (no ellipsis) else last-space+`…`; an async
LLM compressor (smol role, ≤160 chars/≤12 words validator) fills
`~/.omp/agent/skill-descriptions.db` — 5 rows, cache keys
sha256(template+name+ws-description) reproduced 5/5. Compression activated
between 2026-09-24→27: earlier catalogues render descriptions verbatim.
Consequence measured: **17.7% of description chars reach the router; 53/62
quoted triggers lost; 13/13 trigger/anti-trigger clauses sit past the cliff
and never render** — including godspeed's own trigger list (first-sentence
branch keeps only sentence 1) and ufo's `/ufo`, `open the hatch`, etc.
SKILL.md: intro corrected, rule 8 rewritten as the cliff rule, new rules
9–12 (first-sentence exploit, reproduce-don't-assume, CJK edge,
discovery-root gate), 4 new anti-patterns. Artifact:
`corpus/knowledge/render-mechanism-round7.md`.

**Self-audit (reviewer lane on own SKILL.md):** 4 fails cured same round —
description now names the 5 sibling skills concretely with arbitration note
(checklist item 4 tightened: generic "owning domain skill" doesn't count);
`metadata.requires`/recipe-vs-prerequisite carve-out added (item 6); bare
`diff kake-round-4.md` and `opencode.json` citations grounded to bases
(items 8/10); "failure claim" defined (item 9).

**Two new surface checklists landed** — dispatch-prompt (12 items; fleet
application found 37/43 fail) and AGENTS.md (8 items; 6/6 repo files pass,
host `~/.agents/AGENTS.md` fails: procedures at :18/:55, dated attestations
:48/:51 — round-1 "zero procedures" claim in SKILL.md corrected; the six
repo files are shape-identical, not byte-identical — md5s differ).

**Drift recount (critic lane):** CLAUDE.md census 16→18 (+2 vendored);
compression warns 10191→10681; godspeed preamble 14/18 stable; `NOT` routing
11/18 stable; opencode.db histogram stable; session_init 3837→3911.

## Cross-domain evidence (reported, not fixed — PROVINCE boundary)

- **Sibling SKILL.md fleet still unfixed** (sentinel re-verify): 5/5
  descriptions remain `Domain specialist — scopes X`; 0 triggers, 0
  anti-triggers, 0 arbitration clauses. New reframe from the mechanism work:
  these files sit **outside every omp discovery root**, so the defect is
  craft-debt, not live misrouting. Owner: each sibling lane owns its own
  SKILL.md; the **mint-template producer is UNOWNED** — connector lane found
  no producer in MANIFEST.json/scripts/waves; needs integrator assignment.
- **Host agent fleet unchanged:** ufo.md `name:` absent + `cascade_note` 60d
  stale; mutation-tester.md doubled preamble; scout.md `aaron` absent —
  UNOWNED host surface (`~/.config/opencode/agents/`).
- **Driver/prompt defects** (integrator-owned, `scripts/shokunin-watchdog.sh`
  + `.ufo/prompts/`): `report_of()` accepts `<lane>-shokunin.md` contradicting
  PROTOCOL.md:101-102 yet misses `web-properties-publishing.md` (kake's
  round-1 report is invisible to the driver); heredoc numbering drops step 1;
  38/43 prompt files carry stale L2 aliases (`m_composer`/`m_antigravity`/
  `m_grok`) — the v3 generator is already correct, so this is regeneration
  latency; 6 `*-L1.md` have `<lane>` placeholders + duplicated bodies;
  `aggregator-*` prompts read `round-N-1/AGGREGATE.md` paths that never
  existed (ledger landed once at `round-2/AGGREGATE.md`; three-way
  definition divergence PROTOCOL.md vs spawn prompt vs generator).
- **Command-file defects** (`~/.config/opencode/command/`, unowned):
  `sekhmet.md:9` sources dead `~/.xbgst/env.l3-sekhmet.sh`; `ufo.md:11`
  bans nonexistent `general`/`explore` agents; `ufo.md:9` says "Task tool"
  vs host `task`.
- **godspeed coverage split resolved:** omp offer side is 3911/3911 (100%);
  the 51.5% session coverage from round 6 is opencode-side activation —
  different host/store, not an omp offer hole.

## Evidence commands (re-runnable)

```sh
# render mechanism (omp binary)
strings -n 6 ~/.local/bin/omp | sed -n '684191,684199p'   # H7s truncator
sqlite3 -readonly ~/.omp/agent/skill-descriptions.db \
  "select rowid,length(description) from skill_descriptions;"   # 5 rows
# catalogue census
grep -rl '"type":"session_init"' ~/.omp/agent/sessions/ | wc -l  # 3932 files
# stale-alias sweep
grep -l 'm_composer\|m_antigravity\|m_grok' /home/vgpnk/projects/shokunin/.ufo/prompts/*.md | wc -l  # 38
# duplicated spawn bodies
for f in /home/vgpnk/projects/shokunin/.ufo/prompts/*-L1.md; do
  a=$(sed -n 1,5p "$f"|md5sum); b=$(sed -n 6,10p "$f"|md5sum);
  [ "$a" = "$b" ] && echo "DUP $f"; done                          # 6 hits
```

## Deviations / limits

- `[INFERENCE]` render-freeze-per-session is proven only at file granularity;
  request-level timestamps weren't traced. Cache-row order vs render order
  inversion unproven.
- The LLM compressor's `smol` model id is unresolved (logs show Devin
  `invalid_argument` failures; 99.92% of 10681 warns are that error).
- Self-audit verdicts are strict-reading; all 4 fails were worded-adjacent
  (generic arbitration clause, bare-base citations) — recorded as cured, not
  softened.
- Round-7 prompt said route reviewer m_composer/connector m_antigravity/
  sentinel m_grok; MISSION.md (persisted, supersedes) says m_zfl/m_lunamax/
  m_zfl — MISSION.md followed; stale aliases in the prompt corpus are part
  of the reported defect.
- `edit` boundary-echo recurred once (5th occurrence total); caught by
  post-edit re-read, signature confirmed in lessons.
