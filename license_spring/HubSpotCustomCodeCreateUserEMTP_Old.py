# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 18:16:52 2023

@author: crystal
this file is old. We do not need to call the token here. It is done through the api on emtp.com
"""

def main(event):
  # Use inputs to get data from any action in your workflow and use it in your code instead of having to use the HubSpot API.
  email = event["inputFields"]["email"]
  first_name = event["inputFields"]["first_name"]
  last_name = event["inputFields"]["last_name"]
  company_name = event["inputFields"]["company_name"]
  username = first_name + "."+last_name

  import requests
  API_URL = '/session/token'


  response = requests.get(
    #url='{}{}'.format(API_URL, '/api/v1/orders/generate_license/'),
    url='/session/token',
    verify=False
  )


#print(response.json())
#response = response.text #json()
  token = response.content.decode()
  
  jsn={

        "name": [

            {"value": username }

        ],

        "mail": [

            {"value": email}

        ],

        "field_city": [

            {"value": "Delhi"}

        ],

        "field_company_university": [

            {"value": company_name}

        ],

        "field_country": [

            {"value": "India"}

        ],

        "field_first_name": [

            {"value": first_name}

        ],

        "field_last_name": [

            {"value": last_name}

        ],

        "field_organization_type": [

            {"value": "Industry"}

        ]

    }

  response2 = requests.post(
    url='/user/register?_format=json',
    json=jsn,
    headers={
        'Content-Type': 'application/json', 
        'Accept':'application/json',
        'X-CSRF-Token': token
    },
    verify=False
  )
#status = response2.status_code 
  
  
  
  # Return the output data that can be used in later actions in your workflow.
  return {
    "outputFields": {
      "email": email
    }
  }