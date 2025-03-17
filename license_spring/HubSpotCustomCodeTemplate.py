# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 11:15:46 2023
@email 'inputField' is the fields accessible in the form to create an object
@email 'outputFields' is the value available to the workflow the custom code is in.
@author: crystal
"""

def main(event):
  # Use inputs to get data from any action in your workflow and use it in your code instead of having to use the HubSpot API.
  email = event["inputFields"]["email"]
  # Return the output data that can be used in later actions in your workflow.
  return {
    "outputFields": {
      "email": email
    }
  }