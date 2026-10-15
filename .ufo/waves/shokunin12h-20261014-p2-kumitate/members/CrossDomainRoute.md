# CrossDomainRoute — Advisory Report

**Seat:** `CrossDomainRoute` (Connector)  
**Role:** UFO-FSD Connector — Route cross-domain defects found by wave `shokunin12h-20261014-p2-kumitate` to their canonical owners; refuse absorption; synthesize bounded cross-domain resolution.  
**Advisory Status:** Data only. Not a native judge verdict, lane round report, receipt, or admission. Read-only audit; no lane file edited, no commit made, no external fetch, no push, and no subagents dispatched.  
**Lane Repo:** `/home/vgpnk/Projects/shokunin/kumitate-shokunin` (HEAD `175de6ba2e9e904010411b19cab27e0af9aad3d4` at dispatch).  
**Origin Tree:** `/home/vgpnk/Projects/ufo-fsd-alpha` (READ-ONLY, HEAD `964f443ee53df0ce06bd689af01f0dea031b01f9` / `964f443e`).  
**Milestone:** Kumitate round 32: script+runtime layer re-census.  

---

## 1. Axes (Named, Not Judged)

| Axis | Movement | Rationale |
|---|---|---|
| **calibration** | **Improved** | Cross-domain defects are explicitly routed to external owners with concrete repository evidence rather than absorbed into Kumitate test fixtures, shims, or scorecard prose. Upstream runtime bugs are separated from lane census debt. |
| **coverage** | **Maintained / Protected** | Pre-registration halt conditions respected: no phantom members invented; K-block terms remain an enumerable filesystem census without asserting exclusive domain ownership over sibling provinces (`kagi`, `kaidoku`, `tabi`, `kotoba`). |
| **operability** | **Maintained** | All executable checks (`proxy-check.mjs`, `claims-check.mjs`, `kimi-census.mjs`) remain executable and fail-closed where required. No runtime code or substrate files are modified. |

---

## 2. Files Inspected

- `skill://godspeed` — Godspeed posture (name axes, iterate cheap, keep moves improving any axis and harming none).
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/SCORECARD.md` — lines 5–12, 114–153, 276–300, 539–588, and round-32 pre-registration in `## Planned` (lines 1364–1409).
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/scripts/proxy-check.mjs` — `LAYER_PATTERNS` (317–320), secret-shape checks (223–225, 365–370, 640–643), stanza parser and drift evaluation.
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/scripts/claims-check.mjs` — `probeSections()`, anchor/symbol resolution rules, member-section extraction.
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/scripts/kimi-census.mjs` — K-block member rules, secret-shape pins (`isLeaf`, `modeFloor` 0o600/0o700, zero content-read).
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/README.md` — 19-family registry and coverage map.
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/knowledge/executable-scorecard.md` — contract specifications for `kumitate-proxy-v1`.
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/knowledge/native-trial-launch.md` — launch pipeline and documentation of the `membrane-seal write` defect (lines 194–237).
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/knowledge/native-judge-pipeline.md` — R1 member definitions and verification anchors.
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/knowledge/native-admission-detail.md` — Cf vs Mn/Zs format-character interop analysis (lines 59–69).
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/knowledge/kimi-binary-secrets.md` — shape-only census declaration and routing handoff (lines 20–26, 319–331).
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/knowledge/kimi-config-plane.md` — `config.toml` section mapping and model API key boundaries.
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/knowledge/local-ship.md` — local transaction engine, bounds, and journal recovery defects.
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/knowledge/distill-and-l3.md` — distiller dedupe schema staleness.
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/lessons/round-5-aggregator-mirror-out-of-province-membrane-seal.md` — precedent for filing cross-province defects without absorbing them.
- `/home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/lessons/round-6.md` — `is_format_char` parity gap documentation (lines 40–45).
- `/home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-cli/src/main.rs` — CLI `Command` enum and `Charter` subcommand.
- `/home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/loop_driver_publish.rs` — `refuse_if_membrane_sealed` and `write_membrane_seal`.
- `/home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/native_admission_text.rs` — `contains_sensitive_shape` and format character handling.
- `/home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/local_ship.rs` — journal recovery lock acquisition sequence.
- `/home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/live.rs` — distiller dedupe schema version references.
- `/home/vgpnk/Projects/ufo-fsd-alpha/scripts/run-omp-native-trial.mjs` — `writeMembraneSeal` implementation (lines 1831–1863).
- `/home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-credential-screen.mjs` — `containsSensitiveShape` and `FORMAT_CHARS_RE` (lines 51–64).
- `~/.kimi-code/` — shape inspection of `server.token`, `credentials/`, `oauth/` (lstat and permissions only).

---

## 3. Exact Commands & Observed Output

All commands executed from `/home/vgpnk/Projects/shokunin`:

### 3.1 `membrane-seal write` defect in kumitate documentation
```bash
grep -n "membrane-seal" /home/vgpnk/Projects/shokunin/kumitate-shokunin/corpus/knowledge/native-trial-launch.md | head -10
```
**Output:**
```
203:- Shells `spawnSync <staged ufoRuntime> ["membrane-seal", "write", --root,
220:tests pin the `"membrane-seal", "write"` argv against a fake runtime
226:(`~/.cargo/bin/ufo`, 0.1.0) predates `membrane-seal` entirely — the staged
```

### 3.2 Upstream CLI command enum in `ufo-fsd-alpha`
```bash
grep -n "MembraneSeal" /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-cli/src/main.rs
```
**Output:**
```
1029:    // Typed admission: the seal must decode as the runtime's `MembraneSeal`
1036:    let seal: ufo_core_runtime::loop_driver::MembraneSeal =
```
*(Exit code: 0. `Command::MembraneSeal` is completely absent from the `Command` enum in `ufo-cli/src/main.rs:21-90`; only `Charter` remains.)*

### 3.3 Upstream launcher `writeMembraneSeal` in `run-omp-native-trial.mjs`
```bash
grep -n -A 10 "function writeMembraneSeal" /home/vgpnk/Projects/ufo-fsd-alpha/scripts/run-omp-native-trial.mjs
```
**Output:**
```
1831:function writeMembraneSeal({ runId, round, sessionId, acceptDigests }) {
1832-  // Ancestry walk: a symlinked .ufo would redirect the tmp+rename outside
1833-  // the contract root — the seal is the membrane's own record, fail closed.
1834-  const sealBad = realDirChainOrNull(path.dirname(path.dirname(MEMBRANE_SEAL_PATH)), path.dirname(MEMBRANE_SEAL_PATH));
1835-  if (sealBad) {
1836-    throw new Error(realDirChainMessage("membrane seal", sealBad));
1837-  }
1838-  const temporary = `${MEMBRANE_SEAL_PATH}.tmp-${process.pid}`;
1839-  const payload = `${JSON.stringify({
1840-    kind: "ufo-membrane-seal-v1",
1841-    run_id: runId,
```

### 3.4 Runtime `refuse_if_membrane_sealed` in `ufo-core-runtime`
```bash
grep -n -A 15 "pub(super) fn refuse_if_membrane_sealed" /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-core-runtime/src/loop_driver_publish.rs
```
**Output:**
```
113:    pub(super) fn refuse_if_membrane_sealed(&self) -> Result<()> {
114-        let path = membrane_seal_path(&self.root);
115-        if !path.is_file() {
116-            return Ok(());
117-        }
118-        // The cause rides the refusal detail (r11 D8 shape): an unreadable
119-        // seal is still a seal, and the operator sees WHY it could not be
120-        // read — oversized, non-UTF-8, or malformed JSON is evidence, not
121-        // silence. The refusal itself stays unconditional.
122-        let seal = read_bounded_string(&path, MAX_LOOP_STATE_BYTES, "membrane seal")
123-            .map_err(|error| format!("seal unreadable ({error})"))
124-            .and_then(|raw| {
125-                serde_json::from_str::<MembraneSeal>(&raw)
126-                    .map_err(|error| format!("seal unreadable ({error})"))
127-            });
128-        let detail = seal.as_ref().map_or_else(
```

### 3.5 Format-character regex in `scripts/ufo-credential-screen.mjs`
```bash
grep -n -C 5 "FORMAT_CHARS_RE" /home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-credential-screen.mjs
```
**Output:**
```
56-// character) re-join it into the exact shape the screen exists to block. The
57-// wider tier therefore also screens the Cf-stripped text (PrimeAgent
58-// refinement r20 F11). containsCredentialShape above stays byte-exact to the
59-// judge — stripping there would break parity — so the widening lives only on
60:// this evidence-writing side, and Cf-free text pays no second scan.
61:const FORMAT_CHARS_RE = /\p{Cf}/gu;
62-export function containsSensitiveShape(value) {
63-  const text = String(value ?? "");
64-  if (containsCredentialShape(text) || SENSITIVE_LITERAL_RE.test(text)) return true;
65-  if (FORMAT_CHARS_RE.test(text)) {
66-    const stripped = text.replace(FORMAT_CHARS_RE, "");
67-    return containsCredentialShape(stripped) || SENSITIVE_LITERAL_RE.test(stripped);
```

### 3.6 Shape-only measurement of secret-bearing paths
```bash
stat -c '%n mode=%a kind=%F' ~/.kimi-code/server.token ~/.kimi-code/credentials ~/.kimi-code/oauth
```
**Output:**
```
/home/vgpnk/.kimi-code/server.token mode=600 kind=regular file
/home/vgpnk/.kimi-code/credentials mode=700 kind=directory
/home/vgpnk/.kimi-code/oauth mode=755 kind=directory
```
*(All pass declared kind and modeFloor pins: `server.token` regular file with mode 0600; `credentials` directory with mode 0700; `oauth` directory with mode 0755 >= 0700 floor. Zero bytes read.)*

---

## 4. Derived Member Lists & Sections Added/Removed

- **Layer Denominators derived:**
  - `S_members`: **91** (73 top-level `scripts/*.mjs` + 18 recursive `scripts/*/` files).
  - `R_members`: **92** (88 `crates/ufo-core-runtime/src/*.rs` + 4 `crates/ufo-cli/src/*.rs`).
  - `K_members`: **49** (unaffected by S/R re-census).
- **Sections added/removed by this seat:** **0**. (Leaf connector role; parent integrator lands note updates).

---

## 5. Unresolved Blockers

1. **Upstream Runtime Secrecy & Seal Deadlock:**
   The upstream Rust runtime does not expose a public `write_membrane_seal` API to JavaScript launchers, forcing JS scripts (`run-omp-native-trial.mjs`) to duplicate serialization and file creation logic with different permissions (`0o600` vs umask).
2. **Upstream Fail-Open Seal Symlink Vulnerability:**
   `refuse_if_membrane_sealed` in `loop_driver_publish.rs:115` relies on `path.is_file()`, failing open if `.ufo/membrane-seal.json` is a dangling symlink or directory.
3. **Shadow Province Collision (`~/.kimi-code`):**
   `kumitate-shokunin/SCORECARD.md:568` declares "disjoint, exhaustive over `~/.kimi-code`" without recognizing sibling lane authorities (`kagi`, `tabi`, `kaidoku`, `kotoba`).

---

## 6. Cross-Domain Routing Table (One Routing Line per Defect)

Every defect identified across the wave is explicitly routed to its owner with supporting evidence:

| # | Defect Category | Defect Summary | Canonical Owner | File & Line Evidence |
|---|---|---|---|---|
| 1 | **`membrane-seal write` argv defect** | Historical `ufo membrane-seal write` argv failed clap parsing in `ufo-cli`. Upstream resolved this by dropping `Command::MembraneSeal` entirely from CLI and implementing direct JS `writeMembraneSeal()` in `run-omp-native-trial.mjs`. The defect remains as an upstream cross-language duplication with diverging write modes (`0o600` in JS vs umask in Rust). | **`ufo-fsd-alpha`** (Upstream Runtime/CLI) | `kumitate-shokunin/corpus/knowledge/native-trial-launch.md:208-226`<br>`ufo-fsd-alpha/scripts/run-omp-native-trial.mjs:1831-1863`<br>`ufo-fsd-alpha/crates/ufo-cli/src/main.rs:21-99`<br>`ufo-fsd-alpha/reports/nc6/runtime/r01-review.md:13-15` |
| 2 | **ufo-runtime defect** | **Membrane seal fail-open bypass on symlinks/kind:** `refuse_if_membrane_sealed` uses `path.is_file()` (returns `Ok(())` on dangling symlink or directory, bypassing authority boundary) and never verifies that `seal.kind == MEMBRANE_SEAL_KIND`. | **`ufo-fsd-alpha`** (`crates/ufo-core-runtime`) | `ufo-fsd-alpha/crates/ufo-core-runtime/src/loop_driver_publish.rs:113-127`<br>`ufo-fsd-alpha/reports/nc6/final/FULL-REVIEW.md:177`<br>`ufo-fsd-alpha/reports/nc6/final/ONESHOT.md:133-140` |
| 3 | **ufo-runtime defect** | **Unicode format-char credential screening parity gap:** Native judge `contains_sensitive_shape` (`native_admission_text.rs`) performs raw ASCII matching without stripping format characters, while JS screen (`ufo-credential-screen.mjs`) strips `\p{Cf}` (and historically `\p{Cf} ∪ \p{Mn} ∪ 6 Zs`), risking interop rejection of valid handoffs. | **`ufo-fsd-alpha`** (Runtime & Script Maintainers) | `kumitate-shokunin/corpus/knowledge/native-admission-detail.md:59-69`<br>`kumitate-shokunin/corpus/lessons/round-6.md:41-45`<br>`ufo-fsd-alpha/crates/ufo-core-runtime/src/native_admission_text.rs:8-100`<br>`ufo-fsd-alpha/scripts/ufo-credential-screen.mjs:52-67` |
| 4 | **ufo-runtime defect** | **Local-ship journal recovery race condition:** `local_ship.rs` samples `live_sha256` before acquiring the per-target apply lock, then consumes the pre-lock sample without re-reading inside the lock; a concurrent apply committed in that window is reverted to preimage. | **`ufo-fsd-alpha`** (`crates/ufo-core-runtime`) | `kumitate-shokunin/corpus/knowledge/local-ship.md:70-85`<br>`ufo-fsd-alpha/crates/ufo-core-runtime/src/local_ship.rs:1204-1262`<br>`ufo-fsd-alpha/reports/nc6/final/FULL-REVIEW.md:178` |
| 5 | **ufo-runtime defect** | **Live Qwen distiller dedupe schema staleness:** `crates/ufo-core-runtime/src/live.rs` references `ufo_dedupe_v2` wire schema while `crates/ufo-core-runtime/src/distill.rs` implements `ufo.dedupe.v4`. | **`ufo-fsd-alpha`** (`crates/ufo-core-runtime`) | `kumitate-shokunin/corpus/README.md:33`<br>`kumitate-shokunin/corpus/knowledge/distill-and-l3.md:35-50`<br>`ufo-fsd-alpha/crates/ufo-core-runtime/src/live.rs` |
| 6 | **ufo-runtime defect** | **Upstream tree restructuring & member deletions:** 23 script-layer members and 6 runtime-layer members deleted upstream since `5725fa7d3` cause frozen stanza drift (`S_members` 114→91, `R_members` 98→92). | **`ufo-fsd-alpha`** (Upstream Tree Authority); **Parent Integrator** (Stanza Alignment) | `kumitate-shokunin/SCORECARD.md:1371-1380`<br>`git diff --diff-filter=D --name-only 5725fa7d3 HEAD` in `ufo-fsd-alpha`<br>`kumitate-shokunin/scripts/proxy-check.mjs` |
| 7 | **secrets-adjacent path** | **`~/.kimi-code/` credentials, tokens, and OAuth stores:** `server.token` (0600), `credentials/` (0700), `oauth/` (0755/0700) contain live session tokens. Kumitate performs shape-only stat and zero content reads. Fleet vault ops and secret hygiene belong to `kagi-shokunin`. | **`kagi-shokunin`** (Fleet Secret Hygiene Authority); **Operator / Kimi CLI** (Token Lifecycle) | `kumitate-shokunin/corpus/knowledge/kimi-binary-secrets.md:21-26, 328-330`<br>`kumitate-shokunin/scripts/kimi-census.mjs:124-128, 303-314`<br>`kagi-shokunin/PROVINCE.md:3-54` |
| 8 | **secrets-adjacent path** | **`~/.kimi-code/config.toml` API keys & REA spawn keys:** File contains live model `api_key` entries and line 1284 REA spawn configuration. Kumitate censes file as K1 member; line 1284 belongs to `kaidoku-shokunin`. | **`kaidoku-shokunin`** (`PROVINCE.md:35-41`, REA Spawn Key); **`kagi-shokunin`** (Secret Hygiene); **Operator** (Key Values) | `kumitate-shokunin/corpus/knowledge/kimi-config-plane.md`<br>`kaidoku-shokunin/PROVINCE.md:35-41`<br>`kumitate-shokunin/SCORECARD.md:570` |
| 9 | **secrets-adjacent path** | **Pre-dispatch credential screen (`scripts/ufo-credential-screen.mjs`):** Script strips credential patterns and format characters prior to dispatch handoff. | **`ufo-fsd-alpha`** (Upstream Script Authority); **`kagi-shokunin`** (Fleet Secrets Boundary) | `ufo-fsd-alpha/scripts/ufo-credential-screen.mjs:1-75`<br>`kumitate-shokunin/corpus/knowledge/native-trial-launch.md` |
| 10 | **secrets-adjacent path / duplicate claim** | **`SCORECARD.md:568` shadow province expansion:** "Four families, disjoint, exhaustive over `~/.kimi-code`" collides with `tabi` (webbridge plugin internals), `kaidoku` (REA keys), `kotoba` (skill craft), and `kagi` (secret hygiene). | **Kumitate Parent Integrator** (Append Errata Qualifier) | `kumitate-shokunin/SCORECARD.md:568`<br>`tabi-shokunin/PROVINCE.md:6-8`<br>`kaidoku-shokunin/PROVINCE.md:41`<br>`kotoba-shokunin/PROVINCE.md:3-5`<br>`kagi-shokunin/PROVINCE.md:14` |

---

## 7. Proposed Move (Connector Synthesis)

### One Bounded Move: "Upstream Defect Fencing and K-Block Census Qualification"

To reconcile cross-domain defect boundaries without absorbing external bugs, modifying read-only upstream trees, or altering the physical member arithmetic of the scorecard:

1. **Fence Upstream Runtime Defects in Knowledge Prose (Refuse Absorption):**
   - In `corpus/knowledge/native-trial-launch.md`, amend the defect section to note the upstream status: the `ufo membrane-seal write` argv mismatch was retired in `ufo-fsd-alpha` HEAD `964f443e` via direct JS `writeMembraneSeal()`, but leaves an upstream cross-language duplication defect and a fail-open symlink check (`loop_driver_publish.rs:115`).
   - Do not edit `ufo-fsd-alpha` scripts or runtime code. Kumitate strictly maintains read-only posture.
2. **Qualify the K-Block Declaration in `SCORECARD.md`:**
   - Append an explicit qualifying note beside `SCORECARD.md:568` stating:
     > *"Note: The K-block is an enumerable filesystem member census for `coverage:kimi-layer` (49/49 physical members present), not an exclusive domain ownership claim. Primary domain authorities remain partitioned: `plugins/managed/kimi-webbridge/` internals → tabi; `config.toml` REA spawn keys → kaidoku; skill-body craft → kotoba; `server.token`, `credentials/`, `oauth/` secret hygiene → kagi."*
   - Retain `coverage:kimi-layer = 10` unchanged (the score represents member count completeness on disk, which remains 49/49).
3. **Preserve Strict Zero-Read Discipline for Secret Paths:**
   - Maintain `scripts/kimi-census.mjs` and `scripts/proxy-check.mjs` shape-only stat checks (`modeFloor` 0o600 for files, 0o700 for directories). Refuse any readdir or content-reading of secret paths.

---

## 8. Second-Order Effects

- **Runtime Surface:** Fencing the `membrane-seal write` defect ensures Kumitate does not inject fake runtime shims or modify the origin tree, preventing build drift across the fleet.
- **Contract Surface:** Qualifying the K-block declaration resolves the jurisdictional friction between Kumitate and sibling lanes (`tabi`, `kaidoku`, `kotoba`, `kagi`) without altering the 17-province registry or breaking `kumitate-proxy-v1`.
- **Substrate Surface:** Zero-read enforcement on `~/.kimi-code/` prevents credential leakage or race conditions against concurrent Kimi CLI processes.
- **Verification Surface:** `proxy-check.mjs` and `kimi-census.mjs` continue to verify hermetically without warning escalations or unpinned failures.

---

## 9. Risks

- **Risk 1 (Score Bleed):** If parent interprets the K-block qualification as a reason to drop `coverage:kimi-layer` from 10, calibration is harmed. The score measures physical filesystem membership completeness (49/49), which remains physically true.
- **Risk 2 (Upstream Tampering):** If Kumitate attempts to patch the upstream `run-omp-native-trial.mjs` or `loop_driver_publish.rs`, it would violate the contract rule ("Origin tree, READ-ONLY").
- **Risk 3 (Credential Leakage):** Opening secret paths for deeper verification would violate the fleet-wide secrecy contract. Shape-only inspection must remain inviolable.

---

## 10. Verification (Parent Integration Checks)

1. `node scripts/kimi-census.mjs` → Exits 0 (`KIMI_CENSUS: CLEAN`), confirming 49 members checked, 0 shape drift, 0 unpinned leaves, and 0 secret contents read.
2. `node scripts/proxy-check.mjs --json` → Confirms `C1k: 5`, `K_members: 49`, `K_sections: 49`, `coverage_kimi: 10` are unaffected by the script/runtime re-census.
3. `stat -c '%a %n' ~/.kimi-code/server.token ~/.kimi-code/credentials ~/.kimi-code/oauth` → Verifies modes 600, 700, 755 without content inspection.
4. `grep -n "writeMembraneSeal" /home/vgpnk/Projects/ufo-fsd-alpha/scripts/run-omp-native-trial.mjs` → Verifies presence of direct JS writer in origin tree.
5. `grep -n "Command::MembraneSeal" /home/vgpnk/Projects/ufo-fsd-alpha/crates/ufo-cli/src/main.rs` → Verifies exit code 1 (clean removal from CLI).

---

End of advisory report. Not a verdict.
