# Changelog

## v0.2.0

Breaking changes:

- Shuffled & remodularized `eviltyping`. Imports directly from `eviltyping`
  should still be preserved.
- Renamed `evildatetime.TimeDelta` to `evildatetime.Duration`. The alias is still available, albeit deprecated.

Major changes:

- Added `Setter`, `Destructor` types to `eviltypes`.
- Added CHANGELOG.md file.
- Added `evilstructs` module & `evilstructs.frozendict` class.
- Added `evildatetime` module.
- Added `evilrng` module
