# KimiLayerRegression — round-32 K-block unaffected check

Leaf advisory only. Did not edit the lane. Did not claim a round verdict. Secret paths were shape-only (`stat` / census `lstat`); contents were not opened.

## Observation

**No K term moved.** `C1k`, `C1k_total`, `K_members`, `K_sections`, and `coverage_kimi` are the same integers at the dispatch pin, in every live gate run, and at HEAD `edfb9c5301f36b48f84f32d041c33265d985025d`. That is not a scope-discipline defect.

| Term | Dispatch stanza `175de6ba` | Run 1 computed | Run 2 computed | Run 3 computed | HEAD stanza `edfb9c5` | Moved? |
|---|---:|---:|---:|---:|---:|---|
| `C1k` | 5 | 5 | 5 | 5 | 5 | no |
| `C1k_total` | 5 | 5 | 5 | 5 | 5 | no |
| `K_members` | 49 | 49 | 49 | 49 | 49 | no |
| `K_sections` | 49 | 49 | 49 | 49 | 49 | no |
| `coverage_kimi` | 10 | 10 | 10 | 10 | 10 | no |

Arithmetic, re-evaluated, not trusted: `floor(10 × 5/5 × 49/49) = 10`.

`git diff 175de6ba2e9e904010411b19cab27e0af9aad3d4..edfb9c5301f36b48f84f32d041c33265d985025d -- SCORECARD.md | grep -E '^[+-](C1k|C1k_total|K_members|K_sections|coverage_kimi)='` → `NO_K_KEY_LINE_CHANGES`.

## Identity

| Field | Value |
|---|---|
| Member | `KimiLayerRegression` |
| Lane | `/home/vgpnk/Projects/shokunin/kumitate-shokunin` |
| Dispatch pin | `175de6ba2e9e904010411b19cab27e0af9aad3d4` |
| HEAD at the stable re-run | `edfb9c5301f36b48f84f32d041c33265d985025d` (before = after) |
| Origin `--src` (proxy default) | `/home/vgpnk/Projects/ufo-fsd-alpha` |
| `kimiRoot` | `/home/vgpnk/.kimi-code` |
| Contracts | `kumitate-kimi-census-v1`, `kumitate-proxy-v1` |
| Scope | The five K-block terms only |

Commits that landed on the lane during this check, none of which edit a K key line:

- `1a162a4` round-32: land the measured layer re-census (stanza + Axes); name the section-coverage gap; add the K-block boundary clause
- `0ecba26` round-32: fix a self-inflicted registry-parse defect (summary table matched `^\| (S|R)\d+ \|`; the fix text says that would move `C1_total`, not `C1k`)
- `edfb9c5` round-32: land the wave's member-section work (S1–S6 + R1..R11)

`git diff --name-only 175de6ba..edfb9c5` is `SCORECARD.md` plus ten non-kimi `corpus/knowledge/*.md` notes. It does not include `scripts/kimi-census.mjs`, `scripts/proxy-check.mjs`, or any `corpus/knowledge/kimi-*.md`. `pin.kimi-census` stayed `83016d45049b009a6c9868dc392ff6ebcecb357c9abfe423f476459f2724f426` and `match: true` on every proxy run.

## Files inspected

- `SCORECARD.md` — `<!-- kumitate-proxy-v1` block (stanza line 276) at dispatch and at HEAD; round-32 `## Planned` (1364–1409) halt “No frozen term outside the four layer terms + two derived scores changes”; executed K-block boundary clause (1443–1449)
- `scripts/kimi-census.mjs` — frozen `MEMBERS` / `FROZEN` (lines 99–145); secret path is `lstat` + mode floor, never opened
- `scripts/proxy-check.mjs` — K-term header (C1k / K_members / K_sections / coverage_kimi); secret members kind-statted only
- `corpus/knowledge/kimi-binary-secrets.md` and `corpus/knowledge/kimi-skills-plugins.md` — only to see whether `oauth/` mode 755 was already recorded (it is)
- Live `~/.kimi-code` names for the K2 counted dirs; secret paths via `stat -c '%n %F %a'` only

## Commands + observed output

cwd for every gate run: `/home/vgpnk/Projects/shokunin/kumitate-shokunin`.

### Run 1 — exact assigned commands, declared stanza still the dispatch block

The declared block in this JSON is the dispatch stanza (`S_members=114`, `coverage_runtime=7`). HEAD was not sampled inside this command; the next `git rev-parse` in this check returned `1a162a4`, so this run predates that commit. K terms already matched. The six errors are the pre-registered S/R drift, not K.

```text
$ node scripts/kimi-census.mjs
KIMI_ROOT: /home/vgpnk/.kimi-code
FAMILY K1  members=3  checked=3  frozen=3
FAMILY K2  members=25  checked=25  frozen=25
FAMILY K3  members=9  checked=9  frozen=9
FAMILY K4  members=9  checked=9  frozen=9
FAMILY K5  members=3  checked=3  frozen=3
INFO  CHAIN  config.toml.*.bak  generations=12 (reported as info, never gated)
INFO  COUNT  agents/secondary/  children=18 (counted live, names not gated)
INFO  COUNT  skills/  children=5 (counted live, names not gated)
INFO  ROOT_ENUM  -  root children=37 declared=25 chain=12 strays=0 (root enumerated against K1–K5; drift-chain generations exempt)
TOTALS: members=49 checked=49 errors=0 info=4 chain=12
KIMI_CENSUS: CLEAN (members=49 checked=49 chain=12 info=4)
EXIT:0
```

```text
$ node scripts/proxy-check.mjs --json
verdict=DRIFT exitCode=1 errors=6 warnings=0 durationMs=32
kimiRoot=/home/vgpnk/.kimi-code
C1k declared=5 computed=5
C1k_total declared=5 computed=5
K_members declared=49 computed=49
K_sections declared=49 computed=49
coverage_kimi declared=10 computed=10
pin.kimi-census match=true
findings:
  S_MEMBERS_DRIFT S_members declared=114 computed=91 delta=-23
  S_SECTIONS_DRIFT S_sections declared=74 computed=58 delta=-16
  R_MEMBERS_DRIFT R_members declared=98 computed=92 delta=-6
  R_SECTIONS_DRIFT R_sections declared=69 computed=63 delta=-6
  COVERAGE_RUNTIME_DRIFT coverage_runtime declared=7 computed=6 delta=-1
  AXES_DRIFT coverage:runtime-layer declared=7 computed=6
EXIT:1
```

Zero findings whose `term` is `C1k`, `C1k_total`, `K_members`, `K_sections`, `coverage_kimi`, or `coverage:kimi-layer`.

### Run 2 — re-measure after `1a162a4` / `0ecba26`, working tree still dirty

Wrapped so the K slice could be compared without hand transcription. Not a substitute for the exact commands; those were repeated in run 3.

```text
HEAD at start of wrapper: 0ecba2692c45
$ node scripts/kimi-census.mjs
KIMI_CENSUS: CLEAN (members=49 checked=49 chain=12 info=4)
CENSUS_EXIT:0

$ node scripts/proxy-check.mjs --json
PROXY_EXIT:1
C1k declared=5 computed=5 match=true
C1k_total declared=5 computed=5 match=true
K_members declared=49 computed=49 match=true
K_sections declared=49 computed=49 match=true
coverage_kimi declared=10 computed=10 match=true
verdict=DRIFT exitCode=1 errors=6 warnings=0
kFindings=0
findingKinds=S_SECTIONS_DRIFT:S_sections,R_SECTIONS_DRIFT:R_sections,COVERAGE_SCRIPT_DRIFT:coverage_script,COVERAGE_RUNTIME_DRIFT:coverage_runtime,AXES_DRIFT:coverage:script-layer,AXES_DRIFT:coverage:runtime-layer
pins.kimi-census match=true
```

Quoted finding deltas from that JSON: `S_sections` 56→73, `R_sections` 63→74, `coverage_script` 6→8, `coverage_runtime` 6→8. Those are in-flight S/R note edits. They did not move any K term. `S_members` / `R_members` were no longer in the finding list (stanza already carried 91 / 92).

### Run 3 — exact assigned commands at a stable HEAD

```text
HEAD_BEFORE=edfb9c5301f36b48f84f32d041c33265d985025d
$ node scripts/kimi-census.mjs
KIMI_ROOT: /home/vgpnk/.kimi-code
FAMILY K1  members=3  checked=3  frozen=3
FAMILY K2  members=25  checked=25  frozen=25
FAMILY K3  members=9  checked=9  frozen=9
FAMILY K4  members=9  checked=9  frozen=9
FAMILY K5  members=3  checked=3  frozen=3
INFO  CHAIN  config.toml.*.bak  generations=12 (reported as info, never gated)
INFO  COUNT  agents/secondary/  children=18 (counted live, names not gated)
INFO  COUNT  skills/  children=5 (counted live, names not gated)
INFO  ROOT_ENUM  -  root children=37 declared=25 chain=12 strays=0 (root enumerated against K1–K5; drift-chain generations exempt)
TOTALS: members=49 checked=49 errors=0 info=4 chain=12
KIMI_CENSUS: CLEAN (members=49 checked=49 chain=12 info=4)
CENSUS_EXIT:0
```

```text
$ node scripts/proxy-check.mjs --json
{
  "contract": "kumitate-proxy-v1",
  "mode": "check",
  "ok": true,
  "verdict": "MATCH",
  "exitCode": 0,
  "self": "/home/vgpnk/Projects/shokunin/kumitate-shokunin",
  "scorecard": "/home/vgpnk/Projects/shokunin/kumitate-shokunin/SCORECARD.md",
  "src": "/home/vgpnk/Projects/ufo-fsd-alpha",
  "kimiRoot": "/home/vgpnk/.kimi-code",
  "strict": false,
  "terms": {
    "C1k": 5,
    "C1k_total": 5,
    "K_members": 49,
    "K_sections": 49,
    "coverage_kimi": 10,
    "pins.pin.kimi-census.match": true,
    "declared.C1k": "5",
    "declared.C1k_total": "5",
    "declared.K_members": "49",
    "declared.K_sections": "49",
    "declared.coverage_kimi": "10",
    "declared.pin.kimi-census": "83016d45049b009a6c9868dc392ff6ebcecb357c9abfe423f476459f2724f426"
  },
  "findings": [],
  "errors": 0,
  "warnings": 0,
  "durationMs": 40
}
PROXY_EXIT:0
HEAD_AFTER=edfb9c5301f36b48f84f32d041c33265d985025d
```

The live JSON also carried the layer terms the parent had just landed (`S_members=91`, `S_sections=91`, `R_members=92`, `R_sections=74`, `coverage_script=10`, `coverage_runtime=8`) and `findings: []`. Those layer integers are recorded so they are not mistaken for K movement. `coverage_script` 6→10 and `coverage_runtime` 7→8 across the round; `coverage_kimi` stayed 10.

### Stanza key diff and formula

```text
$ git diff 175de6ba2e9e904010411b19cab27e0af9aad3d4..HEAD -- SCORECARD.md \
    | grep -E '^[+-](C1k|C1k_total|K_members|K_sections|coverage_kimi)=' \
    || echo NO_K_KEY_LINE_CHANGES
NO_K_KEY_LINE_CHANGES

$ node -e 'console.log(Math.floor(10*(5/5)*(49/49)))'
10
```

At HEAD the stanza K lines were still:

```text
C1k=5
C1k_total=5
K_members=49
K_sections=49
coverage_kimi=10
pin.kimi-census=83016d45049b009a6c9868dc392ff6ebcecb357c9abfe423f476459f2724f426
```

## Member list derived

Census live totals equal the frozen family counts (3+25+9+9+3 = 49). No member was added or dropped. K2 counted children were listed by name (not secret). Secret slots are ids + kind + mode only.

K1 (3): `config.toml`, `tui.toml`, `config.toml.*.bak` (one member; INFO generations=12, not a scored term).

K2 (25): `agents/secondary/` live 18 —

`sec-fast-hyper-ds-flash.md`, `sec-fast-hyper-glm-flash.md`, `sec-fast-tp1-ds-flash.md`, `sec-fast-tp2-ds-flash.md`, `sec-fast-tp3-ds-flash.md`, `sec-fast-zai-flash-low.md`, `sec-fast-zai-flash.md`, `sec-mid-hyper-qwen-flash.md`, `sec-mid-tp1-qwen-flash.md`, `sec-mid-tp2-qwen-flash.md`, `sec-mid-tp3-qwen-flash.md`, `sec-mid-zai-glm-5-turbo.md`, `sec-strong-hyper-qwen-max.md`, `sec-strong-tp1-qwen-max-xhigh.md`, `sec-strong-tp1-qwen-max.md`, `sec-strong-tp2-qwen-max.md`, `sec-strong-tp3-qwen-max.md`, `sec-strong-zai-glm-53.md`

— plus `skills/` live 5: `godspeed`, `reverse-engineer-anything`, `shokunin`, `ufo`, `wwkd`; plus `plugins/installed.json`; plus `plugins/managed/kimi-webbridge`.

K3 (9): `sessions/`, `session_index.jsonl`, `workspace-trust/`, `telemetry/`, `logs/kimi-code.log`, `file-history/`, `user-history/`, `cache/`, `search-index/`.

K4 (9): `bin/kimi`, `bin/fd`, `updates/`, `server/`, `server.token` (secret, file, mode 600), `device_id`, `region`, `credentials/` (secret, dir, mode 700), `oauth/` (secret, dir, mode 755).

K5 (3): `workspaces.json`, `tui.toml.bak`, `rc-qrcode.png`.

Root enum: children=37, declared=25, chain=12, strays=0. No `UNLISTED`, no `MEMBER_MISSING`, no `SHAPE_DRIFT`.

## Sections added / removed

None by this member. No `kimi-*.md` heading was added or removed in `175de6ba..edfb9c5`. `K_sections` stayed 49 distinct, which is the whole member set, so a phantom K section was not left behind and a new K member was not sectionized.

## Unresolved blockers

None on the K block. Census exit 0 three times. Proxy K slice matched three times. The run-3 proxy exit 0 is a whole-stanza `MATCH`, which is stronger than the K question and is the parent's layer landing, not a K result.

## Cross-domain

- **Owner: parent integrator / layer re-census.** S/R terms and `coverage_script` / `coverage_runtime` moved during this round, as the pre-registration allows (four layer terms + two derived scores). K terms did not. Run 1's `PROXY: DRIFT` and run 2's section-delta DRIFT are that layer work in flight, not a K leak. Run 3's `MATCH` is the layer stanza catching up; K keys were already equal before that catch-up.
- **Owner: kagi (already filed, not new).** `oauth/` mode 755 still satisfies the census `0o700` bit-floor (`755 & 0700 == 0700`) and is already recorded in `corpus/knowledge/kimi-binary-secrets.md` (shape table) and `corpus/knowledge/kimi-skills-plugins.md` (mode-floor erratum). Not a round-32 regression. Contents not read.
- **Owner: tabi / kaidoku / kotoba / kagi, as already written.** The `1a162a4` boundary clause says census membership and `coverage:kimi-layer` = 10 are unchanged by the adjacency routing. This measurement agrees with that sentence; it does not extend it.

## Finding (assigned surface)

- Severity: none.
- Exploit path: a scope leak would be an edit to a K stanza key, `scripts/kimi-census.mjs`, `scripts/proxy-check.mjs`'s K derivation, or a `kimi-*.md` heading, or a live `~/.kimi-code` membership change that the census would score. None of those moved between the dispatch pin and `edfb9c5`. Concurrent S/R note edits changed layer scores and left `K_sections` at 49.
- Evidence: three census CLEAN lines; three proxy K comparisons; `NO_K_KEY_LINE_CHANGES`; `pin.kimi-census` match.
- Impact: `coverage:kimi-layer` stays 10. The round's script/runtime re-census did not perturb the K block.
- Smallest remediation: none.

End advisory. No lane mutation. No commit.
