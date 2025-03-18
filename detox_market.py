#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:53:26 2021

@author: crystalhansen
"""
#https://www.thedetoxmarket.ca/collections/best-sellers
#
url = "https://www.thedetoxmarket.ca/collections/best-sellers"


response = requests.get(url)
Soup = BeautifulSoup(response.text,'lxml')
print(Soup.title.text)
 
 
fileName = "detox_market/products_" + d + ".txt"
f=open(fileName,"w")
for productCat in Soup.find_all( 'div', class_='row no-gutters'):
    print(productCat.text)
    f.write(productCat.text)
    #for product in Soup.find_all( 'div', class_='product product-collection'):
        #print(product)
    for title in Soup.find_all('div',class_='title'):
        print(title.text)
        for href in title.find_all('a', href=True):
            link = href['href']
            print(link)
            prodLink ="https://www.thedetoxmarket.ca"+ link
            
            prodResponse= requests.get(prodLink)
            SoupProducts = BeautifulSoup(prodResponse.text,'lxml')
        
            print(SoupProducts.title.text)
            titleReplace = SoupProducts.title.text
            titleReplace = titleReplace.replace("/", " ")
            fileName2 = "detox_market/products/" + titleReplace + "_"+d + ".txt"
            f2=open(fileName2,"w")
            f2.write(titleReplace + "\n")
            f2.write(link +"\n")
            #get top information section single item page elements
            for item in SoupProducts.find_all('div', class_="col-lg-4"): ##cart-col
                print(item.text.strip())
                f2.write(item.text.strip())
            for itemDetails in SoupProducts.find_all('div',class_="col-lg-5 px-lg-3 px-2"):
                print(itemDetails.text.strip()+ "\n")
                f2.write(itemDetails.text.strip())
            
            
            f2.close()
f.close()
            
#https://www.thedetoxmarket.ca/collections/best-sellers?page=2

url = "https://www.thedetoxmarket.ca/collections/best-sellers?page=2"


response = requests.get(url)
Soup = BeautifulSoup(response.text,'lxml')
print(Soup.title.text)
 
 
fileName = "detox_market/products_" + d + ".txt"
#f=open(fileName,"w")
for productCat in Soup.find_all( 'div', class_='row no-gutters'):
    print(productCat.text)
    #for product in Soup.find_all( 'div', class_='product product-collection'):
        #print(product)
    for title in Soup.find_all('div',class_='title'):
        print(title.text)
        for href in title.find_all('a', href=True):
            link = href['href']
            print(link)
            prodLink ="https://www.thedetoxmarket.ca"+ link
            
            prodResponse= requests.get(prodLink)
            SoupProducts = BeautifulSoup(prodResponse.text,'lxml')
        
            print(SoupProducts.title.text)
            titleReplace = SoupProducts.title.text
            titleReplace = titleReplace.replace("/", " ")
            fileName2 = "detox_market/products/" + titleReplace + "_"+d + ".txt"
            f2=open(fileName2,"w")
            f2.write(titleReplace + "\n")
            f2.write(link +"\n")
            #get top information section single item page elements
            for item in SoupProducts.find_all('div', class_="col-lg-4"): ##cart-col
                print(item.text.strip())
                f2.write(item.text.strip())
            for itemDetails in SoupProducts.find_all('div',class_="col-lg-5 px-lg-3 px-2"):
                print(itemDetails.text.strip()+ "\n")
                f2.write(itemDetails.text.strip())
            
            
            f2.close()            