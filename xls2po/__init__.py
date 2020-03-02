# -*- coding: utf-8 -*-

# django-xls2po
# xls2po/__init__.py


from typing import List  # pylint: disable=W0611


__all__ = ["default_app_config"]  # type: List[str]


default_app_config = "xls2po.apps.DjangoXlsToPoConfig"
