# -*- coding: utf-8 -*-
"""
Created on Fri May  4 21:35:03 2018

@author: pc
"""
import re
import urllib.request
import bs4 as bs
def search_dblp(pub):
    s=3
    chaine=pub.replace(' ','+') 
    page=urllib.request.urlopen("http://dblp.uni-trier.de/search/publ?q="+chaine).read()
    soup=bs.BeautifulSoup(page,'lxml')
    for p in soup.find_all('em'):
        print(p.text)
        if re.search("no matches",soup.text):   s=0
    return s