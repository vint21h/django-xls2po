.. django-xls2po
.. README.rst

A django-xls2po documentation
=============================

    *django-xls2po is a django management command to convert django-po2xls generated .xls files to .po files*

.. contents::

Warning
-------
django-xls2po does not support plural.

Installation
------------
* Obtain your copy of source code from git repository: ``git clone https://github.com/vint21h/django-xls2po.git``. Or download latest release from https://github.com/vint21h/django-xls2po/tags.
* Run ``python ./setup.py install`` from repository source tree or unpacked archive. Or use pip: ``pip install django-xls2po``.

Configuration
-------------
Add ``"xls2po"`` to ``settings.INSTALLED_APPS``.

    INSTALLED_APPS = (
        ...,

        "xls2po",

        ...,

    )

Usage
-----
Just run ``xls-to-po`` django management command after ``po-to-xls``.

Licensing
---------
django-xls2po is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://github.com/vint21h/django-xls2po

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For other authors list see AUTHORS file.
