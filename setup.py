#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages

if sys.argv[-1] == 'install':
    setup(name='pycolony',
          version='0.1.1',
          description='Python Machine Colony SDK',
          author='Machine Colony Inc.',
          author_email='maxwell@machinecolony.com',
          url='https://github.com/MachineColony/pyColony',
          packages=find_packages()
          )
