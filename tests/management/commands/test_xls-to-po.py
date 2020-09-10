# -*- coding: utf-8 -*-

# django-xls2po
# tests/management/commands/test_xls-to-po.py


import os
import pathlib
from importlib import import_module
from typing import List  # pylint: disable=W0611

import git
from django.test import TestCase


# po-to-xls and xls-to-po management commands imported on the fly
# because we can't import something from the module that contains "-"
PoToXlsCommand = import_module("po2xls.management.commands.po-to-xls").Command  # type: ignore  # noqa: E501
XlsToPoCommand = import_module("xls2po.management.commands.xls-to-po").Command  # type: ignore  # noqa: E501


__all__ = ["CommandTest"]  # type: List[str]


class CommandTest(TestCase):
    """
    xls-to-po management command tests.
    """

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Tear down.
        """

        os.remove("xls2po/locale/en/LC_MESSAGES/django.xls")
        os.remove("xls2po/locale/uk/LC_MESSAGES/django.xls")

        # revert converted .po files state to avoid commit them in local development
        repo = git.Repo(".")  # type: git.Repo
        repo.index.checkout(["xls2po/locale/en/LC_MESSAGES/django.po"], force=True)
        repo.index.checkout(["xls2po/locale/uk/LC_MESSAGES/django.po"], force=True)

        super().tearDownClass()

    def test_convert(self) -> None:
        """
        convert method must write converted data to .po files for chosen locale.
        """

        PoToXlsCommand().convert(locale="uk")
        XlsToPoCommand().convert(locale="uk")

        self.assertTrue(
            expr=pathlib.Path("xls2po/locale/uk/LC_MESSAGES/django.po").exists()
        )

    def test_convert__all(self) -> None:
        """
        convert method must write converted data to .po files for all locales.
        """

        PoToXlsCommand().handle()
        XlsToPoCommand().handle()

        self.assertTrue(
            expr=pathlib.Path("xls2po/locale/en/LC_MESSAGES/django.po").exists()
        )
        self.assertTrue(
            expr=pathlib.Path("xls2po/locale/uk/LC_MESSAGES/django.po").exists()
        )

    def test_input(self) -> None:
        """
        input method must return original file path but with extension changed to "xls".
        """

        result = XlsToPoCommand().input(
            src=pathlib.Path("xls2po/locale/uk/LC_MESSAGES/django.po")
        )
        expected = pathlib.Path("xls2po/locale/uk/LC_MESSAGES/django.xls")

        self.assertEqual(first=result, second=expected)
