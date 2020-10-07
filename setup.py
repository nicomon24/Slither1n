from glob import glob
from setuptools import setup, find_packages

setup(
    name='sneks',
    version='0.0.2',
    install_requires=['gym','numpy'],
    packages=find_packages(),
)
