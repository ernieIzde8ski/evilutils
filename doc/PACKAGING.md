# Packaging

Packaging & distribution onto PyPI is managed through GitHub Actions. The
package may also be built locally using `uv build`.

When preparing for a new release, please create the appropriate commit in the
following format:

```sh
git add CHANGELOG.md pyproject.toml
git commit -m 'Bump version number to v3.1.4-alpha2'
git tag -a v3.1.4-alpha2 -m 'Release v3.1.4-alpha2'
```
