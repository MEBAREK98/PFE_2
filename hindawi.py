# -*- coding: utf-8 -*-
"""
Created on Sun May  6 00:14:46 2018

@author: pc
"""

import urllib.request
import bs4 as bs
def search_hindawi():
    x=[]
    page=urllib.request.urlopen("https://www.hindawi.com/journals/").read()
    soup=bs.BeautifulSoup(page,'lxml')
    for p in soup.find_all('a'):
        x.append(p.text.replace(' ',''))
    return x
