# How it works

## At startup

`tracepanel.django` is a Django app. When Django calls its `ready()`:

1. tracepanel reads its settings ([Configuration](configuration.md)) and decides whether it is on: `DEBUG`, unless
   `TRACEPANEL_ENABLED` or `TRACEPANEL["enabled"]` says otherwise. Off, it stops here.
2. It puts its middleware first in `MIDDLEWARE`, so it measures the whole request.
3. It installs its collectors: Django's own hooks where Django has them (signals such as `connection_created` and
   `got_request_exception`), and a wrapper on a few Django methods where it doesn't (the view call, `Template.render`,
   `Atomic`, `EmailMessage.send`, `Signal.send`, `BaseCommand.execute`). Each is put in place once.
4. It installs the [integrations](integrations.md) whose library is there.

## A request

The middleware opens a trace for the request. The trace lives in a context variable, so everything the request runs
records into it, in async code and `sync_to_async` threads too:

| What | How tracepanel sees it |
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

When the response is ready, the trace gets its route (from Django's URL resolver), its view, its status and the user,
if the view loaded one (tracepanel never queries for it). Then it is analysed ([What it finds](issues.md)) and handed
to a background writer that stores it in SQLite under `.tracepanel/`.

The response gets the headers the badge reads (`Tracepanel-Id`, `Tracepanel-Url`, `Server-Timing`) and, for an HTML
page, the panel's script.

Requests under `/__tracepanel__/` are answered by tracepanel itself: the console, its API and the panel's script.

## Outside requests

Management commands become traces of their own (servers, shells and workers excepted). Tasks queued during a request
show in its call tree; their runs are traces of their own, linked back to it.

## The cost

tracepanel is a development tool. Collecting a trace adds little to a request; analysing it and writing it to SQLite
happen after the response is made, on another thread. Nothing is collected when tracepanel is off.
