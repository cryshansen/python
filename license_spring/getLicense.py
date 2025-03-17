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
API_KEY = 'Xxxxxx.xxxxx'

# Send request
product_short_code = 'emtprv'
quantity = 1 # Replace with desired quantity

response = requests.get(
    #url='{}{}'.format(API_URL, '/api/v1/orders/generate_license/'),
    
    url='{}{}'.format(API_URL, '/api/v1/licenses/1234567890/'),
    #license params
    #params={'product': product_short_code, 'range': 'last30'},
    #params={'limit':5854,'offset':0},
    #params={'id':'1309554162'}
    headers={
        'Authorization': 'Api-Key {}'.format(API_KEY)
    }
)

#print(response.json())
license = response.json()
#print(customer.keys())
fields = license.keys()
records = license.values()
print(fields)
print(records)
print(type(records))

for element in records:
    print(element,',')
    #for key,value in element:
      #print(key, '=>', value, ',')
   
       


def writecsv(filename, dct):
   
    with open(filename, "w") as file:
        outfile = csv.DictWriter(file, fieldnames=dct.keys())
        outfile.writeheader()
        outfile.writerows(dct.items()) 
        #for item in dct.items():
            #outfile.writerow(item)


#writecsv("data.csv", data)









filename = "license-record-1234567890.csv"
#print(fields)
# writing to csv file  
with open(filename, 'w') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader() 
        
    # writing data row in this case of query above. 
    writer.writerow(license) 