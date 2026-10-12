# AI coding agents

A coding agent such as Claude Code, Cursor, Codex or Copilot reads your code, but it can't see what the code does when
it runs. It doesn't know how many queries a page makes, where the N+1 is or what failed. `tracepanel mcp` gives the
agent this information. It is an [MCP](https://modelcontextprotocol.io) server that answers from the project's traces.
Its answers are short, and each issue comes with its place in the code and its fix.

With the server, the agent can run this loop without you:

1. You ask "Why is `/api/orders` slow?" The agent finds the request and its issue. It is an N+1 with 50 queries at
   `shop/api.py:40`, and the fix is to add `select_related()`.
2. The agent changes the code.
3. The agent makes the request again with curl or a test, and waits for its trace.
4. The agent compares the two traces. Queries drop from 101 to 3, the time drops from 31 ms to 4 ms, and the issues
   are fixed.

## Connect it

The server runs from the project's directory, because it finds `.tracepanel/` there.

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

Without uv, use the `tracepanel` command from the project's virtualenv: `.venv/bin/tracepanel mcp`.

Then run the app as usual with `python manage.py runserver`, and ask the agent.

## Tools

| Tool | What it answers |
| --- | --- |
| `find_traces` | Recent requests, tasks and commands with their duration, SQL and issues. Takes a [search](panel.md#search). |
| `get_trace` | One trace: issues with place and fix, the error with its stack, the call tree with repeats folded (`SELECT auth_user ×50`), warnings, related tasks. `focus` takes `issues`, `tree`, `sql` or `logs`. |
| `wait_for_trace` | Waits for the next trace that matches a search such as `route:/api/orders`, and returns it. The agent makes the request, then checks the trace. |
| `compare_traces` | Before and after: time, queries, statements, issues fixed and new. |
| `list_issues`, `get_issue` | The project's issues, one per place in the code. `get_issue` returns one issue in detail with its latest traces. |
| `list_endpoints` | Endpoints by traffic: p50, p95, queries per call, errors. |
| `list_queries` | SQL across all traces: how often it runs, how slow it is and where it comes from. |
| `search_logs` | Log records with their trace. |

The tools only read. An answer stays under about 4 000 tokens. The call tree keeps the branches with issues, errors
and most of the time, and it says how much it left out.

## What the model sees

An agent sends its tool answers to its model's provider. So by default, the answers leave out the values in your
data. SQL comes without its parameters (`WHERE id = %s`), and errors come without their local variables. The answers
do include log messages, paths and the names of views and tasks.

`tracepanel mcp --values` adds SQL parameters and local variables. Tracepanel masks values under names that look like
secrets, such as passwords, tokens and keys, with or without `--values`.
