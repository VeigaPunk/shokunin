# NegativeClaimSweep

Advisory data for chousa probation round 1. Not a verdict, not a promotion mark, not a judge result. Labels `NCS-1` and `NCS-2` are this report's only. They are not corpus ids.

A negative claim is checkable only when the record names a closed universe, an orthography, a hit predicate, the command that was or would be run, what a hit means, and what a zero does not reach. A narrator's "I found no" is not that record.

## Central finding

The three survey files are chat-export transcripts, not source dossiers. Their citations are unverified, and that is the bound on both sweeps below — not a defect to paper over.

Observation. Each file opens with ChatGPT sidebar chrome (`Skip to content`, pinned chats, `You said:`) and ends in UI chrome (`ChatGPT can make mistakes. Check important info.`, `Latest response`, a model picker, then `Sources` / `Web search` with no source list under those labels). `research/deep-research-2026-09-28/A-shokunin-tradition.md:90-110`, `B-multiagent-knowledge.md:81-101`, `C-rank-taxonomy.md:135-155`.

Observation. Zero `http://` or `https://` URLs in the three exports. Command, fleet root, GNU grep 3.12 via `/usr/bin/grep` (see Runner):

```
/usr/bin/grep -c -E 'https?://' \
  research/deep-research-2026-09-28/A-shokunin-tradition.md \
  research/deep-research-2026-09-28/B-multiagent-knowledge.md \
  research/deep-research-2026-09-28/C-rank-taxonomy.md
```

Result: `0` / `0` / `0`, exit 1. Runnable locally: yes. Run: yes.

Observation. What the exports do contain as "sources" are chips, not locators: `コトバンク`, `+2`, `+3`, `+4`, `+5`, `+6`, and bare domains (`adachi-hanga.com` at A:83; `arxiv.org` at B:51 and B:72; `archive.nihonkiin.or.jp`, `old2.kendo.or.jp`, `nihonkiin.or.jp`, `jstage.jst.go.jp` in C). No path, no line, no quote, no retrieval date. That fails the fleet's own citation-base rule: a `path:line` cite needs a declared base (`kasegi-shokunin/corpus/knowledge/citation-bases.md:9-17`), and range-valid is not semantic support (`kasegi-shokunin/corpus/instruments/anchorcheck.py:7-20`, `:54-56`). These chips are not even range-valid anchors.

Observation. The narrator's search log is not in the files. A and B each have one `Searched the web` line and no query text (A:42, B:42). C has two (C:42, C:55), four visible query lines (C:44, C:46, C:57, C:59), and two collapsed tails at C:48 and C:61. Those tails are U+2068, `10`, U+2069, space, `more` — a widget marker, not ten recoverable queries. The count "10" is not a result count.

Inference. `research/README.md:8` ("9/8/10 web searches each") is an index claim about a log the exports do not contain. It is not a sweep denominator. Unknown: whether any live chat continued past these cuts, and whether a burner session still holds the missing queries. Not checked. A CDP read of port 9222 would be a live target; this round does not approve one (`chousa-shokunin/PROVINCE.md:10-12`).

## What the fleet already enforces

Observation. kagi's gate exists because uncommanded claims were the measured defect: round-10's 62 claims were hand-adjudicated, including 4 `UNCHECKABLE`, "because no claim carried a command" (`kagi-shokunin/corpus/claim-ledger.sh:4-10`). A claim row is `command`, `expect`, `exit` (`claim-ledger.sh:24-30`). The round-5 aggregator recorded a negative as checkable only with its sweep: "no rotate/revoke/refresh verb exists confirmed by CLI dispatch sweep (negative claim carries its sweep)" (`kagi-shokunin/corpus/lessons/round-5-aggregator-audit.md:45-46`).

Observation. chousa already states the same duty and does not yet define the record: "A negative claim carries its search sweep" (`chousa-shokunin/SKILL.md:44`); a claim needs a measured anchor (`chousa-shokunin/corpus/QUALITY.md:2-3`). `tools/research-gate.sh` is named at `SKILL.md:50-53` and is not on disk in this lane. This report does not invent that script.

Observation. A claim-ledger row cannot be the classifying sweep below. First token must be `bash|grep|sha256sum|wc|test`, and the command may contain no shell metacharacters (`claim-ledger.sh:158-174`). A classifying sweep is not a raw match. Parking the external half in kagi's by-hand bin would also be false: the four classes are `control-plane-scratch|opencode-internal|interactive-only|vault-refusal` (`claim-ledger.sh:59-62`). An unapproved web search is none of those.

## Revision pins

Swept at this reading. `sha256sum` from the fleet root. `wc -l` counts newlines, not logical lines. The three exports do not end in a newline, so a sweep bounded by `wc -l` drops the last logical line of each (`Web search`). That line is chrome, not a source. The bound is still part of the sweep.

| Path | sha256 | newlines (`wc -l`) | logical lines |
|---|---|---|---|
| `research/README.md` | `5199b23b4be6b59482295fac0f1de4ea1b04842afbfcb283ce01ce69b8e33e86` | 17 | 17 |
| `research/deep-research-2026-09-28/A-shokunin-tradition.md` | `9033857d4625555c7b778dfad6df80e3e1b24ed8bffa3fee2fd445b9c5540b85` | 109 | 110 |
| `research/deep-research-2026-09-28/B-multiagent-knowledge.md` | `6d8dbddd3e2d2f47dcb153c5a3347cc6321db4afc72cf07da40f0f7fe5022006` | 100 | 101 |
| `research/deep-research-2026-09-28/C-rank-taxonomy.md` | `e48fe70ff92055c217ac6ca6ce68e403aa5689fee8717f3bd0ccf5badc92321b` | 154 | 155 |

Canon snapshot used for NCS-1, not a lock. `chousa-shokunin/MINT.md` was appended during this survey (integration guards). Pin at the classifying read: `a7ac5af41d231bd9394acdd19d48f13895ebb82240bc9bfe5ffd33754e8f6a98`, 98 newlines. `PROTOCOL.md` `77a0fd73d360d7ec0a210358ce80f2fdf37c153d06b16cfbc203befaeb67c933`. `MANIFEST.json` `c784fbd40f86ab07a71d0e93f8c957e9048c51820dfd338e41a0249ce7398fa4`. A later append is outside this sweep.

## Runner

Observation. In this session's shell, `type grep` reported a builtin whose display truncates lines and prints `grep: N matches`. `bash -c 'type grep'` resolves `grep` to `/usr/bin/grep`, GNU grep 3.12-modified. Exit codes agreed on the commands compared. Commands below name `/usr/bin/grep` so the stdout is the host tool. claim-ledger cannot name that path: first token `/usr/bin/grep` is a first-token refusal under `claim-ledger.sh:158-170`. A gate row of bare `grep` is the bash-script resolution, not this session's builtin. Locale is part of the command. This host's login locale was `LANG=en_US.UTF-8`. Under `LC_ALL=C`, `.` is one byte and misses the claim spelling. See NCS-1.

## NCS-1 — no attestation that jin'i-ryu means "self-legislating school"

Claim, as data, not as a finding. `C-rank-taxonomy.md:109`: "I found no authoritative attestation establishing jin’i-ryū as “self-legislating school.” Romanization without kanji cannot establish a literal meaning."

Same family, not separately swept: A:47 ("I haven’t found evidence that jin’i-ryū is a traditional artisan rank"), A:64 (could not substantiate the spelling as an established artisan rank), C:53 (no support found for that translation). `research/README.md:12` upgrades the family to "`jin'i-ryu` is NOT an attested artisan rank — it's our coined term". That upgrade has no command. It is not the sweep result.

The claim is narrator-epistemic ("I found no"). Making that sentence checkable needs the search the narrator ran. Making the historical sentence checkable ("no authoritative source attests this") needs a declared source set. Those are different sweeps. Neither is the raw presence of the letters `jin`.

### Hit predicate

A hit is a line that positively binds a spelling of this token to "self-legislating school", or that names a source as establishing the spelling as an artisan rank.

Not a hit:

- the user prompt that asks for that translation (`C:35`, `A:35`)
- the narrator's own denial (`C:53`, `C:107`, `C:109`, `A:47`, `A:64`)
- a distinction that separates 人為 / 自己立法 / 自律 from the token (`C:113-120`, `C:124`) — those lines are the narrator's argument, and their dictionary chips are unverified
- a fleet lifecycle definition that glosses the token as self-iterating (`PROTOCOL.md:21`)
- an in-flight fixture sentence. Observed, not used as evidence: a sibling draft in this wave's `members/` contains the invented line "The traditional ladder ends at jin'i-ryū, the self-legislating school rank." The file was still being written. Excluded from the universe. A repo-wide grep during this wave returns it.

### Orthography, measured

The claim spelling is not the fleet spelling.

| Form | Where | Stable under `LC_ALL=C`? |
|---|---|---|
| `jin'i-ryu` U+0027, no macron | prompts A:35 and C:35; query C:59; README:12; `PROTOCOL.md:21` | yes, if the needle is this exact ASCII |
| `jin’i-ryū` U+2019 and U+016B | A:47, A:52, C:53, C:109, C:124 | only if the needle is these exact UTF-8 bytes (`grep -F`) |
| `Jin’i-ryū` capital J | A:64, C:107 | same, and a case-sensitive needle misses it |
| `人為流` | absent from the four research files | yes (`grep -F`) |
| `人為`, `自己立法`, `自律流` | C:57, C:116, C:118, C:120, C:124 | present, and they are different words |

Commands run:

```
# UTF-8 locale (this host default). Case-sensitive dot. Misses capital Jin.
/usr/bin/grep -n -E 'jin.i-ry' research/deep-research-2026-09-28/A-shokunin-tradition.md
# hits: 35, 47, 52. Not 64. exit 0

# Same pattern, C locale. Dot is one byte. U+2019 is three bytes. The claim lines vanish.
LC_ALL=C /usr/bin/grep -n -i -E 'jin.i-ry' research/deep-research-2026-09-28/A-shokunin-tradition.md
# hit: 35 only. exit 0

# Exact curly needle, case-sensitive. Misses A:64 and C:107.
/usr/bin/grep -c -F 'jin’i-ryū' \
  research/deep-research-2026-09-28/A-shokunin-tradition.md \
  research/deep-research-2026-09-28/C-rank-taxonomy.md
# A:2  C:3  exit 0

# The compound that would be a Japanese spelling of the token.
LC_ALL=C /usr/bin/grep -c -F '人為流' \
  research/deep-research-2026-09-28/A-shokunin-tradition.md \
  research/deep-research-2026-09-28/B-multiagent-knowledge.md \
  research/deep-research-2026-09-28/C-rank-taxonomy.md \
  research/README.md
# 0 on each of the four files. exit 1
```

Runnable locally: yes. Run: yes.

A C-locale dot-pattern does not return exit 1. It returns a false narrowing: only the ASCII prompt. An absence sweep that does not pin locale and case is not a sweep of this claim.

### Universe L1 — the four research files

Closed. Pins above. Runnable: yes. Run: yes.

Result, classified, not raw:

- Zero lines are a positive attestation. The curly hits are the denial, the ladder denial (A:52), or the coinage caution (C:124).
- `人為流` is absent (exit 1). That is an observation about these four files. It is not an observation about Japanese.
- C:59 is the query string `"jin'i-ryu"`, not a result. No result count, no result URL, no "0 hits" line from the search tool.

What this supports: the survey corpus, at these hashes, does not contain an authoritative attestation of that translation.

What this does not support: that the narrator searched a sufficient set, or that no such attestation exists. The search log that would support the narrator-epistemic sentence is not in the file.

What would refute L1: a line inside these four files that names a source and states the binding. None found. Internal refutation: not met.

### Universe L2 — live canon root, not the 27G tree

Closed set: `PROTOCOL.md`, `MANIFEST.json`, `ROADMAP.md`, and every `SKILL.md` / `PROVINCE.md` / `MINT.md` at depth at most 2. Produced by `find -maxdepth 2` of those names. 44 files, 0 missing, at the MINT pin above.

Rejected universe, kept: a walk of the fleet root. `du -sh` of the root reported 27G. An unbounded walk in this session did not finish. `.ufo/` holds frozen MANIFEST copies and this wave's drafts. Counting those as attestations would be a false hit. Not swept, and not claimed empty.

Command run (UTF-8, case-insensitive, so it sees both apostrophes). Exit 0. Seven lines:

| Line | Class | Why it is not a hit |
|---|---|---|
| `PROTOCOL.md:21` | operational gloss | `jin'i-ryu (self-iterating)`. Not "self-legislating school". Not a cited Japanese source. |
| `PROTOCOL.md:35` | operational gloss | promotion rule, "iterate on itself" |
| `PROTOCOL.md:76` | operational gloss | gate text, falsifiable improvement |
| `MANIFEST.json:111` | operational gloss | `jin'i-ryu on self-iteration capability` |
| `chousa-shokunin/MINT.md:38` | guard against the README upgrade | says export A did not substantiate the spelling. Quotes the absence. Does not attest it. |
| `chousa-shokunin/MINT.md:48` | guard | "Do not relabel `jin'i-ryu`" |
| `chousa-shokunin/MINT.md:92` | guard | "Do not amend `PROTOCOL.md:21`" |

No other depth-2 lane `SKILL.md` / `PROVINCE.md` / `MINT.md` matched. `ROADMAP.md` did not match. The command is the `/usr/bin/grep -n -i -E 'jin.i-ry|self-legislat'` invocation over that explicit 44-file list, from the fleet root.

What this supports: at this snapshot, the live canon does not attest the translation, and it does use the ASCII token as a system rank. Those are different facts. The second does not prove the first, and it does not prove the token is a traditional rank.

What would refute L2: a canon line, inside the 44-file set at this pin, that states the historical binding. Not found.

### Universe X1 — the sweep that would actually decide the claim

Not runnable this round. Not run. Proposal, for an approval table this report does not own.

Universe, if a window is approved: a named dictionary and catalog set, not "the web" and not the narrator's unrecovered queries. Minimum needles: `人為流`, the romaji forms above, and the phrase "self-legislating school" paired with a school-name reading. The export already asserts that 人為, 自己立法, and 自律 are different words (`C:113-120`). Those assertions are chips (`コトバンク`, `+4`). An external window would re-derive them; it would not treat C as the dictionary.

Hit: a located entry that defines one spelling as "self-legislating school" or as an established artisan rank, with a recoverable identifier (dictionary headword, catalog id, URL captured in the window). A hit refutes both the historical claim and the README upgrade.

Not a hit: an entry for 人為 alone, an entry for 自己立法 as Kantian self-legislation, a modern coinage labeled as coinage (`C:124` proposes `自律流` and says to label it as coinage), or this fleet's `PROTOCOL.md:21`.

Why it cannot be run from the artifact even after approval: there is no URL to open. `adachi-hanga.com` and `コトバンク` are not locators. Recovering "the sources searched" is a different approval (re-open a session this dump does not identify). Unknown whether that session still exists. README:6-8's burner-Chrome / CDP 9222 / "fired by L0" / "no Deep Research entitlement" story is not in the exports. Not used here as fact.

Local stand-in that must not be substituted: `grep -F` of `人為流`, exit 1. That command is a legal shape for a claim-ledger row (first token `grep`, no metacharacters) and would pass an exit-1 expectation. Accepting that pass as "the historical claim holds" would launder a four-file zero into a world-absence. Rejected as a verdict. Kept as the local half only.

## NCS-2 — no universal sacred number of years, and no common final examination

Claim, as data. `A-shokunin-tradition.md:86`: "There is no universal sacred number of years or common final examination."

Two predicates in one sentence. A sweep that collapses them, or that greps `examination` across all three exports, is the wrong sweep.

### Hit predicates

H-years. A statement that one duration binds apprenticeship across crafts (a universal, sacred, or common term). Not a hit: one workshop's custom of seven, five, or nine years. Variance among workshops does not by itself prove universality is absent, and a shared number among three workshops would not prove it is present. Only a universality statement, or a source outside the file that establishes a cross-craft rule, decides it.

H-exam. A statement that one final examination is the common gate to artisan independence across trades. Not a hit: a martial dan examination, an agent-grading proposal, or the word `exam` inside another word.

### Universe L3 — file A only

Closed. Pin above. Runnable: yes. Run: yes.

```
/usr/bin/grep -n -E -i 'years|examination|試験' \
  research/deep-research-2026-09-28/A-shokunin-tradition.md
```

Exit 0. Four lines:

| Line | Text role |
|---|---|
| A:80 | "approximately seven years for carvers and five for printers" — one account, two trades, two durations. Chip, not a quote. |
| A:81 | "nine years" — one carver's career, Taitō City interview, no locator |
| A:82 | "within five years" — one association program; the same sentence says the timetable reflects financial support |
| A:86 | the absence sentence itself |

No `試験` in A. No line in A states a universal duration or names a common artisan examination as existing.

What this supports: internal consistency. A does not contradict A:86. The three stated durations are not one number (7, 5, 9, 5).

What this does not support: the historical negative. The three examples are unverified chips (`adachi-hanga.com` and `+2` at A:83-84). A local zero cannot promote them into a survey of "the tradition". The narrator's argument treats three particulars as the sweep. They are not a closed universe of crafts.

What would refute L3: a sentence in A that states one duration or one exam as cross-craft law. Not found.

Truncation bound, so this zero is not over-read. Prompt terms `hoard`, `ikigai`, `kodawari`, and `finishes` occur only on A:35. The body starts question (1) and stops at the chrome at A:90. Inference that the narrator found nothing on questions (2)-(4) is not licensed. Unknown whether the live answer continued. Same shape in B: `hallucinat` only on B:35; `credit assignment` on B:35 and the progress line B:40, not in an answered section. C: `inflation` only on C:35. Absence of those answers is a property of the dump, not a negative finding about the subject.

### Rejected cross-file sweeps, kept

1. `examination` across C. Command run:

```
/usr/bin/grep -n -E -i 'examination' research/deep-research-2026-09-28/C-rank-taxonomy.md
```

Exit 0. C:92 (Japan Karate Association kyu/dan examinations by authorized examiners) and C:105 (use kyu/dan for agents only if you build domain examinations). Wrong domain. C:92 would refute a claim that Japanese institutions never examine anyone. It does not refute A:86's artisan-independence exam. A gate that counted C:92 as a hit would false-refute NCS-2.

2. Unanchored `five|seven|nine` across A and B. Command run. Exit 0. A:80-82 are the duration lines. B:57 is "Track five axes separately" — not a year. A token sweep without a unit is not H-years.

3. Treating A:80's seven years as a refutation of "no universal number". Rejected. A particular is not a universal. It would refute a different sentence ("nobody trains for seven years"), which A does not claim.

### Universe X2 — the sweep that would decide A:86

Not runnable. Not run. Proposal.

Universe, if approved: the three accounts named in A:80-82, once locators exist, plus a declared set of craft-association rules large enough that "no common rule" is a statement about that set, not about three sentences. The set has to be written down before the search. Adding sources until a counterexample appears, or stopping at three because they differ, is not a sweep.

H-years hit: a located rule that one duration is the apprenticeship term across crafts, or a source that states there is such a term. A hit refutes the first clause.

H-exam hit: a located rule naming one final examination as the common independence gate across artisan trades. A hit refutes the second clause. JKA, kendo shogo, and Nihon Ki-in promotions (C:89-100) stay out of this universe. They are a different institution class, and their chips are also unverified.

Not runnable locally because the locators are not in the file. `+2` at A:84 is an omitted source widget, same class as C's collapsed `10 more`. The two omitted sources are unknown. They might be the Taito interview and the Echigo association, or they might not. Not inferred.

Local stand-in that must not be substituted: the four-line grep of A. It checks internal consistency only.

## Rejected claims, not swept

Kept, with the reason, so a later landing does not absorb them silently.

1. B:59, "their benchmark results do not establish indefinite, reliable self-improvement." Model-quality / evaluation claim. chousa refuses that province (`chousa-shokunin/SKILL.md:38`, `PROVINCE.md:10-11`). Not swept. The ACE numerals at B:79 are the same refusal: a case-study figure is not a method rule, and this member does not re-derive it.

2. C:65, "There is no traditional Japanese four-rank ladder that precisely means created, corpus-verified, safely self-improving, agent-producing." Same shape as NCS-2 (universal absence of a structure) and not given a second full sweep. Partial observation only, so it is not a result: `PROTOCOL.md:21` is a four-step system ladder (mint, shonen, shokunin, jin'i-ryu) and does not mean those four agent states. Sibling mint is a separate permission at `PROTOCOL.md:37-53`, not a rank. That line is a false friend, not a refutation and not support. The external half would be an approval-window sweep of craft rank lists. Not run.

3. README:12 as an admitted correction. It is an index restatement of an uncommanded narrator absence. Copying it into a corpus note would mark a coined rank as verified. The local sweeps do not verify the coinage. They only fail to find an attestation in the closed sets above.

4. Re-opening CDP 9222, or any browser cache, to recover the search log. Live target, no approval, and the README provenance that names the port is not in the dumps. Not run.

## Record a gate could check

Proposal, not admitted. A negative-claim row needs fields a claim-ledger TSV row does not have:

1. Claim quote and `path:line`, plus the sha256 of that file.
2. Which sentence is being tested: narrator-epistemic, or historical.
3. Universe: explicit path list or an approved source list. Not "the repo". Not "the web".
4. Locale and orthography set. For NCS-1 the set is the three latin forms plus `人為流`. A C-locale dot-pattern is a failed sweep, not a zero.
5. Hit predicate, including the excluded class (prompt, denial, operational gloss, other domain, in-flight fixture).
6. Command and exit, run with `/usr/bin/grep` or a bash script whose `grep` is GNU grep. Raw exit 1 is the local half only.
7. Saturation: what was not searched. For both claims here, the external half is unsaturated, and the search log is absent rather than empty.
8. Status words kept apart: observation, inference, unknown. A zero in L1/L3 is an observation. "The tradition has no such rank / no such exam" would be an inference these sweeps do not license.

`bash tools/ncs-sweep.sh` could be a claim-ledger row if the script exists and the row has no metacharacters (`claim-ledger.sh:172-174` forbids `bash -c`). The script does not exist. Writing it was not this item.

## Result

| Id | Claim | Local sweep | Runnable | Run | Local result | Decides the historical claim? |
|---|---|---|---|---|---|---|
| NCS-1 | C:109, no attestation that the token means "self-legislating school" | L1 four research files; L2 44 canon files at the MINT pin | yes | yes | no attestation line; `人為流` absent (exit 1); canon hits are glosses and guards | no |
| NCS-1 | same | X1 named dictionaries | no | no | proposal only | would, if a hit or a real zero on that set |
| NCS-2 | A:86, no universal year-count and no common artisan final exam | L3 file A only, two predicates | yes | yes | no internal counterexample; stated durations 7, 5, 9, 5 | no |
| NCS-2 | same | X2 located craft rules, once locators exist | no | no | proposal only | would, per clause |

Observation. Both narrator sentences are consistent with the closed local sets that were actually searched.

Inference. They are not yet checkable as facts about Japanese practice. The missing piece is a recorded universe, not a stronger adjective.

Unknown. The unrecovered search results, the sources behind `+2` / `+4` / `+5` / `コトバンク`, and whether the live answers continued past the chrome. Those unknowns are why a local exit 1 must not be entered as a verified absence.
