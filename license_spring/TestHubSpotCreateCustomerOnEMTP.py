# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 15:48:05 2023
@description running a test of the code in hubspot minus the def main(event): 
@author: crystal
"""
import requests


email = "john4@test.com"
first_name = "John"
last_name ="Smith"
city = "Montreal"
state_region = "Quebec"
country = "Canada"
company_name = "Test Inc"
username = "j4.smith"
tech_support_exp = "2023-09-22"
license_key = "abcd-23bm-exce"
  
API_URL = '/api/emtp-user?_format=json'

# Can be found in TBD TODO identify path on emtp.com for administration
API_KEY = '=='

jsn={
"name": { "value": username },
"mail": { "value": email },
"field_first_name": { "value": first_name },
"field_last_name": { "value": last_name },
"field_company_university": { "value": company_name },
"field_city": { "value": city },
"field_state_province": { "value": state_region },
"field_country": { "value": country },
"field_organization_type": { "value": "Industry"},
"field_maintenance_expiration": { "value": tech_support_exp },
"field_license_key" : {"value": license_key },
"role": {"value": "client"}

}



response2 = requests.post(
 url='/api/emtp-user?_format=json', 
 json=jsn,
 headers={
   'Content-Type': 'application/json', 
   'Accept':'application/json',
   'Authorization': 'Basic ==',
 },
 verify=False
   )
print(response2.headers)
print(response2.status_code)
 # return the userid to add to the client or license so can use for updating the record and sync with systems
print(response2.text)
user_resp = response2.text
#parse into an array and grab the last value of the array count?
arr = [ x.strip() for x in user_resp.strip('"').split(' ') ]
#print(arr[6])
user_id = arr[6]