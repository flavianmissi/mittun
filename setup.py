from setuptools import setup, find_packages
from mittun import __version__

README = open('README.rst').read()

setup(name="mittun",
      version=__version__,
      description="conference manager",
      long_description=README,
      author="Flavia Missi",
      author_email="flaviamissi@gmail.com",
      packages=find_packages(exclude=['docs', '*.tests', '*.tests.*', 'tests.*']),
      include_package_data=True,
      install_requires=["MySQL-Python==1.2.3", "django==1.3.1", "South==0.7.3", "PIL==1.1.7"],
      tests_require=["nose==1.0.0", "django_nose==0.1.3", "coverage==3.4", "specloud==0.4.2", "splinter", "PyYAML"]
)
