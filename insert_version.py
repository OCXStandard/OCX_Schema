#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""Script to update __version__ number of the xsdata generated databinding."""

from pathlib import Path

import packaging.version
from packaging.version import Version, parse
import sys

PACKAGE_DIR = './ocx'

def insert_version():
    """Insert the version string in __init__.py."""

    new_version = sys.argv[1]
    # parse new_version
    try:
        v= parse(new_version)
        if v.is_prerelease:
            pr1, pr2 = v.pre
            package = f'ocx_{v.major}{v.minor}{v.micro}{pr1}{pr2}'
        else:
            package = f'ocx_{v.major}{v.minor}{v.micro}'
        file = Path(PACKAGE_DIR) / package / '__init__.py'
        if file.exists():
            with open(file, 'r') as f:
                init_py = f.readlines()
        else:
            print('Data-bindings has not been generated.')
            sys.exit(1)
        init_py.insert(0,f'__version__ = "{new_version}"\n')
        init_py.insert(0,f'# The data-bindings are generated from the schema version={new_version}.\n')
        # Update the databinding package
        with open(file, 'w') as f:
            f.writelines(init_py)
    except packaging.version.InvalidVersion as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    insert_version()
