#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 18:34:31 2018
@author: Pradhan Prakash
Snippet for LTV Calculation for Top Customers
"""

import math as m
from datetime import datetime, timedelta

def topXSimpleLTVCustomers(x,D):
    cust_ltv={} #Dictionary to hold Customer ID and corresponding LTV
    t=10 #This is for Shutterfly avg life span
    ltv=0
    
    for key in D.keys():
        no_of_visit=0
        total_amount=0
        order=D[key].get('ORDER',None)
        if order is not None:
            for o in order:
                total_amount=total_amount+float(o.total_amount.split(' ')[0].strip()) 
                #Total Revenue by customer stripping out USD string
	
		#total number of visits
		
        visit=D[key].get('SITE_VISIT',None)
        if visit is not None:
            no_of_visit=len(visit) #Total number of weeks
        curr=D[key].get('CUSTOMER')[0].event_time
        curr = datetime.strptime(curr, '%Y-%m-%dT%H:%M:%S.%fZ').date()
        first_week =curr - timedelta(days=curr.weekday())
        #Assuming the given least date is starting of the week 
        this_week=datetime.now().date()-timedelta(days=datetime.now().date().weekday())
        
        total_weeks=m.ceil(abs((first_week-this_week).days)/7)
        
		#calculating the avaerage part 'a'
        if no_of_visit>0: #checking this inorder to avoid divide by zero error caused by no_of_visit
            avg_cust_amount=total_amount/no_of_visit
            site_visit_per_week=no_of_visit/total_weeks
            ltv=avg_cust_amount*site_visit_per_week*52*t
        else:
            ltv=0
		
        cust_ltv[key]=ltv
	
	#sorting the dictionary in Descending order and printing the top X customers
    resultltv=[]
    if x>len(D):
        print("More number of Customers than expected, so showing all of them")
        x=len(D)
    for i in  sorted(cust_ltv,key=cust_ltv.get,reverse=True):
        resultltv.append((i,cust_ltv.get(i)))
    
    # Print and Return the result
    data_str = "Customer ID                 Life Time Value\n"

    for k in range(0,x):
        data_str += "%s"%(resultltv[k][0]) + "                " + "%s\n"%(resultltv[k][1])
        
    print(data_str)
    return data_str
        
        
    
    
		
				
	