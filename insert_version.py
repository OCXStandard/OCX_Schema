#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""Script to update __version__ number of the xsdata generated databinding."""

from pathlib import Path
import sys

PACKAGE = './ocx'

def insert_version():
    """Insert the version string in __init__.py."""

    new_version = sys.argv[1]
    # parse new_version
    major, minor, patch = new_version.split('.')
    if '-' in patch:
        patch, extra = patch.split('-')
    else:
        extra = ""

    if extra == "":
        package_dir = f'{PACKAGE}_{major}_{minor}_{patch}'
        new_version = f'{major}.{minor}.{patch}'
    else:
        package_dir = f'{PACKAGE}_{major}_{minor}_{patch}_{extra}'
        new_version = f'{major}.{minor}.{patch}-{extra}'

    file = Path(package_dir) / '__init__.py'
    if file.exists():
        with open(file, 'r') as f:
            init_py = f.readlines()
    else:
        print('Data-bindings has not been generated.')
        sys.exit(1)
    init_py.insert(0,f'__version__ = "{new_version}"\n')
    init_py.insert(0,f'# The data-bindings are generated from the schema version={new_version}.\n')

    with open(file, 'w') as f:
        f.writelines(init_py)


if __name__ == "__main__":
    insert_version()
