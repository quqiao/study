#coding=utf-8
'''
Created on 2016年6月7日

@author: quqiao
'''

'''
URLError异常处理
'''
'''
import urllib2

request=urllib2.Request('http://www.xswsxxx.com')
try:
    urllib2.urlopen(request)
except urllib2.URLError,e:
    print e.reason
'''   
    
import urllib2 
request1=urllib2.Request('http://www.baidu.com')
try:
    urllib2.urlopen(request1)
except urllib2.HTTPError,e:
    print e.code
except urllib2.URLError,e:
    print e.reason
else:
    print "OK"
