# HostScout — round-15 fact sheet: checklist rows for the named host surfaces

Scope: row candidates for `corpus/checklist-run.sh` / `corpus/checklist.tsv` (operability 8 → 9).
Every command below was **executed today (2026-09-28)** as `bash -c '<cmd>'` with cwd = repo root
(the gate's own invocation shape), then its exit code and last non-empty stdout line were captured.
Expectations were additionally **mutation-tested** on `/tmp` copies to prove the ERE cannot
half-match. No secret surface was read: no `op` exec, no vault read, no `op.env` bytes, no
handler start/stop, no handler/vault commands, no `claim-ledger.sh` invocation.

Host: `vgpnk`, python3 3.x, pyyaml **6.0.3** (present), jq-1.8.2, `ss` (iproute2),
bash 5.3.15. Handler is **stopped** today (`pgrep -af 'opencode serve'` ⇒ none;
`tmux ls` ⇒ only `ufo_sighting`; `~/.local/state/the-janitor/session-id` ⇒ absent).

Tooling note that matters for the gate: in the omp tool shell `type jq` / `type timeout` report
"shell builtin", but inside a real `bash -c` (what the gate uses) they resolve to
`/usr/bin/jq` and `/usr/bin/timeout` — verified with `bash -c 'type jq; jq --version'` ⇒
`jq is /usr/bin/jq` / `jq-1.8.2`, and `env -i /bin/bash -c 'command -v jq'` ⇒ `/usr/bin/jq`.
So the commands below are portable to the gate.

---

## 0. Falsification warning that changes the design (read first)

`ss` **without** `-l`/`-a` does **not** list LISTEN sockets. Measured with a scratch loopback
listener on 40996:

```
ss -Htn  '( sport = :40996 or dport = :40996 )'   ⇒ (empty, rc=0)
ss -Htnl '( sport = :40996 or dport = :40996 )'   ⇒ LISTEN 0 5 127.0.0.1:40996 0.0.0.0:*
ss -Htna '( sport = :40996 or dport = :40996 )'   ⇒ LISTEN 0 5 127.0.0.1:40996 0.0.0.0:*
```

⇒ a port row written with `ss -Htn` is **false-CLEAN whenever the handler is up**. The row below
uses `ss -Htna`.

---

## 1. Row candidates (validated)

### (a) `ov-assert` — overlay JSON assertions (`share`, `autoupdate`, `enabled_providers`, `default_agent`, baseURL)

```
cmd:           jq -er '. as $c | if ($c.share=="disabled" and $c.autoupdate==false and $c.enabled_providers==["qwen-local"] and $c.default_agent=="janitor" and $c.provider["qwen-local"].options.baseURL=="http://127.0.0.1:8080/v1") then "OVERLAY_OK" else error("overlay drift") end' "$HOME/.config/the-janitor/opencode.json"
expect_exit:   0
expect_lastline: ^OVERLAY_OK$
observed today: rc=0  last=OVERLAY_OK
mutation proof: /tmp copy with .share="enabled" ⇒ rc=5, last non-empty line "jq: error (at /tmp/mut-overlay.json:29): overlay drift" ⇒ ERE_NOMATCH (defect surfaces, exit != 0)
safe: yes
```
`jq -e` makes the non-`true`/`null` outcome exit 5, so a drifted overlay yields `ITEM-FAIL ov-assert`.
One jq invocation covers all five assertions atomically (no partial-pass prose).

### (a2) `ov-model` — the overlay model id matches the agent's model (cross-surface consistency, cheap)

```
cmd:           jq -er '.model' "$HOME/.config/the-janitor/opencode.json"
expect_exit:   0
expect_lastline: ^qwen-local/Qwen3-Coder-30B-A3B-Instruct-UD-IQ2_XXS$
observed today: rc=0  last=qwen-local/Qwen3-Coder-30B-A3B-Instruct-UD-IQ2_XXS
safe: yes
```

### (b) `agent-perm` — permission map parsed from front-matter, cannot half-match

pyyaml presence checked first: `python3 -c "import yaml; print(yaml.__version__)"` ⇒ `6.0.3`.
The parse is total-line: whole front-matter block → YAML → JSON of the `permission` mapping only,
compared against a fully anchored ERE.

```
cmd:           python3 -c 'import re,json,sys,yaml;t=open(sys.argv[1]).read();d=yaml.safe_load(re.match(r"---\n(.*?)\n---",t,re.S).group(1));print(json.dumps(d["permission"],sort_keys=True))' "$HOME/.config/opencode/agents/janitor.md"
expect_exit:   0
expect_lastline: ^\{"\*": "deny", "janitor_auth": "allow"\}$
observed today: rc=0  last={"*": "deny", "janitor_auth": "allow"}
mutation proof: /tmp copy with an added `bash: allow` line ⇒ last={"*": "deny", "bash": "allow", "janitor_auth": "allow"} ⇒ ERE_NOMATCH
anchoring proof: an unanchored ERE (`deny`) matches 1/1 against `{"*": "deny", "janitor_auth": "allow", "extra": "allow"}` ⇒ a loose pattern WOULD half-match; the `^…$` ERE is required.
safe: yes
```
Notes for the gate: `re.match` is front-matter anchored at offset 0; if pyyaml were ever missing the
row exits non-zero with an ImportError traceback (fails loudly, never false-CLEAN). `$HOME` is
expanded by `bash -c`, the python is single-quoted so nothing inside needs escaping.

### (b2) `agent-identity` — `name`/`mode`/`steps` (the `steps: 4` budget named in the checklist)

```
cmd:           python3 -c 'import re,json,sys,yaml;t=open(sys.argv[1]).read();d=yaml.safe_load(re.match(r"---\n(.*?)\n---",t,re.S).group(1));print(json.dumps({k:d[k] for k in ("name","mode","steps")},sort_keys=True))' "$HOME/.config/opencode/agents/janitor.md"
expect_exit:   0
expect_lastline: ^\{"mode": "primary", "name": "janitor", "steps": 4\}$
observed today: rc=0  last={"mode": "primary", "name": "janitor", "steps": 4}
safe: yes
```

### (c) `handoff-boundaries` — `credentials_in_evidence == false`, `target_authority_conferred == false`, presence of `access_receipt` + `receipt_sha256`, **types only**

```
cmd:           jq -er '. as $r | if ($r.boundaries.credentials_in_evidence==false and $r.boundaries.target_authority_conferred==false and $r.access_receipt!=null and $r.receipt_sha256!=null) then "credentials_in_evidence=\($r.boundaries.credentials_in_evidence|type):\($r.boundaries.credentials_in_evidence) target_authority_conferred=\($r.boundaries.target_authority_conferred|type):\($r.boundaries.target_authority_conferred) access_receipt=\($r.access_receipt|type) receipt_sha256=\($r.receipt_sha256|type)" else error("BOUNDARY-FAIL") end' "$HOME/.local/state/tac/handoff-status.json"
expect_exit:   0
expect_lastline: ^credentials_in_evidence=boolean:false target_authority_conferred=boolean:false access_receipt=string receipt_sha256=string$
observed today: rc=0  last=credentials_in_evidence=boolean:false target_authority_conferred=boolean:false access_receipt=string receipt_sha256=string
mutation proof: /tmp copy with .boundaries.credentials_in_evidence=true ⇒ rc=5, "jq: error (at /tmp/mut-handoff.json:54): BOUNDARY-FAIL" ⇒ ERE_NOMATCH
safe: yes — prints only two booleans and the TYPE of the two opaque keys; the receipt/sha values are never rendered (measured lengths 54 / 64 exist but are deliberately not part of the verdict line).
```
Supporting measurement (types only, no values): top-level keys `schema_version,recorded_at,access_receipt,receipt_sha256,janitor_custody,commands,verification,janitor_provenance,future_l1_context_files,current_l1_relay,runner_capacity,boundaries,quiet_operation,temporary_smoke_files_removed`;
`boundaries` keys/types: `tac_status=string model_access=string safeguards_removed=boolean credentials_in_evidence=boolean target_authority_conferred=boolean`.

### (d) `port-40961` — no listener / no established socket, tolerant of the expected handler-up state

```
cmd:           ss -Htna '( sport = :40961 or dport = :40961 )' | awk 'BEGIN{n=0;bad=0} {n++; if ($4 !~ /^127\.0\.0\.1:/) bad++} END{printf "PORT_40961: %s sockets=%d non_loopback=%d\n", (n==0?"SILENT":(bad?"EXTERNAL":"LOOPBACK_ONLY")), n, bad}'
expect_exit:   0
expect_lastline: ^PORT_40961: (SILENT|LOOPBACK_ONLY) sockets=[0-9]+ non_loopback=0$
observed today: rc=0  last=PORT_40961: SILENT sockets=0 non_loopback=0   (raw `ss -Htna …` ⇒ 0 lines)
safe: yes — kernel socket table only; never connects, never probes the service.
```
**What the verdict means when the handler IS up** (measured, not inferred):
`~/.local/bin/the-janitor:225` is `exec opencode serve --hostname 127.0.0.1 --port "$PORT"`, and
`PORT="${THE_JANITOR_PORT:-40961}"` (L15) — so the handler binds **loopback only**. With a live
listener the same command prints `PORT_40961: LOOPBACK_ONLY sockets=1 non_loopback=0`, which the
ERE still accepts ⇒ PASS. Only a non-loopback local address produces `EXTERNAL` (`non_loopback>=1`),
which the ERE rejects ⇒ `ITEM-FAIL port-40961`: that is the real hygiene defect (handler exposed
beyond loopback), not "handler is running".
Both non-SILENT branches were proven on scratch ports (not 40961):
loopback listener 40995 ⇒ `PORT_40961: LOOPBACK_ONLY sockets=1 non_loopback=0` (ERE match);
`0.0.0.0` listener 40994 ⇒ `PORT_40961: EXTERNAL sockets=1 non_loopback=1` (ERE no-match).
ERE behaviour on the three literal verdict lines: SILENT ⇒ MATCH, LOOPBACK_ONLY ⇒ MATCH,
EXTERNAL ⇒ NOMATCH.

### (e) `env-password-absent` — `OPENCODE_SERVER_PASSWORD` is not set by handler or client

```
cmd:           c=$(grep -ho OPENCODE_SERVER_PASSWORD "$HOME/.local/bin/the-janitor" "$HOME/.config/the-janitor/client.py" | wc -l); test "$c" -eq 0 && echo "ENV_OPENCODE_SERVER_PASSWORD: absent count=$c"
expect_exit:   0
expect_lastline: ^ENV_OPENCODE_SERVER_PASSWORD: absent count=0$
observed today: rc=0  last=ENV_OPENCODE_SERVER_PASSWORD: absent count=0   (0 occurrences in both files)
safe: yes — reads two source files (code, no secret material); never touches `op.env`.
```
Corroboration: `_serve` (L220–225) exports only `OPENCODE_CONFIG`, `XDG_DATA_HOME`,
`XDG_CACHE_HOME`, `XDG_STATE_HOME` before `exec opencode serve …`; the request path (L73, L133)
passes only `THE_JANITOR_PORT` + `THE_JANITOR_STATE_DIR` to `client.py`. `printenv OPENCODE_SERVER_PASSWORD` today ⇒ rc=1 (unset), but that reflects the *runner's* shell, not the
handler's — keep the source-occurrence count as the verdict and treat `printenv` as commentary.
**Un-mechanisable half:** SKILL.md L444–447 also says the var must not be enabled. Whether it is
set *inside the live serve process* cannot be observed while stopped, and grepping
`$CONFIG_DIR/op.env` for the name is forbidden by the row constraints ⇒ that residual is by-hand.

### (f) `lock-location` — flock present in `the-janitor`, absent from `client.py`

```
cmd:           a=$(grep -c flock "$HOME/.local/bin/the-janitor" || true); b=$(grep -c flock "$HOME/.config/the-janitor/client.py" || true); test "$a" -gt 0 -a "$b" -eq 0 && echo "LOCK_LOCATION: the-janitor_flock=$a client.py_flock=$b"
expect_exit:   0
expect_lastline: ^LOCK_LOCATION: the-janitor_flock=[1-9][0-9]* client.py_flock=0$
observed today: rc=0  last=LOCK_LOCATION: the-janitor_flock=4 client.py_flock=0
safe: yes
```
Measured detail: `grep -n flock ~/.local/bin/the-janitor` ⇒ L63 `need_command flock`, L131 `flock 9`,
L140 `flock 9`, L176 `flock 9`; `LOCK_FILE="$STATE_DIR/client.lock"` is L12 (created L66–69,
`exec 9>"$LOCK_FILE"` at L130/139/175). `grep -nic lock ~/.config/the-janitor/client.py` ⇒ **0**
(also `grep -n 'lockfile\|flock\|Lock' client.py | wc -l` ⇒ 0).

### (g) `op-env-present` — the env-ref file exists with 0600, bytes never read

```
cmd:           test -f "$HOME/.config/the-janitor/op.env" && echo "OP_ENV: present mode=$(stat -c %a "$HOME/.config/the-janitor/op.env")"
expect_exit:   0
expect_lastline: ^OP_ENV: present mode=600$
observed today: rc=0  last=OP_ENV: present mode=600   (stat: `op.env mode=600 owner=vgpnk`)
safe: yes — path existence + mode byte only via `stat`; **no read of its contents** (that is why the
`OPENCODE_SERVER_PASSWORD`-in-`op.env` sub-check stays by-hand).
```

---

## 2. TSV-ready rows (fields separated by TAB: id, class, cmd, expect_exit, expect_lastline, note)

```tsv
ov-assert	runnable	jq -er '. as $c | if ($c.share=="disabled" and $c.autoupdate==false and $c.enabled_providers==["qwen-local"] and $c.default_agent=="janitor" and $c.provider["qwen-local"].options.baseURL=="http://127.0.0.1:8080/v1") then "OVERLAY_OK" else error("overlay drift") end' "$HOME/.config/the-janitor/opencode.json"	0	^OVERLAY_OK$	overlay asserts share/autoupdate/enabled_providers/default_agent/baseURL in one jq -e
ov-model	runnable	jq -er '.model' "$HOME/.config/the-janitor/opencode.json"	0	^qwen-local/Qwen3-Coder-30B-A3B-Instruct-UD-IQ2_XXS$	overlay model id unchanged and matches the agent front-matter
agent-perm	runnable	python3 -c 'import re,json,sys,yaml;t=open(sys.argv[1]).read();d=yaml.safe_load(re.match(r"---\n(.*?)\n---",t,re.S).group(1));print(json.dumps(d["permission"],sort_keys=True))' "$HOME/.config/opencode/agents/janitor.md"	0	^\{"\*": "deny", "janitor_auth": "allow"\}$	whole-front-matter YAML parse; anchored ERE cannot half-match (mutated copy fails)
agent-identity	runnable	python3 -c 'import re,json,sys,yaml;t=open(sys.argv[1]).read();d=yaml.safe_load(re.match(r"---\n(.*?)\n---",t,re.S).group(1));print(json.dumps({k:d[k] for k in ("name","mode","steps")},sort_keys=True))' "$HOME/.config/opencode/agents/janitor.md"	0	^\{"mode": "primary", "name": "janitor", "steps": 4\}$	agent name/mode/steps budget parsed, not grepped
handoff-boundaries	runnable	jq -er '. as $r | if ($r.boundaries.credentials_in_evidence==false and $r.boundaries.target_authority_conferred==false and $r.access_receipt!=null and $r.receipt_sha256!=null) then "credentials_in_evidence=\($r.boundaries.credentials_in_evidence|type):\($r.boundaries.credentials_in_evidence) target_authority_conferred=\($r.boundaries.target_authority_conferred|type):\($r.boundaries.target_authority_conferred) access_receipt=\($r.access_receipt|type) receipt_sha256=\($r.receipt_sha256|type)" else error("BOUNDARY-FAIL") end' "$HOME/.local/state/tac/handoff-status.json"	0	^credentials_in_evidence=boolean:false target_authority_conferred=boolean:false access_receipt=string receipt_sha256=string$	booleans + types only; receipt values never rendered
port-40961	runnable	ss -Htna '( sport = :40961 or dport = :40961 )' | awk 'BEGIN{n=0;bad=0} {n++; if ($4 !~ /^127\.0\.0\.1:/) bad++} END{printf "PORT_40961: %s sockets=%d non_loopback=%d\n", (n==0?"SILENT":(bad?"EXTERNAL":"LOOPBACK_ONLY")), n, bad}'	0	^PORT_40961: (SILENT|LOOPBACK_ONLY) sockets=[0-9]+ non_loopback=0$	-a required: ss without -l/-a hides LISTEN; loopback bind (the-janitor L225) passes, non-loopback fails
env-password-absent	runnable	c=$(grep -ho OPENCODE_SERVER_PASSWORD "$HOME/.local/bin/the-janitor" "$HOME/.config/the-janitor/client.py" | wc -l); test "$c" -eq 0 && echo "ENV_OPENCODE_SERVER_PASSWORD: absent count=$c"	0	^ENV_OPENCODE_SERVER_PASSWORD: absent count=0$	source-occurrence count; op.env never read (that residual is by-hand)
lock-location	runnable	a=$(grep -c flock "$HOME/.local/bin/the-janitor" || true); b=$(grep -c flock "$HOME/.config/the-janitor/client.py" || true); test "$a" -gt 0 -a "$b" -eq 0 && echo "LOCK_LOCATION: the-janitor_flock=$a client.py_flock=$b"	0	^LOCK_LOCATION: the-janitor_flock=[1-9][0-9]* client.py_flock=0$	flock lives in the CLI (L63/131/140/176), absent from client.py (0)
op-env-present	runnable	test -f "$HOME/.config/the-janitor/op.env" && echo "OP_ENV: present mode=$(stat -c %a "$HOME/.config/the-janitor/op.env")"	0	^OP_ENV: present mode=600$	existence + mode only; bytes never read
```

---

## 3. Mapping the 16 items to classes (Evidence production 8 @ SKILL.md L422–429; Handler operation 8 @ L432–437, L440, L444)

Count verified by executing:
`awk 'NR>=419 && /^## /&&NR>419{exit} NR>=420 && /^- \[ \]/{c++} END{print c}' SKILL.md` ⇒ **16**
(§ heading `## Credential-hygiene checklist` at L419; subsections `Evidence production:` L421 and
`Handler operation:` L431; last item at L444.)

| item line | substance | class | row |
|---|---|---|---|
| L422 | record mechanism/metadata; run `surface-census.sh` first, then `drift-pins.sh` | runnable | existing gates (`SURFACE_CENSUS: CLEAN…`, `DRIFT_PINS: CLEAN…`) — both exit 0 today |
| L423 | after host-file change run `--pin` once, report REPIN/MOVED | by-hand (`manual-change`) | — |
| L424 | quote only metadata-only output | by-hand (`operator-scope`) | — |
| L425 | `refs` output: key names OK, ref paths out of artifacts | by-hand (`operator-scope`) | — |
| L426 | run `op-ref-probe.sh`; per-file `op run … printenv KEY` divergence | runnable (gate) + residual by-hand | `OP_REF_PROBE: CLEAN (checks=44 oprun=12 refs=7 divergent=5 edge=10 sig=6)` exit 0 |
| L427 | never paste `the-janitor run` output | by-hand (`operator-scope`) | — |
| L428 | receipts bind bytes; state scope explicitly | by-hand (`authoring-duty`) | — |
| L429 | `handoff-status.json` `boundaries` vocabulary | runnable | `handoff-boundaries` |
| L432 | one request at a time — `client.lock` flock serializes | runnable | `lock-location` (queueing discipline itself = by-hand `operator-scope`) |
| L433 | after `stop`, next request is `AUTH_REQUIRED` until re-approval | by-hand (`runtime-behavior`) | needs a live handler + operator approval |
| L434 | keep `config_overlay` intact | runnable | `ov-assert` (+ `ov-model`) |
| L435 | never widen janitor permissions | runnable | `agent-perm` (+ `agent-identity`) |
| L436 | CDP 9222 / musketeer profile is cross-fleet | by-hand (`cross-lane`) | — |
| L437–439 | never put secret-adjacent text into a request | by-hand (`operator-scope`) | — |
| L440–443 | run `transcript-scan.sh` (exit 1 by design) | runnable | existing gate; verdict text measured: `TRANSCRIPT_SCAN: %s (cells=%d patterns=%d+%d warns=%d schema-absent=%d) db=%s` where `%s` ∈ {`CLEAN`, `HITS=<n>`} ⇒ row `expect_exit 0\|1`, `expect_lastline ^TRANSCRIPT_SCAN: (CLEAN\|HITS=[0-9]+) \(cells=…` (pin the tail shape against L278–280 before landing) |
| L444–447 | treat `127.0.0.1:40961` as unauthenticated; no local POST; don't enable `OPENCODE_SERVER_PASSWORD` | runnable | `port-40961` + `env-password-absent`; the in-process-env residual is by-hand (`runtime-behavior`) |

By-hand reason-classes used: `manual-change` (L423), `operator-scope` (L424, L425, L427, L432-discipline, L437–439), `authoring-duty` (L428), `runtime-behavior` (L433, L444-env residual), `cross-lane` (L436) — each needs a unique ≥24-char reason note in the `note` column. If the gate wants a single runnable count from the 16, the ceiling is **9–10 runnable / 6–7 by-hand** (the honest, un-inflated split; the three existing gates cover L422, L426, L440).

---

## 4. DEFECT — stale lock attribution (confirmed, both sides)

`client.py` contains **no** lock code; the flock lives in the CLI.

```
grep -nic lock ~/.config/the-janitor/client.py            ⇒ 0
grep -n 'LOCK_FILE\|flock' ~/.local/bin/the-janitor       ⇒ L12 LOCK_FILE="$STATE_DIR/client.lock"
                                                              L63 need_command flock
                                                              L66-69 create + chmod 600
                                                              L130/131, L139/140, L175/176 exec 9>"$LOCK_FILE"; flock 9
```

Stale text:

- `PROVINCE.md:12` —
  `- \`~/.config/the-janitor/client.py\` (755, 117 lines) — HTTP client, lock, session-id, \`THE_JANITOR_REQUEST_TIMEOUT\``
  (line 12, "Evidence production" surface list; the word `lock` is the false half)
- `corpus/surface-census.tsv:22` (tab-separated row, note = field 5) —
  `$HOME/.config/the-janitor/client.py⇥asset⇥exec⇥755⇥HTTP client: lock, session-id, request timeout`

Internal inconsistency in the same file: `PROVINCE.md:24` records
`~/.local/state/the-janitor/{client.lock,session-id}` (600) as the state-side artifacts, so
PROVINCE.md claims the lock on both `client.py` and the `the-janitor` state dir while the evidence
says only the latter + the CLI are involved.

Related stale count (already flagged by the round brief, re-measured here):
`SCORECARD.md:16` says "a **15-item** hygiene checklist"; the checklist has **16** `- [ ]` items
(8 + 8) — see §3.

### Adjacent hits — NOT defects (do not "fix" these)
- `corpus/knowledge/handler-trust-boundary.md:5` — `lock sites L130/139/175; ~/.config/the-janitor/client.py (sha256 8179b241…ce51, 117 lines) L22–38, L41–95` — the lock sites are attributed to
  `the-janitor` (correct: L130/139/175); `client.py` is cited for L22–38/L41–95 only ⇒ correct.
- `corpus/README.md:30` — row "Session-id / lock lifecycle…" whose source column is
  `the-janitor L128–249 …, client.py L41–95, janitor_auth.ts`. Ambiguous, not a clean false
  attribution; flag to L1 but do not edit blind.

### Shape of the fix (L1 owns the edit)
Draft replacement note for `corpus/surface-census.tsv:22`:
`HTTP client: session-id, request timeout (no lock — flock lives in the-janitor L130/139/175)`.
Draft for `PROVINCE.md:12`: `— HTTP client (session-id, \`THE_JANITOR_REQUEST_TIMEOUT\`); the lock is
not here (flock in \`the-janitor\` L130/139/175)`. Both are ≥24 chars and keep the row's kind/mode
fields untouched, so `surface-census.sh` / `drift-pins.sh` stay green.
Note the round-14 caveat: do not `--pin` in the same round that discovers the drift — this is a
note-field-only change, so the pins should not move; if `drift-pins.sh` complains, re-read it before
touching pins.

---

## 5. Gaps / unknowns

- ~~**gate absent at time of writing** — `corpus/checklist-run.sh` / `corpus/checklist.tsv` do not
  exist yet; none of the above was run *through* the gate, only as `bash -c` with the gate's cwd and
  shape.~~ **SUPERSEDED — the gate landed; all 9 runnable rows were re-verified through it, see §7.**
- in-process env of the live handler (`OPENCODE_SERVER_PASSWORD` inside the serve PID) — unobservable
  while stopped and `op.env` is out of bounds ⇒ stays by-hand.
- `op.env` key inventory — intentionally untouched (bytes are out of bounds); `op-ref-probe.sh`
  already owns that contract.
- Are `journals`/`harness` (`ss` socket count on 40961 while a request is in flight) worth a
  `runtime-behavior` by-hand note? Unknown; needs a live handler.

## 6. Smoke proof — the §2 TSV block executed end-to-end

Throwaway runner (in `/tmp`, deleted after; nothing written into the repo): the `tsv` block was
extracted with `awk '/^```tsv$/{f=1;next} /^```$/{if(f){exit}} f'`, then every row was executed as
`bash -c "$cmd"` with cwd = repo root and its last non-empty stdout line matched against field 5:

```
rows=9, fields-per-row = 6 for all 9 (id,class,cmd,expect_exit,expect_lastline,note)
ov-assert             rc=0/0 ere=yes  last=OVERLAY_OK
ov-model              rc=0/0 ere=yes  last=qwen-local/Qwen3-Coder-30B-A3B-Instruct-UD-IQ2_XXS
agent-perm            rc=0/0 ere=yes  last={"*": "deny", "janitor_auth": "allow"}
agent-identity        rc=0/0 ere=yes  last={"mode": "primary", "name": "janitor", "steps": 4}
handoff-boundaries    rc=0/0 ere=yes  last=credentials_in_evidence=boolean:false target_authority_conferred=boolean:false access_receipt=string receipt_sha256=string
port-40961            rc=0/0 ere=yes  last=PORT_40961: SILENT sockets=0 non_loopback=0
env-password-absent   rc=0/0 ere=yes  last=ENV_OPENCODE_SERVER_PASSWORD: absent count=0
lock-location         rc=0/0 ere=yes  last=LOCK_LOCATION: the-janitor_flock=4 client.py_flock=0
op-env-present        rc=0/0 ere=yes  last=OP_ENV: present mode=600
ALL_ROWS_OK=yes
```

So all 9 row candidates are CLEAN today with zero `ITEM-FAIL`, and the block is directly
paste-able into `corpus/checklist.tsv` (tab-separated, 6 fields, no embedded tabs/newlines).

## 7. Gate landed — verification of the shipped rows (round-15 re-run, 2026-09-28)

`corpus/checklist-run.sh` + `corpus/checklist.tsv` now exist (8 cols: id class lead check
expect_exit expect_last reason note). I re-ran **every runnable row's own `check` string** through
`bash -c` and matched its last non-blank stdout line against its own `expect_last`:

```
E1 rc=0 expect=0 ere=yes :: DRIFT_PINS: CLEAN (files=15 symbols=20)
E4 rc=0 expect=0 ere=yes :: REF_PATH_SCAN: hits=0
E5 rc=0 expect=0 ere=yes :: OP_REF_PROBE: CLEAN (checks=44 oprun=12 refs=7 divergent=5 edge=10 sig=6)
E8 rc=0 expect=0 ere=yes :: HANDOFF_STATUS: OK (boundaries=5 receipt=present sha=present)
H1 rc=0 expect=0 ere=yes :: CLIENT_LOCK: flock=3 declared=1 mode=600
H3 rc=0 expect=0 ere=yes :: CONFIG_OVERLAY: OK (providers=1 share=disabled autoupdate=False global=parsed global_providers=absent)
H4 rc=0 expect=0 ere=yes :: JANITOR_PERMS: OK (entries=2 steps=4)
H7 rc=1 expect=0|1 ere=yes :: TRANSCRIPT_SCAN: HITS=2 (cells=888 patterns=32+5 warns=2 schema-absent=0) db=…/opencode.db
H8 rc=0 expect=0 ere=yes :: CONTROL_PLANE: password_refs=0 listeners=0 established=0
```

Gate: `bash corpus/checklist-run.sh` ⇒ `CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7` +
`CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0)` exit 0 in **2.2 s** (E5's ~25 s
estimate is not today's cost); `--list` ⇒ `CHECKLIST_LIST: rows=16 runnable=9 by_hand=7`;
`--only <id>` clean for all 9 ids. So my §3 ceiling (9–10 runnable) matched the shipped 9/7 split.

Re-checked at 22:45:58 after L1's 22:45:04 edit to `checklist-run.sh`, the ratio line gained a
delegation split — `CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7 delegated=3 direct=6` +
`CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0)` rc=0. `delegated=3` matches the §3
mapping exactly: E1 (census + drift-pins chain), E5 (`op-ref-probe.sh`) and H7
(`transcript-scan.sh`) are the three rows that hand off to pre-existing gates; the other six build
their verdict inline.

Fallout from §0 that does **not** apply to the shipped H8: H8 uses `ss -ltnH` — the explicit `-l` is
exactly the fix for the bare-`ss -t` blind spot I flagged, so H8's listener arm is mechanically
sound. Proven with two sockets held open in one process: a `0.0.0.0:40988` listener and a
`127.0.0.1:40987` listener each appear in `ss -ltnH`, and H8's `$4`-selection counts both
(`L_wild=1 L_loop=1`). (`/proc/net/tcp` in this sandbox showed neither; `ss` is the authoritative
view here. My earlier scratch-port confusion was a tool-shell backgrounding artifact: those
`0.0.0.0` servers never reached `listen()`.)

### 7a. REAL GAP in row H8: it could not see the bind scope — **CLOSED 22:41 (L1 landed the arm; see §7d)**

> Update: the shipped H8 check now carries the `NL=$(ss -ltnH … $4 !~ /^127\.0\.0\.1:/ …)` term and
> `test "$NL" -eq 0`, i.e. exactly the patch below; the row prints
> `CONTROL_PLANE: password_refs=0 listeners=0 non_loopback=0 established=0` rc=0 and the full gate is
> CLEAN. The branch proof below is still the evidence that the new arm has teeth.

**Pre-fix H8 arm and the patch that landed (detail):**
The shipped verdict line was
`CONTROL_PLANE: password_refs=%s listeners=%s established=%s`
with `test "$pw" -eq 0 && test "$E" -eq 0`, and the ERE
`^CONTROL_PLANE: password_refs=0 listeners=[0-9]+ established=0$`.

⇒ any `listeners` count passes. If the handler were ever bound to a **non-loopback** address
(`0.0.0.0:40961` / a tailnet IP — today it is not: the-janitor:225 is
`exec opencode serve --hostname 127.0.0.1 --port "$PORT"`), H8 stays **green** while the item it
represents ("treat 127.0.0.1:40961 as unauthenticated handler access") is exactly the containment
being breached. Measured on scratch sockets with the shipped awk shape: a wildcard bind prints
`CONTROL_PLANE: password_refs=0 listeners=1 established=0` ⇒ **PASS**.

Draft patch (same single `ss` call, one extra `awk` term, no new row, keeps `LISTEN_COUNT` semantics):

```
NL=$(ss -ltnH 2>/dev/null | awk '$4 ~ /:40961$/ && $4 !~ /^127\.0\.0\.1:/ {n++} END{print n+0}'); \
printf 'CONTROL_PLANE: password_refs=%s listeners=%s non_loopback=%s established=%s\n' "$pw" "$L" "$NL" "$E"; \
test "$pw" -eq 0 && test "$E" -eq 0 && test "$NL" -eq 0
```

expected last line: `^CONTROL_PLANE: password_refs=0 listeners=[0-9]+ non_loopback=0 established=0$`

Branch proof (sockets held in one process, three ports, same awk as above):

```
wildcard bind (0.0.0.0)  :: CONTROL_PLANE: password_refs=0 listeners=1 non_loopback=1 established=0 :: FAIL (desired)
loopback bind            :: CONTROL_PLANE: password_refs=0 listeners=1 non_loopback=0 established=0 :: PASS
host 40961 today         :: CONTROL_PLANE: password_refs=0 listeners=0 non_loopback=0 established=0 :: PASS
shipped-H8 arm on the wildcard bind :: CONTROL_PLANE: password_refs=0 listeners=1 established=0 :: PASS  <-- the gap
```

Alternative if L1 prefers no new token: pin `listeners=0` (today's state) — but then the row breaks
whenever the handler legitimately runs, which contradicts the row's own note ("a listener is
legitimate while the handler runs"). The `non_loopback` arm is the state-tolerant form.

### 7b. The stale-lock defect (§4) — **CLOSED 22:37:50 / 22:37:58 (fixed by L1; verified at 22:42)**

Historical (pre-fix) reading at 22:36, unchanged at 22:39:

```
sed -n '12p' PROVINCE.md   ⇒ - `~/.config/the-janitor/client.py` (755, 117 lines) — HTTP client, lock, session-id, `THE_JANITOR_REQUEST_TIMEOUT`
sed -n '22p' corpus/surface-census.tsv ⇒ $HOME/.config/the-janitor/client.py<TAB>asset<TAB>exec<TAB>755<TAB>HTTP client: lock, session-id, request timeout
```

Current text after L1's edit (both carry the correction and the falsifier):

```
sed -n '12p' PROVINCE.md ⇒ - `~/.config/the-janitor/client.py` (755, 117 lines) — HTTP client: session-id,
  `THE_JANITOR_REQUEST_TIMEOUT` (the `client.lock` flock lives in the CLI, not here — measured round 15:
  `grep -nic lock client.py` ⇒ 0, flock at `the-janitor` L130/139/175-176)
sed -n '22p' corpus/surface-census.tsv ⇒ $HOME/.config/the-janitor/client.py<TAB>asset<TAB>exec<TAB>755<TAB>HTTP client: session-id, request timeout (the flock is in the CLI)
```

Both gates stayed green after the edit (note-only change): `SURFACE_CENSUS: CLEAN (assets=20 runtime=15
scanned=4 ok=34 absent=2 skipped=0)` rc=0 and `DRIFT_PINS: CLEAN (files=15 symbols=20)` rc=0, measured
after the 22:37 edits.

Residual precision nit (one line, L1's call): the new PROVINCE text says "flock at `the-janitor`
L130/139/175-176"; measured, the three `flock 9` calls are **L131 / L140 / L176** and the
`exec 9>"$LOCK_FILE"` opens are **L130 / L139 / L175** (`sed -n '130,131p;139,140p;175,176p'` shows
exactly that pairing; `grep -c 'flock 9'` = 3, which is what row H1 asserts). The cited set is
correct as "lock sites", just not literally the `flock` lines — worth a parenthetical rather than a
re-edit.

Pin risk measured before the edit (recorded so L1 does not rediscover it):
- `corpus/claim-ledger.tsv:25` (`R11-11`) pins the census **row count only** —
  `grep -cv '^#' corpus/surface-census.tsv` ⇒ `^35$`. It stores **no hash** of the file
  (`grep -nE 'sha256|[0-9a-f]{40,64}' corpus/claim-ledger.tsv` ⇒ no match), so the note edit is safe
  for that row. (The `stamps.tsv`/`cells` machinery does pin the file sha — see §7d.)
- `corpus/drift-pins.sh` contains no reference to `PROVINCE` or `surface-census`; the note edit did
  not move a pin (drift verify green).

### 7c. Row observations that are NOT defects

- `H1` prints `mode=600`, i.e. `~/.local/state/the-janitor/client.lock` **exists** today, so the
  `mode=(600|absent)` alternation is exercised on the 600 branch; the `absent` branch is only
  exercised by `--selftest`. Fine, but worth a selftest assertion — it already has 28 cases.
- `H7`'s pinned `HITS=2` matched my measurement exactly (`cells=888 patterns=32+5 warns=2
  schema-absent=0`); `expect_exit 0|1` correctly lets the by-design exit 1 through.
- `E8` checks receipt **presence** (`k in d`) rather than type (`access_receipt`/`receipt_sha256`
  are strings, len 54/64 — measured); my row printed types. Presence is the weaker but non-leaking
  form; both are safe. Not a defect — flagging only the difference.

### 7d. Mid-flight timeline observed 22:39–22:42 (L1 editing concurrently; all three states resolved)

| when | what I ran | observed |
|---|---|---|
| 22:39:42 (`checklist.tsv` mtime) | `bash corpus/checklist-run.sh` | `ITEM-FAIL E4 (exit 1 want 0)` + `REF_PATH_SCAN: hits=3`, `CHECKLIST_RUN: BROKEN … failed=1`, rc=1 |
| 22:40:48 (tsv) | `--only E4` | `ITEM-LASTLINE E4 (want /^REF_PATH_SCAN: hits=0 excluded=5 raw=5$/ got '')` — the whole check body had been wrapped in `n=$( … )` with nothing consuming it ⇒ empty stdout, rc=0 |
| 22:40:48 (tsv) | `bash corpus/checklist-run.sh` | `POLICY row H7: expect_exit 0\|1\|2 is not N or A\|B` rc=2 (the message had no `…`, i.e. the parser was being widened at that instant) |
| 22:41:28 (tsv) / 22:41:50 (`checklist-run.sh`) | `bash corpus/checklist-run.sh` | `CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7` + `CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0)` rc=0, 2.3 s |

The three E4 survivors (before the exclusion was widened back to a name allowlist):
`./corpus/knowledge/op-env-refs.md:14`, `./corpus/lessons/round-5-aggregator-audit.md:19`,
`./corpus/transcript-scan.sh:202` — all the documented `op://vault/item/field` placeholder, missed by
the interim file-scoped exclusion `(^\./corpus/(surface-census|transcript-scan)\.sh:.*op://(FakeVault|wal)/)|(op://vault/<)`.
Proofs I ran in `/tmp` while the fixes were in flight (nothing written into the repo):
`grep … | grep -vE 'op://(FakeVault|wal|vault)/'` ⇒ `REF_PATH_SCAN: hits=0 excluded=5 raw=5` rc=0; the
unwrapped E4 body ⇒ the identical line rc=0. `checklist-run.sh:135` is now
`[[ "$exexit" =~ ^[0-9]+(\|[0-9]+)*$ ]]`, which accepts H7's `0|1|2`.

### 7e. `claim-ledger.sh` family is RED — round-15 integration tail, not a checklist defect

Measured 22:42–22:43 (the checklist gate itself is green):

```
bash corpus/claim-ledger.sh verify   ⇒ rc=1
CLAIM_LEDGER: FAIL (claims=18 failed=2 stamped=44 stale=3 missing=0 unresolved_ids=5 labeled_ids=17)
STALE corpus/surface-census.tsv sha=f8114ee44b15->4af0dbcc81fd lines=54->54 bytes=4732->4752
STALE PROVINCE.md               sha=0471d0c7c6ba->847cee6b6536 lines=42->43 bytes=6038->7274
STALE SKILL.md                  sha=60a1e8912972->9bdf4b7dc371 lines=653->662 bytes=55525->56718
FAIL R14-01 reason=exit-mismatch exit=1 want=0
FAIL R13-03 reason=exit-mismatch exit=1 want=0
```

The two FAILs are the two audit sub-gates, run as the ledger's own claims:

```
bash corpus/claim-ledger.sh docs  (R14-01) ⇒ rc=1
DOC_AUDIT: BROKEN (entries=18 row_linked=14 by_hand=3 undeclared=0 missing_ids=4 unpinned=1 duplicate_reasons=0 floor=9)
bash corpus/claim-ledger.sh cells (R13-03) ⇒ rc=1
CELL_AUDIT: BROKEN (cells=72 row_pointed=38 stamp_pointed=47 uncited=0 missing_ids=5 rows_run=14 row_failures=0 stale_pointers=3 self_skipped=4 orphans=0)
```

Cause inventory (all traceable to in-flight round-15 work):
- `grep -c '^R15-' corpus/claim-ledger.tsv` ⇒ **0** rows, while
  `corpus/knowledge/checklist-execution.md:11` declares `Reverify: R15-01, R15-02, R15-03, R15-04`
  (and `:170` cites `R15-04`) ⇒ `missing_ids=4` (docs) / `missing_ids=5` (cells).
- `corpus/stamps.tsv` has **no** entry for `corpus/knowledge/checklist-execution.md` ⇒ `unpinned=1`.
- The three edited files carry stale stamps (`stamps.tsv` rows 38/41/44 still hold the pre-edit
  sha) ⇒ `STALE` ×3 and `stale_pointers=3`.

Fix path (L1 is sole editor): add the four `R15-0x` rows, stamp the new knowledge doc, re-`stamp` the
three edited files. Note the checklist contract deliberately forbids any row from invoking
`claim-ledger.sh` (recursion) and the ledger skips self-audit rows, so this red state cannot leak
into the checklist verdict — it is the round-15 closure tail.

### 7f. H7's widened accepted state — judgement call, not a defect

`H7` now carries `expect_exit=0|1|2` and
`expect_last=^(TRANSCRIPT_SCAN: HITS=2 \(cells=… warns=… schema-absent=…\) db=.*|transcript-scan: db not found: .*)$`,
with a note declaring the purged state (`stop` + `rm -rf xdg-data`) as legitimate and "a THIRD state
(any other exit-2 cause) still fails the row". Measured behaviour of the second state:
`bash corpus/transcript-scan.sh --db /tmp/does-not-exist.db` ⇒ `transcript-scan: db not found:
/tmp/does-not-exist.db`, rc=2 — so the row can PASS with the scan never having run. The note's
third-state guard is the mitigation; flagging it as the strongest remaining "passes without the
check running" surface in the gate. L1 owns the call.

## 8. Round-trip

Findings in §7 (H8 bind-scope gap, stale lock note + measured pin risk) were sent to `Main`
via `write agent://Main`, and a correction was sent at 22:43: **7a CLOSED** — L1 landed the
`non_loopback` arm (row prints `CONTROL_PLANE: password_refs=0 listeners=0 non_loopback=0
established=0`, gate CLEAN); **7b CLOSED** — L1 rewrote `PROVINCE.md:12` and
`corpus/surface-census.tsv:22` with the correction plus the falsifier. The 22:43 message also
carried §7d (mid-flight E4 `hits=3` → E4 no-op → H7 `POLICY`, all resolved by L1's concurrent
edits; final CLEAN) and §7e (`claim-ledger.sh` family red: `R15-01..R15-04` not yet in the ledger,
new doc unstamped, 3 stale stamps ⇒ R14-01/R13-03 exit-mismatch).
`[xask dry — in-session fallback]` — no `xask` consult was run for this round (all questions were
answerable on this host).

```text
DESPAWN: gx-scout-hostscout — signal delivered. Send me shutdown_request.
```