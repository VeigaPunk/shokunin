# D5 canonical-sync — independent review (read-only)

Reviewer: `D5CanonicalReview`. Artifact: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kimi-shokunin-canon`
(branch `kaika/canon-sync`), uncommitted changes from base `b3ca98f` (merge-base verified `b3ca98f`).
Fleet comparison tree: `/home/vgpnk/Projects/shokunin` (read-only). No repository or fleet file was
modified; all probe output is under `/tmp/kaika-verify/d5-canonical-review/`.

**Verdict:** no blocking regression found in the reviewed diff. 2 medium and 9 low actionable
findings, none of which invalidates the sync; the one open *decision* (manifest vocabulary) was
already reserved to the operator by the campaign's own W1 audit (D11b).

---

## 0. Artifact state, method, limitations

- Diff reviewed: 21 tracked files, +892/−274, plus untracked `scripts/sources-census.sh` (653 lines,
  sha256 `aed9ed65…`), `scripts/fixtures/sources-census/` (8 files), `templates/mint/corpus/SOURCES.md`.
- On the assignment's instruction not to re-run the harness: no tests/lints/builds were executed.
  Runtime verification is another seat. The probes below are read-only function/data probes.
- **`lsp` is not mounted in this runtime** (`xd://` lists 209 devices; none is `lsp`). No
  `references`/`definition`/`diagnostics` were available; direct reads and grep were the fallback.
  No language server applies to the reviewed bash/markdown/JSON anyway, but the limitation is recorded.
- No JSON-Schema validator is installed (`python3 -c "import jsonschema"` → ModuleNotFoundError; the
  W1 audit records ajv/check-jsonschema absent). Schema conformance was checked with a hand-rolled
  structural walk of the constrained properties over all 312 real ledger entries, not full
  draft-2020-12 validation.
- Post-review byte-sync: the corrected census script (fix commit `ff701da`, merged into
  `fleet-ledger` at `b38d358`, sha256 `a621fe0e…`) had **not** landed in the canonical worktree
  at review time. Section 3 reviews that narrow delta against the old bytes (committed in
  `fleet-ledger`, not yet copied into canonical).

## 1. Verified-good (assignment criteria)

1. **Installer ships the new artifacts.** `install.sh:27-30` requires `scripts/sources-census.sh`,
   the watchdog, the new `templates/mint/corpus/SOURCES.md`, and `bash -n`s all three scripts
   (`install.sh:37`). `bash install.sh` → rc 0 on the tree.
2. **Mint seeds the new registry.** `mint-agent.sh:66` copies the kit recursively
   (`cp -R "$TEMPLATES/."`), so the new `corpus/SOURCES.md` seed lands; its only token is `<name>`,
   substituted at `mint-agent.sh:69-73`, producing the contract header
   `# SOURCES — where <id> learns` (matches all fleet lane headers).
3. **Schema additions permit the real new entries without weakening existing fields.**
   All 18 real `trends` objects have exactly `expansion|quality|discernment` with in-enum values;
   all 57 `supersedes` objects carry exactly `round,type,date` (`entry` as an int on 45 of them) and
   all still pass `additionalProperties:false`; `lane`/`lane_round` are pattern/int-valid on every
   entry that has them. No property was removed or loosened.
4. **Source gate reports conformance, not a fabricated pass.** `sources-census.sh validate` emits
   E/W rows and `ok` only when zero E findings exist; W codes never flip status/exit
   (`sources-census.sh:1-36`, exit block at EOF). Live read-only runs agree with the frozen manual
   commands: `kama` rows 30 = 30, malformed 0 = 0, `validate` → `ok`, rc 0.
   Fleet-wide: 488 rows, 0 E findings, rc 2 only because 6 registries are missing
   (2 main-repo + `audio`, `game-dev-2d`, `kaidoku`, `kumitate`).
5. **Watchdog's report gate tightened without breaking real reports.** 284 report files checked with
   the exact new regex; 110 lack a SHONEN heading, and **0 of those would have passed the old
   regex** — the tightening introduces no new rejection.
6. **Canonical runtime works with both shipped templates.** `render_prompt` probe with axes
   `depth/coverage & ops` and the fleet's live template: zero leftover `{{…}}`/`<{{`, hostile bytes
   rendered literally, `Working dir:` resolved to the lane cwd (`shokunin-watchdog.sh:122-139`;
   D05/M1/M2 fixed).
7. **Canonical stays authoritative and substrate-neutral.** No `/home/…`, `~/…`, or live model
   aliases in the tree; appendix alias mentions are host-notes that neutralize them; the fleet's
   hardcoded `~/.agents/skills/godspeed/directive.md` did **not** leak (canonical
   `round-prompt.md:91` says "the host's Godspeed skill binding"), and the stray `| godspeed`
   artifact was removed. README/schema/SKILL/mint-agent no longer call the fleet "upstream".
8. **Protocol invariants preserved.** lowest non-retired axis (`AXES.md:25-35`, `round-prompt.md:14-15`,
   `SKILL.md:53-59`); independent non-author verifier (`AXES.md:47`, `LEARNING.md:49`, `SKILL.md:64`);
   no scalar averaging (`AXES.md:30-36`, `round-prompt.md:36-38`, `SKILL.md:25`); 1–3 causally
   separable claims on distinct axes, two claims on one axis = one (`AXES.md:25-35`,
   `round-prompt.md:14-24`); append-only ledger and SOURCES rows (`MANIFEST.schema.json:5`,
   `CORPUS.md:115`, `PROTOCOL.md:258-266`).
9. **Same-identity rerouting intact.** Commits still carry `<lane>-shokunin <lane>@shokunin.local>`
   (`shokunin-watchdog.sh:237-243`); launches tag `SHOKUNIN_LANE`/`SHOKUNIN_ROUND` and kill only a
   group whose leader carries the tag (`:143-216`). No untagged live lane exists today (all
   `.ufo/state/*.mission` pids are dead), so the upgrade path is clean.
10. **Honest saturation.** The nudge requires both the saturation line and stagnation window in
    `SCORECARD.md` (`AXES.md:68-70`); no score is minted without a re-derivable command
    (`AXES.md:52-54`).

## 2. Findings (severity order; file:line; minimal repair)

### F1 — MEDIUM — canonical schema still false-fails 80 real ledger entries (type) and 24 lane cells (`closed`)
`templates/MANIFEST.schema.json:94-95` (`type` enum), `:108` (`lanes` enum), framing changed at `:5`.
Real `MANIFEST.json` (312 entries): **80 fail `type`** — 63 `train`, 9 `craft`, 2 `train+audit`,
1 `train+audit+unlock`, 5 missing (`rounds[272,277,279,291,293]`, which also miss required `date`);
**24 lane cells are `closed`**, absent from `{ok,failed,not-dispatched,in-flight}` (`rounds[142..165]`).
The diff's added fields all validate (see §1.3); the failing enums are untouched by this diff and the
campaign already reserved the choice to the operator (`.ufo/waves/kaika-w1/manifest.md` §2 and
recommendation 2: "schema PR upstream adds `entry` … and the four missing `type` values"; D11(b)
"the operator must choose"). The diff *did* complete the `entry` half and the new framing now claims
authority, so shipping without the second half leaves a canonical schema that rejects its own
fleet's verdict-era rows.
**Minimal repair (1–3 lines, operator's call per D11b):** add `train`, `craft`, `loop` to the `type`
enum (either add the two compound historical values or name them in the description as read-only
history), and add `closed` to the `lanes` enum **or** one description sentence stating that
pre-regime rows are tolerated history and only canonical-regime appends are validated. Do not
rewrite old entries.

### F2 — MEDIUM — gate-failed retry reuses the failed attempt's report as the completion signal
`scripts/shokunin-watchdog.sh:308-310` (retry branch), `:108-114` (`report_of`), `:332-341` (tick).
When `sources_gate` returns 1, the driver relaunches the same round (`:310`) but leaves
`.ufo/reports/round-<n>/<lane>.md` from the failed attempt in place. `report_of` is therefore true
immediately; the first tick after the retried lane is live calls `advance` (`:332-336`) and, once the
census passes, `kill_mission` (`:302`) kills the freshly relaunched lane and logs
`complete … advancing` on the **stale** report bytes. Today the branch is cold (0 E findings
fleet-wide), but it is the new gate's only remediation path.
**Minimal repair:** before `launch_lane "$lane" "$n"` in the blocked branch, rename the report aside
(e.g. `mv "$UFO/reports/round-$n/$lane.md" "$UFO/reports/round-$n/$lane.md.pre-retry-$(date +%s)"`),
so the retry must land fresh content before `report_of` can close it.

### F3 — LOW — round contract says "exit 0 required at round end"; the driver advances on census rc 2
`templates/round-prompt.md:55` vs `scripts/shokunin-watchdog.sh:278-284` (rc 0 pass, rc 1 block,
everything ≥2 logged as warning and skipped). This matches the ratified driver spec
(`.ufo/waves/kaika/w2-fleet-tasks.md:142`: "2 = census missing → skip with a logged warning"), but the
lane-facing contract calls exit 0 mandatory. Four live child lanes have no registry at all
(`audio`, `game-dev-2d`, `kaidoku`, `kumitate`; `validate` → rc 2), so the frontier duty is
unenforced for exactly the lanes that never started it; the only record is a `watchdog.log` line
(driver runtime, churns every tick — `PROTOCOL.md:480-483`).
**Minimal repair (pick one):** amend `round-prompt.md:55` to state that a missing registry (rc 2) at
round end is a logged conformance defect, not a blocker; or make the driver block/record rc 2 as a
round-note conformance defect for child lanes. Keep the ratified "skip" only for the census
instrument being absent.

### F4 — LOW — installer does not gate the census fixtures the shipped tool needs
`install.sh:27-30` gates `scripts/sources-census.sh` and the new `templates/mint/corpus/SOURCES.md`
but not `scripts/fixtures/sources-census/`. `sources-census.sh:93-94` and its selftest read
`$FIX/root` and `$FIX/injection-shokunin/corpus/SOURCES.md`; a tree missing them passes `install.sh`
(rc 0 today) and fails only at `selftest` (exit 3). The comment at `install.sh:25-26` promises a
partial tree "fails loudly".
**Minimal repair:** one line — `[ -d "$STAGE_DIR/scripts/fixtures/sources-census/root" ] || fail "missing fixtures: scripts/fixtures/sources-census"`.

### F5 — LOW — `sources-census.sh --help` truncates the usage block (drops the `shared` mode)
`scripts/sources-census.sh:41` prints lines `2,33`, but the header block ends at line 36: the
`shared:` mode (line 36) and the symbolic-cadence tail (34-35) are never printed.
**Minimal repair:** `sed -n '2,36p' "$0"` (same defect in the corrected bytes, line 41).

### F6 — LOW — canonical `CORPUS.md` layout tree omits `SOURCES.md` the diff adds
`skills/shokunin/protocol/CORPUS.md:10-15` lists `README.md`, `QUALITY.md`, `knowledge/`, `lessons/`
only, while the same file adds the SOURCES contract at `:62+`, `LEARNING.md:64` lists
`corpus/SOURCES.md`, and `PROTOCOL.md:444` adds the repo-file row. The fleet's copy has the tree line;
the canonical dropped it during the sync.
**Minimal repair:** add `  SOURCES.md       — curated source registry (contract below)` inside the block.

### F7 — LOW — canonical contract carries fleet-local evidence paths and fleet-wide counts
`skills/shokunin/protocol/CORPUS.md:149-160`: "## Rules added from the kaika campaign" with
`Evidence: .ufo/waves/kaika-w1/mistakes.md … art-curation.md, critic.md` and "From the fleet root,
2026-10-19: 683 knowledge files … 312 carry `recheck:`". The rules are host-neutral; the evidence
pointers and counts are deployment state. (The file already had this style at `:28-31`, and the
appendix is the designated incident digest, so this is a consistency cleanup, not a regression.)
**Minimal repair:** keep the rules, replace the `Evidence:` block with a pointer to the appendix row
(or add an appendix row for these rules) and drop the fleet-wide counts from the contract.

### F8 — LOW — where the fleet root must keep the new instruments is undocumented
`templates/shokunin.conf.example:6-8` defines `SHOKUNIN_ROOT` as "the repo holding MISSION.md,
AXES.md, MANIFEST.json, .ufo/" — no `scripts/`, no `templates/`. The driver hardcodes
`$SHOKUNIN_ROOT/templates/round-prompt.md` (`shokunin-watchdog.sh:46`) and now
`$SHOKUNIN_ROOT/scripts/sources-census.sh` (`:269`); every lane prompt hardcodes
`{{FLEET_ROOT}}/scripts/sources-census.sh` (`round-prompt.md:61`). The fleet's PROTOCOL.md row that
named the census tool was dropped in this sync (`PROTOCOL.md:444` no longer mentions it). If the
operator follows the conf comment, the renderer fails every launch (`launch-fail`) and the gate
silently warns/skips (`:274-276`).
**Minimal repair:** one line in the conf example's `SHOKUNIN_ROOT` comment (and/or the README fleet
block) naming `scripts/` + `templates/round-prompt.md` as required fleet-root contents; optionally
restore the tool mention in `PROTOCOL.md:444`.

### F9 — LOW — PID/tag liveness depends on Linux `/proc`; failure mode is a relaunch storm
`shokunin-watchdog.sh:182` and `:211` read `/proc/$mid/environ`. On a host without `/proc` (or with
environ hidden), `mission_live` returns false for every lane, so each tick logs
`lane-dead-no-report` and launches another process for the same round while the previous lane still
runs (the H6 shape the design set out to remove). The header (`:1-5`) claims substrate neutrality
without stating Linux-only.
**Minimal repair:** state Linux-only in the header/README, or fall back to a group-only liveness
check when `/proc/$mid/environ` is unreadable.

### F10 — LOW — "Trend verdicts" is a required conformance item with no automated logger
`round-prompt.md:112-118` and `PROTOCOL.md:158-166` make both new sections status-neutral
conformance items; the driver logs only a missing `Sources & frontier` heading
(`shokunin-watchdog.sh:250-262`). Absence of the trend verdicts is therefore unobserved by every
shipped instrument (left to the integrator's closure review).
**Minimal repair:** either add the matching `Trend verdicts` heading check/log beside the Sources
check, or say explicitly in `round-prompt.md`/`PROTOCOL.md` that only Sources & frontier is
driver-logged.

### F11 — LOW — corrected census accepts 0–3-space rows; the contract and tool header do not say so
Fleet-ledger corrected bytes: `usedby_findings` regexes `:459-460,463-471`, gawk normalisation
`:528-535`, comment `:492`. The frozen manual census commands in `CORPUS.md:130-147` (which
`round-prompt.md:57-58` calls "the specification") still anchor `^\|`/`^## ` with no indentation,
and neither the tool header nor `CORPUS.md` documents the tolerance. A registry indented 1–3 spaces
passes the gate but the contract's manual commands under-count it.
**Minimal repair:** one sentence in the `CORPUS.md` Census block ("headings and table rows may carry
0–3 leading spaces; 4+ is an indented code block and is ignored") and/or the tool header.

## 3. Post-review narrow byte-sync (census fix `ff701da` / fleet-ledger `b38d358`)

Observed at review time: canonical `scripts/sources-census.sh` = old bytes, sha256 `aed9ed65…`
(28 161 B); corrected script in `fleet-ledger` = sha256 `a621fe0e…` (32 552 B, 20:46). The fixtures
trees are byte-identical between the two worktrees (`diff -r` empty), so no fixture change travels
with the copy. Delta reviewed (+81/−9 lines, 127-line diff):

- Selftest adds indent 0/1/2/3 cases for census rows, validate (E06 + E11), overdue, E12 outside
  Registry, and a two-lane `shared` case; each valid fixture also embeds a 4-space-indented
  `## Paths` + row with invalid tier/status that must be ignored (`:209-271`). The 4-space row is
  asserted not to count and not to flag — the code exclusion is exercised, not just claimed.
- Parser: headings/table rows now match `^ {0,3}` and lead spaces are stripped before cell parsing,
  in both `usedby_findings` and the gawk pass. This matches CommonMark (≤3 spaces is still a
  heading/table; 4 is code), keeps E11 on the same rule, and keeps E12 catching indented
  out-of-Registry rows. Exit-code block, options, output shapes, and `--file/--root/--out` handling
  are untouched.
- Narrow live re-verification with the corrected bytes (`validate --root /home/vgpnk/Projects/shokunin`,
  read-only): rc 2, 0 E findings, 17 lanes `ok`; normalised output is identical to the pre-fix run,
  so the correction is behaviour-preserving on the fleet's unindented registries.
- Selftest check count rises 56 → 93 (parent receipt: 93 killed / 0 survivors; shellcheck 0;
  `.ufo/waves/kaika-w3/census-indent-final-smoke.txt`). Not re-run here per the no-test assignment.
- **Integration note (not a defect):** the fleet-root copy `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`
  is still `aed9ed65…`, i.e. the running deployment's gate uses the pre-fix parser until the ledger
  fix is merged into the fleet root. The canonical copy alone does not update the deployment.
- F5 (usage truncation) and F11 (tolerance not documented) persist in the corrected bytes.

## 4. Residual risk / verification gaps (not actionable findings here)

- W1's fleet-ledger data defects remain outside this diff and still need appended corrections:
  `rounds[138].round = null`; `rounds[1]` not-dispatched without `closed_at`; the 5 type-less kotodama
  rows (`MANIFEST.json` in the fleet root is not a repo under review). W1 §8.3 owns them.
- `verdicts` / `claims` remain undescribed in the schema (allowed because `roundEntry` has no
  `additionalProperties:false`); the amendment that introduced multi-claim rounds still leaves the
  per-claim/per-axis evidence keys undocumented. D11(b) bundled this with the operator decision.
- No full JSON-Schema validation was possible on this host; the structural walk covered every
  constrained property but not format/`allOf` edge cases beyond those named.
- The watchdog loop itself was not run (T-DRIVER forbids it); conclusions about `advance`/retry are
  from source and function-level probes. `report_of`, `render_prompt`, the census, and the schema
  data checks were exercised read-only.

## 5. Evidence commands (reproducible, read-only)

```
sha256sum <canon>/scripts/sources-census.sh <fleet-ledger>/scripts/sources-census.sh
git -C <canon> diff b3ca98f -- <file>                     # per-file diffs
python3  # structural walk of MANIFEST.json vs templates/MANIFEST.schema.json constrained props
<canon>/install.sh                                        # rc 0
<fleet>/scripts/sources-census.sh validate --root <fleet> [lane]   # rc/rows/EW output
<fleet-ledger>/scripts/sources-census.sh validate --root <fleet>   # corrected-bytes re-check
LC_ALL=C grep -qE -f pat-new.txt <report>                 # 284 fleet reports, old-vs-new regex
source <canon>/scripts/shokunin-watchdog.sh; render_prompt <lane> <n>   # in /tmp probe fleet
```
