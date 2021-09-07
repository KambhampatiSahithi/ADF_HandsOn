'''
import pandas as pd

dt = pd.read_csv("student.csv")
print(dt)
dictionary = dict()
print(dictionary)
// using below methods we get single row as one dictionary with key as header in csv.
from csv import DictReader

fl = open("student.csv","r")
reader = DictReader(fl)
dt = dict()
for row in reader:
    print(row)
'''
# here we get header in csv file as key in dictionary and values of that header as list in the dictionary
from csv import DictReader

try:
    fl = open("student.csv","r")
    reader = DictReader(fl)
    dt = dict()
    for row in reader:
        for k,v in row.items():
            if k in dt:
                st = " "
                dt[k] += (st+v)
            else:
                dt[k] = v
    for k,v in dt.items():
        dt[k] = list(v.split())
    print(dt)
except:
    print("Error")