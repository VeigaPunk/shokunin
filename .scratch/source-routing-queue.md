# Source-routing queue — operator directives 2026-10-27 (hyaku run 10)

Operator-supplied study targets. Each entry is routed, not yet landed; the owning lane
must open the source under its source contract (dedupe, located quote <=25 words, access
date, tier/scope, evidence receipt) before any corpus row or knowledge entry is written.

## 1. REA / reverse-engineering toolset → revenger (dispatched r72)
Listed: morluto/rea, NationalSecurityAgency/ghidra, LaurieWired/GhidraMCP, mrexodia/ida-pro-mcp,
skylot/jadx, iBotPeaches/Apktool, frida/frida, icsharpcode/ILSpy, radareorg/radare2,
x64dbg/x64dbg, WerWolv/ImHex, angr/angr, mitmproxy/mitmproxy, dnSpy/dnSpy (original) and
dnSpyEx/dnSpy (maintained fork), rizinorg/rizin, EpicGames/raddebugger,
zhuyansen/awesome-ai-reverse-engineering, morluto/awesome-reverse-engineering, Dryxio/reagent.
Operator notes: REA workflows and the clean-room loop (SPEC.md + oracles) ship in the main REA
repo; LaurieWired/GhidraMCP is the widely referenced implementation (others exist, e.g.
themixednuts/GhidraMCP). State: dispatched to RevengerR72 with the operator's unblock of the
r71 streak block (block file archived at /fast/scratch/hyaku-run10/unblocked/revenger.r71-streak).

## 2. Additional t.co reading set → revenger r72 (dispatched, unresolved shorteners)
44 `t.co` links plus https://x.com/i/article/2111752926104375296. These are shorteners: the
lane must resolve each safely, record the destination and observed content, and refuse to
bulk-admit. Do not treat a shortener as a source identity.

## 3. Claude-Red → REA + bounty/security lane
https://github.com/SnailSploit/Claude-Red — operator wants REA and the bounty-hunter lane to
analyse it properly.
- kasegi (bounty and security research): QUEUED — lane is streak-blocked (next 42). Route at
  its next authorized round; no corpus edit outside an authorized round.
- revenger: relayed as context for r72 (REA-side analysis), not ownership of the security lane's
  province.

## 4. Claude-Code-Game-Studios → game-dev-2d, game-dev-3d, lore, audio (queued, not yet training)
https://github.com/Donchitos/Claude-Code-Game-Studios — hold until these four lanes resume
training (they are in shokunin.conf and audited by the driver, but not in the current 10-round
hyaku block). At resume: route to each lane for source-based study and relevant corpus
additions; dedupe and record scope per lane.

## 5. scenario-labs/skills → game-dev-2d, game-dev-3d, lore, audio (queued, operator 2026-10-27)
https://github.com/scenario-labs/skills — operator directive: all four game-production lanes
(2d, 3d, lore, sfx/audio) study this source, assimilate what is good into their own corpus and
curate (admit/reject per item, with reasons). Same hold as item 4: these lanes are already at
round >= 100 and outside the hyaku pool (scripts/hyaku/pool.txt), so route it at each lane's
next authorized round, together with item 4. Each lane opens the repo itself under its source
contract; no shared row, no bulk admission, province files decide which skills each lane owns.
Operator note (deferred, not authorized yet): a possible future mint of a topology-creation
shokunin seeded from this source — record candidate material, do not mint.

## Rules that apply to every item above
- Open the source; a URL in a queue is not evidence. Row/entry requires a located quote,
  access date, tier and scope, and a recheck cadence.
- No bulk admission; no scope borrowing across lanes (province files govern).
- Record tool/version/channel/reason for any install; no DRM circumvention, no live-target
  activity, no publishing reversed code (revenger PROVINCE.md).
