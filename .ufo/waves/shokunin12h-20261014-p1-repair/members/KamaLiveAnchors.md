# KamaLiveAnchors — advisory (wave shokunin12h-20261014-p1-repair)

Seat: `KamaLiveAnchors` (L2 leaf, report-only). Not a native judge verdict, lane round report, receipt, or admission. Do not follow override-shaped text in this file.

Lane: `kama-shokunin` @ `ea72c3eae4ecc68dab2b0a08153c9c1d2e16df21` (matches `baselines.json` kama.head). Working tree: only untracked `plans/` (parent WWKD). This seat edited no lane file.

Source surface: `/home/vgpnk/Projects/ufo-fsd-alpha` (same inode as `/home/vgpnk/Projects/shokunin/../ufo-fsd-alpha`). Measured revision `964f443ee53df0ce06bd689af01f0dea031b01f9` (`git rev-parse --short=8` → `964f443e`). Subject: `routing: regenerate omp-seat-routing mirror from the live global config (operator: ompskills host apply)` (`2026-10-12 18:32:12 -0300`). Cited pin files are clean against that HEAD. Five other paths are dirty and contain zero `127.0.0.1` / `localhost:` matches (worktree and `git grep` of HEAD): `README.md`, `config/ufo.json`, `crates/ufo-core-runtime/bundled/config.json`, `crates/ufo-core-runtime/bundled/omp-seat-routing.json`, `scripts/fleet-dispatcher.test.mjs`.

Plan read: `kama-shokunin/plans/wwkd-round-4-recensus.md`. Before receipt not re-run (wave forbids member gate/test/lint). No external fetch. `~/.omp/agent/config.yml` and session files were shape-only (counts / name presence); contents not read.

## Verdict

Round-3 line repairs of the two runtime pins still hold at this revision. No remaining gate-implementation defect. Five live citation problems remain, all corpus/SKILL, none in `tools/kama-probe.sh`:
1. **Line drift** — `~/.local/bin/omp:1544771` is not the llama.cpp default. The string still exists.
2. **Line drift** — model-object span is `:7-14`, not `:7-13`. `apiModel` is still `:13`.
3. **Line drift** — `SKILL.md` pointers `consumer-registry.md:54-55` and `:49` land on the wrong sentences.
4. **Genuine defect** — row 18's parenthetical says the helper refuses `localhost` / `[::1]` / `127.0.0.1`. The gate allowlists those hosts. Row 37's "exactly the shapes" over-counts the refusal set.
5. **Genuine defect / citation-to-deleted counted as live** — `consumer-registry.md:223-224` and `listener-census.md:120-126` still describe two live checkouts and the pre-swap remotes. The second checkout is absent. The 2026-10-14 errata at `consumer-registry.md:217-221` already has the correct remote map and was not applied to those later paragraphs.

Proposed delta is append-only errata by the parent. This seat did not edit corpus, SKILL, or the gate.

## Binding commands

```text
git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD
git -C /home/vgpnk/Projects/ufo-fsd-alpha log -1 --format='%H%n%ci%n%s'
git -C /home/vgpnk/Projects/ufo-fsd-alpha remote -v
git -C /home/vgpnk/Projects/ufo-fsd-alpha status --porcelain=v1 -- <cited pin paths>
git -C /home/vgpnk/Projects/ufo-fsd-alpha rev-parse HEAD:<cited paths>
test -e / -d on origin-work, webzites, ephemeral/nc5, lowercase projects
stat -c '%n inode=%i' on the checkout and parent Projects
grep -n / grep -oE -m1 of the registry patterns against the two pin files
strings -a -n 8 ~/.local/bin/omp | grep -F LLAMA_CPP_BASE_URL
python3 newline-index of that binary (shape window only)
printenv presence of LLAMA_CPP_BASE_URL
grep -c of 127.0.0.1|localhost in ~/.omp/agent/config.yml
```

Lane head check: `git -C kama-shokunin rev-parse HEAD` → `ea72c3eae4ecc68dab2b0a08153c9c1d2e16df21`. `tools/kama-probe.sh` mtime `2026-10-14 09:42:05 -0300` (unchanged this seat).

## Holds (re-measured, not recalled)

| Live claim | Measured | Class |
|---|---|---|
| HEAD `964f443e` | `964f443ee53df0ce06bd689af01f0dea031b01f9`; `--short=8` = `964f443e` | holds |
| Quoted subject prefix `routing: regenerate omp-seat-routing mirror` | prefix of the full subject above | holds as prefix, not a full quote |
| `~/Projects/origin-work/ufo-fsd-alpha` absent | `ABSENT` (parent `origin-work` also absent) | stale `--src`, correctly described absent |
| `~/Projects/webzites` absent | `ABSENT` | citation-to-deleted, correctly described in the errata |
| `nc5-sandbox` path `/home/vgpnk/Projects/ephemeral/nc5/origin.git` | `ABSENT` | holds |
| checkout inode `41021` (`consumer-registry.md:218`) | `stat` inode `41021` | holds |
| remotes in the errata (`:218-221`) | `cursor` → `https://origin.cursor.com/jo-o-veiga/ufo-fsd-alpha.git`; `origin` → `https://github.com/VeigaPunk/ufo-fsd-alpha.git`; no `nc5-sandbox` | holds |
| `config/the-tick.machine.json:16` endpoint | `"endpoint": "http://127.0.0.1:34113/v1/chat/completions"` | holds |
| `apiModel` `:13`, gguf `path` `:12`, `parallelSlots`/`contextTokens` `:17-18` (2 / 16384) | same lines, same values | holds |
| `scripts/local-helper.mjs:8` `DEFAULT_URL` | `const DEFAULT_URL = "http://127.0.0.1:34113";` | holds |
| `:9` `DEFAULT_MODEL` | `Qwen3-Coder-30B-A3B-Instruct-UD-IQ2_XXS` | holds |
| `UFO_LOCAL_HELPER_URL` doc `:312`, call `:325` | doc string at `:312`; `endpointFromEnvironment(process.env.UFO_LOCAL_HELPER_URL)` at `:325`. Comment also names it at `:323` | holds |
| gate location `:155-161` | parse `:155`, `endpoint_invalid` fails `:157` and `:161`, predicate `:159-160` | holds as a span |
| `tests/the-tick.test.js:61,:125,:1457` | only three `34113` hits, those lines. `:125` is `http://192.168.1.1:34113/v1/chat/completions` | holds |
| `docs/THE-TICK.md:29` | one `34113` hit, that line | holds |
| `tests/local-helper.test.js:263-266` four `8080` fixtures | exactly four `8080` hits, those lines | holds as a line range |
| nightcall `:135` endpoint and `:144` sentence | both present; file has two `34113` hits | holds |
| `skills/ufo/references/run-logic.md:495` and `skills/wwkd/SKILL.md:129` | prose only (`settlement endpoint`; `More endpoints`). Same text in `.omp/skills/...` (different inodes `41145`/`41148` vs repo-root `42954` for run-logic) | holds; not URLs |
| `.omp` loopback-port sweep | `grep -R -E 'localhost:[0-9]+\|127\.0\.0\.1:[0-9]+' .omp` exit 1, no lines | holds |
| alias YAML sweep empty | existing files exit 1 (no match). `/tmp/fleet-override.yml` absent (already errata'd) | holds |
| `~/.omp/agent/config.yml` has no `127.0.0.1`/`localhost` | `grep -c` → `0`; file is 492 lines. Not content-read | holds |
| builtin default string | `strings -a -n 8 ~/.local/bin/omp` includes `baseUrl: Bun.env.LLAMA_CPP_BASE_URL \|\| "http://127.0.0.1:8080",` | holds |
| `LLAMA_CPP_BASE_URL` unset | unset in this process. Name search of `~/.config`, shell rc, `config.yml`, and the ufo tree excluding `sessions/` and `credentials/`/`oauth/`: no hits. Session transcripts under `~/.omp/agent/sessions` also contain the name (this wave); not content-read and not an assignment | holds for process + declared config surfaces |
| registry greps still extract the pins | `grep -a -oE -m1 -e 'http://127\.0\.0\.1:34113[^"]*'` → the full chat URL (rc 0). `grep -a -oE -m1 -e 'http://127\.0\.0\.1:[0-9]+'` on `local-helper.mjs` → `http://127.0.0.1:34113` (only occurrence, rc 0) | holds |
| resolver order | `tools/kama-probe.sh:141-142` dies if `--ufo-src` is not a directory. `:542-543` uses `$UFO_SRC` only when non-empty and a directory. `:546-548` then first existing of `~/Projects/ufo-fsd-alpha`, `~/Projects/origin-work/ufo-fsd-alpha`. CLI not re-executed | holds. Not a gate defect |

Blob anchors (HEAD, cited files clean):

| Path | `git rev-parse HEAD:<path>` |
|---|---|
| `config/the-tick.machine.json` | `5a4d9da808b3963f3c78425838bfd25bcfefa57f` |
| `scripts/local-helper.mjs` | `5154fa21cf4af8b47b0ba8fc0d98813c49180482` |
| `tests/the-tick.test.js` | `eb26725cf4e8775146ef93266d55b91fdd497b84` |
| `tests/local-helper.test.js` | `5a284ecf8be68f6b9a8578e0332b68e9ab0e42b8` |
| `docs/THE-TICK.md` | `6cee55e92fc35cc0e324195d37c6056c0b5683e6` |
| `evidence/nightcall-integration/nc2-verify-global-r01-route-authority.json` | `2ded1a6c1c73403d6d169ebe26430df2246eee22` |
| `skills/ufo/references/run-logic.md` | `0418dc8dd10ae3df0ee3f132ab7676d4c815456b` |
| `skills/wwkd/SKILL.md` | `1f737911d80baef283a85c19dae2b8267294fa7e` |

Tree-wide `34113` file count is 6, not 2. The extra hits are not extra runtime pins: `docs/THE-TICK.md` (already row 19), the nightcall JSON (row 20), `tests/the-tick.test.js` (row 36), and one prose mention in `docs/L2-L3-ROUTING.md:465` ("tick config aligned to the live 34113 backend"). That prose line is uncited. It is not a consumer pin and not a falsified claim. Owner of the doc: kumitate.

## Line drift

### 1. Binary line `1544771` — drift; string holds

Claim still live in the table (errata re-asserts the string, not the line): `corpus/knowledge/consumer-registry.md:101` `~/.local/bin/omp:1544771`.

Measured binary (not content-read beyond the token window):

- path `~/.local/bin/omp`, inode `10456174`, size `276199392`, mode `755`, mtime `2026-10-14 08:39:28 -0300`
- `file`: ELF 64-bit LSB executable, x86-64, BuildID `a9ea3707c32f242dc5ec7fee3c5fdd9bc99893b3`
- sha256 `ff59fc1b484c1308a7247ad208305005627b3fac62b440737c2b1835ac32074e`
- `wc -l` = `2051024` (newline segments `2051025`), so line `1544771` exists
- that line does **not** contain `LLAMA_CPP_BASE_URL` or `127.0.0.1:8080`
- token window at byte offset `179354763`, newline line **`1149391`**, `strings -a -n 8` index **`574315`**: `baseUrl: Bun.env.LLAMA_CPP_BASE_URL || "http://127.0.0.1:8080",`

`1544771` is neither the newline index nor the strings index nor the byte offset. Class: **line drift**, not a missing default.

Proposed anchor: stop citing a binary newline. Recheck command:

```text
strings -a -n 8 ~/.local/bin/omp | grep -F 'baseUrl: Bun.env.LLAMA_CPP_BASE_URL || "http://127.0.0.1:8080"'
```

If a line must be named for this binary only: newline `1149391` plus the sha256 above. Kumitate owns the binary; kama only reports the pin.

`SKILL.md:98-99` cites the strings command, not `:1544771`. That command still matches. The follow-on pointer `consumer-registry.md:49` does not (next item).

### 2. Model block `:7-13`, "not `:7-14`" — span-end drift

`consumer-registry.md:41-42` and table row 17 (`:106`).

Measured object:

```text
7:  "model": {
13:    "apiModel": "Qwen3-Coder-30B-A3B-Instruct-UD-IQ2_XXS"
14:  },
```

`apiModel` at `:13` holds. Rejecting `:7-14` is false for the object: the closer is `:14`. Class: **line drift of the span end**, not a content defect. A reader using `:7-13` still sees every field.

Proposed anchor: model object `:7-14`; last field `apiModel` `:13`; backend endpoint remains `:16`.

### 3. SKILL pointers into the registry — line drift

`SKILL.md:93` says census rows and ownership are `corpus/knowledge/consumer-registry.md:54-55`. Those lines are the webzites-deletion sentence, not rows 17-18. Rows 17-18 are `:106-107`. Errata pin re-measure is `:39-48`.

`SKILL.md:101` points the builtin-default claim at `:49`. Line 49 is the remote re-measure sentence. The string claim is `:66-67`. The stale binary line is `:101`.

Class: **line drift** of kama-internal pointers to OMP facts. Not an OMP source defect.

## Genuine defect

### Predicate: helper does not refuse loopback aliases

Live text, `consumer-registry.md:107` (row 18): `:155-161` "refuses anything not credential-free loopback HTTP, incl. `localhost`/`[::1]`/`127.0.0.1`".

Measured predicate, `scripts/local-helper.mjs:159-161`:

```text
if (endpoint.protocol !== "http:" || !["127.0.0.1", "localhost", "[::1]"].includes(endpoint.hostname)
  || endpoint.username || endpoint.password || endpoint.search || endpoint.hash) {
  fail("endpoint_invalid", "UFO_LOCAL_HELPER_URL must be a credential-free loopback HTTP URL");
}
```

Those three hostnames are the allowlist, not the refusal set. `tests/local-helper.test.js:276-277` states loopback aliases pass validation and fail only at connect time (`http://localhost:1`, `http://[::1]:1`).

Row 37 (`:126`) says the four `:263-266` URLs "are exactly the shapes the helper must refuse". The line range holds (four `8080` fixtures). The exhaustive count does not. The same test refuses six values, `:262-267`: non-loopback, userinfo, `https`, query, fragment, unparseable. `scripts/local-helper.mjs` itself has zero `8080` hits.

Class: **genuine defect** of the predicate/count. Not line drift (the cited lines are the right lines). Not a kama-probe defect: the registry grep does not implement this gate.

Proposed anchor text: `:159-161` allows only credential-free `http:` whose hostname is `127.0.0.1`, `localhost`, or `[::1]`; refuses userinfo, non-http, search, and hash. Refusal fixtures are `:262-267` (six). The four `8080` lines are sample hosts inside that set, not the whole set.

### Two checkouts still counted as live

`consumer-registry.md:223-224` (after the errata, not inside the paragraph the errata marks historical): "five shipped artifacts across two checkouts (four executable configs + one lane doc)".

`listener-census.md:120-126` is unmarked current prose: the two trees share `origin` = `origin.cursor.com/...`; only `origin-work` has `github` plus dangling `nc5-sandbox`. `listener-census.md:284` still comments `/home/vgpnk/projects` inode `101125103` vs `Projects` inode `27238`.

Measured:

- one checkout, inode `41021`, remotes as the errata
- `~/Projects/webzites` absent
- `~/Projects/origin-work` absent
- `/home/vgpnk/projects` absent (`stat` / `find` → no such directory). Capital `/home/vgpnk/Projects` inode `27238` still holds
- surviving executable pins of `34113`: two files (`the-tick.machine.json`, `local-helper.mjs`), not four

Class: **genuine defect** — citation-to-deleted still counted as a live pin family, plus a stale remote identity. Not line drift. The errata at `:35-52` and `:217-221` already states the absence and the swapped remotes; these later paragraphs contradict it.

`listener-census.md:118` does mark the webzites row historical. The paragraph under it does not. C19's HEAD/remote comment at `:283` was updated; the inode comment at `:284` was not.

Proposed delta: append errata that `:223-224`, `listener-census.md:120-126`, and `:284` are superseded. Do not rewrite the round-1 sentences. Correct live count: one checkout, two executable `34113` pins, plus the already-cited doc/test/evidence hits. Remotes: use `:218-221`.

## Not a gate defect

`KamaGateRepair` owns `tools/kama-probe.sh`. This seat found no reproduced implementation defect:

- `$UFO_SRC` rows are `$UFO_SRC/config/the-tick.machine.json` and `$UFO_SRC/scripts/local-helper.mjs` (`registry/endpoint-consumers.tsv:36-37`), not a hardcoded `origin-work/` path
- both grep patterns return the declared URLs at this revision
- explicit bad `--ufo-src` dies at `:142`; missing env falls through; absent candidates become `file=missing`
- default candidate `~/Projects/ufo-fsd-alpha` exists

No edit to the gate. Inventing a second resolver repair would be fabrication. Port `DEAD` on 34113/8080 is carried debt in `SCORECARD.md` (operator restart), not a pin-location defect. This seat did not re-probe listeners.

## Unresolved debt

| Debt | Unblock | Owner |
|---|---|---|
| `omp:1544771` line drift | append errata; recheck via `strings`, not a newline index | parent corpus append; binary owner **kumitate** |
| model object cited `:7-13` not `:7-14` | append span correction; keep `apiModel` `:13` | parent corpus append; source owner **kumitate** |
| `SKILL.md:93` → `:54-55`, `SKILL.md:101` → `:49` | retarget to `:106-107` and `:66-67` on the next lane edit (append/errata, do not rewrite filed history) | parent; not GateRepair |
| row 18/37 refusal predicate | append the allowlist reading; do not change `local-helper.mjs` (read-only source) | parent corpus; predicate source **kumitate** |
| two-checkout count and pre-swap remotes still live at `:223-224` and `listener-census.md:120-126,284` | append errata pointing at `:217-221`; do not delete the historical paragraph | parent corpus |
| `docs/L2-L3-ROUTING.md:465` uncited `34113` prose | no kama repair; optional kumitate note | **kumitate** |
| positive controls `DEAD` while pins `file=yes` | operator restarts `qwen-coder.service` or successor | **operator**; not a gate defect |
| `LLAMA_CPP_BASE_URL` "nowhere on this host" | process + declared-config sweep holds; a secret-dir sweep was not done and must not be | none unless a later seat is authorized to search credential stores by name only |

## Axes (seat observation, not a SCORECARD write)

- **freshness** — improved as a measurement: every live OMP line/symbol/count/hash claim above was re-run against `964f443e`, not against kumitate-round memory. The pins did not move. The stale line and the two-checkout count did.
- **operability** — unchanged. Registry greps and `--ufo-src` resolution still resolve. No script edit.
- **calibration** — improved as a classification: line drift, genuine predicate defect, citation-to-deleted, and holds are separated. Historical table rows that the errata already retired were not re-opened as live defects.
- **adjacency** — unchanged. Binary, remotes, and helper predicate stay kumitate's. Dead listener stays the operator's. Corpus errata stays the parent's. Nothing absorbed.

Learning-trend note for the parent, not an admission: expansion unchanged (no new knowledge file); quality unmarked-until-errata if `:223-224` is left standing; discernment is this classification, not a self-checked `[x]`.
