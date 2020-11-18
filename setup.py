import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='witnesscomplex',
    version='0.0.1',
    author='Simon Schoenenberger',
    author_email='schsimo@ethz.ch',
    packages=['witnesscomplex'],
    url='https://github.com/MrBellamonte/WitnessComplex',
    description='Witness complex construction package.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
)
