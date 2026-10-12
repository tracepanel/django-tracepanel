# Configuration

Tracepanel works with no settings. You can set each setting in four places, and a later place wins over an earlier
one:

1. `tracepanel.toml`, or `[tool.tracepanel]` in `pyproject.toml`. Tracepanel looks for them from the project's
   directory upward.
2. The `TRACEPANEL` dict in Django's settings. In Django's settings, `DEBUG` turns Tracepanel on and `BASE_DIR` is the
   project's directory.
3. `tracepanel.core.conf.configure()` in code.
4. `TRACEPANEL_<NAME>` environment variables. A list takes comma-separated values.

```python
# settings.py
TRACEPANEL = {
    "slow_sql_ms": 200,
    "ignore_paths": ["/health*", "/static/*"],
}
```

```toml
# pyproject.toml
[tool.tracepanel]
slow_sql_ms = 200
```

```bash
TRACEPANEL_SLOW_SQL_MS=200 python manage.py runserver
```

Tracepanel reports an unknown name or a wrong type as an error, and the error names where the value came from.
`tracepanel config` prints every setting, its value and the place that set it.

## Settings

| Setting | Default | What it does |
| --- | --- | --- |
| `enabled` | `DEBUG` | Whether Tracepanel records anything. `TRACEPANEL_ENABLED`, which `tracepanel run` sets, wins over `DEBUG`. |
| `root` | `BASE_DIR` | The project's directory. Stack paths are relative to it, and the store lives in it. |
| `service` | the directory's name | This project's name on the service map. |
| `widget` | `true` | Add the panel's script to HTML pages. Tracepanel sends the headers either way. |
| `prefix` | `/__tracepanel__/` | The path that serves the console, its API and the panel's script. |
| `dir` | `.tracepanel` | The project's store, relative to `root`. Add it to `.gitignore`. |
| `max_traces` | `2000` | The number of traces the store keeps. Tracepanel deletes older ones. |
| `agent` | `auto` | `auto` uses the project's agent, which the first trace starts. An address such as `tcp:host.docker.internal:7701` points to an agent outside a container. `off` keeps nothing. |
| `console_url` | `http://127.0.0.1:8765/` | The console of an agent set by address. |
| `terminal_summary` | `true` | Print a line at startup and after each task and command. |
| `n_plus_one_threshold` | `3` | How many similar queries from one place Tracepanel reports as an N+1. |
| `slow_sql_ms` | `100` | Tracepanel reports queries slower than this as slow SQL. |
| `long_transaction_ms` | `500` | Tracepanel reports outer `atomic()` blocks longer than this. |
| `capture_locals` | `true` | Keep the local variables of your frames in errors, masked. |
| `capture_mail_body` | `true` | Keep the text and HTML of sent emails. |
| `capture_sql_params` | `true` | Keep query parameters, so the console can run `EXPLAIN`. |
| `capture_task_args` | `true` | Keep task arguments and results, masked. |
| `user_switch` | `true` | Let the panel log in as another user. This also needs `DEBUG`. |
| `ignore_paths` | `/health*`, `/static/*`, `/media/*`, `/favicon.ico` | Glob patterns on the path of requests that Tracepanel doesn't trace. |
| `ignore_tasks` | none | Glob patterns on the name of tasks that Tracepanel doesn't trace, e.g. `celery.backend_cleanup`. |
| `ignore_loggers` | none | Loggers that Tracepanel leaves out, with their children. |
| `ignore_commands` | servers, shells and workers | Management commands that Tracepanel doesn't trace (`runserver`, `shell`, `test`, `rqworker`, …). |
| `celery_enabled`, `channels_enabled`, `django_tasks_enabled`, `dramatiq_enabled`, `drf_enabled`, `logging_enabled`, `ninja_enabled`, `otel_enabled`, `rq_enabled`, `strawberry_enabled` | `true` | One per [integration](integrations.md). `false` leaves that library untouched. Tracepanel reads these at startup. |
