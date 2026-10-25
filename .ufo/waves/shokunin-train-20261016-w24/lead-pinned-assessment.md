# Frozen Lead Assessment - bb177513 Verifier Receipts

The lead has read the four completed verifier receipts below directly,
not merely their summaries. These are frozen derived observations for
future presentation; do not recompute them to rewrite a status update.
This is not a new grader, complete law-set verification, or admission.

Source pin: bb177513a615a32d3bc150ecbdcf78302e110d8c.
Source sha: 801e153b84368bba4a77e85c129376612c797694c435e9104cdad6e62169be2f.
All four fixed-recipe runs returned rc 0 and empty stderr.

| round | entries | top-level leg counts in receipt order | total keys | named coverage blocks |
| --- | --- | --- | --- | --- |
| 93 | 9 | 17/9/10/11/6/6/8/9/14 | 90 | notify_bogus load refusal; g_default silent-post-tap twice |
| 98 | 6 | 15/18/12/4/4/14 | 67 | cap_noprop; x_stall300 and x_stall600 profiler JSON incomplete |
| 99 | 6 | 3/8/7/8/6/5 | 37 | e_native; default-off e_lan_control |
| 100 | 9 | 2/7/4/5/3/7/4/3/2 | 37 | none |

All selected entries have empty failures lists. These are key counts,
not assertions that every key measured its intended law. r99 includes
four tone setup records and 33 non-tone cells. r98's profiler ratio is
not measured by truncated JSON. r100's missing no-config/IR arms cannot
be inferred measured merely because its present entries have no blocks.

## Literal Receipt Paths

- /home/vgpnk/Projects/shokunin/audio-waveb-resume/r93-verifier/tree/corpus/live/runs/20261016T125015677298Z-ebur-r93/measurements.json
- /home/vgpnk/Projects/shokunin/audio-waveb-resume/r98-verifier/tree/corpus/live/runs/20261016T124040716973Z-pwstream-r98/measurements.json
- /home/vgpnk/Projects/shokunin/audio-waveb-resume/r99-verifier/tree/corpus/live/runs/20261016T124136092601Z-rtp-r99/measurements.json
- /home/vgpnk/Projects/shokunin/audio-waveb-resume/r100-verifier/tree/corpus/live/runs/20261016T124442058903Z-sofa-r100/measurements.json

Counting command used by the lead: json.load each path, select
measurements keys starting pwstream_/rtp_/sofa_, print len(rows),
len(row.get("legs", {})), row.get("failures") and
row.get("coverage_blocked"), and sum those dictionary lengths.
No original measurement computation was rerun.

## Directly Inspected r99 Wiring

The fresh r99 e_native fragment sends multicast to port 46814 but binds
its source to 46815; sink/source node props corroborate those ports.
Pinned source uses the sink's default RTP_R99_PORT and the source's
default RTP_R99_PORT + 1. The native call must explicitly use
src_port=RTP_R99_PORT; standalone injection legs retain their +1 default.
This is a confirmed wiring defect. It is not yet proof that correcting
it alone will remove every native-path blocker.

The LAN control row has measured:false, the explicit approval block,
and no arm_tx_packets field. No opt-in was set by the verifier.

## Directly Inspected r100 Clock Witnesses

Fresh metadata witnesses, not the lossy server_clock regex:

| variant | runtime settings |
| --- | --- |
| q512 | clock.quantum="512", clock.max-quantum="2048", clock.rate="48000" |
| q2048 | clock.quantum="2048", clock.rate="48000" |
| r96000 | clock.rate="96000", clock.allowed-rates="[ 96000 ]" |

All declared props are default.clock.*; removing "default." maps them
to the metadata keys. A future repair can compare each runtime value
with str(props[key]) without inventing new target values or bands.

## Still Pending

All twenty seats have returned. Remaining: lead full-report review;
source repairs and adjudications. Neither fully clean source nor
complete learning trends are asserted.
