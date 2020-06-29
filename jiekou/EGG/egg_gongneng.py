#coding=utf-8
'''
Created on 2016年6月30日

@author: quqiao
'''

import StringIO
import urllib
import pycurl


def PostData1(curl, url, data):
    head = ["Accept:*/*"
            ,"User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11"
            ,"Content-Type:application/x-www-form-urlencoded"
            ,"X-AVOSCloud-Application-Id: dcf3uj1qrprt61ltqyhk43v5cs5m7e6xkups9i6ep6nrzg6e"
            ,"X-AVOSCloud-Application-Key: kbvvp733zwghxq3utbd9r5aq48agmpocl58xkvhk2e645f6y"
            ]

    buf = StringIO.StringIO()
    
    curl.setopt(pycurl.SSL_VERIFYPEER, False)
    curl.setopt(pycurl.HTTPHEADER,  head)
    curl.setopt(pycurl.POSTFIELDS,  urllib.urlencode(data))
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.WRITEFUNCTION, buf.write)
    #curl.setopt(pycurl.CUSTOMREQUEST,"POST")
    curl.perform()
    the_page = buf.getvalue() 
    #print the_page
    buf.close()
    return the_page

def PostData2(curl, url, data):
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
    return the_page


if __name__=='__main__':
    c = pycurl.Curl()#创建一个curl对象
    test_url = "http://192.168.1.153/egg-portal/authen/updatePassword.do"
    test_password={"mphone":"17713543052", "password":"123456"} # step1
    PostData1(c,test_url,test_password)

    
    
    
    
        
    
    
    



