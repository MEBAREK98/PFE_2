# -*- coding: utf-8 -*-
"""
Created on Sun May  6 07:46:50 2018

@author: pc
"""
'''
import csv
def publication_IET_lecture_step1():     
    p=[]
    with open('Taylor&Francis.csv', newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
         for row in spamreader:
             pos=row[0].find(',')
             print(row[:pos])
             r=row[0].split('  ')
             p.append(r[0].upper())
    return p

p=publication_IET_lecture_step1()
for i in p:
    
    print(i)
    '''
import pandas as pd
da=pd.read_csv('Taylor&Francis.csv',error_bad_lines=False)
print(str(da))