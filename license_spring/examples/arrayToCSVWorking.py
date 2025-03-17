# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 11:37:10 2023

@author: crystal
This file works
"""

# Python program to demonstrate
# writing to CSV


import csv
	
# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']
	
# data rows of csv file this is an array of values
rows = [ ['Nikhil', 'COE', '2', '9.0'],
		['Sanchit', 'COE', '2', '9.1'],
		['Aditya', 'IT', '2', '9.3'],
		['Sagar', 'SE', '1', '9.5'],
		['Prateek', 'MCE', '3', '7.8'],
		['Sahil', 'EP', '2', '9.1']]
	
# name of csv file
filename = "university_records.csv"
	
# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)
		
	# writing the fields
	csvwriter.writerow(fields)
		
	#  writing the data rows
	csvwriter.writerows(rows)
