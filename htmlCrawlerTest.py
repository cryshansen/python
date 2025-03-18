#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:20:28 2021

@author: crystalhansen
"""

import bs4 as bs  #beautifulSoup
#import urllib.request
import requests
import numpy as np
from datetime import datetime, timedelta


dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")



def get_random_ua():
    print('in call')
    random_ua = ''
    ua_file = 'ua_file.txt'   
    try:
        with open(ua_file) as f:
            lines = f.readlines()
        if len(lines) > 0:
            prng = np.random.RandomState()
            index = prng.permutation(len(lines) - 1)
            idx = np.asarray(index, dtype=np.integer)[0]
            random_ua = lines[int(idx)]
            
            
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    finally:
        return random_ua


user_agent = get_random_ua()
#remove the "\n" from end of file line
ua = user_agent.replace("\n", " ")
print(user_agent)


headers = {
        'user-agent': ua,
    }
#
#delays = [7, 4, 6, 2, 10, 19]
#delay = np.random.choice(delays)
##time.sleep(delay)
#
#
## Our most popular products based on sales. Updated hourly 
### best sellers
##best sellers in beauty 
##beautyhtml= urllib.request.urlopen('https://www.amazon.ca/Best-Sellers-Beauty/zgbs/beauty/ref=zg_bs_nav_0')
##beautySoup = bs.BeautifulSoup(beautyhtml,'lxml')
### testing amazon blockers
r = requests.get('https://www.amazon.ca/Best-Sellers-Beauty/zgbs/beauty/ref=zg_bs_nav_0',headers=headers)
beautySoup = bs.BeautifulSoup(r,'lxml')
print(beautySoup)
#
#
#
#
#fileN= "beauty/beautyPersonalCare/beautyAmazon_test" + d +".txt"
#f=open(fileN,"w")
#f.write(beautySoup.title.string +"\n ")
#for li in beautySoup.find_all('li', class_='zg-item-immersion'):
#    #print(li.text.strip()+", ")
#    f.write(li.text.strip()+";  \n")
#f.close()