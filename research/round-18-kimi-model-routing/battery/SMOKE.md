# Mock smoke — the runner proved itself before spending real quota

The battery runner, the SSE parser and the deterministic grader were exercised end to end against
`scripts/mock_server.py`, a stdlib `ThreadingHTTPServer` that speaks the same three protocols the
pool uses and can be told to misbehave. This record is the result of that run; the live captures are
in `raw/`, this smoke's are in `smoke/raw/`.

## Command

```
python3 scripts/mock_server.py 8799 &
R18_BATTERY_RAW="$PWD/smoke/raw" python3 scripts/run_battery.py \
    --mock-base http://127.0.0.1:8799 --mock-map scripts/mock_map.json \
    --timeout 8 --concurrency 4
```

`R18_BATTERY_RAW` keeps smoke captures out of the live `raw/` tree. `mock_map.json` assigns a
behaviour to each pool id so that one run covers every path.

## Result

188 requests planned (17 models × 10 measured + 1 warm-up for the devin-class lane), 188 recorded,
16 s wall clock. Every failure class the mission names was produced and classified as intended.

| model | mock behaviour | measured classes | perf rep span ms / TPS |
| --- | --- | --- | --- |
| `alibaba-token-plan-2/deepseek-v4.1-flash` | dead | auth×1, skipped_after_fatal×10 | n/a / not derivable |
| `alibaba-token-plan-2/qwen3.8-flash` | dead | auth×1, skipped_after_fatal×10 | n/a / not derivable |
| `alibaba-token-plan-3/deepseek-v4.1-flash` | dead | auth×1, skipped_after_fatal×10 | n/a / not derivable |
| `alibaba-token-plan-3/qwen3.8-flash` | dead | auth×1, skipped_after_fatal×10 | n/a / not derivable |
| `alibaba-token-plan/deepseek-v4.1-flash` | fences | format_break×4, ok×5 | 121 / 1015.07, 122 / 1010.86 |
| `alibaba-token-plan/qwen3.8-flash` | wrong | format_break×3, ok×1, wrong_answer×5 | n/a / not derivable |
| `cascade/deepseek-v4.1-flash` | good | ok×9 | 122 / 991.28, 123 / 983.56 |
| `cascade/glm-5.3-flash` | good | ok×9 | 123 / 987.44, 122 / 988.27 |
| `cursor/composer-2.5` | burst | ok×9 | 0 / not derivable, 0 / not derivable |
| `cursor/cursor-grok-4.5-low-fast` | timeout | transport×2, skipped_after_fatal×9 | n/a / not derivable |
| `hyper/deepseek-v4.1-flash` | good | ok×9 | 122 / 994.73, 122 / 992.97 |
| `hyper/qwen3.8-flash` | notools | format_break×1, ok×8 | 121 / 996.46, 122 / 995.12 |
| `openai-codex/gpt-6.1-sol` | good | ok×9 | 122 / 994.09, 122 / 993.93 |
| `openai-codex/gpt-6.1-sol-high` | noauth | auth×1, skipped_after_fatal×10 | n/a / not derivable |
| `xai-oauth/grok-4.5` | good | ok×9 | 122 / 994.75, 123 / 987.61 |
| `zai-coding-plan/glm-5-turbo` | silent | format_break×8, ok×1 | n/a / not derivable |
| `zai-coding-plan/glm-5.3-flash-low` | good | ok×9 | 123 / 987.46, 122 / 992.11 |

The perf rows carry no pass/fail, so two measured rows per model show no class; that is the
`TTFT/TPS` measurement, not a graded probe.

## What the smoke established

1. **One-attempt rule works.** A quota/auth wall aborts on the first measured probe; a transport
   failure aborts on the second. Dead lanes cost 1 request, a timing-out lane 2, and everything
   after is recorded as `skipped_after_fatal` with the reason.
2. **Content failures do not abort.** The `fences` and `wrong` lanes keep running to the last probe:
   `fences` fails c1–c4 (the instruction forbids markdown) but passes c5, k1–k3 and t1; `wrong`
   fails 8 of 9.
3. **Burst detection is real.** The `burst` lane returns the full answer in one flush: decode span
   0 ms, so TPS is reported as not derivable rather than as a fake throughput figure. This is the
   M1 burst finding reproduced on demand, which is what makes the live TPS column trustworthy.
4. **The codex shape is enforced by the mock**, so a regression in the D6 request shape would fail
   the smoke: `gpt-6.1-sol` answered 200 through the `/responses` path with `store:false`,
   `stream:true`, list `input` and no `temperature`.
5. **Warm-up fires only for the devin-class lane** (`cascade/glm-5.3-flash` ran 12 requests, 11 for
   every other model) and is excluded from the measured counts.
6. **Redaction is intact.** `auth_headers_sent` records header *names*; captured bodies keep
   `max_tokens`, `completion_tokens` and friends at their real values.

## Two runner bugs the smoke caught (fixed before the live run)

- **Perf probes had no failure class**, so the one-attempt rule never fired and a quota-dead lane
  burned all 11 probes (88 s of the first smoke was a single timing-out lane). Fixed by running the
  perf outcome through the same request-level classifier as the graded probes.
- **A content-level format break aborted the model.** A fenced answer to c1 was read as a lane-level
  rejection, ending that model's battery after one probe. Fixed by stamping every verdict with an
  explicit `request_level` flag: only failures the lane is answerable for (refused request shape,
  quota wall, dead socket) trigger the abort.

## Hygiene

```
python3 scripts/hygiene_check.py smoke
hygiene scan over smoke
files scanned: 190
credentials checked: 12 (values never printed)
hits: 0
```

## Known limits of the smoke

- The mock streams at a fixed 6 ms per 24-character chunk, so its ~990 tok/s is a property of the
  mock's pacing loop, not a machine measurement. Nothing in the live table compares against it.
- The mock does not implement rate limits, retries or mid-stream disconnects; those remain untested
  until the live run encounters them.
