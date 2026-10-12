# Safety

Tracepanel is a development tool. Its defaults keep it off outside development.

**Off unless `DEBUG`.** With `DEBUG = False`, `tracepanel.django` installs nothing. Only an explicit
`TRACEPANEL_ENABLED=1`, `TRACEPANEL = {"enabled": True}` or `tracepanel run` turns it on without `DEBUG`.

**Local.** Tracepanel stores traces in `.tracepanel/` in your project. Add that folder to `.gitignore`. Your app
serves the console, and Tracepanel sends nothing anywhere.

**Development data.** To help you debug, traces keep SQL parameters for `EXPLAIN`, local variables in errors, email
bodies and task arguments. Tracepanel masks values in local variables, task arguments and log records when their names
look like secrets, such as passwords, tokens and keys. Turn each kind of data off with `capture_sql_params`,
`capture_locals`, `capture_mail_body` and `capture_task_args`.

**Switching the user** needs `DEBUG = True`, even when you turned Tracepanel on another way. It also needs
`django.contrib.auth` and sessions. The request must come from this machine or from an address in `INTERNAL_IPS`. It
must also come from the page itself, as a same-origin call with Tracepanel's header, which another site can't send.
Turn user switching off with `user_switch = False`.
