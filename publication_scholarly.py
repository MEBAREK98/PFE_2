# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 22:03:39 2018

@author: pc
"""
import time
from IET import trouver_wos,publication_IET_lecture_step2,trouver_scopus
from hindawi import search_hindawi
from dblp_search import search_dblp
from search_springer import springer_search
import scholarly,urllib.request
from DBConnection import insert_revue_scientifique,select_chercheur_nom,select_chercheur_id,\
insert_publication_scientifique_le_rest_wos,\
select_publisher_ID,insert_dans_publisher,supr_doublant_revue_scientifique,\
select_revue_scientifique_ID,insert_article_revue,supr_doublant_publisher
import bs4 as bs
import re
import csv
s=1
def publication_scholar_ext_nom(url_deb1,nb,s):
    page=urllib.request.urlopen(url_deb1).read()
    soup=bs.BeautifulSoup(page,'lxml')
    for p in soup.find_all('p'):
        print(p.text,s)
        s=s+1
    if nb<=4720 :
        nb=nb+10
        url_deb1=url_deb1[:45]+str(nb)
        publication_scholar_ext_nom(url_deb1,nb,s)
        
#url_deb1="http://www.dgrsdt.dz/Fr/Scholar_DZ.php?debut=0"
#publication_scholar(url_deb1, 0, s)
def publication_autheur(nom):
    p=[]
    search_query = scholarly.search_author(nom)
    author = next(search_query).fill()
    
    for i,pub in enumerate(author.publications):
            if "year" in pub.bib and "title" in pub.bib:
                p.append(pub.bib["title"].upper())
    
    return p,len(p)





def publication_information(pub):
    p=""
    c=0
    dat=""
    publisher=""
    search_query = scholarly.search_pubs_query(pub)
#    try:
    publication = next(search_query).fill()
    
    if re.search(publication.bib["ENTRYTYPE"],"article"):
            try:
                dat=publication.bib["year"]
            except:
                    dat=""
            print(dat)
            try:
                p=publication.bib["journal"]
            except:
                p=""
            print(p)
            try:
                c=publication.citedby
            except:
                    c=0
            print(c)
            try:
                publisher=publication.bib["publisher"]
            except:
                    publisher=0
            print(publisher)

#    except:
#        pass
    return p,c,dat,publisher
#publication_information("A statistical approach for the induction of a grammar of Arabic")


def matching_wos_scopus_IET(author,nb):
#    liste_hindawi=search_hindawi()
    t,nb1=publication_autheur(author)
    
    i=0
    while i<nb1:
        z,c,date,publisher=publication_information(t[i])
        print("*******************************Numéro de la publication :\t",i)
        print("Title of the joural:\t",z)
        liste_wos,s=trouver_wos(z.upper())
        liste_scopus,s1=trouver_scopus(z.upper())
        liste_IET=publication_IET_lecture_step2()
        if s==1 and z!="":
            print("indexed wos")
            #insertion dans revue scientifique impact factor index_id revue_name
            insert_revue_scientifique("metricoscience", c, 1, z.upper())
            
            #supprimer les revue scientifique 
            
            supr_doublant_revue_scientifique("metricoscience")
            
            #retourne l'id de la revue scientifique
            try :
                b=select_revue_scientifique_ID("metricoscience",z.upper())
            except TypeError:
                b=(90000,)
            #t[i]: nom de la revue \ liste_wos[1]: publisher \ b[o]: l'id de la revue
            
            insert_article_revue("metricoscience", t[i], liste_wos[1], date, b[0])
            
            #liste_wos[1]: publisher supprimer les doublant et puis selectionner l'id pour le metre 
            #dans publication scientifique
            
            insert_dans_publisher("metricoscience",liste_wos[1],author_ID)
            supr_doublant_publisher("metricoscience")
            a=select_publisher_ID("metricoscience",liste_wos[1])
            insert_publication_scientifique_le_rest_wos("metricoscience",liste_wos[2],a[0],nb)
           
        elif s1==1 and z!="":
            print("indexed scopus")
            insert_revue_scientifique("metricoscience", c, 2, z.upper())
            
            #supprimer les revue scientifique 
            
            supr_doublant_revue_scientifique("metricoscience")
            
            #retourne l'id de la revue scientifique
            try:
                b=select_revue_scientifique_ID("metricoscience",z.upper())
            except TypeError:
                b=(90000,)
            #t[i]: nom de la revue \ liste_wos[1]: publisher \ b[o]: l'id de la revue
            
            insert_article_revue("metricoscience", t[i], publisher, date, b[0])
            
            #liste_wos[1]: publisher supprimer les doublant et puis selectionner l'id pour le metre 
            #dans publication scientifique
            
            insert_dans_publisher("metricoscience",publisher)
            supr_doublant_publisher("metricoscience")
            a=select_publisher_ID("metricoscience",publisher)
            insert_publication_scientifique_le_rest_wos("metricoscience",liste_scopus[0],a[0],nb)
          
        elif z.upper() in liste_IET and z!="": 
            print("indexed IET inspec")
            issn=liste_IET[liste_IET.index(z.upper())+1]
            
            #c=citeby
            
            insert_revue_scientifique("metricoscience", c, 3, z.upper())
            supr_doublant_revue_scientifique("metricoscience")
            try:
                b=select_revue_scientifique_ID("metricoscience",z.upper())
            except TypeError:
                b=(90000,)
            insert_article_revue("metricoscience", t[i], issn, date, b[0])
            insert_dans_publisher("metricoscience",publisher)
            supr_doublant_publisher("metricoscience")
            a=select_publisher_ID("metricoscience",publisher)
            insert_publication_scientifique_le_rest_wos("metricoscience",issn,a[0],nb)
            
        else:
            print("indexed scholar")
            insert_revue_scientifique("metricoscience", c, 0, z.upper())
            
            #drop
            supr_doublant_revue_scientifique("metricoscience")
            
            try :
                b=select_revue_scientifique_ID("metricoscience",z.upper())
            except TypeError:
                b=(90000,)
            
            #article revue
            try:
                insert_article_revue("metricoscience", t[i], "", date, b[0])
            except TypeError:
                insert_article_revue("metricoscience", t[i], "", date, 90000)
            #insertion dans publisher
            
            
            insert_dans_publisher("metricoscience",publisher)
            supr_doublant_publisher("metricoscience")
            try:
                a=select_publisher_ID("metricoscience",publisher)
                insert_publication_scientifique_le_rest_wos("metricoscience","",a[0],nb)
            except:
                insert_publication_scientifique_le_rest_wos("metricoscience","",90000,nb)
            print(publisher)
            #insertion dans publication scientifique
            
            
        i=i+1
        time.sleep(10)

p1=select_chercheur_nom("metricoscience")
p2=select_chercheur_id("metricoscience")
#print(p1)

j=12
while p1!=None:
    print(j,p1[j],p2[j])
    matching_wos_scopus_IET(p1[j],p2[j])
#    matching_wos_scopus_IET("ahmed guessoum",90)
    print("done!")
    p1.remove(p1[j])
    p2.remove(p2[j])
    j=j+1
    