# Shutterfly

Performing Simple Life Time Value for top Customers of Shutterfly

Please run the code from src Directory 

Steps to start the script -
1. cd src
2. python Main_Calculation.py X 
   
   where X - Top X customer


Description of the Code:

1.Python is used to calulate LTV, which will run from command line. This requires two command line arguments 
a.Top X Customer which should be > 0 
b.File which has Events of Customers

2.There are four python snippets
a.Main_Calucation.py - This is the Main code which starts all the below methods.
b.LTV_Ingest.py - This snippet is used to Injest messages
c.LTV_Calulate.py – This snippet is used for giving out LTV for top X customers.
d.LTV_Classes.py – This is a class snippet which has attributes.


Assumptions: 
1.A Week is Monday to Sunday.
2.Say, Number of Customers input in X for the LTV_Calulate is more than the exisiting customers in the file, then all customers would be shown 
3.Event time in the CUSTOMER event is Begin time
4.Each Event has a Customer


Design methodology:


1.All event details from the input are stored in a Python's Class then subseqently into a dictionary
2.There are two functions:
a.	Ingest(e, D):
This Function takes "e" which are events in the file and loads everything to D which is a dictionary. This method is implemented in LTV_Ingest.py file.
b.	topXSimpleLTVCustomers(x,D)
This function used D Dictonary from Ingest and goes through all the customers and calculates the LTV value and prints the top X Customer Id and their corresponding LTV value.
 
Error Handling Mechanisims:
1.   NaN is handled during counting of number of visits.
2.   If the argument value for top X customer is negative then meaningful message will be displayed and it will exit the program.
3.   If the number of argument passed is less than expected, then meaningful message will be displayed and it will exit the program.

Current Performance:
Python's Dictinoraies are like Hash tables and thus each Function  would run in O(N) time.


Performance Improvements:
We could have an intermediatory persistant storage instead of dictinoraies if data ingestion becomes too huge. A NoSQL (Document based like MongoDB) implementation as intermediate storage which is well suited for JSON/Python Dictinory constructs.
IO errors and input value errors can be caught before injestion	

