# What it finds

Tracepanel reads every trace as it ends and reports what is worth fixing. Each issue names the line of your code it
comes from, called the culprit, and says how to fix it in Django's terms. The panel shows issues in the **Issues** tab
and in the badge's count. The console's **Issues** page groups them across requests. Tasks and commands show them in
their terminal line.

![The Issues tab of an API request made from Swagger UI: an N+1 with where it comes from and the fix](assets/screenshots/panel-issues.png)

![The console's Issues page: issues grouped across requests, with the endpoints they happen on and how often](assets/screenshots/console-issues.png)

## N+1 queries

An N+1 is the same query, run once per row of an earlier result:

```python
for post in Post.objects.all():
    print(post.author.name)  # one SELECT per post
```

Similar queries are the same statement with different parameters. Tracepanel reports an N+1 when similar queries run
from the same place at least `n_plus_one_threshold` times. The default is 3. The fix depends on the relation:

- For a ForeignKey or one-to-one relation looked up by its key, use `select_related("author")`. It makes one query
  with a join.
- For a reverse or many-to-many relation, use `prefetch_related("tags")`. It makes one extra query for all rows.

An N+1 inside library code still counts when your view started it. For example, Tracepanel reports a nested DRF
serializer that reads `author.username` against the view. In GraphQL resolvers, the hint suggests a DataLoader.

## Duplicate queries

Tracepanel reports a query that runs more than once in a request with the same parameters. Run it once and reuse the
result.

## Slow SQL

Tracepanel reports a query slower than `slow_sql_ms`. The default is 100 ms. **Explain** on the query shows the plan
and points at full scans.

## Long transactions

Tracepanel reports an outer `atomic()` block that stays open longer than `long_transaction_ms`. The default is
500 ms. The rows the block locked stay locked until `COMMIT`. Keep slow work such as HTTP calls, emails and heavy Python
out of the block. `on_commit()` callbacks run after the commit, and Tracepanel doesn't count them.

## Work inside a transaction

Some work inside `atomic()` should wait for the commit:

| Inside `atomic()` | Why it matters | Fix |
| --- | --- | --- |
| Queueing a task | a worker can run it before `COMMIT` and not see the data, or after a rollback | `transaction.on_commit(lambda: task.delay(...))` |
| Sending an email | it goes out even if the transaction rolls back | `transaction.on_commit(...)` |
| An HTTP call | the transaction holds its locks while the other service answers | call before `atomic()`, or in `on_commit()` |

## Errors

Tracepanel reports unhandled exceptions with the stack and the local variables of your code. The stack shows your
frames first. Tracepanel groups the same error from the same place into one issue across requests, with a count.

## Tuning

The thresholds are settings: `n_plus_one_threshold`, `slow_sql_ms` and `long_transaction_ms`. See
[Configuration](configuration.md).
