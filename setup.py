#!/usr/bin/env python
from setuptools import setup

# This is to disable the 'black magic' surrounding versioned repositories... Terrible!
from setuptools.command import sdist
del sdist.finders[:]

description = \
"""Embellish is a low-friction static website generator.

Docs at http://github.com/boscoh/embellish.
"""

setup(
    name='embellish',
    version='0.9',
    author='Bosco Ho',
    author_email='boscoh@gmail.com',
    url='http://github.com/boscoh/embellish',
    description='Static site generator',
    long_description=description,
    license='BSD',
    install_requires=[
        'markdown',
        'PyYaml',
        'jinja2', 
        'hamlpy',
        'python-dateutil',
        'sassin',
        'pyScss',
        'flask',
    ],
    packages=['embellish',],
    package_data={"embellish": ['defaults/default.haml',]},
    scripts=['bin/embellish'],
)