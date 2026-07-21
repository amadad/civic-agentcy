# CLAUDE.md

civic-cli-tools — policy research CLI. Gemini + 8 data sources.

## Commands

```bash
uv sync                          # install
uv run civic "topic"             # all sources
uv run civic "topic" -s federal  # federal only
uv run civic "topic" -s state:CA # state only
uv run civic "topic" -s policy   # policy-primary sources only
uv run civic "topic" -v          # verbose
uv run civic "topic" -f json     # JSON output (for agents)
uv run civic "topic" --limit 10  # per-tool results cap (default 25)
uv run civic "topic" --since 2026-01-01  # filter results to items on/after date
uv run civic "topic" --no-review # skip reviewer pass (faster)
uv run civic -                   # read topic from stdin
uv run civic run <preset>        # run named preset (markdown brief)
uv run civic signals --direct --topic "X" -s federal # source fan-out; no Gemini
uv run civic signals <preset>    # model-selected signals for interactive use
uv run civic topics              # list presets
uv run civic doctor              # validate required/optional API keys
uv run civic get <url>           # fetch URL content (raw | JSON envelope)
uv run civic cache stats         # cache size + entries
uv run civic cache clear         # purge cached responses
```

Honors `NO_COLOR` and auto-disables Rich formatting when stdout is not a TTY.

`civic signals --direct` is the automation seam: it invokes each available
adapter for the selected scope once, in parallel, and emits atomic JSON without
Gemini or writes. Hound owns workflow state, approvals, and canonical changes.
Signals mode without `--direct` retains model-selected research for interactive
use. Both paths preserve movement metadata and movement-aware bill IDs.

## Files

```
src/
├── cli.py              # entry, scope parsing, --format json, run/signals/doctor/get subcommands
├── _agent_cli.py       # minimal doctor helpers shared by the CLI
├── agents.py           # gemini, multi-tool loop, parallel execution
├── scopes.py           # shared scope parsing + labeling helpers
├── prompts.py          # system prompts
├── output.py           # markdown + JSON output (synthesis mode)
├── output_signals.py   # per-finding atomic JSON (for web-pulse and similar consumers; schema v1)
└── tools/
    ├── base.py            # BaseTool, ToolResult helpers, retry, caching, set_results_limit
    ├── models.py          # Finding, ToolResult, ResearchResults
    ├── declarations.py    # Gemini function specs
    ├── registry.py        # tool name → execution + ToolResult formatting
    └── implementations.py # 8 tool implementations
```

## Tools

| Tool | API | Key |
|------|-----|-----|
| web_search | Exa | EXA_API_KEY |
| academic_search | Semantic Scholar | — |
| census_search | US Census | CENSUS_API_KEY (optional) |
| congress_search | Congress.gov | CONGRESS_GOV_API_KEY |
| federal_register_search | Federal Register | — |
| regulations_search | Regulations.gov | REGULATIONS_GOV_API_KEY |
| court_search | CourtListener | — |
| state_legislation_search | OpenStates + LegiScan fallback | OPENSTATES_API_KEY or LEGISCAN_API_KEY (single-state fallback) |

## Scope

- `federal` → web, academic, census, congress, federal_register, regulations, court
- `state:XX` → web, academic, census, state_legislation
- `news` → web only
- `policy` → congress, federal_register, regulations, court, state_legislation
- `all` → all 8 tools

Tools gated by optional API keys are omitted from Gemini's tool list when the key is missing; the rest of the run still proceeds. ToolRegistry only executes tools that are currently available for the requested scope, so out-of-scope tool calls are rejected instead of leaking broader research into policy-only runs. LegiScan is only exposed for single-state scopes and is used as a situational fallback for state legislation search.

## Model

`gemini-3.1-flash-lite-preview` in `src/agents.py:MODEL` (configurable via `CIVIC_MODEL` env var)
