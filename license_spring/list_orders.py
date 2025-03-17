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
    url='{}{}'.format(API_URL, '/api/v1/orders/'),
    params={'product': product_short_code},
    headers={
        'Authorization': 'Api-Key {}'.format(API_KEY)
    }
)


#print(response.json())
orders = response.json()

for order in orders['results']:
   #print (product)
   for key, value in order.items():
       if(key == 'customer'):
           customer = value
           print(customer)
       else:    
         print(key, '=>', value)
 # for order_customer in order['customer']:
 #       print(product_features['id'],", ", product_features['name'])