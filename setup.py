# -*- coding: utf-8 -*-

"""libroman package installation script"""

from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='libroman',
    version='0.1.0',
    url='http://github.com/lukassup/libroman',
    description=('utility to convert Roman numerals to integers and vice versa.'),
    long_description=readme(),
    author='Lukas Šupienis',
    author_email='lukassup@yahoo.com',
    keywords='roman numerals convert digits math',
    license='GPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
    ],
    packages=find_packages(exclude=['tests']),
    test_suite='tests',
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'roman=libroman.cli:main',
        ]
    }

)
