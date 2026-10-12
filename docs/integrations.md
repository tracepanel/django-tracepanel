# Integrations

Tracepanel records these parts of Django with no setup: SQL, transactions and `on_commit()`, the view, templates, the
cache, signals, emails, management commands and `sync_to_async`. For SQL, it records every connection and the `async`
ORM.

Tracepanel also traces the libraries it finds installed. Each integration is on as soon as its library is installed.
To turn one off, use its setting, such as `drf_enabled = False` or `TRACEPANEL_DRF_ENABLED=false`. `tracepanel config`
lists the integrations and shows which are on.

| Integration | Setting | What you get |
| --- | --- | --- |
| logging | `logging_enabled` | Log records of the request, attached to the span they were logged in. Tracepanel adds no handler, so your logging setup stays the same. |
| Django REST framework | `drf_enabled` | The view named after the ViewSet action (`PostViewSet.list`). Auth, permissions with the class that refused and why, throttles, validation with the 400's errors, and serialization as steps. |
| Django Ninja | `ninja_enabled` | The view named after the operation's function. Auth, input validation with the 422's errors, and response serialization as steps. |
| Celery | `celery_enabled` | Each task run as a trace, linked to the request that queued it. Retries and failures, arguments and results. |
| RQ | `rq_enabled` | The same for RQ jobs, through RQ's forking worker. |
| Dramatiq | `dramatiq_enabled` | The same for Dramatiq actors. |
| Django Tasks | `django_tasks_enabled` | The same for `django.tasks` and the `django-tasks` backport. |
| Channels | `channels_enabled` | WebSocket events as traces. Group messages linked to their sender. |
| Strawberry | `strawberry_enabled` | GraphQL requests named after the operation, and resolvers as spans. Tracepanel records errors returned with HTTP 200. |
| OpenTelemetry | `otel_enabled` | Spans from the OpenTelemetry instrumentations you enable (httpx, requests, redis, boto3, gRPC…) in the call tree, and the services they call on the Services map. See below. |

## OpenTelemetry

A library that Tracepanel has no integration for may have an OpenTelemetry instrumentation. Enable the instrumentation
as usual. Its spans show up in the request, task or job they ran in, under the span that was current:

```python
from opentelemetry import trace
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.sdk.trace import TracerProvider

trace.set_tracer_provider(TracerProvider())  # or your own, with its exporters; or `opentelemetry-instrument`
HTTPXClientInstrumentor().instrument()
```

Tracepanel joins the `TracerProvider` that the project sets, before or after Django starts. Tracepanel never sets a
provider itself, so the exporters you configured for it keep working. Tracepanel drops OpenTelemetry spans for what it
records itself, such as Django, SQL, Celery and logging, so nothing shows twice. The integration needs
`opentelemetry-sdk`, which a project that uses OpenTelemetry already has.

## Tasks

A task queued during a request shows in the request's call tree. Each run of the task is a trace of its own that links
back to the request.

![The console's Tasks page: runs and latency over time, the slowest and the failing tasks](assets/screenshots/console-tasks.png)

A worker started with `tracepanel run`, or with `tracepanel.django` in `INSTALLED_APPS`, prints a line per task with a
link to its trace:

```bash
tracepanel run celery -A config worker
```

## Settings changed at startup

Tracepanel installs the integrations when the app starts. After you change an `*_enabled` setting, restart the app.
