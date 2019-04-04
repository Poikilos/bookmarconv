#!/usr/bin/env python
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='bookmarconv',
      version='0.1',
      description='Analysis tools for bookmark files created with the goal to convert Firefox JSON backup to xBrowserSync',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: General',
      ],
      keywords='python bookmark JSON file analysis conversion bookmarconv',
      url='http://github.com/poikilos/bookmarconv',
      author='Jake Gustafson',
      author_email='7557867+poikilos@users.noreply.github.com',
      license='GPLv3+',
      packages=['bookmarconv'],
      install_requires=[
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['bookmarconv=bookmarconv.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
