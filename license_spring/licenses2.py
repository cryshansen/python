# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:08:34 2023

@author: crystal
"""

import requests #to make  API calls
import csv  # to make csv file to load the values
#import json #to use dictionary component
# field names 
fields=[]

# data rows of csv file 
rows = []

API_URL = 'https://saas.licensespring.com'

# Can be found in `Settings` -> `Settings` -> `Keys`
API_KEY = '12Xxxx.xxxxx'


#License API request.get().json() call to license spring
license_api = requests.get(
    url='{}{}'.format(API_URL, '/api/v1/licenses/'),
    params={'limit':100,'offset':101},
    headers={
        'Authorization': 'Api-Key {}'.format(API_KEY)
    }
).json()


licenses = license_api["results"]
#f = open("licenses2.txt", "a")
while license_api["next"]:
    license_api = requests.get(
                        license_api["next"],
                        headers={
                            'Authorization': 'Api-Key {}'.format(API_KEY)
                        }
                    ).json()
    #f.write( str(license_api) )
    #f.write('\n')
    #append to the existing results json array?
    licenses.extend(license_api["results"])


#f = open("licenses2-processed.txt", "a")
for license in licenses:
   #print (customer)
   #f.write('\n')
       
# field names or column names
#fields = ['Name', 'Branch', 'Year', 'CGPA'] 
    
   for key, value in license.items():
       #print(key, '=>', value, ',')

       fields.append(key)
       #f.write( key + '=>' + str(value) + ',')
       

#f.close()




#example to iterate over the list of results of licenses fed into  
#printing license id and license fields
#for i, row in enumerate(licenses):
    #print(i, row['id'], row['status'],row['floating_in_use_devices'],)
    #print('customer') #an object with multiple values
    #print('product_features') #object of modules for emtp with multiple values multiple 'product_feature'
    #print('product_custom_fields') #object with values related to modules or is modules? difference between above field and this one?
    #print('license_users') #object of multiple records one or more
    
#converting the file to an csv for injesting into either mysql or hubspot via spreadsheet load
#create the 'fields' array via the 'key'
#create the rows via values

  

# my data rows as dictionary objects 
#mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'}, 
#         {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'}, 
#        {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'}, 
#         {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'}, 
#         {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'}, 
#         {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}] 
    
# field names 
#fields = ['name', 'branch', 'year', 'cgpa'] 
    
# name of csv file 
filename = "license_records.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader() 
        
    # writing data rows 
    #writer.writerows(mydict) 
    writer.writerows(licenses)