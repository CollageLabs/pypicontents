.. image:: https://gitcdn.xyz/repo/CollageLabs/pypicontents/master/docs/_static/title.svg

-----

.. image:: https://img.shields.io/pypi/v/pypicontents.svg
   :target: https://pypi.python.org/pypi/pypicontents
   :alt: PyPI Package

.. image:: https://img.shields.io/travis/CollageLabs/pypicontents.svg
   :target: https://travis-ci.org/CollageLabs/pypicontents
   :alt: Travis CI

.. image:: https://coveralls.io/repos/github/CollageLabs/pypicontents/badge.svg?branch=master
   :target: https://coveralls.io/github/CollageLabs/pypicontents?branch=master
   :alt: Coveralls

.. image:: https://landscape.io/github/CollageLabs/pypicontents/master/landscape.svg?style=flat
   :target: https://landscape.io/github/CollageLabs/pypicontents/master
   :alt: Landscape

.. image:: https://readthedocs.org/projects/pypicontents/badge/?version=latest
   :target: https://readthedocs.org/projects/pypicontents/?badge=latest
   :alt: Read The Docs

.. image:: https://cla-assistant.io/readme/badge/CollageLabs/pypicontents
   :target: https://cla-assistant.io/CollageLabs/pypicontents
   :alt: Contributor License Agreement

.. image:: https://badges.gitter.im/CollageLabs/pypicontents.svg
   :target: https://gitter.im/CollageLabs/pypicontents
   :alt: Gitter Chat

.. _pipsalabim: https://github.com/CollageLabs/pipsalabim
.. _Contents: https://www.debian.org/distrib/packages#search_contents

PyPIContents is an application that generates a Module Index from the Python Package Index (PyPI)
and also from various versions of the Python Standard Library.

PyPIContents generates a configurable index written in ``JSON`` format that serves as a database for applications
like `pipsalabim`_. It can be configured to process only a range of packages (by initial letter) and to have
memory, time or log size limits. It basically aims to mimic what the `Contents`_ file means for a Debian
based package repository, but for the Python Package Index.

This repository stores the application in the ``master`` branch. It also stores a Module Index in the ``contents``
branch that is updated daily through a Travis cron. Read below for more information on how to use one or the other.

* Free software: GPL-3
* Documentation: https://pypicontents.readthedocs.org

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2

   installation
   usage
   api
   contributing
   authors
   history
   maintainer
