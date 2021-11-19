# -*- coding: utf-8 -*-

# django-xls2po
# xls2po/apps.py


from typing import List

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__: List[str] = ["DjangoXlsToPoConfig"]


class DjangoXlsToPoConfig(AppConfig):
    """Application config."""

    name: str = "xls2po"
    verbose_name: str = _("Convert django-po2xls generated .xls files to .po files")
