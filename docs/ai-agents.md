# AI coding agents

A coding agent (Claude Code, Cursor, Codex, Copilot) reads your code but can't see what it does when it runs: how many
queries a page makes, where the N+1 is, what failed. `tracepanel mcp` gives it that: an
[MCP](https://modelcontextprotocol.io) server that answers from the project's traces, compactly, with each issue's place
in the code and its fix.

The loop it makes possible, without you in the middle:

1. "Why is `/api/orders` slow?" The agent finds the request: N+1, 50 queries, `shop/api.py:40`, add `select_related()`.
2. It changes the code.
3. It makes the request again (curl, a test) and waits for its trace.
4. It compares the two: 101 queries → 3, 31 ms → 4 ms, the issues fixed. Done.

## Connect it

The server runs from the project's directory: that is where it finds `.tracepanel/`.

=== "Claude Code"

    ```bash
    claude mcp add --scope project tracepanel -- uv run tracepanel mcp
    ```

=== "Cursor"

    `.cursor/mcp.json`:

    ```json
    {"mcpServers": {"tracepanel": {"command": "uv", "args": ["run", "tracepanel", "mcp"]}}}
    ```

=== "VS Code"

    `.vscode/mcp.json`:

    ```json
    {"servers": {"tracepanel": {"type": "stdio", "command": "uv", "args": ["run", "tracepanel", "mcp"]}}}
    ```

=== "Codex"

    `.codex/config.toml`:

    ```toml
    [mcp_servers.tracepanel]
    command = "uv"
    args = ["run", "tracepanel", "mcp"]
    ```

Without uv, use the `tracepanel` of the project's virtualenv: `.venv/bin/tracepanel mcp`.

Then run the app as usual (`python manage.py runserver`) and ask.

## Tools

| Tool | What it answers |
| --- | --- |
| `find_traces` | Recent requests, tasks and commands: what, how long, SQL, issues. Takes a [search](panel.md#search). |
| `get_trace` | One trace: issues with place and fix, the error with its stack, the call tree with repeats folded (`SELECT auth_user ×50`), warnings, related tasks. `focus`: `issues`, `tree`, `sql`, `logs`. |
| `wait_for_trace` | Waits for the next trace that matches, e.g. `route:/api/orders`, and returns it: the agent makes the request, then checks it. |
| `compare_traces` | Before and after: time, queries, statements, issues fixed and new. |
| `list_issues`, `get_issue` | The project's issues, one per place in the code; one in detail with its latest traces. |
| `list_endpoints` | Endpoints by traffic: p50, p95, queries per call, errors. |
| `list_queries` | SQL across all traces: how often, how slow, where from. |
| `search_logs` | Log records with their trace. |

The tools only read. An answer stays under about 4 000 tokens: the call tree keeps the branches with issues, errors and
most of the time, and says how much it left out.

## What the model sees

An agent's tool answers go to its model's provider. So by default they carry the shape of your data, not the data:
SQL without its parameters (`WHERE id = %s`), errors without their local variables. Log messages, paths and names of
views and tasks are shown.

`tracepanel mcp --values` adds SQL parameters and local variables; values under names that look like secrets
(passwords, tokens, keys) are masked either way.
