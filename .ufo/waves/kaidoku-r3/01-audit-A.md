<!-- r3 audit lane 01 — re-verification of round-2 corpus entries by re-running their own verify commands. Audit date: 2026-10-13 (same day as r2). Host: plazir27, Linux x86_64. All commands re-run verbatim against live host state. -->

# kaidoku-r3 / 01 — audit of round-2 entries (pe-e2e, crash-inspect-probe, jq-shadow)

## File: corpus/knowledge/2026-10-13-r2-pe-e2e-proof.md

### Verify: `sha256sum /home/vgpnk/.cache/uv/archive-v0/M1E0QXq07p7Gx3Fp/setuptools/cli-64.exe` + `file`
- result: confirmed — `bbb3de5707629e6a60a0c238cd477b28f07f0066982fda953fa6fcec39073a4a`; `PE32+ executable for MS Windows 6.00 (console), x86-64, 6 sections`. Byte-exact match with the entry.

### Verify: `timeout 900 npx -y rea-agents@6.4.0 analyze <path> --format json` (twice, diffed)
- result: confirmed — provider `{'id': 'ghidra', 'name': 'Ghidra', 'version': '12.1.4'}`; `segment_count 8, procedure_count 142, string_count 89`; segments `[Headers, .text, .rdata, .data, .pdata, .rsrc, .reloc, tdb]`. Two runs this round produced **byte-identical** output (`diff -q` → IDENTICAL), re-confirming the determinism claim. Output is 2,993 B, the exact size r2 reported.

### Verify: `npx -y rea-agents@6.4.0 search <path> ".*" --kind procedures --mode regex --format json | …` (expect 81)
- result: confirmed — total 142 = **81 local + 61 EXTERNAL** (exactly the entry's split). 23,046 B output = r2's recorded size.

### Verify: `npx -y rea-agents@6.4.0 decompile <path> 0x140001d40 --format json | …`
- result: confirmed — `void entry(void) { __security_init_cookie(); FUN_140001bc4(); return; }`, provider ghidra 12.1.4. 3,613 B = r2's recorded size.

### Verify: `npx -y rea-agents@6.4.0 inspect-pe-resources <path> --format json | …` (expect `rea-pe-resources {'kind': 'id', 'id': 24}`)
- result: confirmed — verbatim output `rea-pe-resources {'kind': 'id', 'id': 24}`; format pe32-plus, machine 34404; payload sha256 `4bb79dcea0a901f7d9eac5aa05728ae92acb42e0cb22e5dd14134f4421a3d8df` identical to r2; `icon_groups` empty. 2,948 B = r2's recorded size.

### Verdict audit: agree — every quantitative claim (provider, 8/142/89, 81+61 split, decompile body, resource parser identity, byte-determinism) reproduced exactly. The `suggested: admit` on all five candidates stands. Minor note: the evidence_id for `analyze` today is `ev_d81a08f0…` (r2 deleted its /tmp files so cross-round byte-identity can't be compared, but within-round determinism — the load-bearing claim — holds).

## File: corpus/knowledge/2026-10-13-r2-crash-inspect-probe.md

### Verify: bare `npx -y rea-agents@6.4.0 inspect-recorded-crash <core> --format json` (no REA_PWNTOOLS_PYTHON)
- result: confirmed — **the verb currently fails again**, exactly as the entry predicts on a host without the env var. `/tmp/kaidoku-pwnenv` is gone, `REA_PWNTOOLS_PYTHON` unset; bare run on a fresh `coredumpctl dump 1150573` (still 724,992 B, still recorded EXE `/usr/bin/bash` comm `crash-godot`) exits 1 `provider_unavailable`/`unavailable`/retryable:true with the identical rejection text demanding `REA_PWNTOOLS_PYTHON` → pwntools 4.15.0 + pyelftools 0.33 + Unicorn 2.1.2 ("REA never installs Python or packages").

### Verify: `uv venv /tmp/pv --python 3.11 && uv pip install --python /tmp/pv/bin/python "pwntools==4.15.0" "pyelftools==0.33" "unicorn==2.1.2" && REA_PWNTOOLS_PYTHON=/tmp/pv/bin/python npx -y rea-agents@6.4.0 inspect-recorded-crash --help`
- result: confirmed — venv built on cached cpython-3.11.17, pinned wheels resolved cleanly, `--help` printed the verb's usage (`path` + `--debugger-context`). Provisioning recipe reproduces in seconds, verbatim.

### Verify: `coredumpctl dump 1150573 -o /tmp/c && REA_PWNTOOLS_PYTHON=<venv> npx … inspect-recorded-crash /tmp/c --format json | …registers`
- result: confirmed (with venv=/tmp/pv) — exit 0, 25,635 B Evidence envelope; provider `pwntools-elf` (`pwntools@4.15.0;pyelftools@0.33;unicorn@2.1.2`); `format elf-core`, `x86_64-little-endian`; **segments 40, notes 8, threads 1, signals 1, registers 27** — all exact. Signal: number 11, code 0, errno 0, fault_address null, meanings "unknown". No backtrace/frame fields anywhere — the raw-retention/no-unwinding claim holds. limitations[7]. (Size delta vs r2's 25,700 B is evidence_id/timestamp noise.)

### Verify: `coredumpctl dump 1728 -o /tmp/c && stat -c%s /tmp/c && REA_PWNTOOLS_PYTHON=<venv> npx … inspect-recorded-crash /tmp/c --format json`
- result: confirmed — waybar core still decompresses to exactly **434,184,192 B**; run exits 1 `invalid_request`/`out_of_range`: "Selected artifact exceeds 33554432 bytes". The 32 MiB cap boundary is unmoved.

### Verify: negative probes — raw `.zst` blob; `/usr/bin/waybar` (ET_EXEC); `--debugger-context`
- result: confirmed — `.zst` → `invalid_request`/`invalid_format` "Selected recording lacks a complete ELF identification" (retryable); `/usr/bin/waybar` → `unsupported_target` "requires x86-64 ET_CORE" (not retryable); `--debugger-context` on the good core → `capability_unavailable`/`unsupported_provider` demanding `REA_PWNDBG_GDBINIT`. No pwndbg anywhere on host (`find` empty, `which pwndbg` none, `pacman -Qs pwndbg` empty). All three coredump PIDs (1728, 689428, 1150573) still listed by coredumpctl.

### Verdict audit: agree — the entire refusal taxonomy {provider_unavailable → invalid_format → unsupported_target → out_of_range → capability_unavailable} reproduced verbatim, and the summary's "mechanism held, coverage frontier" framing is accurate: with the ad-hoc venv gone, the verb is dead-by-default on this host again (BYO-Python is the only path, now re-proven). `suggested: admit` stands on all six candidates.

## File: corpus/knowledge/2026-10-13-r2-jq-shadow-verdict.md

### Verify: `sha256sum ~/.local/bin/jq`; fetch `https://github.com/jqlang/jq/releases/download/jq-1.8.2/sha256sum.txt`
- result: confirmed — local `b1c22172dd303f3be49e935aa56aa48a8b7a46e0bc838b4997d3bb451495870f` (2,267,912 B, mtime 2026-10-03 18:34:03 -0300, owner vgpnk). Live-fetched upstream `sha256sum.txt` carries that exact digest on **both** the `jq-linux-amd64` and `jq-linux64` lines — the entry states this dual-listing correctly, byte-for-byte. `/usr/bin/jq` sha256 `e815667…f7806` also matches the entry.

### Verify: `readelf -h/-d/-r/-x .init_array/-l/-p .comment ~/.local/bin/jq`
- result: confirmed — Type `EXEC`, entry 0x403a50, "There is no dynamic section", 50 relocations **all** `R_X86_64_IRELATIVE` (no other type), `.init_array` = single qword `0x403b40`, INTERP count 0, `.comment` = `GCC: (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0`, BuildID `0ebe5e23…`. `JQ_BUILD_CONFIGURATION` and `decNumber 3.68` strings present.

### Verify: `npx -y rea-agents@6.4.0 analyze ~/.local/bin/jq --format json`
- result: confirmed — ghidra 12.1.4; **26 segments / 2,279 procedures / 2,915 strings** exactly; evidence_id `ev_95ccd1f3edbd49f1…` reproduced byte-identically across rounds — the strongest possible determinism corroboration.

### Verify: `npx -y rea-agents@6.4.0 search ~/.local/bin/jq '.' --kind procedures --mode regex --format json` (entry expects `[]`)
- result: **drifted** — the corpus is NOT empty. Returns **2,279 rows**: 2,207 `FUN_*`, 59 `thunk_FUN_*`, plus 13 labels (`entry`, `switchD_…::caseD_*`). Identical result via the `--pattern '.'` flag form. The entry's sub-claim "`search --kind procedures` returns 0 rows for any pattern … REA's procedure corpus indexes named symbols only" is wrong as stated — the corpus indexes all Ghidra procedures including auto-generated `FUN_*`/`thunk_FUN_*` names. (The r2 lane probably ran patterns that matched nothing, e.g. literal `FUN_\|entry` without regex alternation.) This does not undermine the candidate's real claim — the 26/2279/2915 census and its static-linkage explanation are confirmed — but the empty-corpus mechanism explanation should be corrected in the corpus.

### Verify: `npx -y rea-agents@6.4.0 decompile ~/.local/bin/jq 0x403a50`
- result: confirmed — `void processEntry entry(...) { FUN_00492360(FUN_00401f00, param_2, &stack0x00000008, 0, 0, param_1, auStack_8); do { /* infinite loop */ } while(true); }` — textbook `_start` tail-calling `__libc_start_main` with `main`=0x401f00, exactly as claimed.

### Verify: `~/.local/bin/jq --version && /usr/bin/jq --version`; `echo '{"a":1}' | … '.a'`
- result: confirmed — `jq-1.8.2` twice; `.a` → `1` from both binaries.

### Verdict audit: agree — the benign-payload verdict stands on the decisive evidence: the published-checksum match was re-fetched live and holds on both asset names, and every internal artifact (toolchain, IRELATIVE-only relocs, single init hook, `_start`/`main` shape, identical behavior) agrees. One required correction: Candidate 3's "procedures corpus returns 0 rows" sub-claim drifted — it returns 2,279 rows; correct the mechanism note ("corpus lists anonymous FUN_*/thunk_* too") while keeping the census verdict. `suggested: admit` on Candidates 1, 2, 4, 5, 6 and the Unknown stands; Candidate 3's verdict stands but its stated mechanism needs the fix above.

## Summary

**Net verdict: round-2 entries are trustworthy; one sub-claim correction needed in the jq entry.**

- `r2-pe-e2e-proof.md` — 5/5 verifies confirmed; all `admit` verdicts endorsed. PE-via-Ghidra is proven, deterministic, and still reproducible today.
- `r2-crash-inspect-probe.md` — 6/6 verifies confirmed; all `admit` verdicts endorsed. Direct answer to the task question: **yes, `inspect-recorded-crash` currently fails again** — `/tmp/kaidoku-pwnenv` is gone, `REA_PWNTOOLS_PYTHON` is unset, and a bare run on the still-recorded 724,992 B bash core exits 1 `provider_unavailable`. The `uv`-provisioning path was re-executed verbatim (/tmp/pv) and the full taxonomy + successful envelope reproduced.
- `r2-jq-shadow-verdict.md` — the flagship conclusion (**benign payload, genuine upstream jq-1.8.2 `jq-linux-amd64`/`jq-linux64` artifact, sha256 `b1c22172…5870f`**) is re-confirmed against the live-fetched `sha256sum.txt`, stated correctly in the entry including the dual asset names. One drifted detail to patch: the "procedures corpus empty / indexes named symbols only" claim — `search --kind procedures '.'` now verifiably returns all 2,279 Ghidra procedures (FUN_*/thunk_*/entry labels). Corrective note only; no verdict flips.
