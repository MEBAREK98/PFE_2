# -*- coding: utf-8 -*-
"""
Created on Sun May  6 07:01:53 2018

@author: pc
"""

chaine = 'aa bb www.free.fr_/a azertyuiop' 
pos1 = chaine.find('www') 
pos2 = chaine.find('/a') 
#extraction sans le '/a' 
sousChaine = chaine[pos1:pos2] 
print (sousChaine )
#extraction avec le '/a' 
pos2=pos2+len('/a') 
sousChaine = chaine[pos1:pos2] 
print (sousChaine )