# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:20:38 2018

@author: pc
"""
import scholarly
def information(pub):
    
    search_query = scholarly.search_pubs_query(pub)
    p=next(search_query)
    print(p.bib["author"])
    return p.bib["author"]
#information("TOWARDS SEAMLESS TRACKING-FREE WEB: IMPROVED DETECTION OF TRACKERS VIA ONE-CLASS LEARNING")