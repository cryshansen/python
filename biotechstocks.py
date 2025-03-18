#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 10:59:13 2021

@author: crystalhansen
"""



import bs4 as bs  #beautifulSoup
import urllib.request
from datetime import datetime, timedelta




dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")

#stocks in biotech
urlStock = "https://fknol.com/ca/stock/biotechnology.php"

response= requests.get(urlStock)
stockSoup = BeautifulSoup(response.text,'lxml')


fileName = "stocks/biotech_"+ d +".txt"
f=open(fileName,"w")

for product in stockSoup.find_all( 'table', class_="w3-table w3-striped w3-bordered w3-pale-red"):
    #print(product)
    print("product")
    for tr in product.find_all('tr'):
        
        f.write(";")
        for td in tr.find_all('td'):
            print(td.text.strip() +" ,")
            f.write(td.text.strip() +" ,")
            for href in td.find_all('a', href=True):
                print(href['href'])
                f.write(href['href'] +" ,")
                name = href['href'].split("/")
                
                lenth = len(name)
                
                print(name[lenth-1])
                symbol = name[lenth-1].split(".php")
                print(symbol)
                stockFile = "stocks/individuals/biotech_"+ symbol[0]+ "_" + d +".txt"
                response2 = requests.get(href['href'])
                stockElSoup = BeautifulSoup(response2.text, 'lxml')
                f3=open(stockFile,"w")
                f3.write(symbol[0])
                for product in stockElSoup.find_all('article' , class_='w3-twothird w3-container'):
                    #print(product.text.strip())
                    for table in product.find_all('table', class_="w3-table-twothird w3-striped w3-bordered w3-grey"):
                        print("table")
                        for tr in table.find_all("tr"):
                            print(";")
                            f3.write(";")
                            for td in tr.find_all('td'):
                                print(td)
                                f3.write(td.text.strip() +" ,")
                f3.close()

urlStock="https://fknol.com/ca/stock/biotechnology.php?go=b25"

response= requests.get(urlStock)
stockSoup = BeautifulSoup(response.text,'lxml')


for product in stockSoup.find_all( 'table', class_="w3-table w3-striped w3-bordered w3-pale-red"):
    #print(product)
    #print("product")
    for tr in product.find_all('tr'):
        f.write(";")
        for td in tr.find_all('td'):
            #print(td.text.strip() +",")
            f.write(td.text.strip() +" ,")
            for href in td.find_all('a', href=True):
                print(href['href'])
                f.write(href['href'] +" ,")
                name = href['href'].split("/")
                #['https:', '', 'fknol.com', 'ca', 'stock', 'cot.php']
                lenth = len(name)
                
                print(name[lenth-1])
                symbol = name[lenth-1].split(".php")
                print(symbol)
                stockFile = "stocks/individuals/biotech_"+ symbol[0]+ "_" + d +".txt"
                response2 = requests.get(href['href'])
                stockElSoup = BeautifulSoup(response2.text, 'lxml')
                f3=open(stockFile,"w")
                f3.write(symbol[0])
                for product in stockElSoup.find_all('article' , class_='w3-twothird w3-container'):
                    #print(product.text.strip())
                    for table in product.find_all('table', class_="w3-table-twothird w3-striped w3-bordered w3-grey"):
                        print("table")
                        for tr in table.find_all("tr"):
                            print(";")
                            f3.write(";")
                            for td in tr.find_all('td'):
                                print(td)
                                f3.write(td.text.strip() +" ,")
                f3.close()
f.close()





#
#fileName2 = "stocks/stocklist_"+ d +".txt"        
#f2=open(fileName2,"w")
#for article in stockSoup.find_all('article',class_="w3-container"):
#    
#    for p in article.find_all('p', class_="w3-container"):
#        print (p.text.strip())
#        f2.write(p.text.strip() +"\n\n")
#        f2.write("Category: " + p.text.strip() + "\n\n")
#        for href in p.find_all('a'):
#            f2.write( href['href'] + "\n")
#            print(href['href'])
#            f2.write("link: " + href.text.strip() )
#            print(href.text.strip())
#            
#f2.close()