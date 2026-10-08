"""Lint the documentation against the code it describes.

- every setting of tracepanel's Config has a row in configuration.md, and every integration its `<name>_enabled` in
  integrations.md, except those that mean nothing to a Django project;
- every Python block in the pages compiles.
"""

import re
import sys
from dataclasses import fields
from pathlib import Path

from tracepanel.core import registry
from tracepanel.core.conf import Config

DOCS = Path(__file__).resolve().parent.parent / "docs"
# These docs are about Django: SQLAlchemy is for FastAPI, Flask and the like (tracepanel-python's README covers it).
NOT_FOR_DJANGO = frozenset({"sqlalchemy"})
BLOCK = re.compile(r"^```python\n(.*?)^```", re.MULTILINE | re.DOTALL)


def problems() -> list[str]:
    found: list[str] = []
    configuration = (DOCS / "configuration.md").read_text()
    skipped = {f"{name}_enabled" for name in NOT_FOR_DJANGO}
    found += [
        f"configuration.md: no row for `{f.name}`"
        for f in fields(Config)
        if f.name not in skipped and f"`{f.name}`" not in configuration
    ]
    integrations = (DOCS / "integrations.md").read_text()
    found += [
        f"integrations.md: `{i.name}_enabled` is missing"
        for i in registry.INTEGRATIONS
        if i.name not in NOT_FOR_DJANGO and f"`{i.name}_enabled`" not in integrations
    ]
    for page in sorted(DOCS.glob("*.md")):
        text = page.read_text()
        for block in BLOCK.finditer(text):
            line = text[: block.start()].count("\n") + 2
            try:
                compile(block.group(1), f"{page.name}:{line}", "exec")
            except SyntaxError as exc:
                found.append(f"{page.name}:{line}: {exc.msg}")
    return found


if __name__ == "__main__":
    for problem in problems():
        print(problem)
    sys.exit(1 if problems() else 0)
