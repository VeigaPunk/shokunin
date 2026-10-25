# Artifact provenance — `research/` harvest of 2026-09-28

Advisory data for chousa round 1. Not a verdict. Not a model-quality claim. No external fetch. Live browser profiles, cookies, and session stores were not opened (shape-only boundary). Instruction-shaped text inside the exports was treated as data and is not reproduced in full.

Fleet HEAD at reading: `ee2c018` (`2026-10-14T21:51:28-03:00`, subject `ops: fix the wave-registry invocation; dispatch chousa round 1`). Content of the four files matches the introducing commit; the worktree is clean on `research/`.

## Answer

| Artifact | What produced the bytes that are on disk | What the file's own header says | Unknowable locally |
|---|---|---|---|
| `research/README.md` | Same landing commit as the three dumps. Hand-written index, not a chat export. | Operator-surface harvest index. Names GPT-6-Astra, burner Chrome, CDP 9222, L0, no Deep Research entitlement, search counts 9/8/10. | Who typed it; whether those claims were counted from a live UI that the dumps do not preserve. |
| `A-shokunin-tradition.md` | ChatGPT web-UI text dump, chat title "Shokunin Mastery Tradition Research". Model **label** in page chrome: `GPT-6 Astra`. No session id. | Skip-link, sidebar, account label, user prompt, two duration strings, then a truncated answer. | Provider model id, effort tier, conversation id, whether the live answer continued past the dump. |
| `B-multiagent-knowledge.md` | Same capture class. Chat title "Research agent knowledge bases". Same model label. | Same chrome shape. One visible "Searched the web". Answer cut after an ACE case-study paragraph. | Same unknowns. Search-count 8 is not in the file. |
| `C-rank-taxonomy.md` | Same capture class. Chat title "Agent Maturity Naming Research". Same model label. | Same chrome, plus two visible search groups with query text and collapsed `10 more` rows. Answer cut after the menkyo-kaiden paragraph. | Same unknowns. The `10` is a collapsed-row widget, not a total of 10 searches. |

The landing event is knowable. The model completion session is not. `GPT-6 Astra` is a string in scraped page chrome plus a same-commit index claim. It is not a provider receipt.

## Surfaces and sweeps

Assigned surfaces, all read:

- `research/README.md` (17 lines, entire file)
- `research/deep-research-2026-09-28/A-shokunin-tradition.md`
- `research/deep-research-2026-09-28/B-multiagent-knowledge.md`
- `research/deep-research-2026-09-28/C-rank-taxonomy.md`

Widened only where the question "which session/model" cannot be answered from those four files alone. Each widening is labeled secondary. Not re-measured: the bounties telemetry ledger cited by kengaku round 3 (that tree is outside this pass; kasegi already records it lost).

Negative sweeps (absence is the result):

| Sweep | Result |
|---|---|
| `git log -- research/` | Exactly one commit, `0863746`. No later content edit. |
| `git diff 0863746 HEAD -- research/` and `git diff -- research/` | Empty. Worktree blobs equal the introducing blobs. |
| `git notes show 0863746` | `error: no note found`. |
| `grep` `LOG.md` for `0863746`, `browse harvest`, `deep-research-2026-09-28`, and `research/` | No matches. The fleet log never recorded this harvest. |
| `grep` `.ufo/l0-questions.md` for `deep-research`, `GPT-6-Astra`, `browse harvest` | No matches. The L0 side channel has no question or answer for this harvest. |
| `grep` `.ufo/watchdog.log` for `0863746`, `browse harvest`, `deep-research-2026-09-28`, `GPT-6-Astra` | No matches. The surviving driver log covers `2026-09-28T15:44:59-03:00` through `2026-09-28T23:55:00-03:00` (`.ufo/watchdog.log:1` and `:294`), which includes the landing minute. |
| `grep` `MISSION.md` for `Astra` or `GPT-6` | No matches. The current mission route table does not name this label. |
| Python scan of A/B/C for `http`, `https`, `chatgpt.com`, UUID, `conv_`, `chatcmpl-`, `resp_`, `session`, `9222`, `CDP`, `Deep Research`, `entitlement` | No hits. |
| `research/` directory listing | Only `README.md` and the three dumps. No HAR, CDP json, capture script, or sidecar. |
| `.ufo/watchdog-driver.log` | Path absent in this worktree. Unknown whether a second driver log existed on 2026-09-28 and was not preserved. |

`research/` inode birth `2026-10-13 16:44:48 -0300` is materialization time, not production time. `.git` birth is `2026-10-13 11:54:36 -0300`. The harvest commit is an ancestor of relaunch merge `e867f78` (`2026-10-13T16:47:03-03:00`, parents `415666f` lacks `research/README.md`, `bdff08b` has it, blob of A identical to `0863746`). Do not read filesystem mtime as an edit.

## Observed: landing event

Commit `0863746e9da95457f71b9e00a40361b88ab0df15`.

- Author and committer are the same string: `integrator <integrator@shokunin.local>`.
- Author date equals committer date: `2026-09-28T22:51:25-03:00` (unix `1790646685`).
- Subject: `research: 3 GPT-6-Astra browse harvests on shokunin tradition, self-improving agents, rank taxonomy`.
- Body empty. No trailer. No git note.
- Single parent: `2d19a64` at `2026-09-28T22:44:21-03:00` (424 seconds earlier), subject `sibling-mint allowance + kama probation entry`, same git identity.
- Single child: `3069841` at `2026-09-28T22:52:19-03:00` (54 seconds later), author `Joao Pedro Veiga <jpveigao10@gmail.com>`, subject a kake round-15 report. That child does not touch `research/`.
- The commit adds exactly four paths, mode `100644`:

| Path | Git blob | SHA-256 | Bytes | Logical lines | `wc -l` | Trailing newline |
|---|---|---|---|---:|---:|---|
| `research/README.md` | `455ac441585b876e1bd4093fdb7741707d905233` | `5199b23b4be6b59482295fac0f1de4ea1b04842afbfcb283ce01ce69b8e33e86` | 937 | 17 | 17 | yes |
| `.../A-shokunin-tradition.md` | `caf880d4c444d6ba5faaca17884f032ad5b11561` | `9033857d4625555c7b778dfad6df80e3e1b24ed8bffa3fee2fd445b9c5540b85` | 6474 | 110 | 109 | no |
| `.../B-multiagent-knowledge.md` | `7230cd692266b860b7ec5b2ae079f950687cda66` | `6d8dbddd3e2d2f47dcb153c5a3347cc6321db4afc72cf07da40f0f7fe5022006` | 5364 | 101 | 100 | no |
| `.../C-rank-taxonomy.md` | `71e0f74af3f7faf22b0bde6ccd83a9685b83a7a3` | `e48fe70ff92055c217ac6ca6ce68e403aa5689fee8717f3bd0ccf5badc92321b` | 8922 | 155 | 154 | no |

Logical lines are `splitlines()` (the last line has no newline, so `wc -l` is one short on A/B/C). Git `--stat` insertions match the logical counts (110/101/155). Line citations below use logical lines.

`0863746` is an ancestor of HEAD (`git merge-base --is-ancestor` exit 0) but is **not** on `git rev-list --first-parent HEAD` (count 0). `git name-rev` places it at `remotes/origin/devin/1792007067-readme-wiki-link~43^2~30`. A first-parent log of current HEAD will not show the harvest. The original parent/child neighborhood above is the landing line.

Neighbor in the driver log, not a producer: `.ufo/watchdog.log:251-252` records `complete kumitate round=15` at `22:51:39` and `launch kumitate round=16 runId=shokunin-r16-kumitate-r1790646699` at `22:51:41`. That run id is 14 seconds after the harvest unix time and names kumitate. It is not a ChatGPT session and it does not mention `research/`.

## Observed: what each header says

### `research/README.md`

The whole file is the header. No model chrome, no prompt, no duration.

- `:1-3` — `# research/`; "External research harvested by the operator surface, indexed by date dir."
- `:5-6` — section `deep-research-2026-09-28/`; "Three GPT-6-Astra research tabs on the burner Chrome (CDP 9222), fired 2026-09-28 by L0."
- `:7-8` — "the burner account has NO Deep Research entitlement — these are browse-enabled GPT-6-Astra responses (9/8/10 web searches each), not the Deep Research pipeline."
- `:10-17` — one-line glosses of A, B, and C. A's gloss restates corrections (`shokunin katagi`, `jin'i-ryu` coined). Those glosses are the index author's reading of the dumps, not a second source.

"operator surface" occurs in this file and, in a fleet-wide search for that phrase, nowhere else. It is not defined locally.

`L0` in fleet vocabulary is the operator side channel, not a model: `MISSION.md:84-88` ("The operator is reachable via `.ufo/l0-questions.md` ... the L0 answers by editing the file in place"). The README's "fired by L0" therefore means "fired by the operator" if it uses that vocabulary. The commit author string is not the operator personal identity. See rejections.

### Shared page chrome (A, B, and C)

Lines 1–16 and 18–29 are byte-identical across the three dumps. Line 17 and line 30 are the active chat title and differ. Line 32 is `Work` in all three. Line 33 is `Share` in all three (a button label; no URL follows it).

Observed header skeleton:

| Lines | Text | What it is |
|---|---|---|
| `:1` | `Skip to content` | Skip-link. Not how a ChatGPT JSON export or a clean markdown share starts. |
| `:2-8` | `ChatGPT`, `New chat`, `Scheduled`, `Library`, `Plugins`, `Explore`, `Pinned` | App navigation. |
| `:9-14` | Pinned titles, identical: PC Build Components; Open Bug Bounties Compilation; Clean Omarchy Install Guide; Explain DSH Integration; L1 T3; Clip Big Hero 6 | Sidebar state. Data only. `L1 T3` is a pinned title, not this wave's L1. |
| `:16-26` | `Recents` plus a list whose first item is the active chat and whose remainder is identical | Same account sidebar, three captures. |
| `:28` | `jpveiga` | Account display label. Not an email, not a user id. |
| `:29` | `Pro` | Standalone plan badge. (A substring count of `Pro` is inflated by `Propose` in the recents list; the badge is this one line.) |
| `:30-33` | Active title, `·`, `Work`, `Share` | `Work` is a project label in the UI. What project it is, unknown. `Share` is not a link. |
| `:34` | `You said:` | Start of the single user turn. |
| `:35` | One long line beginning `Deep research:` | User instruction text. Data. Not a mode badge. |
| `:36` and `:37` | `Worked for …` and `Working for …` | Two different duration strings. See per-file table. |
| `:38` | `ChatGPT said:` | First assistant beat. Each file has this label exactly three times. |

The identical sidebar with only the active title swapped is observed evidence that the three dumps came from one web UI profile at three chats, not from three independently authored notes.

### Per-file header facts

| | A `:36-37` | B `:36-37` | C `:36-37` |
|---|---|---|---|
| `Worked for` | `1m 33s` | `1m 36s` | `1m 11s` |
| `Working for` | `2m 9s` | `2m 8s` | `2m 7s` |
| Active title `:17` and `:30` | Shokunin Mastery Tradition Research | Research agent knowledge bases | Agent Maturity Naming Research |
| User turn topic (line 35, not quoted in full) | shokunin apprenticeship terms, kishitsu, ikigai, kodawari; asks for primary-ish sources | persistent specialist agents, self-rewrite failure, domain split, credit assignment; asks to cite papers | belt/dan/kyu and craft rank names; asks which terms map and what rank-inflation failure modes are; asks to cite sources |
| `Searched the web` | 1 (`:42`) | 1 (`:42`) | 2 (`:42`, `:55`) |
| Visible query text | none | none | `:44` `site.nihonkiin.or.jp english rank dan kyu professional amateur`; `:46` `site.kodokanjudoinstitute.org dan kyu history ranks`; `:57` `"自己立法" "自律"`; `:59` `"jin'i-ryu"` |
| Collapsed search rows | none | none | `:48` and `:61`, each `10 more` wrapped in U+2068 FIRST STRONG ISOLATE and U+2069 POP DIRECTIONAL ISOLATE |
| `Response started` | 1 | 1 | 1 |
| Citation chips in the body (`+N` alone on a line) | `:69` `+3`, `:84` `+2` | `:73` `+6` | `:83` `+5`, `:122` `+4` |
| Last substantive body line before the footer | `:89` (Nishioka / graduated responsibility). Section 1 is unfinished. | `:79` (ACE brevity-bias case study). The three numbered questions are unfinished. | `:133` (menkyo kaiden). No terminal source list. |
| Disclaimer | `:90` `ChatGPT can make mistakes. Check important info.` | `:81` same | `:135` same |
| `Latest response` | `:91` | `:82` | `:136` |
| Model-picker block | `:96-110` | `:87-101` | `:141-155` |

The picker block is byte-identical in all three files:

```
GPT-6 Astra
Light
None
Minimal
Light
Medium
High
Extra High
Max
Ultra
Persistent
Outputs
Create file or site
Sources
Web search
```

`Light` appears twice. Nothing in the block is marked selected. `Sources` and `Web search` here are footer controls. B also has a body line `:71` beginning `Sources:` that names papers; that is answer text, not the footer control. A and C have `Sources` only in the footer.

No file contains a date. The calendar date `2026-09-28` is the directory name and the commit timestamp. It is not inside the chats.

A and B contain U+0009 tabs in table rows only. C has those tabs plus the two isolate pairs. No BOM, no CR, no NUL.

## Observed: model label versus session

What is in the files:

- The string `GPT-6 Astra` occurs once per dump, inside the picker block above, not inside the answer prose.
- The commit subject and `research/README.md:6-8` repeat `GPT-6-Astra` (hyphenated). Same commit as the dumps, so this is not an independent later measurement.
- No API model slug, snapshot, system fingerprint, response id, or effort-selection marker is in the dumps, the commit object, or `MISSION.md`.

What is not a receipt for these files (secondary, name overlap only):

- `.ufo/reports/round-3/kengaku.md:24` (dated 2026-09-28 in that report) lists a route-name count `gpt-6-astra:max` 123 inside a census of `~/Projects/bounties/ledger/telemetry.jsonl`. This pass did not re-read that ledger. The report is a fleet lane's claim about a routing ledger, not a ChatGPT completion id, and it does not cite `research/`.
- `.ufo/waves/shokunin12h-20261014-p1-repair/members/KamaHistoryClaims.md:112` records `openai-codex/gpt-6-astra:max` as a selector absent from a later non-secret config reading. That is a historical-name note. It does not tie a completion to these dumps.
- Current `MISSION.md` route table (`:19-30`) names lane axes and `route: swe`. It does not name Astra.

No local artifact binds the picker label to a fleet `runId`. The dumps' chrome is ChatGPT web UI (`ChatGPT`, `You said:`, `ChatGPT said:`, skip-link, sidebar). Fleet lane launches in `watchdog.log` do not look like that.

## README claims against local corroboration

| README claim | Lines | Corroborated locally by | Status |
|---|---|---|---|
| Three artifacts under a `2026-09-28` directory | `:5-6`, `:10-16` | The three files exist; one commit added them on that calendar date | Observed for existence and landing date. Generation date is not in the chats. |
| GPT-6-Astra | `:6`, `:8` | Picker label `GPT-6 Astra` in each dump; commit subject | Label observed. Provider id unknown. |
| Browse harvest / not the Deep Research pipeline | `:7-8`; commit subject says `browse harvests` | Dumps show `Searched the web` and footer `Web search`. User text says `Deep research:`. No mode chip reading `Deep Research` appears. | The "browse" description matches visible search chrome. The pipeline denial is a README/commit claim, not an account record. |
| Burner Chrome, CDP 9222 | `:6` | Not in A/B/C, not in the commit object, not in `watchdog.log`, not in `l0-questions.md`. A standing CDP 9222 / musketeer lease is documented elsewhere in the fleet (contested kake/kagi surface). That documentation does not name these files. | README-only. Not a capture receipt. |
| Fired by L0 | `:6` | `L0` means the operator (`MISSION.md:84-88`). Commit author is `integrator`, not `Joao Pedro Veiga`. Parent commit `2d19a64` is the same integrator identity; `PROTOCOL-APPENDIX.md:42` describes **that** commit as the operator minting kama. It does not mention `0863746`. | Actor claim uncorroborated for this commit. Not contradicted. |
| No Deep Research entitlement | `:7-8` | String `entitlement` and `Deep Research` absent from A/B/C. No billing or account record in the assigned surfaces. | README-only. Absence in a truncated dump is not proof. |
| 9/8/10 web searches each | `:8` | A has 1 `Searched the web`, B has 1, C has 2, plus two collapsed `10 more` widgets and `+N` citation chips. Integers 9 and 8 do not occur as search totals. The triple is not labeled onto filenames. | Not recoverable from the dumps. Same-commit index claim. Mapping 9→A, 8→B, 10→C would be a left-to-right reading, not a labeled assignment. Not adopted. |
| External research harvested by the operator surface | `:3` | The dumps are external-UI text. "operator surface" is undefined. Landing identity is `integrator`. | Half observed (external UI text), half undefined. |

## Inference (not observation)

1. Capture class is a rendered-page text dump (innerText, accessibility tree, or equivalent), not an official conversation export. Basis: `:1` skip-link, full sidebar before the turn, footer picker after a mid-argument body, no JSON, no URLs, C's U+2068/U+2069 around a widget count, A/B/C lacking a trailing newline while the hand-written README has one. The exact tool is not in the files. Confidence: medium on the class, none on the tool name.
2. The live DOM at scrape time contained both a completed-duration widget and a progressive `Working for` widget, and the answer region did not include a finished source list. That is compatible with a scrape during generation, a scrape of a virtualized/collapsed answer, or a finished page whose text extractor stopped at the footer. Which of those is true is unknown. Do not treat the cut as the model's stopping point.
3. The three chats existed in one sidebar (shared recents tail). They were not necessarily scraped in one atomic second: each file shows its own title as the current recent. Order of capture is unknown.
4. Generation time is ≤ scrape time ≤ commit time `2026-09-28T22:51:25-03:00`. No lower bound. The path date may name the harvest day rather than the generation day. The UI durations are one to two minutes of labeled work, not wall-clock dates.
5. String prefix `jpveiga` overlaps the operator git local-part `jpveigao10`. That is not an identity binding. No email is in the dumps.

## Unknown

- ChatGPT conversation id, share URL, message id, response id, CDP target id, browser profile path used for **this** capture.
- Provider model slug, snapshot, and which effort row was active. The picker lists options and marks none.
- Whether `GPT-6 Astra` in that UI is the same system as any fleet route whose name contains `gpt-6-astra`. Not decidable from these files. Not evaluated for quality.
- Whether the account label is the operator's ChatGPT account.
- Whether the operator, an agent under `integrator@shokunin.local`, or a script created the files and the commit. The author string is the only process fact.
- Whether the answers were longer in the live UI than in these 5–9 KiB dumps.
- Whether search totals were 9/8/10 in a part of the UI the dump collapsed, or the index invented them.
- Account entitlement.
- Wall-clock start of each chat.
- A preserved capture log. None is in `research/`, `LOG.md`, `l0-questions.md`, or the watchdog log that covers the landing minute.

## Rejected conclusions (kept)

1. **Rejected:** the exports themselves show 9, 8, and 10 web searches. Reason: visible search events are 1, 1, and 2; C's `10 more` is a collapsed-row label wrapped in bidi isolates; `+N` chips are citation clusters, not search totals.
2. **Rejected:** missing Deep Research chrome proves the account had no entitlement. Reason: truncated page dump; entitlement is an account fact; no account record was consulted.
3. **Rejected:** these files were captured through CDP 9222 / the musketeer burner profile. Reason: those identifiers are absent from the dumps and the commit. Fleet docs of that lease do not name this harvest. The README asserts the link; nothing else locally ties it.
4. **Rejected:** sidebar `jpveiga` is authenticated as `Joao Pedro Veiga <jpveigao10@gmail.com>`. Reason: display label only. Shape-only stop. No session store opened to test it.
5. **Rejected:** fleet route `gpt-6-astra:max` produced these chats. Reason: different surface (a routing-ledger count in a kengaku report, not re-read here) and no shared response id. Name overlap is not a session. This is not a quality comparison and is not kengaku's evaluation to absorb.
6. **Rejected:** filesystem birth `2026-10-13 16:44:48` is when the chats were produced. Reason: git author date is 2026-09-28; blobs unchanged since `0863746`; birth matches the relaunch checkout window, not the commit.
7. **Rejected:** the dumps are complete transcripts. Reason: footer chrome follows an unfinished answer; user text asked for citations; no source list was dumped; sizes are 6474 / 5364 / 8922 bytes.
8. **Rejected:** "fired by L0" is a verified actor fact for `0863746`. Reason: L0 is the operator side channel; this commit's author is `integrator`; the personal-identity commit 54 seconds later is a different subject and does not touch `research/`. The appendix's "operator minted" sentence is about parent `2d19a64` only (`PROTOCOL-APPENDIX.md:42`).
9. **Rejected:** a watchdog-dispatched lane session produced the chat text. Reason: no `runId` in the dumps or the commit; the driver log covering `22:51` records a kumitate respawn and does not record this harvest.

## Later local narratives (not production receipts)

These post-date the landing and must not be folded back into it.

- `chousa-shokunin/MINT.md:8-13` (heading date 2026-10-14) says the three artifacts were "produced by an operator research pass" and are "archived, unindexed", citing "the files plus `research/README.md`". The operator-pass sentence is the same class of claim as README `:6`, still without a session id. "Unindexed" is false of the tree that contains `research/README.md:10-17`, which indexes them. Mint narrative, not a receipt.
- `.ufo/scopes/shokunin-12h-20261014/operator-demand.md:25` says the exports' citation labels are research data, not externally verified primary sources. That matches what the containers are. It does not add a producer session.
- `.ufo/scopes/shokunin-12h-20261014/data-walk.md:25` lists A/B/C and omits the README. Inventory note only.
- `.ufo/reports/round-10/seats/sweep-window.md:37` indexes `0863746` as integrator, `22:51:25-03:00`, "research: 3 GPT-6-Astra browse harvests". Restates the commit. Does not add a model receipt.

## Central finding (provenance slice)

These three artifacts are truncated ChatGPT web-UI text dumps landed by `integrator` at `2026-09-28T22:51:25-03:00` in `0863746`, indexed in the same commit by a README whose capture-method claims (CDP 9222, L0, entitlement, 9/8/10) are not independently present in the dumps or in the driver log. Their in-body citations are unverified text in that dump — names and chips, not fetched sources, and not checked here. A reader who cites A/B/C as primary research is citing an unverified, incomplete page scrape whose producing completion session cannot be recovered from local evidence.

Confidence: high on file identity, the landing commit, header text, and the named absence sweeps. Medium on capture class (page-text dump). None on provider model id, effort, conversation id, CDP target, entitlement, and which process sat behind `integrator@shokunin.local`.
