#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.test import test as TestCommand
from io import open
import sys


setup(
    name='gender_guesser',
    version='0.1',
    author='Israel Saeta Pérez',
    author_email='israel@lead-ratings.com',
    packages=['gender_guesser'],
    package_dir={'gender_guesser': 'gender_guesser'},
    package_data={'gender_guesser': ['data/*.txt']},
    test_suite='test',
    tests_require=['tox'],
    cmdclass = {'test': Tox},
    url='https://github.com/lead-ratings/gender-guesser',
    license='GPLv3',
    description='Get the gender from first name.',
)
