"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""
# Always prefer setuptools over distutils
from setuptools import setup
import pandas
import numpy

setup(
    name='dspt11-assignment-pmorg',  # Required
    version='0.0.1',  # Required
    author='Petr Morgoun',  # Optional
    author_email='petr-morgoun@lambdastudents.com',  # Optional
    keywords='helper functions',  # Optional
    packages=['mymodules'],  # Required
    python_requires='>=3.6, <4',
    install_requires=[pandas, numpy],  # Optional
)