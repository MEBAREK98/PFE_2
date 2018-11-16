# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 23:01:40 2018

@author: pc
"""

import scholarly,re,urllib.request,nltk
import bs4 as bs
# =============================================================================
# #Probléme les derniere conf ne se rajoute pas 
# =============================================================================
def find_ComputerScienceConferences_Workshops_names_DBLP(url_deb):
    page=urllib.request.urlopen(url_deb).read()
    c,soup=0,bs.BeautifulSoup(page,'lxml')
    for p in soup.find_all('a'):
        if c==1 and p.text!="[previous 100 entries]": 
             fichier = open("confs.txt", "a")
             fichier.write("\n"+p.text)  
             fichier.close()
#            print(p.text)
#            s1=p.get("href")
#            if re.search(r"http://dblp.uni-trier.de/db/conf/.",s1): 
#                publication_conf_dblp(s1)
        if p.text=="[next 100 entries]": 
            c,s=1,p.get("href")             
            url_a="http://dblp.uni-trier.de/db/conf/"+s
        if (p.text=="[previous 100 entries]")and(c==1):   find_ComputerScienceConferences_Workshops_names_DBLP(url_a)      

def Timeline_of_conferences(url_deb):
    page=urllib.request.urlopen(url_deb).read()
    soup=bs.BeautifulSoup(page,'lxml')
    last_s=""
    for q in soup.find_all('a'):    
        s=q.get("href")       
        if re.search(r"http://dblp.uni-trier.de/db/conf/.*/.*\.html",s): 
           if last_s!=s:
                fichier = open("Lien_de_toutes_les_conf.txt", "a")
                fichier.write("\n"+s)  
                fichier.close()
                last_s=s
def publication_conf_dblp(url):
    page=urllib.request.urlopen(url).read()
    soup=bs.BeautifulSoup(page,'lxml')
    c=0
    
    for p in soup.find_all('span'):
        x,x1,x2,x3,x4,x5,x6=[],[],[],[],[],[],[]    
        s1=p.get("class")
        try:
            if s1[0]=='title':
                 x6.append(p.text)
        except TypeError:
            pass
        s2=p.get("itemprop")
#        try:
        if s2=="name" and not p.get("class"):
                print(p.text)
                x1.append(p.text)
                print(x1)
        if s2=="publisher":
                x2.append(p.text)
                print(x2)
        if s2=="datePublished":
                 x3.append(p.text)
        if s2=="isbn":
                 x4.append(p.text)
        if s2=="pagination":
                 x5.append(p.text)              
#        except TypeError:
#            pass
        x.append(x1)
        x.append(x2)
        x.append(x3)
        x.append(x4)
        x.append(x5)
        x.append(x6)
    print(x)
    import csv
    c = csv.writer(open("CONFERANCE.csv", "wb"))
    c.writerow(["mebarek","mouloud"])
url_deb='https://dblp.uni-trier.de/db/conf/' 
url_deb2='http://dblp.uni-trier.de/db/conf/3dim/3dimpvt2012.html'  
url_deb3='http://dblp.uni-trier.de/db/conf/3dpvt/'
def matche(names_dblp):
    fichier1=open(names_dblp,"r",encoding='latin-1')
    author=fichier1.read()
    fichier1.close()
    liste_author=author.splitlines()
    print(liste_author)
    fichier2=open("USTHB_names2.txt","r",encoding='utf-8')
    author=fichier2.read()
    fichier2.close()
    liste_author2=author.splitlines()
#    print(liste_author2)
    print(liste_author2[1])
    for i in liste_author:
        for u in liste_author2:
            if i==u:
                print("trouver")
#matche("Organisateur.txt")    
#Timeline_of_conferences(url_deb2)
publication_conf_dblp(url_deb3)
#find_ComputerScienceConferences_Workshops_names_DBLP(url_deb)            