# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 15:06:13 2018

@author: pc
"""
import urllib.request,scholarly
import bs4 as bs
from selenium import webdriver
def comfirmation_ieee(pub):
    driver = webdriver.PhantomJS()
    driver.set_window_size(1120, 550)
    driver.get("https://www.ieee.org/")
    driver.find_element_by_id('q').send_keys(pub)
    driver.find_element_by_id("searchSubmitButton").click()
    url=driver.current_url
#    driver.get(url)
    print(url)
#    assert "Suggestions: " in driver.page_source
#    print("ça marche pas")
#    driver.quit()
    page=urllib.request.urlopen(url).read()
    soup=bs.BeautifulSoup(page,'lxml')
    for p in soup.find_all('p'):
        print(p.text)
#        print("ça boucle")
#        print(p.text)
#        if re.search("Sorry, there were no results for your search query. Search again!",p.text):print("ça marche")
    
#Methode pour avoire l'url 
#    driver.get("https://duckduckgo.com/")
#    driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
#    driver.find_element_by_id("search_button_homepage").click()
#    print (driver.current_url)
#    driver.quit()
comfirmation_ieee("ABABOU NOUREDDINE")



def publication_autheur(nom):
    search_query = scholarly.search_author(nom)
    author = next(search_query).fill()
    for i,pub in enumerate(author.publications):
                print(i+1,pub.bib["title"])
                
#publication_autheur("ahmed guessoum")                