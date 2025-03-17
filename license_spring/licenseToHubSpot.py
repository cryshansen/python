# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:22:17 2023

@author: crystal
call hubspot to get the fields one per line

"""

import requests #to make API calls



API_URL = 'https://api.hubspot.com'

# Can be found in `Settings` -> `Settings` -> `Keys`
API_KEY = '12Xxxxxxxxx'


#License API request.get().json() call to HUBSPOT
license_api = requests.get(
    url='{}{}'.format(API_URL, '/crm/v3/schemas/#-###'), #/crm/v3/schemas/{objectTypeId}
   #params={'limit':100,'offset':101},
    headers={
        'Authorization': 'Bearer {}'.format(API_KEY)
    }
).json()

#print(license_api)
properties = license_api['properties']
for propertie in properties:
    print(propertie, "\n")
    print(propertie['name']," ", propertie['type'], " ," )
    #for item in row:
      #print(row['properties'])#backwards as id is after properties so capture properties first then clear if not correct id
      #print(item)