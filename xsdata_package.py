#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""Script to update the xsdata package name from the schema version."""
import re
from pathlib import Path
import sys
from xsdata.models.config import GeneratorConfig

PACKAGE = 'ocx'
CONFIG_FILE = '.xsdata.xml'

# The new package version


def insert_package_name():
    """Update the package name in .xsdata.xml."""

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
        package_dir = f'{PACKAGE}_{major}_{minor}_{patch}_{extra.replace(".","_")}'
        new_version = f'{major}.{minor}.{patch}-{extra}'
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

if __name__ == "__main__":
    insert_package_name()
