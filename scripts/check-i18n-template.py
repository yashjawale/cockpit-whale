"""Smoke-check that all supported source formats are in the gettext template."""

import pathlib
import re
import sys


def main():
    pot = pathlib.Path(sys.argv[1]).read_text()
    assert re.search(r'#: .*src/index\.html:\d+.*\nmsgid "Cockpit Whale"', pot)
    assert re.search(r'#: .*src/manifest\.json:\d+.*\nmsgid "Docker containers"', pot)
    assert re.search(
        r'#: .*in\.yashjawale\.cockpit_whale\.metainfo\.xml:\d+.*\n'
        r'msgid "Manage Docker containers and images"', pot)
    assert '#-#-#-#-#' not in pot
    assert pot.startswith('# Cockpit Whale translation template.\n')
    assert 'Report-Msgid-Bugs-To: https://github.com/yashjawale/cockpit-whale/issues' in pot


if __name__ == "__main__":
    main()
