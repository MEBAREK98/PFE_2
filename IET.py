# -*- coding: utf-8 -*-
"""
Created on Sat May  5 23:15:25 2018

@author: pc
"""
import csv
def publication_IET_lecture_step1():     
    p=[]
    with open('IET.csv', newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
         for row in spamreader:
             r=row[0].split('  ')
             p.append(r[0].upper())
    return p

def publication_IET_lecture_step2():
    x=publication_IET_lecture_step1()
    p=[]
    for i in x:
        pos=i.find(',')
        p.append(i[:pos])
        p.append(i[pos+1:pos+9])
    return p

    
##########################################################################


#liste SCOPUS



##########################################################################
def publication_SCOPUS_lecture_step1():
    p=[]
    with open('SCOPUS.csv', newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
         for row in spamreader:
             r=row[0].split('  ')
             p.append(r[0].upper())
    return p

def publication_SCOPUS_lecture_step2():
    y=publication_SCOPUS_lecture_step1()
    p2=[]
    for i in y:
        l=i.split(',')
        p2.append(l)
    return p2

def trouver_scopus(pub):
    p=publication_SCOPUS_lecture_step2()
    s=0
    liste=[]
    for elt in p:
        taille=len(elt)
        i=0
        while i<taille:
            if pub==elt[i]:
                s=1
                liste=elt
            i=i+1
    return liste,s

##########################################################################


#liste WOS



##########################################################################
def publication_wos_lecture():     
    p=[]
    with open('WOS.csv', newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    
         for row in spamreader:  
             p1=[]
             chaine=row[0]
             l=chaine.split('  ')
             for i in l:
                 if i!='':
                     p1.append(i.upper())
             p.append(p1)
    return p
def trouver_wos(pub):
    p=publication_wos_lecture()
    s=0
    liste=[]
    for elt in p:
        taille=len(elt)
        i=0
        while i<taille:
            if pub==elt[i]:
                s=1
                liste=elt
            i=i+1
    return liste,s
