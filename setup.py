#!/usr/bin/env python
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_reqs = ['autopep8', 'haralyzer @ git+https://github.com/mrname/haralyzer.git']
if sys.version_info < (3, 4):
    install_reqs.extend([
        "backports.statistics",
    ])

setup(
        name='har2tests',
        version='1.0.0',
        description='A python framework for getting useful stuff out of HAR files',
        long_description='',
        author='',
        author_email='',
        url='https://github.com/tinhien11/har2tests',
        download_url='https://github.com/tinhien11/har2tests',
        packages=[
            'har2tests'
        ],
        package_dir={'har2tests': 'src'},
        install_requires=install_reqs,
        extras_require={
        },
        license='MIT',
        zip_safe=False,
        keywords='har',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 3',
        ],
        entry_points={
          'console_scripts': [
              'har2tests = har2tests.src.har2tests:main'
          ]
      },
)