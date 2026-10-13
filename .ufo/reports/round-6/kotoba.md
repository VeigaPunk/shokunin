# kotoba-shokunin — round 6 report

Commit: `kotoba-shokunin@a614927` — "round-6: agent-def checklist+audit
(15/18 clean, 4 fails), CLAUDE.md surface census, literal-trigger miss proxy"

## SHONEN

Rank: shonen. SHONEN.md re-attributed per the round-6 verifier-attribution
rule: all four boxes now `[~] kotoba-self (L1)` — the prior `[x]` marks were
self-attested (the round-5 "independent" reviewer lane was self-dispatched,
which the round-6 protocol report flags as still-the-lane). No external
verifier has run yet; promotion boxes stay asserted-not-verified.

## Gap selected

Three records again converged: (1) round-5 proved a verbatim-checklist audit
lane is cheap and productive — the agent-definition surface had evidence
(18 files, round-4) but no checklist and no audit; (2) the README gap list
named CLAUDE.md/MCP/plugin surfaces uncovered; (3) telemetry was *located*
but no fidelity number existed. All three landed.

## Landed

**Agent-definition checklist + audit (second end-to-end task).** SKILL.md
gained a 9-item agent-definition fidelity checklist (AD-1…AD-9: name,
reachability, routing cue, schema resolution, dated-text ban, identity-only
body, duplication/conflict, no trigger restatement, resolvable commands and
file paths). A blank-context L2 reviewer applied it verbatim to all 18
`~/.config/opencode/agents/*.md` — **15/18 clean, 4 fail cells**, all L1
re-verified:

| Defect | File:line | Verified by |
|--------|-----------|-------------|
| No `name:` key (latent — stem fallback) | ufo.md:1–9 | frontmatter read |
| Stale dated `cascade_note` ("until 2026-08-29", 30d stale) | ufo.md:7 | grep |
| Gods­peed preamble duplicated in-file | mutation-tester.md:8–14,34–40 | grep -c = 2 |
| `aaron` bin declared "on PATH", absent, no fallback | scout.md:38 | `command -v aaron` empty |

All are drift defects, zero design defects — this fleet was hand-maintained,
not template-minted (contrast: sibling SKILL.md fleet 0/5 on trigger items).
Fixes are cross-domain: audited-and-reported, not landed. The audit also
corrected two of my round-4 counts (godspeed preamble 13→**14**/18;
negative routing 7→**11**/18) — fixed in SKILL.md and the corpus file.

**Checklist hardened by its own audit, again.** 10 meta-findings resolved in
SKILL.md same-round: frontmatter keys now judged against the harness schema
(not a fixed list — `mode`/`variant`/`cascade_class`/`steps` observed),
dated-text ban widened to `description` (connector.md/planner.md carry
round-indexed routing text), same-name-differing-content blocks are
conflict defects (labrat.md's two DESPAWN templates), body file paths need
resolvable bases (`../godspeed-core/` refs absent under `~/.config/`),
harness tool literals (`SendMessage`/`TaskCreate`) carved out of the command
rule, `the-*` delegated names must match enrollment keys.

**CLAUDE.md = seventh surface class, cold channel.** 16-file census: 5
operator-authored (incl. a 4339-line unconditional-tax outlier and
`HVM4/CLAUDE.md` headed "# AGENTS.md" — a rename in flight), 1 dispatch
template wearing the name, 10 vendored/cache. Loader strings exist in both
harness binaries (opencode 9×, omp 17×) but **zero captured injections** and
no session ever ran in a CLAUDE.md dir — the surface is recognized, not
exercised. SKILL.md surfaces table now carries all 7 classes. MCP/tool-
description and plugin-manifest surfaces verified *absent* on this host
(`opencode.json` key set has no `mcp`; `plugin/` holds one nudge script) —
the README gap list is now empty of surface classes; only implicit-intent
fidelity remains.

**First fidelity number: literal-trigger miss proxy.** opencode.db, 398
sessions / 415 skill calls, user text scrubbed of slash-commands and
injected directive blobs (that scrub killed a 60-session phantom `ufo`
cluster — `/skill:godspeed` dispatch text contains the token). Result:
**unique-token triggers miss 0%** (wwkd, bailian terms, sekhmet, omarchy);
**godspeed always-on coverage is 51.5%** of sessions — an offer-side hole
an always-on `description` cannot fix; domain-term names produce false
"misses" (all 5 `ufo` misses are domain references, not invocations).
SKILL.md gained frontmatter rule 9: invocation-shaped triggers for
domain-term names. Artifact: `corpus/knowledge/trigger-miss-proxy-round6.md`
with re-runnable SQL.

**Sibling defect re-check:** all 5 sibling `description`s unchanged since
the round-5 audit — the mint-template defect persists; fix remains
cross-domain (mint template lives outside this province).

## Evidence commands (re-runnable)

```sh
# miss proxy
sqlite3 -readonly ~/.local/share/opencode/opencode.db \
 "select p.session_id, json_extract(p.data,'$.state.input.name') from part p
  where json_extract(p.data,'$.tool')='skill'"
# CLAUDE.md census + loader strings
find ~ -maxdepth 6 -iname 'claude.md' -not -path '*/node_modules/*'
grep -o 'CLAUDE.md' ~/.opencode/bin/opencode | wc -l   # 9
grep -o 'CLAUDE.md' ~/.local/bin/omp | wc -l           # 17
# verified defects
command -v aaron            # empty — scout.md:38 fail
grep -n 'Godspeed-enabled' ~/.config/opencode/agents/mutation-tester.md  # 8,34
grep -n 'name:' ~/.config/opencode/agents/ufo.md       # absent — AD-1 fail
```

## Deviations / limits

- Agent-def audit verdicts are strict-reading; `ufo.md` AD-1 is latent
  (stem fallback) not behavioral — recorded as such rather than softened.
- Implicit-intent fidelity remains unmeasured (needs prompt labeling);
  cross-store dedupe (opencode.db vs omp jsonl) is future work.
- CLAUDE.md injection semantics are proven only negatively (0 captures) —
  positive verification needs a scratch session in a CLAUDE.md dir.
- `edit` boundary-echo recurred twice this round (4th occurrence overall);
  both caught by post-edit re-read, signature now sharp: bodies that echo
  adjacent file text.
