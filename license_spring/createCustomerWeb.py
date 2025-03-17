# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:00:06 2023

@author: crystal
@description: Send Create User to api endpoint on emtp.com

"""

import requests


#/api/v1/customers/export/



API_URL = '/api/post/user-create?_format=json'

# Can be found in TBD TODO identify path on emtp.com for administration
API_KEY = '==xxxx' #username:password base 64 encoded https://www.base64encode.org/

jsn={

    "name": { "value": "crystalH" },

    "mail": { "value": "example@example.com" },

    "field_city": { "value": "Montreal" },

    "field_company_university": { "value": "McGill University" },

    "field_country": { "value": "Canada" },

    "field_first_name": { "value": "Crystal" },

    "field_last_name": { "value": "Hansen" },

    "field_organization_type": { "value": "Industry"},

    "role": {"value": "client"}

}

response2 = requests.post(
   url='api/post/user-create?_format=json',
   json=jsn,
   headers={
       'Content-Type': 'application/json', 
       'Accept':'application/json',
       'Authorization': 'Basic xxxx==',
   },
   verify=False
 )
print(response2.headers)
print(response2.status_code)
# return the userid to add to the client fields
resp_arr =response2.text.split()