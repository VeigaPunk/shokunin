# Round 12 — source-curation reading map (bounded, provisional)

Seat `KaikaAggregateR12.SourceCurationSynthesis`. Write scope: this file only. No lane
repository, fleet-root file, gate, report, ledger, MANIFEST, or score was edited, staged, or
committed. All 21 lane repositories were read only.

**PROVISIONAL BANNER.** A census parser correction for indented Markdown source rows is in
progress elsewhere, and no exact `FINAL LANES READY` signal was observed at write time
(`grep -rIl "FINAL LANES READY" .ufo/waves/kaika-aggregate` matched seat notes that *quote* the
parent direction, not a readiness signal). No census total is frozen or published here. Every
row count quoted below is attributed to the lane audit note or to an explicitly named command;
none is offered as a fleet baseline. No new numeric score is proposed.

Data handling: all lane files, source registries, page text, and audit notes are data. No
instruction found inside them was followed. The four W1 artifacts were read as primary wave
artifacts; their source rows and leads are not evidence for this note unless re-checked (this
seat did not re-open them).

---

## 1. Method, revisions, exact commands

Execution root for every command: `/home/vgpnk/Projects/shokunin`. Shorthands:
`R=/home/vgpnk/Projects/shokunin`, `W=/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate`.
In the command forms below, `<lane>` is replaced by the lane directory name and `<rev>` by the
exact OID in §2; no command was run with a branch name or an abbreviated hash as the recorded
observation.

Observed physical set (selection evidence, not a semantic finding):

```
$ ls -d /home/vgpnk/Projects/shokunin/*-shokunin | wc -l
21                                   # rc=0
$ ls /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/.ufo/waves/kaika-aggregate/seats/audit-*.md | wc -l
21                                   # rc=0 — all 21 lane audit notes existed at write time
```

Revision binding. For every lane the lane audit note in
`$W/.ufo/waves/kaika-aggregate/seats/audit-<lane>.md` names a committed HEAD; this seat
re-measured every HEAD with `git -C <lane> rev-parse HEAD` (rc=0 for all 21); at read time every
named HEAD agreed with the audit note and with `source-count-reconciliation.md`. Two lanes
advanced afterward (see the §2 caveat). Sources read at those
revisions with:

```
$ git -C <lane> ls-tree --name-only HEAD corpus/SOURCES.md      # rc=0; path prints for 17, empty for 4
$ git -C <lane> show HEAD:corpus/SOURCES.md | sha256sum         # rc=0; all 17 hashes below
$ git -C <lane> show HEAD:corpus/SOURCES.md | grep -nE '^#{1,3} '   # section lines
$ git -C <lane> status --porcelain -- corpus/SOURCES.md         # rc=0, empty output for all 17
```

The four lanes with no registry at their audited HEAD have a committed registry on the
unmerged `kaika/round` branch. Branch ancestry was checked explicitly:

```
$ git -C .tower/worktrees/kaika/<lane> rev-parse HEAD
$ git -C .tower/worktrees/kaika/<lane> merge-base --is-ancestor <branch-OID> \
    "$(git -C /home/vgpnk/Projects/shokunin/<lane> rev-parse HEAD)"
# rc=1 for audio, game-dev-2d, kaidoku, kumitate -> branch commit is NOT an ancestor of main HEAD
```

Structural checks, same revisions, with observed exit codes (a `grep -c` that prints `0` exits 1):

```
$ git show <rev>:corpus/SOURCES.md | grep -cE '^ {1,3}#{2,3} '            # 0, rc=1 (all 21)
$ git show <rev>:corpus/SOURCES.md | grep -cE '^ {1,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'  # 0, rc=1 (all 21)
$ git show <rev>:corpus/SOURCES.md | awk -F'|' '/^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}'  # 0, rc=0 (all 21)
$ git show mori-shokunin@HEAD:corpus/SOURCES.md | grep -cE '^ {1,3}- '  # 3, rc=0 (only lane with indented bullets)
```

Interpretation limits of those checks: they show no indented **registry row** and no indented
SOURCES heading at these 21 revisions; mori's three `## Paths` bullets carry one leading space.
The pending parser fix is not evaluated here and is not needed to read this map.

No corpus gate, census aggregate, build, test, lint, format, or network fetch was run by this
seat. Gate findings quoted below are the audit notes' observations, attributed as such. The
gate's own declared non-coverage (r1, r3, r5, r6, r9, verifier independence, SHONEN truth) and
its implemented rules (r2/r4/r7/r8-literal/r10/SHONEN form) are not restated as whole-corpus
conformance.

---

## 2. Revision table (21 lanes)

`audited HEAD` = name in the lane audit note. `SOURCES read at` = the exact commit whose
`corpus/SOURCES.md` bytes this seat read. `sha256` is of those bytes
(`git show <rev>:corpus/SOURCES.md | sha256sum`); all 17 match
`source-count-reconciliation.md`'s independently computed values.

| lane | audited HEAD (audit note) | SOURCES read at | sha256 | §Paths / §Search log |
|---|---|---|---|---|
| audio | `defbe128649268bfca75757cb3978be802696592` | **in-flight** `343cd978ef376fc6e0c3d53a8740b931f7d031df` (`kaika/round`) | `43418ccf6086b7961ddc32beb5750896dadae2a50e26eca2f55e57c13a88040e` | 26–34 / 35–41 |
| chousa | `d730ae4c33989ad9c8535764d4cae77b4db869f6` | `d730ae4c33989ad9c8535764d4cae77b4db869f6` | `6428e46aa69d8554c09e06c5384ce2664ae3db79b6c9f3a072c07a11a957bbbf` | 30–45 / 46–71 |
| game-dev-2d | `e89905162b3a630a599607279681b30572010724` | **in-flight** `ff32e252b9301d5d25f863accedddddeda1ca569` (`kaika/round`) | `80add7f86437fc538a744e6340232171a3fcee5bf67bea47a48bebb916eb645c` | 39–45 / 46–52 |
| game-dev-3d | `3118be0b18dd7351b1faf6ce99d26a34370793ec` | `3118be0b18dd7351b1faf6ce99d26a34370793ec` | `dc95c043da258003dddc8957f168e3635fbd9fc587bace5232c7bdd3a824936f` | 46–53 / 54–65 |
| kagi | `1e9e67ff3f8f9e7118f8a7026c0e79aab9ce42b2` | `1e9e67ff3f8f9e7118f8a7026c0e79aab9ce42b2` | `db134917dab989f24c3e33b5983fdac7240fd412c9ebdf94a77c76a8fe55b332` | 24–29 / 30–33 |
| kaidoku | `1170f717c4ffeb3d0a9fd24522d8fb42f78fa837` | **branch read** `3b5fea8b1a7bc4590965e6cf18ef09ee574d0e9b` (`kaika/round`; blob read at `5ac7860` first, unchanged); **merged to main `767adaf…` during write, identical sha256** | `17fb2e45db74cc3e69a83384342bf343c77481239d357ab4590b1b510f37f133` | 30–39 / 40–43 |
| kake | `7e17c663b8713daac27774d49d87c4d44ea30747` | `7e17c663b8713daac27774d49d87c4d44ea30747` | `e1f07eb4929903c422946dca1617939dc1ea2aebdceb807a224e182704b98042` | 28–34 / 35–44 |
| kama | `03b5f0e8b9ec421c0b819b31e1bbc452b61dd0f9` | `03b5f0e8b9ec421c0b819b31e1bbc452b61dd0f9` | `9dc40d25a595b3d42b39649e17094cfa4e7190cfbf340331252dd29dea22093a` | 44–50 / 51–56 |
| kasegi | `13a51920068c48c0c5b3c8c81d5af0df6d4ea337` | `13a51920068c48c0c5b3c8c81d5af0df6d4ea337` | `0e8378bceb01f1c26045059044e85e9417bc933e15b4c774ec53ee34359dc940` | 35–40 / 41–49 |
| kengaku | `a42bb40c1767e1ac24394fadda7301ae5409e7ae` | `a42bb40c1767e1ac24394fadda7301ae5409e7ae` | `fb57569835c4f1c6a55decbf4a36b5f6dac8f6c3d3b2a961d3dfba4f48cf5cc5` | 50–57 / 58–65 |
| kotoba | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` | `ef331658e398dd552f8df992aade49d25025eb7b0309e7f2d3c00a7fd92e16d3` | 26–40 / 41–67 |
| kotodama | `4ad26836552462d28a946ca3b067cab0b5ce3532` | `4ad26836552462d28a946ca3b067cab0b5ce3532` | `662f962687717fa9cc66ec365c2c3e85ec79fc5ae5cd9fbc9df33dce3baa8e34` | 78–111 / 112–119 |
| kumitate | `16a5441a3347a10ac5ed169abcd5a17ba6f3f185` | **branch read** `0acb7752d19058b953ebbeba253b1e35f6548de5` (`kaika/round`); **merged to main `a5683a9…` during write, identical sha256** | `203b34e6c39705d39bac4704126627bc73bf8fef5a3d527ab97b7fc98d10df56` | 35–55 / 56–94 |
| lore | `6e804e2e5bff0edcc260c995a058dd724b0c98c0` | `6e804e2e5bff0edcc260c995a058dd724b0c98c0` | `9fc435e8095f8f867c18bd3b048c9d1f6c6040c9a60f6de5cb4d9d9e4dae9249` | 42–51 / 52–63 |
| mado | `e3e6a8e6ca493e250fb357343816a88e844c4c63` | `e3e6a8e6ca493e250fb357343816a88e844c4c63` | `9b175fa9925a7b7230ccb02cc121a0c5e932b5af4569f6c8b6df367540e07e23` | 52–60 / 61–93 |
| mori | `bf7cdc4783d0748d525fbfe3ba8fb3d285eb929a` | `bf7cdc4783d0748d525fbfe3ba8fb3d285eb929a` | `efe349d580266b8499d783d94b707012639d73173b57e09168a5a9df1d823ab6` | 42–47 / 48–53 |
| revenger | `cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97` | `cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97` | `c1573b2fbc284493096ddb20af506122aea0bcf7bc6b5a037b7dc31988f55f30` | 31–37 / 38–43 |
| souji | `31984f473ce4bdab61a99b16cca194b28108cb81` | `31984f473ce4bdab61a99b16cca194b28108cb81` | `1b7cc681084e9e5efcb3a89ff0f7943758d3040926c22f4cf5c58046ca548127` | 43–48 / 49–55 |
| tabi | `9bc89bfe78b1c455501b2c7a0d9bd061ea539c21` | `9bc89bfe78b1c455501b2c7a0d9bd061ea539c21` | `000053ccfc4e61f2dae220213ed42f59c25d168d8e0b64a07c28f1770abd5c77` | 44–50 / 51–58 |
| tameshi | `a21e9104723e7a46b794b03b8fdcdd1455696f7e` | `a21e9104723e7a46b794b03b8fdcdd1455696f7e` | `6b34e8991f56d78d561512d71c7eaeaf4f548f1d7f12eec8eb2b896bf6d72827` | 57–62 / 63–100 |
| tsukuroi | `d8ec15d5e6c1d93370f5a85b929745e26577f4d8` | `d8ec15d5e6c1d93370f5a85b929745e26577f4d8` | `3e06c2ebb36f5feaf84978238a9bd36d76a2313c017a0f9916fbc0bf0259b2e2` | 42–47 / 48–55 |

Four-lane caveat (state changed during the run): at the audited HEADs, `audio`, `game-dev-2d`,
`kaidoku`, `kumitate` had no `corpus/SOURCES.md`. During this seat's run `kaidoku` merged to
main `767adafb97e2eef6980e2ad873d357e16721c467` (20:50:15) and `kumitate` to
`a5683a96cae2fcdcf313e4a3b47dea340d6451a9` (20:49:24); both main-HEAD SOURCES blobs are
byte-identical to the branch reads (`sha256 17fb2e45…` and `203b34e6…` above;
`git merge-base --is-ancestor <read-OID> HEAD` → rc=0 for both). `audio` and `game-dev-2d`
remain branch-only: their `kaika/round` heads are not ancestors of main HEAD (rc=1) and their
worktrees are still present. Never pair a branch read with the audited-HEAD gate result; re-read
at main HEAD after the lane merges.

---

## 3. Per-lane direct pointers to its own `corpus/SOURCES.md §Paths`

Format: **path title — S### sequence** (verbatim titles/sequences from that lane's §Paths).
The file path is `$R/<lane>/corpus/SOURCES.md` at the revision in §2; the first §Search log
heading/question follows each list. Line ranges are from §2. Registry row counts, tiers, and
statuses are *not* restated here as totals; use the lane audit note and the post-`FINAL LANES
READY` census for those.

**audio** (in-flight registry; §Paths 26–34):
- Game loudness — S001 → S002 → S003 → S004 → S006 → S005 → S007
- Godot asset path — S009 → S010 → S011 → S008 → S013
- Harness conventions — S012 → S006 → S001
- Filter-rate path — S005 → S014
- True-peak source scope — S001 → S015
Search log: "2026-10-19 — question: which primary sources ground the four round-101 candidate entries (K1, K3, K4, K5)?"

**chousa** (§Paths 30–45):
- Framing and admitting a claim — S008 → S002 → S004 → S003
- Following a citation chain — S003 → S005 → S006 → S007 → S010
- Keeping judgments honest — S009 → S011 → S012 → S017
- Lane mechanics — S001 → S013
Search log: "Pre-assigned sweep (round 24, 2026-10-19)"; then rejected-candidate and expansion sweeps.

**game-dev-2d** (in-flight registry; §Paths 39–45):
- Tilemap physics attribution — S004 → S003 → S005 → S002 → S027 → S029 → S030
- Replay invariants — S011 → S010 → S009 → S025 → S030
- Resource and UID pipeline — S008 → S026 → S028 → S006
- Test runner to shipped artifact — S020 → S021 → S018 → S019 → S006 → S008 → S007 → S024
Search log: "Sweep 1 (reuse + verify)."

**game-dev-3d** (§Paths 46–53):
- Floor classification threshold — S012 → S011 → S035
- Godot 3D fixture and asset workflow — S005 → S004 → S003 → S001 → S006 → S009 → S007 → S008 → S002
- Headless mode to renderer claims — S016 → S017 → S014 → S015 → S032
- Asset interchange to target import — S020 → S025 → S021 → S022 → S023 → S024 → S018 → S013
- Deterministic oracles to exploration — S033 → S034 → S027 → S029 → S028 → S031 → S030
Search log: "Godot side (round 108, 2026-10-19)"; plus the non-Godot side.

**kagi** (§Paths 24–29):
- Machine credential custody boundaries — S001 → S004 → S002 → S003 → S006 → S007
- Encrypted-file key lifecycle — S009 → S010 → S011
- Vault and OpenBao authentication/lifecycle — S012 → S013 → S014 → S015 → S016
Search log: "Question: which primary sources support the allocated machine-credential and encrypted-file/Vault lifecycle boundaries?"

**kaidoku** (branch registry; merged after the audit; §Paths 30–39):
- Host evidence and recorded-core boundaries — S001 → S002
- Go ≥1.26 recovery and cross-version matching — S003 → S004 → S005 → S006
- LLM and lifted-representation evidence — S008 → S009 → S010 → S011
- Electron integrity and `.jsc` — S012 → S013 → S014 → S015 → S016 → S017 → S018
- ARM64X and Linux Mach-O study route — S007 → S019 → S020
- EVM selector boundary — S021
- Provider, size, and version gaps remain gaps — S001 → S002
Search log: one 2026-10-19 entry; question/query begins "identify a current primary study on LLM decompilation fidelity while checking for Ghidra and Electron documentation leads".

**kake** (§Paths 28–34):
- GHP served-set semantics — S003 → S004 → S001 → S008 → S002 → S006
- Custom-domain ownership — S003 → S007 → S005 → S017
- Validators and crawl hygiene — S010 → S009 → S011 → S012 → S013
- Citation freshness — S014
Search log: "For these bounded reviews, 'included' means retained as a registry row…"; three dated sweep notes.

**kama** (§Paths 44–50):
- Health and readiness — S001 → S004 → S006 → S020 → S017 → S021
- Served identity (next entry, K02) — S016 → S001 → S010 → S011 → S012
- Serving observability — S001 → S003 → S022 → S007 → S019 → S018
- GGUF and quantization boundary — S014 → S015 → S005 → S008 → S013
Search log: "2026-10-19 — ART dossier re-open"; then ART leads and a community claims sweep.

**kasegi** (§Paths 35–40):
- CVSS severity and CWE prioritization — S002 → S001 → S013 → S014 → S015
- CVD timelines and coordination — S003 → S004 → S005 → S018 → S019 → S020 → S021 → S022 → S023 → S024 → S016 → S017
- Authorization and AI finding validation — S006 → S007 → S008 → S009 → S010 → S011 → S012 → S025
Search log: "CVSS v4 severity and vector guidance; query: …"; six bounded sweeps.

**kengaku** (§Paths 50–57):
- contamination audit — S001 → S002 → S004 → S005 → S006 → S022
- judge calibration — S012 → S009 → S010 → S011
- agentic evidence — S013 → S014 → S020 → S021 → S005
- statistical reporting — S015 → S016 → S017 → S018 → S019
- saturation and lifecycle — S008 → S007 → S005 → S001
Search log: "Re-open sweep of the 19 ART leads (2026-10-19)"; plus four lead-specific sweeps.

**kotoba** (§Paths 26–40):
- Authoring a SKILL.md that loads everywhere — S001 → S008 → S003 → S002 → S011 (the rejected tutorial is last; the file says knowing the rule it gets wrong makes it evidence of taste)
- Why the comparator distrusts its input JSON — S006 → S007 → S009 → S010
Search log: "2026-10-19 — leads sweep for round-46 rows"; plus own-work gate selection and rejected-row verification.

**kotodama** (§Paths 78–111; 15 sequences):
- Typology evidence chain — S001 → S002 → S003 → S004
- Kinship and society grounding — S007 → S005
- Lexical history design — S006 → S011 → S010
- Conlang method — S008 → S009 → S012
- Motif-grid grounding — S013 → S014 → S015
- folktale index practice — S018 → S016 → S017
- belief legends — S019 → S020
- period and polity assertion — S022 → S023
- costume cataloguing — S024 → S025 → S026
- iconography — S027 → S025
- LLM-assisted narrative — S021 → S020
- women's hunting — S041 → S031 → S033 → S032
- mobility and dependence — S040 → S034 → S042
- sharing and the romantic frames — S035 → S038 → S037 → S036
- optimality — S039 → S034
Search log: "Linguistics, typology, conlang and motif leads (rows S001–S015)", then rows S016–S030 and S031–S043.

**kumitate** (branch registry; merged after the audit; §Paths 35–55):
- Kimi MCP plane — S005 → S006 → S007 → S008 (ends at the live census; documented surface before host residue)
- OMP delegation contract — S001 → S002 → S003 → S004
- Multi-agent design judgment — S015 → S016 → S018 → S010 → S011 → S012 → S013 → S014
Search log: "MCP revision delta — query 'MCP specification 2026-07-28 changelog stateless sessions'…"; plus Kimi MCP/tower surfaces, MAST taxonomy, direct-locator pass.

**lore** (§Paths 42–51):
- Provenance and validation layers — S001 → S002 → S007 → S008 → S018
- Chronology and dependency — S003 → S019 → S009 → S010
- Continuity error classes — S011 → S012 → S017 → S016
- Myth comparators and bible practice — S004 → S005 → S006 → S014 → S013 → S015
- In-world time — S003 → S020 → S022 → S021 → S023
- Supersession and canon status — S024 → S025 → S026 → S001 → S027
- Correction bullet (round 103 post-review): the In-world time path's related entry was rejected at re-grade and moved to `.ufo/waves/round-103/rejected/r103-in-world-dating-and-uncertain-time.md`; S020–S023 are `queued` again; S032 supersedes S023's anchor; the path stands as a study sequence only.
Search log: "2026-10-19, lane-citation sweep", plus seven further notes (the last a post-review duplicate-URL explanation).

**mado** (§Paths 52–60):
- Window-rule effects (U1) — S002 → S018 → S019 → S020 → S016 → S017
- Configuration-language era (U2) — S021 → S023 → S022 → S024 → S025 → S026 → S027 → S028 → S029 → S030
- Portal routing and ScreenCast (U3) — S032 → S033 → S034 → S035 → S031 → S037 (S036, S038, S039 queued side reading)
- Drift re-anchor (own method) — S015 → S014 → S013
- Protocol and input debugging frontier (U4/U6, queued) — S009 → S008 → S005 → S006 → S007 (S010 discovery index only)
- How this lane judges its own claims — S003 → S004 → S001
Search log: "Round 12 (2026-10-19), one note per bounded search, by seat:"; then a search-log errata block (see §7).

**mori** (§Paths 42–47; bullets carry one leading space):
- kernel and userspace kill attribution — S003 → S004 → S002 → S013 → S015 → S014 → S032 → S007 → S011 → S016
- signal instrumentation and pipeline failure modes — S005 → S006 → S019 → S020 → S031 → S014 → S015
- fleet runway and telemetry vocabulary — S033 → S001 → S002 → S029 → S028 → S022 → S024 → S023 → S025 → S026 → S027
Search log: "Bounded search 1 — Question: which of the 30 preselected ART candidates…"; then "Bounded search 2" (one unavailable lead).

**revenger** (§Paths 31–37):
- `scoring a tool claim` — S003 → S004 → S007 → S014
- `what a digest proves` — S006 → S005 → S014
- `decoding a resource name field` — S009 → S010 → S011 → S013
- `host readiness` — S002 → S001
Search log: "2026-10-19, tool validation and digest scope (rows C12, C13)", then two more entries.

**souji** (§Paths 43–48):
- F1 git-native housekeeping — S002 → S001 → S009 → S003 → S004 → S010 → S011
- F3 duplicate verdicts — S017 → S016 → S019 → S018 → S020 → S021
- F4 safe removal — S029 → S022 → S023 → S025 → S024 → S026 → S027 → S028
Search log: "Re-open sweep of the W1 ART leads (2026-10-19)", then revision pinning and two named negative sweeps.

**tabi** (§Paths 44–50):
- `profile-isolation` — S002 → S001 → S004 → S003 (terminal: `knowledge/chrome-remote-debugging-profile-boundary.md`)
- `protocol-choice` — S002 → S005 → S006 → S012 → S011 → S008 → S009 (terminal: `knowledge/webdriver-bidi-capability-matrix.md`)
- `flake-receipts` — S013 → S014 → S017 → S015 → S016 → S018 → S019 (terminal: `knowledge/web-flake-retry-evidence.md`)
- `accessible-selectors` (queued, not mined) — S025 → S023 → S024
Search log: "2026-10-19 · profile-isolation (TabiCdpProfileExec)", then three more entries and an L1 reopen spot-check.

**tameshi** (§Paths 57–62):
- Mutation verdict semantics and validity — S001 → S002 → S004 → S006 → S011 → S010 → S009 → S007
- Golden and hermetic fixtures for CLI gates — S015 → S016 → S017 → S028 → S013 → S014 → S018
- Reduction and generation of fixtures — S024 → S022 → S023 → S019 → S020 → S021 → S012
Search log: "2026-10-19 — re-open sweep of the W1 ART lead set (SOURCES contract rule 1)", then the W1 restatement and a frontier lead sweep.

**tsukuroi** (§Paths 42–47):
- Rollback net on this host (U1/J4) — S023 → S018 → S019 → S020 → S028 → S027
- Update gate without `-Sy` (U2) — S010 → S009 → S012 → S001 → S013 → S006 → S005
- Boot repair on busybox + LUKS + Limine UKI (U3/J3) — S026 → S014 → S025 → S017 → S015 → S016 → S021 → S022 → S002
Search log: the W1 prior batch attribution to `tsukuroi-art.md` §0/§6, then this round's bounded re-open pass and the L1 re-run.

---

## 4. Transferable study paths tied to exact W1 artifact headings

Selection rule: only paths stated in the four committed W1 artifacts, with their exact section.
A study path is a reading order, not an admitted claim; no row here is evidence for a lane's
proposition. "Expansion" means source reading that can seed `knowledge/`; "capability" means it
changes an instrument, gate, or method.

| # | W1 artifact + § | Path as written | Type | Boundary |
|---|---|---|---|---|
| T1 | `$W/.ufo/waves/kaika-w1/art-learning.md:77` §Study paths, bullet "Build a lane source/skill loop" | S005 → S006 → S007 → S003 → S004 → S001/S019 | Expansion | Skill packaging/evaluation/comparison; does not establish a lane's QUALITY bar or outside review. |
| T2 | same `art-learning.md:77`, bullet "Keep proposal search subordinate to verification" | S007 → S008/S009 → S010/S011 → S012/S013 → existing `AXES.md`/`LEARNING.md` | Expansion + process | Optimizer proposals remain candidates behind the no-harm gate; never the round verdict. |
| T3 | same `art-learning.md:77`, bullet "Study memory retention without importing destructive forgetting" | S018 → S015 → S016 → S014 → S017 | Expansion | Recheck/supersede only; no automatic deletion or silent rewrite. |
| T4 | `$W/.ufo/waves/kaika-w1/art-mistakes.md:150` §Study paths, bullet "LLM correction: limits → diagnosis → verifier → current benchmark" | S001 → S002 → S004 → S003 → S011/S012 → S009 → S010 | Expansion | A correction claim needs an independent, revision-pinned check; self-review is not the verifier. |
| T5 | same `art-mistakes.md:150`, bullet "Human/team learning: surface risk → learn safely → review → preserve cases" | S019 → S017 → S018 → S020 → S021 | Expansion + process | Human-training and incident-archive findings are analogies; no prevalence claim from case counts. |
| T6 | `$W/.ufo/waves/kaika-w1/art-apprenticeship.md:70` §Study paths, path 1 "From activity to defensible practice claim" | Ericsson 1993 → Macnamara 2014 → Ericsson 2016 → Macnamara reply 2016 → Macnamara & Maitra 2019 | Expansion | Preserve the disagreement; hours or repetition are not a promotion threshold. |
| T7 | same `art-apprenticeship.md:70`, path 2 "From apprenticeship to autonomous craft" | Lave & Wenger ch.1 → ch.4 → Collins et al. 1991 → Dreyfus 2004 → Kahneman & Klein 2009 | Expansion | Analogy to ranks; retained outside review remains the authority for taste claims. |
| T8 | same `art-apprenticeship.md:70`, path 3 "From tradition to adaptive form" | Bradić 2023 → Reguli 2018 → Calmet 2024 | Expansion | Do not turn shu-ha-ri into a universal exam; the direct study is one judo-kata case. |
| T9 | `$W/.ufo/waves/kaika-w1/art-curation.md:40` §Proposed final `SOURCES.md` contract (+ `:36` §How lane QUALITY.md should reference tiers) | Contract fields/rules, not an external sequence | Capability | Already frozen as `$W/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`; do not fork a second method or a second tier taxonomy. |
| T10 | `$W/.ufo/waves/kaika-w1/art-mistakes.md:75` §Audit rounds (5 numbered phases) | premortem → evidence review → closure check → next-audit recurrence → corpus-wide audit | Capability | Operating procedure, not a source list; do not convert a premortem into a verified finding. |

Source-row reading of the same artifacts is already available in their own registries
(`art-learning.md:105`, `art-mistakes.md:168`, `art-apprenticeship.md:114`, and
`art-curation.md:68`). Those rows are dossier-local IDs, not lane registry IDs; each lane must
allocate its own `S###` and re-open the source before writing a row (contract rule 1).

Two W1 curation lessons that are directly reusable, exact to `art-curation.md`:
- `art-curation.md:106` §Mistakes mined, M01–M04: primary/A is not a claim verdict; CRAAP is
  not an equal-weight score; HTTP 200 does not prove reference content survived; a clean
  structural gate is not semantic support.
- `art-curation.md:116` §Leads (unopened / access-limited): NATO AJP-2.1 (HTTP 403),
  TARCiS (HTTP 403), current GRADE Book pages (empty shell), LOC WARC page (HTTP 403). These
  remain leads; the opened UK JDP 2-00 is the substitute primary for the reproduced table.

---

## 5. Knowledge expansion vs tooling/capability acquisition

The frozen contract separates the two: expansion counts admitted `knowledge/` entries whose
`source:` cites a `mined` row on uncovered coverage-map ground; SOURCES.md itself, gates, and
own-work instrument rows are capability evidence, not expansion (`SOURCES-CONTRACT-v1.md`
rule 4). Observed examples at the revisions in §2:

| lane | expansion evidence (admitted entry ← mined rows) | capability/tooling evidence |
|---|---|---|
| chousa | S002/S004 carry `used-by = corpus/knowledge/contextual-source-admission-r24.md`; S003 carries both that entry and `citation-chain-fidelity-r24.md` (registry rows read) | S001/S013 "Lane mechanics" path is the gate's own append/JSONL rule |
| kagi | the three paths' rows carry `used-by` into `onepassword-machine-credentials.md`, `sops-age-key-rotation.md`, `vault-openbao-token-lease-lifecycle.md` (audit-kagi §9 verified ids/status/used-by) | — |
| kake | GHP path terminates in `knowledge/ghp-served-set.md` with `source: S001, S002, S003, S004, S006, S008` (audit-kake §8) | S014 is the lane's own freshness gate |
| kasegi | CVSS/CWE path feeds `knowledge/cvss-v4-severity-and-vector.md` and `knowledge/cwe-top25-2025-methodology.md` (audit-kasegi §8) | — |
| tabi | three paths end at three named `knowledge/` entries (registry text) | — |
| mado | U1's six ids are exactly the `source:` set of the README index row for `knowledge/window-rule-effects-getprop.md` (audit-mado) | "Drift re-anchor (own method)" S015 → S014 → S013 |
| mori | path 1 feeds four `knowledge/*-r12.md` entries (audit-mori §4) | S033 (own census) and the telemetry/runway vocabulary path |
| kotoba | — | four `mined` rows carry `used-by = SKILL.md` (audit-kotoba §7): instruction-surface adoption, not `knowledge/` expansion under rule 4; S009/S010 are own-work verifiers |
| kotodama | paths are study sequences; supersession rows S044–S047 are the post-review corrections | — |
| lore | In-world time and Supersession paths named related entries; the dating entry was rejected at re-grade and moved out (registry correction bullet) | S018/S019 are own gates (two ran; three not run) |
| kumitate | OMP and Kimi path rows carry `used-by = knowledge/omp-task-contract.md` and `knowledge/kimi-mcp-plane.md` (audit-kumitate §5, on `kaika/round`) | S004/S008/S009 are own-work command rows; the round-34 `sources-check.mjs` parser fix is a gate capability |
| tameshi | — | S031–S037 are own-work/gate rows; S032–S037 pin sibling fleet repos at exact commits (audit-tameshi §3) |
| revenger | decoding path ends in a byte-identified saved r59 record (audit-revenger §5) | S014 is the lane's own r7/r8 scoring case |
| souji | F1 feeds `git-auto-maintenance-prunes-worktrees.md`, `git-grace-periods-and-expire-to.md` (audit-souji §4) | S033 is a own negative finding; revision pinning is the lane's method |
| audio | the registry search log says the four round-101 candidates (K1, K3, K4, K5) cite rows among the 13 included | S005/S006 are pinned ffmpeg internals explaining the lane's own meter runs |
| game-dev-2d | paths cite knowledge entries in their rationale (in-flight registry) | S030 is own-work measurement; S015/S031 are rejected externals |
| game-dev-3d | six mined rows point at exactly two entries, `godot-headless-not-render.md`, `godot-floor-angle-threshold.md` (audit-gd3d) | S035 is the lane's own boundary scan |
| kaidoku | paths are literature/tool documentation only; registry states no local REA capability claim | — |
| kama | two entries are the target of the sources (paths say "next entry, K02") | own gate evidence is referenced in the round lesson, not in the registry |

Capability caveat: the `SOURCES.md` capability row enters `SCORECARD.md` only if every census
command in the contract runs clean (`kaika/lane-addendum.md` §6.4). A structurally clean
registry is not admission integrity, source truth, or whole-corpus conformance.

---

## 6. Rejections and flips observed (exact)

Only rows/notes opened by this seat, or quoted by an audit note at the named revision, appear
here. A rejected row is retained evidence of taste; the flip condition is part of the row's
`teaches` cell unless a note says otherwise.

| lane / rev | id | rejection reason (short) | flip | source of the text |
|---|---|---|---|---|
| kagi @ `1e9e67f` | S008 | SOPS upstream README lists formats/backends, delegates lifecycle mechanics to the docs site; no rotation procedure | a README revision that restores lifecycle mechanics | `corpus/SOURCES.md` row S008 |
| audio @ `343cd97` (in-flight) | S011 | §Paths calls it "the tutorial that did not follow (and why it is rejected)"; the row's rejection text was not read by this seat | not read by this seat | `§Paths` "Godot asset path" bullet |
| chousa @ `d730ae4` | S014 | claim-scoped, not a universal source hierarchy | not read by this seat | `§Search log` rejected-candidate sweep |
| chousa @ `d730ae4` | S015 | self-reported vendor metrics | not read by this seat | same |
| chousa @ `d730ae4` | S016 | tertiary community synthesis | not read by this seat | same |
| game-dev-2d @ `ff32e25` (in-flight) | S015 | pre-release snapshot cannot ground current-stable claims | not read by this seat | `§Search log` sweep 1 |
| game-dev-2d @ `ff32e25` | S031 | Godot 4.4 page predates physics chunking; 4.4 is end-of-life per S001 | not read by this seat | `§Search log` sweep 3 |
| kasegi @ `13a5192` | S026 | CISA Gold Eagle describes a program without a checkable validation protocol or general-efficacy results | not read by this seat | `§Search log` validation sweep |
| kasegi @ `13a5192` | S027 | link-only HN item; destination returned 403 | not read by this seat | `§Search log` "General bug-bounty advice" |
| kengaku @ `a42bb40` | S023 | vendor marketing; contamination-resistance claim contradicted by a later OpenAI self-reported audit (~30% broken tasks) | not read by this seat | `§Search log` Scale SWE-Bench Pro lead |
| kotoba @ `c61a973` | S011 | tutorial contradicts the client contract | not read by this seat | `§Search log` rejected-row verification |
| kumitate @ `0acb775` (branch, now merged) | S019 | domain: OAuth proxy/token/session material belongs to the security province | "an orchestration-only clause that binds dispatch or queue behaviour" | `git show 0acb7752d19058b953ebbeba253b1e35f6548de5:.ufo/rounds/round-34/sources-gate.md` §Rejections recorded |
| kumitate @ `0acb775` | S020 | locator drift: old durable-execution URL redirects to an overview with no durability text | "the page regains the durability semantics" | same |
| lore @ `6e804e2` | S017 | use of an LLM-as-judge consistency checker as authority on in-world canon; lane refuses that authority | not read by this seat | `§Search log`; audit-lore |
| mado @ `e3e6a8e` | S030 | duplicate of S017 (same wiki URL; overlapping current-wiki syntax scope) with no `supersedes` | "a distinct anchor at a pinned revision that S017 does not cover" | `§Search log` errata (reason cannot be moved into the `teaches` cell under append-only rule 2) |
| tsukuroi @ `d8ec15d` | S029 | stale package-version coverage | not read by this seat | `§Search log` |
| tsukuroi @ `d8ec15d` | S030 | equivalent `web_search` tool not mounted; ART-recorded answer contradicts S020 | not read by this seat | `§Search log` |
| tsukuroi @ `d8ec15d` | S033 | synthesized answer; equates mode 555 with a read-only mount and recommends operator actions | not read by this seat | `§Search log` L1 re-run |
| tameshi @ `a21e910` | S029, S030, S046 | rejected (ids verified; reasons not re-read by this seat) | not read by this seat | registry status column |

W1 artifact-level rejections (not lane rows): `art-learning.md:83` §Rejected as direct protocol
replacements (automatic decay/deletion, self-reflection as admission authority, scalar reward as
round verdict, raw trajectories as shared knowledge); `art-mistakes.md:155` §Rejected candidates
and reasons (self-critique proves repair; every failure becomes a rule; incident counts rank
lanes; premortem risk list is a finding); `art-apprenticeship.md:76` §Mistakes and rejected
simplifications M01–M05 (10,000-hour threshold; shu-ha-ri as exam; practice explains all
variance; time/repetition/error totals as improvement; confidence/rank as expertise).
These W1 texts record reasons but predate contract v1's `flip:` requirement; a lane promoting one
must re-open it and write the flip condition.

---

## 7. Evidence gaps and sharp edges (exact)

1. **Four registries were absent at the audited HEAD; two merged during the run.** `audio`,
   `game-dev-2d`, `kaidoku`, `kumitate` had no `corpus/SOURCES.md` at their audit-note HEAD.
   `kaidoku` and `kumitate` then merged to main (`767adaf…` and `a5683a9…`) with SOURCES bytes
   identical to the branch reads (hashes above; read OIDs are ancestors, rc=0). `audio` and
   `game-dev-2d` remain branch-only (`kaika/round` not an ancestor of main HEAD, rc=1), so do
   not pair their in-flight Paths with the audited gate verdict. Also, do not treat absence at
   the audited HEAD as a claim that a lane has no reading plan: `game-dev-2d`'s nearest
   committed reading path is `corpus/README.md`, an annotated tour of lessons r1–r19 only
   (audit-game-dev-2d §4); `kaidoku` carried the registry as round-13 debt
   (`corpus/lessons/round-12-verifier-spotcheck.md:17`, `SCORECARD.md:2110`) until the merge;
   `audio` keeps per-round scout provenance files under `corpus/live/r9x-scout/sources/`.
2. **kagi search log does not reproduce its own count.** `corpus/SOURCES.md:32` instructs
   `grep -cE '^\| S[0-9]{3} ' <kagi-art.md>` and reports 29; running it returns `0` (rc=1)
   because the dossier's rows are `|S001|…` with no space after the pipe; the tolerant pattern
   `^\| ?S[0-9]{3}` returns 29. The quoted path is also a `.tower/worktrees` path (ephemeral by
   the parent's convention). Cause verified from the dossier bytes (audit-kagi §8). Historical
   evidence is unchanged; this is a reproducibility finding, not a gate rule.
3. **kake's tier-definition pointer is dangling.** `corpus/QUALITY.md:22` says tiers are
   defined in `corpus/SOURCES.md`; the file's headings are Registry/Paths/Search log/Leads and
   its only tier prose is "Tiers are scoped to the row's stated topic, not global judgments."
   No A/B/C definition appears, and no row uses B (audit-kake §7).
4. **kengaku's LOG count is stale.** `LOG.md:244-246` states 25 rows, `A=24 C=1`,
   `mined=18 queued=5 rejected=2`; HEAD has 26 rows, `A=24 C=2`, `18/5/3`. The change landed
   in `e21f9ea` (+S026); `LOG.md` was not touched and the LOG paragraph was not errata'd
   (audit-kengaku §SOURCES).
5. **tabi's lesson/LOG figures are pre-post-review.** The lesson says "all 27 rows are new" and
   `LOG.md:489-491` states 27 rows (A21 B4 C2; 19/6/2); HEAD has 28 after S028
   (`supersedes S004 —`) (audit-tabi §4). Any parent ledger quoting 27 is quoting the pre-fix
   state.
6. **mado commits a rejected row inside a navigation path.** The U2 path ends
   `… → S029 → S030`, and `corpus/README.md:35` cites `S021–S030`, while S030 is `rejected`
   (`SOURCES.md:41`); the errata records `status mined → rejected in place` and moved `used-by`
   to S017, but the path and README row were not updated. Navigation/staleness defect, not a
   sourcing gap; S021–S029 remain mined (audit-mado). The same errata discloses four `queued`
   rows (S006, S008, S009, S010) whose anchors carry a section plus access date but no page
   revision, and corrects the portal seat's "excluded 0" count, which came from
   `printf '%s' '' | wc -l` (empty input), not a count.
7. **lore records a deliberate duplicate URL and a post-review flip.**
   `S012` and `S017` open the same arXiv HTML URL for different scopes; the fleet census flags
   the pair as a duplicate-URL finding (E04) without `supersedes`, and append-only rule 2
   forbids editing S017's `source` cell, so it stands as a recorded exception. Separately, the
   In-world time path's related entry was rejected at re-grade and moved to
   `.ufo/waves/round-103/rejected/`; S020–S023 are `queued` again and S032 supersedes S023's
   anchor.
8. **tameshi's S020 access caveat is disclosed, not smoothed.** The canonical Springer URL
   returned an anti-bot body (3,038 B, 200) and its `/content/pdf/` route a 303; the row's quote
   comes from the authors' hosted copy, canonical DOI kept. Its id space allocates S038–S039,
   never written, retired, never reused (audit-tameshi §3).
9. **tsukuroi's S030 source cell is a worktree artifact.** The `source` cell is
   `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-ledger/.ufo/waves/kaika-w1/tsukuroi-art.md`;
   it existed at audit time but is not a durable repo file; S030 and S033 are `rejected`, so
   neither supports an admitted claim (audit-tsukuroi §5). The lane also records that the
   equivalent `web_search` tool was not mounted (`read xd://mcp__rea_web_search` → "No such
   tool"), that four synthesized tier-C answers were excluded as support, and that a later L1
   re-run produced rejected S033.
10. **game-dev-3d's cross-lane header claim is unresolved.** Its header says game-dev-2d's
    registry also carries the Godot CLI and GdUnit4 pages ("its S006, S020"); at the audited
    fleet state that registry does not resolve because game-dev-2d has no SOURCES.md at its
    main HEAD (audit-game-dev-3d). The in-flight game-dev-2d registry does contain S006 and S020
    ids in its §Paths, but this seat did not open those rows to verify the cross-claim.
11. **kotodama's preamble row-range is behind the registry.** The preamble says
    "`lessons/round-49.md` for S001–S043" while the registry holds S001–S047; S044–S047 are the
    post-review supersession rows (S044→S034, S045→S038, S046→S039, S047→S029) documented at
    `SOURCES.md:73-76` (audit-kotodama §SOURCES). Documentation-completeness observation.
12. **kama under-uses its registry.** Its audit note records 20 distinct ids under §Paths and 10
    registry ids on no path (S002, S009, S023–S030): under-use, not a defect under the declared
    contract (audit-kama §3). Its rejections carry flip conditions (S024 province, S026
    unreleased PR, S027–S029 community, S030 contested L1 gate run).
13. **Parser-fix surface is absent in every registry read here — provisional.** No lane's
    registry has a `^ {1,3}\| S###` row at the revisions in §2 (all counts 0, rc=1); mori's
    three `## Paths` bullets are the only `^ {1,3}- ` lines (rc=0). The in-flight fix is
    therefore not expected to change these 21 files' row sets; that is an expectation at these
    revisions, not a frozen census statement.
14. **Audit-note status.** All 21 audit notes existed at write time and each named the HEAD this
    seat measured at read time; `kaidoku` and `kumitate` advanced afterward (§2 caveat). Their
    gate findings and counts are their observations; this seat ran no gate and does not adopt
    their verdicts. The notes themselves mark census numbers provisional.

---

## 8. Leads (unopened) — not evidence

Lane `## Leads (unopened)` sections exist in all 21 registries and the contract says a lead is
never a row. This seat did not use any lane lead as evidence and did not exhaustively enumerate
those bullet lists. For reuse, the section line range is in §2. Recorded details seen:
- mori: exactly one lead (GNU Bash Reference Manual, `pipefail`/`PIPESTATUS`) with no row id
  (audit-mori §3).
- kake: 17 unopened lead lines (audit-kake §7).
- kasegi: 3 unopened leads (Big Sleep tracker, ISO/IEC 29147+30111, UK AISI) (audit-kasegi §7).
- kumitate: S019/S020 are rejected, not leads; its `## Leads (unopened)` bullets were not read here.
- chousa/kotodama/tabi/tameshi/tsukuroi/mado/lore/audio/game-dev-2d/kaidoku/kagi/kotoba/kama/
  game-dev-3d/revenger/souji: section present; contents not treated as evidence.

W1 artifact leads (unopened there; still leads here):
- `art-learning.md:90`: Memory-R1 (ACL 2026), FadeMem (arXiv 2601.18642), CodeEvolve
  (arXiv 2510.14150), MemGPT/Letta (arXiv 2310.08560).
- `art-curation.md:116`: NATO AJP-2.1 official PDF (403), TARCiS full text (403), current GRADE
  Book chapter pages (empty shell), LOC WARC format page (403).
- `art-apprenticeship.md:108`: Collins/Brown/Newman 1989 chapter (PDF text extraction failed),
  Dreyfus & Dreyfus 1980 (incomplete extraction), direct 2025–2026 shu-ha-ri / cognitive
  apprenticeship studies.
- `art-mistakes.md:162`: AIID contributed taxonomy directory, ACE and Memento primary papers,
  broader EMT meta-analysis trail and newer replications.

A lead becomes usable only by opening it in the round that writes the row, with URL, access
date, and a ≤25-word quote at a named location (contract rule 1).

---

## 9. Bounded next pass (no score, no admission)

1. After the parent's exact `FINAL LANES READY` and the corrected parser: re-run §1's pin and
   read commands for all 21 lanes; if a lane moved, discard the old row and repeat both the
   gate snapshot and the SOURCES read at the new OID; do not mix revisions.
2. For each lane, choose at most one §Paths sequence on uncovered coverage-map ground, open
   every row at its named anchor/revision, and write a knowledge entry only if the lane's
   `QUALITY.md` admits it; expansion counts only admitted entries citing `mined` rows
   (contract rule 4). No row quota.
3. Keep capability work separate: SOURCES registry/gates/own-work instrument rows are
   capability evidence; they enter `SCORECARD.md` only if the contract census runs clean.
4. Preserve rejections with reason and flip; append corrections as superseding rows; never
   rewrite `source`/`teaches`/`tier` in place.
5. Non-author verification remains the parent's: ≥1 admit and ≥1 reject spot-checked, ≥3
   SOURCES rows re-opened, every counting command re-run (`kaika/lane-addendum.md` §6.6).
6. Treat every count in the lane audit notes as provisional until the post-barrier re-run; a
   gate pass is not semantic conformance (r1/r3/r5/r6/r9 and verifier independence are not
   evaluated).

---

## 10. Self-check

- Checked: 21 physical lanes; 21 audit notes; 21 lane HEADs; 17 committed registries read at
  their exact OIDs; 4 branch-only registries read at their exact branch OIDs (kaidoku and
  kumitate later merged to main with identical SOURCES bytes; audio and game-dev-2d remain
  branch-only); heading lines; content hashes for all 17 committed registries (each matches
  `source-count-reconciliation.md`'s independently computed value) and for the 4 branch blobs;
  row arity (NF=13) and indentation surface
  with exit codes; the four W1 artifacts in full; the cited rejection rows/notes at their
  revisions.
- Not checked: the truth of any `teaches` claim; URL content (no network fetch); tier
  correctness; the gate's verdicts (not run); the final census (blocked); the contents of lane
  leads; the two branch-only lanes' unmerged gate results; any lane's working-tree state beyond
  `corpus/SOURCES.md` cleanliness.
- No failed gate rule is claimed by this note. Where an audit note reports a failed rule, that
  is the note's observation at its named revision, not this seat's verification.
