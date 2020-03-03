# -*- coding: utf-8 -*-

# django-xls2po
# tests/test_converters.py


from importlib import import_module
import os
import pathlib
from typing import List  # pylint: disable=W0611

from django.test import TestCase

# po-to-xls management command imported on the fly
# because we can't import something from the module that contains "-"
from xls2po.converters import XlsToPo
from xls2po.exceptions import ConversionError


PoToXlsCommand = import_module("po2xls.management.commands.po-to-xls").Command  # type: ignore  # noqa: E501


__all__ = ["XlsToPoTest"]  # type: List[str]


class XlsToPoTest(TestCase):
    """
    .xls to .po converter tests.
    """

    @classmethod
    def setUp(cls):
        """
        Set up.
        """

        PoToXlsCommand().handle()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down.
        """

        os.remove("xls2po/locale/en/LC_MESSAGES/django.xls")
        os.remove("xls2po/locale/uk/LC_MESSAGES/django.xls")

        super().tearDownClass()

    def test___init___raises_conversion_error_exception(self):
        """
        __init__ method must raise "ConversionError".
        """

        with self.assertRaises(expected_exception=ConversionError):
            XlsToPo(src="locale/uk/LC_MESSAGES/django.xls")

    def test_output(self):
        """
        output method must return original file path but with extension changed to "po".
        """

        converter = XlsToPo(src="xls2po/locale/uk/LC_MESSAGES/django.xls")

        result = converter.output(
            src=pathlib.Path("xls2po/locale/uk/LC_MESSAGES/django.xls")
        )
        expected = pathlib.Path("xls2po/locale/uk/LC_MESSAGES/django.po")

        self.assertEqual(first=result, second=expected)

    def test_convert__file_exists(self):
        """
        convert method must write converted data to .po file.
        """

        XlsToPo(src="xls2po/locale/uk/LC_MESSAGES/django.xls").convert()

        self.assertTrue(
            expr=pathlib.Path("xls2po/locale/uk/LC_MESSAGES/django.po").exists()
        )

    # TODO: add check file content test.
