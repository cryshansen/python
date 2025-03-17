# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:50:40 2022
Read a directory and output to a csv file.

@author: crystal
"""
import pandas as pd
from pathlib import Path

filename = "";
for child in Path('.').iterdir():
    if child.is_file():
        if child.suffix == '.txt':
            #print(f"{child.name}:\n")
            #"\"news_item\" , \""+ c.extract() + "\"\r\n"
            filename = child.name;
            name = Path(filename).stem
            fileto_save = name+"csv"
            print(fileto_save)
            print( child.read_text())
            read_file = child.read_text()
            #read_file.to_csv ( fileto_save, index=None)