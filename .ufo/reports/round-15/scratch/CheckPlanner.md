# Round-15 credential-hygiene checklist matrix

IDs follow document order: E1–E8 under **Evidence production**, then H1–H8 under **Handler operation**. Lead phrases are verbatim and each is under 90 characters. “Expected last line” is the checklist ERE; “observed last line” is the exact final non-empty stdout line from the command run for that row.

## Runnable

| ID | SKILL.md lead phrase (line) | Exact command | Expected exit | Expected last line (ERE) | Observed exit / last stdout line | Why this is a direct check |
|---|---|---|---:|---|---|---|
| H3 | ``Keep `config_overlay` (`opencode.json`) intact:`` (434) | `bash corpus/drift-pins.sh` | 0 | `^DRIFT_PINS: CLEAN \(files=15 symbols=20\)$` | exit 0; `DRIFT_PINS: CLEAN (files=15 symbols=20)` | Pins the overlay and global config source files and their declared symbols. This is an input-integrity check only; it does not claim to recompute OpenCode’s merged runtime config. |
| H4 | ``Never widen `janitor` agent permissions`` (435) | `bash corpus/drift-pins.sh` | 0 | `^DRIFT_PINS: CLEAN \(files=15 symbols=20\)$` | exit 0; `DRIFT_PINS: CLEAN (files=15 symbols=20)` | The host agent file and auth-tool source are in the drift baseline, including the wildcard-deny symbol pin; changes to the pinned source fail this gate. |
| H7 | ``Run `corpus/transcript-scan.sh` after any request that carried`` (440) | `bash corpus/transcript-scan.sh` | 1 (current pinned observation) | `^TRANSCRIPT_SCAN: HITS=2 \(cells=888 patterns=32\+5 warns=2 schema-absent=0\) db=/home/vgpnk/\.local/state/the-janitor/xdg-data/opencode/opencode\.db$` | exit 1; `TRANSCRIPT_SCAN: HITS=2 (cells=888 patterns=32+5 warns=2 schema-absent=0) db=/home/vgpnk/.local/state/the-janitor/xdg-data/opencode/opencode.db` | Runs the exact content-free scan named by the item. The recorded expected exit is the current HITS=2 observation, not a claim that the scan was CLEAN; changed counts/result require review. |

## By-hand

| ID | SKILL.md lead phrase (line) | Class | Unique reason (≥24 chars) |
|---|---|---|---|
| E1 | `Record mechanism and metadata:` (422) | by-hand — authoring-duty | Census and drift gates observe host state, but cannot certify that metadata was recorded accurately in the evidence; the required in-repo citation/stamp check is also disallowed for checklist rows. |
| E2 | `After any intentional host-file change` (423) | by-hand — manual-change | Intentionality, accepted `REPIN`/`MOVED` lines, and the rule against re-pinning in the discovery round depend on a human-reviewed change history. |
| E3 | `Quote command output only when it is metadata-only` (424) | by-hand — authoring-duty | No gate can know which output an operator will quote or inspect every resulting artifact for accidentally included non-metadata. |
| E4 | `refs output:` (425) | by-hand — authoring-duty | Whether reference paths escaped internal use is a property of authored artifacts, not a fact established by running an unrelated gate. |
| E5 | `Before relying on a key inventory` (426) | by-hand — cross-lane | The real inventory-versus-resolver comparison requires the named probe’s `op` execution; checklist rows are forbidden from executing `op`, so its live contract cannot be checked here. |
| E6 | ``Never paste `the-janitor run` output:`` (427) | by-hand — authoring-duty | A gate cannot predict what run output will be pasted or whether an operator mistakes unmasked plain-valued output for safe-to-share text. |
| E7 | `Receipts/checksums bind *bytes*:` (428) | by-hand — authoring-duty | Byte-integrity evidence alone cannot ensure the report says “local receipt integrity only” and avoids provider-attestation or live-access claims. |
| E8 | `Handoffs carry context + receipt *path*;` (429) | by-hand — authoring-duty | Each handoff’s actual context and receipt-path use is authored content; presence of JSON keys cannot certify that its narrative is complete or appropriately bounded. |
| H1 | `One request at a time` (432) | by-hand — runtime-behavior | A safe check cannot establish serialization across concurrent callers. The host measurement places flock in the wrapper rather than `client.py`, and it does not cover direct HTTP callers. |
| H2 | ``After `stop`, expect `AUTH_REQUIRED` on next request`` (433) | by-hand — runtime-behavior | Proving this transition requires a real stop followed by a request and operator re-approval; handler start/stop and auth actions are prohibited for checklist rows. |
| H5 | `CDP port 9222 + musketeer profile are shared with the kake fleet:` (436) | by-hand — operator-scope | Local socket inspection cannot determine the fleet’s profile lease owner; taking or clearing a conflicting lease would cross the other lane’s ownership boundary. |
| H6 | `Never put secret-adjacent text into a request expecting memory-only` (437) | by-hand — authoring-duty | A scan catches only known persisted shapes after submission; it cannot judge arbitrary future request text or the operator’s memory-only expectation before sending. |
| H8 | ``Treat `127.0.0.1:40961` as unauthenticated handler access:`` (444) | by-hand — operator-scope | A local check cannot prove that no process will POST to the socket; testing the password/client mismatch would require changing access configuration or contacting the handler. |

## Decision note

No item is undecided as to class. H1 is deliberately by-hand, but its wording should not be treated as a verified assertion: the supplied host measurement says flock is in the wrapper, not `client.py`, and does not serialize direct HTTP callers. H3’s runnable check is limited to source-pin integrity, not merged-config behavior.

runnable=3 by_hand=13
