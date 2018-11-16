# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:37:24 2018

@author: pc
"""

#liste[0]
import scholarly 
search_query = scholarly.search_author("ahmed guessoum")
print(next(search_query))