#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""Script to update the xsdata package name from the schema version."""
import re
from pathlib import Path
import sys

import packaging.version
from packaging.version import Version, parse
from xsdata.models.config import GeneratorConfig

PACKAGE = 'ocx'
CONFIG_FILE = './ocx/.xsdata.xml'

# The new package version


def insert_package_name():
    """Update the package name in .xsdata.xml."""

    new_version = sys.argv[1]
    # parse new_version
    try:
        v= parse(new_version)
        if v.is_prerelease:
            pr1, pr2 = v.pre
            package_dir = f'{PACKAGE}_{v.major}{v.minor}{v.micro}{pr1}{pr2}'
        else:
            package_dir = f'{PACKAGE}_{v.major}{v.minor}{v.micro}'
        file_path = Path(CONFIG_FILE)
        if file_path.exists():
            config = GeneratorConfig.read(file_path)
            print(f'Updating the configuration file {CONFIG_FILE} ')
        else:
            print(f'Initializing configuration file {CONFIG_FILE}')
            config = GeneratorConfig.create()
            # OCX databindings defaults
            config.output.docstring_style = 'Google'

        config.output.package = package_dir
        print(f'New package name is {package_dir} from new version {new_version}')
        with file_path.open("w") as fp:
            config.write(fp, config)
    except packaging.version.InvalidVersion as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    insert_package_name()
