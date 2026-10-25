# FleetBoundaryConnector — advisory

Not a native judge verdict, lane round report, receipt, or admission. Read-only. No lane file was edited. No gate, build, lint, or formatter was run. Starting revisions match `baselines.json` (`git -C <lane> rev-parse HEAD` this session): kagi `fecee8743e52eb8fb5fbb40782934cb619a1a96e`, kake `b0feb30886585d8df6d4671845a2d18989ca722b`, kama `ea72c3eae4ecc68dab2b0a08153c9c1d2e16df21`, kasegi `d1e6e8f3931a2bfbeb4319b9b41980c1e801e9f1`, kengaku `d84e48d525d6af6b1d137d608aea8c726f8bead4`, kotoba `02302c521b933c55fc4be79193e61537e3380751`. Lane plans read before measurement: each `plans/wwkd-round-*-recensus.md`.

## Axes this note moves

| Axis | Effect of the proposed erratum | Why |
|---|---|---|
| calibration | improved | Live claims separated from historical pins; one round-15 "resolves" line is falsified by sibling clusters plus a fresh `test -d`. |
| adjacency | improved | Duplicate ownership named with the province that already owns the predicate. Nothing is absorbed into a runtime fix. |
| freshness | improved, narrowly | New absence is recorded. Historical pins are not deleted or re-pinned to green. |
| operability | unchanged | No gate, `--src` default, or probe behavior changes. Landed derivations stay. |

No scalar. Contradiction kept: kumitate `coverage:kimi-layer` can stay 10 as a membership census and still be the wrong exclusive-ownership reading. Rescoring it this wave would harm calibration.

## Evidence

### Seventeen PROVINCE boundaries (the actual files)

Counted on disk: 17 `*-shokunin/PROVINCE.md`. No other `PROVINCE.md` under the fleet root.

| # | File | Boundary that matters here |
|---|---|---|
| 1 | `audio-shokunin/PROVINCE.md:3-17` | Audio content only. Writes `.shokunin/audio/**`. Refuses mechanics (game-dev-2d) and canon (lore). |
| 2 | `game-dev-2d-shokunin/PROVINCE.md:3-12` | 2D headless fixtures. Refuses lore canon and harness auditing. |
| 3 | `game-dev-3d-shokunin/PROVINCE.md:3-47` | 3D fixtures. REA is supporting static inspection only; reverse engineering as an end is revenger's. |
| 4 | `kagi-shokunin/PROVINCE.md:3-54` | Secrets and vault ops. Live surfaces are the janitor substrate, now marked historical-absent (`:10-17`). CDP/chrome profile contested with kake (`:43`). |
| 5 | `kaidoku-shokunin/PROVINCE.md:35-41` | REA on this host. Owns `~/.kimi-code/config.toml:1284` as an REA MCP spawn key, and self-launched CDP on `:9222` (`:50`). |
| 6 | `kake-shokunin/PROVINCE.md:3-6` | Web properties and publishing. One-line owns/refuses. Round-18 migration lives in SCORECARD/pins, not in this file. |
| 7 | `kama-shokunin/PROVINCE.md:6-30` | Local model serving and endpoint identity. Concrete artifact `~/.config/systemd/user/qwen-coder.service` (`:10`). Refuses eval (kengaku), credentials (kagi), dispatch (kumitate), remote web (kake). |
| 8 | `kasegi-shokunin/PROVINCE.md:3-25` | Bounty research. Round-19 annotation: mirror and `origin-work` absent; `ufo-fsd-alpha` relocated to `~/Projects/ufo-fsd-alpha`. |
| 9 | `kengaku-shokunin/PROVINCE.md:8-33` | Eval craft. Still lists `~/Projects/webzites/repos/llm-wiki`, `~/archive/bench-arena/`, and `:34113` pid 1299 as the surface table (`:12-14`). Says the serving plane is unowned (`:24-25`). |
| 10 | `kotoba-shokunin/PROVINCE.md:3-6` | Prompt and skill craft. One-line owns/refuses. |
| 11 | `kumitate-shokunin/PROVINCE.md:1-6` | Still the six-line seed: orchestration and tooling. No Kimi surfaces. |
| 12 | `lore-shokunin/PROVINCE.md:3-11` | Fictional canon. Refuses mechanics. |
| 13 | `mado-shokunin/PROVINCE.md:6-18` | Compositor configs, read-only. Secrets → kagi. Endpoints → kama. |
| 14 | `revenger-shokunin/PROVINCE.md:3-25` | Shipped-artifact RE. Refuses live-target execution and game mechanics. |
| 15 | `tabi-shokunin/PROVINCE.md:6-19` | Owns `~/.kimi-code/plugins/managed/kimi-webbridge/` as primary substrate, plus CDP session discipline. Publishing → kake. Secrets → kagi. Forensics → revenger/kaidoku. |
| 16 | `tameshi-shokunin/PROVINCE.md:6-18` | Verification-fixture method. Reads sibling gates; never edits them. |
| 17 | `tsukuroi-shokunin/PROVINCE.md:6-17` | Host/systemd health, read-only. Endpoint health → kama. Driver internals → kaidoku/revenger. |

Clean splits, not defects: mado→kagi/kama, tsukuroi→kama, tabi→kake/kagi, tameshi's method-vs-product rule, game-dev-3d's refusal of RE-as-end, kama `corpus/knowledge/cross-lane-scope.md:8-31` (consumer text vs endpoint identity).

### Kumitate SCORECARD rounds 18-31, the claim that collides

Rounds 18-31 are a Kimi-CLI expansion, not an OMP gate rewrite. The collision is the membership rule, still live:

- `kumitate-shokunin/SCORECARD.md:539-569` — round 18 pre-register: "Expand the province" and "Four families, disjoint, exhaustive over `~/.kimi-code`."
- `:137-141` — registry rows K1-K5 still `yes`, including `plugins/managed/kimi-webbridge` (K2) and shape-only `credentials/`, `oauth/`, `server.token` (K4).
- `:310` — `coverage:kimi-layer` = 10 at round 22, term `49/49` distinct members. That score counts the colliding members.
- `:623-628` — origin move recorded 2026-10-13; `--src` repair queued, not done in the definition round.
- Later rounds (`:386-389`) run `proxy-check.mjs --src ~/Projects/ufo-fsd-alpha`. The gates now derive that root (`scripts/cite-check.mjs:102-119`, `scripts/claims-check.mjs:74-92`, `scripts/proxy-check.mjs:257-263`). Header `:12` still names `~/Projects/origin-work/ufo-fsd-alpha` at `ee907f1cf` as the baseline tree for HEAD `7a4c9a0`. That sentence is a baseline stamp, not the live default. Do not re-repair `--src`.

`PROVINCE.md` was not updated. A reader of the 17 province files cannot see the K-block. The exhaustive claim lives only in the scorecard and the `kimi-*.md` notes.

Measured this session, shape only (no `config.toml` / `credentials/` / `oauth/` / `server.token` content read):

- PRESENT: `~/.kimi-code`, `config.toml` (mode 600), `credentials/` (700), `oauth/`, `plugins/managed/kimi-webbridge` (700), `server.token` (600), `skills/`.
- ABSENT: `/home/vgpnk/projects`, `/home/vgpnk/projects/shokunin`, `/home/vgpnk/Projects/origin-work`, `/home/vgpnk/Projects/webzites`, `/home/vgpnk/archive`, `/home/vgpnk/bench-arena`, `~/.config/the-janitor`, `~/.local/bin/the-janitor`, `~/.config/systemd/user/qwen-coder.service`, `~/.config/opencode/agents/janitor.md`, `~/.local/share/the-musketeer/chrome-profile`.
- `find /home/vgpnk /home/vgpnk/Projects /home/vgpnk/archive -maxdepth 5` for `llm-wiki`, `bench-arena`, `webzites`: no hits.
- `ss -ltn` showed no listener on `:8080`, `:34113`, `:9222`, or `:40961`. `systemctl --user status qwen-coder.service` → unit could not be found.
- `git -C /home/vgpnk/projects/shokunin/kasegi-shokunin rev-parse` → `fatal: cannot change to ... No such file or directory`.
- `git -C /home/vgpnk/Projects/ufo-fsd-alpha log -1` → `964f443e` 2026-10-12, same HEAD kasegi and kumitate already recorded.

`config.toml` line identity (`kaidoku` `:1284` vs kumitate `kimi-modes-machinery.md:69` `:1285-1292`) was not re-opened. The file is credential-shaped. Overlap is the file, not a re-verified line.

### Duplicate ownership

| Surface | Who already owns the predicate | Who else counts it | Defect |
|---|---|---|---|
| `~/.kimi-code/plugins/managed/kimi-webbridge/` | tabi `PROVINCE.md:6-8`. Anatomy note `corpus/knowledge/webbridge-plugin-anatomy.md:1-18` (same 3 files, sha256 first-12 `e70aff5c40ff` / `84a8e69d04c5` / `b811d9c23dfd`, re-pinned 2026-10-14). | kumitate K2 (`SCORECARD.md:138`) and `corpus/knowledge/kimi-skills-plugins.md:208-253` (plugin manifest, skill frontmatter, CDP verb list). Routing section `:324-336` sends `:10086` to kama and secret modes to kagi. It does not name tabi. | Duplicate. Census membership is fine. Internals-level skill/CDP writeup is tabi's surface, scored inside `coverage:kimi-layer`. |
| `~/.kimi-code/config.toml` REA spawn keys | kaidoku `PROVINCE.md:41`. | kumitate K1 whole-file census plus `kimi-modes-machinery.md:69` (`[mcp_servers.rea]` called inert). | Same file, two predicates. Exclusive "disjoint" wording erases kaidoku's line-scoped claim. Line drift unverified (file not content-read). |
| `~/.kimi-code/skills/*` craft | kotoba `PROVINCE.md:3-5` (trigger fidelity, SKILL.md quality). Skills are symlinks into `~/.agents/skills` and `~/Projects/myskills` (`kimi-skills-plugins.md` README row, kumitate `corpus/README.md:71`). | kumitate K2 counts the five skill entries as members and documents trigger/mode machinery (`kimi-modes-machinery.md`). | Mechanism (resolution order, User>Extra>Built-in) can stay kumitate. Craft rules for the skill bodies are kotoba's. The K2 count does not say so. |
| `credentials/` `oauth/` `server.token` shape | Fleet refusals route secrets to kagi (mado `:14`, tabi `:16`, tsukuroi `:14`, kama `PROVINCE.md:17`). Kumitate cites "kagi census discipline" (`SCORECARD.md:588`). | K4 counts the members toward the kimi coverage score. kagi `PROVINCE.md` surfaces are the janitor tree, not `~/.kimi-code`. | Gap, not a second content owner. Method is cited; the surface is not in kagi's province. Kumitate's note correctly did not open the files (`kimi-skills-plugins.md:322`). The defect is the missing partition row, not a secret read. |
| Serving plane `:34113` / `qwen-coder.service` | kama `PROVINCE.md:10-14` owns process, port, and served-model identity. Operator owns unit edits (`:22-26`). | kengaku `PROVINCE.md:24-25` says no lane owns the plane. `SCORECARD.md:213-216` carries restoration as kengaku freshness debt (unblock = operator restores the unit). | Contradiction. kama owns identity. Operator owns the unit. kengaku keeps historical capability interpretation (q4_0 KV, pid 1299 as capture-time fact) and should not own restoration. |
| Chrome profile / `:9222` | kagi `adjacency.tsv:82` contested with kake; kaidoku owns self-launched CDP; tabi owns webbridge CDP discipline. | — | Not a live duplicate. Profile directory is absent. Leave the contested row as historical partition. Do not adjudicate it here. |

### Wrong-root citations — three classes

Class 1, stale `--src`, is landed. Do not repeat.

- kama `tools/kama-probe.sh:529-547` and `registry/endpoint-consumers.tsv:13-14`: `$UFO_SRC` then first existing of `~/Projects/ufo-fsd-alpha`, `~/Projects/origin-work/ufo-fsd-alpha`, else `file=missing`.
- kumitate `SRC_CANDIDATES` in `cite-check.mjs:106-119`, `claims-check.mjs:74-92`, `proxy-check.mjs` (same list). Explicit bad `--src` stays bad (`claims-check.mjs:473`).
- kasegi instruments derive (`citation-bases.md:54-59` describes that). kake round 18 marked `origin-work` cites historical (`SCORECARD.md:21-24`, `corpus/lessons/round-18.md:13-17`).

Class 2, citation-to-deleted, is landed where annotated and still live where a province or scorecard asserts presence.

| Claim, presented as current | Measurement this session | Sibling cluster that already recorded the absence |
|---|---|---|
| kengaku `SCORECARD.md:217-219`: `~/archive/bench-arena` resolves; `~/Projects/webzites/repos/llm-wiki` resolves | Both parents absent. `find` depth 5: no hits. | kama `consumer-registry.md:53-60` (webzites including `repos/llm-wiki` gone; `~/archive/bench-arena/loop.sh` deleted). kake `freshness-pins.json:81` lists `~/Projects/webzites` in `pathsMissSet` (round 18, updated 2026-10-14). |
| kengaku `PROVINCE.md:12-14`: those two paths plus live `:34113` / pid 1299 | Port not listening. Unit not found. | kama errata `:70-72`. kengaku's own `:208-216` marks `:34113` ABSENT, then `:217-219` still says the other two resolve. |
| kama `PROVINCE.md:10`: unit file as a concrete owned artifact | Unit file absent. | Same lane's errata `:56-64` and `:70-72`. Province text was not annotated. Scorecard moved; province boundary did not. |
| kama `consumer-registry.md:111` row 21 path `~/archive/bench-arena/loop.sh` | Absent. Errata `:60` marks row 21 historical. Table path left as the historical quote. | Not a remaining defect if read under the errata rule ("rows below keep their round-1 text"). |

Class 3, lowercase fleet root, is the remaining wrong-root. `/home/vgpnk/projects` does not exist. The fleet is `/home/vgpnk/Projects/shokunin`. kake fixed its own descendant cite (`LOG.md:318-322`, SCORECARD round 17). The other lanes' landed repairs did not cover this class.

| Still presented as openable | What happens | Uppercase counterpart |
|---|---|---|
| kama `consumer-registry.md:111-119` rows 22-30, `:191`, `:332`, `:334`, `:337` use `~/projects/shokunin/...` | Path does not exist. Errata `:30-80` re-anchored `origin-work` and marked webzites/archive gone. It does not mention this class. | Lane files exist, e.g. `~/Projects/shokunin/kengaku-shokunin/PROVINCE.md`, `kagi-shokunin/corpus/knowledge/janitor-env-contract.md`, `kumitate-shokunin/corpus/knowledge/ops-watchers.md`. |
| kasegi `citation-bases.md:72-73` runnable `git -C /home/vgpnk/projects/shokunin/kasegi-shokunin show fc6d398:SKILL.md` | Command fails as measured. | `git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin` is the lane whose HEAD was just parsed. |
| kotoba `SKILL.md:88`, `:97`, `:106` — dispatch-prompt class "no harness loads `/home/vgpnk/projects/shokunin/.ufo/prompts/`" and `md5sum` over `/home/vgpnk/projects/shokunin/*/AGENTS.md`, "re-verified round 7" | The directory is gone. Round-19 errata in `SKILL.md:34-37` covers the origin-work ufo skill path, not this fleet root. | Prompts and `AGENTS.md` live under `/home/vgpnk/Projects/shokunin/`. |
| kagi `adjacency.tsv:19`, `corpus/knowledge/adjacency-scope.md:92`, `claim-ledger.tsv:22` still say `lane:` resolves under `~/projects/shokunin/<lane>-shokunin` | Prose is false. The gate does not use that literal: `corpus/scope-gate.sh:91` sets `LANE_ROOT` from `SCRIPT_DIR/../..`, and `:338-342` joins `${lname}-shokunin` onto it. `LOG.md:710-711` records the repair at `8a6ec16`. | Do not re-edit the gate. The remaining defect is the contract sentence. |

Lessons and verifier fixtures that quote the old path as a historical string or a pointer-shape example (`kotoba-shokunin/verifiers/verify_corpus_integrity.py:624-625`, kengaku `LOG.md:5`, kagi `corpus/lessons/round-1-aggregator-seed.md`) are append-only record. Not this class. Do not rewrite them.

### Cross-domain defects (absorbed, not only overlapped)

1. kengaku round 15 classified the relocation as "drift never reached us" (`SCORECARD.md:184-200`, `LOG.md` round-15 entry: failure classes 0/0/0/0) because `grader.py` has no `--src`. That survey grepped `origin-work` and missed sibling claim clusters that already had the wiki, bench-arena, and serving-plane absences. The serving-plane absence was then absorbed as kengaku freshness debt (`:213-216`) instead of routed to kama (identity) and the operator (unit). That contradicts kengaku's own refusal at `PROVINCE.md:24-25` and kama's province.

2. Kumitate rounds 18-31 absorbed `~/.kimi-code` as an exclusive family. `kimi-skills-plugins.md:324-336` does route two predicates (daemon port → kama, secret modes → kagi) and then still counts the members. It never routes the plugin tree to tabi, which already holds an internals-level anatomy of the same three files. `kimi-modes-machinery.md:449-469` routes endpoints to kama and secret shape to kagi, and does not name kaidoku or kotoba. The scorecard's "disjoint, exhaustive" sentence (`:568`) is the absorption. The six-line `PROVINCE.md` hides it from every lane that trusts province files.

3. kama `PROVINCE.md:10` still offers the deleted unit as a current owned artifact while the same lane's errata says the unit is gone. That is intra-lane, and it is also the boundary other lanes are supposed to read. kengaku's "unowned" sentence is what you get if you never re-read kama's province against kama's errata.

Not absorbed, correctly refused: kumitate did not open secret members; kama `cross-lane-scope.md` keeps credential and instruction text out of kama; kake did not resurrect `origin-work` cites; tameshi does not edit sibling gates. Orchestration/runtime defects inside `ufo-core-runtime` and the parked S/R re-census (`SCORECARD.md:636-642`) stay kumitate's. This note does not take them.

## Proposed move

One append-only fleet adjacency erratum, parent-owned, no gate edit, no score change, no lesson rewrite.

Title it `FLEET-ADJACENCY` and put three clauses in it.

**Clause A — K-block is a census, not exclusive ownership.** Qualifier on kumitate `SCORECARD.md:568`, not a term change:

- `plugins/managed/kimi-webbridge/` behavior, skill text, and CDP verbs → tabi. Kumitate may keep the member in the K2 count only as "plugin package present."
- `config.toml` `[mcp_servers.rea]` spawn keys → kaidoku. Kumitate keeps the provider/model registry predicate.
- Skill-body craft under the five `skills/` symlinks → kotoba. Kumitate keeps resolution order.
- Secret-member shape → kagi discipline. kagi does not yet list the paths; the erratum names that gap for kagi, it does not invent a kagi surface edit in this wave.
- `:10086` stays kama's, as `kimi-skills-plugins.md:332-333` already says.

Do not retune `coverage:kimi-layer`. A score edit in the measuring round is the thing rounds 18-22 refused.

**Clause B — citation class `FLEET-CASE`.** A cite of `~/projects/shokunin` or `/home/vgpnk/projects/shokunin` is non-openable. The tree is `~/Projects/shokunin`. Apply an inline erratum, not a table rewrite, only where the path is still offered as a command or resolver:

- kama `consumer-registry.md` rows 22-30 and lines 191, 332, 334, 337. Owner: kama. Errata section already exists; add the class there.
- kasegi `citation-bases.md:72-73`. Owner: kasegi. Point the shell command at the uppercase lane root. Leave blob id `fc6d398` alone.
- kotoba `SKILL.md:88`, `:97`, `:106`. Owner: kotoba. Erratum beside the round-7 re-verification sentence. Do not rewrite the round-7 claim in place.
- kagi `adjacency.tsv:19`, `adjacency-scope.md:92`, `claim-ledger.tsv:22`. Owner: kagi. State that `scope-gate.sh:91` derives `LANE_ROOT`. Do not patch the gate.

Out of scope for Clause B: lessons, verifier string fixtures, kake's already-fixed cite, every landed `--src` derivation.

**Clause C — kengaku round-15 presence lines are not current.** Owner: kengaku, routed not absorbed.

- Append that `SCORECARD.md:217-219` is falsified for `~/archive/bench-arena` and `~/Projects/webzites/repos/llm-wiki` (kama `:53-60`, kake `freshness-pins.json:81`, this session's `test -d` / `find`).
- Replace the live reading of `PROVINCE.md:24-25` ("no lane owns the serving plane") with: kama owns endpoint identity; the operator owns unit restoration; kengaku keeps capture-time capability notes (pid 1299, q4_0 KV) as historical.
- Annotate kama `PROVINCE.md:10` the same way the errata already annotates the unit. Owner: kama. One absence line, not a re-scope.

Parent integrates. This seat does not commit, does not edit lane files, and does not run the gates.

## Risks

- Reading Clause A as permission to drop `coverage:kimi-layer` from 10 harms calibration. The term was pre-registered as member counts, and the members are still on disk. The harm is the exclusive-ownership sentence, not the numerator.
- Rewriting kama rows 22-30 in place harms the append-only census the errata header already protects (`consumer-registry.md:30`).
- Rewriting kotoba `SKILL.md:106` in place falsifies the round-7 re-verification record. Erratum only.
- Re-opening kumitate `--src` or kake round-18 markers repeats a landed repair and can pin a superseded root as current.
- Treating kaidoku `:1284` as confirmed line-drift would be a fabricated measurement. The file was not content-read.
- kengaku's round-15 "resolves" lines may have been true earlier on 2026-10-14 and false later. The defect is that they are still the current sentence while kama's same-day errata and kake's miss set say otherwise. Do not call the round-15 author false; call the sentence stale.

## Verification (parent, after integration — not run here)

1. `test -d /home/vgpnk/projects/shokunin; echo $?` → non-zero. `test -d /home/vgpnk/Projects/shokunin` → zero.
2. `test -d ~/Projects/webzites/repos/llm-wiki; test -d ~/archive/bench-arena; test -e ~/.config/systemd/user/qwen-coder.service` → all non-zero, unless the operator restored them. If restored, Clause C's absence half is withdrawn and the ownership half (kama, not unowned) still stands.
3. `git -C /home/vgpnk/projects/shokunin/kasegi-shokunin rev-parse` fails; `git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin rev-parse` prints `d1e6e8f3931a2bfbeb4319b9b41980c1e801e9f1` at this baseline.
4. `rg -n "disjoint, exhaustive over" kumitate-shokunin/SCORECARD.md` still finds `:568` until the qualifier lands. After the erratum, that sentence must remain, with the qualifier beside it, not deleted.
5. `sed -n '91p;338,342p' kagi-shokunin/corpus/scope-gate.sh` still shows derived `LANE_ROOT`. A Clause B prose fix that also edits this script has exceeded the move.
6. Do not treat a green `grader.py` as evidence that kengaku's host surfaces resolve. The round-15 classification error was exactly that substitution.

## Unresolved debt

| Debt | Owner | Unblock |
|---|---|---|
| K-block exclusive wording vs tabi / kaidoku / kotoba / kagi | integrator applies Clause A; kumitate does not retune the proxy | Append the qualifier. Leave `coverage:kimi-layer` at 10 until a pre-registered term change. |
| kagi has no `~/.kimi-code` secret-shape rows | kagi, after integrator confirms the gap | Declare shape-only rows or explicitly leave shape census with kumitate under kagi's discipline. No content read. |
| `FLEET-CASE` cites still offered as commands | kama, kasegi, kotoba, kagi (prose only) | Inline errata listed in Clause B. |
| kengaku province/scorecard still assert deleted roots and an unowned serving plane | kengaku, with the identity predicate handed to kama | Clause C. Operator restores or retires `qwen-coder.service`; that restoration is not a kengaku or kama edit. |
| kama province still names the deleted unit as a current artifact | kama | One absence annotation on `PROVINCE.md:10`. |
| kaidoku `config.toml:1284` vs kumitate `:1285-1292` | kaidoku, shape-safe re-anchor only | Re-verify the spawn-key line without copying credential-shaped values. Not done here. |
| Chrome profile contest | integrator, only if the profile returns | Surface is absent. No ruling. |
| Parked S/R re-census and origin-tree `PROXY: DRIFT` | kumitate | `SCORECARD.md:636-642`. Not this seat. Do not absorb. |

Cross-domain owner of the erratum itself: the integrator (parent). This report is the evidence packet, not the erratum.
