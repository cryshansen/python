# -*- coding: utf-8 -*-
"""
Created on Wed Aug 7 10:20 :53 2023

@author: crystal
"""

import requests
import json

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
    params={'limit':100,'offset':100},
    headers={
        'Authorization': 'Api-Key {}'.format(API_KEY)
    }
)





customer_api = response.json()
customers = customer_api["results"]
while customer_api["next"]:
    customer_api = requests.get(customer_api["next"]).json()
    print(customer_api["results"])
    #customers.extend(customer_api["results"])

#printing license customer data
for i, customer in enumerate(customers):
    print(i, customer['id'], customer['email'],customer['first_name'],customer['last_name'],customer['company_name'],customer['phone'],customer['country'], customer['city'],customer['state'],customer['license_user'])
    
    