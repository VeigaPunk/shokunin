# Kaika runtime probe — fresh CLI inheritance of the operator tooling directive

Seat: GlobalToolingRuntime (read-only runtime probe; no repo edits, no installs, no config changes).
Date: 2026-10-19. All times UTC unless noted.

## Hypothesis and expected observation (declared before the run)

Expected: a fresh noninteractive `omp` session (route `@m_flash` given only on the CLI) would
(a) report the operator `Tooling directive` from its own inherited context, and (b) spawn a
`sonic` task that can quote the directive's first sentence and answer the install-authorization
question. The mechanism under test was the runtime wiring of
`~/.omp/agent/RULES.md` + `~/.omp/agent/hooks/pre/godspeed-always-on.js`.

Pre-declared falsifier: any directive bytes present in the CLI prompt would make a quote
meaningless (prompt echo); absence of the bytes in both the fresh session's context and the
child's spawned context would mean no inheritance.

## Command (one bounded invocation; nothing else was run against the route)

```
cwd: /tmp/kaika-verify/global-tooling-runtime
timeout 900 omp -p --no-title --max-time 600 --model @m_flash \
  --session-dir /tmp/kaika-verify/global-tooling-runtime/sessions \
  @/tmp/kaika-verify/global-tooling-runtime/probe-prompt.txt
```

- rc = 0. Wall time 5m09.307s. Start 2026-10-19T23:39:28Z, end 23:44:38Z.
- Route resolution, from the session record (`type:"model_change"`):
  `model = charm-hyper/deepseek-v4.1-flash`, `resolvedModelIsFallback = false`;
  thinking level `max`. This is `@m_flash` from `modelRoles`.
- Child route, from the spawn records: `agent = sonic`, `modelRole = smol`,
  `resolvedModel = charm-hyper/qwen3.8-flash:high`.
- Prompt sent: `/tmp/kaika-verify/global-tooling-runtime/probe-prompt.txt`,
  1,772 bytes, sha256 `e2e333cd0dc780f504513facb828dd0ce42c0452941c95c32c08929a7d4af8b7`.
  A pre-run scan over that file for `Tooling directive`, `installs or updates`,
  `full privilege`, `without asking first`, `sudo`, `pacman` returned **0 matching lines**.
- The main-session user message stored in the transcript is exactly
  `<file name="…/probe-prompt.txt">…</file>` with **0** occurrences of `Tooling directive`.
- One earlier local attempt aborted before `omp` started (shell wrapper `__fnmcd`, rc 127);
  it produced no session and is not part of the probe.
- CLI output was captured with `tee` to `/tmp/kaika-verify/global-tooling-runtime/probe.out`
  (6,984 bytes) so the result survives loss of the outer tool background notification.

## Fresh session (main agent) — result

The main session reported (final message in `probe.out`; also in its session transcript):

- Heading, quoted verbatim:
  `# Tooling directive — operator, 2026-10-19 (always on, every agent)`
- First body sentence, quoted verbatim (the file hard-wraps it; reproduced as displayed):
  `Any agent — main session or subagent, any lane, any wave — installs or updates any tool that helps its task or is a strict upgrade, with full privilege, without asking first.`
  (It additionally quoted the next sentence, `Passwordless \`sudo\` is available.`)
- Placement claim: arrived via its **system prompt**, in a `<generic-rules>` block in the
  runtime section; explicitly not from the user message and not from tool output.
- Install authorization: **YES**, citing `with full privilege, without asking first` and
  `Passwordless \`sudo\` is available.`
- It also listed the standing constraints (channel order; official sources only;
  full-system upgrades behind the tsukuroi-shokunin gate; no partial upgrade;
  record every install) — all matching `RULES.md`.

Artifact corroboration / limits:

- The **first assistant message** (recorded before any tool result exists; the first tool
  result is 91 bytes and contains no directive text) already contains
  `Tooling directive`, `Passwordless`, and the heading. The user message has 0 directive
  bytes. The only channel available to the model at that point was its session system
  prompt. No file-reading tool was used on `RULES.md`; the main session's tools were
  `task` (×3), `write` (×3, `proc://…/kill`), `eval` (×1) and `wait` (×1).
- Limitation: omp persisted only a 16-hex system-prompt digest for this session
  (`system-prompt-digest = 902ac102a05321ec`), not the rendered system prompt. The
  system-prompt placement is therefore the model's report, corroborated by first-turn
  timing and byte-exact quoting, but not directly readable as a stored prompt body.

## Child (sonic) — result

Requested: exactly one `sonic` task. Observed deviation: main spawned **four**
(`SonicDirectiveCheck`, `-2`, `-3`, `-4`) while diagnosing a payload-wrapping anomaly.
`-2` was cancelled before output; `-1` and `-3` were cancelled after completion
(their snapshot `.md` outputs both quote the heading and first sentence; `-2.md` is
empty). `-4` is the final child relayed by main. All four spawn records have the same
task length and the same injected payload shape (below).

Child `-4` model report, relayed verbatim by main in `probe.out`:

- `(1) Yes — my context contains such a section.`
- Location claim: system prompt, inside a `<generic-rules>` block after the main
  instructions; it notes the same text is also echoed in the task/user message but says
  the original placement is the system prompt.
- Heading quoted verbatim: `# Tooling directive — operator, 2026-10-19 (always on, every agent)`
- First body sentence quoted verbatim: `Any agent — main session or subagent, any lane, any wave — installs or updates any tool that helps its task or is a strict upgrade, with full privilege, without asking first.`
- Authorization: `YES`, citing `installs or updates any tool … with full privilege, without asking first`, `Passwordless \`sudo\` is available.`, `Official sources only …`, the tsukuroi gate / no-partial-upgrade rule, and the record-every-install rule.
- It stated it ran no tools and installed nothing.

### Actual recorded child prompt vs the child's report (separately)

From the child session spawn records (`SonicDirectiveCheck*.jsonl`), not from the model's
answer:

1. **System prompt does carry the directive.** The recorded `systemPrompt` is a 3-part
   array (~63,376 characters joined for `-4`); it contains exactly **one** occurrence of
   `Tooling directive`, inside `<generic-rules>` immediately after `</skills>`, and the
   full `RULES.md` content is byte-identical to `RULES.md` trimmed of its final newline
   (`contains(RULES.md.rtrim("\n")) = true`; the block tail is
   `… Record every install or update — tool, version, channel, reason — in your report or handoff.`).
   The same is true for all four spawn records. The system prompt does **not** contain
   the godspeed directive body (APPEND_SYSTEM is main-only); the child's leading
   `/skill:godspeed` comes from the task text.
   → The child's "system prompt" attribution **agrees with the recorded prompt**.
2. **Task/user prompt also carries the directive, appended at dispatch.** Recorded
   executed task text (`-4`, 1,639 code points, identical for all four):
   `Complete assignment thoroughly:\n\n` (33) + `/skill:godspeed\n\n` (17) +
   the 609-code-point probe block + `\n\n` (2) + `RULES.md.trim()` (978) = 1,639.
   Exactly one occurrence of `/skill:godspeed` and one of `Tooling directive`; no
   double-append. The appended text ends byte-identically with `RULES.md.trim()`
   (`endswith = true`).
   → The child's "also echoed in the task/user message" note **agrees with the record**.

### Runtime rewrite evidence (hook fired; not caller transcription)

`SonicDirectiveCheck-4` was spawned by main from the eval kernel. Main's recorded eval
code calls `tool.task({… tasks:[{ name:'SonicDirectiveCheck', agent:'sonic', task: block, …}]})`
where `block` is exactly the probe block extracted between the `---` markers
(609 code points / 613 UTF-8 bytes, sha256
`30a646c226f99432e114cc01b25b4ace919805b0f44b704dc983592dcb56b60e`). The eval log
(`sessions/…/0.eval.log`) shows the resulting assignment already wrapped with
`/skill:godspeed` + the directive, and the child's stored task text matches that.
Therefore the invocation prepend and directive append happened **in the dispatch layer**,
not by caller transcription. The shape matches `godspeed-always-on.js` exactly:
`hasInvocation(block)=false` → prepend `/skill:godspeed`; marker absent → append
`RULES.md.trim()`.

For the three `task` tool calls, the recorded tool-call arguments are post-rewrite and
measure 1,606 code points (= 17 + 609 + 2 + 978); the model-authored pre-rewrite bytes for
those three calls are not separately recorded. Main's final narrative claims it inserted
the invocation/appended the directive itself; that is contradicted for the eval spawn by
its own recorded code, where the bare block was passed and the wrapper still appeared.
No hook-load log line exists (`setLabel` is not persisted), so hook execution is inferred
from the byte-exact rewrite semantics and the absence of any other `RULES.md` reader in
the run.

## Is the quote a prompt echo? (explicit check)

- The CLI prompt contained **0** directive bytes (hash and marker scan above), and the
  fresh session's user message is that file with **0** occurrences.
- The child's context did contain the directive from two runtime channels: the recorded
  system prompt under `<generic-rules>`, and the hook-appended task text.
- Therefore the quoted first sentence is **not** an echo of the probe prompt; it matches
  inherited/dispatch-injected bytes. The child's system-prompt inheritance is
  independently substantiated by the stored prompt, so the conclusion does not rely on
  the task-prompt copy.

## Observed discrepancies and scope notes

1. `godspeed-always-on.js`'s comment says user sticky rules are not inherited by task
   sessions. In this runtime (omp 18.12.3) the sonic system prompts **do** carry
   `RULES.md` under `<generic-rules>`; the hook's append is therefore redundant for the
   directive on this path (it remains idempotent: exactly one task-prompt occurrence).
2. The hook comment says eval helpers emit no `tool_call`; here a direct `tool.task`
   call from the eval kernel **was** rewritten (the `agent()`/`workpool()` helpers were
   not exercised by this probe).
3. A harness envelope prefixes spawned assignments with
   `Complete assignment thoroughly:\n\n`; this is not produced by the hook.
4. Main's own diagnosis ("I inserted `/skill:godspeed` and appended the directive") is a
   misattribution: its recorded eval code passed the bare block. The three tool-call
   args are stored post-rewrite, so the model could only have inferred authorship from
   the echoed payload.

## Limitations

- One fresh CLI invocation, one route (`@m_flash`), one cwd; not a cross-host or
  cross-tool test. The parent notes `~/.agents/AGENTS.md` and `~/.config/devin/AGENTS.md`
  were created after this probe started, so they are not explanations of this result;
  no Devin/Kimi runtime inheritance is claimed.
- Main's rendered system prompt is not persisted (digest only). Main's system-prompt
  placement is a model report corroborated by first-turn timing and byte-exact quotes,
  not by a stored prompt body.
- The probe spawned four children instead of one; the first three were cancelled (two
  after producing output). Only `-4` was relayed by main, though `-1`/`-3` snapshots
  agree in substance.
- Child reports are model answers; all mechanism conclusions above are based on the
  recorded `systemPrompt`, `task`, spawn result, and eval log, not on model intent.
- No installs, no config edits, no repository edits, no pushes. No second CLI run.

## Cleanup and evidence

- Retained (probe evidence): `/tmp/kaika-verify/global-tooling-runtime/`
  `probe-prompt.txt` (sha256 `e2e333cd…af8b7`), `block.txt`, `probe.out` (6,984 bytes),
  and `sessions/` (main session + four child sessions + `0.eval.log`, 668 KB total).
  Main session: `2026-10-19T23-39-29-057Z_01a15688-cfa1-76df-ad8c-7192c79b4bc6.jsonl`.
- Removed an unrelated scratch dump created while inspecting the CLI binary
  (`/tmp/omp-strings.txt`).
- No background processes were left running; the probe job completed and was captured.
