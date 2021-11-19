# -*- coding: utf-8 -*-

# django-xls2po
# xls2po/exceptions.py


from typing import List


__all__: List[str] = [
    "ConversionError",
]


class ConversionError(Exception):
    """Problem while converting exception."""

    ...
