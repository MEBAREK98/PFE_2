# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 20:38:19 2018

@author: pc
"""
import scholarly,urllib.request
import bs4 as bs
from DBConnection import insert_info
#import csv
def chercheur_algerien(url_deb1,nb):
    page=urllib.request.urlopen(url_deb1).read()
    soup=bs.BeautifulSoup(page,'lxml')
    c=0
    for i,p in enumerate(soup.find_all('p')):
        c=c+1
        print(c,i,p.text)
        try:
            search_query = scholarly.search_author(p.text)
            author = next(search_query).fill()
            insert_info("amira4", author.name, "", author.citedby, author.hindex)
        except AttributeError:
            insert_info("amira4", author.name, "", 0, author.hindex)
        except StopIteration:
                insert_info("amira4", p.text, "", 0, 0)
    if nb<=4720 :
        nb=nb+10
        url_deb1=url_deb1[:45]+str(nb)
        chercheur_algerien(url_deb1,nb)
url_deb1="http://www.dgrsdt.dz/Fr/Scholar_DZ.php?debut=4400"
chercheur_algerien(url_deb1,nb=4400)        
