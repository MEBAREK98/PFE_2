# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:21:32 2018

@author: pc
"""
import scholarly,re,urllib.request,nltk
import bs4 as bs,codecs
import DBConnection
def load_file(name): return codecs.open(name, "r", "utf-8").read()

def save_file(name,text):
    file = codecs.open(name, "w", "utf-8")
    file.write(text)
    file.close()

def find_researcher_names(file_to_save_names):
    max_pages=40
    latters=list("abcdefghijklmnopqrstvwxyz")
    found_names=[]
    for lettre in latters:
        for nbr in range(1,max_pages+1,1):
            try:
                names_in_page=[]
                page=urllib.request.urlopen('http://www.usthb.dz/spip.php?article538&x='+str(nbr)+'&xx='+lettre).read()
                print("Done reading page",nbr,"for the names starting with",lettre)
                soup=bs.BeautifulSoup(page,'lxml')
                for p in soup.find_all('a'):
                    names_in_page.extend([name for name in re.findall(lettre.upper()+".*\\xa0.*",p.text) if len(list(name))<40])
                if (len(names_in_page)==0):
                    print("Done reading names for letter",lettre)
                    print("The total nbr of names is ",len(found_names))
                    break
                else: found_names.extend(names_in_page)
            except ValueError:
                print("Done reading names for letter",lettre)
                print("The total nbr of names is ",len(found_names))
                break
    save_file(file_to_save_names,"\n".join(found_names))

def getAuthorInfos(author_name):
    search_query = scholarly.search_author(author_name)
    author = next(search_query).fill()

    print("Name:",author.name) 
    print("Affiliation:",author.affiliation)
    print("Email:",author.email)
    print("Interests",author.interests)
    print("H_index:",author.hindex)
    print("Number of citations:",author.citedby)
    DBConnection.insert_info('inforet',author.name,author.name,author.email,author.affiliation,author.hindex,author.citeby,author.interests)
    print("List of publications:")
    for i,pub in enumerate(author.publications):
        if "year" in pub.bib and "title" in pub.bib:
            print(i+1,pub.bib["title"],pub.bib["year"])
#insert author informations into the database

# find_researcher_names("USTHB_names.txt")
getAuthorInfos("Mohamed Hadj Ameur")