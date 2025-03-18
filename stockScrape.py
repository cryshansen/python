#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 10:33:22 2020

@author: crystalhansen
"""

import bs4 as bs  #beautifulSoup
import urllib.request
from datetime import datetime, timedelta




dt = datetime.now() #+ timedelta(hours=1) #sadds an hour for a condition of time is less than one hour ahead
d = dt.strftime("%m-%d-%Y_%H-%M-%S")


#https://simplywall.st/stocks/ca/banks/tsx-cwb/canadian-western-bank-shares?blueprint=1376355&utm_medium=finance_user&utm_campaign=conclusion&utm_source=post#executive-summary
stockhtml = urllib.request.urlopen('https://ca.finance.yahoo.com/quote/cwb.to/')
stockSoup = bs.BeautifulSoup(stockhtml,'lxml')

print(stockSoup.title.string)


fileN= "stocks/stock_CWB_" + d +".txt"
f = open(fileN,"w") #open file with name test.txt
f.write(stockSoup.title.string +"\n ")    
for a2 in stockSoup.find_all('div',class_='YDC-Lead'):
    print(a2.text.strip() + "; \n")
    f.write(a2.text.strip()+";  \n")
    
for a3 in stockSoup.find('div', class_='quote-summary-section'):
    print(a3.text.strip() + "; \n")
    f.write(a3.text.strip()+";  \n")
    
f.close()

# try globe and mail. 
#https://www.theglobeandmail.com/investing/markets/stocks/CWB-T/

# Health
# Bausch Health (TSX:BHC)(NYSE:BHC).

#gas convenience stocks
#Alimentation Couche-Tard (TSX:ATD.B)
stockhtml = urllib.request.urlopen('https://ca.finance.yahoo.com/quote/ATD.BE?p=ATD.BE')
stockSoup = bs.BeautifulSoup(stockhtml,'lxml')
print(stockSoup.title.string)


fileN= "stocks/stock_TRIL_" + d +".txt"
f = open(fileN,"w") #open file with name test.txt
f.write(stockSoup.title.string +"\n ")    
for a2 in stockSoup.find_all('div',class_='YDC-Lead'):
    print(a2.text.strip() + "; \n")
    f.write(a2.text.strip()+";  \n")
    
for a3 in stockSoup.find('div', class_='quote-summary-section'):
    print(a3.text.strip() + "; \n")
    f.write(a3.text.strip()+";  \n")
    
f.close()



#online shopping
#Cargojet (TSX:CJT) 
#partnership with DHL express and amazon has a share in it
stockhtml=urllib.request.urlopen('https://ca.finance.yahoo.com/quote/CJT.TO?p=CJT.TO')
stockSoup = bs.BeautifulSoup(stockhtml,'lxml')

print(stockSoup.title.string)


fileN= "stocks/stock_TRIL_" + d +".txt"
f = open(fileN,"w") #open file with name test.txt
f.write(stockSoup.title.string +"\n ")    
for a2 in stockSoup.find_all('div',class_='YDC-Lead'):
    print(a2.text.strip() + "; \n")
    f.write(a2.text.strip()+";  \n")
    
for a3 in stockSoup.find('div', class_='quote-summary-section'):
    print(a3.text.strip() + "; \n")
    f.write(a3.text.strip()+";  \n")
    
f.close()

stockhtml =urllib.request.urlopen('https://ca.finance.yahoo.com/quote/CJT.TO/history?period1=1329091200&period2=1609545600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true')
stockSoup=bs.BeautifulSoup(stockhtml,'lxml')
#download the file of historical data
print(stockSoup.title.string)

fileN= "stocks/stock_TRIL_Historical" + d +".txt"
f = open(fileN,"w") #open file with name test.txt
f.write(stockSoup.title.string +"\n ")    
for div2 in stockSoup.find_all('div',class_="Pb(10px) Ovx(a) W(100%)"):
    
    print(div2.text.strip() + "; \n")
    f.write(div2.text.strip()+";  \n")
    
        
#for a3 in stockSoup.find('div', class_='quote-summary-section'):
#    print(a3.text.strip() + "; \n")
#    f.write(a3.text.strip()+";  \n")
    
f.close()





#quote-header-info
stockhtml= urllib.request.urlopen('https://ca.finance.yahoo.com/quote/TRIL.TO?p=TRIL.TO')
stockSoup = bs.BeautifulSoup(stockhtml,'lxml')

print(stockSoup.title.string)


fileN= "stocks/stock_TRIL_" + d +".txt"
f = open(fileN,"w") #open file with name test.txt
f.write(stockSoup.title.string +"\n ")    
for a2 in stockSoup.find_all('div',class_='YDC-Lead'):
    print(a2.text.strip() + "; \n")
    f.write(a2.text.strip()+";  \n")
    
for a3 in stockSoup.find('div', class_='quote-summary-section'):
    print(a3.text.strip() + "; \n")
    f.write(a3.text.strip()+";  \n")
    
f.close()
