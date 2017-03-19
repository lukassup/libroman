libroman
========

.. image:: https://travis-ci.org/lukassup/libroman.svg?branch=master
    :target: https://travis-ci.org/lukassup/libroman

libroman is a Python package which is used to convert Roman numerals to
integers and vice versa.

.. _installation:

Installation
------------

Supported versions of Python are: 2.7, 3.3, 3.4, and 3.5. The recommended way
to install this package is via `pip <https://pypi.python.org/pypi/pip>`_.

.. code-block:: bash

    $ git clone https://github.com/lukassup/libroman.git
    $ pip install ./libroman

For instructions on installing python and pip see "The Hitchhiker's Guide to
Python" `Installation Guides
<http://docs.python-guide.org/en/latest/starting/installation/>`_.

.. _usage:

Usage
-----

.. code-block:: python

    from libroman import Roman

    Roman(999) == Roman('CDXIV')

