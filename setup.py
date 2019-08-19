#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from io import open
import sys


setup(
    name='gender_guesser',
    version='0.1',
    packages=['gender_guesser'],
    package_dir={'gender_guesser': 'gender_guesser'},
    package_data={'gender_guesser': ['data/*']},
    license='GPLv3',
    description='Get the gender from first name.',
)
