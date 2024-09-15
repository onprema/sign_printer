from setuptools import setup, find_packages
from sign_printer import __version__ as version

setup(
    name='sign_printer',
    version=version,
    packages=find_packages(),
    install_requires=[
        'pyfiglet',
    ],
)
