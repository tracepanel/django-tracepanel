# Command line

`pip install django-tracepanel` installs the `tracepanel` command.

## `tracepanel run`

```bash
tracepanel run [--set name=value]... <command>
```

Runs any command with Tracepanel on: `python manage.py runserver`, `gunicorn`, `uvicorn`, `celery`, `pytest`. Nothing in
the project changes: Django gets `tracepanel.django` in `INSTALLED_APPS` as it reads its settings, and Tracepanel is on
even with `DEBUG = False`. `--set` sets a setting for this run:

```bash
tracepanel run --set slow_sql_ms=50 python manage.py runserver
```

## `tracepanel dev`

```bash
tracepanel dev [--host 127.0.0.1] [--port 8765]
```

Runs the Tracepanel agent in the foreground: it receives the project's traces and serves the console on
http://127.0.0.1:8765/, with no Django running. Without it the first trace starts the agent in the background, so this
is for watching its output, or for reading the traces after the server has stopped. `EXPLAIN` and switching the user
need the app: they are at `/__tracepanel__/`.

## `tracepanel mcp`

```bash
tracepanel mcp [--values]
```

An MCP server on stdin and stdout for AI coding agents: they read the project's traces and issues through it. Run from
the project's directory; see [AI coding agents](ai-agents.md).

## `tracepanel config`

Prints every setting, its value and where it was set, then the integrations: on, not installed, or turned off.

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
