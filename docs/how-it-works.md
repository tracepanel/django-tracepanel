# How it works

## At startup

`tracepanel.django` is a Django app. When Django calls its `ready()`, Tracepanel runs these steps:

1. It reads its settings ([Configuration](configuration.md)) and decides whether to turn on. It follows `DEBUG`, unless
   `TRACEPANEL_ENABLED` or `TRACEPANEL["enabled"]` says otherwise. If Tracepanel is off, it stops here.
2. It puts its middleware first in `MIDDLEWARE`, so it measures the whole request.
3. It installs its collectors. Where Django has a hook, Tracepanel uses it, such as the `connection_created` and
   `got_request_exception` signals. Where Django has none, Tracepanel wraps a few Django methods: the view call,
   `Template.render`, `Atomic`, `EmailMessage.send`, `Signal.send` and `BaseCommand.execute`. It installs each collector
   once.
4. It installs the [integrations](integrations.md) whose library is installed.

## A request

The middleware opens a trace for the request. The trace lives in a context variable, so everything the request runs
records into it. This includes async code and `sync_to_async` threads. The table shows how Tracepanel records each
part:

| What | How Tracepanel sees it |
| --- | --- |
| SQL | an execute wrapper on each database connection |
| Transactions | `atomic()` blocks, savepoints and `on_commit()` callbacks |
| The view | the call Django makes to it |
| Templates | `Template.render` |
| Cache | each backend of `django.core.cache.caches` |
| Signals | `Signal.send` and its variants, each receiver timed |
| Emails | `EmailMessage.send` |
| Logs | records as loggers pass them to their handlers |
| Errors | `got_request_exception` |

When the response is ready, Tracepanel adds the route from Django's URL resolver, the view and the status to the trace.
It also adds the user if the view loaded one. Tracepanel never queries for the user. Then a background thread sends
the trace to the Tracepanel agent.

Tracepanel adds the headers that the badge reads to the response: `Tracepanel-Id`, `Tracepanel-Url` and
`Server-Timing`. For an HTML page, it also adds the panel's script.

Requests under `/__tracepanel__/` go to the agent, which serves the console, its API and the panel's script. Your app
handles `EXPLAIN` and user switching itself, because it has the database connections and the sessions.

## The agent

`pip install django-tracepanel` installs the Tracepanel agent, which is a separate program. The first trace starts the
agent for the project, and each project has one agent. The agent keeps running across `runserver`'s reloads and
across workers. It exits after 30 minutes with nothing to do. The agent finds the issues in each trace
([What it finds](issues.md)), keeps the traces in a SQLite file under `.tracepanel/` and serves the console. The badge
shows a request's status and time at once. It shows the request's issues a moment later, once the agent has found
them.

`tracepanel dev` runs the agent in the foreground instead ([Command line](cli.md)). If the agent can't run, Tracepanel
prints the reason in the terminal. Requests still get their headers, but Tracepanel stores nothing.

## Outside requests

Each management command becomes a trace of its own, except servers, shells and workers. A task queued during a request
shows in the request's call tree. Each run of the task is a trace of its own, linked back to the request.

## The cost

Tracepanel is a development tool. Collecting a trace adds little to a request. Another thread sends the trace after
the response is made. The agent, which is another process, finds the issues and stores the trace. Tracepanel collects
nothing when it is off.
