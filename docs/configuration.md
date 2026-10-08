# Configuration

tracepanel works with no settings. Each setting can be set in four places; a later one wins over an earlier one:

1. `tracepanel.toml`, or `[tool.tracepanel]` in `pyproject.toml`, found from the project's directory upward;
2. the `TRACEPANEL` dict in Django's settings (`DEBUG` turns tracepanel on, `BASE_DIR` is the project's directory);
3. `tracepanel.core.conf.configure()` in code;
4. `TRACEPANEL_<NAME>` environment variables (lists comma-separated).

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

An unknown name or a wrong type is an error that names where it came from. `tracepanel config` prints every setting,
its value and the place it was set.

## Settings

| Setting | Default | What it does |
| --- | --- | --- |
| `enabled` | `DEBUG` | Whether tracepanel records anything. `TRACEPANEL_ENABLED` (set by `tracepanel run`) wins over `DEBUG`. |
| `root` | `BASE_DIR` | The project's directory: stack paths are shown relative to it, and the store lives in it. |
| `service` | the directory's name | This project's name on the service map. |
| `widget` | `true` | Add the panel's script to HTML pages. The headers are sent either way. |
| `prefix` | `/__tracepanel__/` | Where the console, its API and the panel's script are served. |
| `dir` | `.tracepanel` | The local store, relative to `root`. Add it to `.gitignore`. |
| `max_traces` | `2000` | Traces kept in the store; older ones are deleted. |
| `console_url` | `http://127.0.0.1:8765/` | Where `tracepanel console` serves: the terminal lines link to it. |
| `terminal_summary` | `true` | The line at startup and after each task and command. |
| `n_plus_one_threshold` | `3` | Similar queries from one place reported as an N+1. |
| `slow_sql_ms` | `100` | Queries slower than this are reported as slow SQL. |
| `long_transaction_ms` | `500` | Outer `atomic()` blocks longer than this are reported. |
| `capture_locals` | `true` | Keep local variables of your frames in errors (masked). |
| `capture_mail_body` | `true` | Keep the text and HTML of sent emails. |
| `capture_sql_params` | `true` | Keep query parameters, so the console can run `EXPLAIN`. |
| `capture_task_args` | `true` | Keep task arguments and results (masked). |
| `user_switch` | `true` | Let the panel log in as another user (also needs `DEBUG`). |
| `ignore_paths` | `/health*`, `/static/*`, `/media/*`, `/favicon.ico` | Requests not traced: glob patterns on the path. |
| `ignore_tasks` | none | Tasks not traced: glob patterns on the task name, e.g. `celery.backend_cleanup`. |
| `ignore_loggers` | none | Loggers left out, with their children. |
| `ignore_commands` | servers, shells and workers | Management commands not traced (`runserver`, `shell`, `test`, `rqworker`, …). |
| `celery_enabled`, `channels_enabled`, `django_tasks_enabled`, `dramatiq_enabled`, `drf_enabled`, `logging_enabled`, `ninja_enabled`, `rq_enabled`, `strawberry_enabled` | `true` | One per [integration](integrations.md): `false` leaves that library untouched. Read at startup. |
