#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-xls2po
# setup.py

from setuptools import (
    setup,
    find_packages,
)

# metadata
VERSION = (0, 2, 0)
__version__ = ".".join(map(str, VERSION))
setup(
    name="django-xls2po",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "Django",
        "django-rosetta==0.7.12",
        "polib==1.0.8",
        "xlrd==1.0.0",
    ],
    author="Alexei Andrushievich",
    author_email="vint21h@vint21h.pp.ua",
    description="django-xls2po is a django management command to convert django-po2xls generated .xls files to .po files",
    license="GPLv3 or later",
    url="https://github.com/vint21h/django-xls2po/",
    download_url="https://github.com/vint21h/django-xls2po/archive/{version}.tar.gz".format(version=__version__),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Environment :: Console",
        "Environment :: Plugins",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "Framework :: Django :: 1.5",
        "Framework :: Django :: 1.6",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
    ]
)
