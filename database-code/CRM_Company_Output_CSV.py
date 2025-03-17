# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:51:42 2023

@author: crystal
"""
import file
import MySQLdb
import csv

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="crm")        # name of the data base

cur = db.cursor()
#C:\Users\crystal\hubspot-git\hubspot\emtp_database
csv_data = csv.reader(file('..\crm\db_columns.csv'))

for row in csv_data:

   # cur.execute ("INSERT INTO part_table_test (ID,SCHOOL_CODE,DISTNAME,AC_YEAR,SCHOOL_NAME,STATE_NAME,BLOCK_NAME,CLUSTER_NAME,VILLAGE_NAME,PINCODE,RURURB,ELECTRIC_YN,SCHMGT,LOWCLASS,HIGHCLASS,COMPUTER,CAL_YN,MEDINSTR1,MEDINSTR2,MEDINSTR3,MEDINSTR4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",row)
   print(row)
db.close()