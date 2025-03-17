# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 12:43:53 2023

@author: crystal
@description request of all unique product and product features in license spring 
"""

import requests
import csv

# field names or column names
fields=['id','name']
# data rows of csv file must have keys within row
rows = []
API_URL = 'https://saas.licensespring.com'

# Can be found in `Settings` -> `Settings` -> `Keys`
API_KEY = '84bzumf9.xl9QkVWvy3i7yFIY3jhD33K9oUy3aACc'

# Send request
product_short_code = 'emtprv'
quantity = 1 # Replace with desired quantity

response = requests.get(
    #url='{}{}'.format(API_URL, '/api/v1/orders/generate_license/'),
    url='{}{}'.format(API_URL, '/api/v1/products/'),
    params={'product': product_short_code, 'quantity': quantity},
    headers={
        'Authorization': 'Api-Key {}'.format(API_KEY)
    }
)

#print(response.json())
products = response.json()

for product in products['results']:
   #print (product)
   rows.extend(product['product_features'])
   for product_features in product['product_features']:
       #fields.append(key)
       print(product_features)
       for key, value in product_features:
           print(key)
           #print(product_features['id'],", ", product_features['name'])
      
       
       
filename = "products_records.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader() 
        
    # writing data rows 
    #writer.writerows(mydict) 
    writer.writerows(rows)