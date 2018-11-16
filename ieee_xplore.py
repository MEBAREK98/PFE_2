# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 11:33:44 2018

@author: pc
"""


import scholarly,urllib.request
import bs4 as bs
#donne les titre des publication d'un autheur
def publication_information_1(pub):
    p=[]
    search_query = scholarly.search_author(pub)
    author = next(search_query).fill()
    for i,pub in enumerate(author.publications):
        if "year" in pub.bib and "title" in pub.bib:
            print(i+1,pub.bib["title"])
            p.append(pub.bib["title"])
    return p
#publication_information("ahmed guessoum")   
#donne la structure d'une publication sur scholar    
def publication_information_2(pub):
    publication={}
    try:
        search_query_1 = scholarly.search_pubs_query(pub)
        publication = next(search_query_1).fill()
        print(publication)
    except:
        print(publication)
liste=publication_information_1("ahmed guessoum")
for i in liste:
    publication_information_2(i)