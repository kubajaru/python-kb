# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Python Knowledge Base',
    long_description=readme,
    author='Jakub Jaruga',
    author_email='kubajaru@gmail.com',
    url='https://github.com/kubajaru/python-kb',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

