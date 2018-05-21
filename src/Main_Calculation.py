#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 18:10:51 2018
@author: Pradhan Prakash
Snippet for Main Method
"""

from collections import defaultdict
from LTVClass import Customer,Site_Visit,Image_Upload,Order
import calculation 
import ingestion

import sys
import os
import json
#command line arguments
#First argument provides X customers
#Second argument provides file name
if len(sys.argv)!=3:
	print ("Provide Customers and File Name as 2 Parameters")
	exit(1)
file=sys.argv[2]
x=int(sys.argv[1])

#Dicionary to store each customer information
D={}

if x<0:
	print ("Enter a Positive Number as Customer Count")
	exit(1)

#parsing the JSON file 
try:
    cur_dir = os.path.split(os.getcwd())[0]
    in_dir = os.path.join(cur_dir, 'in')
    file_path = os.path.join(in_dir, file)
    
    with open(file_path,"r") as fh:
        e=json.load(fh)
        
except:
    print("Unable to open the File")
    exit(1)

#calling the Ingestion method in ingestion snippet 
D=ingestion.Ingest(e,D)
#calling Top X Analytical Method in calculation snippet
data_result = calculation.topXSimpleLTVCustomers(x,D)

out_dir = os.path.join(cur_dir, 'out')
file_path = os.path.join(out_dir, "output_result.txt")

with open(file_path,"w") as fh:
        fh.write(data_result)
        
print ("Execution completed!!")        