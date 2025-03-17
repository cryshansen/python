# -*- coding: utf-8 -*-
"""
Created on Wed Aug 7 10:20 :53 2023

@author: crystal
@param pulled all 5854 records into a file.
"""

import requests

API_URL = 'https://saas.licensespring.com'

# Can be found in `Settings` -> `Settings` -> `Keys`
API_KEY = '12Xxxx.xxxxx'

# Send request
product_short_code = 'compname'
quantity = 1 # Replace with desired quantity

response = requests.get(
    #url='{}{}'.format(API_URL, '/api/v1/orders/generate_license/'),
    
    url='{}{}'.format(API_URL, '/api/v1/customers/'),
    #license params
    #params={'product': product_short_code, 'range': 'last30'},
    params={'limit':5854,'offset':0},
    headers={
        'Authorization': 'Api-Key {}'.format(API_KEY)
    }
)


#print(response.json())


#open and read the file after the appending:
#f = open("demofile2.txt", "r")
#print(f.read())
f = open("customers.txt", "a")
customers = response.json()
#if(customers['next'] !=''):
 #   next_customers = customers['next']
 #   next_bool = True
for customer in customers['results']:
   #print (customer)
   f.write('\n')
   for key, value in customer.items():
       # print(key, '=>', value, ',')

       
        f.write( key + '=>' + str(value) + ',')
       

f.close()