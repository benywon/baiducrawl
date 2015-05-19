# -*- coding: utf-8 -*- 
__author__ = 'benywon'
import urllib2
from bs4 import BeautifulSoup

with open('./log.txt','r') as r:
	cc=r.readline()
number=int(cc)
fwrong=open('./wrongtext.txt','a')
for i in range(number,10000000):
    url='http://baike.baidu.com/view/'+str(i)+'.htm'
    fwrong.flush()
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req,timeout=2)
        the_page = response.read()
        soup = BeautifulSoup(the_page)
        sorry=soup.find_all('p', class_='sorryCont')
        if len(sorry)>0:
            fwrong.write(str(i)+u'no content\n')
            continue
        print(i)
        with open(u'L:/program/cip/SAT-HISTORY/3月/PYTHONwork/crawler/'+str(i)+'.html','w') as f:
            f.write(the_page)
        with open('./log.txt','w') as f1:
            f1.write(str(i))
    except:
        fwrong.write(str(i)+'其他错误\n')
        continue
fwrong.close()

print the_page
