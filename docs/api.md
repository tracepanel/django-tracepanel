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

Tracepanel attaches the queries, logs and errors inside a span to that span. Outside a trace, and when Tracepanel is
off, all these functions do nothing, so you can leave them in your code.

```python
@tracepanel.traced
def price(cart): ...


tracepanel.set_attr("order.id", order.pk)  # on the current span
tracepanel.set_attr("tenant", tenant.slug, on_trace=True)  # on the trace: searchable
tracepanel.event("cache warmed")  # a point on the timeline
```

`tracepanel.trace()` creates a trace in code that has none, such as a script, a scheduled job or a consumer of your
own.

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
