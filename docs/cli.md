# Command line

`pip install django-tracepanel` installs the `tracepanel` command.

## `tracepanel run`

```bash
tracepanel run [--set name=value]... <command>
```

Runs any command with tracepanel on: `python manage.py runserver`, `gunicorn`, `uvicorn`, `celery`, `pytest`. Nothing in
the project changes: Django gets `tracepanel.django` in `INSTALLED_APPS` as it reads its settings, and tracepanel is on
even with `DEBUG = False`. `--set` sets a setting for this run:

```bash
tracepanel run --set slow_sql_ms=50 python manage.py runserver
```

## `tracepanel console`

```bash
tracepanel console [--host 127.0.0.1] [--port 8765] [--dir .tracepanel]
```

Serves the console from the project's store, with no Django running: for a project whose only work is in workers, or
to read the traces after the server has stopped. The terminal lines of tasks and commands link to it. Read only:
`EXPLAIN` and switching the user need the app.

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
