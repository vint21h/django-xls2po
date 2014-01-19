# -*- coding: utf-8 -*-

# xls2po
# __init__.py

import sys
import os
import logging

import polib
import xlrd

__all__ = ['models', 'views', 'management', 'XlsToPo', ]


class XlsToPo(object):

    logger = logging.getLogger(__name__)

    def __init__(self, src, *args, **kwargs):

        self.quiet = kwargs.pop('quiet', False)

        if os.path.exists(src):
            self.src = src
        else:
            if not self.quiet:
                sys.stderr.write(u"ERROR: File '%s' does not exists." % src)
            self.logger.error(u"ERROR: File '%s' does not exists." % src)
            sys.exit(-1)

        self.xls = xlrd.open_workbook(self.src)
        self.po = polib.POFile()

    def _get_output_path(self):
        """
        Create full path for .po file.
        """

        path, src = os.path.split(self.src)
        src, ext = os.path.splitext(src)

        return os.path.join(path, u"%s.po" % src)

    def _write_metadata(self):
        """
        Write metadata to .po.
        """

        sheet = self.xls.sheet_by_name(u'metadata')
        n = sheet.nrows
        metadata = {}

        for row_i in range(1, n):
            row = sheet.row_values(row_i)
            metadata[row[0]] = row[1]

        self.po.metadata = metadata

    def _write_strings(self):
        """
        Write strings to .po.
        """

        sheet = self.xls.sheet_by_name(u'strings')
        n = sheet.nrows

        for row_i in range(1, n):
            row = sheet.row_values(row_i)
            entry = polib.POEntry(
                msgid=row[0],
                msgstr=row[1],
            )
            self.po.append(entry)

    def parse(self, *args, **kwargs):
        """
        Yes it is, thanks captain.
        """

        self._write_metadata()
        self._write_strings()

        self.po.save(self._get_output_path())
