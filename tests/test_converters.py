# -*- coding: utf-8 -*-

# django-xls2po
# tests/test_converters.py


import os
import pathlib
from typing import List

import git
import xlrd
import polib
from django.test import TestCase
from po2xls.converters import PoToXls

from xls2po.converters import XlsToPo
from xls2po.exceptions import ConversionError


__all__: List[str] = ["XlsToPoTest"]


class XlsToPoTest(TestCase):
    """.xls to .po converter tests."""

    @classmethod
    def setUp(cls) -> None:
        """Set up."""
        PoToXls(src="xls2po/locale/uk/LC_MESSAGES/django.po").convert()

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down."""
        os.remove("xls2po/locale/uk/LC_MESSAGES/django.xls")

        # revert converted .po files state to avoid commit them in local development
        repo: git.Repo = git.Repo(".")
        repo.index.checkout(["xls2po/locale/uk/LC_MESSAGES/django.po"], force=True)

        super().tearDownClass()

    def test___init___raises_conversion_error_exception(self) -> None:
        """__init__ method must raise "ConversionError"."""
        with self.assertRaises(expected_exception=ConversionError):
            XlsToPo(src="locale/uk/LC_MESSAGES/django.xls")

    def test_output(self) -> None:
        """output method must return original file path but with extension changed to "po"."""  # noqa: D403,E501
        converter = XlsToPo(src="xls2po/locale/uk/LC_MESSAGES/django.xls")

        result = converter.output(
            src=pathlib.Path("xls2po/locale/uk/LC_MESSAGES/django.xls")
        )
        expected = pathlib.Path("xls2po/locale/uk/LC_MESSAGES/django.po")

        self.assertEqual(first=result, second=expected)

    def test_convert__file_exists(self) -> None:
        """convert method must write converted data to .po file."""  # noqa: D403
        XlsToPo(src="xls2po/locale/uk/LC_MESSAGES/django.xls").convert()

        self.assertTrue(
            expr=pathlib.Path("xls2po/locale/uk/LC_MESSAGES/django.po").exists()
        )

    def test_convert(self) -> None:
        """convert method must write converted data to .po file."""  # noqa: D403
        XlsToPo(src="xls2po/locale/uk/LC_MESSAGES/django.xls").convert()

        po: polib.POFile = polib.pofile(
            pofile="xls2po/locale/uk/LC_MESSAGES/django.po"
        )
        po_metadata: List[List[str]] = [["key", "value"]] + [  # noqa: ECE001
            [data, po.metadata[data]] for data in po.metadata
        ]
        po_strings: List[List[str]] = [["msgid", "msgstr"]] + [
            [entry.msgid, entry.msgstr] for entry in po
        ]
        xls: xlrd.Workbook = xlrd.open_workbook(
            filename="xls2po/locale/uk/LC_MESSAGES/django.xls"
        )
        xls_metadata: List[List[str]] = [
            xls.sheet_by_name(sheet_name=PoToXls.METADATA_SHEET_NAME).row_values(
                rowx=row_i
            )
            for row_i in range(
                0, xls.sheet_by_name(sheet_name=PoToXls.METADATA_SHEET_NAME).nrows
            )
        ]
        xls_strings: List[List[str]] = [
            xls.sheet_by_name(sheet_name=PoToXls.STRINGS_SHEET_NAME).row_values(
                rowx=row_i
            )
            for row_i in range(
                0, xls.sheet_by_name(sheet_name=PoToXls.STRINGS_SHEET_NAME).nrows
            )
        ]

        self.assertListEqual(list1=po_metadata, list2=xls_metadata)
        self.assertListEqual(list1=po_strings, list2=xls_strings)
