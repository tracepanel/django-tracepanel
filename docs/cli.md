# Command line

`pip install django-tracepanel` installs the `tracepanel` command.

## `tracepanel run`

```bash
tracepanel run [--set name=value]... <command>
```

Runs any command with Tracepanel on, such as `python manage.py runserver`, `gunicorn`, `uvicorn`, `celery` or
`pytest`. You don't change anything in the project. As Django reads its settings, `tracepanel run` adds
`tracepanel.django` to `INSTALLED_APPS`. Tracepanel is on even with `DEBUG = False`. `--set` sets a setting for this
run:

```bash
tracepanel run --set slow_sql_ms=50 python manage.py runserver
```

## `tracepanel dev`

```bash
tracepanel dev [--host 127.0.0.1] [--port 8765]
```

Runs the Tracepanel agent in the foreground. The agent receives the project's traces and serves the console on
http://127.0.0.1:8765/, with no Django running. Without `tracepanel dev`, the first trace starts the agent in the
background. Use this command to watch the agent's output, or to read the traces after the server has stopped. `EXPLAIN`
and switching the user need the app, so use them at `/__tracepanel__/`.

## `tracepanel mcp`

```bash
tracepanel mcp [--values]
```

Runs an MCP server on stdin and stdout for AI coding agents. A coding agent reads the project's traces and issues
through this server. Run the command from the project's directory. See [AI coding agents](ai-agents.md).

## `tracepanel config`

Prints every setting with its value and the place that set it. Then it prints each integration and its state: on,
not installed or turned off.

```text
slow_sql_ms           200     pyproject.toml [tool.tracepanel]
capture_locals        false   env TRACEPANEL_CAPTURE_LOCALS
...

integrations
  logging         on
  Celery          on
  DRF             on (Django apps only)
  Dramatiq        off: not installed
```
