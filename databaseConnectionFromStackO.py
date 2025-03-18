#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 08:53:45 2020

@author: crystalhansen
"""

#!/usr/bin/python


import MySQLdb
import random
import requests
import time


db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="*********",  # your password
                     db="db-local")       # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# The first line is defined for specified vendor
mac = [ 0x00, 0x24, 0x81,
    random.randint(0x00, 0x7f),
    random.randint(0x00, 0xff),
    random.randint(0x00, 0xff) ]

device_mac =  ':'.join(map(lambda x: "%02x" % x, mac))
cpe_mac = '000D6766F2F6'

url = "https://randomuser.me/api/"
data = requests.get(url).json()
firstname = data['results'][0]['user']['name']['first']
lastname = data['results'][0]['user']['name']['last']
email = data['results'][0]['user']['email']
gender = data['results'][0]['user']['gender']

age_range_options = [">15", "15-25", "25-40","40+"]
age_range = random.choice(age_range_options)

ip = '10.10.10.10'
host_name = 'cron.job'
visit_count = 1
created_at = time.strftime('%Y-%m-%d %H:%M:%S')
updated_at = time.strftime('%Y-%m-%d %H:%M:%S')

sql = ('''INSERT INTO visitors (device_mac,cpe_mac,firstname, lastname, email, gender, age_range,ip,host_name,visit_count,created_at, updated_at) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''')

args = (device_mac,cpe_mac, firstname, lastname, email, gender, age_range,ip, host_name,visit_count, created_at, updated_at)
cur.execute(sql,args)
db.commit()


# for record in records:
# print records

db.close()