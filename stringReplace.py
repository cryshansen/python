#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:54:54 2020

@author: crystalhansen
"""

## string replace python script

 
# Function to replace multiple occurrences   
# of a character by a single character 
def replace(string, char): 
    pattern = char + '{4,}'
    string = re.sub(pattern, char, string) 
    return string 
# call function
 #char = " "  ##a white space
 #replaceString = replace(stringToReplace, char)