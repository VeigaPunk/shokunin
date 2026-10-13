# Round 15 checklist policy/leak audit

Scope: landed `corpus/checklist.tsv` and `corpus/checklist-run.sh`; read-only audit. Commands below were run from the repository root unless stated otherwise. No handler start/stop, `op`, vault read, or `$CONFIG_DIR/op.env` byte read was performed by this audit.

## 1. Runnable-check host surfaces

The nine runnable rows are E1, E4, E5, E8, H1, H3, H4, H7, H8. `checklist.tsv` was inspected directly with:

    read corpus/checklist.tsv
    read corpus/checklist-run.sh:1-180

| row | surface touched by the row | classification | denied operation audit |
|---|---|---|---|
| E1 | repo `corpus/surface-census.sh`/TSV/state-shape plus host declared paths; `corpus/drift-pins.sh` plus its 15 pinned host paths | mixed: metadata-only for ordinary files; secret-bearing paths (`$CONFIG_DIR/op.env`, private custody/handoff JSON) are touched only for mode/line/key-shape metadata | no `op`, no reference resolution, no handler start/stop, no op.env bytes emitted; drift gate deliberately does not hash no-hash secret-bearing files and prints paths/counts/verdicts only |
| E4 | repository tracked `*.md`, `*.tsv`, `*.sh` bytes, via grep; it reports counts only | metadata-only corpus scan (the bytes are documentation/source, not host credential material) | no denied operation; placeholder-shaped literals are counted and the three declared placeholder names (`vault`, `FakeVault`, `wal`) are excluded visibly in `REF_PATH_SCAN` |
| E5 | `corpus/op-ref-probe.sh`; generated temporary fixture files and the installed `op` executable | fixtures are synthetic/plain-value metadata; the executable is an external credential-capable boundary | **executes `op` on generated plain-value fixtures**. It does not read real `$CONFIG_DIR/op.env`, does not resolve a reference (its guard refuses ref tokens before exec), does not start/stop handler, and does not write `$STATE_DIR`. This is the one runnable row whose delegated gate invokes `op`; its note explicitly documents the exception and the guard. |
| E8 | `~/.local/state/tac/handoff-status.json`, parsed by Python | secret-adjacent/private custody surface; row reads JSON values to test two boundary booleans and field presence | no secret/hash/path value is printed; output is only boundary count and `receipt=present sha=present`; no op/ref/handler/state write |
| H1 | `~/.local/bin/the-janitor` source; `$STATE_DIR/client.lock` via `stat` (if present) | metadata-only source/permission/lock metadata | no lock acquisition, no handler invocation, no op.env read, no write |
| H3 | `~/.config/the-janitor/opencode.json` and global `~/.config/opencode/opencode.json`, parsed as JSON | configuration metadata; not secret-bearing in the measured fields | prints only counts/booleans/labels, not URLs or provider values; no op/ref/handler/state write |
| H4 | `~/.config/opencode/agents/janitor.md` front matter | policy/config metadata | prints only entry count and `steps`; no denied operation |
| H7 | `$STATE_DIR/xdg-data/opencode/opencode.db` and its WAL/SHM siblings, copied to `mktemp`; SQLite transcript tables are scanned | **secret-bearing durable transcript surface** (may contain secret-shaped material); scanner is counts-only and scans the copy, not the source in place | no secret row/text output; no reference resolution, op exec, handler start/stop, or state-dir write. The source DB is copied; no SQLite open is made against the live DB. |
| H8 | CLI/client source for password-token count; `ss` network socket metadata for port 40961 | metadata-only | `ss` is read-only; no connect/request/start/stop. It prints only password-reference count and listener/connection counts, not payloads or secret values. |

Additional literal command audit: `grep -n 'op.env\|op run\|the-janitor start\|the-janitor stop\|the-janitor run\|claim-ledger.sh' corpus/checklist.tsv` shows the gate's deny policy and the E5 delegation. `checklist-run.sh` line 66 denies those strings in a row's own check; E5 delegates to `op-ref-probe.sh`, whose own header/guard states that only generated plain fixtures reach `op` and any ref token is refused before exec.

**GATE: PASS** — every runnable row was classified; no row reads real `$CONFIG_DIR/op.env` bytes, resolves a ref, starts/stops the handler, or writes `$STATE_DIR`. E5 is explicitly flagged as an `op` execution on synthetic fixtures, not silently treated as no-op execution.

## 2. Encoding `transcript-scan.sh`'s designed exit 1

The exact command used to inspect its exit discipline was:

    grep -n 'exit 2\\|exit \\$((\\|absent' corpus/transcript-scan.sh
    sed -n '276,282p' corpus/transcript-scan.sh

Observed source contract: exit 0 means clean-or-warn, exit 1 means any HIT, exit 2 means usage/DB/schema error; the final line is `TRANSCRIPT_SCAN: HITS=<n> (...)` and the script exits `1` when `hits > 0`, otherwise `2` for schema absence. The landed H7 row encodes:

    expect_exit = 0|1|2
    expect_lastline = ^(TRANSCRIPT_SCAN: HITS=2 (...exact summary shape...)|transcript-scan: db not found: .*)$

This is safe against absorbing a future leak only because the HITS branch pins the **exact current count `2` and summary shape**. A future genuine leak changes the count (or output shape), producing `ITEM-LASTLINE`; an unrelated exit-2 error cannot match the separately allowed `db not found` line. The proposed/required encoding is therefore a disjoint union of explicitly named states: `1 + exact baseline verdict`, plus any separately justified setup state with its exact terminal diagnostic; never `expect_exit=1` with a broad `.*` or an exit-only acceptance. Re-baseline only after reading count-only HIT diagnostics. `--selftest` remains a separate runnable row if desired; it expects exit 0 and `SELFTEST OK`.

**GATE: PASS** — H7's row cannot absorb arbitrary exit 1: exit and last-line are both required, with exact HITS count and a separately named DB-absent state.

## 3. `ss` and receipt redaction

Commands used (values intentionally withheld):

    ss -ltnp 2>/dev/null | awk '$4 ~ /:40961$/ {print}'
    ss -tn 2>/dev/null | awk '$5 ~ /:40961$/ {print}'
    jq -r 'keys_unsorted[]' ~/.local/state/tac/handoff-status.json
    jq -r '.receipt_sha256 | length' ~/.local/state/tac/handoff-status.json
    jq -r '.access_receipt | type' ~/.local/state/tac/handoff-status.json
    sha256sum "$(jq -r .access_receipt ~/.local/state/tac/handoff-status.json)" | cut -d' ' -f1

Observed: no port-40961 listener/connection rows; handoff keys include `access_receipt` and `receipt_sha256`; hash length is 64; access receipt is a string; a non-secret equality check confirmed the first 8 hash characters match the locally computed receipt digest (only `prefix8 match: YES` was printed).

`ss` endpoint/listener/process metadata is safe for this gate when restricted to counts/loopback classification; do not print socket payloads, command lines, or environment. `receipt_sha256` is **not safe to print**: the corpus's hash policy calls it a private-custody confirmation oracle. A full digest (and even a prefix) can confirm guesses about private receipt bytes. Receipt paths are also not safe to print in the gate's generic stdout: they disclose private filesystem layout and can identify the evidence artifact. The gate must use presence/type/shape only.

Redaction rule: never interpolate `access_receipt`, `receipt_path`, `receipt_sha256`, or any nested receipt value into a verdict. Emit only fixed labels such as `receipt=present sha=present`, a boolean/type, and bounded structural counts (for example `boundaries=3`). If a diagnostic must distinguish a path, emit a fixed token such as `path=present` (or a scrubbed basename only if a separate policy explicitly permits it); never emit the path, digest, digest prefix, or file contents. This matches the landed E8 output, which prints presence labels only.

**GATE: PASS** — the checklist's E8 stdout is redacted; no `ss` payload or receipt value enters it. The rule above is mandatory for future rows.

## 4. Durable artifact grep findings

Exact commands:

    grep -rnoE 'op://[A-Za-z0-9_.-]+/' --include='*.sh' --include='*.md' --include='*.tsv' . | sort | uniq -c | sort -rn
    grep -rnE 'the-janitor run --|run --' --include='*.md' --include='*.tsv' --include='*.sh' .
    grep -rnoE 'op://[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(/[A-Za-z0-9_.-]+)+' .

Findings (all paths are durable corpus/source artifacts, and all reported literals are schematic/test placeholders, not live vault paths):

- `corpus/op-ref-probe.sh:184-186,188-189,591,620-622` uses `op://Kagi12NoVault/I/F` in generated refusal/selftest fixtures.
- `corpus/surface-census.sh:608` uses `op://FakeVault/FakeItem/F3` in a scratch fixture.
- `corpus/transcript-scan.sh:202` uses `op://vault/item/field` in a seeded selftest row; `:242` uses `op://wal/...` in a WAL selftest marker.
- `corpus/knowledge/op-env-refs.md:14`, `corpus/knowledge/op-ref-consumption.md:56-58`, and `corpus/lessons/round-5-aggregator-audit.md:19` use schematic `op://vault/item/field`, `op://V/I/F`, or explanatory placeholder forms.
- The segmented-ref scan produced no live-looking path: every hit is one of the above placeholders. E4's landed scan reported `REF_PATH_SCAN: hits=0 excluded=5 raw=5` (the five raw shape hits are all excluded placeholder forms).
- The `run` grep found command syntax/documentation and test commands, but no pasted secret-bearing output. Examples are `corpus/knowledge/janitor-env-contract.md:88`, `corpus/lessons/round-5-aggregator-mirror-bare-path-and-unclosed-prereq.md:30`, and generated scratch commands in `corpus/surface-census.sh:590,612,661`; these contain command shapes or fabricated values, not captured output.
- No durable artifact was found with a concrete vault/item/field ref path or pasted `the-janitor run` secret output. `SKILL.md:30,32` explicitly warns against the practice; warnings are not violations.

**GATE: PASS** — no durable artifact violates item 7 (real ref paths out of artifacts) or item 6 (never paste `the-janitor run` output). The E4 allowlist is a visible, named placeholder exception; its residual risk is that a future artifact could reuse one of those names, so the count/allowlist output must remain reviewed rather than treated as proof of semantic safety.
