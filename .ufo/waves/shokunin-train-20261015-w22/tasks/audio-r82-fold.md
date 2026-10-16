# audio-r82-fold — apply correction queue to measure_audio.py

Custody free (r83 author landed a151a226). Apply the landed correction queue to corpus/fixtures/measure_audio.py:

1. Simplifier report reports/round-82/r82-simplifier.md — the proven −25-line patch (10 items, patch file in its corpus dir).
2. Reviewer F1: r82 tone pairs collide with r78 family at pid%4==1 (1208/1711 inside both ±6% bands) — re-key or shift the r82 tone freqs; add a same-family band guard.
3. Reviewer F2: arm the `-channels 0` rc=8 ALSA class (boundary-observed exact class).
4. Critic F1: a2_hw_free_pwheld holds hw:0,1 (headphones) not claimed hw:0,0 — fix premise or retarget claim.
5. Critic F2: t2_cap_* has no content gate — add a sustained-zeros rejection (r85 class).
6. Critic F3: fixed tag + no same-family lock — derive tag from pid/namespace + take a family lock.
7. Critic F4: _gst_r81_unload_own substring predicate kills foreign modules — exact-name/pid match only.
8. Scribe items A-list count/timeline corrections where they touch armed rows.

Rerun the affected legs green twice on final bytes. Commit nothing; report to reports/round-82/r82-fold.md + receipts corpus/live/r82-fold/. Return: report path, diffstat, leg results, blockers.
