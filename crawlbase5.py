# -*- coding: utf-8 -*- 
__author__ = 'benywon'
import urllib2
from bs4 import BeautifulSoup

fs=open("./wrong.txt","a")
for i in range(999999,10000000):
    # url='http://www.dianping.com/shop/'+str(i)
    url='http://www.tripadvisor.com/Restaurant_Review-g294212-d4256072-Reviews-Pinotage_Sanlitun-Beijing.html'
    try:
        req = urllib2.Request(url)
        req.add_header("User-agent","Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/57.36 (KHTML, like Gecko) Chrome/27.0.1453.110 Safari/537.36 CoolNovo/2.0.9.20")
        response = urllib2.urlopen(req,timeout=2)
        the_page = response.read()
        soup = BeautifulSoup(the_page)
        sorry=soup.find_all('div', class_='errorMessage')
        if len(sorry)>0:
            continue
        print(i)
        with open(u'L:/program/cip/SAT-HISTORY/3月/PYTHONwork/crawler/'+str(i)+'.html','w') as f:
            f.write(the_page)
        with open('./log.txt','w') as f1:
            f1.write(str(i))
    except Exception,e:
        print(e.__unicode__())
        fs.write(str(e.__unicode__())+"\n")
        fs.flush()
        continue
fs.close()
print the_page
