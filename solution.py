#!/bin/usr/python

import csv

CSV_FILE = 'company_data.csv'

with open(CSV_FILE, 'r') as F:
    items = csv.reader(F) # read per line with iterator
    for index, item in enumerate(items):
        print index, item, type(item)

# Fetching a specific line
FH = open(CSV_FILE, 'r')
print '+++++++++++++++++++'
for i, line in enumerate(FH):
    if i == 2:
        print i, line
        break
print 'File Closed'
FH.close()

class FileOperations:

    def __init__(self, f):
        self.file_name = f
        self.F = open(self.file_name, 'r')
        self.G = csv.reader(self.F)

    def get_company_list(self):
        c_list = self.G.next()
        return c_list 

    def get_line(self, no):
        for i, line in enumerate(self.F):
            if i == no:
                return (i, line)

    
if __name__ == '__main__':
    f = FileOperations(CSV_FILE)
    print 'FIRST-ROW', f.get_company_list()
# Iterator state are saved from last next().
    print 'ONE LINE', f.get_line(6)

