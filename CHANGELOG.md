# Changelog

## v0.2.0

Breaking changes:

- Shuffled & remodularized `eviltyping`. Imports directly from `eviltyping`
  should still be preserved.

Major changes:

- Added `Setter`, `Destructor` types to `eviltypes`.
- Added CHANGELOG.md file.
- Added `evilstructs` module & `evilstructs.frozendict` class.
- Added `evildatetime` module.
- Added `evilrng` module.

## v0.3.0, 2026-09-28

Breaking changes:

- Renamed `evildatetime.TimeDelta` to `evildatetime.Duration`. The `TimeDelta`
  alias is deprecated & scheduled for future removal.

## v0.3.1-alpha1, 2026-09-28

Internal changes only. See `v0.3.0` for changes from `v0.2.0`.

## master

- `evildatetime`:
  - Add methods to class `Duration`: `from_seconds`, `from_milliseconds`
  - Add `Seconds` class.
