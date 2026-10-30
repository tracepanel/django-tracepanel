# django-tracepanel

[![CI](https://github.com/tracepanel/django-tracepanel/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/tracepanel/django-tracepanel/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/django-tracepanel)](https://pypi.org/project/django-tracepanel/)
[![Python](https://img.shields.io/pypi/pyversions/django-tracepanel)](https://pypi.org/project/django-tracepanel/)
[![Django](https://img.shields.io/pypi/frameworkversions/django/django-tracepanel)](https://pypi.org/project/django-tracepanel/)

**See what your Django app is really doing.** Tracepanel records each request,
Celery task and management command of your Django app with its SQL queries,
cache calls, Redis commands, outgoing HTTP calls, templates, signals, emails,
logs and errors. It points out N+1 queries and calls, duplicates, slow SQL and
slow HTTP calls, and long transactions, and names the line of code to fix.

[![A 40-second demo: Swagger UI's Try it out on an endpoint, and the panel docked under it with the request's call tree, an N+1 with its query plan, a background task, its profile, and the same call after the fix](https://raw.githubusercontent.com/tracepanel/django-tracepanel/main/assets/demo-video.jpg)](https://tracepanel.dev/video/demo.mp4)

▶ [Watch the 40-second demo](https://tracepanel.dev/video/demo.mp4)

## Works with

| | Supported |
| --- | --- |
| **Python and Django** | Django 5.2 on Python 3.11 to 3.14, Django 6.0 on 3.12 to 3.14, Django 6.1 on 3.12 to 3.15. Each pair is tested in CI. |
| **Django** | Views, sync and async, under `runserver` or any WSGI or ASGI server. Templates, Django's and Jinja2. Cache, signals, email, logins, file storages, `collectstatic`, management commands, `migrate`, system checks. |
| **Databases** | PostgreSQL, MySQL, SQLite, SQL Server and Oracle, through the ORM or a driver directly. EXPLAIN on all but Oracle. SQLAlchemy and MongoDB. |
| **APIs** | Django REST framework, Django Ninja, Graphene, Strawberry, htmx. |
| **Background work** | Celery, Dramatiq, RQ, Huey, django-q2, Taskiq, Django Tasks, Channels. |
| **Clients** | requests and urllib3, httpx, aiohttp, Redis and Valkey, AWS through boto3 and aiobotocore, the OpenAI and Anthropic SDKs. Spans from OpenTelemetry instrumentations join the trace. |
| **Profiling** | Where a request's or a task's time goes, and its memory when you ask for it. |
| **Tests** | `pytest --tracepanel` fails a test that makes an N+1 or duplicate queries. |

The drivers, the versions of each library and the settings are in the
[Django guide](https://tracepanel.dev/docs/django).

This package has no code of its own. It installs
[tracepanel](https://github.com/tracepanel/tracepanel-python) with Django
support, the same as `pip install "tracepanel[django]"`.

```bash
pip install django-tracepanel
```

## Setup

Add the app to your settings. It is on whenever `DEBUG = True`.

```python
# settings.py
INSTALLED_APPS += ["tracepanel.django"]
```

To leave the settings as they are, start the server through `tracepanel run`
instead. It turns Tracepanel on even with `DEBUG = False`.

```bash
tracepanel run python manage.py runserver
```

Open any page and click the badge in the corner to open the panel. The console
is at `/__tracepanel__/`.

## What it looks like

Each request shows its call tree, with the SQL queries, the calls and the
issues in it:

![Swagger UI's endpoint run with Try it out and the start of its 200 response, and the panel docked under it with the same request's call tree and its two N+1 queries](https://raw.githubusercontent.com/tracepanel/django-tracepanel/main/assets/panel-call-tree.png)

The panel also lists the requests your pages and tools make with `fetch()`,
here Swagger UI's Try it out. Each issue comes with its fix in Django's terms,
such as the `select_related()` that removes an N+1:

![Swagger UI's endpoint run with Try it out, and the panel docked under it on that request's Issues tab: each N+1 with where it comes from and the fix](https://raw.githubusercontent.com/tracepanel/django-tracepanel/main/assets/panel-issues.png)

The console shows every endpoint over time, with the slowest and the failing
ones:

![The console's HTTP page: requests and latency over time, the slowest and the failing endpoints](https://raw.githubusercontent.com/tracepanel/django-tracepanel/main/assets/console-http.png)

Work outside a request, such as Celery tasks, has its own pages:

![The console's Tasks page: runs and latency over time, the slowest and the failing tasks](https://raw.githubusercontent.com/tracepanel/django-tracepanel/main/assets/console-tasks.png)

## Documentation

The Django guide is at
[tracepanel.dev/docs/django](https://tracepanel.dev/docs/django): what
Tracepanel records in Django, its settings, workers and commands. The panel,
the console and the issues are the same in every framework, under
[tracepanel.dev/docs](https://tracepanel.dev/docs).

## License

Licensed under the [MIT License](LICENSE).
