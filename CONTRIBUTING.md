# Contributing

Contributions are welcome. For bugs or feature ideas, open an issue; for code
changes, open a pull request against `main`.

## Development setup

See the [README](README.md#development) for build dependencies and local
development installation. In brief:

```sh
git clone https://github.com/yashjawale/cockpit-whale.git
cd cockpit-whale
make
```

## Checks and tests

Before submitting a pull request, run the static checks and browser integration
tests:

```sh
make codecheck
TEST_BROWSER=firefox make check
```

The integration tests use a test VM and may require additional setup; see
[AGENTS.md](AGENTS.md) for project-specific commands and test guidance.

## Translations

Translatable strings are extracted into the gettext template. After changing
strings, regenerate it with:

```sh
make po/cockpit-whale.pot
```

Translation contributions through Weblate are planned; see the note in the
README for the current status.

## Pull requests

- Keep changes focused and follow the existing code and documentation style.
- Include tests or documentation updates when they help explain or verify a
  change.
- Describe the behavior changed and the checks you ran in the pull request.
