import os
import sys
import nose
from django.conf import settings

curdir = os.path.abspath(os.path.dirname(__file__))

class SpecloudTestRunner(object):

    def __init__(self, verbosity=2, **kwargs):
        self.verbosity = verbosity
        settings.DEBUG = False

    def run_tests(self, test_labels, extra_tests=[], **kwargs):
        nose_argv = [
            'specloud', '-s', '--verbosity=2', '--exe', '--with-coverage', '--cover-inclusive'
        ]
        package = os.path.split(os.path.dirname(__file__))[-1]
        app_names = [app for app in settings.INSTALLED_APPS if not app.startswith("django") and app != 'lettuce.django']

        nose_argv.extend(map(lambda name: "--cover-package=%s" % name, app_names))
        nose_argv.extend(map(lambda name: "--cover-package=%s.%s" % (package, name), app_names))

        nose_argv.append('--nologcapture')

        if sys.argv[-1] in ('unit', 'functional', 'integration'):
            kind = sys.argv[-1]
            apps = map(lambda app: "%s/tests/%s" % (app, kind), app_names)
        else:
            apps = app_names

        nose_argv.extend(apps)

        try:
            os.remove(os.path.join(curdir, '.coverage'))
        except:
            pass

        passed = nose.run(argv=nose_argv)

        if passed:
            return 0
        else:
            return 1
