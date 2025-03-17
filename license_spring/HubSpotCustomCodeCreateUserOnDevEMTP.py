# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:14:17 2023

@author: crystal
@description This code is to create a user on emtp in custom code on hubspot 

"""

import requests

def main(event):
#/api/v1/customers/export/

  email = event["inputFields"]["email"]
  first_name = event["inputFields"]["first_name"]
  last_name = event["inputFields"]["last_name"]
  city = event["inputFields"]["city"]
  state_region = event["inputFields"]["state_region"]
  country = event["inputFields"]["country"]
  company_name = event["inputFields"]["company_name"]
  username = event["inputFields"]["client_username"]
  tech_support_exp = event["inputFields"]["tech_support_exp"]
  license_key = event["inputFields"]["license_key"]
  
  API_URL = '/api/emtp-user?_format=json'

# Can be found in TBD TODO identify path on emtp.com for administration
  API_KEY = 'Xxxxx=='

  jsn={
    "name": { "value": username },
    "mail": { "value": email },
    "field_first_name": { "value": first_name },
    "field_last_name": { "value": last_name },
    "field_company_university": { "value": company_name },
    "field_city": { "value": city },
    "field_state": { "value": state_region },
    "field_country": { "value": country },
    #"field_organization_type": { "value": "Industry"},
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
  response_arr = response2.text.split()
  
 # return the userid to add to the client or license so can use for updating the record and sync with systems
 # Return the output data that can be used in later actions in your workflow.
  return {
   "outputFields": {
     "email": email
   }
 }