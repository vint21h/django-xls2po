# -*- coding: utf-8 -*-

# django-xls2po
# xls2po/management/commands/xls-to-po.py


import sys
import logging
from pathlib import Path
from typing import Any, Dict, List  # pylint: disable=W0611

from django.conf import settings
from rosetta.poutil import find_pos
from django.utils.translation import gettext_lazy as _
from django.core.management.base import BaseCommand, CommandParser

from xls2po.converters import XlsToPo
from xls2po.exceptions import ConversionError


__all__ = ["Command"]  # type: List[str]


class Command(BaseCommand):
    """
    Convert django-xls2po generated .xls files to .po.
    """

    ALL = "all"
    help = str(_("Convert django-xls2po generated .xls files to .po"))
    logger = logging.getLogger(name=__name__)

    def add_arguments(self, parser: CommandParser) -> None:
        """
        Add command arguments.

        :param parser: command arguments parser instance
        :type parser: CommandParser
        """

        parser.add_argument(
            "--locale",
            "-l",
            dest="locale",
            help=_("Locale to convert"),
            default=self.ALL,
            required=True,
            metavar="LOCALE",
            type=str,
        )
        parser.add_argument(
            "--quiet",
            "-q",
            dest="quiet",
            help=_("Be quiet"),
            default=False,
            action="store_true",
        )

    def handle(self, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        """
        Run command.

        :param args: additional args
        :type args: List[Any]
        :param kwargs: additional args
        :type kwargs: Dict[str, Any]
        """

        locale = kwargs.get("locale", self.ALL)

        if all([locale == self.ALL, settings.LANGUAGES]):
            for language in dict(settings.LANGUAGES):
                self.convert(locale=language, **kwargs)
        elif all([settings.LANGUAGES, locale in dict(settings.LANGUAGES)]):
            self.convert(locale=locale, **kwargs)  # type: ignore

    def convert(self, locale: str, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        """
        Run converter.

        :param locale: locale to process
        :type locale: str
        :param args: additional args
        :type args: List[Any]
        :param kwargs: additional args
        :type kwargs: Dict[str, Any]
        """

        quiet = kwargs.get("quiet", False)

        for po in find_pos(lang=locale):
            try:
                XlsToPo(src=str(self.input(src=Path(po))), **kwargs).convert()
            except ConversionError as error:
                if not quiet:
                    self.stderr.write(str(error))
                self.logger.error(error)

                sys.exit(-1)

    @staticmethod
    def input(src: Path) -> Path:
        """
        Create full path for .xls file.

        :param src: path to .po file
        :type src: Path
        :return: path to .xls file
        :rtype: Path
        """

        return src.parent.joinpath(f"{src.stem}.xls")
