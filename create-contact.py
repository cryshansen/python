def main(event):
  import requests

  email = event["inputFields"]["email"]
  first_name = event["inputFields"]["first_name"]
  last_name = event["inputFields"]["last_name"]
  city = event["inputFields"]["city"]
  state_region = event["inputFields"]["state_region"]
  country = event["inputFields"]["country"]
  company_name = event["inputFields"]["company_name"]
  username = event["inputFields"]["client_username"]
  tech_support_exp = event["inputFields"]["maintenance_renewal_date"]
  license_key = event["inputFields"]["licensing_key"]
  
  API_URL = '/api/emtp-user?_format=json'

# TBD if we use it as a secret key in our code
# TODO identify path on emtp.com for administration of the key
  API_KEY = 'xxxxx'

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
       'Authorization': 'Basic xxxxx',
     },
     verify=False
   )
  print(response2.headers)
  print(response2.status_code)
# return the userid to add to the client fields
  user_id = ""
  #if response["user_id"]:
    #user_id = response["user_id"]
 # Return the output data that can be used in later actions in your workflow.
  return {
    "outputFields": {
      "user_id": user_id
    }
  }
