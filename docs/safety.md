# Safety

tracepanel is for development. Its defaults keep it there.

**Off unless `DEBUG`.** With `DEBUG = False`, `tracepanel.django` installs nothing. Only an explicit
`TRACEPANEL_ENABLED=1`, `TRACEPANEL = {"enabled": True}` or `tracepanel run` turns it on without `DEBUG`.

**Local.** Traces are stored in `.tracepanel/` in your project (add it to `.gitignore`); the console is served by your
app. Nothing is sent anywhere.

**Development data.** Traces keep what helps you debug: SQL parameters (for `EXPLAIN`), local variables in errors,
email bodies, task arguments. In local variables, task arguments and log records, values under names that look like
secrets (passwords, tokens, keys) are masked. Turn each kind off with `capture_sql_params`, `capture_locals`,
`capture_mail_body` and `capture_task_args`.

**Switching the user** needs `DEBUG = True` even when tracepanel was turned on another way, `django.contrib.auth` and
sessions, and a request from this machine (or `INTERNAL_IPS`) coming from the page itself: a same-origin call with
tracepanel's header, which another site can't send. Turn it off with `user_switch = False`.
