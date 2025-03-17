# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 12:43:53 2023

@author: crystal
"""

import requests

API_URL = 'https://saas.licensespring.com'

# Can be found in `Settings` -> `Settings` -> `Keys`
API_KEY = '12Xxxx.xxxxx'

# Send request
product_short_code = 'emtprv'
quantity = 1 # Replace with desired quantity

response = requests.get(
    #url='{}{}'.format(API_URL, '/api/v1/orders/generate_license/'),
    url='{}{}'.format(API_URL, '/api/v1/licenses/'),
    params={'limit':500,'offset':501},
    headers={
        'Authorization': 'Api-Key {}'.format(API_KEY)
    }
)

print(response.json())

f = open("licenses.txt", "a")
licenses = response.json()
#if(licenses['next'] !=''):
 #   next_customers = licenses['next']
 #   next_bool = True
for license in licenses['results']:
   #print (license)
   f.write('\n')
   for key, value in license.items():
       # print(key, '=>', value, ',')

       
        f.write( key + '=>' + str(value) + ',')
       

f.close()