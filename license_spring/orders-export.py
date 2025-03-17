# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:08:34 2023

@author: crystal
@description this is the working copy of licenses and files  
"""

import requests #to make TMDB API calls



API_URL = 'https://saas.licensespring.com'

# Can be found in `Settings` -> `Settings` -> `Keys`
API_KEY = '12Xxxx.xxxxx'


#Discover API url filtered to movies >= 2004 and containing Drama genre_ID: 18
#discover_api = 'https://api.themoviedb.org/3/discover/movie? 
#api_key=['my api key']&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&primary_release_year=>%3D2004&with_genres=18'

orders_api = requests.get(
    #url='{}{}'.format(API_URL, '/api/v1/orders/generate_license/'),
    url='{}{}'.format(API_URL, '/api/v1/orders/'),
    #params={'range':'last30'},
    params={'limit':100,'offset':101},
    headers={
        'Authorization': 'Api-Key {}'.format(API_KEY)
    }
).json()

print(orders_api)