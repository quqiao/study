#coding=utf-8
'''
Created on 2016年6月30日

@author: quqiao
'''

import encrypt
import StringIO
import urllib
import pycurl
import demjson

def PostData(curl,url,data):
    head = ["Accept:*/*"
            ,"User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (sKHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11"
            ,'Accept:*/*' 
            ,'Content-Type:application/x-www-form-urlencoded',  
            
            ]
    
    buf = StringIO.StringIO()  
    curl.setopt(pycurl.SSL_VERIFYPEER,False)
    curl.setopt(pycurl.HTTPHEADER,head)  
    curl.setopt(pycurl.POSTFIELDS,urllib.urlencode(data))
    curl.setopt(pycurl.WRITEFUNCTION,buf.write)
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.CUSTOMREQUEST,"POST")
    curl.perform()
    the_page=buf.getvalue()
    buf.close()
    return the_page


if __name__=='__main__':
    token ="72465872a0ff482784a8985615792f4f"
    c = pycurl.Curl()
    test_url1 = "http://test.passport.maifangma.com/login"  #需要请求的API接口的URL
    test_data1="version=1.0.0&deviceNo=72465872a0ff482784a8985615792f4f&deviceType=2&cityId=51010000&data={\"account\":\"admin\",\"password\":\"123456\",\"type\":\"1\"}"#用于加密的公共参数和输入参数
    encrypt.initSdk(token)#初始化sdk
    deskey=encrypt.getToken()
    signature=encrypt.signature(test_data1, deskey)#获取签名
    strencrypt= encrypt.encrypt("{\"account\":\"admin\",\"password\":\"123456\",\"type\":\"1\"}",deskey)#加密请求参数
    data1={"sign":signature,
           "version":"1.0.0",
           "deviceNo":"72465872a0ff482784a8985615792f4f",
           "deviceType":"2","cityId":"51010000" , 
           "data": strencrypt}                #用于请求的公共参数和请求参数
    print "登录：",PostData(c, test_url1, data1) #
    data2=demjson.decode(PostData(c,test_url1,data1))#json格式转换为Python对象
    data3=data2.get('data')#获取data的value
    dencryptData = encrypt.dencrypt(data3,deskey)#解密
    print dencryptData
    
    
    
    
    
        
    
    
    
