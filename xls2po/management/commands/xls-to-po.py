# -*- coding: utf-8 -*-

# django-xls2po
# xls2po/management/commands/xls-to-po.py

from __future__ import unicode_literals
import os
from optparse import make_option

from django.core.management.base import BaseCommand
from django.conf import settings

from rosetta.poutil import find_pos

from xls2po import XlsToPo


class Command(BaseCommand):
    """
    Convert django-xls2po generated .xls files to .po.
    """

    _all = "all"

    option_list = BaseCommand.option_list + (
        make_option("--language", "-l", dest="language", help="Language", default=_all),
        make_option("--quiet", "-q", dest="quiet", help="Be quiet", default=False, action="store_true"),
    )

    def handle(self, *args, **kwargs):

        if kwargs["language"] == self._all:
            for language in dict(settings.LANGUAGES).keys():
                self._parse(language)
        else:
            self._parse(kwargs["language"])

    def _parse(self, language, *args, **kwargs):

        for f in find_pos(language):
            XlsToPo(self._get_input_path(f), **kwargs).parse()

    def _get_input_path(self, f):
        """
        Create full path for .xls file.
        """

        path, f = os.path.split(f)
        f, ext = os.path.splitext(f)

        return os.path.join(path, "%s.xls" % f)
