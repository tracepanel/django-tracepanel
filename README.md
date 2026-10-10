# django-tracepanel

See what your Django app is really doing.

![Swagger UI with the panel docked under it: the requests made with Try it out, and the call tree of one with two N+1 queries](docs/assets/screenshots/panel-call-tree.png)

Every request, query and task of your Django app, traced: the SQL, cache calls, templates, signals, emails, logs and
errors of each request, the tasks it queues, and what is worth fixing (N+1 queries with the `select_related()` that
removes them, duplicates, slow SQL, long transactions).

This package has no code of its own: it installs [tracepanel](https://github.com/tracepanel/tracepanel-python) with
Django support, the same as `pip install "tracepanel[django]"`.

```bash
pip install django-tracepanel
```

## Setup

Add the app to your settings. It is on whenever `DEBUG = True`:

```python
# settings.py
INSTALLED_APPS += ["tracepanel.django"]
```

Or leave the settings as they are and start the server through `tracepanel run`, which also turns Tracepanel on with
`DEBUG = False`:

```bash
tracepanel run python manage.py runserver
```

Then open any page: the panel is at the bottom, and `/__tracepanel__/` is the console.

## What it looks like

Requests your pages and tools make with `fetch()` (here, Swagger UI's Try it out) show up in the panel too, each with
the fix for what is wrong, in Django's terms:

![The Issues tab of an API request made from Swagger UI: an N+1 with where it comes from and the fix](docs/assets/screenshots/panel-issues.png)

The console shows every endpoint over time, with the slowest and the failing ones:

![The console's HTTP page: requests and latency over time, the slowest and the failing endpoints](docs/assets/screenshots/console-http.png)

And the work that has no page, such as Celery tasks:

![The console's Tasks page: runs and latency over time, the slowest and the failing tasks](docs/assets/screenshots/console-tasks.png)

## Documentation

The documentation is in `docs/` (MkDocs with Material): `uv run poe docs` serves it at http://127.0.0.1:8000/,
`uv run poe docs-build` builds it the way CI does.
