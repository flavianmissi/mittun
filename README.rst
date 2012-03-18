Mittun
======

OpenSource Conference Manager.

Installation
============

Install via pip::

    $ pip install mittun

Bootstrap your environment
--------------------------

    $ [sudo] pip install -r requirements.txt

Migrations
------------

This project uses `South <http://south.aeracode.org>`_ for database migrations.

Initial migration
-----------------

The first migration of an app is the ``initial migration``, you can create it by running:

    $ python manage.py schemamigration <app_name> --initial

Add a new migration
-------------------

After the initial migration, you can create new migrations by running:

    $ python manage.py schemamigration <app_name> --auto

Running migrations
------------------

Just run on terminal:

    $ python manage.py migrate <app_name>

Running tests
^^^^^^^^^^^^^

Inside the project root, you can use the Makefile for running tests:

Unit
^^^^

    $ make unit

Functional
^^^^^^^^^^

    $ make functional

Acceptance
^^^^^^^^^^

    $ make acceptance

All tests
^^^^^^^^^
    $ make tests
