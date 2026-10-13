# django-tracepanel

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

## Supported versions

Django 5.2, 6.0 and 6.1 on Python 3.11 and newer. Django 6.x needs Python 3.12
or newer, and Python 3.15 runs with Django 6.1.

## Documentation

The documentation is at
[tracepanel.dev/docs/django](https://tracepanel.dev/docs/django): what
Tracepanel records in Django, its settings, workers and commands. The panel,
the console and the issues are the same in every framework, under
[tracepanel.dev/docs](https://tracepanel.dev/docs).

## License

Licensed under the [MIT License](LICENSE).
