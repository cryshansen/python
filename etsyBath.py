#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 22:11:40 2021

@author: crystalhansen
"""
#categoryUrl={}
#'https://www.etsy.com/ca/c/bath-and-beauty/soaps?ref=catnav-891',
#'https://www.etsy.com/ca/c/bath-and-beauty/soaps?ref=pagination&page=2',
#'https://www.etsy.com/ca/c/bath-and-beauty/soaps?ref=pagination&page=3',
#'https://www.etsy.com/ca/c/bath-and-beauty/soaps?ref=pagination&page=4',
#'https://www.etsy.com/ca/c/bath-and-beauty/soaps?ref=pagination&page=5',
#'https://www.etsy.com/ca/c/bath-and-beauty/soaps?ref=pagination&page=6',
#'https://www.etsy.com/ca/c/bath-and-beauty/soaps?ref=pagination&page=7',
#'https://www.etsy.com/ca/c/bath-and-beauty/soaps?ref=pagination&page=8',
#'https://www.etsy.com/ca/c/bath-and-beauty/skin-care?ref=catnav-891',
#'https://www.etsy.com/ca/c/bath-and-beauty/skin-care/salves-and-balms?ref=catcard-303-275530152&explicit=1',
#'https://www.etsy.com/ca/c/bath-and-beauty/skin-care/moisturizers?ref=catcard-302-154931737&explicit=1',
#'https://www.etsy.com/ca/c/bath-and-beauty/skin-care/facial-care?ref=catcard-298-532045996&explicit=1',
#'https://www.etsy.com/ca/c/bath-and-beauty/essential-oils?ref=catnav-891',
#'https://www.etsy.com/ca/c/bath-and-beauty/makeup-and-cosmetics?ref=catnav-891',

#'https://www.etsy.com/ca/c/bath-and-beauty/makeup-and-cosmetics/eyes?ref=catcard-242-153944555&explicit=1',
#'https://www.etsy.com/ca/c/bath-and-beauty/makeup-and-cosmetics/lips?explicit=1&ref=catcard-255-124149286',
#'https://www.etsy.com/ca/c/bath-and-beauty/hair-care?ref=catnav-891'




#shopsUrl ={}
#'https://www.etsy.com/ca/shop/BeNUcrafts?ref=simple-shop-header-name&listing_id=942650159',
#'https://www.etsy.com/ca/shop/JouanBeauty?ref=simple-shop-header-name&listing_id=248835178',
#'https://www.etsy.com/ca/shop/MariaEcoline?ref=simple-shop-header-name&listing_id=259041741',
#'https://www.etsy.com/ca/shop/AnnBoyar?ref=simple-shop-header-name&listing_id=490407667',
#'https://www.etsy.com/ca/shop/SavonsCaouane?ref=simple-shop-header-name&listing_id=465121730',
#'https://www.etsy.com/ca/shop/PebbermintCo?ref=simple-shop-header-name&listing_id=691772711',
#'https://www.etsy.com/ca/shop/Camiella?ref=simple-shop-header-name&listing_id=478470887',
#'https://www.etsy.com/ca/shop/RoseCitronCosmetics?ref=simple-shop-header-name&listing_id=274517524',
#'https://www.etsy.com/ca/shop/Naturestestimony?ref=simple-shop-header-name&listing_id=233921108',
#'https://www.etsy.com/ca/shop/BeauteCrepue?ref=simple-shop-header-name&listing_id=244052359',
#'https://www.etsy.com/ca/shop/LolaJaneNaturals?ref=simple-shop-header-name&listing_id=599305535',
#'https://www.etsy.com/ca/shop/BeNUcrafts?ref=simple-shop-header-name&listing_id=942650159'
#


lushUrl4="https://www.etsy.com/ca/shop/shopamongtheflowers?ref=simple-shop-header-name&listing_id=613066669"
response4= requests.get(lushUrl4)
lushSoup4 = BeautifulSoup(response4.text,'lxml')

fileName = "products/shopamongtheflowers_homePage_" + d + ".txt"
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
