import os
import sys
import warnings

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

install_requires = ['requests >= 0.8.8']

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'taxamo'))

# Get simplejson if we don't already have json
if sys.version_info < (3, 0):
    try:
        from util import json
    except ImportError:
        install_requires.append('simplejson')

setup(
    name='taxamo',
    cmdclass={'build_py': build_py},
    version='0.0.1',
    description='Taxamo python bindings',
    author='Taxamo',
    author_email='support@taxamo.com',
    url='https://taxamo.com/',
    packages=['taxamo', 'taxamo.test', 'taxamo.models'],
    package_data={'taxamo': ['data/ca-certificates.crt', '../VERSION']},
    install_requires=install_requires,
    test_suite='taxamo.test.all',
    use_2to3=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
