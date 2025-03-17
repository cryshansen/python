# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 12:43:53 2023

@author: crystal
@description new file to create a license with python if we go the route of webhooks.
"""

import requests

API_URL = 'https://saas.licensespring.com'

# Can be found in `Settings` -> `Settings` -> `Keys`
API_KEY = '12Xxxx.xxxxx'

# Send request
product_short_code = 'companyname'
quantity = 1 # Replace with desired quantity

response = requests.get(
    #url='{}{}'.format(API_URL, '/api/v1/orders/generate_license/'),
    url='{}{}'.format(API_URL, '/api/v1/license-custom-fields/'),
    params={'product': product_short_code, 'quantity': quantity},
    headers={
        'Authorization': 'Api-Key {}'.format(API_KEY)
    }
)

print(response.json())