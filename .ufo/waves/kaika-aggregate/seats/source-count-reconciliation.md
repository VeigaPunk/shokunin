# Source-count reconciliation — aggregator round 12 (seat KaikaAggregateR12.SourceCountReconciliation)

**PROVISIONAL BANNER.** Every total and finding summary below is PROVISIONAL. A census parser
correction for indented Markdown source rows is in progress elsewhere (`CensusIndentFix`); no
totals are frozen, no baseline is published, and nothing here may be copied into README / LOG /
SCORECARD / reports / MANIFEST. No new numeric score is proposed. The 21 lane repositories were
read only; the single write from this seat is this file.

## 0. Revision binding

| Artifact | Identity |
|---|---|
| `scripts/sources-census.sh` (fleet root) | sha256 `aed9ed65e42eaa5d372c380509e05f6fabbb39ec15cc75f06010898474ae8d1b`; git blob `b5dcc152212a38d2e3ee122fc46081453840cdcf` (mode 100755), `git status --porcelain` clean → equals fleet-root HEAD |
| `.tower/worktrees/kaika/fleet-aggregate/scripts/sources-census.sh` | byte-identical (same sha256) → no version skew between fleet root and worktree |
| `shokunin.conf` (both copies) | sha256 `a42e8406082ebb9a4248d91df06cb331c365b94e3ce877a6d8652363baebc5ee` (identical) |
| fleet-root HEAD | `dcf3b6484e02452fc7aec55d724744de188779b9` |
| worktree `fleet-aggregate` HEAD | `ee8ba85736ee7bdeda46ba8e0e1267a8366ee7f2` |
| Execution root | `/home/vgpnk/Projects/shokunin` (all lane reads absolute; no lane mutated) |

Targets: the 21 physical `/home/vgpnk/Projects/shokunin/*-shokunin`. Per-lane revision binding
(HEAD + sha256 of `corpus/SOURCES.md`); all 17 present files are clean vs their own HEAD
(`git -C <lane> status --porcelain=v1 -- corpus/SOURCES.md` → empty for every lane), so the
working-tree reads equal committed content.

| lane | HEAD | SOURCES.md sha256 |
|---|---|---|
| audio | `defbe128649268bfca75757cb3978be802696592` | ABSENT |
| chousa | `d730ae4c33989ad9c8535764d4cae77b4db869f6` | `6428e46aa69d8554c09e06c5384ce2664ae3db79b6c9f3a072c07a11a957bbbf` |
| game-dev-2d | `e89905162b3a630a599607279681b30572010724` | ABSENT |
| game-dev-3d | `3118be0b18dd7351b1faf6ce99d26a34370793ec` | `dc95c043da258003dddc8957f168e3635fbd9fc587bace5232c7bdd3a824936f` |
| kagi | `1e9e67ff3f8f9e7118f8a7026c0e79aab9ce42b2` | `db134917dab989f24c3e33b5983fdac7240fd412c9ebdf94a77c76a8fe55b332` |
| kaidoku | `1170f717c4ffeb3d0a9fd24522d8fb42f78fa837` | ABSENT |
| kake | `7e17c663b8713daac27774d49d87c4d44ea30747` | `e1f07eb4929903c422946dca1617939dc1ea2aebdceb807a224e182704b98042` |
| kama | `03b5f0e8b9ec421c0b819b31e1bbc452b61dd0f9` | `9dc40d25a595b3d42b39649e17094cfa4e7190cfbf340331252dd29dea22093a` |
| kasegi | `13a51920068c48c0c5b3c8c81d5af0df6d4ea337` | `0e8378bceb01f1c26045059044e85e9417bc933e15b4c774ec53ee34359dc940` |
| kengaku | `a42bb40c1767e1ac24394fadda7301ae5409e7ae` | `fb57569835c4f1c6a55decbf4a36b5f6dac8f6c3d3b2a961d3dfba4f48cf5cc5` |
| kotoba | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` | `ef331658e398dd552f8df992aade49d25025eb7b0309e7f2d3c00a7fd92e16d3` |
| kotodama | `4ad26836552462d28a946ca3b067cab0b5ce3532` | `662f962687717fa9cc66ec365c2c3e85ec79fc5ae5cd9fbc9df33dce3baa8e34` |
| kumitate | `16a5441a3347a10ac5ed169abcd5a17ba6f3f185` | ABSENT |
| lore | `6e804e2e5bff0edcc260c995a058dd724b0c98c0` | `9fc435e8095f8f867c18bd3b048c9d1f6c6040c9a60f6de5cb4d9d9e4dae9249` |
| mado | `e3e6a8e6ca493e250fb357343816a88e844c4c63` | `9b175fa9925a7b7230ccb02cc121a0c5e932b5af4569f6c8b6df367540e07e23` |
| mori | `bf7cdc4783d0748d525fbfe3ba8fb3d285eb929a` | `efe349d580266b8499d783d94b707012639d73173b57e09168a5a9df1d823ab6` |
| revenger | `cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97` | `c1573b2fbc284493096ddb20af506122aea0bcf7bc6b5a037b7dc31988f55f30` |
| souji | `31984f473ce4bdab61a99b16cca194b28108cb81` | `1b7cc681084e9e5efcb3a89ff0f7943758d3040926c22f4cf5c58046ca548127` |
| tabi | `9bc89bfe78b1c455501b2c7a0d9bd061ea539c21` | `000053ccfc4e61f2dae220213ed42f59c25d168d8e0b64a07c28f1770abd5c77` |
| tameshi | `a21e9104723e7a46b794b03b8fdcdd1455696f7e` | `6b34e8991f56d78d561512d71c7eaeaf4f548f1d7f12eec8eb2b896bf6d72827` |
| tsukuroi | `d8ec15d5e6c1d93370f5a85b929745e26577f4d8` | `3e06c2ebb36f5feaf84978238a9bd36d76a2313c017a0f9916fbc0bf0259b2e2` |

The four ABSENT lanes have **no** `SOURCES.md`/`SOURCES*.md` at depth ≤ 4 anywhere in the lane
(`find <lane> -maxdepth 4 -iname 'sources*.md'` → 0 matches for all four) — they are registry-less,
not mis-named. The fleet root has **no** `corpus/` directory at all (`ls -d corpus` → exit 2).

## 1. Exact commands, observed output volume, exit codes

Run root: `/home/vgpnk/Projects/shokunin`; `S=scripts/sources-census.sh`; `R=/home/vgpnk/Projects/shokunin`;
`P=$R/*-shokunin` (21 expanded dirs).

```
bash $S census   --root $R --today 2026-10-19                # rc=1, 131 stdout lines, stderr empty
bash $S validate --root $R --today 2026-10-19                # rc=2,  30 stdout lines, stderr empty
bash $S shared   --root $R --today 2026-10-19                # rc=2,  10 stdout lines, stderr empty
bash $S overdue  --root $R --today 2026-10-19                # rc=2, 478 stdout lines, stderr empty
bash $S census   --root $R --today 2026-10-19 $P             # rc=1, 126 stdout lines, stderr empty
bash $S validate --root $R --today 2026-10-19 $P             # rc=2,  25 stdout lines, stderr empty
bash $S shared   --root $R --today 2026-10-19 $P             # rc=2,   5 stdout lines, stderr empty
bash $S overdue  --root $R --today 2026-10-19 $P             # rc=2, 473 stdout lines, stderr empty
bash $S selftest                                             # rc=0, 57 lines = 56 checks, all "killed" + "selftest ok"
bash $S --help                                               # rc=0 (usage header lines)
```

Shorthand used below: **roster mode** = no lane arguments (targets built from `shokunin.conf`,
lane labels are the conf lane ids) and **dir mode** = the 21 explicit `*-shokunin` paths (lane
labels are directory basenames). `--today 2026-10-19` was passed in every run, so no run depends on
the machine's UTC date.

## 2. Census counts (PROVISIONAL)

FLEET lines are byte-identical in both target modes:

```
FLEET rows 488 | tier.A 420 | tier.B 28 | tier.C 40 | tier.invalid 0
FLEET status.queued 192 | status.mined 253 | status.rejected 43 | status.invalid 0
FLEET missing 4 (dir mode)   /   FLEET missing 6 (roster mode)
```

`rows = tier.A+tier.B+tier.C` and `rows = queued+mined+rejected` hold for the fleet total and for
every lane individually.

Per-lane (dir mode; roster mode prints the same numbers under conf lane ids):

| lane | rows | A | B | C | queued | mined | rejected | missing |
|---|---|---|---|---|---|---|---|---|
| chousa | 18 | 14 | 1 | 3 | 7 | 8 | 3 | |
| game-dev-3d | 36 | 33 | 2 | 1 | 28 | 6 | 2 | |
| kagi | 16 | 14 | 0 | 2 | 1 | 14 | 1 | |
| kake | 18 | 16 | 0 | 2 | 2 | 14 | 2 | |
| kama | 30 | 27 | 0 | 3 | 8 | 17 | 5 | |
| kasegi | 27 | 25 | 0 | 2 | 10 | 15 | 2 | |
| kengaku | 26 | 24 | 0 | 2 | 5 | 18 | 3 | |
| kotoba | 11 | 10 | 0 | 1 | 6 | 4 | 1 | |
| kotodama | 47 | 34 | 6 | 7 | 22 | 20 | 5 | |
| lore | 32 | 24 | 3 | 5 | 17 | 12 | 3 | |
| mado | 39 | 35 | 1 | 3 | 9 | 27 | 3 | |
| mori | 34 | 31 | 2 | 1 | 21 | 12 | 1 | |
| revenger | 15 | 14 | 0 | 1 | 1 | 12 | 2 | |
| souji | 33 | 29 | 3 | 1 | 15 | 16 | 2 | |
| tabi | 28 | 22 | 4 | 2 | 6 | 20 | 2 | |
| tameshi | 44 | 37 | 5 | 2 | 29 | 12 | 3 | |
| tsukuroi | 34 | 31 | 1 | 2 | 5 | 26 | 3 | |
| audio | — | — | — | — | — | — | — | `<root>/audio-shokunin/corpus/SOURCES.md` |
| game-dev-2d | — | — | — | — | — | — | — | `<root>/game-dev-2d-shokunin/corpus/SOURCES.md` |
| kaidoku | — | — | — | — | — | — | — | `<root>/kaidoku-shokunin/corpus/SOURCES.md` |
| kumitate | — | — | — | — | — | — | — | `<root>/kumitate-shokunin/corpus/SOURCES.md` |

Roster-mode additions (not a discrepancy in the corpus, a roster difference): `protocol` and
`aggregator` are conf lanes whose repo is `.` → both resolve to `<root>/corpus/SOURCES.md`, which
does not exist (fleet root has no `corpus/`), so they add 2 `missing` lines and 0 rows; and the 3
physical dirs absent from `shokunin.conf` (`audio-shokunin`, `game-dev-2d-shokunin`,
`game-dev-3d-shokunin`) are auto-added with an `unlisted` marker line (rows for game-dev-3d = 36,
the other two contribute `missing`). Hence 6 missing / 23 targets in roster mode vs 4 missing / 21
targets in dir mode. Zero `tier.invalid` and zero `status.invalid` in both modes.

## 3. Independent reconciliation probe (different implementation, read-only)

An independent Python pass over the same 17 files, re-deriving rows/tier/status from the same
`## Registry`-section rule, reproduced the census exactly:

```
rows 488 | tier A 420 / B 28 / C 40 | status queued 192 / mined 253 / rejected 43
```

Additional independent checks (all clean):

- **Indented registry rows: 0** in all 17 files (`^[ \t]+\|[ \t]*S[0-9]{3,}[ \t]*\|` → no matches).
  Consequence (PROVISIONAL, and the reason this seat is provisional): on the *currently committed*
  corpus the known `^\|` row filter and the `'|'*` first-char test in `usedby_findings` skip
  nothing — the in-progress indentation fix changes today's row totals by **0 rows**. It is a
  latent-robustness fix, not a correction of the present numbers. It says nothing about lanes that
  later author indented rows.
- Registry-section `|`-led lines that are not header/separator and not `S\d{3,}` ids: **0**.
- `NF != 13` rows: **0**. Duplicate ids: **0**. `kind` values ⊆ the 9-value enum.
- Rows outside `## Registry`: **0** (E12 clean corroborated). All 17 files use the exact heading
  `## Registry`; none uses a variant heading, so no lane silently reports `rows 0`.
- Mined rows with `used-by = —`: **0** (no W03), thin rejected rows: **0** (no W02); every
  `used-by` path of every mined row resolves on disk (E11 clean corroborated).
- Cadence classification of all 488 rows: `NNd` 249, symbolic 220, ISO date 19 (249+220 = 469
  cadence lines; ISO rows produce no cadence line — see §5).

## 4. Validate: warnings vs errors (PROVISIONAL)

`validate` printed **zero `E` lines** in both target modes (`grep -cE '\tE[0-9]+\t'` → 0) and
exactly **four `W` lines**, identical in both modes:

```
lore-shokunin  W01  S027 tierC mined used-by=corpus/knowledge/r103-canon-status-and-supersession.md
lore-shokunin  W04  S017 duplicate url arxiv.org/html/2603.05890 across scopes
lore-shokunin  W04  S032 duplicate url www.iso.org/standard/70908.html across scopes
mado-shokunin  W04  S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
```

Warning vs error behavior actually observed:

- W codes do not change a lane's status: `lore` and `mado` emit their W lines **and** `ok <path>`,
  and W codes never raise the exit code (script contract; consistent with these runs, which have
  W-only registries and non-zero exit only from the missing-registry path).
- No E finding exists in the current corpus, so exit-1-from-E was **not** observable here; the
  script's ordering makes `missing_error` (exit 2) precede `findings` (exit 1), i.e. a run with
  both missing registries and E findings reports 2 — exit 2 must not be read as "clean". Observed
  coupled evidence: `rc=2` with zero E lines and zero overdue rows.
- `census` exits 1 when any target lacks `SOURCES.md` (`rc=1` in both modes, missing 4 / 6).
- `unlisted` marker lines are informational: `game-dev-3d` is unlisted yet fully counted and
  validated `ok`.

Cross-checks that explain the W codes without contradicting them: the 6 same-URL+same-scope groups
my naive pass flagged in `kotodama` are exempt from E04 by explicit `supersedes S0xx` text in
`teaches` (S044→S034, S045→S038, S046→S039, S047→S029), so the script's zero-E04 result is correct,
not a hole in that case.

Latent weaknesses noticed while reconciling (no impact on any current total or finding; recorded
for the parent, not scored):

1. `symbolic()` accepts any word (`^[A-Za-z][A-Za-z0-9 _-]*$`): `kama S030` has
   `recheck=every round`, reported as cadence and never E09. Placeholder tokens like `todo`/`unknown`
   would pass the same way.
2. The `supersedes S[0-9]{3}` E04 exemption is not integrity-checked: 8 refs across the corpus; 7
   point at the same normalized URL (5 also same scope), but `game-dev-3d S036 → S011` names a
   different URL and scope, and no check verifies the target id exists in the same lane.
3. Lane labels are invocation-dependent (conf ids `kama`/`lore` vs dir basenames
   `kama-shokunin`/`lore-shokunin`), so per-lane census keys from roster and dir modes are not
   directly comparable; only the FLEET lines matched field-for-field.

## 5. Overdue / cadence (fixed date 2026-10-19)

`overdue --today 2026-10-19`: **0 rows judged overdue** in both modes (`awk '$2=="overdue"'` → 0);
469 `cadence` lines in both modes (dir mode: 469 cadence + 4 missing = 473 lines; roster mode:
469 + 6 missing + 3 unlisted = 478 lines). No overdue line means the days-sorted block was empty,
so the `sort -k2 -rn` ordering path was not exercised by real data.

Recheck-token distribution over the 469 cadence lines:

```
on-release 211 | 90d 97 | 180d 80 | 365d 62 | 730d 10 | on-change 5 | on-commit 2
on-gate-change 1 | every round 1
```

The 19 rows carrying an ISO `recheck` date emit no cadence line and are the only rows eligible for
a date-based overdue verdict: earliest is `2027-01-17` (all 19 are `kengaku` rows, opened recent),
so none is due on 2026-10-19. `on-release`/`on-change`/… rows are reported (never judged overdue),
and `NNd` rows are due only at `opened + N days`; every opened date observed is recent, hence the
zero-overdue result. The built-in selftest independently covers the `opened + N days` boundary
(`cadence-due-on-opened-plus-N`), symbolic reporting, and "invalid recheck is not overdue" — all
killed.

## 6. Shared

`shared` printed exactly one URL present in ≥2 lanes (both target modes, differing only in label
style):

```
kubernetes.io/docs/concepts/workloads/pods/probes   shared   kama-shokunin,mori-shokunin   (dir mode)
kubernetes.io/docs/concepts/workloads/pods/probes   shared   kama,mori                    (roster mode)
```

Rows behind it: `kama S017` and `mori S028`. An independent pass (host-lowercased, fragment and
trailing slash stripped — the same normalization the script applies) found the same single
multi-lane URL and no other. `shared` still exits 2 here, because missing registries set the same
`missing_error` flag in every non-census mode.

## 7. Selftest and fixture coverage

`bash scripts/sources-census.sh selftest` → 57 output lines, all 56 checks `killed`, final line
`selftest ok`, rc 0. `scripts/fixtures/sources-census` holds 8 files and contains **no** indented
pipe-led row (`^[ \t]+\|` → 0 matches). Therefore the current 56/56 selftest says **nothing** about
indented-row handling: the in-progress parser correction must ship its own fixture, and that fixture
must be shown to fail against the pre-fix script.

## 8. Exact reruns owed after integration

Run every item after the parent's parser correction lands and after the parent's parity check
confirms which script copy is canonical; all commands as written (cwd `/home/vgpnk/Projects/shokunin`):

1. `bash scripts/sources-census.sh selftest` → expect 57 lines, 56 `killed`, `selftest ok`, rc 0,
   **plus** a new indented-row fixture that fails on the pre-fix script and passes post-fix.
2. Pre/post byte diff on the frozen corpus: `census --root /home/vgpnk/Projects/shokunin --today
   2026-10-19` and the same with the 21 explicit `*-shokunin` dirs → expect byte-identical stdout
   (0 indented rows today) and rc 1 both times. Any non-zero diff means lanes changed or the fix
   altered row matching.
3. Same pre/post diff for `validate` (expect the 4 W lines above, 0 E lines, rc 2), `shared` (expect
   the one kama/mori URL, rc 2), `overdue --today 2026-10-19` (expect 0 overdue, 469 cadence, rc 2).
4. Re-read the 21 lane HEADs and `corpus/SOURCES.md` sha256s immediately before the rerun; if any
   lane advanced past the hashes in §0, the counts must be re-read, not carried over.
5. Indentation coverage is two-sided: if row matching becomes indent-tolerant, verify
   `usedby_findings`' `'|'*` first-char test moved with it — otherwise E11 stays indent-blind.
   Concrete fixture: a mined row indented by whitespace whose `used-by` path does not exist → E11
   absent pre-fix, present post-fix.
6. `tier.invalid` / `status.invalid` must stay 0; `rows = Σtier = Σstatus` must hold per lane and for
   FLEET; `shared` must still report exactly one URL unless a lane legitimately adds one.
7. Nothing is frozen or appended to README/LOG/SCORECARD/reports/MANIFEST until the parent emits the
   exact `FINAL LANES READY` signal.

## 9. Limits and cleanup

- Modes exercised: `census`, `validate`, `shared`, `overdue`, `selftest`, `--help`. **Not**
  exercised: `--file`, `--out`, `--verbose`, `--root` default derivation from `$SHOKUNIN_ROOT`/
  script dir, `-h`-vs-unknown-option paths, and the `--today` UTC default (I always passed the fixed
  date). The `--out`-not-truncated, canary/injection, TZ and gawk-failure behaviors are covered only
  by the selftest, not re-derived here.
- The corpus audit gate (`.ufo/waves/round-9/corpus-gate.mjs`) was not invoked by this seat; a gate
  pass or the zero-E validator result above is **not** semantic conformance of the corpus. This seat
  asserts counts and script behavior only: r2/r4/r7/r8-literal/r10/SHONEN form, r1/r3/r5/r6/r9,
  verifier independence and SHONEN truth remain not-evaluated.
- Read-only against all 21 lane repos and all fleet config/report/gate files; no lane, no manifest,
  no report touched. Scratch: transient stdout/stderr captures under `/tmp/kaika-r12/` (created and
  then removed; the numbers above are transcribed from them). This note is the only artifact written.
- Concurrent-activity observation (not this seat's writes): at the time of the read-only checks three
  lane working trees carried untracked paths — `game-dev-3d-shokunin/reports/round-107/`,
  `kama-shokunin/.ufo/round-10/{SEAT-PROTOCOL.md,plan.json}`, `lore-shokunin/.scratch/` — and the
  fleet root showed `M README.md`. No lane's `corpus/SOURCES.md` was dirty in any lane, so the
  revision binding in §0 is unaffected; the untracked paths are outside every file this census reads.
- The independent counts in §3 come from a re-implementation over the same files, not from the
  script; agreement therefore supports (does not prove) the totals, and both remain provisional.