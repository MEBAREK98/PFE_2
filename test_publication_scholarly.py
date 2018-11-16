# -*- coding: utf-8 -*-
"""
Created on Tue May  8 22:57:08 2018

@author: pc
"""
import scholarly


search_query = scholarly.search_author('ahmed guessoum')
print(next(search_query))


#search_query = scholarly.search_pubs_query('Social Validation of Learning Objects in Online Communities of Practice Using Semantic and Machine Learning Techniques 2013')
#print(next(search_query))