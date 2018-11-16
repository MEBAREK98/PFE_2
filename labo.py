# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:49:06 2018

@author: pc
"""
import urllib.request
import bs4 as bs
from DBConnection import insert_lab,insert_univ,insert_domaine,supr_doublant_domaine
def labo(url_deb1):
    page=urllib.request.urlopen(url_deb1).read()
    soup=bs.BeautifulSoup(page,'lxml')
    s=2
    while s<=1473:
        for i,p in enumerate(soup.find_all('a',attrs={'onclick':"show_notice('"+str(s)+"');"})):
            if i==0: s1=p.text
            if i==1: s2=p.text
            if i==2: s3=p.text
        print(s1,s2)
        insert_lab("metricoscience", s1, s2)
        insert_univ("metricoscience", s2)
        insert_domaine("metricoscience", s, s3)
        s=s+1
url_deb1="http://dalilab.dgrsdt.dz/index.php?option=1&search=1"
labo(url_deb1)
supr_doublant_domaine("metricoscience")
