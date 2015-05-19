
# -*- coding: utf-8 -*- 
__author__ = 'benywon'
import urllib2
from bs4 import BeautifulSoup



for i in range(1,1000000):
    string=str(i)
    url='http://detail.tmall.com/item.htm?&id='+string
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req,timeout=1)
        the_page = response.read()
        print i
    except Exception,e:
        print e.message
        continue


print the_page
