# -*- coding: utf-8 -*-

# django-xls2po
# xls2po/apps.py


from typing import List  # pylint: disable=W0611

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__ = ["DjangoXlsToPoConfig"]  # type: List[str]


class DjangoXlsToPoConfig(AppConfig):
    """
    Application config.
    """

    name = "xls2po"  # type: str
    verbose_name = _(
        "Convert django-po2xls generated .xls files to .po files"
    )  # type: str
