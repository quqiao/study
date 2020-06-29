#coding=utf-8
'''
Created on 2016年5月5日

@author: quqiao
'''

import math

for i in range(10000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if(x*x==i+100)and(y*y==i+268):
        print i
    