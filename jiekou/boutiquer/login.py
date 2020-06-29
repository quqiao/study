#coding=utf-8
'''
Created on 2016年11月16日

@author: quqiao
'''

import urllib2 
from urllib2 import URLError



for i in range(50000):
    
    req = urllib2.Request('http://admin.boutiquer.net/login.html')
    try:
        urllib2.urlopen(req)
        print "success!"
    except URLError,e:
        print e.code
        print e.read() 
