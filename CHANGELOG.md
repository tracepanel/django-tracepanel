# Changelog

django-tracepanel installs `tracepanel[django]` at its own version. What
changes in each version is in
[tracepanel's changelog](https://github.com/tracepanel/tracepanel-python/blob/main/CHANGELOG.md).

## 0.0.1a2 (2026-10-12)

### Changed

- Installs `tracepanel[django]==0.0.1a2`: SQL from database drivers used
  without the ORM, outgoing HTTP calls, Redis commands, and Django's cache with
  its Redis commands inside, each with its issues.

## 0.0.1a1 (2026-10-12)

### Added

- The first release: `pip install django-tracepanel` installs
  `tracepanel[django]==0.0.1a1`.
