# -*- coding: utf-8 -*-

# django-xls2po
# tests/settings.py


import sys
import random
import pathlib
from typing import Dict, List, Tuple, Union, Iterable  # pylint: disable=W0611


# black magic to use imports from library code
sys.path.insert(0, str(pathlib.Path(__file__).absolute().parent.parent.parent))

# secret key
SECRET_KEY = "".join(
    [
        random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)")  # nosec
        for i in range(50)
    ]
)  # type: str

# configure databases
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
}  # type: Dict[str, Dict[str, str]]

# configure templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]  # type: List[Dict[str, Union[str, List[str], bool, Dict[str, str]]]]


# i18n settings
LANGUAGE_CODE = "en"  # type: str
LANGUAGES = [("en", "English"), ("uk", "Українська")]  # type: Iterable[Tuple[str, str]]
DEFAULT_LANGUAGE = "en"  # type: str
LOCALE_PATHS = ["xls2po/locale"]  # type: List[str]

# add testing related apps
INSTALLED_APPS = [
    "django_nose",
    "po2xls",
    "xls2po",
]  # type: List[str]

# add nose test runner
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"  # type: str

# configure nose test runner
NOSE_ARGS = [
    "--rednose",
    "--force-color",
    "--with-timer",
    "--with-doctest",
    "--with-coverage",
    "--cover-inclusive",
    "--cover-erase",
    "--cover-package=xls2po",
    "--logging-clear-handlers",
]  # type: List[str]

# configure urls
ROOT_URLCONF = "xls2po.urls"  # type: str

# xls2po settings
