#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:29:18 2020

@author: crystalhansen
"""

from datetime import datetime, timedelta

while 1:
    print ('Run something..')

    dt = datetime.now() + timedelta(hours=1)
    dt = dt.replace(minute=10)

    while datetime.now() < dt:
        time.sleep(1)