#coding=utf-8
'''
Created on 2016年6月7日

@author: quqiao
'''


import urllib
import urllib2

url='http://www.testin.cn/site/login'
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
values={'username':'sha.lin@ck-telecom.com','password':'678abc123'}
headers={'User-Agent':user_agent}
data=urllib.urlencode(values)
request=urllib2.Request(url,data,headers)
response=urllib2.urlopen(request)
print response.read()