#coding=utf-8
import urllib2

'''
#URLError
request = urllib2.Request('http://www.baidussssss.com')
try:
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError,e:
    print e.reason 


#HTTPError
req = urllib2.Request('http://www.baidu.com')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError,e:
    print e.reason
    print e.code
'''

#HTTPError的父类是URLError，根据编程经验，父类的异常应当写到子类异常的后面，如果子类捕获不到，那么可以捕获父类的异常
req1 = urllib2.Request('http://www.baidu.com')
try:
    urllib2.urlopen(req1)
except urllib2.HTTPError,e:
    print e.code
    print e.reason
except urllib2.URLError,e:
    print e.reason
else:
    print "OK"
    

#加入 hasattr属性提前对属性进行判断
req2 = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req2)
except urllib2.URLError,e:
    if hasattr(e, 'code'):
        print e.code
except urllib2.HTTPError,e:
    if hasattr(e, 'reason'):
        print e.reason
else:
    print 'OK'