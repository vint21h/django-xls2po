# -*- coding: utf-8 -*-

# django-xls2po
# xls2po/converters.py


from pathlib import Path
from typing import Any, Dict, List

import xlrd
import polib

from xls2po.exceptions import ConversionError


__all__: List[str] = ["XlsToPo"]


class XlsToPo:
    """.xls to .to converter."""

    METADATA_SHEET_NAME: str = "metadata"
    STRINGS_SHEET_NAME: str = "strings"

    def __init__(self, src: str, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        """
        Setup conversion.

        :param src: path to ".po" file
        :type src: str
        :param args: additional args
        :type args: List[Any]
        :param kwargs: additional args
        :type kwargs: Dict[str, Any]
        :raises ConversionError: raised when file does not exists, IO errors or file format problems
        """  # noqa: E501
        self.src: Path = Path(src)

        if not self.src.exists():
            raise ConversionError(f"ERROR: File '{src}' does not exists.")

        try:
            self.xls: xlrd.Workbook = xlrd.open_workbook(filename=self.src)
        except (ValueError, IOError) as error:
            raise ConversionError(f"ERROR: '{src}' - file problem: {error}")

        self.po = polib.POFile()

    @staticmethod
    def output(src: Path) -> Path:
        """
        Create full path for .po file to save parsed translations strings.

        :param src: path to .xls file
        :type src: Path
        :return: path to .po file
        :rtype: Path
        """
        return src.parent.joinpath(f"{src.stem}.po")

    def metadata(self) -> None:
        """Write metadata to .po."""
        sheet: xlrd.Worksheet = self.xls.sheet_by_name(
            sheet_name=self.METADATA_SHEET_NAME
        )
        metadata: Dict[str, str] = {}

        for row_i in range(1, sheet.nrows):
            row = sheet.row_values(rowx=row_i)
            metadata[row[0]] = row[1]

        self.po.metadata = metadata

    def strings(self) -> None:
        """Write strings to .po."""
        sheet: xlrd.Worksheet = self.xls.sheet_by_name(
            sheet_name=self.STRINGS_SHEET_NAME
        )

        for row_i in range(1, sheet.nrows):
            row: List[xlrd.sheet.Cell] = sheet.row_values(rowx=row_i)
            entry: polib.POEntry = polib.POEntry(msgid=row[0], msgstr=row[1])
            self.po.append(entry)

    def convert(self, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        """
        Yes it is, thanks captain.

        :param args: additional args.
        :type args: List[Any].
        :param kwargs: additional args.
        :type kwargs: Dict[str, Any].
        """
        self.metadata()
        self.strings()

        self.po.save(fpath=str(self.output(src=self.src)))
