#!/usr/bin/env python

#AUTHOR     :   Avi Mehenwal
#DATED      :   12th-nov-2013

import csv
import os

'''
Q)  Consider Share prices for a N number of companies given for each month since year     
         1990 in a CSV file.  Format of the file is as below with first line as header.
 
Year,Month,Company A, Company B,Company C,Company D
1990, Jan, 10, 153, 204, 501
1990, Feb, 20, 150, 220, 502
1990, Mar, 30, 151, 520, 503
1990, Apr, 40, 151, 120, 523
1990, May, 23, 154, 220, 544
2013, Sep, 50, 103, 153, 500
 

a) List for each Company year and month in which the share price was highest.
b) Submit a unit test with sample data to support your solution.   
'''

INPUT_DIR = '/home/avimehenwal/Projects'
filename = 'data.csv'

'''Class to create company instances which will store share,month,year data individually '''
class CompanyName(object):
    '''Class Constructor'''
    
    def __init__(self):
        self.data_dict = {}
        
    '''Inserting records as dictionary in class data_dict attribute
       fORMAT : KEY=(year, month), VALUE=share values'''
    def append_data(self,year,month,value):
        self.data_dict[(year,month)] = value
        return "data appended"
    
    '''returns maximum share value of Companys Instance'''
    def max_sharePrice(self):
        l = self.data_dict.values()
        return max(l)
    
    '''returns minimum share value of Companys Instance'''
    def min_sharePrice(self):
        l = self.data_dict.values()
        return min(l)
    
    '''returns maximum share price entire record from data_dict'''
    def max_sharePrice_record(self):
        v = self.max_sharePrice()
        #getting key from dictionary value from generator functions
        k = [key for key, value in self.data_dict.iteritems() if value==v]
        print k,v
        return k,v
    
    '''returns maximum share price entire record from data_dict'''
    def min_sharePrice_record(self):
        v = self.min_sharePrice()
        k = [key for key, value in self.data_dict.iteritems() if value==v]
        print k,v
        return k,v


#MAIN
with open(os.path.join(INPUT_DIR,filename), 'rb') as infile:
    #Reading and parsing data from csv
    reader = csv.reader(infile)
    line_no = 0
    header_item_no = 0
    data_item_no = 0
    #company_tuple = (A, B, C, D)
    
    
    for row in reader:
        line_no += 1
        if line_no == 1:
            #print "HEADER"
            #On header instantiate from class CompanyName with blank data_dict attribute
            header_item_no = len(row)
            print "Instantiatng Companies as read from HEADER section"
            A = CompanyName()
            B = CompanyName()
            C = CompanyName()
            D = CompanyName()
        else:
            data_item_no = len(row)
            if header_item_no == data_item_no:
                #print "No of Items in record checked -- No Blanks"
                #print "DATA"
                #Appending year,month and share value to company objects using class method
                #populating Company Instances with share,value and month data
                A.append_data(row[0].strip(),row[1].strip(),row[2].strip())
                B.append_data(row[0].strip(),row[1].strip(),row[3].strip())
                C.append_data(row[0].strip(),row[1].strip(),row[4].strip())
                D.append_data(row[0].strip(),row[1].strip(),row[5].strip())
            else:
                print "Number of items in data dont match that of header"


#Querying Instances for Required Information
print "Company A's complete data",A.data_dict
print "Company A max_sharePrice",A.max_sharePrice()
print "Company A max_sharePrice_record",A.max_sharePrice_record()
print "Company A min_sharePrice",A.min_sharePrice()
print "Company A min_sharePrice_record",A.min_sharePrice_record()

print "Company B's complete data",B.data_dict
print "Company B max_sharePrice",B.max_sharePrice()
print "Company B max_sharePrice_record",B.max_sharePrice_record()
print "Company B min_sharePrice",B.min_sharePrice()
print "Company B min_sharePrice_record",B.min_sharePrice_record()

print "Company C's complete data",C.data_dict
print "Company C max_sharePrice",C.max_sharePrice()
print "Company C max_sharePrice_record",C.max_sharePrice_record()
print "Company C min_sharePrice",C.min_sharePrice()
print "Company C min_sharePrice_record",C.min_sharePrice_record()

print "Company D's complete data",D.data_dict
print "Company D max_sharePrice",D.max_sharePrice()
print "Company D max_sharePrice_record",D.max_sharePrice_record()
print "Company D min_sharePrice",D.min_sharePrice()
print "Company D min_sharePrice_record",D.min_sharePrice_record()
