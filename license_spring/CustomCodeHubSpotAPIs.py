# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 17:07:41 2023

@author: crystal
work in progress of the license field updating.
"""

import os
from hubspot import HubSpot
import hubspot
from pprint import pprint
from hubspot.crm.deals import ApiException
from hubspot.crm.line_items import ApiException

def main(event):
  # Use inputs to get data from any action in your workflow and use it in your code instead of having to use the HubSpot API.
  license_id = event["inputFields"]["license_id"]
  license_key = event["inputFields"]["license_key"]
  order_id = event["inputFields"]["order_id"]
  valid_period = event["inputFields"]["valid_period"]
  
  # How to use secrets
  # Secrets are a way for you to save API keys or private apps and set them as a variable to use anywhere in your code
  # Each secret needs to be defined like the example below

  #hubspot = HubSpot(access_token=os.getenv('SECRET_NAME'))


  client = hubspot.Client.create(access_token="xxxx")

  try:
      api_response = client.crm.deals.basic_api.get_by_id(deal_id="dealId", archived=False)
      pprint(api_response)
  except ApiException as e:
      print("Exception when calling basic_api->get_by_id: %s\n" % e)
  
  

  #client = hubspot.Client.create(access_token="YOUR_ACCESS_TOKEN")

  try:
    api_response = client.crm.line_items.basic_api.get_page(limit=10, archived=False)
    pprint(api_response)
  except ApiException as e:
    print("Exception when calling basic_api->get_page: %s\n" % e)
  
  
  
  # Return the output data that can be used in later actions in your workflow.
  return {
    "outputFields": {
      #"email": email
    }
  }