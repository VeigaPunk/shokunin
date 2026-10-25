# PinAudit — round 32 pin sha256 census

Advisory data only. Not a verdict. Snapshot `2026-10-15T00:29:49Z`. Lane `/home/vgpnk/Projects/shokunin/kumitate-shokunin`. Dispatch `175de6ba2e9e904010411b19cab27e0af9aad3d4`. HEAD at snapshot `edfb9c5301f36b48f84f32d041c33265d985025d`.

## Result

**PIN_DRIFT: none.** All six `kumitate-proxy-v1` pin keys match the raw sha256 of the live file `scripts/proxy-check.mjs` hashes (`readFileSync` bytes, `sha256` hex; `scripts/proxy-check.mjs:440-445`, `comparePins` at `:852-872`).

**Re-pin owed: none.** Round 32 has not changed any of the six files. A pin may be rewritten only when its file bytes change. Rewriting any of these six values now would be unjustified. `pin.proxy-check` stays put: the pre-registration allows that re-pin only if `proxy-check.mjs` changed (`SCORECARD.md` planned step 4), and it did not.

Later confirmation, `2026-10-15T00:34:49Z`, HEAD `cdeaa0a` (commits since the snapshot: `5d250b4` bind stanza and Axes, `c64b380` LOG, `4151491` integrate S8 and re-bind stanza, `ccd82e4` K-block scope check, `cdeaa0a` S4 cell line counts). `git diff --stat edfb9c5..HEAD` on the six scripts was empty. `git diff -U0 edfb9c5..HEAD -- SCORECARD.md` had no added or removed `pin.` lines. Worktree pin-line diff was empty. `sha256sum` of the six files was byte-identical to the table below. Those stanza re-binds did not re-pin.

## Member list derived

The pin family is `PINS` in `scripts/proxy-check.mjs:292-298`. It is also exactly `scripts/*.mjs` in this lane (count 6). No phantom pin member. No pin file absent. No section added or removed by this audit.

| pin key | file | round 32 touched the file? | re-pin? |
|---|---|---|---|
| `pin.cite-check` | `scripts/cite-check.mjs` | no | no |
| `pin.surface-probe` | `scripts/surface-probe.mjs` | no | no |
| `pin.round-gate` | `scripts/round-gate.mjs` | no | no |
| `pin.proxy-check` | `scripts/proxy-check.mjs` | no | no |
| `pin.claims-check` | `scripts/claims-check.mjs` | no | no |
| `pin.kimi-census` | `scripts/kimi-census.mjs` | no | no |

Last commit that actually changed each file (all before this round; not a round-32 touch):

- `scripts/cite-check.mjs` — `1205c66` 2026-10-14 06:40:03 -0300, round 30, message records the pin re-pin
- `scripts/surface-probe.mjs` — `e404431` 2026-10-13 21:26:43 -0300, round 23
- `scripts/round-gate.mjs` — `364f1d5` 2026-10-13 22:49:20 -0300, round 24
- `scripts/proxy-check.mjs` — `e404431` 2026-10-13 21:26:43 -0300, round 23
- `scripts/claims-check.mjs` — `e404431` 2026-10-13 21:26:43 -0300, round 23
- `scripts/kimi-census.mjs` — `f86b8ed` 2026-10-13 19:46:25 -0300, round 20

## Declared vs computed

Worktree stanza lines at the snapshot (`SCORECARD.md:294-299`). One block head at line 276 (line trim starts with the kumitate-proxy-v1 HTML-comment opener). A second substring of that opener exists in prose at `SCORECARD.md:366` and is not a block head.

```
pin.cite-check      declared=40573448330f52fb7d45c59cb0b91d236b6e277a250d850a0e2585adc7c10c9f
                    computed=40573448330f52fb7d45c59cb0b91d236b6e277a250d850a0e2585adc7c10c9f  bytes=126735  match
pin.surface-probe   declared=148cbf85ce4c7682a4ca4a663b730d28f4c41698100f7a0313f424c7b0ecb52e
                    computed=148cbf85ce4c7682a4ca4a663b730d28f4c41698100f7a0313f424c7b0ecb52e  bytes=76395   match
pin.round-gate      declared=f890e277af83a78f2dd265e442c8c5912dc3975a36b18ae1be927022a834d3e9
                    computed=f890e277af83a78f2dd265e442c8c5912dc3975a36b18ae1be927022a834d3e9  bytes=80415   match
pin.proxy-check     declared=a052ddb97a0b6f84be5993891273905bcb19f2dfef25aa523924c0d3cc5dcdba
                    computed=a052ddb97a0b6f84be5993891273905bcb19f2dfef25aa523924c0d3cc5dcdba  bytes=119613  match
pin.claims-check    declared=e9a21b441f1216bf41d1cca037b36021c581ec7892df3bf973295f9321b0f61b
                    computed=e9a21b441f1216bf41d1cca037b36021c581ec7892df3bf973295f9321b0f61b  bytes=48265   match
pin.kimi-census     declared=83016d45049b009a6c9868dc392ff6ebcecb357c9abfe423f476459f2724f426
                    computed=83016d45049b009a6c9868dc392ff6ebcecb357c9abfe423f476459f2724f426  bytes=43273   match
```

## Whether the round touched the files

Commands and observed output:

```
git rev-parse HEAD
edfb9c5301f36b48f84f32d041c33265d985025d

git log --format='%H %ci %s' 175de6ba2e9e904010411b19cab27e0af9aad3d4..HEAD
0ecba2692c453c421a9a3c5f47aa64d8abb864f9 2026-10-14 21:27:20 -0300 round-32: fix a self-inflicted registry-parse defect (my own summary table matched the S|R row regex)
1a162a4dac6eae22eec19260d6fd14c07458dac9 2026-10-14 21:27:00 -0300 round-32: land the measured layer re-census (stanza + Axes); name the section-coverage gap; add the K-block boundary clause
edfb9c5301f36b48f84f32d041c33265d985025d 2026-10-14 21:29:26 -0300 round-32: land the wave's member-section work (S1,S2,S3,S4,S5,S6 + R1..R11 note sections and phantom removals)

git diff --stat 175de6ba2e9e904010411b19cab27e0af9aad3d4..HEAD -- scripts/cite-check.mjs scripts/surface-probe.mjs scripts/round-gate.mjs scripts/proxy-check.mjs scripts/claims-check.mjs scripts/kimi-census.mjs
(empty)

git diff -U0 175de6ba2e9e904010411b19cab27e0af9aad3d4..HEAD -- SCORECARD.md | rg '^[+-]pin\.'
NO committed pin-line change since dispatch

git diff -U0 -- SCORECARD.md | rg '^[+-]pin\.'
NO worktree pin-line change

git status --porcelain -- scripts/cite-check.mjs scripts/surface-probe.mjs scripts/round-gate.mjs scripts/proxy-check.mjs scripts/claims-check.mjs scripts/kimi-census.mjs
(empty)

git rev-parse 175de6ba:FILE vs HEAD:FILE for each of the six
UNCHANGED scripts/cite-check.mjs
UNCHANGED scripts/surface-probe.mjs
UNCHANGED scripts/round-gate.mjs
UNCHANGED scripts/proxy-check.mjs
UNCHANGED scripts/claims-check.mjs
UNCHANGED scripts/kimi-census.mjs
```

`1a162a4` and `0ecba26` edit only `SCORECARD.md`. The `1a162a4` diff mentions `pin.` only as hunk context (`pin.kimi-census=83016d45…` unchanged) and as the planned sentence `re-pin pin.proxy-check if proxy-check.mjs changed`. `0ecba26` has no `pin.` diff lines. `edfb9c5` does not appear in `git log --name-status 175de6ba..HEAD --` the six scripts and `SCORECARD.md`, so it did not touch those paths. Worktree `SCORECARD.md` was dirty at the snapshot; its `pin.*` lines were not part of that dirt.

`sha256sum` at `2026-10-15T00:29:49Z` (cwd the lane), after HEAD had moved to `edfb9c5`:

```
40573448330f52fb7d45c59cb0b91d236b6e277a250d850a0e2585adc7c10c9f  scripts/cite-check.mjs
148cbf85ce4c7682a4ca4a663b730d28f4c41698100f7a0313f424c7b0ecb52e  scripts/surface-probe.mjs
f890e277af83a78f2dd265e442c8c5912dc3975a36b18ae1be927022a834d3e9  scripts/round-gate.mjs
a052ddb97a0b6f84be5993891273905bcb19f2dfef25aa523924c0d3cc5dcdba  scripts/proxy-check.mjs
e9a21b441f1216bf41d1cca037b36021c581ec7892df3bf973295f9321b0f61b  scripts/claims-check.mjs
83016d45049b009a6c9868dc392ff6ebcecb357c9abfe423f476459f2724f426  scripts/kimi-census.mjs
```

File mtimes are all before the round opened (`cite-check` 2026-10-14 06:37 -0300; the other five 2026-10-13). Dispatch before-evidence `evidence/kumitate-proxy-before.json` (revision `175de6ba`, `2026-10-14T23:43:33Z`) already had `terms.pinsMatched=6`, `terms.pinsTotal=6`, and zero `PIN_DRIFT` findings. Its other findings were layer-term drift, not pins.

## Gate observation

```
node scripts/proxy-check.mjs --json
EXIT:1
verdict DRIFT
pinsMatched 6
pinsTotal 6
PIN_DRIFT 0
```

Each `terms.pins.*` entry had `match=true` and `declared==computed` equal to the table above. Exit 1 was non-pin drift (`S_SECTIONS_DRIFT`, `R_SECTIONS_DRIFT`, `COVERAGE_SCRIPT_DRIFT`, `COVERAGE_RUNTIME_DRIFT`, `AXES_DRIFT` x2) on that run. Do not treat that exit as a pin failure, and do not clear it by re-pinning. That non-pin list was not re-measured after `edfb9c5`; the pin bytes and pin lines were.

`ls scripts/*.mjs | wc -l` → 6, the same six names. `comparePinCoverage` therefore has nothing to warn on. The gate run reported `warnings 0`.

## Sections added / removed

None in the pin set. No pin key names a file outside the live tree. This audit did not add or remove note sections.

## Unresolved blockers

None for the pin comparison. Snapshot limit: the wave was still landing note and scorecard edits at `00:29:49Z`. If a later edit changes one of the six files before close, re-pin only that key to the new sha256 and leave the other five. This report does not cover edits after the snapshot.

## Cross-domain findings (not PIN_DRIFT)

1. **Scorecard prose still says five pins.** `SCORECARD.md:262-263`: "The five pins are full sha256 hex of `scripts/*.mjs`". The live block has six pins, and `scripts/*.mjs` is six files, including `pin.kimi-census`. Owner: parent integrator, scorecard prose only. Do not "fix" it by dropping `pin.kimi-census` or by re-pinning. The gate requires all twenty-three keys (`scripts/proxy-check.mjs:154`, `STANZA_KEYS` at `:300`); a missing pin key is `STANZA_MALFORMED`, not a quiet shrink.

2. **Skill text lists five pin keys.** `SKILL.md:748-754` stops at `pin.claims-check` and does not name `pin.kimi-census`. Owner: `SKILL.md`. Same constraint: the live stanza is the pin set; the skill list is stale prose.

3. **Knowledge-note example is a round-16 block, not the live pins.** `corpus/knowledge/executable-scorecard.md:78-109` still says seventeen keys and five pins, shows different hex (`a11ead17…`, `86bdcd9a…`, `4c447463…`) plus two placeholders, and points at `SCORECARD.md:167-179` for the live hex. Those lines are not the live pins (live pins are `SCORECARD.md:294-299`). The note labels the fence as the round-16 block, so it is not a second stanza. Owner: that knowledge note. Copying that fence into the live block would create `PIN_DRIFT`. Do not.

## Files inspected

- `SCORECARD.md` stanza `276-300`, prose `256-265`, planned re-pin sentence, round-32 commit diffs
- `scripts/proxy-check.mjs` `PINS`, `sha256File`, `comparePins`, `parseStanza`
- `scripts/cite-check.mjs`, `scripts/surface-probe.mjs`, `scripts/round-gate.mjs`, `scripts/claims-check.mjs`, `scripts/kimi-census.mjs` (bytes only; not edited)
- `SKILL.md:745-761`
- `corpus/knowledge/executable-scorecard.md:73-113`
- `evidence/kumitate-proxy-before.json` pin fields
