import os
import sys
import subprocess
from django.conf import settings
from django.test.simple import DjangoTestSuiteRunner

curdir = os.path.abspath(os.path.dirname(__file__))


class SpecloudTestRunner(DjangoTestSuiteRunner):

    def __init__(self, verbosity=2, **kwargs):
        self.verbosity = verbosity
        self.interactive = True
        settings.DEBUG = False

    def run_tests(self, test_labels, extra_tests=[], **kwargs):
        specloud_argv = [
            'specloud', '-s', '--verbosity=2', '--exe', '--with-coverage', '--cover-inclusive'
        ]
        package = os.path.split(os.path.dirname(__file__))[-1]
        app_names = [app for app in settings.INSTALLED_APPS if not app.startswith("django") and app != 'lettuce.django' and app not in settings.SKIP_TESTS]

        specloud_argv.extend(map(lambda name: "--cover-package=%s" % name, app_names))
        specloud_argv.extend(map(lambda name: "--cover-package=%s.%s" % (package, name), app_names))

        specloud_argv.append('--nologcapture')

        if sys.argv[-1] in ('unit', 'functional', 'acceptance'):
            kind = sys.argv[-1]
            apps = map(lambda app: "%s/tests/%s" % (app, kind), app_names)
        else:
            apps = app_names

        specloud_argv.extend(apps)

        try:
            os.remove(os.path.join(curdir, '.coverage'))
        except:
            pass

        old_config = self.setup_databases()
        result = subprocess.call(specloud_argv)
        self.teardown_databases(old_config)

        return result
