#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 09:56:52 2021

@author: crystalhansen
"""




import bs4 as bs  #beautifulSoup
import urllib.request
from datetime import datetime, timedelta

dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")

print('dailyBestSellers')

lushUrl="https://www.lush.ca/en/face/face/"


response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/face/products/daily_bestSellers_"+ d +".txt"
f=open(fileName,"w")
for product in lushSoup.find_all( 'div', class_="product"):
    #print(product.text.strip())
    f.write(product.text.strip() + "\n")
    for href in product.find_all('a', class_="link",href=True):
        #print(href['href']) 
        link = href['href']
        f.write(link +"\n")
    
f.close()

lushUrl="https://www.lush.ca/en/hair/hair/"

#has best sellers
#section-swiper
#swiper-container
#swiper-wrapper
#product-tiles  swiper-slide swiper
#product
# this has all the individual top level information get the link to get the ingredients

response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/hair/products/daily_hair_bestSellers_"+ d +".txt"
f=open(fileName,"w")
for product in lushSoup.find_all( 'div', class_="product"):
    #print(product.text.strip())
    f.write(product.text.strip() + "\n")
    for href in product.find_all('a', class_="link",href=True):
        #print(href['href']) 
        link = href['href']
        f.write(link +"\n")
f.close()


lushUrl="https://www.lush.ca/en/body/body/"
#has best sellers
#section-swiper
#swiper-container
#swiper-wrapper
#product-tiles  swiper-slide swiper
#product
# this has all the individual top level information get the link to get the ingredients

response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/body/products/daily_body_bestSellers_"+ d +".txt"
f=open(fileName,"w")
for product in lushSoup.find_all( 'div', class_="product"):
    #print(product.text.strip())
    f.write(product.text.strip() + "\n")
    
    for href in product.find_all('a', class_="link",href=True):
        #print(href['href']) 
        link = href['href']
        f.write(link +"\n")
f.close()

lushUrl="https://www.lush.ca/en/discover/bestsellers/?cgid=bestsellers&start=0&sz=42"
#all best sellers
#list of items 


response= requests.get(lushUrl)
lushSoup = BeautifulSoup(response.text,'lxml')
fileName = "lush/allBestSellers/daily_allBestSellers_"+ d +".txt"
f=open(fileName,"w")
for product in lushSoup.find_all( 'div', class_="product"):
    #print(product.text.strip())
    f.write(product.text.strip() + "\n")
    for href in product.find_all('a', class_="link",href=True):
        #print(href['href']) 
        link = href['href']
        f.write(link +"\n")
f.close()

