# -*- coding: utf-8 -*-

# django-xls2po
# xls2po/management/commands/xls-to-po.py

from __future__ import unicode_literals
import os
from optparse import make_option

from django.core.management.base import BaseCommand
from django.conf import settings

from rosetta.poutil import find_pos

from xls2po.utils import XlsToPo


class Command(BaseCommand):
    """
    Convert django-xls2po generated .xls files to .po.
    """

    all = "all"

    option_list = BaseCommand.option_list + (
        make_option("--language", "-l", dest="language", help="Language", default=all),
        make_option("--quiet", "-q", dest="quiet", help="Be quiet", default=False, action="store_true"),
    )

    def handle(self, *args, **kwargs):

        if kwargs["language"] == self.all:
            for language in dict(settings.LANGUAGES).keys():
                self.convert(language)
        else:
            self.convert(kwargs["language"])

    def convert(self, language, *args, **kwargs):
        """
        Run converter.
        Args:
            language: (unicode) language code.
        """

        for f in find_pos(language):
            XlsToPo(self.input(f), **kwargs).convert()

    def input(self, f):
        """
        Create full path for .xls file.
        Args:
            f: (unicode) ".po" file path.
        Returns:
            unicode: path to ".po" file.
        """

        path, f = os.path.split(f)
        f, ext = os.path.splitext(f)

        return os.path.join(path, "{f}.xls".format(**{"f": f, }))
