# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:08:34 2023

@author: crystal
@description this is the working copy of licenses and files  
"""

import requests #to make License Spring API calls
import csv # to make csv file to load the values


API_URL = 'https://saas.licensespring.com'

# Can be found in `Settings` -> `Settings` -> `Keys`
API_KEY = '12Xxxx.xxxxx'


#Discover API url filtered to movies >= 2004 and containing Drama genre_ID: 18
#discover_api = 'https://api.themoviedb.org/3/discover/movie? 
#api_key=['my api key']&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&primary_release_year=>%3D2004&with_genres=18'

orders_api = requests.get(
    #url='{}{}'.format(API_URL, '/api/v1/orders/generate_license/'),
    url='{}{}'.format(API_URL, '/api/v1/orders/'),
    params={'limit':100,'offset':101},
    headers={
        'Authorization': 'Api-Key {}'.format(API_KEY)
    }
).json()

#discover_api = requests.get(discover_api).json()
orders = orders_api["results"]
#f = open("licenses2.txt", "a")
while orders_api["next"]:
    orders_api = requests.get(
                        orders_api["next"],
                        headers={
                            'Authorization': 'Api-Key {}'.format(API_KEY)
                        }
                    ).json()
    #f.write( str(orders_api) )
    #f.write('\n')
    orders.extend(orders_api["results"])


f = open("orders.txt", "a")
for order in orders:
   #print (customer)
   f.write('\n')
   for key, value in order.items():
       #print(key, '=>', value, ',')

       
        f.write( key + '=>' + str(value) + ',')
       

f.close()
#printing movie_id and movie_title by popularity desc
#for i, film in enumerate(licenses):
    #print(i, film['id'], film['title'])
