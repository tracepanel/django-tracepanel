# The panel and the console

## The badge

Tracepanel adds a few headers to every response it traces. The badge on the page reads them and shows the status, the
total time, the number of queries and the number of issues. The badge appears on HTML pages. It also picks up the
`fetch()` and XHR calls the page makes, so a single-page app shows its API calls the same way.

## The panel

Click the badge to open the panel. The panel docks at the bottom of the page or on the right, and you can resize it.

![Swagger UI with the panel docked under it: the requests made with Try it out, and the call tree of one with two N+1 queries](assets/screenshots/panel-call-tree.png)

The left side lists the requests of this page, with the newest last. **Follow new** keeps the newest request selected
as new requests arrive.

The right side shows the selected request in tabs:

Request
:   The tab label shows the status and the time. The tab shows the URL, the route, the view, the user and every
    attribute of the trace.

Call tree
:   The tab shows what the request did, in order: middleware, the view, SQL, cache calls, templates, signals, emails,
    queued tasks and logs. A bar on top splits the time between framework, your code and the database. Filters narrow
    the tree to one kind of span. Similar queries fold into one row with a count.

Issues
:   The tab lists the issues Tracepanel found in this request, each with its fix. See [What it finds](issues.md).

SQL
:   The tab lists every query with its time and the place in your code it came from. **Explain** runs `EXPLAIN` on
    the query and shows the plan.

Logs, Mail, Error
:   These tabs show the request's log records, the emails it sent in text and HTML, and its error with the stack and
    local variables.

![The SQL tab of an API request: 101 queries folded into 3 statements, two of them N+1](assets/screenshots/panel-sql.png)

The panel opens on the tab you used last. A request with an error opens on **Error**.

**Explore** jumps from the request to related views in the console, such as the same endpoint over time or the same
query elsewhere. **Console** opens the trace in the console. The theme button switches between the light theme, the
dark theme and the system's theme.

### Switching the user

If your project installs `django.contrib.auth` and `django.contrib.sessions` and has `DEBUG = True`, the panel can log
you in as another user. Search by username, name or email, and the page reloads as that user. Custom user models work
too. Only requests from this machine or from `INTERNAL_IPS` can switch the user, and only from the page itself.

## The console

The console is at `/__tracepanel__/` on your app. The agent also serves it on its own address, and the terminal lines
link to that address. With `tracepanel dev`, the console is on port 8765.

**Entry points.** The console has one page per kind of work. A page appears once there is data for it:

- **HTTP** lists endpoints by route.
- **GraphQL** lists operations by name.
- **Tasks** lists Celery, Dramatiq, RQ and Django Tasks runs.
- **WebSockets** lists Channels consumers.
- **Jobs** lists management commands.

Each page starts with an overview of volume, errors, latency percentiles, and the slowest and the failing groups. Drag
on a chart to zoom into a time range. The list follows the overview. It shows the calls in groups, such as
**By endpoint** or **By task**, or shows every call.

![The HTTP page of the console](assets/screenshots/console-http.png)

Every trace opens on a page of its own, with the timeline, the time split and the call tree.

![A trace in the console: the timeline of its spans and its call tree](assets/screenshots/console-trace.png)

**Data.** The data pages are Services, Database, Emails, Logs and Issues. Services lists the databases, caches and
outside services your app talks to. Database shows queries across requests.

![The Database page: each statement across requests, how often it runs, how long it takes, where it comes from](assets/screenshots/console-database.png)

![The Logs page: log records of every request and task, with their level, logger and trace](assets/screenshots/console-logs.png)

### Search

The search box takes free text and filters. Some of the filters:

| Filter | Example |
| --- | --- |
| `status` | `status>=500` |
| `route` | `route:/api/*` |
| `duration` | `duration>500ms` |
| `queries` | `queries>20` |
| `task`, `state`, `queue` | `task:newsletter.* state:failure` |
| `user` | `user:42` |
| `since`, `until` | `since:1h` |

Type a key and the box suggests the rest. Finish a filter with a space or Enter to turn it into a chip.
