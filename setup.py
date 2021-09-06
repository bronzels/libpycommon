import setuptools
import os
import requests

from libpycommon.common.misc import md_to_rst

from _version import __version__

md_to_rst("README.md", "README.rst")

if os.path.exists('README.rst'):
    long_description = open('README.rst', encoding="utf-8").read()
else:
    long_description = 'Add a fallback short description here'

if os.path.exists("requirements.txt"):
    install_requires = open("requirements.txt").read().split("\n")
else:
    install_requires = []
print('install_requires:\n{}'.format(install_requires))

setuptools.setup(
    name="libpycommon",
    version=__version__,
    author="Alex Liu",
    license='Copyright © 2021 阿卡索外教 Inc. All Rights Reserved.',
    author_email="alexliu@acadsoc.com",
    python_requires='>=3.7.0',
    description="library with functions not coupled with acadsoc and specific service module",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://www.acadsoc.com/",
    packages=setuptools.find_packages(exclude=["tests", "test_*"]),
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=install_requires
)