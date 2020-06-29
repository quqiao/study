#coding=utf-8

import urllib
import urllib2


#header
url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
values = {'username' : 'cqc',  'password' : 'XXXX'}
headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)
print data
request = urllib2.Request(url,data,headers)
print request
response = urllib2.urlopen(request)
page = response.read()
print page

#Proxy(代理)的设置

enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

#使用 HTTP 的 PUT 和 DELETE 方法
request = urllib2.Request(url,data=data)
request.get_method = lambda:'PUT'
response = urllib2.urlopen(request)