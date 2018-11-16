# -*- coding: utf-8 -*-
"""
Created on Sat May  5 00:47:10 2018

@author: pc
"""

import bs4 as bs
from selenium import webdriver

def springer_search(author,pub):
    s=4
    browser = webdriver.PhantomJS()
    browser.set_window_size(1120, 550)
    browser.get('https://link.springer.com/advanced-search')
    browser.find_element_by_name('title-is').send_keys(pub)
    browser.find_element_by_name('author-is').send_keys(author)
    browser.find_element_by_id('submit-advanced-search').click()
    code_source=browser.page_source
    soup=bs.BeautifulSoup(code_source,'lxml')
    for p in soup.find_all('strong'):
        if p.text=='0': s=0
    return s