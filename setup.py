"""
setup
"""
import os
from typing import List

import semver
import setuptools


def get_version() -> str:
    """
    read version from VERSION file
    """
    version = '0.0.0'
    version_file = os.path.join(
        os.path.dirname(__file__),
        'VERSION'
    )

    with open(version_file, 'r', encoding='utf-8') as version_fh:
        # Get X.Y.Z
        version = version_fh.read().strip()

    return version


def get_long_description() -> str:
    """get long_description"""
    with open('README.md', 'r', encoding='utf-8') as readme_fh:
        return readme_fh.read()


def get_install_requires() -> List[str]:
    """get install_requires"""
    with open('requirements.txt', 'r', encoding='utf-8') as requirements_fh:
        return requirements_fh.read().splitlines()


setuptools.setup(
    name='wechaty-plugin-foo',
    version=get_version(),
    author='<author>',
    author_email='<author_email>',
    description='Python Wechaty Plugin <foo>',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    license='Apache-2.0',
    url='https://github.com/<author>/python-wechaty-plugin-<foo>',
    install_requires=get_install_requires(),
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
