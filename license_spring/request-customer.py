# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:00:06 2023

@author: crystal
@description: this file gets a small request value and writes to a csv

suspect not able to get values because of api access limitation

"""

# importing the csv module 
import csv 
import requests


#/api/v1/customers/export/



API_URL = 'https://saas.licensespring.com'

# Can be found in `Settings` -> `Settings` -> `Keys`
API_KEY = '12Xxxx.xxxxx'

# Send request
product_short_code = 'compname'
quantity = 1 # Replace with desired quantity

response = requests.get(
    #url='{}{}'.format(API_URL, '/api/v1/orders/generate_license/'),
    
    url='{}{}'.format(API_URL, '/api/v1/customers/export/'),
    #license params
    #params={'product': product_short_code, 'range': 'last30'},
    #params={'limit':5854,'offset':0},
    headers={
        'Authorization': 'Api-Key {}'.format(API_KEY)
    }
)

#print(response.json())
customers = response.json()
#if(customers['next'] !=''):
 #   next_customers = customers['next']
 #   next_bool = True
for customer in customers['results']:
    print (customer)
    #print(customer.items())