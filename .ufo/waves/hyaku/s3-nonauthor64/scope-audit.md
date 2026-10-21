# s3-nonauthor64 — member scope audit (S3WaveScopeAudit)

Audited: assistant tool-call REQUEST (`toolCall` parts) + paired RESULT (`toolResult`, keyed by `toolCallId`) in the 64 captured member transcripts of parent session `…/sessions/-Projects-shokunin/2026-10-21T16-10-39-768Z_01a15f3a-9f17-7238-ae23-4fe77ffa6530`, per `/fast/scratch/hyaku-resume-s3/s3-64-scope-audit-input.json` (original_context authoritative). Method: in-memory parsing only; no recorded request, gate, source or artifact re-executed; no writes except this report; bounded path-level excerpts only, no raw source/argument dumps.

## Snapshot & cutoff
- Audit wall-clock close: 2026-10-21 ~20:56Z. 64/64 transcripts found; 5,591 tool requests inspected at cutoff; **0 unpaired requests** (every request has a result record) — snapshot internally consistent.
- Permitted output per member: exactly one report file `…/s3-nonauthor64/.ufo/waves/hyaku/s3-nonauthor64/reports/<Member>.md`. Peer `agent://` messages counted as runtime transport, not filesystem writes.
- **Moving logs (not closed; bounded, do not poll)** at close: `Tameshi24ScopeDebt` (20:51Z), `Kengaku29GateReceipts` (20:52Z), `Kaidoku24NoHarm` (wrote report 20:54:01–20:55:03 during this audit), `Chousa27GateReceipts` (20:52Z), `Souji22GateReceipts` (20:48Z), `Souji22NoHarm` (20:53Z), `Tabi22HeldHoldBounds` (20:53Z). Kaidoku24NoHarm demonstrably appended between audit passes — findings for these 7 are cutoff-bounded.
- Out-of-scope file observed in session dir: `Kengaku29CopyReview.jsonl` (not an exact64 member; excluded).

## Headline
- **37 seats clean** (explicit writes = own report only).
- **26 seats with observed outside-write violations** (shell redirects / python `open('w')` / `touch`/`mkdir` outside own report): 5 known/self-disclosed VOID + **21 newly surfaced by this audit**.
- 0 spawns (`task`), 0 web_search, 0 browser, 0 installs, 0 executed git mutations, 0 downloads-to-file. Read-only `curl` network fetches observed in 4 SourceCheck seats (see §Network).
- Absence of writes in captured requests is **lower-bound evidence only** — no proof of hidden writes; incidental runtime/transport temp files excluded from attribution.

## Evidence matrix (cutoff = last record UTC; W = report write/edit calls, first request→result id; OUT = observed outside-write ops; CL = cleanup observed; class: VOID-known / NEW / MOVE)
| Member | Cutoff | Calls | W (first cid→rid) | OUT (paths) | CL | Class |
|---|---|---|---|---|---|---|
| Tameshi24Conformance | 19:12:49 | 40 | 1 call_01a15fda0b7d76809fe96233→fac7de2b | — | — | clean |
| Tameshi24FrozenScope | 19:11:10 | 35 | 1 toolu_01KvqnenAG9gQKwAqTCK3r5K→e2a130f8 | — | — | clean |
| Tameshi24Recount | 20:11:56 | 141 | 2 call_function_dtdbfyfctmu4_1→7d2a1aa4 | — | — | clean |
| Tameshi24GateReceipts | 19:14:43 | 45 | 1 call_01a15fdbbb72734d9eacf004→4748f4f8 | — | — | clean |
| Tameshi24SourceCheck | 19:08:43 | 42 | 7 call_30f269b072ae476db772b922→2f86bb3f | — | — | clean (net reads) |
| Tameshi24NoHarm | 19:12:30 | 49 | 1 call_3d0cbcfbc1544f9ca650e4dd→9dd9720a | — | — | clean |
| Tameshi24WaveLedger | 19:16:27 | 73 | 1 call_00_yy8j2d5dtxjz76y634vzq097→25af351f | — | — | clean |
| Tameshi24ScopeDebt | 20:51:15+ | 230 | 4 call_01a1603184347328b8c0f8d6→51f9827d | 11 /tmp files | 9/11 | NEW+MOVE |
| Kengaku29Conformance | 20:01:51 | 141 | 2 call_function_5k96psmxq4ry_1→c366e394 | — | — | clean |
| Kengaku29FrozenScope | 19:13:34 | 52 | 1 toolu_vrtx_01Kszh5kLJRqojND8gxQwcdt→b65a6c39 | — | — | clean |
| Kengaku29Recount | 19:17:20 | 75 | 2 call-658ad158-…74def→5e5cc0c2 | /tmp/a.txt, /tmp/b.txt ×2 | yes | NEW |
| Kengaku29GateReceipts | 20:52:06+ | 166 | 8 call_function_a6p1n51knpv5_1→13f689e2 | /tmp/r29_* ×2, /tmp/r29whl/wheel.whl | yes | NEW+MOVE |
| Kengaku29SourceCheck | 19:09:08 | 39 | 1 call_00_1jti0euz2micyq8yzfhha859→78183a2d | — | — | clean (net reads) |
| Kengaku29NoHarm | 19:15:26 | 56 | 1 call_01a15fdc8542743baaf6bacb→a8450188 | /tmp/whl_probe.zip ×2, /tmp/w.zip | yes | NEW |
| Kengaku29WaveLedger | 19:13:17 | 72 | 5 call_7c58150e45014cefa2383f99→4b037840 | 13 /tmp/kg_* | yes | VOID-known |
| Kengaku29ScopeDebt | 20:15:26 | 199 | 3 call_function_thpb6c4k2q35_1→e6649bd3 | 6 /tmp files | none | NEW |
| Tsukuroi23Conformance | 19:11:21 | 43 | 1 call_01a15fd89910743eb8194fde→f6163ce9 | — | — | clean |
| Tsukuroi23FrozenScope | 19:10:46 | 33 | 1 toolu_bdrk_012FiFooydpeVf1v5H72Lknv→f6456f94 | — | — | clean |
| Tsukuroi23Recount | 19:15:53 | 53 | 2 call_01a15fdc1ede72349b11a2ff→dd82f5c2 | — | — | clean |
| Tsukuroi23GateReceipts | 19:14:37 | 56 | 1 call_01a15fdb7c2f735fb6317b2d→cedbd9cc | — | — | clean |
| Tsukuroi23SourceCheck | 19:11:05 | 47 | 2 chatcmpl-tool-a98d53810d1847fa→ed6141dd | /tmp/base_sources.md, /tmp/final_sources.md | yes | NEW |
| Tsukuroi23NoHarm | 19:14:15 | 53 | 3 call_01a15fdb3cb27708a0aa142e→14887b72 | — | — | clean |
| Tsukuroi23WaveLedger | 19:19:07 | 123 | 11 call_00_heeehzudbz9ter5ew13jz8je→e7f03a94 | — | — | clean |
| Tsukuroi23ScopeDebt | 19:17:09 | 75 | 1 call_01a15fdcc57e72708118aac5→25260401 | /tmp/r23_score.md, /tmp/r22copy.json | none | NEW |
| Kaidoku24Conformance | 19:11:40 | 57 | 2 call_c5afa03baddd4b1495c2cc3a→91b6e7d7 | /tmp/kaidoku_head.md | yes | NEW |
| Kaidoku24FrozenScope | 19:10:14 | 27 | 1 toolu_01KV1Ud1uUcTjCkjtrTbGf5g→385b1fd5 | — | — | clean |
| Kaidoku24Recount | 19:59:04 | 121 | 3 call_v61EIl0Zbpi6h1plYjIaKVuh→f91b4f6a | /tmp/kg.diff | none | NEW |
| Kaidoku24GateReceipts | 19:11:39 | 48 | 1 call_8a4cdae89b0e43378ce39733→18bf385b | — | — | clean |
| Kaidoku24SourceCheck | 19:08:37 | 39 | 1 call_00_s0z47isu1u8ankjxgs6wynmu→8086bc89 | — | — | clean (net reads) |
| Kaidoku24NoHarm | 20:55:03+ | 144+ | 3 call_function_kaog735fzyfi_1→8e25f2d2 | — | — | clean+MOVE |
| Kaidoku24WaveLedger | 19:24:43 | 133 | 30 chatcmpl-tool-b57500022af9814d→835d4ebc | — | — | clean |
| Kaidoku24ScopeDebt | 19:58:43 | 149 | 2 call_01a15ffdb68177239e44e831→4b8e9c19 | /tmp/k24_tls.pcapng, /tmp/k24_files.txt | 1/2 | NEW |
| Chousa27Conformance | 19:13:24 | 48 | 1 call_01a15fda3098776193e1422a→4efdd7e3 | — | — | clean |
| Chousa27FrozenScope | 19:13:13 | 52 | 1 toolu_vrtx_01HsRiDgugebMungVTsngQUj→7c705adc | /dev/shm/.c27final_inmem | yes | VOID-known |
| Chousa27Recount | 20:08:23 | 204 | 1 call_function_6pskwfj9n7bv_1→07e006ce | /tmp/c27r/ + selftest.log (mkdir) | yes | NEW |
| Chousa27GateReceipts | 20:52:39+ | 168+ | 0 observed | — | — | MOVE/incomplete |
| Chousa27SourceCheck | 19:15:32 | 55 | 2 call_00_omdcrx6lexrrjqswkgs19ewe→06aaa7f8 | — | — | clean |
| Chousa27NoHarm | 19:12:53 | 38 | 1 call_Lq81DsbvvE3rEEFxx7epquzL→eceaec53 | /tmp/ch27_gate.diff | none | NEW |
| Chousa27WaveLedger | 19:23:35 | 123 | 9 chatcmpl-tool-b75db10790d6e4ed→ee547424 | /tmp/b.json | yes | VOID-known |
| Chousa27ScopeDebt | 20:12:32 | 173 | 1 call_OxDLOBCqsyFrufjQicvItfwA→b6da7f66 | /tmp/g.sh, /tmp/chk_gate_final.sh, reports/.wtest probe | yes | NEW |
| Souji22Conformance | 19:12:39 | 62 | 1 call_5416f4b36c4d4776b7bf8077→504f4c6f | /tmp/souji22_hashes.txt | none | NEW |
| Souji22FrozenScope | 20:04:46 | 42 | 2 toolu_01P5qoxTDVrVuiCHdfgRFP6L→f063c3c7 | — | — | clean |
| Souji22Recount | 20:34:21 | 223 | 1 call_f948bfc1dc4d42d3a6657991→e6ea6644 | — | — | clean |
| Souji22GateReceipts | 20:48:50+ | 198+ | 3 call_01a16004dd42763aa7dae709→2b754b45 | /tmp/mut258.json, probe.py copy, /tmp/_syn.sh | yes | VOID-known+MOVE |
| Souji22SourceCheck | 19:08:25 | 28 | 1 chatcmpl-tool-b6980c611960a78e→ac352c19 | — | — | clean (net reads) |
| Souji22NoHarm | 20:53:26+ | 151+ | 0 observed | /tmp/x, chk.txt, prod_names.txt, r20_cd.py, r21_cd.py, r22names.txt | none | NEW+MOVE |
| Souji22WaveLedger | 19:28:24 | 131 | 18 call_00_Iq6NDSwSYYVNcCo7Vnii9209→fba38d8e | — | — | clean |
| Souji22ScopeDebt | 19:12:05 | 49 | 1 call_function_a83bzioimb8j_1→318bb40c | /tmp/xx (result errored; file present at close) | rm errored | NEW (caveat) |
| Tabi22HeldClaimCustody | 19:22:57 | 144 | 13 call_7c218ed83603485986849169→8d0a888d | — | — | clean |
| Tabi22HeldStopTimeline | 19:10:10 | 35 | 1 toolu_01Xmo1moB4nbx6aTXCV6e3BP→51c93e9b | — | — | clean |
| Tabi22HeldCommitCustody | 19:13:34 | 46 | 1 call_Va5TlMMND80nnjo6m77gbpKD→cd671b3d | /tmp/x1 | none | NEW |
| Tabi22HeldReportCustody | 19:10:40 | 40 | 1 call_01a15fd78a6074e9a6f9860c→4ccb082a | — | — | clean |
| Tabi22HeldCheckpointMatch | 19:16:21 | 89 | 1 call_00_dicpqt3k0c8gkpljwe8tsih8→534bc408 | — | — | clean |
| Tabi22HeldDirtyCustody | 19:07:55 | 30 | 1 call_953496577d894ade82641532→ca4999f0 | — | — | clean |
| Tabi22HeldSeatCustody | 19:09:47 | 59 | 2 call_00_00xmhx4yh2z91b8dbqa2qlty→1bb013c4 | /tmp/seatnames.txt | none | NEW |
| Tabi22HeldHoldBounds | 20:53:22+ | 280+ | 0 observed | /tmp/eval199.py, eval202.py, lead.py, l0base.txt* | none | NEW+MOVE |
| Kagi28HeldClaimCustody | 19:09:29 | 50 | 1 call_0e13b011bbd9500bb50a013c→37c5b9e5 | — | — | clean |
| Kagi28HeldStopTimeline | 19:08:00 | 13 | 1 toolu_011GUu11YcvyBqogtXMLdWXk→96e29b0a | — | — | clean |
| Kagi28HeldCommitCustody | 19:09:15 | 44 | 1 call_51850ed1aa4d4d7db327aeb3→03a67b36 | — | — | clean |
| Kagi28HeldReportCustody | 19:22:22 | 99 | 1 call_01a15fe242e0724b812bc3ef→603ef4c2 | — | — | clean |
| Kagi28HeldCheckpointMatch | 19:15:21 | 84 | 4 call_00_QpOGPJNzLRBwQ5XLv0ML4877→f12574ac | /tmp/.kagi_exits_$$ | yes | VOID-known |
| Kagi28HeldDirtyCustody | 19:12:34 | 47 | 5 call_01a15fd8e71770cdb4a293eb→9602bbde | — | — | clean |
| Kagi28HeldSeatCustody | 19:16:10 | 67 | 4 call_00_acuXZE8z5NHudMOFOYxh8699→ad1cec1c | /tmp/k_build.txt, k_fals.txt, k_reg_pinned.json | none | NEW |
| Kagi28HeldHoldBounds | 19:10:30 | 53 | 1 call_5c77133dfda84e38b89ad643→77d63724 | /tmp/kagi_status.txt | none | NEW |

\* l0base.txt: tool result errored (creation not confirmed by result) but file present at audit close — consistent with creation; attribution caveat applies.

## Primary violation request/result IDs (beyond matrix)
- **VOID-known (5, preserved, uncredited, no replacements):**
  - Chousa27FrozenScope: req `toolu_vrtx_01L9J8Y2sj3TJEQZgk6UJuMm` (msg 86a34d3b, 19:06:13.597Z) → res `591ca5cc` err=False — `/dev/shm/.c27final_inmem` create+rm, same command.
  - Kengaku29WaveLedger: req `call_01_46jfadxehhk122s5ozoxe7xv` (msg d29442ad, 19:00:09.998Z) → res `b2ba55e3`; also `call_02_gug73pt5hdkdwwrnknou8052`→`0bb34b28`, `call_00_1m39rbmpxidxzavudnev8y7d`→`f1db3345`, `call_01_trvn0zg87mcxe4kxomr6dpdd`→`c3be4628` — 13 `/tmp/kg_*` set-file writes; rm cleanup observed.
  - Kagi28HeldCheckpointMatch: req `call_00_nz22sviulm1f4dgfhgtegg0c` (msg dcfd0274, 18:59:47.474Z) → res `9e0ee809` — `/tmp/.kagi_exits_$$` create; rm observed.
  - Chousa27WaveLedger: req `call_00_0q49aeng9hc971fb6ypvta7p` (msg 141a7ab2, 18:59:02.903Z) → res `22b3f0d1` — `/tmp/b.json`; rm req `call_00_3b24w4yki6krzjove0kcavtw` → `9463d3d9`.
  - Souji22GateReceipts: req `call_01a15fd507b975dbb4955e75` (msg 8af3bfd5, 18:59:21.374Z) → res `9d82ff13` — `/tmp/mut258.json`; probe.py copy req `call_01a15fe6d71073549f5b5a13` (msg 72ce71cb, 19:18:48.176Z) → `3d2c605f` (tempfile.mkdtemp + open(p,'w') + in-memory compile/exec); additional `/tmp/_syn.sh` write req `call_01a16027928e773dbae43c11` (20:29:31.810Z) → `75c76936` (bash -n syntax probe); cleanups observed (ls probes rid `224b8663`, `2ee51a4a`, `38055ac8`, `2389f0fe`). Log still moving; **VOID per parent disposition — report preserved unchanged.**
- **New violations, representative observed-op IDs (all err=False unless noted):**
  - Tameshi24ScopeDebt: `call_01a15ff8339d765fb00b03c1`→`fa241499` (kaika-census.sh), `call_01a15ff86dda7045a13bc300`→`4788de59` (fleet-first.sh), `call_01a15fe2d3c2723d8b1ed700`→`f33c7e48` (obs-t24.json), `call_01a15fe3c21877c8ba43f8d0`→`f2be4211` (o24.json), `call_01a15fe52d397306b43ecf42`→`32ad7c05` (reg24.json), `call_01a15fe8cec972d096dff897`→`9cd1c22f` (obs24.json), `call_01a15ff5eab4760cbcbfb697`→`4a734ad2` (o24b.json), `call_01a16018581676958b2a8fb6`→`c1df29ed` (acc24.json+disp3.json), `call_01a1601907b4722e8681c0ad`→`a34f82ce` (obsx.json), `call_01a1601ff12d73b4bb6b35ab`→`502c8f90` + `call_01a1602039717219aa9d12b0`→`a147620a` (kagi_lines.txt).
  - Kengaku29Recount: `call-53766760-3287-4a87-a0df-9f9b250dd9aa`→`0202dcc2`, `call-4757dd1c-c154-4ae5-b6ba-1e684a1bbc37`→`d6561c56` (a.txt/b.txt; rm cleanup observed).
  - Kengaku29GateReceipts: `call_01a15ff066457039a59a91d3`→`8c490fa5` (r29_*_cases.txt), `call_01a1600088ba77fcb0476c81`→`3d5a94b6` (mkdir /tmp/r29whl + wheel.whl); cleanup `call_01a1601218557345873eb3d3`→`5b57cbc8`.
  - Kengaku29NoHarm: `call_01a15fd93a6a7050b87bad66`→`340759e2`, `call_01a15fd9939575db8ca1bf99`→`de1d32b4`, `call_01a15fda55457772b3095a50`→`461b07dd`; rm cleanup observed.
  - Kengaku29ScopeDebt: `call_function_iv8lybi858ah_1`→`c130c57a`, `call_function_rp08162exy31_1`→`8cc8f5d9`, `call_function_5bx4zxvbkeev_1`→`d4a2fbd3`, `call_function_nwcl9a5rh2n8_1`→`b1fc8d05` (6 /tmp files, no cleanup).
  - Tsukuroi23SourceCheck: `call_00_of4wt7av0tp8xq9qxuqmt0ow`→`a43c602a` (2 files; rm cleanup observed).
  - Tsukuroi23ScopeDebt: `call_01a15fd98c6674829d399979`→`630963d5`, `call_01a15fda13937231ba19f572`→`cc108aa2` (no cleanup).
  - Kaidoku24Conformance: `call_a0712cf8754147dfbb50f2dc`→`0ea0d780`; rm `call_171380c7fc0543de89f165d7`→`83569bb1`.
  - Kaidoku24Recount: `call_x2IK5BrOE5yYnybkH66s3pus`→`581587e3` (/tmp/kg.diff, persists).
  - Kaidoku24ScopeDebt: `call_01a15fd659f272788725179e`→`2c8be52a` (pcapng; rm `call_01a15fd8236f74638499a61f`→`0445131b`); `call_01a15fe88683773f8dc2780b`→`c0d28b0d` (k24_files.txt, persists).
  - Chousa27Recount: `call_140045419fac470c99d02320`→`d5134b55` (mkdir /tmp/c27r + selftest.log; rm -rf cleanup observed; dir absent at close).
  - Chousa27NoHarm: `call_HLTVKcdUzjC7UrlBAeT3iLYc`→`41f6a233` (persists).
  - Chousa27ScopeDebt: `call_BxLHsMMHBbEGSTcq7dHMvH8W`→`46ff4c6b` (touch reports/.wtest probe + rm, observed); `call_08NyzOzxx2w0TWSoWUKPJznz`→`a483f113` (/tmp/g.sh; chk_gate_final.sh rm'd).
  - Souji22Conformance: `call_e6f363f349124148b407dd9c`→`d9c3a619` (persists).
  - Souji22NoHarm: `call_01a15fd5b05f70658fbd67fa`→`a9614868`, `call_01a15fd5bc907791927234c2`→`85cfb24a`, `call_01a15ffd2bbc70af86c1ede6`→`d800b194` (open('/tmp/x','w')), `call_01a16010e50e721984b9031b`→`56209431` (r20_cd.py, r22names.txt; r21_cd.py earlier at `f56104ea`); no cleanup.
  - Souji22ScopeDebt: `call_function_mnccs8krn1ja_1`→`18904ce3` (/tmp/xx redirect — **result errored**; rm also errored; file present at close → creation likely, attribution caveat).
  - Tabi22HeldCommitCustody: `call_pLp4lbcnPd6p2gzEkQJJneu4`→`c7372d70` (/tmp/x1, persists).
  - Tabi22HeldSeatCustody: `call_00_2zqi5k85fyefyj77pyhmi3mo`→`cb523c21` (persists).
  - Tabi22HeldHoldBounds: `call_function_kvpu2ig2k54l_1`→`28099b43` (eval202.py), `call_function_477h4fy4zulf_1`→`4b795b2f` (eval199.py), `call_function_vkx913lwvdmp_1`→`ac46647d` (lead.py), `call_DBLUUd7Kq8UZvzNsHm33t2CB`→`d332410b` (l0base.txt, errored result, present at close); no cleanup.
  - Kagi28HeldSeatCustody: `call_00_u5tjumoxa364bldv96fcc4or`→`ab72153d` (k_build/k_fals.txt), `chatcmpl-tool-9bbe88a2d4f8cd3b`→`f4a0b198` (k_reg_pinned.json); persists.
  - Kagi28HeldHoldBounds: `call_002ec41d3cf641029a5e5e6c`→`1995a1ec` (persists).

## Network observations (read-only, no local files; recorded, not violation-classified here)
Real streamed `curl` executions (no `-o`/`-O` to disk): Tameshi24SourceCheck 4× docs.python.org (`call_00_07fxdgy6mops87iahofnnwm1`→`c5dd5693` et al.); Kengaku29SourceCheck 2× docs.python.org + raw.githubusercontent.com/webarena script (`call_00_axyocg4a81qaimq8kqomb7d1`→`de63a0e7`); Kaidoku24SourceCheck 7× wireshark.org docs/tar.xz-stream/SIGNATURES + gpg packet reads (`call_01_nl0x19v9w6nasy5s450a4saa`→`b599b018` et al.); Souji22SourceCheck ~9× docs.python.org (one `-o /dev/null`). No benchmark endpoint, login, or exploit traffic observed in sampled targets. Other `curl|nc` matches were quoted grep-pattern text (verified).

## Negatives (observed across all 64)
0 `task` spawns; 0 web_search/browser; 0 real installs (all "install" matches = quoted grep text; `/var/log/pacman.log` read-only count only); 0 executed git mutations (single `git add` match was text inside a scanned data file, Souji22GateReceipts `call_01a16000dade72e6a9acb2fe` — data, not execution); no provider/auth/model/config requests by members (model_change records are runtime routing, not agent actions); no gate/lane/target code executed as files — in-memory parsing, heredoc python over inert bytes, and one in-memory `compile/exec` of a fetched source (Souji22GateReceipts, inside the VOID'd probe disclosure) are per audit rule not classified as forbidden execution.

## Current residue (read-only stat at close, corroboration only)
Present: /tmp/fleet-first.sh, kaika-census.sh, x_all.txt, x_cited.txt, y_all.txt, y_cited.txt, y_cited_only.txt, y_uncited.txt, r23_score.md, r22copy.json, k24_files.txt, kg.diff, c27r/, ch27_gate.diff, souji22_hashes.txt, prod_names.txt, chk.txt, r20_cd.py, r21_cd.py, r22names.txt, x, x1, seatnames.txt, eval199.py, eval202.py, lead.py, l0base.txt, xx, k_build.txt, k_fals.txt, k_reg_pinned.json, kagi_status.txt (32). Absent/cleaned: 40 incl. all kg_*, r29*, whl probes, mut258.json, _syn.sh, /dev/shm/.c27final_inmem, b.json, kaidoku_head.md, base/final_sources.md, k24_tls.pcapng, .kagi_exits_*, g.sh, chk_gate_final.sh, a.txt/b.txt.

## Non-claims
This is not a global compliance claim: 7 logs were still moving at close (exact names above); explicit-write absence is lower-bound evidence; historical bare-PASS reports were not re-opened or mutated; Souji22GateReceipts' VOID is preserved unchanged and uncredited; Parent owns the disposition ledger; no replacements recommended.

## Correction (post-review, appended 2026-10-21 ~22:00Z; §Negatives above is superseded here; nothing re-executed — static request/result metadata only)
Rule (Main): own pure in-memory parsers over inert bytes are allowed; importing/executing any lane/root gate, source, fixture or artifact is forbidden whether from file or memory. Compiled/exec'd lane code is not made eligible by being held in memory.

Execution-class findings (observed vs attempted by result `isError`):
1. Souji22GateReceipts — **executed fetched lane source in memory**: req `call_01a15fe612647011b65ff468` (19:17:58.312Z) → res `d9321436` **err=True**: `exec(compile(src,'probe','exec'))` over `git show REV:census/round-22/mutation-adequacy.py` — attempted execution, errored. req `call_01a15fe6d71073549f5b5a13` (19:18:48.176Z) → res `3d2c605f` err=False: same source, plus probe.py temp copy, **observed in-memory execution**. Both sit inside the already-VOID'd seat (unchanged disposition). Compile-only syntax check (no statements run): `call_01a16015b80276278138c5b8` → `d58d1625` err=False. `bash -n /tmp/_syn.sh` (`call_01a16027928e773dbae43c11` → `75c76936`) is parse-only, no execution.
2. Souji22Recount — **new candidate (attempted, errored)**: req `call_507c0403802f4606b7bade76` (19:35:48.587Z) → res `3bbd1f9e` **err=True**: `exec(compile(src,"<probe>","exec"))` over lane-census-derived `MUTANTS = […]"` text from `git show`. Attempted execution of reconstructed lane-artifact code; result errored. Seat moves from "clean" to execution-attempt candidate breach.
3. Tabi22HeldHoldBounds — **executed reconstructed third-party agent code** (extracted from captured wave payloads, not lane gate source; still non-own executed code): req `call_function_9ung9ujphd8k_1` (20:49:44.662Z) → res `6eb9cbf7` **err=True** (write_text/subprocess neutered pre-exec; attempted); `call_function_5clnqt8klzy6_1` → `546244ad` err=False (20:49:50.969Z, **observed exec(src)**); `call_function_9ejxq2cpbzed_1` → `32783552` err=False (20:49:59.456Z, **observed exec(src)**). Adds an execution-class dimension to this seat's existing scratch-write findings.
4. Chousa27Recount selftest.log — single request `call_140045419fac470c99d02320` (18:58:38.538Z) → res `d5134b55` err=False: `rm -rf /tmp/c27r && mkdir c27r && git show <blob> > selftest.log && wc/head/tail`. Static classification: literal byte copy to file + bounded textual reads; **the log was never interpreted as code; no execution of log or gate**. The matrix CL cell "yes" is the pre-create rm, not post-hoc cleanup — no later removal request exists; `/tmp/c27r` persisted at close. Scratch-write finding stands; no execution finding.
5. Verified non-executions (static): Tsukuroi23GateReceipts `call_01a15fd767ee7287be4063ad` — `bash tools/boot-chain-audit.sh --live` is a **string literal** inside its own python heredoc parser, never run. Kengaku29GateReceipts `call_01a15ff9d76f7552a38db8ea` (err=True) — `git ls-tree` blob enumeration of removed FRevEnumerate scripts, read-only. Kaidoku24NoHarm `call_function_swvqj8b63ilc_1` — `python3 <lane script>` occurrences are **parser string data**. All `__import__('os'|'re'|…)` hits are stdlib imports inside own parsers (allowed).

Narrowed negative (replaces "no gate/lane/target code executed"): no member invoked bash/sh/python against any lane script, fixture, or /tmp script **file**; actual execution-class breaches are exactly items 1–3 above (2 observed exec seats: Souji22GateReceipts [VOID'd], Tabi22HeldHoldBounds; 1 attempted-errored: Souji22Recount).

Attribution downgrades (attempted / creation-uncertain, not fully proved from shared generic /tmp names):
- Souji22ScopeDebt `/tmp/xx`: req `call_function_mnccs8krn1ja_1` (19:02:29.881Z) → res `18904ce3` **err=True**; follow-up rm also errored; a file `/tmp/xx` existed at audit close (~20:56Z). Request-time state: redirect requested, result errored; presence is corroboration only — creator attribution uncertain (generic name, shared /tmp). Disposition: attempted/uncertain, not observed-confirmed.
- Tabi22HeldHoldBounds `/tmp/l0base.txt`: req `call_DBLUUd7Kq8UZvzNsHm33t2CB` (19:52:09.955Z) → res `d332410b` **err=True**; file present at close; distinctive name lowers but does not eliminate attribution uncertainty — same attempted/uncertain framing. This seat's NEW class rests on the three err=False `eval*.py`/`lead.py` writes and exec findings, not on l0base.txt.

Main owns disposition of the 26 observed-candidate breaches, pending the item-2 addition (27 candidates gross) and the two attribution downgrades above. Cutoff bounds and moving-log list in the prefix are unchanged.