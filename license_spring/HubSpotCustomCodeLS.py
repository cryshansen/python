
  
def main(event):
  from datetime import datetime, timedelta
  import requests
  import random
  # Use inputs to get data from any action in your workflow and use it in your code instead of having to use the HubSpot API.
  email = event["inputFields"]["email"]
  first_name = event["inputFields"]["first_name"]
  last_name = event["inputFields"]["last_name"]
  company_name = event["inputFields"]["company_name"]
  in15days = datetime.now() + timedelta(days=15)
  
  API_URL = 'https://saas.licensespring.com'

  # Can be found in `Settings` -> `Settings` -> `Keys`
  API_KEY = 'AXxxxx.xxxxx'

  # Send request
  product_short_code = 'emtprv'
  quantity = 1 # Replace with desired quantity
  try:
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
    #print(license_key)
  except:
    raise
    
  lo = 0
  hi = 10
  size = 5
  ref_id = [random.randint(lo, hi) for _ in range(size)]
  #creates a string of the random number but really we want an incremental number
  str_ref_id = ''.join(map(str,ref_id)) 
  
  jsn={
      "id": str_ref_id+"_33765",
      "is_test": True,
      "reference": "ref_usr_321",
      "customer":
      {
          "email": email,
          "first_name": first_name,
          "last_name": last_name,
          "company_name": company_name,
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
                  "email": email,
                  "is_manager": False
              },
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

  try:
    #https://eo5nv4ekryi19tp.m.pipedream.net to test the values sent
    response2 = requests.post( 
      url='https://saas.licensespring.com/api/v1/orders/create_order/',
      json=jsn,
      headers={
          'Authorization': 'Api-Key {}'.format(API_KEY),
          #'Content-type' : 'application/json',
          #'Content-Type': 'text/plain; charset=utf-8',
          'Content-Type': 'application/json', 
          'Accept':'application/json',
      }
   ) 
  
    resp = response2.json()
    license_id=""
    order_id = ""
    for order_items in resp['order_items']:
    #print(order_items)
      for licenses in order_items["licenses"]:
        license_id = licenses["id"]
        print(licenses["order"])
        order_id = licenses["order"]
        #for customer in licenses["customer"]:
  except:
    raise
  # Return the output data that can be used in later actions in your workflow.
  return {
      "outputFields": {
        "email": email,
        "first_name" : first_name,
        "last_name" : last_name,
        "license_key" : license_key,
        "order_id" : order_id,
    		"license_id": license_id,
        "valid_period": in15days.isoformat(),
        "activated": "Yes"
      }
   }