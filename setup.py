#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version(filename):
    import ast
    version = None
    with open(filename) as f:
        for line in f:
            if line.startswith('__version__'):
                version = ast.parse(line).body[0].value.s
                break
        else:
            raise ValueError('No version found in {}.'.format(filename))
    if version is None:
        raise ValueError(filename)
    return version


#version = get_version(filename='src/__init__.py')

setuptools.setup(
    name='witnesscomplex',
    version='0.0.2',
    author='Simon Schoenenberger',
    author_email='schsimo@ethz.ch',
    package_dir={'': 'src'},
    #packages=setuptools.find_packages('src'),
    packages=setuptools.find_packages(include=['src', 'src.*']),
    url='https://github.com/MrBellamonte/WitnessComplex',
    description='Witness complex construction package.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.7',
)
