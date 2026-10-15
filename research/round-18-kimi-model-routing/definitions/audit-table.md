# config audit table

Config: `/home/vgpnk/.kimi-code/config.toml`  
file sha256 `e3c223e054a626b847e69f73020ac9b4fdec1ccc2c8f00dcbf414dcda8acfe78`  
json-canonical digest/16 `61f22a2bbe52d616`

| # | alias | provider | proto | model | ctx | in | out | caps | efforts | dflt | off | rkey |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | **managed:kimi-code** (kimi) | | | | | | | | | | | |
| 1 | `kimi-code/kimi-for-coding` | managed:kimi-code | kimi | `kimi-for-coding` | 1048576 | - | - | thinking+always_think+image_in+video_in+tool_use+dynamically_ | low+high+max | max | - | - |
| 2 | `kimi-code/kimi-for-coding-highspeed` | managed:kimi-code | kimi | `kimi-for-coding-highspeed` | 262144 | - | - | thinking+always_think+image_in+video_in+tool_use | - | - | - | - |
| 3 | `kimi-code/k3` | managed:kimi-code | kimi | `k3` | 1048576 | - | - | thinking+always_think+image_in+video_in+tool_use+dynamically_ | low+high+max | high | - | - |
| 4 | `kimi-code/k3-256k` | managed:kimi-code | kimi | `k3-256k` | 262144 | - | - | thinking+always_think+image_in+tool_use+dynamically_ | low+high+max | high | - | - |
| | **alibaba-token-plan** (openai) | | | | | | | | | | | |
| 5 | `alibaba-token-plan/qwen3.7-max` | alibaba-token-plan | openai | `qwen3.7-max` | 1000000 | - | 131072 | thinking+tool_use | - | - | - | reasoning_content |
| 6 | `alibaba-token-plan/deepseek-v4-flash-0731` | alibaba-token-plan | openai | `deepseek-v4-flash-0731` | 1000000 | - | 384000 | thinking+tool_use | high+max | - | - | reasoning_content |
| 7 | `alibaba-token-plan/qwen3.8-max` | alibaba-token-plan | openai | `qwen3.8-max` | 1000000 | - | 131072 | image_in+video_in+thinking+tool_use | low+medi+xhig | - | - | reasoning_content |
| 8 | `alibaba-token-plan/qwen3.8-max-xhigh` | alibaba-token-plan | openai | `qwen3.8-max` | 1000000 | - | 131072 | image_in+video_in+thinking+tool_use | low+medi+xhig | xhigh* | - | reasoning_content |
| 9 | `alibaba-token-plan/glm-5` | alibaba-token-plan | openai | `glm-5` | 202752 | - | 16384 | thinking+tool_use | - | - | - | reasoning_content |
| 10 | `alibaba-token-plan/deepseek-v4.1-flash` | alibaba-token-plan | openai | `deepseek-v4.1-flash` | 1000000 | - | 384000 | image_in+thinking+tool_use | low+high+max | - | - | reasoning_content |
| 11 | `alibaba-token-plan/kimi-k2.6` | alibaba-token-plan | openai | `kimi-k2.6` | 262144 | - | 262144 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 12 | `alibaba-token-plan/kimi-k2.5` | alibaba-token-plan | openai | `kimi-k2.5` | 262144 | - | 98304 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 13 | `alibaba-token-plan/qwen3.6-flash` | alibaba-token-plan | openai | `qwen3.6-flash` | 1000000 | - | 65536 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 14 | `alibaba-token-plan/deepseek-v4-pro-0813` | alibaba-token-plan | openai | `deepseek-v4-pro-0813` | 1000000 | - | 384000 | thinking+tool_use | high+max | - | - | reasoning_content |
| 15 | `alibaba-token-plan/MiniMax-M2.5` | alibaba-token-plan | openai | `MiniMax-M2.5` | 196608 | 196601 | 32768 | thinking+tool_use | - | - | - | reasoning_content |
| 16 | `alibaba-token-plan/qwen3.8-flash` | alibaba-token-plan | openai | `qwen3.8-flash` | 1000000 | - | 131072 | image_in+video_in+thinking+tool_use | low+medi+xhig | - | - | reasoning_content |
| 17 | `alibaba-token-plan/glm-5.2` | alibaba-token-plan | openai | `glm-5.2` | 1000000 | - | 131072 | always_think+tool_use | high+max | - | - | reasoning_content |
| 18 | `alibaba-token-plan/glm-5.1` | alibaba-token-plan | openai | `glm-5.1` | 202752 | - | 128000 | thinking+tool_use | - | - | - | reasoning_content |
| 19 | `alibaba-token-plan/deepseek-v4-pro` | alibaba-token-plan | openai | `deepseek-v4-pro` | 1000000 | - | 384000 | thinking+tool_use | high+max | - | - | reasoning_content |
| 20 | `alibaba-token-plan/qwen3.6-plus` | alibaba-token-plan | openai | `qwen3.6-plus` | 1000000 | - | 65536 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 21 | `alibaba-token-plan/deepseek-v3.2` | alibaba-token-plan | openai | `deepseek-v3.2` | 131072 | - | 65536 | thinking+tool_use | - | - | - | - |
| 22 | `alibaba-token-plan/glm-5.3` | alibaba-token-plan | openai | `glm-5.3` | 1000000 | - | 131072 | always_think+tool_use | low+high+max | - | - | reasoning_content |
| 23 | `alibaba-token-plan/qwen3.7-plus` | alibaba-token-plan | openai | `qwen3.7-plus` | 1000000 | - | 65536 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 24 | `alibaba-token-plan/deepseek-v4-flash` | alibaba-token-plan | openai | `deepseek-v4-flash` | 1000000 | - | 384000 | thinking+tool_use | high+max | - | - | reasoning_content |
| | **alibaba-token-plan-2** (openai) | | | | | | | | | | | |
| 25 | `alibaba-token-plan-2/qwen3.7-max` | alibaba-token-plan-2 | openai | `qwen3.7-max` | 1000000 | - | 131072 | thinking+tool_use | - | - | - | reasoning_content |
| 26 | `alibaba-token-plan-2/deepseek-v4-flash-0731` | alibaba-token-plan-2 | openai | `deepseek-v4-flash-0731` | 1000000 | - | 384000 | thinking+tool_use | high+max | - | - | reasoning_content |
| 27 | `alibaba-token-plan-2/qwen3.8-max` | alibaba-token-plan-2 | openai | `qwen3.8-max` | 1000000 | - | 131072 | image_in+video_in+thinking+tool_use | low+medi+xhig | - | - | reasoning_content |
| 28 | `alibaba-token-plan-2/glm-5` | alibaba-token-plan-2 | openai | `glm-5` | 202752 | - | 16384 | thinking+tool_use | - | - | - | reasoning_content |
| 29 | `alibaba-token-plan-2/deepseek-v4.1-flash` | alibaba-token-plan-2 | openai | `deepseek-v4.1-flash` | 1000000 | - | 384000 | image_in+thinking+tool_use | low+high+max | - | - | reasoning_content |
| 30 | `alibaba-token-plan-2/kimi-k2.6` | alibaba-token-plan-2 | openai | `kimi-k2.6` | 262144 | - | 262144 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 31 | `alibaba-token-plan-2/kimi-k2.5` | alibaba-token-plan-2 | openai | `kimi-k2.5` | 262144 | - | 98304 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 32 | `alibaba-token-plan-2/qwen3.6-flash` | alibaba-token-plan-2 | openai | `qwen3.6-flash` | 1000000 | - | 65536 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 33 | `alibaba-token-plan-2/deepseek-v4-pro-0813` | alibaba-token-plan-2 | openai | `deepseek-v4-pro-0813` | 1000000 | - | 384000 | thinking+tool_use | high+max | - | - | reasoning_content |
| 34 | `alibaba-token-plan-2/MiniMax-M2.5` | alibaba-token-plan-2 | openai | `MiniMax-M2.5` | 196608 | 196601 | 32768 | thinking+tool_use | - | - | - | reasoning_content |
| 35 | `alibaba-token-plan-2/qwen3.8-flash` | alibaba-token-plan-2 | openai | `qwen3.8-flash` | 1000000 | - | 131072 | image_in+video_in+thinking+tool_use | low+medi+xhig | - | - | reasoning_content |
| 36 | `alibaba-token-plan-2/glm-5.2` | alibaba-token-plan-2 | openai | `glm-5.2` | 1000000 | - | 131072 | always_think+tool_use | high+max | - | - | reasoning_content |
| 37 | `alibaba-token-plan-2/glm-5.1` | alibaba-token-plan-2 | openai | `glm-5.1` | 202752 | - | 128000 | thinking+tool_use | - | - | - | reasoning_content |
| 38 | `alibaba-token-plan-2/deepseek-v4-pro` | alibaba-token-plan-2 | openai | `deepseek-v4-pro` | 1000000 | - | 384000 | thinking+tool_use | high+max | - | - | reasoning_content |
| 39 | `alibaba-token-plan-2/qwen3.6-plus` | alibaba-token-plan-2 | openai | `qwen3.6-plus` | 1000000 | - | 65536 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 40 | `alibaba-token-plan-2/deepseek-v3.2` | alibaba-token-plan-2 | openai | `deepseek-v3.2` | 131072 | - | 65536 | thinking+tool_use | - | - | - | - |
| 41 | `alibaba-token-plan-2/glm-5.3` | alibaba-token-plan-2 | openai | `glm-5.3` | 1000000 | - | 131072 | always_think+tool_use | low+high+max | - | - | reasoning_content |
| 42 | `alibaba-token-plan-2/qwen3.7-plus` | alibaba-token-plan-2 | openai | `qwen3.7-plus` | 1000000 | - | 65536 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 43 | `alibaba-token-plan-2/deepseek-v4-flash` | alibaba-token-plan-2 | openai | `deepseek-v4-flash` | 1000000 | - | 384000 | thinking+tool_use | high+max | - | - | reasoning_content |
| | **alibaba-token-plan-3** (openai) | | | | | | | | | | | |
| 44 | `alibaba-token-plan-3/qwen3.7-max` | alibaba-token-plan-3 | openai | `qwen3.7-max` | 1000000 | - | 131072 | thinking+tool_use | - | - | - | reasoning_content |
| 45 | `alibaba-token-plan-3/deepseek-v4-flash-0731` | alibaba-token-plan-3 | openai | `deepseek-v4-flash-0731` | 1000000 | - | 384000 | thinking+tool_use | high+max | - | - | reasoning_content |
| 46 | `alibaba-token-plan-3/qwen3.8-max` | alibaba-token-plan-3 | openai | `qwen3.8-max` | 1000000 | - | 131072 | image_in+video_in+thinking+tool_use | low+medi+xhig | - | - | reasoning_content |
| 47 | `alibaba-token-plan-3/glm-5` | alibaba-token-plan-3 | openai | `glm-5` | 202752 | - | 16384 | thinking+tool_use | - | - | - | reasoning_content |
| 48 | `alibaba-token-plan-3/deepseek-v4.1-flash` | alibaba-token-plan-3 | openai | `deepseek-v4.1-flash` | 1000000 | - | 384000 | image_in+thinking+tool_use | low+high+max | - | - | reasoning_content |
| 49 | `alibaba-token-plan-3/kimi-k2.6` | alibaba-token-plan-3 | openai | `kimi-k2.6` | 262144 | - | 262144 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 50 | `alibaba-token-plan-3/kimi-k2.5` | alibaba-token-plan-3 | openai | `kimi-k2.5` | 262144 | - | 98304 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 51 | `alibaba-token-plan-3/qwen3.6-flash` | alibaba-token-plan-3 | openai | `qwen3.6-flash` | 1000000 | - | 65536 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 52 | `alibaba-token-plan-3/deepseek-v4-pro-0813` | alibaba-token-plan-3 | openai | `deepseek-v4-pro-0813` | 1000000 | - | 384000 | thinking+tool_use | high+max | - | - | reasoning_content |
| 53 | `alibaba-token-plan-3/MiniMax-M2.5` | alibaba-token-plan-3 | openai | `MiniMax-M2.5` | 196608 | 196601 | 32768 | thinking+tool_use | - | - | - | reasoning_content |
| 54 | `alibaba-token-plan-3/qwen3.8-flash` | alibaba-token-plan-3 | openai | `qwen3.8-flash` | 1000000 | - | 131072 | image_in+video_in+thinking+tool_use | low+medi+xhig | - | - | reasoning_content |
| 55 | `alibaba-token-plan-3/glm-5.2` | alibaba-token-plan-3 | openai | `glm-5.2` | 1000000 | - | 131072 | always_think+tool_use | high+max | - | - | reasoning_content |
| 56 | `alibaba-token-plan-3/glm-5.1` | alibaba-token-plan-3 | openai | `glm-5.1` | 202752 | - | 128000 | thinking+tool_use | - | - | - | reasoning_content |
| 57 | `alibaba-token-plan-3/deepseek-v4-pro` | alibaba-token-plan-3 | openai | `deepseek-v4-pro` | 1000000 | - | 384000 | thinking+tool_use | high+max | - | - | reasoning_content |
| 58 | `alibaba-token-plan-3/qwen3.6-plus` | alibaba-token-plan-3 | openai | `qwen3.6-plus` | 1000000 | - | 65536 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 59 | `alibaba-token-plan-3/deepseek-v3.2` | alibaba-token-plan-3 | openai | `deepseek-v3.2` | 131072 | - | 65536 | thinking+tool_use | - | - | - | - |
| 60 | `alibaba-token-plan-3/glm-5.3` | alibaba-token-plan-3 | openai | `glm-5.3` | 1000000 | - | 131072 | always_think+tool_use | low+high+max | - | - | reasoning_content |
| 61 | `alibaba-token-plan-3/qwen3.7-plus` | alibaba-token-plan-3 | openai | `qwen3.7-plus` | 1000000 | - | 65536 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 62 | `alibaba-token-plan-3/deepseek-v4-flash` | alibaba-token-plan-3 | openai | `deepseek-v4-flash` | 1000000 | - | 384000 | thinking+tool_use | high+max | - | - | reasoning_content |
| | **zai-coding-plan** (openai) | | | | | | | | | | | |
| 63 | `zai-coding-plan/glm-5.3-flash` | zai-coding-plan | openai | `glm-5.3-flash` | 1000000 | - | 131072 | image_in+video_in+always_think+tool_use | low+high+max | - | - | reasoning_content |
| 64 | `zai-coding-plan/glm-5.3-flash-low` | zai-coding-plan | openai | `glm-5.3-flash` | 1000000 | - | 131072 | image_in+video_in+always_think+tool_use | low+high+max | low* | - | reasoning_content |
| 65 | `zai-coding-plan/glm-5.3-highspeed` | zai-coding-plan | openai | `glm-5.3-highspeed` | 1000000 | - | 131072 | always_think+tool_use | low+high+max | - | - | reasoning_content |
| 66 | `zai-coding-plan/glm-5.2-highspeed` | zai-coding-plan | openai | `glm-5.2-highspeed` | 1000000 | - | 131072 | always_think+tool_use | high+max | - | - | reasoning_content |
| 67 | `zai-coding-plan/glm-4.7` | zai-coding-plan | openai | `glm-4.7` | 204800 | - | 131072 | thinking+tool_use | - | - | - | reasoning_content |
| 68 | `zai-coding-plan/glm-5.2` | zai-coding-plan | openai | `glm-5.2` | 1000000 | - | 131072 | always_think+tool_use | high+max | - | - | reasoning_content |
| 69 | `zai-coding-plan/glm-5-turbo` | zai-coding-plan | openai | `glm-5-turbo` | 200000 | - | 131072 | thinking+tool_use | - | - | - | reasoning_content |
| 70 | `zai-coding-plan/glm-5.3` | zai-coding-plan | openai | `glm-5.3` | 1000000 | - | 131072 | always_think+tool_use | low+high+max | - | - | reasoning_content |
| | **hyper** (openai) | | | | | | | | | | | |
| 71 | `hyper/qwen3.7-max` | hyper | openai | `qwen3.7-max` | 1000000 | - | 64000 | thinking+tool_use | mini+low+medi+high | - | none | - |
| 72 | `hyper/qwen3.8-27b` | hyper | openai | `qwen3.8-27b` | 1000000 | - | 128000 | image_in+thinking+tool_use | mini+low+medi+high | - | none | - |
| 73 | `hyper/qwen3.8-2.4t-a95b` | hyper | openai | `qwen3.8-2.4t-a95b` | 1000000 | - | 128000 | always_think+tool_use | mini+low+medi+high | - | - | - |
| 74 | `hyper/glm-5.3-flash` | hyper | openai | `glm-5.3-flash` | 1048576 | - | 131072 | image_in+always_think+tool_use | low+high+max | - | - | - |
| 75 | `hyper/deepseek-v4-flash-0731` | hyper | openai | `deepseek-v4-flash-0731` | 1000000 | - | 384000 | always_think+tool_use | low+high+max | - | - | - |
| 76 | `hyper/qwen3.8-max` | hyper | openai | `qwen3.8-max` | 1000000 | - | 65536 | image_in+thinking+tool_use | mini+low+medi+high | - | none | - |
| 77 | `hyper/kimi-k3` | hyper | openai | `kimi-k3` | 1048576 | - | 16000 | image_in+always_think+tool_use | low+high+max | - | - | - |
| 78 | `hyper/deepseek-v4.1-flash` | hyper | openai | `deepseek-v4.1-flash` | 1048576 | - | 262144 | image_in+always_think+tool_use | low+high+xhig | - | - | - |
| 79 | `hyper/qwen3.7-flash` | hyper | openai | `qwen3.7-flash` | 1000000 | 991808 | 64000 | image_in+thinking+tool_use | mini+low+medi+high | - | none | - |
| 80 | `hyper/kimi-k2-thinking` | hyper | openai | `kimi-k2-thinking` | 262144 | - | 26214 | thinking+tool_use | - | - | - | - |
| 81 | `hyper/gemma-4-26b-a4b-it` | hyper | openai | `gemma-4-26b-a4b-it` | 256000 | - | 25600 | thinking+tool_use | - | - | - | - |
| 82 | `hyper/minimax-m2.7` | hyper | openai | `minimax-m2.7` | 262100 | - | 6553 | thinking+tool_use | - | - | - | - |
| 83 | `hyper/deepseek-v4-pro-0813` | hyper | openai | `deepseek-v4-pro-0813` | 1000000 | - | 262144 | always_think+tool_use | low+high+max | - | - | - |
| 84 | `hyper/inkling` | hyper | openai | `inkling` | 1048576 | - | 65536 | image_in+always_think+tool_use | low+medi+high | - | - | - |
| 85 | `hyper/minimax-m3` | hyper | openai | `minimax-m3` | 512000 | - | 512000 | image_in+always_think+tool_use | low+medi+high | - | - | - |
| 86 | `hyper/qwen3.8-flash` | hyper | openai | `qwen3.8-flash` | 1000000 | - | 128000 | image_in+thinking+tool_use | mini+low+medi+high | - | none | - |
| 87 | `hyper/glm-5.2` | hyper | openai | `glm-5.2` | 1000000 | - | 32768 | always_think+tool_use | high+xhig | - | - | - |
| 88 | `hyper/gpt-oss-120b` | hyper | openai | `gpt-oss-120b` | 131072 | - | 13107 | always_think+tool_use | low+medi+high | - | - | - |
| 89 | `hyper/glm-5.3` | hyper | openai | `glm-5.3` | 1000000 | - | 128000 | always_think+tool_use | low+high+max | - | - | - |
| 90 | `hyper/kimi-k2.7-code` | hyper | openai | `kimi-k2.7-code` | 256000 | - | 16000 | image_in+thinking+tool_use | - | - | - | - |
| 91 | `hyper/qwen3.7-plus` | hyper | openai | `qwen3.7-plus` | 1000000 | - | 64000 | image_in+thinking+tool_use | mini+low+medi+high | - | none | - |
| | **opencode-go** (openai) | | | | | | | | | | | |
| 92 | `opencode-go/mimo-v2.6-pro` | opencode-go | openai | `mimo-v2.6-pro` | 1048576 | - | 131072 | image_in+video_in+audio_in+thinking+tool_use | - | - | - | reasoning_content |
| 93 | `opencode-go/mimo-v2.5` | opencode-go | openai | `mimo-v2.5` | 1000000 | - | 128000 | image_in+video_in+audio_in+thinking+tool_use | - | - | - | reasoning_content |
| 94 | `opencode-go/grok-4.7` | opencode-go | openai_responses | `grok-4.7` | 500000 | - | 500000 | image_in+always_think+tool_use | low+medi+high+xhig | - | - | - |
| 95 | `opencode-go/longcat-2.5-preview-free` | opencode-go | openai | `longcat-2.5-preview-free` | 1000000 | - | 131072 | image_in+thinking+tool_use | - | - | - | reasoning_content |
| 96 | `opencode-go/glm-5.3-flash` | opencode-go | openai | `glm-5.3-flash` | 1000000 | - | 131072 | image_in+video_in+always_think+tool_use | low+high+max | - | - | reasoning_content |
| 97 | `opencode-go/qwen3.8-max` | opencode-go | anthropic | `qwen3.8-max` | 1000000 | - | 131072 | image_in+video_in+thinking+tool_use | low+medi+xhig | - | - | - |
| 98 | `opencode-go/kimi-k3` | opencode-go | openai | `kimi-k3` | 1048576 | - | 131072 | image_in+video_in+always_think+tool_use | max | - | - | reasoning_content |
| 99 | `opencode-go/deepseek-v4.1-flash` | opencode-go | openai | `deepseek-v4.1-flash` | 1000000 | - | 384000 | image_in+always_think+tool_use | low+high+max | - | - | reasoning_content |
| 100 | `opencode-go/deepseek-v4-flash-vision-exp` | opencode-go | openai | `deepseek-v4-flash-vision-exp` | 1000000 | - | 384000 | image_in+thinking+tool_use | low+high+max | - | - | reasoning_content |
| 101 | `opencode-go/longcat-2.0` | opencode-go | openai | `longcat-2.0` | 1000000 | - | 131072 | thinking+tool_use | - | - | - | reasoning_content |
| 102 | `opencode-go/space-bunny` | opencode-go | openai | `space-bunny` | 1048576 | 524288 | 524288 | image_in+video_in+always_think+tool_use | low+medi+high+xhig+max | - | - | reasoning_content |
| 103 | `opencode-go/minimax-m2.7` | opencode-go | anthropic | `minimax-m2.7` | 204800 | - | 131072 | thinking+tool_use | - | - | - | - |
| 104 | `opencode-go/mimo-v2.5-pro` | opencode-go | openai | `mimo-v2.5-pro` | 1048576 | - | 128000 | thinking+tool_use | - | - | - | reasoning_content |
| 105 | `opencode-go/mimo-v2.6-flash` | opencode-go | openai | `mimo-v2.6-flash` | 1048576 | - | 131072 | image_in+video_in+audio_in+thinking+tool_use | - | - | - | reasoning_content |
| 106 | `opencode-go/minimax-m3` | opencode-go | anthropic | `minimax-m3` | 1000000 | - | 131072 | image_in+video_in+thinking+tool_use | - | - | - | - |
| 107 | `opencode-go/gpt-5.6-luna` | opencode-go | openai_responses | `gpt-5.6-luna` | 1050000 | 922000 | 128000 | image_in+thinking+tool_use | low+medi+high+xhig+max | - | none | - |
| 108 | `opencode-go/qwen3.8-flash` | opencode-go | anthropic | `qwen3.8-flash` | 1000000 | - | 131072 | image_in+video_in+thinking+tool_use | low+medi+xhig | - | - | - |
| 109 | `opencode-go/glm-5.2` | opencode-go | openai | `glm-5.2` | 1000000 | - | 131072 | always_think+tool_use | high+max | - | - | reasoning_content |
| 110 | `opencode-go/hy3` | opencode-go | openai | `hy3` | 256000 | 192000 | 128000 | thinking+tool_use | low+high | - | none | - |
| 111 | `opencode-go/muse-spark-1.2-contributor` | opencode-go | openai_responses | `muse-spark-1.2-contributor` | 1048576 | - | 131072 | image_in+video_in+audio_in+always_think+tool_use | mini+low+medi+high+xhig | - | - | - |
| 112 | `opencode-go/claude-haiku-5-5` | opencode-go | anthropic | `claude-haiku-5-5` | 1000000 | - | 128000 | image_in+thinking+tool_use | low+medi+high+xhig+max | - | - | - |
| 113 | `opencode-go/gpt-6-luna` | opencode-go | openai_responses | `gpt-6-luna` | 1050000 | 922000 | 128000 | image_in+thinking+tool_use | low+medi+high+xhig+max | - | none | - |
| 114 | `opencode-go/deepseek-v4-pro` | opencode-go | openai | `deepseek-v4-pro` | 1000000 | - | 384000 | always_think+tool_use | high+max | - | - | reasoning_content |
| 115 | `opencode-go/hy4-preview` | opencode-go | openai | `hy4-preview` | 1024000 | - | 64000 | thinking+tool_use | high | - | none | - |
| 116 | `opencode-go/muse-spark-1.3-contributor` | opencode-go | openai_responses | `muse-spark-1.3-contributor` | 1048576 | - | 131072 | image_in+video_in+audio_in+always_think+tool_use | mini+low+medi+high+xhig | - | - | - |
| 117 | `opencode-go/step-5-preview-free` | opencode-go | openai | `step-5-preview-free` | 1000000 | 1000000 | 65536 | image_in+video_in+always_think+tool_use | low+medi+high | - | - | reasoning_content |
| 118 | `opencode-go/glm-5.3` | opencode-go | openai | `glm-5.3` | 1000000 | - | 131072 | always_think+tool_use | low+high+max | - | - | reasoning_content |
| 119 | `opencode-go/kimi-k2.7-code` | opencode-go | openai | `kimi-k2.7-code` | 262144 | - | 262144 | image_in+video_in+thinking+tool_use | - | - | - | reasoning_content |
| 120 | `opencode-go/grok-4.6` | opencode-go | openai_responses | `grok-4.6` | 500000 | - | 500000 | image_in+always_think+tool_use | low+medi+high+xhig | - | - | - |
| 121 | `opencode-go/qwen3.7-plus` | opencode-go | anthropic | `qwen3.7-plus` | 1000000 | - | 65536 | image_in+video_in+thinking+tool_use | - | - | - | - |
| 122 | `opencode-go/deepseek-v4-flash` | opencode-go | openai | `deepseek-v4-flash` | 1000000 | - | 384000 | always_think+tool_use | low+high+max | - | - | reasoning_content |
| | **openai-codex** (openai_responses) | | | | | | | | | | | |
| 123 | `openai-codex/gpt-6.1-sol` | openai-codex | openai_responses | `gpt-6.1-sol` | 500000 | - | - | image_in+thinking+tool_use | low+medi+high+xhig+max | - | - | - |
| 124 | `openai-codex/gpt-6.1-sol-high` | openai-codex | openai_responses | `gpt-6.1-sol` | 500000 | - | - | image_in+thinking+tool_use | low+medi+high+xhig+max | high* | - | - |
| 125 | `openai-codex/gpt-6-luna` | openai-codex | openai_responses | `gpt-6-luna` | 272000 | - | - | image_in+thinking+tool_use | - | - | - | - |
| | **devin** (openai) | | | | | | | | | | | |
| 126 | `devin/swe-2` | devin | openai | `swe-2` | 262144 | - | - | thinking | - | - | - | - |
| 127 | `devin/swe-2-medium` | devin | openai | `swe-2-medium` | 262144 | - | - | thinking | - | - | - | - |
| 128 | `devin/swe-2-high` | devin | openai | `swe-2-high` | 262144 | - | - | thinking | - | - | - | - |
| 129 | `devin/swe-2-max` | devin | openai | `swe-2-max` | 262144 | - | - | thinking | - | - | - | - |
| 130 | `devin/deepseek-v4-1-flash-high` | devin | openai | `deepseek-v4-1-flash-high` | 1048576 | - | - | thinking | - | - | - | - |
| 131 | `devin/deepseek-v4-1-flash-max` | devin | openai | `deepseek-v4-1-flash-max` | 1048576 | - | - | thinking | - | - | - | - |
| 132 | `devin/glm-5-3-flash-low` | devin | openai | `glm-5-3-flash-low` | 1048576 | - | - | thinking | - | - | - | - |
| 133 | `devin/glm-5-3-flash-high` | devin | openai | `glm-5-3-flash-high` | 1048576 | - | - | thinking | - | - | - | - |
| 134 | `devin/glm-5-3-flash-max` | devin | openai | `glm-5-3-flash-max` | 1048576 | - | - | thinking | - | - | - | - |
| | **xai-oauth** (openai) | | | | | | | | | | | |
| 135 | `xai-oauth/grok-4.7` | xai-oauth | openai | `grok-4.7` | 500000 | - | - | image_in+thinking+tool_use | low+medi+high+xhig | high | - | - |
| 136 | `xai-oauth/grok-4.6` | xai-oauth | openai | `grok-4.6` | 500000 | - | - | image_in+thinking+tool_use | low+medi+high+xhig | high | - | - |
| 137 | `xai-oauth/grok-4.5` | xai-oauth | openai | `grok-4.5` | 500000 | - | - | image_in+thinking+tool_use | low+medi+high+xhig | high | - | - |
| | **cursor** (openai) | | | | | | | | | | | |
| 138 | `cursor/composer-2.5-fast` | cursor | openai | `composer-2.5-fast` | 200000 | - | - | thinking | - | - | - | - |
| 139 | `cursor/cursor-grok-4.5-high-fast` | cursor | openai | `cursor-grok-4.5-high-fast` | 500000 | - | - | thinking | - | - | - | - |
| 140 | `cursor/composer-2.5` | cursor | openai | `composer-2.5` | 200000 | - | - | thinking | - | - | - | - |
| 141 | `cursor/cursor-grok-4.5-low-fast` | cursor | openai | `cursor-grok-4.5-low-fast` | 500000 | - | - | thinking | - | - | - | - |
| | **ds-flash-cascade** (openai) | | | | | | | | | | | |
| 142 | `cascade/deepseek-v4.1-flash` | ds-flash-cascade | openai | `deepseek-v4.1-flash` | 1048576 | - | - | thinking+tool_use | - | - | - | - |
| | **glm-flash-cascade** (openai) | | | | | | | | | | | |
| 143 | `cascade/glm-5.3-flash` | glm-flash-cascade | openai | `glm-5.3-flash` | 1048576 | - | - | thinking | - | - | - | - |

`*` = pinned via `[models.<alias>.overrides]`.
