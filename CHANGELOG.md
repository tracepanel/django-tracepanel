# Changelog

django-tracepanel installs `tracepanel[django]` at its own version. What
changes in each version is in
[tracepanel's changelog](https://github.com/tracepanel/tracepanel-python/blob/main/CHANGELOG.md).

## 0.1.0 (2026-10-13)

### Changed

- Installs `tracepanel[django]==0.1.0`, with `tracepanel-agent` 0.1.0:
  MongoDB queries with their N+1 and duplicates, slow datastore and gRPC calls
  with each system's hints, returned rows counted for every database driver,
  blocking calls in async views, and a trace shared as one HTML file. The
  agent starts a new store: traces kept by an earlier one aren't carried over.
- The documentation is at
  [tracepanel.dev/docs/django](https://tracepanel.dev/docs/django), next to
  the rest of Tracepanel's. This repository keeps the README.

## 0.0.1a2 (2026-10-12)

### Changed

- Installs `tracepanel[django]==0.0.1a2`: SQL from database drivers used
  without the ORM, outgoing HTTP calls, Redis commands, and Django's cache with
  its Redis commands inside, each with its issues.

## 0.0.1a1 (2026-10-12)

### Added

- The first release: `pip install django-tracepanel` installs
  `tracepanel[django]==0.0.1a1`.
