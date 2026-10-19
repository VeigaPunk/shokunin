# kaika D5 — canonical runtime smoke (final completed-slice probe)

**Hypothesis:** the canonical completed tree at `.tower/worktrees/kaika/kimi-shokunin-canon`
(worktree `kaika/canon-sync`, HEAD `b3ca98f` + 21 modified / 3 untracked commitment candidates)
executes its documented install → mint → render → census → schema paths as documented, with
data-safe `/ & \` handling, valid empty-registry seeds, and a schema that accepts the actual
fleet's lane/trend/supersedes closure entries.

**Isolation:** all writes under `/tmp/kaika-verify/D5CanonicalRuntime` (own HOME, fleet, TMPDIR).
Canonical worktree and `/home/vgpnk/Projects/shokunin` read-only; `ufo-fsd-alpha` untouched; no
watchdog loop, no model API calls. Tested bytes = working-tree commitment candidates, staged
content-identical (`rsync` + `diff -r` clean).

Sha256 pins of tested files (canon worktree):

```
aed9ed65e42eaa5d372c380509e05f6fabbb39ec15cc75f06010898474ae8d1b  scripts/sources-census.sh
5042448abf3d5924d8bdd8af63121650c72bedab78a193facda03c0ace845bf2  scripts/shokunin-watchdog.sh
fa411a7014a296c9d45bc05d815f59b9a601648ac61d33165e9d026091d86937  scripts/mint-agent.sh
ed5960ff3804de537d633a192bd3e948783cccd47d8837ba439cf89f55d5dd71  install.sh
6c223567f9efe055339a166649ffc7bebd51a1ebbb8712ed5d787ad85e8e0506  templates/round-prompt.md
d6fc5f0a39122471cd1576910975d9649f7e2150582de723c29eac21d57c995c  templates/MANIFEST.schema.json
b4e460dc3a8bc228c912c10ec999e290f0330f65c0fbec6a83bf9279e5cbe393  templates/mint/corpus/SOURCES.md
87c36d9fdf2856b2003e9bf93a1ca0ec1a87889f04b6960ca16a3eb0a0f28923  sha256 of the sorted per-file sha256 list of all 8 scripts/fixtures files
```

## 1. install.sh gate (documented sanity gate)

```
$ env -i HOME=/tmp/kaika-verify/.../home PATH=/usr/bin:/bin bash <stage>/install.sh; echo rc=$?
[kimi-shokunin] Sanity checks
[kimi-shokunin] required files OK (mint kit: 7 root files + corpus seeds)
[kimi-shokunin] script syntax OK
[kimi-shokunin] manifest JSON OK
[kimi-shokunin] Install the plugin from Kimi Code CLI with: /plugins install … /reload
rc=0
```

Kimi CLI at `/home/vgpnk/.kimi-code/bin/kimi` exposes no non-interactive plugin-install
subcommand (`--help` lists `provider/session/acp/web/plastic login/doctor/…`; plugin install is
only the in-session `/plugins install` slash command), so the Kimi-side install step itself was
not executed without a model session. Gate output and rc recorded.

## 2. Real mint flow (`scripts/mint-agent.sh`, isolated fleet root)

Conf prepared as documented (`cp templates/shokunin.conf.example shokunin.conf`, placeholder
LANES rows cleared), then two real mints (second domain carries `/ & \`):

```
$ mint-agent.sh --id probe-a --domain "probe smoke domain" --fleet-root $S/fleet   # rc=0
$ mint-agent.sh --id probe-b --domain 'A / B & C \ D' --fleet-root $S/fleet       # rc=0
minted …/probe-a-shokunin (seed commit: 0549120);  minted …/probe-b-shokunin (seed commit: 523cc71)
```

Author identity (lane commit, both author and committer):

```
probe-a | author: probe-a-shokunin <probe-a@shokunin.local> | committer: probe-a-shokunin <probe-a@shokunin.local> | mint: seed probe-a-shokunin (probe smoke domain)
probe-b | author: probe-b-shokunin <probe-b@shokunin.local> | committer: probe-b-shokunin <probe-b@shokunin.local> | mint: seed probe-b-shokunin (A / B & C \ D)
```

Seed tree = 7 root files + `corpus/{QUALITY,README,SOURCES}.md` + `knowledge/.gitkeep`,
`lessons/.gitkeep` (12 tracked files). `<name>` header substituted: `# SOURCES — where probe-a learns`.

Conf wiring: both lanes appended verbatim, incl. the escaped domain:

```
LANES="$LANES
probe-b|probe-b-shokunin|A / B & C \ D"
```

Round trip through the real watchdog parser (`source` with the definitions-only guard):

```
probe-a|repo=probe-a-shokunin|axes=[probe smoke domain]
probe-b|repo=probe-b-shokunin|axes=[A / B & C \ D]
probe-b axes == minted domain (verbatim)   # rc=0
```

Placeholder resolution: zero leftovers of `{{…}}`, `<name>`, `<lane>`, `<DOMAIN>`,
`<YYYY-MM-DD>` in either lane. 28 by-design fill-in tokens remain for the minting orchestrator
(e.g. `<sibling lane id>` ×16, `<lane id>` ×8, `<N>`/`<NUMBER>`, MINT.md evidence spans) —
same token set as the pre-mint kit minus the four substituted ones.

## 3. Prompt render — child lane and `repo='.'`, axes with `/ & \`

Harness sources the real `scripts/shokunin-watchdog.sh` (guard: `BASH_SOURCE[0] != $0` → no
`main`) and calls `render_prompt` for `probe-a|probe-a-shokunin|alpha / beta & gamma \ delta axes`
and `rooted|.|main-repo lane: slash/amp & backslash\ here`. bash 5.3.15. Both rc=0.

```
rendered: .../fleet/.ufo/prompts/probe-a-round-3.md
rendered: .../fleet/.ufo/prompts/rooted-round-1.md
You are the probe-a L1, round 3. Working dir: /tmp/kaika-verify/D5CanonicalRuntime/fleet/probe-a-shokunin.
You are the rooted L1, round 1. Working dir: /tmp/kaika-verify/D5CanonicalRuntime/fleet.
Your lane axes: alpha / beta & gamma \ delta axes. …
Your lane axes: main-repo lane: slash/amp & backslash\ here. …
placeholder leftovers: none
probe-a byte-identical: True   rooted byte-identical: True   (vs independent reference render)
```

sha256 of the rendered prompts: `a920845e…5babf`, `d6b9ce10…f729e7`.

## 4. Census selftest (committed candidates incl. 8 untracked fixtures)

```
$ TMPDIR=$S/tmp bash <stage>/scripts/sources-census.sh selftest   # rc=0
killed=56  survived=0
selftest ok
```

All 56 checks killed; exit 3 path not taken.

## 5. Empty-registry SOURCES is valid

```
$ sources-census.sh validate --root $S/fleet --today 2026-10-19 probe-a probe-b   # rc=0
probe-a	ok	…/probe-a-shokunin/corpus/SOURCES.md
probe-b	ok	…/probe-b-shokunin/corpus/SOURCES.md
$ sources-census.sh census --root $S/fleet                                       # rc=0
probe-a rows 0 · probe-b rows 0 · FLEET rows 0 · FLEET missing 0
$ sources-census.sh validate --file …/corpus/SOURCES.md                          # rc=0
$ sources-census.sh validate --file <stage>/templates/mint/corpus/SOURCES.md     # rc=0 (seed kit itself)
```

## 6. Schema check — canonical `roundEntry` vs actual fleet `MANIFEST.json`

Validator: `check-jsonschema 0.38.2`, `--base-uri file://<canon>/templates/`, canonical
`templates/MANIFEST.schema.json#/$defs/roundEntry`. Fleet file `/home/vgpnk/Projects/shokunin/MANIFEST.json`
(312 `rounds[]` entries), read-only.

Selected actual entries (passed):

- ordinary closure `rounds[311]` (kake r20: `lane`,`lane_round`,`trends{expansion,quality,discernment}`) → `ok -- validation done`, rc=0.
- closure-correction `rounds[310]` (kagi r21: `lane`,`lane_round`,`lane_rounds`,`lanes`,`trends`, `closed_at`, `supersedes {round:21,type:"closure",date:"2026-10-19",entry:308}`) → rc=0.
- All 45 entries carrying `supersedes.entry` validate; all 154 entries carrying any of
  `lane|lane_round|trends|supersedes` fail only if their `type` is a legacy/null one — no
  failure among entries with a canonical type + `date` + `round` (list is empty).

Mutation controls (prove the check bites):

```
trends.discernment="worse"   → $ .trends.discernment: 'worse' is not one of [...]; rc=1
supersedes.entry="4" (str)   → $ .supersedes.entry: '4' is not of type 'integer'; rc=1
```

Aggregate over all 312 actual entries: **206 pass / 106 fail (rc=1)**, classes:

| class | n | example |
|---|---|---|
| legacy `type` outside canonical enum (`train`,`train+audit`,`train+audit+unlock`,`craft`) | 75 | `rounds[75].type: 'train' …` |
| `lanes.<lane> = "closed"` (outside canonical status vocabulary; PROTOCOL.md:258 = `ok\|failed\|not-dispatched\|in-flight`) | 24 | `rounds[2..11].lanes.mori: 'closed'` (mori's whole 2026-10-15 history) |
| aux entries missing `type`/`date` (kotodama loop/provider/model records carrying `lane`) | 5 | `rounds[272,277,279,291,293]` |
| `round: null` on a closure entry | 1 | `rounds[138]` (kagi/kake/kama/kasegi/kengaku/kotoba all `ok`, `lane_rounds` populated) |
| `lanes` contains `not-dispatched` without `closed_at` (canonical conditional rule) | 1 | `rounds[1]` (work, 2026-09-28) |

Interpretation: all five classes are actual-fleet data shapes that predate or bypass the
canonical vocabulary; none is a canonical-slice internal inconsistency (schema ↔ canonical
PROTOCOL.md agree on the enum and the `closed_at` rule). They are reconciliation items for the
integrator if the canonical schema is meant to accept the fleet's full history: the `closed`
status gap covers a live slice of mori rounds 2–11; `rounds[138]`'s null `round` and
`rounds[1]`'s missing `closed_at` are single-row anomalies.

## Defects / reproductions

- **No canonical-file defect reproduced.** install.sh, mint-agent.sh, watchdog `render_prompt`,
  census (selftest + empty registry), and the schema's acceptance of actual
  lane/lane_round/trends/supersedes closure and closure-correction entries all behaved as
  documented (rc=0 where expected).
- **Fleet-vs-canonical data mismatches** (above table): 106/312 actual entries are rejected; the
  three notable reproductions are `lanes.mori='closed'` (24 rows), `rounds[138].round=null`, and
  `rounds[1]` not-dispatched without `closed_at`.

## Limitations

- Kimi `/plugins install` is TUI-only (no non-interactive subcommand in `kimi --help`); only the
  `install.sh` gate ran. No model calls.
- Render test exercises `render_prompt` via the script's own source-guard, not a live driver
  tick; mission-liveness/kill/advance paths untested (probe forbade a live loop).
- Schema check covers `rounds[]` entries, not `roster[]`; validator is the host's
  `check-jsonschema 0.38.2` against the canonical schema file.
- Prior probe input found in D5CanonicalSync's handoff (synced smoke used a hand-built
  closure-correction example); this probe is independent and uses the actual fleet corpus.

## Cleanup

Scratch `/tmp/kaika-verify/D5CanonicalRuntime` removed after this report was written; no
background processes were started. Canon worktree status re-checked after all runs: identical
to pre-probe (`21 M`, `3 ??`), no `.ufo`/driver state written into it.