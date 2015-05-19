# -*- coding: utf-8 -*- 
__author__ = 'benywon'
from bs4 import BeautifulSoup
with open(u'L:/program/cip/SAT-HISTORY/3月/PYTHONwork/crawler/127550.html') as f:
    html_doc=f.read()
soup = BeautifulSoup(html_doc)


print soup.title

print soup.title.name

print soup.title.string

print soup.p

print soup.a

print soup.find_all('a')

print soup.find(id='link3')

print soup.get_text()