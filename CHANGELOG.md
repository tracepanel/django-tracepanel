# Changelog

django-tracepanel installs `tracepanel[django]`, any patch of its own minor
version. What changes in each version is in
[tracepanel's changelog](https://github.com/tracepanel/tracepanel-python/blob/main/CHANGELOG.md).

## 0.4.0 (2026-10-21)

### Changed

- Installs `tracepanel[django]` 0.4, with `tracepanel-agent` 0.4.0: the
  panel's Request and Profile tabs, a form's POST that redirected listed
  before the page it led to, the place in the app that made a library's
  query, Celery, RQ, Dramatiq and Django Tasks in flight on the console's
  Tasks page, and logs by level, with their exceptions as frames.

## 0.3.2 (2026-10-17)

### Changed

- Installs any `tracepanel[django]` 0.3 from 0.3.2 on, rather than exactly
  its own version. tracepanel's patches now reach a Django project without a
  django-tracepanel release. 0.3.2 fixes a SQLAlchemy `AUTOCOMMIT`
  connection shown as a transaction.

## 0.3.1 (2026-10-16)

### Changed

- Installs `tracepanel[django]==0.3.1`, with `tracepanel-agent` 0.3.1: the
  console's script is a fifth smaller, and the source around an error's
  frame is highlighted in more languages.

## 0.3.0 (2026-10-15)

### Changed

- Installs `tracepanel[django]==0.3.0`, with `tracepanel-agent` 0.3.0: the
  console finds logs by the spans they were written in, runs EXPLAIN for a
  query, follows calls to another project's app to its trace, and limits
  how much one trace keeps.

## 0.2.0 (2026-10-14)

### Changed

- Installs `tracepanel[django]==0.2.0`, with `tracepanel-agent` 0.2.0: the
  console's Pages section lists what users do in the browser, which an SPA's
  dev server sends through the app's console, and apps in many more
  languages and frameworks are labelled. The console takes such writes from
  this machine only, or from `INTERNAL_IPS`.

## 0.1.1 (2026-10-13)

### Changed

- Installs `tracepanel[django]==0.1.1`, with `tracepanel-agent` 0.1.1: the
  console's Services map fits the width it has, and the Share dialog and the
  Issues page describe what they do now.

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
