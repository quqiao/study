#coding=utf-8
'''
Created on 2016年6月21日

@author: quqiao
'''


import StringIO
import urllib
import pycurl


def PostData1(curl, url,data):
    head = ["Accept:*/*"
            ,"User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11"
            ,'Accept:*/*',  
                'Content-Type:application/x-www-form-urlencoded',  
                'render:json',  
                'clientType:json',  
                'Accept-Charset:GBK,utf-8;q=0.7,*;q=0.3',  
                'Accept-Encoding:gzip,deflate,sdch',  
                'Accept-Language:zh-CN,zh;q=0.8',  
            ]

    buf = StringIO.StringIO()
    
    curl.setopt(pycurl.SSL_VERIFYPEER, False)
    curl.setopt(pycurl.HTTPHEADER,  head)
    curl.setopt(pycurl.POSTFIELDS,  urllib.urlencode(data))
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.WRITEFUNCTION, buf.write)
    curl.setopt(pycurl.CUSTOMREQUEST,"POST")
    curl.perform()
    the_page = buf.getvalue() 
    #print the_page
    buf.close()
    return the_page

'''def PostData2(curl, url, data):
    head = ["Accept:*/*"
            ,"User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11"
            ,"Content-Type:application/x-www-form-urlencoded"
            ,"X-LC-Session:d4t6bbjuh1s9chcfqc9jzm9wp"
            ,"X-AVOSCloud-Application-Id: dcf3uj1qrprt61ltqyhk43v5cs5m7e6xkups9i6ep6nrzg6e"
            ,"X-AVOSCloud-Application-Key: kbvvp733zwghxq3utbd9r5aq48agmpocl58xkvhk2e645f6y"
            ]

    buf = StringIO.StringIO()
    
    curl.setopt(pycurl.SSL_VERIFYPEER, False)
    curl.setopt(pycurl.HTTPHEADER,  head)
    curl.setopt(pycurl.POSTFIELDS,  urllib.urlencode(data))
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.WRITEFUNCTION, buf.write)
    curl.setopt(pycurl.CUSTOMREQUEST,"PUT")
    curl.perform()
    the_page = buf.getvalue()
    #print the_page
    buf.close()
    return the_page'''

if __name__=='__main__':
    c = pycurl.Curl()
    test_url1 = "http://manager.maifangma.com/house/search"
    test_data1 = {"sign":"","version":"1.0.0","deviceNo":"DESKTOP-A34KG0E","deviceType":"2","cityId":"51010000","houseName":"珠江青云台"}
    
    test_url2="http://manager.maifangma.com/house/getalbum"
    test_data2={"sign":"","version":"1.0.0","deviceNo":"DESKTOP-A34KG0E","deviceType":"2","cityId":"51010000","houseId":"600001"}
    
    test_url3="http://manager.maifangma.com/house/get"
    test_data3={"sign":"","version":"1.0.0","deviceNo":"DESKTOP-A34KG0E","deviceType":"2","cityId":"51010000","houseId":"600001","step":"2"}
    
    
    test_url4="http://manager.maifangma.com/house/onoffshelf"
    test_data4={"sign":"","version":"1.0.0","deviceNo":"DESKTOP-A34KG0E","deviceType":"2","cityId":"51010000","houseId":"600001","on":"true"}
    
    test_url5="http://manager.maifangma.com/house/list"
    test_data5={"sign":"","version":"1.0.0","deviceNo":"DESKTOP-A34KG0E","deviceType":"2","cityId":"51010000","signedStatus":"0","status":"1"}
    
    #test_url6="http://manager.maifangma.com/house/album"
    #test_data6={"sign":"","version":"1.0.0","deviceNo":"DESKTOP-A34KG0E","deviceType":"2","cityId":"51010000","houseId":"600001","albumInfo":"1"}
    
    
    
    
    
    
    test_url10="http://passport.maifangma.com/login"
    test_data10={"sign":"","version":"1.0.0","deviceNo":"DESKTOP-A34KG0E","deviceType":"2","cityId":"51010000","account":"18008062016","password":"123456","type":"2"}
    
    
    print "楼盘管理：",PostData1(c,test_url1,test_data1)
    print "获取相册：",PostData1(c,test_url2,test_data2)
    print "编辑详情：",PostData1(c,test_url3,test_data3)
    print "上架/下架: ",PostData1(c,test_url4,test_data4)
    print "楼盘列表：",PostData1(c,test_url5,test_data5)
    
    
    
    print "登陆：",PostData1(c, test_url10, test_data10)
    pass
