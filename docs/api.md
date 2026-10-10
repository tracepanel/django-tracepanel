# Your own spans

The call tree shows what Django and the libraries do. To see the steps of your own code, wrap them:

```python
import tracepanel


def checkout(cart):
    with tracepanel.span("price the cart", items=len(cart)):
        total = price(cart)
    with tracepanel.span("charge"):
        charge(cart.owner, total)
```

Queries, logs and errors inside a span attach to it. Outside a trace, and when Tracepanel is off, all of these do
nothing, so they can stay in the code.

```python
@tracepanel.traced
def price(cart): ...


tracepanel.set_attr("order.id", order.pk)  # on the current span
tracepanel.set_attr("tenant", tenant.slug, on_trace=True)  # on the trace: searchable
tracepanel.event("cache warmed")  # a point on the timeline
```

`tracepanel.trace()` makes a trace where there is none: a script, a scheduled job, a consumer of your own.

```python
with tracepanel.trace("nightly import", kind="command"):
    run_import()
```

## Reference

::: tracepanel.span

::: tracepanel.traced

::: tracepanel.trace

::: tracepanel.set_attr

::: tracepanel.event
