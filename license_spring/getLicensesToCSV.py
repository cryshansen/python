# -*- coding: utf-8 -*-
"""
Created on Wed Aug 7 10:20 :53 2023

@author: crystal
@param pulled all 5854 records into a file.

This python works and stores the customers with a company object as well.

file - "ls-license-test.csv"
file - "ls-licenses.csv" did not respect the limit provided. must use the iterator of licenses2.py



"""

import requests
import csv

# field names 
fields=[]

API_URL = 'https://saas.licensespring.com'

# Can be found in `Settings` -> `Settings` -> `Keys`
API_KEY = 'Xx.xx'

# Send request
product_short_code = 'companyid'
quantity = 1 # Replace with desired quantity




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
    #append to the existing results json array?
    licenses.extend(license_api["results"])


for license in licenses:
    fields = license.keys()
    break
    
print(fields)

"""
TODO: separate variables that are: 
    customer array(customer) 
    ,product_features(array aka emtpworks),
    ,product_custom_fields(array modules)
    ,product(emtp an array)
    ,license_users(array-licensevals)
save to separate csv files for loading store id in license table for normalized database. 
then for extract to hubspot create csv for loading into hubspot.

hs_license table exists in local crm database to use as the basis of keynames 
and may be loaded with the finalized data to compare to


"""

filename = "ls-licenses.csv"
#print(fields)
# writing to csv file  
with open(filename, 'w') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader() 
        
    # writing data row in this case of query above. 
    writer.writerows(licenses) 