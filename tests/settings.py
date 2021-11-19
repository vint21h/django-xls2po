# -*- coding: utf-8 -*-

# django-xls2po
# tests/settings.py


import sys
import pathlib
from random import SystemRandom
from typing import Dict, List, Tuple, Union, Iterable


# black magic to use imports from library code
path = pathlib.Path(__file__).absolute()
project = path.parent.parent.parent
sys.path.insert(0, str(project))

# secret key
SECRET_KEY: str = "".join(
    [
        SystemRandom().choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)")
        for i in range(50)
    ]
)

# configure databases
DATABASES: Dict[str, Dict[str, str]] = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
}

# configure templates
TEMPLATES: List[Dict[str, Union[str, List[str], bool, Dict[str, str]]]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]


# i18n settings
LANGUAGE_CODE: str = "en"
LANGUAGES: Iterable[Tuple[str, str]] = [("en", "English"), ("uk", "Українська")]
DEFAULT_LANGUAGE: str = "en"
LOCALE_PATHS: List[str] = ["xls2po/locale"]

# add testing related apps
INSTALLED_APPS: List[str] = [
    "po2xls",
    "xls2po",
]

# configure urls
ROOT_URLCONF: str = "xls2po.urls"
