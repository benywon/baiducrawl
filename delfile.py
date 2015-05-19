# -*- coding: utf-8 -*- 
__author__ = 'benywon'

from bs4 import BeautifulSoup
import os
for root,dirs,files in os.walk(u'L:\\program\\cip\\SAT-HISTORY\\4月\\baidubaike\\crawler'):
    for filespath in files:
        filespath=os.path.join(root,filespath)
        with open(filespath,'r') as f:
          cc=f.read()
        soup = BeautifulSoup(cc)
        sorry=soup.find_all('p', class_='sorryCont')
        if len(sorry)>0:
            # print cc
            print(filespath)
            os.remove(filespath)


# if os.path.isfile(targetFile):
#     os.remove(targetFile)