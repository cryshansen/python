# -*- coding: utf-8 -*-
"""
Created on Wed Aug 7 10:20 :53 2023

@author: crystal
@param pulled all 5854 records into a file.

This python works and stores the customers with a company object as well.

file - "ls-customers-test.csv"

"""

import requests
import csv

# field names 
fields=[]

API_URL = 'https://saas.licensespring.com'

# Can be found in `Settings` -> `Settings` -> `Keys`
API_KEY = 'Xxxxxxx.xxxxx'

# Send request
product_short_code = 'companyId'
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


results = response.json()
customers = results['results']
#print(customers)
for customer in customers:
#    customer.keys()
    fields = customer.keys()
    
print(fields)



filename = "ls-customers-test.csv"
#print(fields)
# writing to csv file  
with open(filename, 'w') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader() 
        
    # writing data row in this case of query above. 
    writer.writerows(customers) 