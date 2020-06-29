#coding=utf-8
'''
Created on 2016年11月16日

@author: quqiao
'''


import threading
from urllib2 import URLError
import urllib2
import sys


def test():
    test1=sys.stdout
    test=open('log1.txt','w')
    sys.stdout=test
    for req in range(2):   
        req = urllib2.Request('https://www.baidu.com')
        try:
            urllib2.urlopen(req)
            print "success!"
        except URLError,e:
            print e.code
            print e.read() 
            
    sys.stdout=test1
    test.close()
            
threads = []
for t in range(5):
    t = threading.Thread(target=test)
    threads.append(t)

if __name__=='__main__':
    for t in threads:
        t.start()    