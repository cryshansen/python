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
product_short_code = 'compname'
quantity = 1 # Replace with desired quantity

response = requests.get(
    #url='{}{}'.format(API_URL, '/api/v1/orders/generate_license/'),
    url='{}{}'.format(API_URL, '/api/v1/devices/'),
    params={'limit': 234, 'offset': 0},
    headers={
        'Authorization': 'Api-Key {}'.format(API_KEY)
    }
)

#print(response.json())
devices = response.json()
f = open("devices.txt", "a")
for device in devices['results']:
   print (device)
  # for product_features in product['product_features']:
       #print(product_features)
   #    print(product_features['id'],", ", product_features['name'])
   f.write('\n')
   for key, value in device.items():
        print(key, '=>', value, ',')

       
        f.write( key + '=>' + str(value) + ',')
       

f.close()