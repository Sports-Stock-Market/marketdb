from setuptools import setup, find_packages

with open('requirements.txt') as reqs_f:
    reqs = reqs_f.read().splitlines()

setup(
    name='marketdb',
    version='1.0',
    description='DB interface for sports stock market',
    author='Vedant Pathak',
    author_email='vpathak@uchicago.edu',
    packages=find_packages(),
    install_requires=reqs
)
