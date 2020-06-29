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
#import base64







def PostData(curl,url,data):
    '''
    head = ["Accept:*/*"
            ,"User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (sKHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11"
            ,'Accept:*/*' 
            ,'Content-Type:application/x-www-form-urlencoded',  
            
            ]
    '''
    
    buf = StringIO.StringIO()  
    
    curl.setopt(pycurl.SSL_VERIFYPEER,False)
    #curl.setopt(pycurl.HTTPHEADER,head)  
    curl.setopt(pycurl.POSTFIELDS,urllib.urlencode(data))
    curl.setopt(pycurl.WRITEFUNCTION,buf.write)
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.CUSTOMREQUEST,"POST")
    curl.perform()
    the_page=buf.getvalue()
    buf.close()
    return the_page


if __name__=='__main__':
    count=0
    while count<10:
        count +=1
        token  ="72465872a0ff482784a8985615792f4f"
        c = pycurl.Curl()
        #test_url2="http://192.168.10.115:8084/house/get"
        test_url1 = "http://test.passport.maifangma.com/login"
        #test_data2=str(test_data1)
        test_data1="version=1.0.0&deviceNo=72465872a0ff482784a8985615792f4f&deviceType=2&cityId=51010000&data={\"account\":\"18008062016\",\"password\":\"111111\",\"type\":\"2\"}"
    #test_data1={"version":"1.0.0","deviceNo":"DESKTOP-A34KG0E","deviceType":"2","cityId":"51010000","data":{"houseId":"748427593056780288","step":"1"}}# step1
    #test = demjson.encode(test_data1);
    #print temp
        encrypt.initSdk(token)
        deskey=encrypt.getToken()
    #print deskey
        signature=encrypt.signature(test_data1, deskey)
    
    #print signature
        strencrypt= encrypt.encrypt("{\"account\":\"18008062016\",\"password\":\"111111\",\"type\":\"2\"}",deskey)
        data1={"sign":signature,"version":"1.0.0","deviceNo":"72465872a0ff482784a8985615792f4f","deviceType":"2","cityId":"51010000" , "data": strencrypt}
        print "登录：",PostData(c, test_url1, data1)
    
        data2=demjson.decode(PostData(c,test_url1,data1))
        data3=data2.get('data')
        dencryptData=encrypt.dencrypt(data3,deskey)
        print dencryptData
    
    #print strencrypt
    #a=base64.b64decode(encrypData)
    #PostData(c,test_url1,a)
    #dencryptData=encrypt.dencrypt(strencrypt,deskey)
    #test=demjson.decode(dencryptData)
    #print test
    #print dencryptData
    #test_data2={"sign":signature,"version":"1.0.0","deviceNo":"DESKTOP-A34KG0E","deviceType":"2","cityId":"51010000","data":{"houseId":"748427593056780288","step":"1"}}
    #print "注册：",PostData(c, test_url1, test_data2)
    
    
    
    
        
    
    
    
