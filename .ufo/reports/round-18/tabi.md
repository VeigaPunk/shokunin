# tabi round 18 — early source rechecks, guarded browser execution, routed corrections

## Work performed

Declared claims: **C1 freshness8** — round-specific source-reopen receipts0→51; **C2 operability8** — six finite harness/witness hazards0→6; **C3 calibration9** — five round17 outside-check defects0→5. Freshness and operability each work a lowest non-retired tie; no stagnation waiver. All scalar scores remain unchanged. No exploratory claim or new capability.

- **C1:** Reopened the fixed baseline cohort51 (38 living-URL,12 pinned-URL,1 own-work by the URL classifier), not51 current products or overdue sources. Final receipts retain compressed actual response bodies and recompute raw/compressed SHA, size, decoder, quote offset and exact excerpt. Final classification:41 held,9 drift-superseded,1 own-work, no rejected receipts. The zero baseline means absence of this round's receipt contract, not absence of lifetime source checking. Evidence: `corpus/evidence/round-18/source-recheck/`, `corpus/knowledge/source-recheck-round-18.md` §7–8, final C1 counter/self-test.
- **C2:** Added the hardened successor `scripts/webmcp-invoke-round18.mjs`: signals/abnormal cleanup, in-flight launch termination, private temp ownership, pipe CDPSession instead of a DevTools TCP listener, recorded refused downloads with live byte scans, merged effective feature switches, bounded cleanup and cached executable hashing. The guarded `scripts/freshness-witness.mjs` refuses symbolic witness input on its own path. Final main run retains all11 original scenarios/four controls plus the download case (12/12); six hazard predicates pass. Evidence: `corpus/evidence/round-18/webmcp-invoke/receipt.json`, main `measurements.json`, source note citing S059–S064 and S070.
- **C3:** Closed all five routed defects from `corpus/lessons/round-17-verifier-spotcheck.md:157-165`: corrected six siblings (not seven) in both named historical locations; ran all20 historical gates at actual round17 measured `93bfead1f5f25f584353df3152a60209bbd89a2e`; retained the57-case adjacency self-test receipt; appended S058 with the publisher premise corrected in all its cells; retained seven **new**, successful round17 harness reruns with full digests and artifact bytes. The lost old temporary outputs were not recovered or relabeled. Evidence: round18 lesson `## Corrections`, `corpus/evidence/round-18/routed/`, final C3 counter.
- **Falsification repairs:** Bound the source cohort to B, retained bodies after the forged-HTTP-digest survivor, isolated Git environment/replacement refs, matched StackExchange question/answer identity, bound actual browser PIDs/executable and receipt producer to the executed artifact, and closed the demonstrated C3 prose-count/digest/publisher/replay/argv/recovery-label shapes. Targeted self-tests preserve the finite attack scope; no authenticity/universality claim. Evidence: `.ufo/waves/round-18/w2/{MutC1,MutC2,MutC3,ReviewCounterInputs,ReviewQuality}.md`, final self-test receipts.
- **Source semantics:** S065–S076 supersede unsupported assertions or bad anchors, including attached HEAD, per-API Selenium attribution, inverted historical cleanup semantics, client-versus-protocol event policy, shipment chronology, declarative input validation, canonical Chrome docs, proposal-versus-shipment wording, source-token-versus-runtime inference, response variance and PDF page numbers. Imperative no-inputSchema enforcement is not generalized to declarative forms. Evidence: new rows, lesson `## Gate`, source note §7, `sources/DeclarativeValidation.md` and README correction index.
- **Swarm:** Wave1=70 seats: scout36/executor12/scribe7/reviewer6/connector5/critic2/sentinel1/revenger1. Wave2=80: scout59/reviewer7/executor4/mutation-tester3/sentinel2/critic2/connector2/simplifier1. **150 dispatched L2 seats;150 scoped reports present; no dead workers or replacements.** L1 TabiR18 holds the canonical planner seat; connector seats performed bounded overlap/data walks, not another judge. Wave2's first all80 dispatch was refused at the100-job cap, spawning none; unchanged payload succeeded on retry2 after180s. Its `-2` task-name suffixes are reserved-name effects, not replacement workers. Specs, validation, dispatch attempts, assignments/registries and `.ufo/waves/round-18/final/wave-summary.json` retain evidence.
- **Conformance miss, not hidden:** Wave1 writers used disjoint assigned lane files but not separate writer worktrees, contrary to the stronger addendum isolation contract. Repair writers used private clones; wave2 production was read-only except named evidence/report outputs. Old drafts are explicitly archived build-wave evidence (`drafts/history.json`), not active unfinished instructions. No byte-frozen prior lesson, gate, old harness, PROVINCE or SHONEN was edited.

## Landed changes

Every item is logged under `LOG.md` round18 (`:1042`, final record `:1066`) and the round18 lesson; SCORECARD and SKILL carry the current interpretation.

| Pushed lane commit | Landed content | LOG/evidence tie |
|---|---|---|
| `530f40a9bc3f10436161a2af1ca0fe9bffffc004` | First build integration: source receipts, successor/wrapper, counters, source rows/notes, routed evidence, wave1 | LOG round18 motivation and work items; first-integration history only |
| `c0aff2364b49b21c41669f050e03800138589fa7` | Wave2 attacks/repairs, regenerated retained bodies, final hardened producer/counters, S065–S076 and semantic corrections | LOG final outcome; main code-run measurements and complete harm comparison |
| `01531daf3fa784410db454e4d606488e467a039a` | Frozen evidence checkpoint: main self-test/measurement/tool-identity receipts, final corpus interpretation | LOG/SCORECARD measured checkpoint; all three claims reproduced here |
| `2ec136e78a0d65bee694c1350686a5c4307e1490` | SCORECARD/SKILL/LOG, external-prefix binding manifest, exact-checkpoint23-gate comparison and binding reproduction | LOG final evidence pointers; delivered binding exit0, claims3/bound3 |
| **`df51a0724772e8190445544767248d9f6fca05a7`** | Delivered binding receipt and protected-driver misroot sweep | LOG round18 final evidence closure; no counted input changed, only two receipt files |

Final lane helper state: local=remote=`df51a0724772e8190445544767248d9f6fca05a7`, ahead0/behind0, detached Git HEAD (jj-colocated), tracked0/untracked0. Commits/pushes used only `scripts/hyaku/jj-lane.sh`; these hashes are its `landed` outputs.

## Before → after measurements

B=`2bff864fdfee684ddbcd066cc8e735adaba2735c`; final frozen checkpoint M=`01531daf3fa784410db454e4d606488e467a039a`. Main first ran exact before/after commands at code revision `c0aff2364b49b21c41669f050e03800138589fa7`; then `check-measurement-binding --reproduce` executed all six B/M arms at M and again at `2ec136e78a0d65bee694c1350686a5c4307e1490`, both exit0, claims3/bound3, no findings. The last commit adds only those outside-prefix receipts.

Commands below run from `/home/vgpnk/Projects/shokunin/tabi-shokunin`; `REV` is substituted with B or M:

| Claim / axis | Counting command | Before → after | Verdict |
|---|---|---|---|
| C1 freshness | `node .ufo/waves/round-18/measure-c1.mjs REV` (`c1_rows_rechecked`) | 0/51→51/51; after held41/drift-superseded9/own-work1, rejected[] | improved; scalar8→8 |
| C2 operability | `node .ufo/waves/round-18/measure-c2.mjs REV` (`c2_hazards_closed`) | 0/6→6/6; retained11 original cases+four controls+download case | improved; scalar8→8 |
| C3 calibration | `node .ufo/waves/round-18/measure-c3.mjs REV` (`c3_routed_closed`) | 0/5→5/5; all d1–d5 pass | improved; scalar9→9 |

Every evaluation exit was0; a zero counter exit means evaluated, not all predicates passing. Baseline C2's actual red reasons include fail-on-SIGTERM, SIGINT/watchdog residue, observed browser-owned TCP listeners, duplicate/lost feature flags and missing refusal/wrapper paths—not merely directory absence.

Evidence:
- Full argv, output, exit, producer hashes: `corpus/evidence/round-18/measurements.json` (before arms explicitly B; codeRevision separately recorded).
- Binding manifest: `.ufo/waves/round-18/measurement-binding.json`; receipts `.ufo/waves/round-18/final/binding-at-{checkpoint,delivered}.json`.
- Main self-tests: **C1 38/38, C2 26/26, C3 38/38, wrapper8/8**, exit0; exact receipts under `corpus/evidence/round-18/selftests/`. SHA map: `corpus/evidence/round-18/tool-identities.json`.
- Runtime measured by C2: Chromium154.0.8037.97 (`/usr/lib/chromium/chromium`, SHA256 `95b17db7512c34bf5d78a0d55e0e49719725c73736c47eb0a7a831553c4b330a`), Playwright1.64.0, Node24.21.0; receipt producer matches selected harness. This is build/fixture-scoped, not current stable-product support.
- Causal removal matrix at first integration (`w2/CriticSeparability.md`):51/6/5; remove C1→0/6/5, C2→51/0/5, C3→51/6/0. Final receipts/counter bindings remain separately declared; C2's conservative evidence-directory binding is broader than its actual matching-receipt reads.
- **No harm:** all23 gate exits equal B at the exact measured checkpoint M:22 exit0 plus inherited USER `round_count` exit1 (six user rounds, ten expected). No timeout; faithful fleet sandbox clean before/after. Full streams/argv/producers: `.ufo/waves/round-18/final/harm-at-checkpoint.json`. The earlier full set at the code revision is separately retained as `corpus/evidence/round-18/harm-at-measured.json`; neither is mislabeled as the other.

Binding lives outside `corpus/evidence/`: C2 enumerates/snapshots matching evidence receipts and conservatively declares that prefix, so putting its own changing binding record inside it would invalidate the snapshot. Corpus evidence was frozen before M; final binding receipts/root records are outside all counted prefixes.

## Sources & frontier

Counting command: `node scripts/check-sources.mjs`; source registry counts include historical/superseded rows, not76 active facts.

| Census | Rows | Tier A/B/C | Mined/queued/rejected |
|---|---:|---|---|
| B | 57 | 46/4/7 | 42/8/7 |
| M | 76 | 64/4/8 | 60/8/8 |

Added19 rows:18 tierA mined,1 tierC rejected. S058 corrects S057; S059–S064 are the hardening sources; S065–S076 are wave2 supersessions. All were opened this round; every new row's URL/access date/≤25-word located quote is in lesson `## Gate`. **No existing status/recheck/used-by cells changed**, so there are no undocumented old→new transitions.

Required command at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi
```

- Start stdout: `tabi\tok\t/home/vgpnk/Projects/shokunin/tabi-shokunin/corpus/SOURCES.md`; exit0.
- End stdout: ten `W04 ... duplicate url ... across scopes` warnings for explicit supersessions, followed by `tabi\tok\t/home/vgpnk/Projects/shokunin/tabi-shokunin/corpus/SOURCES.md`; exit0. Full output: `measurements.json` → `runs.sources-census-end`.
- Exact final lane-parser output, in the23-gate receipt: `SOURCES_GATE verdict=clean rows=76 tiers=A:64,B:4,C:8 status=queued:8,mined:60,rejected:8 findings=0 file=corpus/SOURCES.md`.

No row was date-due. The sweep is early source/evidence quality work, not an overdue repair. Both new notes deepen already-held ground; the frontier does not advance by row count. Real-site journeys, agent-side invocation, default-profile work and Chromium152 remain open. Source-only S071 does not assert a new runtime validation capability.

Sibling overlap was scanned by connector seats with pinned pointers (`w1/ConnSiblings.md`, `w2/ConnScope.md`); no sibling-owned files or routes were absorbed. The two tabi round17 L0 questions remain open: the-musketeer CDP lease (filed `ebeb396f7db43c55de2711baa409f8bb9b71147b`) and reach of the CDP ruling to revenger/kama (filed `b6b3b5e42044b7cd7307d1d923ee054bf98eeb43`). No new L0 question was necessary and none was appended.

## Trend verdicts

- **expansion: unchanged** — notes34→36, but source re-verification and harness hardening are on already-held map ground; no new capability. README explicitly preserves the open frontier.
- **quality: improved** — actual retained-body rechecks, twelve source supersessions, bounded cleanup/transport/download repairs, full measured-revision harm evidence and no false/stale assertion left unmarked as current. The fresh C1 field/metadata corrections are not relabeled old captures.
- **discernment: improved** — round17's outside disagreements became explicit corrections and lesson-backed QUALITY33–37; counter-forgery failures further grounded38–39. This does not claim this round's in-lane reviewers are non-authors; its independent closure remains pending.

Limits retained: the guarded wrapper does not prevent direct frozen-CLI calls with HEAD; pipe messages do not expose raw wire numeric error codes; compressed-byte integrity does not authenticate a remote publisher; loopback/temp-profile success grants no real-site approval. USER6/10 and L0 boundaries still block scalar promotion. Depth8 is deliberately deferred—not retired—and is the next-steer priority recorded in SCORECARD.

Tool installs: only SimplifyTools installed **acorn8.19.0, acorn-walk8.3.5, eslint9.39.5**, official npm registry, private `/tmp/r18-ast`, for AST reachability/unused-binding probes (`w2/SimplifyTools.md:30-36`). No global/host/pacman transaction or service restart. L1 resumed under the same identity after the Anthropic429 steer; no duplicate writer identity was started.

Misroot sweep: required `git -C /home/vgpnk/Projects/shokunin status --porcelain` found only driver watchdog/state paths. No lane-authored misroot; protected driver files left untouched. Receipt `.ufo/waves/round-18/final/misroot-sweep.json`. Lane ended clean/pushed; no inherited uncommitted lane work existed at dispatch. The outside round17 verifier lesson remained untouched.

Stale-lane: this one respawn-per-round mission was progressing through committed lane work and both swarms; no other mission of this lane is open. No round19 work was started.

## SHONEN

- [~] Real decision tables/error patterns/checklists with sources — `SKILL.md` round18 browser table/registry and `corpus/knowledge/harness-hardening-round-18.md`; author assessment, no promotion claimed.
- [~] End-to-end domain execution logged — final12-case/four-control loopback receipt, main C2 measurement, `LOG.md` round18; not real-site authority.
- [~] Executable without oral context — exact CLIs, producer/body/counter identities, self-test receipts and checkpoint binding reproduction; current non-author execution judgment remains closure-owned.
- [~] No cross-domain bleed — frozen `PROVINCE.md`, unchanged adjacency map, connector reports and the two explicitly open L0 rulings; no bilateral agreement inferred from silence.
