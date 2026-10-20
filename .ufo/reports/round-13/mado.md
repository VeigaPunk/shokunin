# mado — round 13 (attempt 1), 2026-10-20

## Work performed

Declared claims: **C1 — coverage:** sourced current-art ground U1–U3 → U1–U4, separating protocol phase, advertised globals and unexercised behavior. **C2 — operability:** complete missing/extra diagnostics in four isolated source/local-file census cases. C1 works the previous lowest-scoring sub-axis. These are causally separable; the U4 entry needs no census implementation, and the census needs no U4 entry. No exploratory claim.

**Local verdict:** both claims verified improved; **admission pending** the parent's fresh non-author closure. No retained axis harm was observed. The temporary data-fence defect below is disclosed, not treated as a clean capture.

- Admitted one author-gated U4 entry, `mado-shokunin/corpus/knowledge/wayland-protocol-boundaries-r13.md`, with primary phase/governance/core-registry sources, sanitized host advertisements and explicit diagnostic-client bindings/detail queries. README and SKILL route to it. Evidence: S005, S040–S043, S046; lane `95cbc41fe5d5db121b89c2ddd1f953728663c5f4`; `LOG.md:769-809`.
- Replaced set-blind source/local presence checks with named expected/observed differences, preserving positional include-order checks and target existence. gkeep is an observed baseline member, not an ownership or operator-intent endorsement. Empty sources fail safely; unsupported `# hyprlang` directives fail closed rather than being parsed as inert comments. Evidence: `tools/mado-verify.sh:2305-2485`; `.ufo/waves/round-13/evidence/after.txt`.
- Preserved the original historical mutation spec (`c7ee75b9…`), re-cut the target after a real 10/10 kill sweep, and killed eight separate covering mutants over the derived executable, not through pin-identity assertions. Evidence: `evidence/{regression-recut,covering-mutants}.txt`, `historical-results.tsv`, `covering-results.tsv` under the lane's `.ufo/waves/round-13/`.
- Registered the gate modes, source-merge screen, measurement probe and frozen-regression companion in `SKILL.md` § Gate registry. The companion verifies committed gate/harness digests **before** execution; selftest and a frozen replay both ran. Evidence: `.ufo/waves/round-13/frozen/{verify.py,expected.json,gate.sh,harness.sh}` and `evidence/frozen-regression.txt`.
- Learned the prior outside S030 disagreement into QUALITY criterion 17; the new screen rejects the actual historical admitted S017/S030 pair despite different scope wording, but permits rejected history and valid supersession. Corrected the U2 citation mapping, S006 revision debt and the wrong gate re-anchor authority append-only. Evidence: `corpus/lessons/round-13.md` § Mistakes/Gate; `corpus/QUALITY.md:32-39`; `evidence/collision-{selftest,red-corrected,green-corrected}.txt`.
- Dispatched **one validated native wave, 32 seats**: 8 executor, 7 scout, 4 connector, 5 reviewer, 4 critic, 2 scribe, 1 sentinel, 1 revenger. L1 held the canonical planner seat; PlanningWalk was a connector-routed bounded data walk. Role routing used session configuration, no model parameters or routing edits. Godspeed directive bytes were included, and the validator's taskCall was passed unchanged in one call. Evidence: `.ufo/waves/round-13/w1/{spec.json,dispatch.json,assignments.json,reports/swarm-registry.json}`. All seats, including continuations, finished before L1 verification and final commits.

**Tool installation:** `wayland-utils 1.3.0-1`, pacman extra, `sudo pacman -S --needed --noconfirm wayland-utils`, to obtain the assigned `wayland-info` diagnostic. GlobalCapture read `/home/vgpnk/.omp/agent/RULES.md` first. No partial/full system upgrade. Installed package evidence: `.ufo/waves/round-13/evidence/packages.txt`; opening/probe record: `w1/GlobalCapture.md`.

**Safety and honest failures:** Safety found two world-readable raw Wayland scratch outputs; their owner deleted both and corrected the capture report. Only interface/version projection is retained and pushed. The first frozen selftest raised `UnboundLocalError`; the sole counter-scope correction produced 12/12 on the same self-invocation. Initial source-screen calls used an incorrect positional CLI (argparse 2); the exercised rejection proof uses `--registry`. L1's first safe inventory replay lacked WAYLAND_DISPLAY and correctly returned UNKNOWN; an explicit previously correlated socket prerequisite then reproduced the capture digest. Evidence: `w1/Safety.md`; `evidence/{frozen-selftest,frozen-selftest-corrected,collision-red,collision-red-corrected,globals-recheck,globals-recheck-bound}.txt` and `session-prerequisites.json`.

## Landed changes

**Pushed lane HEAD before this report was written:** `59cfbdc3ab5e7b6aaf68f86e1b2ae8d51c938b1e` on the mado remote. The final `git status --porcelain` after push printed nothing. Initial inherited lane state was clean at `7dcb785b7b943d03703181b218d7860a7b43007b`; no earlier-attempt output was inherited or discarded. No aggregator/operator file was swept.

| Landed change | Carrying commit | LOG binding |
|---|---|---|
| U4 entry; SOURCES/QUALITY/index/SKILL; append-only U2, drift and standing-use corrections | `95cbc41fe5d5db121b89c2ddd1f953728663c5f4` | `LOG.md:769-809`, `:839-866` |
| Census implementation and hermetic cases; preserved historical spec, re-cut pin, covering mutants; source screen and digest-pinned frozen companion | `95cbc41fe5d5db121b89c2ddd1f953728663c5f4` | `LOG.md:811-849` |
| Validated wave, native assignments, completed seat artifacts and exercised verification evidence | `95cbc41fe5d5db121b89c2ddd1f953728663c5f4` | `LOG.md:859-878` |
| Committed-revision after measurement, byte bindings, per-claim SCORECARD results and final closure entry | `59cfbdc3ab5e7b6aaf68f86e1b2ae8d51c938b1e` | `LOG.md:880-915` |

Gate SHA-256 at the measured content commit: `037b05dcd3f86e12e1b89ee5631f76ce95301b7c411957fad17ff0d7438a6569`, identical to the frozen gate input. S041 capture SHA-256: `ced47240c2a1941bbbf1f125d9a1e41624cfeeb8218ab2a3a425eb335a08a949`. Re-derive with `git show <measured-commit>:<path> | sha256sum`; exact paths/full digests are in `.ufo/waves/round-13/evidence/committed-bindings.json`.

Cross-domain boundary: OS/kernel/input-device and DRM diagnosis remain tsukuroi-owned; secrets remain kagi-owned. No such defect was absorbed or remediated. The sanctioned diagnostic package installation above is explicit. Configuration trees, compositor actions, operator gkeep project and sibling repositories were not edited. The copied harness is a frozen read-only input with preserved attribution, not a sibling modification.

## Before → after measurements

Run from `/home/vgpnk/Projects/shokunin/mado-shokunin`:

```sh
python3 .ufo/waves/round-13/measure.py 7dcb785b7b943d03703181b218d7860a7b43007b
python3 .ufo/waves/round-13/measure.py 95cbc41fe5d5db121b89c2ddd1f953728663c5f4
```

Both observation probes exited **0**; this is not automatic admission. They read the source registry, knowledge and navigation from the named revision and run the named census cases in isolated fixtures. Full outputs: `evidence/before.txt`, `evidence/after.txt`.

| Claim | Before at `7dcb785…` | After at `95cbc41…` | Verdict |
|---|---|---|---|
| C1 coverage / source-joined current-art ground | U1–U3, **3/7 = 4.2857/10** | U1–U4, **4/7 = 5.7143/10**; three U4 facet rows plus phase/advertisement/core-spec joins present | locally verified improved, +1.4286 on this bounded rubric |
| C2 operability / complete named-set diagnostics in four cases | **0/4 = 0.0000/10** on the responsible census rows; overall runs already failed **3/4** | **4/4 = 10.0000/10** with every relevant missing/extra name; overall runs fail **4/4** | locally verified improved; not a claim that the baseline detected nothing, nor whole-domain saturation |

Actual delivered case rows (all run exits 1):

```text
extra-local     hypr.local.inventory       FAIL extra: extra.conf
replace-local   hypr.local.inventory       FAIL missing: xdph.conf extra: extra.conf
replace-source  hypr.root.sources_resolve  FAIL missing: ~/.config/hypr/ai-usage.conf extra: ~/.config/hypr/replacement.conf
missing-gkeep   hypr.local.inventory       FAIL missing: gkeep.conf
```

The baseline's ordered include check already detected source substitution, and its source resolver already detected a vanished gkeep target. C2 measures complete diagnostics on the owning census row, not overall detection recall; the clarification was recorded **before** L1 measurements.

Harm watch / exercised verification:

| Check | Command | Observed result |
|---|---|---|
| Navigation | revision counter above | **26/26 → 27/27**, missing/extra/duplicate 0 |
| Hermetic gate | `bash tools/mado-verify.sh --selftest` | **310/310**, exit 0; prior 269/269 is the previous round's record, not freshly rerun here |
| File-plane health | `bash tools/mado-verify.sh --no-live` | **29 PASS, 0 FAIL, 0 UNKNOWN, 8 SKIP, 4 NOTE**, CLEAN, exit 0; byte-identical before/after |
| Historical mutation re-cut | actual printed REGRESSION_RECUT command in `evidence/regression-recut.txt` | **10/10 KILLED**, restore OK; original spec SHA `c7ee75b9…` unchanged |
| New covering mutants | exact command in `evidence/covering-mutants.txt`, spec `.ufo/waves/round-13/covering.spec` | **8/8 KILLED**, restore OK; derived target `87910c39…` |
| Frozen input replay | `python3 .ufo/waves/round-13/frozen/verify.py` | both digests verified first; **10/10 table match**, flips 0; `MADO_REGRESSION: PASS`, `frozen_match`, exit 0 |
| Frozen gate self-invocation | same runner with `--selftest` | **12/12**, exit 0; tamper/missing input fixtures reject before execution |
| Source-merge gate | `python3 .ufo/waves/round-13/w1/reports/MistakeFix.py --selftest`; same script `--registry <path>` | **25/25**; actual historical bad registry exits 1 naming S017/S030; current exits 0 |
| Safe global recheck | literal recipe in the U4 entry, recorded in `evidence/globals-recheck-command.txt`, with explicit bound WAYLAND_DISPLAY | **72 advertisements / 71 interfaces**, digest `9569d02fe2b04bf62079258b1d74f5d2ad8510c26ef0710a1a64c95f1a9becaa`, exit 0; no raw persisted output |

The U4 source/claim table was also reviewed for phase versus registry versus behavior semantics; a header-only entry does not satisfy the counter's U4 facet predicate. No current full live desktop-health run or promotion verdict is claimed.

Per-axis disposition: **coverage improved; operability improved; freshness unchanged** (file-plane fraction remains 10); **calibration unchanged as an axis claim** (criterion learning is reported under discernment); **depth and adjacency unscored/unchanged**. Remaining limits include expanded toggle-glob membership, directory-shaped source targets, general parser semantics, a dedicated order-swap fixture, the historical theme-mutation gap, whole-config boundary-hash breadth and rendered/feature behavior. These are named, not silently closed.

## Sources & frontier

Counting commands are the same two revision-bound probes above (`source_registry` field):

```text
rows:      39 → 46
A/B/C:     35/1/3 → 42/1/3
statuses:  mined=27 queued=9 rejected=3 → mined=34 queued=8 rejected=4
```

Rows added: **7 A, 0 B, 0 C** — S040–S046, including rejected correction S045. This yielded **one new admitted author-gate knowledge entry on U4**, not seven units of expansion. Combined curated row-action candidates S005/S017/S040–S046: 9 present, 8 mined, 1 rejected, directly enumerated by the committed counter.

Existing cells touched, logged old→new in `corpus/lessons/round-13.md` § Gate:

- S005 status `queued → mined`; used-by `— → corpus/knowledge/wayland-protocol-boundaries-r13.md`.
- S017 used-by adds `corpus/lessons/round-13.md`; prior two knowledge paths retained.
- No existing recheck, tier, opened, anchor or teaches cell changed. S006 remains queued; new S042 supersedes its missing revision. S030 remains rejected; new S045 supplies the explicit rejection reason/flip.

New rows were opened this round; every URL/access date/≤25-word located quote is in lesson § Gate. The external phase and core contracts stay distinct from host behavior. S046 specifically grounds the observer's bindings/detail queries; the retained capture is not the whole execution. U5–U7, complete per-interface phase classification, rule attribution and output/colour behavior remain frontier ground.

Required census command, **run both at round start and end**:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado
```

Before (retained `.ufo/waves/round-13/census-before.txt`):

```text
mado W04 S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado ok /home/vgpnk/Projects/shokunin/mado-shokunin/corpus/SOURCES.md
exit=0
```

After (`.ufo/waves/round-13/evidence/census-after.txt`):

```text
mado W04 S030 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado W04 S042 duplicate url wayland.freedesktop.org/extras.html across scopes
mado W04 S045 duplicate url wiki.hypr.land/Configuring/Basics/Window-Rules across scopes
mado ok /home/vgpnk/Projects/shokunin/mado-shokunin/corpus/SOURCES.md
exit=0
```

Warnings are retained historical/superseding URL records, not hidden failures. The stricter lane-local screen ignores rejected historical collisions, validates supersedes links and stops active URL reuse for human review; it does not claim semantic overlap automation. Mistake M1 mines the prior non-author disagreement; M2–M5 retain census, citation, scratch-data and helper-test lessons with evidence. The captured raw-data defect was fixed before any push.

## Trend verdicts

- **expansion — improved:** one new source-joined U4 entry on previously uncovered ground; measured U-items 3/7 → 4/7 and navigation remains complete. Source-row volume is not the growth signal (`evidence/after.txt`, U4 entry, README coverage map).
- **quality — improved:** named-set diagnostics replace the weaker presence checks; 310/310 suite, 10/10 historical and 8/8 covering kills, clean file plane and digest-verified frozen replay support the stronger instrument. Existing notes receive dated append-only corrections/current receipts; limits are retained (`gate-standing-use.md` round-13 receipt; `evidence/`).
- **discernment — improved, narrowly:** the **previous round's outside** S030 disagreement becomes criterion 17 and a real red historical case while corrected history remains green. This is not a claim of current-round outside agreement; that spot-check is pending (`round-12-verifier-spotcheck.md`, round-13 lesson M1, collision proof).

**Stale-lane:** respawn-per-round; no other mado mission is open. Durable dispatch digest copied from the observed runtime line: `2026-10-20T01:04:05-03:00 launch mado round=13 pgid=654654 driver=hyaku-inline attempt=1`. This round exceeded two 450-second ticks but was **progressing**, now evidenced by the two pushed lane-authored commits; no runtime/counter mutation. No next round was opened.

**L0 / closure:** no new operator decision was needed. The inherited round-12 caveat about gkeep permanence remains unresolved historical operator intent, not a claim of desired configuration. The parent explicitly owns the fresh non-author admit/reject source-reopen spot-check and MANIFEST closure **after this report lands**. Admission remains pending that closure. SHONEN/promotion is not self-cleared.

## SHONEN

- [~] Real decision tables, error patterns, checklists and cited sources — `SKILL.md`, the new U4 entry and existing `corpus/knowledge/executor-test-sufficiency.md`; current outside-lane promotion clearance not supplied.
- [~] End-to-end domain task executed/logged — inherited `corpus/knowledge/config-health-report-r3.md` and `LOG.md` round 3; this round's scoped diagnostic/gate evidence does not replace a fresh outside-lane promotion review.
- [~] Instructions executable without oral context — `SKILL.md` registry and scoped routes; U4's literal safe recipe exercised with its session prerequisite; inherited executor-test record remains dated evidence.
- [~] No cross-domain bleed / province accuracy — `PROVINCE.md` unchanged, boundary notes and `w1/SiblingOverlap.md`; lane-dispatched seats are not named independent promotion verifiers.
