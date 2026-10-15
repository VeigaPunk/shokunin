# w17 — post-reset surge (dispatch when routes recover ~13:01 UTC)

Rate-limit sweep at ~09:0x killed the entire ufo-* seat band (zfl/flash/Sol
pooled). Survived: subagent_general route (audio r80 author d03f3ac6 live).
This wave restores the 16–32 band. Dispatch order: wave-B seats first
(they unblock the committed rounds' adjudication), then authors, then scouts.

## Wave-B backlogs (committed work awaiting seats)

| round | needs | basis |
|---|---|---|
| g2d r86 (7ae7083, 182/182) | critic, verifier, boundary, simplifier, scribe | phys2d_backends.gd 8 cells: engine census, silent boot fallback, manager refusal lattice, thread gate, dummy degenerate/timeout |
| g3d r90 (191f131, 225/225) | critic, verifier, boundary, simplifier, scribe | phys3d_joints.gd + r90_child.gd: 8 arms ×3 backends, crash-envelope pins, bimodal freeb_ops@gp |
| g3d r89 (closed) | scribe retry only | post-hoc record audit; adjudicator absorbed |
| audio r80 | full wave-B when author lands | in flight (d03f3ac6) |

## Forward authors (locks free)

- g3d r91 — bpy point-cache surface (scout landed r91)
- audio r81 — take scout r82's ffmpeg surface (playback `-device` never
  validated / capture validates / target-loss re-link 0.2–0.3s both ways)
- g2d r87 — needs scout first

## Scouts deeper out

- g2d: r87, r88, r89, r90
- audio: r89, r90
- g3d: r97, r98, r99

## Seat budget

~15 wave-B + 3 authors + 9 scouts ≈ 27 — inside the 16–32 band.
Route mix per prior convention: swe-2 on author/verifier/sentinel,
flash on critic/simplifier, zfl on scout/boundary/scribe, Sol when clear.
