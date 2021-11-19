.. django-xls2po
.. README.rst

A django-xls2po documentation
=============================

|GitHub|_ |Coveralls|_ |pypi-license|_ |pypi-version|_ |pypi-python-version|_ |pypi-django-version|_ |pypi-format|_ |pypi-wheel|_ |pypi-status|_

    *django-xls2po is a Django management command to convert django-po2xls generated .xls files to .po files*

.. contents::

Warning
-------
django-xls2po does not support plural.

Installation
------------
* Obtain your copy of source code from the git repository: ``$ git clone https://github.com/vint21h/django-xls2po.git``. Or download the latest release from https://github.com/vint21h/django-xls2po/tags/.
* Run ``$ python ./setup.py install`` from the repository source tree or unpacked archive. Or use pip: ``$ pip install django-xls2po``.

Configuration
-------------
Add ``"xls2po"`` to ``settings.INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS += [
        "xls2po",
    ]


Usage
-----
Just run: ``$ python ./manage.py xls-to-po`` Django management command from project folder and if you have ``django-po2xls`` generated .xls files near of your .po files they will be overwritten by .xls files content.

Contributing
------------
1. `Fork it <https://github.com/vint21h/django-xls2po/>`_
2. Install `GNU Make <https://www.gnu.org/software/make/>`_
3. Install and configure `pyenv <https://github.com/pyenv/pyenv/>`_ and `pyenv-virtualenv plugin <https://github.com/pyenv/pyenv-virtualenv/>`_
4. Install and configure `direnv <https://github.com/direnv/direnv/>`_
5. Create environment config from example

.. code-block:: bash

    cp .env.example .env

6. Install development dependencies:

.. code-block:: bash

    make install

7. Create your fix/feature branch:

.. code-block:: bash

    git checkout -b my-new-fix-or-feature

8. Check code style and moreover:

.. code-block:: bash

    make check

9. Run tests:

.. code-block:: bash

    make test

10. Push to the branch:

.. code-block:: bash

    git push origin my-new-fix-or-feature

11. `Create a new Pull Request <https://github.com/vint21h/django-xls2po/compare/>`_

Licensing
---------
django-xls2po is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://github.com/vint21h/django-xls2po/

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For other authors list see AUTHORS file.


.. |GitHub| image:: https://github.com/vint21h/django-xls2po/workflows/build/badge.svg
    :alt: GitHub
.. |Coveralls| image:: https://coveralls.io/repos/github/vint21h/django-xls2po/badge.svg?branch=master
    :alt: Coveralls
.. |pypi-license| image:: https://img.shields.io/pypi/l/django-xls2po
    :alt: License
.. |pypi-version| image:: https://img.shields.io/pypi/v/django-xls2po
    :alt: Version
.. |pypi-django-version| image:: https://img.shields.io/pypi/djversions/django-xls2po
    :alt: Supported Django version
.. |pypi-python-version| image:: https://img.shields.io/pypi/pyversions/django-xls2po
    :alt: Supported Python version
.. |pypi-format| image:: https://img.shields.io/pypi/format/django-xls2po
    :alt: Package format
.. |pypi-wheel| image:: https://img.shields.io/pypi/wheel/django-xls2po
    :alt: Python wheel support
.. |pypi-status| image:: https://img.shields.io/pypi/status/django-xls2po
    :alt: Package status
.. _GitHub: https://github.com/vint21h/django-xls2po/actions/
.. _Coveralls: https://coveralls.io/github/vint21h/django-xls2po?branch=master
.. _pypi-license: https://pypi.org/project/django-xls2po/
.. _pypi-version: https://pypi.org/project/django-xls2po/
.. _pypi-django-version: https://pypi.org/project/django-xls2po/
.. _pypi-python-version: https://pypi.org/project/django-xls2po/
.. _pypi-format: https://pypi.org/project/django-xls2po/
.. _pypi-wheel: https://pypi.org/project/django-xls2po/
.. _pypi-status: https://pypi.org/project/django-xls2po/
