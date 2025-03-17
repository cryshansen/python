# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 10:46:56 2023

@author: crystal
"""


from datetime import datetime, timedelta
import requests
import json

API_URL = 'https://saas.licensespring.com'

# Can be found in `Settings` -> `Settings` -> `Keys`
API_KEY = ''

# Send request
product_short_code = 'companyid'
quantity = 1 # Replace with desired quantity

response = requests.get(
    #url='{}{}'.format(API_URL, '/api/v1/orders/generate_license/'),
    url='{}{}'.format(API_URL, '/api/v1/orders/generate_license/?product=emtprv&quantity=1'),
    headers={
        'Authorization': 'Api-Key {}'.format(API_KEY)
    }
)


#print(response.json())
response = response.json()
license_key = response[0]
print(license_key)
user_email="test@customer.com"
in15days = datetime.now() + timedelta(days=15)

id = 1234 #int(time.time())

user_id =33617 #emtp.com user id
#cars = ["Ford", "Volvo", "BMW"]

jsn={
	"id": "1234570_33765",
	"is_test": True,
	"customer":
	{
		"email": "a@abc.com",
		"first_name": "John",
		"last_name": "Smith",
		"company_name": "Acme Inc.",
		"phone": "+1656123123123",
		"reference": "ref_usr_321"
	},
	"items": [
	{
		"product_code": "emtprv",
		"licenses": [
		{
			"key": license_key,
			"users":
			{
				"email": "a@abc.com",
				"is_manager": False
			},
            "product_features": ["EMTPWorks3", "EMTPWorks2","EMTPWorks","Panel","ScopeView","EMTPStdLibs","EMTPNetlistRun"],
			"is_trial": True,
			"validity_period": in15days.isoformat(),
			"license_type": "time-limited",
			"enable_maintenance_period": True,
			"maintenance_period": in15days.isoformat(),
			"max_license_users": 1,
			"is_floating": True,
			"floating_users": 1,
			"max_transfers": -1,
			"is_floating_cloud": False,
			"max_activations": 1,
			"prevent_vm": True,
			"can_borrow": False
		}]
	}]
}


#https://eo5nv4ekryi19tp.m.pipedream.net to test the values sent
response2 = requests.post(
    #url='{}{}'.format(API_URL, '/api/v1/orders/create_order/'),
    #url='https://eo5nv4ekryi19tp.m.pipedream.net',
    url='https://saas.licensespring.com/api/v1/orders/create_order/',
    #data = x,
    #data=json.dumps(x),
    json=jsn,
    headers={
        'Authorization': 'Api-Key {}'.format(API_KEY),
        #'Content-type' : 'application/json',
        #'Content-Type': 'text/plain; charset=utf-8',
        'Content-Type': 'application/json', 
        'Accept':'application/json',
    }
)
print(response2.headers) 
print(response2.status_code)
resp = response2.json()
print(type(resp))
print(resp)
if response2.status_code == 200:
    for order_items in resp['order_items']:
        #print(order_items)
       for licenses in order_items["licenses"]:
            print(licenses)
            print(licenses["id"])
            print(licenses["order"])
            #for customer in licenses["customer"]:
            
