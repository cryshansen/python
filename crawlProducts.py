#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:18:22 2021

@author: crystalhansen
"""

import bs4 as bs  #beautifulSoup
#import urllib.request
import requests
import numpy as np
from datetime import datetime, timedelta


dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")

##Etsy use

lushUrl="https://www.etsy.com/ca/shop/TaigaBees?ref=simple-shop-header-name&listing_id=288955151"
response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')

fileName = "products/TaigaBees_homePage_"+ d +".txt"
f=open(fileName,"w")
for product in lushSoup.find_all( 'div', class_="js-merch-stash-check-listing"):
     print(product.text.strip())
     f.write(product.text.strip() + "\n")
     for href in product.find_all('a', class_="listing-link",href=True):
        #print(href['href']) 
        link = href['href']
        
        lushItemURL = link
        #print(lushItemURL)
        
        #follow Link
        itemResponse= requests.get(lushItemURL)
        lushSoupItem = BeautifulSoup(itemResponse.text,'lxml')
        
        print(lushSoupItem.title.string)
        titleReplace = lushSoupItem.title.string
        titleReplace = titleReplace.replace("/", " ")
        
        fileName2= "products/" + titleReplace + "_"+d + ".txt"
        
        f2=open(fileName2,"w")
        f2.write(lushItemURL + "\n")
        f2.write(link +"\n")
        #get top information section single item page elements
        for item in lushSoupItem.find_all('div', class_="listing-page-cart"): ##cart-col
            print(item.text.strip())
            f2.write(item.text.strip())
        #get item details of single page elements    
        for itemDetails in lushSoupItem.find_all('div',class_="listing-info"):
            print(itemDetails.text.strip()) 
            f2.write(itemDetails.text.strip())
        f2.close()
        
        
f.close()

lushUrl2="https://www.etsy.com/ca/shop/LolaJaneNaturals?ref=simple-shop-header-name&listing_id=599305535"
response2= requests.get(lushUrl2)
lushSoup2 = BeautifulSoup(response2.text,'lxml')

fileName = "products/LolaJaneNaturals_homePage_"+ d +".txt"
f=open(fileName,"w")
for product in lushSoup2.find_all( 'div', class_="js-merch-stash-check-listing"):
     print(product.text.strip())
     f.write(product.text.strip() + "\n")
     for href in product.find_all('a', class_="listing-link",href=True):
        #print(href['href']) 
        link = href['href']
        
        lushItemURL = link
        #print(lushItemURL)
        
        #follow Link
        itemResponse= requests.get(lushItemURL)
        lushSoupItem = BeautifulSoup(itemResponse.text,'lxml')
        
        print(lushSoupItem.title.string)
        titleReplace = lushSoupItem.title.string
        titleReplace = titleReplace.replace("/", " ")
        
        fileName2= "products/LolaJaneNaturals_" + titleReplace + "_"+d + ".txt"
        
        f2=open(fileName2,"w")
        f2.write(lushItemURL + "\n")
        f2.write(link +"\n")
        #get top information section single item page elements
        for item in lushSoupItem.find_all('div', class_="listing-page-cart"): ##cart-col
            print(item.text.strip())
            f2.write(item.text.strip())
        #get item details of single page elements    
        for itemDetails in lushSoupItem.find_all('div',class_="listing-info"):
            print(itemDetails.text.strip()) 
            f2.write(itemDetails.text.strip())
        f2.close()
        
        
f.close()



lushUrl3="https://www.etsy.com/ca/shop/ElegantRoseBoutique?ref=simple-shop-header-name&listing_id=84919440"
response3= requests.get(lushUrl3)
lushSoup3 = BeautifulSoup(response3.text,'lxml')

fileName = "products/ElegantRoseBoutique_homePage_"+ d +".txt"
f=open(fileName,"w")
for product in lushSoup3.find_all( 'div', class_="js-merch-stash-check-listing"):
     print(product.text.strip())
     f.write(product.text.strip() + "\n")
     for href in product.find_all('a', class_="listing-link",href=True):
        #print(href['href']) 
        link = href['href']
        
        lushItemURL = link
        #print(lushItemURL)
        
        #follow Link
        itemResponse= requests.get(lushItemURL)
        lushSoupItem = BeautifulSoup(itemResponse.text,'lxml')
        
        print(lushSoupItem.title.string)
        titleReplace = lushSoupItem.title.string
        titleReplace = titleReplace.replace("/", " ")
        
        fileName2= "products/ElegantRoseBoutique_" + titleReplace + "_"+d + ".txt"
        
        f2=open(fileName2,"w")
        f2.write(lushItemURL + "\n")
        f2.write(link +"\n")
        #get top information section single item page elements
        for item in lushSoupItem.find_all('div', class_="listing-page-cart"): ##cart-col
            print(item.text.strip())
            f2.write(item.text.strip())
        #get item details of single page elements    
        for itemDetails in lushSoupItem.find_all('div',class_="listing-info"):
            print(itemDetails.text.strip()) 
            f2.write(itemDetails.text.strip())
        f2.close()
        
        
f.close()

##https://www.etsy.com/ca/shop/shopamongtheflowers?ref=simple-shop-header-name&listing_id=613066669

lushUrl4="https://www.etsy.com/ca/shop/shopamongtheflowers?ref=simple-shop-header-name&listing_id=613066669"
response4= requests.get(lushUrl4)
lushSoup4 = BeautifulSoup(response4.text,'lxml')

fileName = "products/shopamongtheflowers_homePage_"+ d +".txt"
f=open(fileName,"w")
for product in lushSoup4.find_all( 'div', class_="js-merch-stash-check-listing"):
     print(product.text.strip())
     f.write(product.text.strip() + "\n")
     for href in product.find_all('a', class_="listing-link",href=True):
        #print(href['href']) 
        link = href['href']
        
        lushItemURL = link
        #print(lushItemURL)
        
        #follow Link
        itemResponse= requests.get(lushItemURL)
        lushSoupItem = BeautifulSoup(itemResponse.text,'lxml')
        
        print(lushSoupItem.title.string)
        titleReplace = lushSoupItem.title.string
        titleReplace = titleReplace.replace("/", " ")
        
        fileName2= "products/shopamongtheflowers_" + titleReplace + "_"+d + ".txt"
        
        f2=open(fileName2,"w")
        f2.write(lushItemURL + "\n")
        f2.write(link +"\n")
        #get top information section single item page elements
        for item in lushSoupItem.find_all('div', class_="listing-page-cart"): ##cart-col
            print(item.text.strip())
            f2.write(item.text.strip())
        #get item details of single page elements    
        for itemDetails in lushSoupItem.find_all('div',class_="listing-info"):
            print(itemDetails.text.strip()) 
            f2.write(itemDetails.text.strip())
        f2.close()
        
        
f.close()
