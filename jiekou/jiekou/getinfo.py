#coding=utf-8
'''
Created on 2016年6月23日

@author: quqiao
'''

import StringIO
import pycurl

c=pycurl.Curl()
str=StringIO.StringIO()
c.setopt(pycurl.URL, "http://www.jb51.net/article/74840.htm")
c.setopt(pycurl.WRITEFUNCTION,str.write)
c.setopt(pycurl.FOLLOWLOCATION, 1)

c.perform()

print str.getvalue()