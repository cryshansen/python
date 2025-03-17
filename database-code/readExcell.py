# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 15:04:40 2023

@author: crystal
"""

# Import pandas
import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="emtp",         # your username
                     passwd="sqlemtp/1526VanK",  # your password
                     db="crm")        # name of the data base
cur = db.cursor()

insert_query = "Insert into contact () Values "

# reading csv file 
#pd.read_csv("Contact.csv")

#xl = pd.ExcelFile("crm\Contact.xlsx")
#xl.sheet_names[u'A']
#df = xl.parse("A")
#df.head()



#df = pd.read_excel("crm\Contact.xlsx", sheet_name=0) #corrected argument name


df =pd.read_excel(open('crm\Contact2.xlsx', 'rb'), sheet_name='A')  

for sh in range(0,len(df)):
    sheet= df.sheet_by_index(sh)
    
    for r in range(1,sheet.nrows):
        product_id = sheet.cell(r,0).value

        product_name = sheet.cell(r,1).value

        product_price = sheet.cell(r,2).value
     
        product_rating = sheet.cell(r,3).value
      
        product_star_rating = sheet.cell(r,4).value
        
        product_url = sheet.cell(r,5).value
        
        product_details_value = (product_id,product_name,product_price,product_rating,product_star_rating,product_url)
        
        
        cursor.execute(insert_query,product_details_value)
        database.commit()
