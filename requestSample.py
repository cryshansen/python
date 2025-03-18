#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:45:29 2020

@author: crystalhansen
"""
from lxml import html
import requests
import re 
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

 
dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")
print('request Sample Amazon')
 
###seems must simulate the search feature for side navigation to work    
## Home : Home Décor : Candles & Holders : Candles : "candles"
#candleURL="https://www.amazon.ca/b/ref=amb_link_42?ie=UTF8&node=2224030011&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_s=merchandised-search-leftnav&pf_rd_r=7EBA7V948PJNC0HJSKQW&pf_rd_r=7EBA7V948PJNC0HJSKQW&pf_rd_t=101&pf_rd_p=0ec90a34-e8ee-471d-b36c-2504eaa0445c&pf_rd_p=0ec90a34-e8ee-471d-b36c-2504eaa0445c&pf_rd_i=2206275011"
#candles="https://www.amazon.ca/b?node=6647042011&ref=sr_nr_n_4"
#"https://www.amazon.ca/s?k=candles&rh=n%3A6647042011&dc&qid=1603461152&rnid=5264023011&ref=sr_nr_n_1"    

HandmadeHomeKitchen = "https://www.amazon.ca/Best-Sellers-Handmade-Home-Kitchen-Products/zgbs/handmade/16910099011/ref=zg_bs_nav_hnd_1_hnd"

mostGiftedBeauty = "https://www.amazon.ca/gp/most-gifted/beauty"
mostGiftedCandles = "https://www.amazon.ca/gp/most-gifted/kitchen/6647042011/"

response = requests.get(mostGiftedBeauty)
soup = BeautifulSoup(response.text)
#print (soup)
fileN= "mostgifted/MostGiftedBeautyAmazon_" + d +".txt"

f=open(fileN,"w")
f.write(soup.title.string +"\n")

for li in soup.find_all('li', class_='zg-item-immersion'):
   
  
    #char = " "
    #replaceString = replace(li.text.strip(), char)
    #print(li.text.strip()+"; \n")
    
    f.write(li.text.strip() + "; \n")
f.close()


response = requests.get(mostGiftedCandles)
soup = BeautifulSoup(response.text)
#print (soup)
fileN= "mostgifted/MostGiftedCandlesAmazon_" + d +".txt"
#fileN= "HandmadeHomeKitchenProductsAmazon_" + d +".txt"
f=open(fileN,"w")
f.write(soup.title.string +"\n")

#for div in soup.find_all('div', class_='s-main-slot s-result-list s-search-results sg-row'):
for li in soup.find_all('li', class_='zg-item-immersion'):
    #print(li.text.strip()+"; \n")
    f.write(li.text.strip() + "; \n")
f.close()   


#HandmadeHomeKitchenProducts

response = requests.get(HandmadeHomeKitchen)
soup = BeautifulSoup(response.text)


fileN= "mostgifted/HandmadeHomeKitchenProductsAmazon_" + d +".txt"
f=open(fileN,"w")
f.write(soup.title.string +"\n")

for li in soup.find_all('li', class_='zg-item-immersion'):
   
    
    f.write(li.text.strip() + "; \n")
f.close()


fileN= "mostgifted/TestPageForDealsInfo_" + d +".txt"
f=open(fileN,"w")
f.write(soup.title.string +"\n")
#f.write(soup.string)
f.close()
