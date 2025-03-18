#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:15:17 2020

@author: crystalhansen
"""
from lxml import html
import requests
import re 
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")


###seems must simulate the search feature for side navigation to work    
## Home : Home Décor : Candles & Holders : Candles : "candles"
#candleURL="https://www.amazon.ca/b/ref=amb_link_42?ie=UTF8&node=2224030011&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_s=merchandised-search-leftnav&pf_rd_r=7EBA7V948PJNC0HJSKQW&pf_rd_r=7EBA7V948PJNC0HJSKQW&pf_rd_t=101&pf_rd_p=0ec90a34-e8ee-471d-b36c-2504eaa0445c&pf_rd_p=0ec90a34-e8ee-471d-b36c-2504eaa0445c&pf_rd_i=2206275011"
#candles="https://www.amazon.ca/b?node=6647042011&ref=sr_nr_n_4"
#"https://www.amazon.ca/s?k=candles&rh=n%3A6647042011&dc&qid=1603461152&rnid=5264023011&ref=sr_nr_n_1"    
#hit captcha on dealsSample for human interaction. Message about using web services

#widgetContent
#shop all deals 
url = "https://www.amazon.ca/s?k=Candles+%26+Holders"


response = requests.get(url)
soup = BeautifulSoup(response.text)
print (soup)

fileN= "allDeals/CandlesAmazon_" + d +".txt"

#f=open(fileN,"w")
#f.write(soup.title.string +"\n")
for container in soup.find_all('div',class_='a-section'):
    print(container.text.strip()+"; \n")
    #for div in container.find_all('div', class_='a-row dealContainer dealTile'):
       # print(div.text.strip()+"; \n")
    
 #   f.write(li.text.strip() + "; \n")
#f.close()
