# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:41:34 2023

@author: crystal
"""

import random
import numpy as np

lo = 0
hi = 10
size = 5
ref_id = [random.randint(lo, hi) for _ in range(size)]
str_ref_id = ''.join(map(str,ref_id))
print(ref_id)
print(str_ref_id)

product_addons = "Renewables;PSSEtoEMTPTool"
product_features_default ="EMTPWorks3;EMTPWorks2;EMTPWorks;Panel;ScopeView;EMTPStdLibs;EMTPNetlistRun;"


my_prod_features_default = [ x.strip() for x in product_features_default.split(';') ]
my_prod_addons = [ x.strip() for x in product_addons.split(';') ]
my_prod_features_default.extend(my_prod_addons)
print(my_prod_features_default)
#