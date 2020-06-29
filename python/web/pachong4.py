#coding=utf-8
'''
Created on 2016年6月8日

@author: quqiao
COOKIE的使用
'''

import urllib2
import cookielib
import urllib


'''
#获取Cookie保存到变量

#声明一个CookieJar对象实例来保存cookie
cookie=cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener=urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response=opener.open("http://www.baidu.com")
for item in cookie:
    print 'Name='+item.name
    print 'Value='+item.value
'''

'''
#保存Cookie到文件

#设置保存cookie的文件，同级目录下的cookie.txt
filename="cookie.txt"
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie=cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener=urllib2.build_opener(handler)
#创建一个请求，原理同urllib2的urlopen
response=opener.open("http://www.baidu.com")
#保存cookie到文件
cookie.save(ignore_discard=True,ignore_expires=True)
'''

'''
#从文件中获取Cookie并访问

#创建MozillaCookieJar实例对象
cookie=cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
request=urllib2.Request("http://www.baidu.com")
#利用urllib2的build_opener方法创建一个opener
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response=opener.open(request)
print response.read()
'''

#利用cookie模拟网站登录

filename='cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie=cookielib.MozillaCookieJar(filename)
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata=urllib.urlencode({'login':'sha.lin@ck-telecom.com','password':'678abc123'})
#登录testin系统
loginUrl='http://www.testin.cn/site/login'
#模拟登录，并把cookie保存到变量
result=opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，
gradeUrl='http://www.testin.cn/site/login'
#请求访问成绩查询网址
result=opener.open(gradeUrl)
print result.read()


