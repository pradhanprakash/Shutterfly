#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 18:18:37 2018
@author: Pradhan Prakash
Snippet for Ingestion
"""

from collections import defaultdict
from LTVClass import Customer,Site_Visit,Image_Upload,Order


def Ingest(e,D):
    for item in e:
        if item['type']=='CUSTOMER':
            
            key=item['key']
            verb=item['verb']
            event_time=item['event_time']
            last_name=item['last_name']
            adr_city=item['adr_city']
            adr_state=item['adr_state']
            cust_details=Customer(key,verb,event_time,last_name,adr_city,adr_state)
            if key not in D:
                D[key]=defaultdict(list)  
            #Injesting only New Customers and not existing ones as an array due to async input
            D[key]['CUSTOMER'].append(cust_details)
        
        elif item['type']=='SITE_VISIT':
            key=item['key']
            verb=item['verb']
            event_time=item['event_time']
            customer_id=item['customer_id']
            tags=item['tags']
            site_details=Site_Visit(key,verb,event_time,customer_id,tags)
            D[customer_id]['SITE_VISIT'].append(site_details)
            #Injesting Site_Visit
        
        elif item['type']=='IMAGE':
            key=item['key']
            verb=item['verb']
            event_time=item['event_time']
            customer_id=item['customer_id']
            camera_make=item['camera_make']
            camera_model=item['camera_model']
            image_details=Image_Upload(key,verb,event_time,customer_id,camera_make,camera_model)
            D[customer_id]['IMAGE'].append(image_details) 
            #Injesting Image
            
        elif item['type']=='ORDER':
            key=item['key']
            verb=item['verb']
            event_time=item['event_time']
            customer_id=item['customer_id']
            total_amount=item['total_amount']
            order_details=Order(key,verb,event_time,customer_id,total_amount)
            D[customer_id]['ORDER'].append(order_details)
            #Injesting Order
            
        else:
            print ("Wrong Json Input")
            exit(1)
    return (D)
