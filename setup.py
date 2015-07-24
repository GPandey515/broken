#!/usr/bin/env python

from setuptools import setup, find_packages


version = '0.0.1'

setup(
    name='broken',
    version=version,
    description='brokenlink generates brokenlink url from the command line for you',
    author='Ganesh Pandey',
    author_email='ganesh.pandey255@gmail.com',
    license='MIT',
    url='http://github.com/GPandey515',
    packages=find_packages(),
    install_requires=[
        'docopt>=0.6.1',
    ],
    entry_points={
        'console_scripts': [
            'broken=broken.broken:main'
        ],
    }
)