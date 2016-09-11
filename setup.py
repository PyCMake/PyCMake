#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pip.req import parse_requirements

with open('README.rst', 'r') as fp:
    readme = fp.read()
with open('HISTORY.rst', 'r') as fp:
    history = fp.read().replace('.. :changelog:', '')


def _parse_requirements(filename):
    return [str(ir.req) for ir in parse_requirements(filename, session=False)]


requirements = _parse_requirements('requirements.txt')
dev_requirements = _parse_requirements('requirements-dev.txt')

# Require pytest-runner only when running tests
pytest_runner = (['pytest-runner>=2.0,<3dev']
                 if any(arg in sys.argv for arg in ('pytest', 'test'))
                 else [])

setup_requires = pytest_runner

setup(
    name='scikit-build',
    version='0.3.0',
    description='Improved build system generator for Python C extensions',
    long_description=readme + '\n\n' + history,
    author='The scikit-build team',
    author_email='scikit-build@googlegroups.com',
    url='https://github.com/scikit-build/scikit-build',
    packages=[
        'skbuild',
        'skbuild.platform_specifics',
        'skbuild.command',
    ],
    package_dir={'skbuild': 'skbuild',
                 'skbuild.platform_specifics': 'skbuild/platform_specifics',
                 'skbuild.command': 'skbuild/command'},
    package_data={'skbuild': ['resources/cmake/*.cmake']},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='scikit-build',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    tests_require=dev_requirements,
    setup_requires=setup_requires
)
