#Mittun

Conference manager.

##Bootstrap your environment

    $ [sudo] pip install -r requirements.txt

##Migrations

This project uses [South](http://south.aeracode.org) for database migrations.

###Initial migration

The first migration of an app is the ``initial migration``, you can create it by running:

    $ python manage.py schemamigration <app_name> --initial

###Add a new migration

After the initial migration, you can create new migrations by running:

    $ python manage.py schemamigration <app_name> --auto

###Running migrations

Just run on terminal:

    $ python manage.py migrate <app_name>

##Running tests

Inside the project root, you can use the Django manage.py test file for running tests:

###Unit

    $ python manage.py test unit

###Functional

    $ python manage.py test functional

###Acceptance

    $ python manage.py test acceptance
