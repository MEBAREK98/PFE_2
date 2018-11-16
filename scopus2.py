# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 22:11:41 2018

@author: pc
"""

from newspaper import Article

url = 'https://www.scopus.com/authid/detail.uri?authorId=35934255800'
article = Article(url)
article.download()
article.parse()
#print(article.html)
#print(help(open()))
fichier=open("text.txt","w")
fichier.write(article.html)
fichier.close()