#coding=utf-8
'''
Created on 2016年7月27日

@author: quqiao
'''

import encrypt
import StringIO
import urllib
import pycurl                                                                                                                                                                                                                                                                                 
import demjson
#import thread
import threading
import time
#import sys
#import base64







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

#deskey = ''
#encrypt.setEnv(1)
token  ="72465872a0ff482784a8985615792f4f"
test_url1 = "http://test.passport.maifangma.com/login"
test_url3 = "http://test.platforms.maifangma.com/user/modifymoney"
test_data1= "version=1.0.0&deviceNo=72465872a0ff482784a8985615792f4f&deviceType=2&cityId=51010000&data={\"account\":\"18008062016\",\"password\":\"111111\",\"type\":\"2\"}"
test_data2= "version=1.0.0&deviceNo=72465872a0ff482784a8985615792f4f&deviceType=2&cityId=51010000}"
c = pycurl.Curl()
encrypt.initSdk(token)
deskey=encrypt.getToken()

#test_url2="http://192.168.10.115:8084/house/get"
signature=encrypt.signature(test_data1, deskey)

#encrypt.initSdk(token)
#deskey=encrypt.getToken()
#test_data2= "version=1.0.0&deviceNo=72465872a0ff482784a8985615792f4f&deviceType=2&cityId=51010000&ticketId=dict1.get('ticketId')"


    #deskey = ''
    #token  ="72465872a0ff482784a8985615792f4f"
    #encrypt.initSdk(token)
    #deskey=encrypt.getToken()
    #test_url2="http://192.168.10.115:8084/house/get"
    #test_url1 = "http://test.passport.maifangma.com/login"
    #test_data1= "version=1.0.0&deviceNo=72465872a0ff482784a8985615792f4f&deviceType=2&cityId=51010000&data={\"account\":\"admin\",\"password\":\"123456\",\"type\":\"1\"}"
   
    #signature=encrypt.signature(test_data1, deskey)
strencrypt= encrypt.encrypt("{\"account\":\"1800806216\",\"password\":\"111111\",\"type\":\"2\"}",deskey)
data1={"sign":signature,
               "version":"1.0.0",
               "deviceNo":"72465872a0ff482784a8985615792f4f",
               "deviceType":"2",
               "cityId":"51010000" , 
               "data": strencrypt}
    #print "%f" %time.time()
    #sys.stdout.write(str(time.time()))
print "%s" %PostData(c, test_url1, data1)
data2=demjson.decode(PostData(c,test_url1,data1))
data3=data2.get('data')
dencryptData = encrypt.dencrypt(data3,deskey)
dict1=eval(dencryptData)
print dict1

signature2=encrypt.signature(test_data2, deskey)
    
def modifymoney():
    #print "登录:",dencryptData

    c=pycurl.Curl()
    data4={"sign":signature2,
            "version":"1.0.0",
            "deviceNo":"72465872a0ff482784a8985615792f4f",
            "deviceType":"2",
            "cityId":"51010000" , 
            "ticketId": dict1.get('ticketId')}
    print "%f" %time.time()
    print "%s" %PostData(c, test_url3, data4)
    #sys.stdout.write(str(time.time()))
    #print "%s: %s,%s" % ( threadName, time.ctime(time.time()), PostData(c, test_url1, data1))
    #time =time.ctime(time.time())
    #res =  PostData(c, test_url1, data1)
    #log = str(threadName)+' ' + res + ' ' + time
    
   
    #sys.stdout.flush()
    

    


threads = []
t1 = threading.Thread(target=modifymoney)
threads.append(t1)
t2 = threading.Thread(target=modifymoney)
threads.append(t2)
if __name__=='__main__':

    for t in threads:
        #t.setDaemon(True)
        t.start()

    #print "all over %s" %PostData(c, test_url1, data1)
    
        
    
    
    
