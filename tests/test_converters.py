# -*- coding: utf-8 -*-

# django-xls2po
# tests/test_converters.py


from importlib import import_module
import os
import pathlib
from typing import List  # pylint: disable=W0611

from django.test import TestCase
import git
from po2xls.converters import PoToXls
import polib
import xlrd

from xls2po.converters import XlsToPo
from xls2po.exceptions import ConversionError


# po-to-xls management command imported on the fly
# because we can't import something from the module that contains "-"
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

        # reset git repo state to avoid commit changed .po files
        repo = git.Repo(".")
        repo.git.reset("--hard")

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

    def test_convert(self):
        """
        convert method must write converted data to .xls file.
        """

        XlsToPo(src="xls2po/locale/uk/LC_MESSAGES/django.xls").convert()

        po = polib.pofile(
            pofile="xls2po/locale/uk/LC_MESSAGES/django.po"
        )  # type: polib.POFile
        po_metadata = [["key", "value"]] + [
            [data, po.metadata[data]] for data in po.metadata
        ]  # type: List[List[str]]
        po_strings = [["msgid", "msgstr"]] + [
            [entry.msgid, entry.msgstr] for entry in po
        ]  # type: List[List[str]]
        xls = xlrd.open_workbook(
            filename="xls2po/locale/uk/LC_MESSAGES/django.xls"
        )  # type: xlrd.Workbook
        xls_metadata = [
            xls.sheet_by_name(sheet_name=PoToXls.METADATA_SHEET_NAME).row_values(
                rowx=row_i
            )
            for row_i in range(
                0, xls.sheet_by_name(sheet_name=PoToXls.METADATA_SHEET_NAME).nrows
            )
        ]  # type: List[List[str]]
        xls_strings = [
            xls.sheet_by_name(sheet_name=PoToXls.STRINGS_SHEET_NAME).row_values(
                rowx=row_i
            )
            for row_i in range(
                0, xls.sheet_by_name(sheet_name=PoToXls.STRINGS_SHEET_NAME).nrows
            )
        ]  # type: List[List[str]]

        self.assertListEqual(list1=po_metadata, list2=xls_metadata)
        self.assertListEqual(list1=po_strings, list2=xls_strings)
