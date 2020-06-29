#coding=utf-8
'''
Created on 2016年6月22日

@author: quqiao
'''

import StringIO
import urllib
import pycurl



            

def GetDate(curl, url):
    head = ['Accept:*/*'
            ,'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11'
            ,"X-LC-Session:"
            ]
    buf = StringIO.StringIO()
    curl.setopt(pycurl.WRITEFUNCTION, buf.write)
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.HTTPHEADER,  head)
    curl.perform()
    the_page =buf.getvalue()
    buf.close()
    return the_page

def PostData(curl,url,data):
    head = ["Accept:*/*"
            ,"User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11"
            ,'Accept:*/*' 
            ,'Content-Type:application/x-www-form-urlencoded',  
            ]
    
    buf = StringIO.StringIO()  #字符串的缓存
    
    curl.setopt(pycurl.SSL_VERIFYPEER,False)
    curl.setopt(pycurl.HTTPHEADER,head)  #设置http的包头信息
    curl.setopt(pycurl.POSTFIELDS,urllib.urlencode(data))#设置post过去的数据，注意是一个字典样式的字符串
    curl.setopt(pycurl.URL,url)#设置url
    curl.setopt(pycurl.WRITEFUNCTION,buf.write)#将返回的内容定向buf缓冲中
    curl.setopt(pycurl.CUSTOMREQUEST,"POST")#设置封装方法，有put，post，get，delete等多种方法
    curl.perform()#执行curl命令
    the_page=buf.getvalue()#返回对象buf中的所有数据
    buf.close()#关闭缓存
    return the_page
    
    
if __name__=='__main__':
    c = pycurl.Curl()#创建一个curl对象
    test_url1 = "http://manager.maifangma.com/house/search"
    test_data1 = {"houseName":"珠江青云台"}
    
    test_url2="http://manager.maifangma.com/house/getalbum"
    test_data2={"houseId":"600001"}
    
    test_url3="http://passport.maifangma.com/login"
    test_data3={"sign":"","version":"1.0.0","deviceNo":"DESKTOP-A34KG0E","deviceType":"2","cityId":"51010000","account":"18008062016","password":"123456","type":"2"}
    

    #print "楼盘管理：",PostData(c,test_url1,test_data1)
    #print "获取相册：",PostData(c,test_url2,test_data2)
    print "登陆：",GetDate(c, test_url3)
    pass
    
    
    
    
    
    
    
    
    