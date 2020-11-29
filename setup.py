import os
from setuptools import setup, find_packages

# with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
#     README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='console_search',
    version='1.1',
    packages=find_packages(),
    include_package_data=True,
    license='GNU General Public License v3.0',
    description='Some info to desctibe our project',
    # long_description=README,
    url='https://github.com/Andrey-Yakovtsev/Urls_finder.git',
    author='Andrey-Yakovtsev',
    author_email='ayakovtsev@gmail.com',
    keywords=['search'],
    classifiers=[],
)
