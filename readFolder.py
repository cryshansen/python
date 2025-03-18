#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:34:19 2020

@author: crystalhansen
"""
from pathlib import Path
import os
from os import listdir
from os.path import isfile, join
home = str(Path.home())
print(home)
      
location = os.path.join(home, 'Documents','CWBTrackerScreenshots')
print(location)

from os import walk


for (dirpath, dirnames, filenames) in walk(location):
    print(filenames)
    break