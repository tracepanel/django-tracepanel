# Getting started

Tracepanel supports Django 5.2 and newer on Python 3.11 and newer.

## Install

```bash
pip install django-tracepanel
```

`django-tracepanel` has no code of its own: it is the same as `pip install "tracepanel[django]"`.

Add the app:

```python
# settings.py
INSTALLED_APPS += ["tracepanel.django"]
```

There is no middleware to add and no URL to include: the app puts its middleware first in `MIDDLEWARE` (so it measures
the whole request) and answers under `/__tracepanel__/` itself.

## Turn it on

Tracepanel is on when `DEBUG = True`, and does nothing at all otherwise: no middleware, no patches. Start the server as
usual:

```bash
python manage.py runserver
```

The first line in the terminal says what is on:

```text
tracepanel ▸ on (DEBUG) · Django · logging, Celery, DRF → console at /__tracepanel__/
```

Open any page: a badge appears in the bottom right corner. Click it for the panel. `/__tracepanel__/` is the console.

## Without changing settings

`tracepanel run` starts any command with Tracepanel on, without touching the project:

```bash
tracepanel run python manage.py runserver
tracepanel run celery -A config worker
```

It adds `tracepanel.django` to `INSTALLED_APPS` as Django reads the settings, and turns Tracepanel on even when
`DEBUG` is off (useful to look at production-like settings locally). With the app already in `INSTALLED_APPS`, it
changes nothing more: one middleware, one trace per request.

## Workers and commands

A Celery worker or a management command has no page for the panel. Each task run and each command ends with a line in
the terminal:

```text
tracepanel ▸ task newsletter.tasks.send_digest · success · 230 ms · 14 queries · n+1 → http://127.0.0.1:8765/#/t/01M4…
```

The link opens the trace in the console, which the Tracepanel agent serves even with no web server running. To run
it in the foreground, on a port of your choice:

```bash
tracepanel dev
```

## Next

- [The panel and the console](panel.md): what each part shows.
- [What it finds](issues.md): the issues Tracepanel reports, and how to fix them.
- [Configuration](configuration.md): every setting.
