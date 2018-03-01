## -*- encoding: utf-8 -*-
import os
import sys
from distutils.core import setup
from codecs import open # To open the README file with proper encoding
from setuptools.command.test import test as TestCommand # for tests
from distutils.command import build as build_module


# Get information from separate files (README, VERSION)
def readfile(filename):
    with open(filename,  encoding='utf-8') as f:
        return f.read()

# Check the right Sage version
class build(build_module.build):
    def run(self):
        from sagemath.check_version import check_version
        check_version(sage_required_version)
        build_module.build.run(self)

# For the tests
class SageTest(TestCommand):
    def run_tests(self):
        errno = os.system("sage -t --force-lib brocoli")
        if errno != 0:
            sys.exit(1)

# Specify the required Sage version
sage_required_version = '>=8.1'
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines() if i[0] != '#']
CLASSIFIERS = [i.strip() for i in open("classifiers.txt").readlines() if i[0] != '#']

setup(
    name = "brocoli",
    version = readfile("VERSION"), # the VERSION file is shared with the documentation
    description='A Sage package to work with limit roots of Coxeter groups',
    long_description = readfile("README.rst"), # get the long description from the README
    url='https://github.com/jplab/brocoli',
    author='Jean-Philippe Labbé',
    author_email='labbe@math.fu-berlin.de', # choose a main contact email
    license='GPLv2+', # This should be consistent with the LICENCE file
    classifiers=[
      # How mature is this project? Common values are
      #   3 - Alpha
      #   4 - Beta
      #   5 - Production/Stable
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Science/Research',
      'Topic :: Software Development :: Build Tools',
      'Topic :: Scientific/Engineering :: Mathematics',
      'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
      'Programming Language :: Python :: 2.7',
    ], # classifiers list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords = "SageMath",
    packages = ['brocoli'],
    cmdclass = {'test': SageTest} # adding a special setup command for tests
)
