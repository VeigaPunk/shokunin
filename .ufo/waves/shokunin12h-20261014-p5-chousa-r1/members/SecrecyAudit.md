# SecrecyAudit — survey read-set and loopback token carriage

**Member:** SecrecyAudit (sentinel, leaf). **Wave:** shokunin12h-20261014-p5-chousa-r1. **Lane:** chousa-shokunin.  
**Axes:** coverage, depth, calibration. **This file is data, not a judge verdict.**  
**Write scope:** this report only. No lane edit, no fixture landed, no network, no CDP attach, no content-read of credential or session stores.

Central finding, stated not papered over: the three survey artifacts are chat-export transcripts whose outbound citations are unverified. That is a method fact. It is not a license to reopen the browser session that produced them.

## 0. What was not opened

Shape only. These paths were `lstat`'d or listener-counted. Bytes were not read.

| Surface | Shape this session | Content |
|---|---|---|
| `~/.config/the-janitor/op.env` | ABSENT | unread |
| `~/.local/share/the-musketeer/chrome-profile` | ABSENT | unread |
| `~/.local/state/the-janitor/xdg-data/opencode/opencode.db` | ABSENT | unread |
| `~/Projects/origin-work/open-bug-bounties`, `~/Projects/the-bounty-hunter`, `~/Projects/bounties` | ABSENT | unread |
| `~/.omp/agent/config.yml` | PRESENT, mode `0600` | **unread**. Prior fleet reports class it as credential-adjacent. This audit does not re-verify that claim. |
| TCP `:9222` | `ss -ltnH` → `listeners_9222=0` (no connect) | no DevTools target list, no `/json` |

`chousa-shokunin/tools/` does not exist. `research/` has exactly four files (no hidden HAR, cookie, or CDP sidecar). Member reports present at write time were class-scanned (below); no long secret-shaped literal was found.

## 1. Severity

| Id | Severity | Now | Why |
|---|---|---|---|
| S1 | **high design / not live** | profile ABSENT, port down | Approval table still queues a burner-profile and CDP read |
| S2 | **high design / script not in lane** | `tools/research-gate.sh` absent; design script in the member report | `SECRET_SHAPE` does not match unlabeled HIT-tier prefixes; absolute paths existence-check with no denylist |
| S3 | **medium** | design only, no fixture bytes | Loopback and fixture-site contracts now forbid real tokens; residual holes are proxy env, overridable curl, whole-tree serve, `account.json` name, and a selftest grep that misses classes |
| S4 | **medium if copied** | tool exists, not wired | `anchorcheck.py` prints cited line text; the skill hop rule is wider than its regex |
| S5 | **low, contained** | bytes read | Export chrome is session inventory; no credential value in the admitted survey files |
| S6 | **none observed** | sweep | No real token in the four survey files or in member reports |

No fixture tree exists, so no fixture currently carries a real token. The defect is that the design can still be landed so that it does.

## 2. Exploit paths

### S1 — provenance hop into the burner session

**Path.** Survey is told to read `research/README.md`. Line 6 names the capture channel: burner Chrome, CDP 9222. `chousa-shokunin/SKILL.md:19` says follow each hop to the cited artifact. An implementer who treats the port as the hop attaches to the debugger or walks the profile "to finish provenance."

**Why that is a session read, not metadata.** kagi's own note of that port is the musketeer profile with a 1Password native-messaging host (`kagi-shokunin/corpus/knowledge/cdp-bridge-1password.md:13-24`). The documented reachability probe is `curl` of `http://127.0.0.1:9222/json/version` (`:52-55`) and is specified to print no credential. `/json/list`, cookie, and network domains are not that probe. They are session material. This audit did not issue either request.

**Queued, not refused.** `ApprovalTable.md:139-140` rows M-01 and M-02 are `pending`. M-01 is "if still operator-accessible on burner profile," including an optional screenshot. M-02 is "CDP 9222 burner session metadata only." The table header says pending is not a grant (`ApprovalTable.md:5-7`, `:63`). A later agent that treats the table as a work queue still opens the profile. `RecordShape.md:276-277` already parks the untruncated session and the CDP identifiers as not required. M-01/M-02 contradict that park.

**Impact.** Live browser session, cookies, and a profile that the fleet documents as wired to 1Password browser support. Today the attach fails closed (profile ABSENT, zero listeners). The row remains the instruction to try later.

**Smallest remediation.** Rewrite M-01 and M-02 to `refused`, or to "operator pastes a redacted URL list; no agent opens the profile or port 9222." Do not interpolate `9222` into a client. README:6 is provenance prose, not a hop.

### S2 — CLEAN record that contains a token

**Path.** `chousa-shokunin/SKILL.md:50-53` defines `tools/research-gate.sh` as question, rank, hops, claims. Checklist `:43-46` and seed `corpus/QUALITY.md:3-7` have no secrecy item. The lane script is not on disk. A record that satisfies those four checks and also contains a bearer value is CLEAN under the skill sentence alone.

The design script in `ResearchGateDesign.md` is further along, and it is still the wrong scanner. `SECRET_RE` (`:331`) matches `(api_key|password|secret|token|bearer|authorization)[=:]` plus one non-space token. `verify_record` (`:471-472`) uses `grep -qiE` and emits `SECRET_SHAPE` with the fixed text "values not printed". The selftest (`:880`, `:882`) plants a labeled fake assignment and asserts the finding id, not the value. That path does not echo the match.

What that regex misses, and what it false-hits:

- Miss: unlabeled HIT-tier forms from `transcript-scan.sh:83-95` — `op://`, `sk-`, `ghp_`, `eyJ` / `eyJhbG`, PEM `-----BEGIN`, and `Bearer` followed by a space rather than `=` or `:`. A pasted vault ref or JWT with no keyword is CLEAN.
- False-hit: the English words `token` and `authorization` when followed by `:` or `=`. `B:79` is safe (no `=`/`:`) but a note that writes `token: 18282` fires. Do not use this regex as the class list.
- No `SESSION_READ` and no `9222` rule in that file at this read. A peer message said CDP 9222 would be treated as provenance, not a hop. That sentence is not in the file this seat read. If a later edit adds it, re-anchor; do not treat the message as landed.
- `ptr_file_resolves` (`:359-375`) returns success on `[[ -f ]]` for any absolute path (`:371`) and any relative path under `CHOUSA_ROOT` or `LANE_ROOT`, including `..` (`:373`). It does not print file bytes, and the comment says line numbers are not EOF-checked. That is a stat, not a content read. It is still a hop that calls a credential path resolved. A record citing `config.yml` by absolute path is `path-ok`.

`RecordShape.md:152` names `SECRECY_SHAPE` without a class list or a no-echo rule. `RecordShape.md:147` says a resolved hop's `local_evidence` is a `path:line` that **opens**. The design script does not open. Parent must not implement the RecordShape verb.

kagi already measured the scanner-as-exfiltrator bug: a failing check's output is echoed, so a row that prints a value leaks it (`kagi-shokunin/corpus/checklist.tsv:23-25`); the ref-path scan prints counts only because printing the matched line is the leak (`kagi-shokunin/corpus/checklist-run.sh:41-44`). `claim-ledger.sh:84-86` never echoes claim output for the same reason. Keep the design script's quiet grep. Do not "improve" it by printing the match for diagnosis.

**Impact.** Unlabeled secret bytes in a well-formed record stay CLEAN. A diagnostic that prints the `SECRET_RE` match would copy the value the finding exists to catch.

**Smallest remediation.** Replace `SECRET_RE` with the HIT-tier prefix list plus the three header names. On hit, print `path:line class=<name>` only. Never the span, never a hash of the secret bytes (`kagi-shokunin/corpus/drift-pins.sh:21-24`). Refuse absolute paths and `..` before the `-f` test (`SESSION_READ`, file not opened). Selftest plants a fake prefix in a temp file, not a live value.

### S3 — loopback fixture carries a real token, or the client adds one

No fixture bytes exist. Two designs disagree.

**LoopbackFixturePlan, as re-read after its secrecy edit.** One section, not two. Hard rule `:6` and halt line `:26`: static files, bind `127.0.0.1`, no Cookie/Authorization/Set-Cookie, no CDP 9222, no cookie jar, auth literals only as `fx-…`, HIT-tier prefix is a halt. MANIFEST policy `:123-126` matches that. §2.5 `:132-153` is the same rule, plus "SecrecyAudit owns audit" at `:148` — ownership is not a scan. Selftest cases 14–17 are `:347-350` (`HIT_PREFIX_IN_FIXTURE`, `HEADER_LEAK`, `AUTH_LITERAL_NOT_FX_PREFIX`, `CDP_ATTACH_REFUSED`). S4 sketch `:457` is `fx-demo-not-a-secret`, which is not a HIT-tier prefix. The earlier placeholder row and the leaked `PUT` opcodes are **gone** on this re-read. Do not cite them.

What that plan still does not pin: the HIT-prefix scan's output (class only, or the matching line). `serve.sh` at `:399` is `cd "$FX" && python3 -m http.server -b 127.0.0.1`, so the whole fixture tree is published, including a distractor and any file the preflight was supposed to reject. If the scan is skipped, the token is on the wire.

**FixtureSiteDesign, re-read after its pin edit.** Fence table `:77-81` now denies live credential shapes, requires `fx-` for any auth-shaped literal, forbids capture `-H Cookie`, `-H Authorization`, `-b`, `--oauth`, netrc, strips headers before `quote_span`, and forbids CDP 9222 and the burner profile. Selftest rows `:433-437` include `site-no-real-tokens`, `site-no-auth-flags`, `site-strip-headers`, `site-fx-prefix-only`, `site-no-cdp`. That is the right contract.

Residual holes in that same file:

- `:76` still unsets only `http_proxy` and `HTTPS_PROXY`, and only as "may." `HTTP_PROXY`, `https_proxy`, `ALL_PROXY`, `all_proxy` are unset-not. A proxy still forwards the loopback request off-box.
- `:319` still leaves `CHOUSA_CURL` overridable. `:320` says NEVER those flags. A runtime override is not caught by `:434`, which greps the harness scripts, not the env value.
- `:433` `site-no-real-tokens` greps `sk-|ghp_|op://|BEGIN .*PRIVATE` and misses `Bearer `, `github_pat_`, `eyJ`, and a cookie file. `:437` fails if a comment says "never 9222", because it greps the scripts for the port. The test as written punishes the prohibition comment.
- `:462` still says TLS, auth headers, and cookies are omitted because they are this seat's surface. That contradicts `:77-81`. Parent should delete `:462`'s deferral so the fence table is the only rule.
- `account.json` remains (`:111`, `:133`, `:230`). The body in the sketch is a craft interview. The name is how a later edit drops session JSON in.

**Whole-tree serve.** `LoopbackFixturePlan.md:399` is `cd "$FX" && python3 -m http.server -b 127.0.0.1`. That publishes every file under the fixture root. Per-docroot bind (FixtureSiteDesign process model) is the smaller set. Neither is a scan.

**Name footgun.** Capture target `sources/s2-workshop/account.json` (`FixtureSiteDesign.md:111`, `:230`) is a craft-interview body in the sketch, not an account record. Rename to `workshop.json` before land.

**Impact.** Round-2 evidence capture (`operator-demand.md:23`, "evidence capture at every claim") is the durable copy. A header or a cookie jar in that capture is a secret record inside the method corpus. Province text forbids secret values "in any record" (`PROVINCE.md:12-13`) but does not name fixture files or capture logs as records. The gap is that naming.

**Smallest remediation.** Keep `:132-153`. State that `HIT_PREFIX_IN_FIXTURE` prints class + path only. Pin the client: no `-b`, no `Authorization` header, `env -u` for `http_proxy`, `HTTP_PROXY`, `https_proxy`, `HTTPS_PROXY`, `ALL_PROXY`, `all_proxy`. Serve the docroot, not `$FX` (`:399`). Preflight scan refuses to bind if it fired. Rename `account.json`.

### S4 — hop opener prints the secret it was asked to verify

**Path.** Skill `:19` is "follow each hop to the cited artifact," with no denylist. The two precedents are narrower and not the same:

- `claim-ledger.sh` `cite_class` / `cite_target` (`:442-466`) only existence-tests repo-relative classes. It does not print file bytes. It does not open `op.env`. `docs` mode refuses an absolute entries dir (`:839-840`) and reads `Reverify:` lines from markdown. `verify` (`:941-943`) **runs** claim commands. One of those surfaces is `transcript-scan.sh`, whose default DB is the session store (`transcript-scan.sh:4-9`, `:34-35`). The wave admits **docs mode**, not `verify`. Running `verify` is a session-material open attempt. The DB is ABSENT today, so the attempt misses; it is still the wrong mode.
- `anchorcheck.py` `CITE` (`:104`) does **not** match `op.env`, `config.yml`, or an arbitrary absolute path. On OK it prints up to 100 characters of each cited line (`:226-227`, `:261`). Adopting that echo, and widening the regex to match the skill sentence, is the read. `ExportTrustAudit.md` independently flags the same echo (its remediation item 5). This seat agrees: do not copy `:227` into the chousa opener.

**Impact.** A research record that cites `/home/vgpnk/.omp/agent/config.yml:N` is outside anchorcheck's regex, so today's tool would not open it. A gate written from `SKILL.md:19` plus "print the cited line" would. The file is present and mode 600. This audit did not open it, and does not claim its contents.

**Smallest remediation.** Read allowlist checked **before** open: the four research files, `claim-ledger.sh` (source / docs mode only), `anchorcheck.py`, `citation-bases.md`, and chousa lane files. Anything else matching the denylist in §4 is `SESSION_READ` and is not opened. Quotes come only from allowlisted files, and only after the class scan.

### S5 — export chrome copied into the corpus

**Observation.** Full read of A (109 lines), B (100), C (154), README (17). Lines 1–33 of each export are UI chrome: sidebar chat titles, an account display-name at `:28`, workspace labels at `:29` and `:32`. No `op://`, `Bearer `, JWT header, `sk-`, `ghp_`, `AKIA`, PEM, `Cookie:`, `Set-Cookie:`, or `Authorization:` in those four files (sweep in §3). The word `token` at `B:79` is an LLM context-window count (18282→122). The word `authorization` at `C:99` is English ("deployment authorization"). A scanner that matches those English words false-hits the survey corpus.

**Instruction-shaped text.** The user turns (`:34-35`) ask for citations of tradition, papers, and ranks. They do not say to read a credential path, attach to CDP, or print a token. Not followed. Injection census is ExportTrustAudit's seat; this seat only claims the secret-read subset, which is empty in the current bytes.

**Copy path.** `ClaimCapture.md:38` and `:104` (post-update) refuse quoting the preamble and keep it as a path:1-N shape. `RecordShape.md:239` quotes generic chrome strings ("Skip to content", "ChatGPT said:") as observations about export shape. That is not the display-name and not the sidebar titles. Residual risk is a later quote of `:9-26` or `:28` "for completeness" (`QualityBar.md` W10).

**Smallest remediation.** Corpus notes cite `path:line` for chrome. Do not copy the display-name or the sidebar titles into a new record. Research-body quotes start at the answer sections (`A:47`, `B:55`, `C:53` class), which ClaimCapture already used.

### S6 — wrong gate mode and ambient proxy

Covered under S3 and S4. Separate only so the parent does not "prove the precedent" by running `claim-ledger.sh verify` or `transcript-scan.sh` against the live state dir. Docs-mode source read is the admitted surface (`spec.json` contract: claim-ledger.sh docs mode). This seat read the script. It did not run it.

## 3. Negative sweeps (this session)

| Claim | Sweep | Result |
|---|---|---|
| Admitted survey files contain no HIT-tier credential literal | `grep` over `research/` for `op://`, `Bearer `, `eyJ`+10, `sk-`, `ghp_`, `github_pat_`, `AKIA`, `PRIVATE KEY`, `Set-Cookie`, `Authorization:`, `Cookie:`, `api_key=`, `password=`, `token=`, `session_id` | no matches |
| No sidecar secret dump beside the exports | `find research` | exactly README + A + B + C |
| No fixture to carry a token yet | `find chousa-shokunin -type f` excluding `.git` | seed markdown + `.gitkeep` only; no `tools/`, no `fixtures/` |
| Member reports do not embed a long token | class scan of `members/*.md` (12 files at scan time; 13 at a later pass) | hits were class-mentions only: `CorpusMap.md:353` `op://` length 6; `ExportTrustAudit.md:33` `Bearer ` length 9 and `ghp_` length 6; `FixtureSiteDesign.md:77` `op://` length 7 and `Bearer ` length 9. No display-name hit in that scan |
| Port 9222 not listening | `ss -ltnH`, count of local `:9222`, no connect | 0 |
| Named session stores absent | `lstat` only | see §0 |

The class scan does not cover files written after it. `ResearchGateDesign.md` landed later. Its selftest at `:880` plants a synthetic `api_key=` assignment whose tail is a refusal label, not a live credential. This report does not repeat that tail. `FixtureSiteDesign.md:77-81` was rewritten after the scan; the new lines are class names and prohibitions, re-read above, not values.
A later file landing after the scan is **unknown** to that row. This report's own text names the classes and must not be counted as a leak.

## 4. Enforcement points

### 4.1 Exist, and are prose

| Point | What it actually stops | Anchor |
|---|---|---|
| Shape-only, no secret values in a record; custody is kagi | Writing a value into a chousa record, if a human obeys | `SKILL.md:39`; `PROVINCE.md:12-13` |
| Loopback-only without an approval table | External fetch, not a local secret read | `SKILL.md:34-36`; `PROVINCE.md:11-12` |
| Repo-only operating rule | Conflicts with the wave read-set (research/ and sibling gates). Does not name a denylist | `AGENTS.md:3` |
| Q-SEC / W10 | Admission cue, not a gate. QualityBar marks Q-GATE as proposal | `QualityBar.md:65`, `:97`, `:78` |
| Round-2 halt H11 / P9 | Prose halt pointing at this seat | `RoundTwoPlan.md:269`, `:294` |
| Search stop on secret path | Prose stop, no opener | `SearchStrategyTaxonomy.md:206` |
| Approval hard-refusal row for secrets | Says no capture of secret bytes; does not withdraw M-01/M-02 | `ApprovalTable.md:63` |

### 4.2 Exist in fleet code, and chousa must not cargo-cult the open

| Point | Keep | Do not copy |
|---|---|---|
| `claim-ledger.sh:84-86` never echo claim output | print id, reason, exit | — |
| `claim-ledger.sh:164` deny-words include `curl`, `wget`, `ssh`, `op` | a chousa claim row that fetches is POLICY | the janitor/vault verbs as if they were chousa's domain |
| `claim-ledger.sh:839-840` docs path jail | relative dir, no `..` | pointing `--docs` at a secret file; running `verify` |
| `drift-pins.sh:21-24`, `:142-146` | never hash a secret-bearing path; POLICY before read | hashing `config.yml` "to pin it" |
| `transcript-scan.sh:8-9`, `:83-95` | class names and counts-only; HIT vs WARN | opening the live DB; treating WARN words (`token`, `authorization`) as hits |
| `checklist-run.sh:41-44`, `checklist.tsv:23-25` | counts only; echo-on-fail is the leak | a research-gate diagnostic that prints the offending line |
| `anchorcheck.py:104` narrow cite grammar + OUTSIDE-BASE for two roots | do not widen casually | `:226-227` content echo; ORIGIN/MIRROR opens (those trees are ABSENT today; the echo remains) |
| `cdp-bridge-1password.md:52-55` | version probe prints no credential | using that sentence as permission to call `/json` |

### 4.3 Specified this wave, not yet a program

| Point | State at this write | Gap |
|---|---|---|
| `LoopbackFixturePlan.md:6`, `:26`, `:123-126`, `:132-153`, cases `:347-350` | advisory text; one secrecy section; synthetic `fx-` sketch at `:457` | not code; scan output unspecified; whole-tree serve at `:399` |
| `ResearchGateDesign.md:36`, `:331`, `:359-375`, `:471-472` | design script, not landed in the lane; quiet `SECRET_SHAPE`; selftest fake assignment at `:880` | regex misses unlabeled HIT-tier prefixes; absolute path `-f` is path-ok; no `SESSION_READ`; no `9222` rule in the file this seat read |
| `FixtureSiteDesign.md:77-81`, selftest `:433-437` | fence table matches the loopback rule; planted-prefix case exists | proxy unset incomplete (`:76`); `CHOUSA_CURL` still overridable (`:319`) and the flag grep does not see the env; token grep misses `Bearer ` / `eyJ`; `:462` still defers cookies; `account.json` name (`:111`) |
| `RecordShape.md:152` `SECRECY_SHAPE` | schema invariant | no class list, no no-echo rule, hop still "opens" (`:147`) |
| `FindingIds` `SECRET_SHAPED` / `SESSION_READ` | peer message only | `members/FindingIds.md` was **not** on disk when this report was written. Do not treat the message as a landed id |
| `tools/research-gate.sh` | absent | skill contract has no secrecy check |

### 4.4 Proposed denylist (not an admitted rule until parent lands it)

Do not open, and do not follow a hop into:

- `op.env`, any `*.env`, `~/.omp/agent/config.yml`
- `*.db` under a state dir, especially `opencode.db` and its `-wal`/`-shm`
- `the-musketeer/chrome-profile` and any `Cookies` / `Login Data` sibling
- a URL whose port is `9222` or whose path is `/json` or `/json/list`
- `~/.config`, `~/.local/state`, `~/.omp` as roots

Finding id, if FindingIds lands the spelling: `SESSION_READ`. Print the class and the path **shape**, not file bytes. `SECRET_SHAPED` / `HIT_PREFIX_IN_FIXTURE` print `path:line` + class name drawn from `transcript-scan.sh:83-95` (HIT tier) plus the three header names. Do not match the English words `token` or `authorization`. Synthetic fixture literals must match `^fx-[a-z0-9-]{8,}$` and are not HIT-tier.

## 5. Rejections kept

| Rejected reading | Reason |
|---|---|
| "The survey files are safe to quote in full" | Lines 1–33 are session inventory. Quote the research body, or cite the line without copying the label |
| "anchorcheck is a safe secret hop-follower" | Its regex misses secret paths, which is containment, but it echoes 100 characters of whatever it does accept. The skill sentence is wider than the regex |
| "A placeholder string proves the fixture is clean" | Withdrawn as a description of the current LoopbackFixturePlan (the placeholder row is gone). Still true of FixtureSiteDesign's `TOKEN_SHAPE_FORBIDDEN` word: presence of a forbidden-word comment is not a negative scan |
| "M-01/M-02 are safe because they say metadata only" | The access method is the burner profile and CDP. Metadata-only is not enforceable once the debugger socket is open. Pending is not a grant, and it is still a queue |
| "Running claim-ledger docs mode proves kagi, so verify is the same evidence" | `verify` executes claims. Docs mode reads markdown `Reverify:` lines. The wave named docs mode |
| "config.yml holds a live token" as a finding of **this** audit | File is present, mode 600, unread. Prior reports are not re-verified here |

## 6. Unknowns

- Whether a later edit of `ResearchGateDesign.md` adds the CDP-provenance sentence from the peer message. Not in the file at this read.
- Whether `FindingIds.md` lands `SECRET_SHAPED` / `SESSION_READ` after this write. Not on disk at the earlier check.
- Contents of `config.yml`. Intentionally unknown.
- Whether a burner profile or a listener on 9222 appears after this `lstat` / `ss`. This report's shape rows are as-of this session, not a standing guarantee.
- Member files written after the class scan. The scan's "no long literal" claim does not cover files that did not exist yet.

## 7. What parent should land (smallest set)

1. Refuse or rewrite ApprovalTable M-01 and M-02. No agent opens the profile or port 9222.
2. Before landing `tools/research-gate.sh`, replace `ResearchGateDesign.md:331` with the HIT-tier prefix list plus header names; print `path:line class=` only; refuse absolute paths and `..` before `-f` (`SESSION_READ`). Do not implement `RecordShape.md:147` "opens".
3. Keep LoopbackFixturePlan `:132-153` and FixtureSiteDesign `:77-81`. Delete the deferral at FixtureSiteDesign `:462`. Pin curl argv (ignore or refuse a `CHOUSA_CURL` that adds `-b` or `Authorization`) and unset all proxy variables, not only `:76`. Change LoopbackFixturePlan `:399` to a docroot serve. Rename `account.json`. Widen `:433` to the HIT-tier list; do not fail `:437` on a prohibition comment.
4. Survey read allowlist = the four research files + the three named precedent files (source / docs mode) + the chousa lane. README:6 is not a hop. Do not run `claim-ledger.sh verify` as survey evidence.
5. Do not copy export `:9-26` or `:28` into corpus notes.

No process was left running. No fixture server was started. No credential file was read.
