#-*- coding:utf-8 -*-
from os.path import dirname
from optparse import make_option
from django.core.management.base import BaseCommand
from django.conf import settings
from events.management.browser_helper import browser

import nose
import time


class Command(BaseCommand):

    browser = None
    help = "Run acceptance tests"

    option_list = BaseCommand.option_list + (
        make_option("-a", "--app", dest="app", default=None),
    )

    def handle(self, *args, **options):

        # if not options['sem_db_migrate']:
        #     print 'cleaning temp data...'
        #     self.clean()
        #     print 'reseting database...'
        #     self.reset_db()

        app = options["app"]

        if app:
            apps = [app]
        else:
            apps = settings.TESTABLE_APPS

        self.run(apps)

    def clean(self):
        self.run_target(self.clean_target)

    def run_target(self, target):
        target.execute()
        while not target.poll():
            time.sleep(0.5)

    def reset_db(self):
        self.run_target(self.db)

    def run(self, apps):
        nose_argv = ['nosetests','-sd', '--verbosity=2', '--nologcapture']

        test_file = False
        test_type = 'acceptance'

        modules = []
        if not test_file:
            for app in apps:
                test_module_path = "%s.tests" % (app)
                try:
                    module = getattr(__import__(test_module_path, locals(), globals(), [test_type], 3), test_type)
                    modules.append(module)
                except AttributeError:
                    pass
            nose_argv.extend([dirname(x.__file__) for x in modules])

        else:
            nose_argv.append(test_file)
        ret = nose.run(argv=nose_argv)

        browser.quit()

        if ret:
            code = 0
        else:
            code = 1
