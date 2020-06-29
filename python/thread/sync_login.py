#coding=utf-8
'''
Created on 2016年6月30日

@author: quqiao
'''

import encrypt
import StringIO
import urllib
import pycurl
#import demjson
#import thread
import threading
import time
import sys
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
token  ="72465872a0ff482784a8985615792f4f"
encrypt.initSdk(token)
deskey=encrypt.getToken()

    #test_url2="http://192.168.10.115:8084/house/get"
test_url1 = "http://test.passport.maifangma.com/login"
test_data1= "version=1.0.0&deviceNo=72465872a0ff482784a8985615792f4f&deviceType=2&cityId=51010000&data={\"account\":\"admin\",\"password\":\"123456\",\"type\":\"1\"}"
signature=encrypt.signature(test_data1, deskey)

def login():
    #deskey = ''
    #token  ="72465872a0ff482784a8985615792f4f"
    #encrypt.initSdk(token)
    #deskey=encrypt.getToken()
    c = pycurl.Curl()
    #test_url2="http://192.168.10.115:8084/house/get"
    #test_url1 = "http://test.passport.maifangma.com/login"
    #test_data1= "version=1.0.0&deviceNo=72465872a0ff482784a8985615792f4f&deviceType=2&cityId=51010000&data={\"account\":\"admin\",\"password\":\"123456\",\"type\":\"1\"}"
   
    #signature=encrypt.signature(test_data1, deskey)
    strencrypt= encrypt.encrypt("{\"account\":\"admin\",\"password\":\"123456\",\"type\":\"1\"}",deskey)
    data1={"sign":signature,
               "version":"1.0.0",
               "deviceNo":"72465872a0ff482784a8985615792f4f",
               "deviceType":"2","cityId":"51010000" , 
               "data": strencrypt}
    print "%f" %time.time()
    #sys.stdout.write(str(time.time()))
    print "%s" %PostData(c, test_url1, data1)
    #sys.stdout.write(str(time.time()))
    #print "%s: %s,%s" % ( threadName, time.ctime(time.time()), PostData(c, test_url1, data1))
    #time =time.ctime(time.time())
    #res =  PostData(c, test_url1, data1)
    #log = str(threadName)+' ' + res + ' ' + time
    
   
    #sys.stdout.flush()


threads = []
t1 = threading.Thread(target=login)
threads.append(t1)
t2 = threading.Thread(target=login)
threads.append(t2)
if __name__=='__main__':

    for t in threads:
        #t.setDaemon(True)
        t.start()

    #print "all over %s" %PostData(c, test_url1, data1)

    
    
    
    
        
    
    
    

    
    
        
    
    
    
