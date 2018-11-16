# -*- coding: utf-8 -*-
"""
Created on Thu May 10 20:42:37 2018

@author: pc
"""
from DBConnection import select_chercheur_nom,select_chercheur_id
from DBConnection2 import select_ID_chercheur,select_ISSN_publicationscientifique,\
select_article_revu_revu_ID,select_revue_scientifique_revue_id_WOS,\
select_revue_scientifique_revue_id_SCOPUS,select_revue_scientifique_revue_id_IET

import scholarly
def getAuthor_nobmbre_de_publication_scholar(author_name):
    search_query = scholarly.search_author(author_name)
    author = next(search_query).fill()
    try:
        s=author.citedby
    except:
        s=0
    for i,pub in enumerate(author.publications): pass
    return i+1,author.hindex,s

def getAuthor_nobmbre_de_publication_wos(author_name):
    c=0
    author_id=select_ID_chercheur("metricoscience",author_name)
    issn=select_ISSN_publicationscientifique("metricoscience",author_id)
    for i in issn:
        rows=i[0]
        if rows!="":
            p=select_article_revu_revu_ID("metricoscience",rows)
            s=select_revue_scientifique_revue_id_WOS("metricoscience", p[0][0])
            if s!=None : c=c+1
    return c   
#print(getAuthor_nobmbre_de_publication_wos("Abdelkader Hadidi"))
def getAuthor_nobmbre_de_publication_IET(author_name):
    c=0
    author_id=select_ID_chercheur("metricoscience",author_name)
    issn=select_ISSN_publicationscientifique("metricoscience",author_id)
    for i in issn:
        rows=i[0]
        if rows!="":
            p=select_article_revu_revu_ID("metricoscience",rows)
            s=select_revue_scientifique_revue_id_IET("metricoscience", p[0][0])
            if s!=None : c=c+1
    return c
#print(getAuthor_nobmbre_de_publication_IET("Abdelkader Hadidi"))
def getAuthor_nobmbre_de_publication_scopus(author_name):
    c=0
    author_id=select_ID_chercheur("metricoscience",author_name)
    issn=select_ISSN_publicationscientifique("metricoscience",author_id)
    for i in issn:
        rows=i[0]
        if rows!="":
            p=select_article_revu_revu_ID("metricoscience",rows)
            s=select_revue_scientifique_revue_id_SCOPUS("metricoscience", p[0][0])
            if s!=None : c=c+1
    return c
#print(getAuthor_nobmbre_de_publication_scopus("Abdelkader Hadidi"))



def productiviter_chercheur(datab):
    p1=select_chercheur_nom("metricoscience")
    for i in p1:
        print(getAuthor_nobmbre_de_publication_scholar(i))
#print(productiviter_chercheur("metricoscience"))