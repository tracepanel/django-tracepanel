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

![Swagger UI with the panel docked under it: the requests made with Try it out, and the call tree of one with two N+1 queries](https://raw.githubusercontent.com/tracepanel/django-tracepanel/main/assets/panel-call-tree.png)

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

The panel also lists the requests your pages and tools make with `fetch()`,
here Swagger UI's Try it out. Each issue comes with its fix in Django's terms,
such as the `select_related()` that removes an N+1:

![The Issues tab of an API request made from Swagger UI: an N+1 with where it comes from and the fix](https://raw.githubusercontent.com/tracepanel/django-tracepanel/main/assets/panel-issues.png)

The console shows every endpoint over time, with the slowest and the failing
ones:

![The console's HTTP page: requests and latency over time, the slowest and the failing endpoints](https://raw.githubusercontent.com/tracepanel/django-tracepanel/main/assets/console-http.png)

Work without a page, such as Celery tasks, has its own pages:

![The console's Tasks page: runs and latency over time, the slowest and the failing tasks](https://raw.githubusercontent.com/tracepanel/django-tracepanel/main/assets/console-tasks.png)

## Supports

Django 5.2, 6.0 and 6.1 on Python 3.11 to 3.15, each pair tested in CI.
Django 6.x needs Python 3.12 or newer, and Python 3.15 runs with Django 6.1.

- **Django**: requests and views, sync and async, under `runserver` or any
  WSGI or ASGI server. Templates, Django's and Jinja2, with their context.
  The cache, signals, email, logins and logouts, file storages and
  `collectstatic`, management commands, `migrate` and its operations, and the
  App tab's settings, system checks and unapplied migrations.
- **Databases**: the ORM's queries and `atomic()` blocks on any database,
  tested on SQLite, PostgreSQL and SQL Server (mssql-django). Queries sent
  through a driver directly too: sqlite3, aiosqlite, psycopg, psycopg2,
  asyncpg, PyMySQL, mysqlclient, MySQL Connector, aiomysql, asyncmy,
  python-oracledb, pyodbc and pymssql. EXPLAIN on PostgreSQL, MySQL, SQLite
  and SQL Server. SQLAlchemy and MongoDB (PyMongo) as well.
- **APIs**: Django REST framework, Django Ninja, Graphene, Strawberry and
  htmx.
- **Background work**: Celery, Dramatiq, RQ, Huey, django-q2, Taskiq, Django
  Tasks (Django 6.0, or the `django-tasks` backport on 5.2) and Channels, its
  WebSocket consumers and workers.
- **Clients**: requests and anything else on urllib3, httpx, aiohttp, Redis
  and Valkey, AWS through boto3 and aiobotocore, and the OpenAI and Anthropic
  SDKs. Spans from OpenTelemetry instrumentations join the trace.
- **Profiling**: where a request's or a task's time goes, from the panel. Its
  memory too, when asked for.
- **Tests**: `pytest --tracepanel` fails a test that makes an N+1 or
  duplicate queries, with pytest-django and pytest-xdist.

## Documentation

The Django guide is at
[tracepanel.dev/docs/django](https://tracepanel.dev/docs/django): what
Tracepanel records in Django, its settings, workers and commands. The panel,
the console and the issues are the same in every framework, under
[tracepanel.dev/docs](https://tracepanel.dev/docs).

## License

Licensed under the [MIT License](LICENSE).
