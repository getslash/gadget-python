#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Logbook',
    'munch',
]

test_requirements = [
]

setup(
    name='gadget-python',
    version='0.1.0',
    description="Python utilities for emitting and processing Gadget log entries",
    long_description=readme + '\n\n' + history,
    author="Slash Team",
    author_email='vmalloc@gmail.com',
    url='https://github.com/getslash/gadget-python',
    packages=[
        'gadget',
    ],
    package_dir={'gadget':
                 'gadget'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='gadget_python',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
