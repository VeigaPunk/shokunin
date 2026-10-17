# Lead-Authored r99 Wiring And Leak-Branch Repair

Status: exact source decisions, not executed. The matching regression
must be fully authored before implementation is delegated.

Baseline: audio HEAD 81b268f7, source sha
f753f9a9695d47c0d892833f5347c78fb536e3622d99ccd0f965b24735e8f254.
All twenty GLM reviewers and the scoped host-lock executor are complete.
No current live family or source writer exists.

## Native Pair

In rtp_e2e_r99_entry's first native fragment ONLY, replace the source
call `_rtp_r99_source_args()` with
`_rtp_r99_source_args(src_port=RTP_R99_PORT)`.
The source helper's +1 default must remain unchanged: standalone crafted
packet-injection legs rely on it. The lead directly reads the fresh
verifier fragment and props: sink destination 46814, source bind 46815.
This is a real fixture miswire, not evidence of host-dependent silence.
Do not claim the fix alone guarantees the source will now receive until
one new controlled family run proves that.

Replace only the unsupported comment attributing the difference to
"host state" with this precise explanation:
"The native pair must share a port. The source helper's +1 default
belongs to standalone packet-injection legs. A non-reproducing native
leg remains named unmeasured, not a silent green."
Keep the earlier multicast-versus-connected-unicast explanation.

## Leak Predicate

The lead reads the full existing e_lan branch. It currently assigns
allowance only in the final else, after a wide-band abstention. A
full-volume leak can therefore never fail when the idle band is wide.

Minimal exact repair, no threshold tuning:

1. Immediately after `excess = arm - band`, assign the existing
   `allowance = 0.2 * max(1, lan["emitted"])`.
2. Change the wide-band elif to:
   `elif excess <= allowance and band > 0.25 * max(1, lan["emitted"]):`
3. Remove the now-duplicate allowance assignment from the final else.
4. Keep the existing <=0 strongest arm and final `_rtp_r99_true`
   `excess <= allowance` grader unchanged. Keep its existing "armed"
   verdict semantics (test applied; failures list reports red).
5. Add one source comment explaining that noisy small excess can be
   unmeasured, but already-out-of-band excess cannot be hidden by noise.

This changes reachability of the EXISTING bound; it introduces no new
numeric threshold or score. NIC counters remain a coarse proxy under
background variance, not universal proof of physical-network isolation.
The physical-LAN control remains default-off, and must NEVER be enabled
to make this repair's tests or run green.

## Authored Test Design (Code Still To Be Written By Lead)

AST-isolate the actual sink/source arg builders and first native
source call inside rtp_e2e_r99_entry. Namespace literal test-only
RTP_R99_PORT=46000, matching SINK/SRC/SESS names and multicast address.
Evaluate actual native source-call expression: its source.port must
equal actual native sink destination.port. Assert both local.ifname
properties are lo. Separately the unoverridden source helper must
still produce 46001. No socket or process runs in this test.

For branch regression, extract the actual `if excess <= 0` AST and
the actual allowance assignment from the e2e entry. Execute those
nodes with real `_rtp_r99_true`, entry/failures lists, lan dictionary
(`emitted`, precreated `resolution`), iface="test0", band and excess.
Executing the actual allowance assignment before the old branch does
not change the old failure: the wide-band elif still wrongly abstains.

Required synthetic cases (excess, band, emitted -> outcome):
- -1, 9000, 20000 -> armed_below_band; no failure/block.
- 1, 9000, 20000 -> coverage_block; no failure.
- 4001, 9000, 20000 -> FAILURE, not a coverage block.
- 4001, 100, 20000 -> FAILURE, not a coverage block.
- 4000, 100, 20000 -> armed; no failure/block.

Keep before/after source, exact source-only diff, and all raw test
commands/stdout/stderr/rc in a fresh proof directory. The regression
must fail on current source and pass after these exact changes.
No live family, other source edits, new law-set grading, service
restart, network opt-in, report rewrite, commit or push is authorized
by this document. A later lead recipe will run affected final bytes
once, after the remaining source fixes are integrated.
