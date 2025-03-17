# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:20:17 2023

@author: crystal
"""
# importing the csv module 
import csv 
import requests



#/api/v1/customers/export/


fields=[]
records =[]
API_URL = 'https://saas.licensespring.com'

# Can be found in `Settings` -> `Settings` -> `Keys`
API_KEY = 'Xxxxx.xxxxxxx'

# Send request
product_short_code = 'companyid'
quantity = 1 # Replace with desired quantity

response = requests.get(
    #url='{}{}'.format(API_URL, '/api/v1/orders/generate_license/'),
    
    url='{}{}'.format(API_URL, '/api/v1/licenses/16612345434567890/'),
    #license params
    #params={'product': product_short_code, 'range': 'last30'},
    #params={'limit':5854,'offset':0},
    #params={'id':'123434343'}
    headers={
        'Authorization': 'Api-Key {}'.format(API_KEY)
    }
)

#print(response.json())
order = response.json()
#print(customer.keys())
fields = order.keys()
#records = order.values()
print(fields)



filename = "order-record-1234567.csv"
#print(fields)
# writing to csv file  
with open(filename, 'w') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader() 
        
    # writing data row in this case of query above. 
    writer.writerow(order) 