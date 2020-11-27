========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-cli-config-manager/badge/?style=flat
    :target: https://readthedocs.org/projects/python-cli-config-manager
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/ryohare/python-cli-config-manager.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ryohare/python-cli-config-manager

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ryohare/python-cli-config-manager?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ryohare/python-cli-config-manager

.. |requires| image:: https://requires.io/github/ryohare/python-cli-config-manager/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ryohare/python-cli-config-manager/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/ryohare/python-cli-config-manager/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ryohare/python-cli-config-manager

.. |version| image:: https://img.shields.io/pypi/v/cli-config-manager.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/cli-config-manager

.. |wheel| image:: https://img.shields.io/pypi/wheel/cli-config-manager.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/cli-config-manager

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/cli-config-manager.svg
    :alt: Supported versions
    :target: https://pypi.org/project/cli-config-manager

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/cli-config-manager.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/cli-config-manager

.. |commits-since| image:: https://img.shields.io/github/commits-since/ryohare/python-cli-config-manager/v1.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ryohare/python-cli-config-manager/compare/v1.0.0...master



.. end-badges

A simple configuration file manager designed for CLI applications.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install cli-config-manager

You can also install the in-development version with::

    pip install https://github.com/ryohare/python-cli-config-manager/archive/master.zip


Documentation
=============


https://python-cli-config-manager.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
