# Getting started

Tracepanel supports Django 5.2 and newer on Python 3.11 and newer.

## Install

```bash
pip install django-tracepanel
```

`django-tracepanel` has no code of its own. Installing it is the same as `pip install "tracepanel[django]"`.

Add the app:

```python
# settings.py
INSTALLED_APPS += ["tracepanel.django"]
```

You don't add middleware or include URLs. The app puts its middleware first in `MIDDLEWARE`, so it measures the whole
request. The app also serves `/__tracepanel__/` itself.

## Turn it on

Tracepanel is on when `DEBUG = True`. Otherwise it does nothing, so it adds no middleware and patches nothing. Start
the server as usual:

```bash
python manage.py runserver
```

The first line in the terminal shows what Tracepanel turned on:

```text
tracepanel ▸ on (DEBUG) · Django · logging, Celery, DRF → console at /__tracepanel__/
```

Open any page, and a badge appears in the bottom right corner. Click it to open the panel. The console is at
`/__tracepanel__/`.

## Without changing settings

`tracepanel run` starts any command with Tracepanel on, without touching the project:

```bash
tracepanel run python manage.py runserver
tracepanel run celery -A config worker
```

It adds `tracepanel.django` to `INSTALLED_APPS` while Django reads the settings. It turns Tracepanel on even when
`DEBUG` is off, so you can look at production-like settings locally. If the app is already in `INSTALLED_APPS`,
`tracepanel run` changes nothing more. You still get one middleware and one trace per request.

## Workers and commands

A Celery worker or a management command has no page for the panel. Each task run and each command ends with a line in
the terminal:

```text
tracepanel ▸ task newsletter.tasks.send_digest · success · 230 ms · 14 queries · n+1 → http://127.0.0.1:8765/#/t/01M4…
```

The link opens the trace in the console. The Tracepanel agent serves this console even when no web server is
running. To run the agent in the foreground, on a port of your choice:

```bash
tracepanel dev
```

## Next

- [The panel and the console](panel.md) explains what each part shows.
- [What it finds](issues.md) lists the issues Tracepanel reports and how to fix them.
- [Configuration](configuration.md) lists every setting.
