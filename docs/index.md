# Tracepanel for Django

See what your Django app is really doing.

Tracepanel turns each request your app serves into a trace. The trace holds the request's SQL, cache calls,
templates, signals, emails, logs, the tasks it queues and the errors it raises, in the order they happened. Tracepanel
reads the trace and points at what to fix. It finds an N+1 and names the `select_related()` that removes it. It also
finds duplicate queries, slow SQL and transactions that hold their locks too long.

```bash
pip install django-tracepanel
```

```python
# settings.py
INSTALLED_APPS += ["tracepanel.django"]
```

That is the whole setup. With `DEBUG = True`, open any page of your app.

![Swagger UI with the panel docked under it, showing the requests made with Try it out and the call tree of one with two N+1 queries](assets/screenshots/panel-call-tree.png)

## What you get

**A panel on every page.** A badge in the corner shows the request's status, time, queries and issues. Click it to
open the panel. The panel docks at the bottom or on the right, like the browser's DevTools. It lists every request the
page made, including `fetch()` calls. For each request it shows the call tree, the SQL and the logs.

**A console at `/__tracepanel__/`.** The console shows everything the app did, beyond one page. It covers HTTP
endpoints, GraphQL operations, Celery and other tasks, management commands and WebSocket consumers. It draws charts
over time and searches across all of it.

![The console's HTTP page: requests and latency over time, the slowest and the failing endpoints](assets/screenshots/console-http.png)

**A line in the terminal.** Tasks and management commands have no page to show the panel on. Each task run and each
management command ends with a summary line and a link to its trace.

## How it differs from django-debug-toolbar

| | django-debug-toolbar | Tracepanel |
| --- | --- | --- |
| What it sees | the HTML page you are on | every request, `fetch()`, API call, task and command |
| JSON APIs, SPAs | needs a page to attach to | the same panel, and headers any client can read |
| Tasks | — | Celery, RQ, Dramatiq and Django Tasks: each run traced and linked to the request that queued it |
| Findings | the raw queries | N+1, duplicates, slow SQL, long transactions, errors, each with the fix in Django's terms |
| History | the current request | a local store of recent traces, searchable |

Nothing leaves your machine. Tracepanel keeps traces in a SQLite file in `.tracepanel/` in your project, and your own
app serves the console at its own address.
